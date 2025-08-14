# XV2 Save Checksum & Crypto Tool

A Python CLI tool for decrypting, editing, re-encrypting, and recalculating checksums for Xenoblade Chronicles 2 and Dragon Ball Xenoverse 2 PS4 save files.

---

## 🚀 Usage

Run the tool from the command line with the path to your save file:

```bash
python xv2tool.py /path/to/savefile

    If the save is encrypted, the tool produces a decrypted file with .dec extension.

    If the save is decrypted, the tool recalculates checksums and outputs an encrypted file with .enc extension.

The script automatically detects the save format and handles decryption or encryption accordingly.
📜 Credits

    Zhaxxy – First PS4 save decryption for Xenoblade Chronicles 2.

    ezwizard – Contributions to PS4 save decryption.

    hzhreal/HTOS – HTOS reference implementation.

    alfizari – Python port and patching.

    mineminemine – Checksum logic from Switch version.

    gabrieluto – XV2 PS4 save research & spreadsheet of offsets.
