docker build -t plot .

docker run -it -v $(pwd)/..:/COVID-19/ -p 8000:8000 plot /bin/bash

cd COVID-19/docker

python plot.py