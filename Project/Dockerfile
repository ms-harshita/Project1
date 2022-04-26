FROM python:latest
WORKDIR /app
COPY . /app
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install 
RUN aws configure set output json

RUN pip install flask
RUN pip install boto3

EXPOSE 8080

CMD [ "python3", "routes.py" ]