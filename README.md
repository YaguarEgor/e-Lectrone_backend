Для запуска ввести в терминал:

py -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
uvicorn main:app --reload --port 8003
