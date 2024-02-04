# CrtRecon

CrtShExplorer is a Python script for exploring and extracting information from the Certificate Transparency logs provided by crt.sh.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - requests
  - termcolor

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/CrtShExplorer.git
cd CrtShExplorer
```

## Usage

```bash
python3 crtsh_explorer.py <domain> <output_dir>
```

Replace **<domain_name>** with the target domain you want to explore and **<output_dir>** with the desired output directory.

## Output
The script will generate or append to a file named **<domain>**.txt in the specified output directory, containing the extracted information.

## Contributing
Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are welcome!
