
# PayToView

A medium-like web application in which a user pays for a membership after viewing three free posts.

![Screencast from 2023-01-17 20-47-35](https://user-images.githubusercontent.com/63336944/212935042-c509f822-fb4a-48fb-9758-002dfb5a2c07.gif)

## Configuration
### Settings.py
**Stripe:** Add necessary stripe keys (Secret Key, Webhook Key)

```python
MAX_FREE_POSTS: the number of free posts a user can read before having to pay (default = 3)
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/sulavmhrzn/pay-to-view
```

Go to the project directory

```bash
  cd pay-to-view
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Migrate database

```bash
  py manage.py migrate
```

Start the server

```bash
  py manage.py runserver
```

Start stripe webhook

```bash
stripe listen --forward-to localhost:8000/payment/webhook/
```


## Tech Stack

**Server:** Python, Django

**Payment:** Stripe

**PDF:** Weasyprint

