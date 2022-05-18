import os
import sys
import esp_bin2elf
import flash_layout


def main():
    binary, path = os.path.split(sys.argv[1])
    flash = flash_layout.layout_without_ota_updates
    rom = esp_bin2elf.parse_rom(binary, path, flash)
    section_names = esp_bin2elf.name_sections(rom)
    elf = esp_bin2elf.convert_rom_to_elf(rom, section_names, 'flash_bin.elf')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s 'path/to/flashdump.bin'" %sys.argv[0]
        sys.exit(1)
    else:
        main()