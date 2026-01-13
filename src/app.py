import streamlit as st
from services.blob_service import upload_to_blob
from ultils.Config import configure_page
import sys
import os

# Adiciona o diretório pai ao sys.path para permitir importações relativas se necessário,
# embora a estrutura atual pareça funcionar bem com execução direta se o PYTHONPATH estiver correto.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def configure_interface():
    configure_page() # Configura a página e carrega variáveis de ambiente
    st.title("Analyze Image for Fraud Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    fileName = None
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_to_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Uploaded Image {fileName}")
            # Mock credit_card_image data for demonstration
            credit_card_image = {
                "card_name": "John Doe",
                "card_number": "1234567812345678",
                "card_type": "Visa",
                "card_expiration_date": "12/25",
                "card_cvv": "123"
            }
            show_image_and_validation_results(blob_url, credit_card_image)
    else:
        st.write("No image uploaded yet. Please upload an image.")

def show_image_and_validation_results(blob_url, credit_card_image):
    st.write("Displaying image and validation results...")
    st.image(blob_url, caption='Uploaded Image', use_column_width=True)
    st.write(credit_card_image)
    if credit_card_image and credit_card_image.get("card_name"):
        st.markdown(f"<h1 style='color: green;'>valid card</h1>", unsafe_allow_html=True)
        st.write(f"Card Name: {credit_card_image['card_name']}")
        st.write(f"Card Number: {credit_card_image['card_number']}")
        st.write(f"Card Type: {credit_card_image['card_type']}")
        st.write(f"Card Expiration Date: {credit_card_image['card_expiration_date']}")
        st.write(f"Card CVV: {credit_card_image['card_cvv']}")
    else:
        st.markdown(f"<h1 style='color: red;'>invalid card</h1>")
        st.write("Could not validate the card details from the image.")

if __name__ == "__main__":
    configure_interface()
