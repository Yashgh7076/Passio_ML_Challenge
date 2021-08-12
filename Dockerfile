FROM tensorflow/tensorflow

WORKDIR /model

COPY . .

CMD ["python" , "passio_challenge.py"]
