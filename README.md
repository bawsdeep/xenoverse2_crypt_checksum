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
```

## 📜 Credits & Acknowledgements

Big thanks to the following people and projects whose work made this tool possible:

- **[Zhaxxy](https://github.com/Zhaxxy/xenoverse2_ps4_decrypt)** – First PS4 save decryption for Xenoverse 2 and creator of ezwizard.  
- **[ezwizard](https://github.com/Zhaxxy/eZwizard3-bot)** – Free PS4 save decryption tool by Zhaxxy.
- **[hzhreal/HTOS](https://github.com/hzhreal/HTOS)** – Free PS4 save decryption tool.
- **[alfizari](https://github.com/alfizari)** – Python porting and patching work.  
- **[mineminemine](https://github.com/mineminemine)** – Checksum logic from the Switch version of the tool.  
- **gabrieluto** – Extensive research on Xenoverse 2 PS4 saves and detailed spreadsheet of offsets.


