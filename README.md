## Pheran Valley – Streamlit Kashmir-Themed App

This is a **Streamlit** web app that shows a Kashmir-themed site for ordering pherans:

- Kashmir gradient background and moodboard
- Gallery of sample pherans
- Order request form with summary
- About & contact info

### 1. Install Python packages

1. Make sure you have **Python 3.9+** installed.
2. Open **PowerShell** and go to the app folder:

```powershell
cd "C:\Users\advpr\Desktop\pheran-valley-streamlit"
```

3. Install the required libraries:

```powershell
pip install -r requirements.txt
```

This will install:

- `streamlit`
- `beautifulsoup4` (included as requested, not required for UI)
- `pillow`

### 2. Run the app locally

From the same folder:

```powershell
streamlit run app.py
```

Streamlit will print a URL like:

```text
Local URL: http://localhost:8501
```

Open that URL in your browser to see the site.

### 3. Push to GitHub

1. Create a repository on GitHub (e.g. `pheran-valley-streamlit`).
2. In PowerShell, in this folder:

```powershell
cd "C:\Users\advpr\Desktop\pheran-valley-streamlit"
git init
git add .
git commit -m "Initial Pheran Valley Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pheran-valley-streamlit.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 4. Optional: Deploy

You can deploy this Streamlit app to:

- Streamlit Community Cloud
- Render
- Railway

by connecting your GitHub repository and choosing `streamlit run app.py` as the start command.


