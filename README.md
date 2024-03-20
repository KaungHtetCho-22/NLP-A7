# NLP-A7
NLP assignments from AIT

**Kaung Htet Cho (st124092)**

## Task1
### Collecting data

- Implemented web crawling through https://ait.ac.th/ but limited to 100 webpages and the datas were converted into pdf

- Prompt-template ==> "Welcome to the AIT Information Chatbot! I'm here to assist you with any questions you have about the Asian Institute of Technology (AIT).Whether you want to know about our academic programs, admissions process, campus facilities, or any other aspect of AIT, feel free to ask!"

- Design the prompt template just like in the lecture's code, context and question remains the same and implemented model (T5) that can provide gentle and informative answers based on the designed template

## Task2
### Unrelated information issue

- T5 model = https://huggingface.co/lmsys/fastchat-t5-3b-v1.0

1. The T5 model produces excellent results despite my training dataset being too small. Thanks to its internal knowledge and pretrained database, it can provide the best answers to all of my questions about AIT.

- gpt2 model = https://huggingface.co/anas-awadalla/gpt2-span-head-few-shot-k-16-finetuned-squad-seed-2

1. Even though I used a fine-tuned GPT-2 model for question answering, the performance suffers due to the limited resources of my dataset. Moreover, choosing a superior model for improved accuracy is challenging because of our restricted GPU capabilities. With access to a better dataset, we could develop a more accurate lightweight model. Additionally, some PCs encounter difficulties with the Langchain packages not functioning properly.

## Task3
### Web development and documentation

- Users can type anything related to AIT and AIT GPT will respond accordingly, similar to ChatGPT. The chain dictionary has been separated into questions, answers, and chat message history. The website can be accessed through localhost:8000.

