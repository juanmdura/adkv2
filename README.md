# Zubale-ADK

This is a simple base project to spin up AI agents using Google ADK.

Official documentation: [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)

Samples: [https://github.com/google/adk-samples](https://github.com/google/adk-samples) 

## Initial Steps
1.  This project uses [UV Python Manager](https://github.com/astral-sh/uv?tab=readme-ov-file)
    ```bash
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    
    ```bash
    # On Windows.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2. **Install Dependencies:**
    ```bash
    uv sync
    ```

3. **Set Up Environment Variables:** Each agent example relies on a `.env` file for configuration (like API keys, Google Cloud project IDs, and location). This keeps secrets out of the code.

    You will need to create a `.env` file in each agent's directory you wish to run (copy the provided `.env.example`).

## Example Agent

This project includes an example agent with simple logic to be used and run.

### Running the Example Agent

1.  Navigate to the agent's directory:
    ```bash
    cd example_agent
    ```
2.  Create a `.env` file from the example:
    ```bash
    cp .env.example .env
    ```
3.  Update the `.env` file with your specific configurations.
4.  Run the agent:
    ```bash
    cd agents
    uv run adk web
    ```

## 🧱 Repository Structure
```bash
.
├── Zubale-ADK                  # Main repository
│   ├── agents                  # Contains individual agent projects
│   │   ├── agent1              # Specific agent directory
│   │   │   └── README.md       # Agent-specific instructions
│   │   ├── agent2
│   │   │   └── README.md
│   │   ├── ...
│   └── README.md               # This file (Repository overview)
```

## Deployment

Make sure every agent has `requirements.txt` in its path, you can generate from poetry using this command:

```bash
uv pip compile pyproject.toml -o requirements.txt
```