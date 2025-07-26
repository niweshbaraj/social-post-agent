# 🔗 Social Post Generator

Create, optimize, and automatically post AI-generated content (with images) to different social media using LangGraph, LangChain and LangSmith.


## Getting Started

1. Clone repo, install dependencies through following steps.


### Step 1 : Install UV 

For Windows - Powershell (Normal Mode)

```Bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For MacOS & Linux :


```Bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### Step 2 : Created a folder named social-post-agent (optional if repo cloned)


### Step 3 : Initialize UV by following command :


```Bash
uv init
```


### Step 4 : Create a Virtual Environment through UV by following command :


```Bash
uv venv
```


### Step 5 : Activate Virtual Environment :


```Bash
.venv\Scripts\activate  # for windows

source .venv/bin/activate		# Linux/Mac OR
```

### Step 6 : Create a requirements.txt file and add necessary library names into it


### Step 7 : Install dependencies from requirements file :


```Bash
uv add -r requirements.txt
```


### Step 8 (Optional) : Install ipykernel for running Jupyter Notebook in VS Code :


```Bash
uv add ipykernel
```

# Setup Instructions for Developer Accounts and API Credentials

1. X (Twitter) API Setup

    Step 1.1 : Create a X (Twitter) Developer Account

    - Go to Twitter Developer Platform
    - Sign in and apply for a developer account if you don’t have one.
    - Fill in any required information about your intended usage.

    Step 1.2 : Create a Project and App

    - Navigate to Developer Portal > Projects & Apps.
    - Create a new project and app in it.

    Step 1.3 : Configure App Permissions

    - In your app **Settings**, go to **User Authentication Settings** -> click **Set Up**.
    - Under **App permissions**, *select* permission to **Read and write**.
    - Then, under **Type of App**, *select* **Web App, Automated App or Bot**
    - Under **App info**, add **Callback URI / Redirect URL** (even http://localhost/ works for testing) and also add **Website URL** (may give github repo link).
    - Save changes.

    Step 1.4 : Generate API Keys and Tokens

    - Under Keys and Tokens tab, generate and note down:
      - API Key
      - API Secret Key
      - Bearer Token (used for read-only or app-authenticated requests)
      - Access Token
      - Access Token Secret
    - Ensure tokens are regenerated after changing app permissions.

2. Setting Up `.env` File

    Create a `.env` file in your project root directory (social-post-agent/) storing the credentials securely.

    **Example .env template:**

    ```
    # Twitter (X) API credentials
    X_API_KEY=your_twitter_api_key_here
    X_API_SECRET=your_twitter_api_secret_key_here
    X_ACCESS_TOKEN=your_twitter_access_token_here
    X_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret_here
    X_BEARER_TOKEN=your_twitter_bearer_token_here  # optional, for read-only v2 API calls
    ```

    - **Do NOT include quotes (single or double) around the values.**