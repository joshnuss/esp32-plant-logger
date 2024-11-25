ESP32 Plant Logger
------------------

Logs temperature, humidity and moisture of plant soil using MicroPython.

## Components

- Microcontroller: [ESP-WROOM32 DEVKIT 1](https://embedded-systems-design.github.io/overview-of-the-esp32-devkit-doit-v1)
- Temperature sensor: [DHT20](http://www.aosong.com/userfiles/files/media/Data%20Sheet%20DHT20%20%20A1.pdf)
- Moisture/humidity sensor: [Geekus Soil Sensor](https://abra-electronics.com/sensors/sensors-temperature-en/gk-as-shm-geeekus-soil-moisture-humidity-detection-sensor-module.html)
- Micro SD slot: [3.3V Mini TF](https://abra-electronics.com/robotics-embedded-electronics/breakout-boards/storage/bb-microsd-tf-micro-sd-card-board-3-3v-mini-tf.html)
- Micro SD Card: Any card, formatted to FAT32 without any partitions.

## Pinout

| Component | Pin Name | Pin # |
| -------   | ---      | ----  |
| SD Card   | MISO     | 19    |
| SD Card   | MOSI     | 23    |
| SD Card   | SCK      | 18    |
| SD Card   | CS       | 5     |
| DHT20     | SCL      | 14    |
| DHT20     | SDA      | 13    |
| Moisture  | ADC      | 36    |

## Setup

### Erase flash

```sh
esptool.py --chip esp32 erase_flash
```

### Compile & install micropython firmware

Build micropython locally

```sh
# compile micropython
cd micropython/
make clean
make submodules
make BOARD=ESP32_GENERIC

# write firmware to device
esptool.py --chip esp32 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 4MB --flash_freq 40m 0x1000 build-ESP32_GENERIC/bootloader/bootloader.bin 0x8000 build-ESP32_GENERIC/partition_table/partition-table.bin 0x10000 build-ESP32_GENERIC/micropython.bin
```

### Copy code

Initial RTC clock:

```sh
mpremote rtc --set
```

Copy `*.py` files to device

```sh
mpremote fs cp src/*.py :
```

## License

MIT
