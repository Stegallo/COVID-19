docker build -t plot .

docker run -it --rm -v $(pwd)/..:/COVID-19/ -w /COVID-19/docker plot /bin/bash
