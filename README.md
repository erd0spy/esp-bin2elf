# esp-bin2elf

Updated version of esp-bin2elf.

------------------------------------------------------------------------------------------------------------------------------

Converts a flash dump from an esp8266 device into an ELF executable file for analysis and reverse engineering.

esp-bin2elf will create sections for each of the sections in the flash dump.  For convenience, esp-bin2elf also creates a flash section at 0x40200000 (**.irom0.text**) containing the SDK from flash, a section at 0x40000000 containing the bootrom (**.bootrom.text**), and includes all SDK symbols.

Tested in IDA Pro with the excellent [Xtensa processor plugin](https://github.com/themadinventor/ida-xtensa) from Fredrik Ahlberg.

Once you have your ELF loaded, you can + should leverage the [rizzo IDA plugin](https://github.com/devttys0/ida) to identify common functions from the SDK and RTOS examples.

------------------------------------------------------------------------------------------------------------------------------

Tested in Ghidra with the excellent [Tensilica Xtensa module for Ghidra](https://github.com/yath/ghidra-xtensa) from Sebastian Schmidt.

## Installation:

```
$ git clone https://github.com/erd0spy/esp-bin2elf
$ cd esp-bin2elf/
$ git clone https://github.com/erd0spy/elffile2
$ cd elffile2/
$ pip2 install -r requirements.txt
$ python2 setup.py install --user
$ cd ..
$ pip2 install -r requirements.txt
```

## Usage:

```bash
$ python2 bin2elf.py ./flash_dump.bin
```

Then run `readelf -a flash_bin.elf` and make sure things look ok.

## Feedback and issues:

Feel free to report an issue on github or contact me privately if you prefer.

## Thanks:

* Richard Burton for image format details: http://richard.burtons.org/2015/05/17/esp8266-boot-process/
* Max Filippov (**jcmvbkbc**) for bootrom.bin: https://github.com/jcmvbkbc/esp-elf-rom
* Fredrik Ahlberg (**themadinventor**) for the IDA plugin and esptool.

------------------------------------------------------------------------------------------------------------------------------

* Joel Sandin (**jsandin**) for the esp-bin2elf: https://github.com/jsandin/esp-bin2elf
* Sebastian Schmidt (**yath**) for the Tensilica Xtensa module for Ghidra: https://github.com/yath/ghidra-xtensa