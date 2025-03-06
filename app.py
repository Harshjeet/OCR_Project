import streamlit as st 
from PIL import Image
from ocr import extract_text_function

LANGUAGES = {
    "Afrikaans": "af", "Arabic": "ar", "Assamese": "as", "Azerbaijani": "az",
    "Belarusian": "be", "Bulgarian": "bg", "Bhojpuri": "bho", "Bengali": "bn",
    "Bosnian": "bs", "Simplified Chinese": "ch_sim", "Traditional Chinese": "ch_tra",
    "Czech": "cs", "Welsh": "cy", "Danish": "da", "German": "de",
    "English": "en", "Spanish": "es", "Estonian": "et", "Persian (Farsi)": "fa",
    "French": "fr", "Hindi": "hi", "Croatian": "hr", "Hungarian": "hu",
    "Indonesian": "id", "Italian": "it", "Japanese": "ja", "Kannada": "kn",
    "Korean": "ko", "Kurdish": "ku", "Latin": "la", "Lithuanian": "lt",
    "Latvian": "lv", "Maithili": "mai", "Mongolian": "mn", "Marathi": "mr",
    "Malay": "ms", "Nepali": "ne", "Dutch": "nl", "Norwegian": "no",
    "Polish": "pl", "Portuguese": "pt", "Romanian": "ro", "Russian": "ru",
    "Serbian (Cyrillic)": "rs_cyrillic", "Serbian (Latin)": "rs_latin", "Slovak": "sk",
    "Slovenian": "sl", "Albanian": "sq", "Swedish": "sv", "Swahili": "sw",
    "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr",
    "Ukrainian": "uk", "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi"
}

#title of the app
st.title("OCR Web application")
st.write("Upload the image (should be in hindi or english)")


# creating the file uploader
upload_image = st.file_uploader("choose an image...", type =["jpg","png", "jpeg"])

selected_language = st.selectbox("Select the image language: ",options=list(LANGUAGES.keys()))

if st.button("convert"):
    if upload_image is not None:
        column1, column2 = st.columns([1,1])
        # open the uploaded image
        image = Image.open(upload_image)
        
        with column1:
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        #Extract text
        extracted_text = extract_text_function(image,LANGUAGES[selected_language])
        
        with column2:
            #Display extracted text
            st.write("Extracted Text: ")
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50; 
                    padding: 10px; 
                    border-radius: 10px;
                    background-color: #f4f4f4;
                    max-height: 300px; 
                    overflow-y: auto;">
                    {extracted_text}
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            #Keyword Search functionalities
            search_keyword = st.text_input("Enter a keyword to search: ")
            
            if search_keyword:
                if search_keyword in extracted_text:
                    # Highlight the search keyword
                    highlighted_text = extracted_text.replace(
                        search_keyword, f'<span style="color:red;">{search_keyword}</span>'
                    )
                    st.write("### search Results: ")
                    st.markdown(
                        f"""
                        <div style="
                            border: 2px solid #FF5733; 
                            padding: 10px; 
                            border-radius: 10px;
                            background-color: #fff3e6;
                            max-height: 200px; 
                            overflow-y: auto;">
                            {highlighted_text}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.write(f'no such keyword:{search_keyword}')
else:
    st.warning("load the image first!")