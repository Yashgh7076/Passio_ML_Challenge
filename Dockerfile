FROM tensorflow/tensorflow

WORKDIR /challenge

COPY . .

CMD ["python" , "passio_challenge.py"]