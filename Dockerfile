FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --root-user-action=ignore -r requirements.txt

COPY app.py ./
COPY *.sav ./

CMD [ "python", "./app.py" ]