Для запуска ввести в терминал:

py -m venv venv (только в первый раз)

.\venv\Scripts\activate

pip install -r .\requirements.txt (только в первый раз)

uvicorn main:app --reload --port 8003
