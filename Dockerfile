FROM python:3.6

RUN pip install --upgrade pip
RUN pip install pandas==1.1.5 \
                tabulate==0.8.9 \
                numpy==1.19.5 \
                matplotlib==3.3.4 \
                scikit-learn==0.24.1