FROM brewblox/brewblox-service:rpi-latest

RUN apt-get update && apt-get install -y bluez libbluetooth-dev

RUN mkdir -p /pkg
COPY ./pkg/* /pkg/

EXPOSE 5000

RUN pip3 install /pkg/* || true \
    && pip3 install bluetooth-demo \
    && pip3 show bluetooth-demo

ENTRYPOINT ["python3", "-m", "blueblox_demo"]
