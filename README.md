quick setup script:

```bash
python3 -m venv .venv
source .venv/bin/activate
touch requirements.txt
pip install jupyter pandas lets_plot palmerpenguins
pip freeze > requirements.txt
```