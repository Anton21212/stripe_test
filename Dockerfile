FROM  python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/anton/python-project/stripe_test

COPY req /home/anton/python-project/stripe_test/req.txt
RUN pip install -r /home/anton/python-project/stripe_test/req.txt


COPY . /home/anton/python-project/stripe_test

EXPOSE 8000
CMD ["python","manage.py","migrate"]