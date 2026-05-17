# DJI Decryptor

A research-focused tool for decrypting and analyzing DJI flight log data.

## ⚠️ Disclaimer

This tool is developed for **forensic analysis, research, and educational purposes only**. It is intended for authorized security research and legitimate forensic investigations. Ensure compliance with all applicable laws and regulations in your jurisdiction before use.

## 📖 Overview

DJI Decryptor is an exploratory project focused on analyzing encrypted flight logs from DJI drones. It includes reverse-engineering components for understanding binary structures and encryption schemes used in DJI flight data.

## 🔬 Research Focus

- **Binary Structure Analysis** — Understanding DJI flight log file formats
- **Encryption Schemes** — Reverse-engineering cryptographic methods
- **Data Recovery** — Extracting flight information from encrypted logs
- **Forensic Analysis** — Supporting UAV forensic investigations
- **Academic Research** — Contributing to cybersecurity and UAV security knowledge

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| Cryptography | PyCryptodome, cryptography library |
| Binary Parsing | struct, binascii |
| Analysis | NumPy, Pandas |

## 📁 Project Structure

```
DecryptorDJI/
├── src/
│   ├── decryptor.py       # Core decryption logic
│   ├── parsers/
│   │   ├── binary_parser.py
│   │   └── flight_log_parser.py
│   └── utils/
│       └── crypto_utils.py
├── tests/
├── data/
│   └── sample_logs/       # Sample encrypted logs (for testing)
├── docs/
│   └── research_notes.md
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Required libraries:
  ```bash
  pip install pycryptodome
  ```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kshitiz464/DecryptorDJI.git
cd DecryptorDJI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Review the research documentation:
```bash
cat docs/research_notes.md
```

## 💡 Key Concepts

### Encryption Analysis
The project focuses on understanding:
- DJI's proprietary encryption algorithms
- Flight log structure and encoding
- Key derivation methods
- Integrity verification schemes

### Usage Scenarios
- 🔬 Academic research on drone security
- 🛡️ Authorized forensic analysis
- 🔍 Security vulnerability research
- 📊 Flight data analysis for authorized investigations

## ⚙️ Core Modules

### Decryptor
Main decryption engine for processing DJI flight logs:
```python
from src.decryptor import DJIDecryptor

decryptor = DJIDecryptor()
decrypted_data = decryptor.decrypt_log("flight_log.encrypted")
```

### Binary Parser
Utilities for parsing binary flight log structures:
```python
from src.parsers.binary_parser import BinaryParser

parser = BinaryParser(decrypted_data)
flight_info = parser.extract_flight_info()
```

## 📊 Supported Analysis

- Flight duration and distance
- GPS coordinates and altitude
- Speed and acceleration metrics
- Gimbal/camera orientation
- Battery and signal information
- Error codes and warnings

## 🔐 Security & Compliance

- **Use Only for Authorized Purposes** — Comply with CFAA and similar laws
- **Respect Privacy** — Only analyze logs from devices you own or have permission to analyze
- **Document Findings** — Maintain clear audit trails for forensic investigations
- **Responsible Disclosure** — Report security findings to DJI through proper channels

## 📚 Research References

This project is related to work on:
- UAV security and forensics
- Binary reverse engineering
- Cryptographic analysis
- Drone flight log structures

## 🤝 Contributing

This is a research-focused project. Contributions related to:
- Binary format documentation
- Encryption scheme analysis
- New parsing capabilities
- Test cases and validation

are welcome through pull requests.

## 📝 License

This project is available for research and educational purposes.

## ⚖️ Legal Notice

Users are solely responsible for ensuring their use of this tool complies with all applicable laws and regulations. The authors assume no liability for misuse.

---

**Made by** [Kshitiz Yadav](https://github.com/kshitiz464)

*For academic research and authorized forensic analysis only.*
