# Bluetooth demo for BrewBlox

This repository is based on the BrewBlox boilerplate, and serves as a proof of concept for bluetooth communication.

## Running

Requires:
* A Docker installation
* An enabled bluetooth dongle / connector

Recommended:
* A bluetooth-capable smartphone

Starting:
```
docker run --net=host --privileged brewblox/bluetooth-demo:develop
```

The simplest way to ensure there is a discoverable device is to enable bluetooth on a smartphone.

Instructions (for Android 8):
* Go to `Settings`
* Go to `Connected devices`
* Enable `Bluetooth` toggle
* Select `Bluetooth`
* select `Pair new device`

Instructions (for iPhone):
* Go to `Settings`
* Go to `Bluetooth`
* Enable `Bluetooth` toggle


Now navigate to [localhost:5000/blueblox/api/doc#!/Bluetooth/bluetooth_discover](localhost:5000/blueblox/api/doc#!/Bluetooth/bluetooth_discover) and click 'Try it out!'.


## Known issues

### Asyncio

The BrewBlox services are written using the `asyncio` framework to allow concurrency without multi-threading. There does not seem to be a simple asyncio library for Bluetooth.

This does not mean it's impossible to integrate the two, but it would require writing an async wrapper around a raw Python socket.

An alternative approach would be to use a separate thread for Bluetooth communication.

### Bluetooth Low Energy

There are two Bluetooth protocols: Bluetooth, and Bluetooth Low Energy (BLE). The current demo only supports Bluetooth devices.

### Accessing Bluetooth from Docker

Docker containers are not inherently granted access to the Bluetooth connector.

The simple solution (used in the demo) is to run the container in privileged mode on the host network. This approach will be an issue if the service is to be integrated with the rest of the BrewBlox services.

### Communication Protocol

Bluetooth itself is little more than a serial transport procotol.
Communication with concrete devices will require implementing their protocol.

## Conclusion

Using Bluetooth certainly seems feasible, but there are a few issues that must be resolved.

There does not seem to be an off-the-shelf library solution, so it is likely that integration involves writing a new asyncio-compatible bluetooth library.
