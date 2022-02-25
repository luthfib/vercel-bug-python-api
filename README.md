# Requirements to run project

- Node version 16+
- npm i -g pnpm
- python 3.9+
- pipenv (pip3 install pipenv)
- `pipenv --python 3.9` to create env with python 3.9
- If not using vercel to build reqs:
  - `pipenv shell` to enter env
  - Run `pipenv install` if not using vercel to build reqs
  - Run `pipenv shell` to enter the virtualenv

## Setup project frontend

Need to have pnpm installed. Once you have pnpm installed you can run `pnpm install`

## Setup vercel local development

Install vercel `npm i -g vercel`

- Navigate to `http://localhost:3000/api/hello`. Now go to vercel/cache and you should see two werkzeug distributions in the cache which can occasionaly cause import errors
