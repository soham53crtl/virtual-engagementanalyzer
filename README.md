# Virtual Engagement Analyzer — Streamlit deploy helper

Files added for Streamlit Community Cloud:
- `streamlit_app.py` — minimal Streamlit entrypoint (replace with your app).
- `requirements.txt` — Python dependencies; add any others your app needs.

Run locally
1. python -m venv .venv
2. source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
3. pip install -r requirements.txt
4. streamlit run streamlit_app.py

Create a branch, commit, push, and open a PR (example)
```
git checkout -b add-streamlit-deploy
git add streamlit_app.py requirements.txt README.md
git commit -m "Add minimal Streamlit entrypoint and requirements for deployment"
git push --set-upstream origin add-streamlit-deploy
```

Deploy on Streamlit Community Cloud
1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click "New app".
3. Select your repository `soham53crtl/virtual-engagementanalyzer`, branch `main`, and the file `streamlit_app.py`.
4. Click "Deploy".
5. To add secrets (API keys, DB passwords), open your app dashboard → Manage app → Settings → Secrets and add key=value pairs. Access them via `st.secrets["KEY"]`.

Notes
- If your repo is private and you prefer me to push the branch/PR, either make it public temporarily or grant me repo access. Otherwise copy these files into the repo yourself.
