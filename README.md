### `hadrian`

#### Features:
- Captures images using the Raspberry Pi camera.
- Sends images to ChatGPT for driving instructions.
- Controls RC car based on ChatGPT's JSON responses.
- Logs metrics and image data to an SQLite database.

#### Requirements:
- Python 3.11
- Dependencies: `openai`, `RPi.GPIO`, `picamera2` 

#### Setup:
1. Clone the repository.
2. Install dependencies:
   ```bash
   poetry install
3. `poetry shell`
4. `./boot.sh`

In reality this is unlikely to work out the box. Config trial and
error inevitable. This deployment worked seamlessly on some RPis, but
not others.
