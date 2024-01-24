import string

import fitz  # PyMuPDF
from PIL import Image
import io
import os


def extract_images_with_keyword_names(pdf_path, image_folder="dataimage", target_size=(1000, 1000), name_limit=50):

    text_file = open("image.txt", "a")


    genai.configure(api_key='AIzaSyA8Jn6cFDCoaH6TNLyvOQvKck7fXxJkrNg')
    model = genai.GenerativeModel('gemini-pro')

    os.makedirs(image_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        images = page.get_images(full=True)
        text = page.get_text("text")

        # Use Gemini to generate keywords from text
        keywords_response = model.generate_content("Extract keywords from this text" + text)
        keywords = keywords_response.text.strip().split()  # Extract keywords from the response
        keywords_str = "_".join(keywords[:5])  # Limit to 5 keywords and join with underscores

        i = 0

        for img_index, img_info in enumerate(images):
            img_index += 1
            img_index_str = f"{page_num + 1}_{img_index}"
            img = doc.extract_image(img_info[0])
            img_bytes = img["image"]

            pil_img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
            pil_img = pil_img.resize(target_size)

            # Use keywords and index as the image name, ensuring length limit
            image_name = sanitize_filename(keywords_str[:name_limit])+ str(i) + ".png"  # Truncate if needed

            text_file.write(image_name+"\n")

            i+=1


            img_filename = os.path.join(image_folder, image_name)
            pil_img.save(img_filename)

            print(f"Image {img_index_str} extracted, resized, and saved as {img_filename}")

    text_file.close()

    doc.close()


def sanitize_filename(text):
    filename = text.replace(" ", "_").replace('-', '').replace('/', '')  # Replace spaces with underscores
    return filename


if __name__ == "__main__":
    pdf_path = '/Users/shankarlohar/Github/AssemblyAlly/mychatbot/data/guide_1.pdf'
    extract_images_with_keyword_names(pdf_path)

