
# Brute-Force Password Cracker

!()[https://scontent.fdac178-1.fna.fbcdn.net/v/t39.30808-6/474455319_604970755472342_4043078737732248162_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=aa7b47&_nc_eui2=AeG-oarKbPHpM-7zx4_OHoGVzSfWx37fgafNJ9bHft-Bpz1pljkkV4gRgQsfXmSsO5M7GIXInb8qf3A6v945ddFp&_nc_ohc=LoIorcrlYvYQ7kNvgHu7Q4_&_nc_zt=23&_nc_ht=scontent.fdac178-1.fna&_nc_gid=Au9-XeVG9kEXDiQP1PObB9V&oh=00_AYAeIVr2qNeMc4pWe5vmBIyItJwrl9GjNpIfruGUC5kWCg&oe=6795B047]

This Python script demonstrates a brute-force password attack by generating all possible combinations of a given set of characters. It attempts to match a target password and provides progress updates during the process.

## Features

- Generates all possible character combinations up to the length of the target password.
- Tracks and displays the number of attempts.
- Returns the password when found or notifies if the password isn't found after all attempts.

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/SagarBiswas-MultiHAT/brute-force-password-cracker.git
```

Navigate to the project directory:

```bash
cd brute-force-password-cracker
```

## Usage

1. Open the `script.py` file and set your desired `target_password` and `allowed_characters`.
2. Run the script:
   ```bash
   python script.py
   ```

## Example

Here's a breakdown of how the script calculates the number of combinations:

```python
characters = "abc"
target_password = "abc"
```

For each length:
- Length 1: 3 ** 1 = 3 (e.g., "a", "b", "c")
- Length 2: 3 ** 2 = 9 (e.g., "aa", "ab", "ac", ..., "cc")
- Length 3: 3 ** 3 = 27 (e.g., "aaa", "aab", ..., "ccc")

Total combinations to try: 3 + 9 + 27 = 39.

