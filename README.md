
# ENGLISH

# MyFirstChatbotinEN
My BlenderBot English chatbot using Transformers

# BlenderBot Chatbot (Transformers)

This project is a command-line chatbot powered by Facebook's BlenderBot model via Hugging Face Transformers.

## Features

- Interactive conversation with a pre-trained conversational AI
- Maintains conversation history for context-aware responses
- Uses `facebook/blenderbot-400M-distill` model
- Prevents token overflow using `truncation=True`

## Technologies Used

- Python 3
- Hugging Face Transformers
- PyTorch
- BlenderBot 400M distilled model

## Project Structure

- `chatbot.py`: Main application file
- `notes.txt`: Optional notes or test inputs
- `.gitignore`: Excludes virtual environment and cache files

## How to Run

1. Clone the repo or download the files.
2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   pip install transformers torch

# ***********************
# TURKISH 

# MyFirstChatbotinEN
My BlenderBot English chatbot using Transformers
#  BlenderBot Chatbot (Transformers)

Bu proje, Hugging Face Transformers kütüphanesini kullanarak BlenderBot 400M modeline dayalı bir sohbet botu uygulamasıdır.

## Özellikler

- Kullanıcıyla etkileşimli sohbet
- Geçmiş konuşmaları hafızada tutar
- `facebook/blenderbot-400M-distill` modeliyle çalışır
- Maksimum token sınırını aşmamak için otomatik kırpma (`truncation=True`)

## Kullanılan Teknolojiler

- Python 3
- Hugging Face Transformers
- PyTorch
- BlenderBot 400M modeli

## Dosya Yapısı

- `chatbot.py` – Ana uygulama kodu
- `notes.txt` – Notlar ve test verileri (isteğe bağlı)
- `.gitignore` – Sanal ortam gibi gereksiz dosyaları hariç tutar

## Kullanım

Terminalde şu şekilde çalıştırılır:

```bash
python chatbot.py



