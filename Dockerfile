FROM tensorflow/tensorflow

COPY . .

RUN mkdir /model

CMD ["python" , "passio_ml_challenge.py"]