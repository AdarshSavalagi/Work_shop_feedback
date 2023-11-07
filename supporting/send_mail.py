from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO

def create(certificate_path, text):
    certificate = Image.open(certificate_path)
    certificate.convert('RGB')  # for PNG, uncomment this
    draw = ImageDraw.Draw(certificate)
    text_color = (227, 178, 32)  
    font_size = 70
    font = ImageFont.truetype('supporting/RobotoSlab-SemiBold.ttf', font_size)
    W, H = 2000, 1555  
    w, h = font.getbbox(str.title(text))[:-2]
    draw.text(((W - w) / 2, (H - h) / 2), str.title(text), font=font, fill=text_color)
    output_buffer = BytesIO()
    certificate.save(output_buffer, format="jpeg")  # You can change the format if needed

    # Get the bytes from the buffer
    image_bytes = output_buffer.getvalue()

    return image_bytes
# Usage example


if __name__ == '__main__':
    create('supporting\icriis.png', ["B V Muhammed Adil Ahmed Rafeeque ",
                                                                                 ],
           'modified_certificate.png')
    # sender_email = 'envision.sitmng@gmail.com'
    # sender_password = 'gspzbhhdmhppizjo'
    # receiver_email = 'adarshsavaligi@gmail.com'
    # subject = 'Here is your certificate'
    # image_path = 'C:/Users/AIML/Desktop/Conference/modified_certificate.png'
    # send_image_email(receiver_email, image_path)
