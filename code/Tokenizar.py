import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import re

# Configurar lematizador y stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Función para limpiar y lematizar el texto
def preprocess_text(text:str) -> str:
    '''
    Preprocesa una cadena de texto utilizando técnicas de procesamiento de lenguaje natural.
    
    Parameters:
    ----------
    text (str):
        El texto a procesar. Se espera que no sea nulo y que contenga caracteres de texto.
    
    Return (str): 
    ----------
        Una cadena de texto limpia y procesada, compuesta por palabras relevantes lematizadas y en minúsculas.
    '''
    # Eliminar caracteres no alfabeticos
    text = re.sub("[^a-zA-Z]"," ",str(text))
    # Reemplaza múltiples espacios
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenizar el texto
    tokens = word_tokenize(text)
    
    # Etiquetar las palabras
    tag_tokens = pos_tag(tokens)
    # Filtrar nombres propios (NNP, NNPS)
    tokens = [word for word, tag in tag_tokens if tag not in ['NNP', 'NNPS']]
    # Convertir el resto del texto a minúsculas
    tokens = [word.lower() for word in tokens]
    
    # Eliminar stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lematizar las palabras
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return ' '.join(tokens)