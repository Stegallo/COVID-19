docker build -t plot .

docker run -it --rm -v $(pwd)/..:/COVID-19/ plot /bin/bash

cd COVID-19/docker

python plot.py
