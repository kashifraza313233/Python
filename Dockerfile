FROM python:3.12

WORKDIR /app/

COPY . /app/

CMD [ "python","Strings.py" ]

# CMD [ "python","StudentResult.py" ]
# CMD [ "python","Cal.py" ]