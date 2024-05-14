# FastAPI + Dash Sample App
This is a sample application that integrates a Dash app within a FastAPI webserver, providing a seamless combination of Python web frameworks. TailwindCSS has been integrated for enhanced styling.

## Quickstart

1. Install Dependencies
```bash
pip install
```
2. Run Webserver:
```bash
make rund
make runj
```
3. Load up in browser: http://localhost:9000

## TailwindCSS

I've added it via npm because most people recommended cli over cdn and that v4 is going to be fast and efficient enough to handle it, so bear with it.
* Added an ability to customize ui with `https://www.shadcn-svelte.com/themes`.
* Copy your preferred design and paste it to `tailwind.pcss` to make changes.

Why did I do it? Apparently `https://plotly.com/dash/design-kit/` is going to cost you over 50 grands per year, yes, that's right! so here take it for free.

## Debug

Hold Shift + Tab to see docstrings

---

PRs from Data Scientists and Frontend Developers are welcomed for better UI and cleaner Jupyter Lab/Notebooks experience 
