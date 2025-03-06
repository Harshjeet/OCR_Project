import easyocr
from PIL import Image 
import numpy as np 



def extract_text_function(image, language_code):
    
    # we will convert image to numpy array
    image_np = np.array(image)
    
    # first load the easyocr lib (it support english + hindi for now)
    reader = easyocr.Reader([language_code])
    
    # performing the ocr (detail=0 indicates it will only return text )
    extract_results = reader.readtext(image_np, detail=0)
    
    # join all the extracted text 
    join_extracted_text = "\n".join(extract_results)
    
    return join_extracted_text
    
    
    
    
    

