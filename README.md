# CrtRecon

CrtRecon is a Python script for exploring and extracting information from the Certificate Transparency logs provided by `crt.sh` specifically the alternative names inside the certifications.

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
sudo mv ./CrtRecon /usr/bin
```

## Usage

```bash
CrtRecon <domain> <output_dir>
```

Replace **<domain_name>** with the target domain you want to explore and **<output_dir>** with the desired output directory.

## Output

The script will generate or append to a file named **<domain_name>**.txt in the specified output directory, containing the extracted information.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are welcome!
