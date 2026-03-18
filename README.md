# narrator-ai-cli

CLI client for Narrator AI video narration API. Designed for AI Agents and developers.

Two workflow paths for creating AI-narrated videos:

- **Standard**: popular-learning -> generate-writing -> clip-data -> video-composing -> magic-video
- **Fast**: fast-writing -> fast-clip-data -> video-composing -> magic-video

## Installation

### One-line Install

```bash
curl -fsSL https://raw.githubusercontent.com/jieshuo-ai/narrator-ai-cli/main/install.sh | bash
```

This will clone the repo, create a virtualenv, install the CLI, and add it to your PATH.

### Manual Install

Requires Python 3.10+ and pip or uv.

```bash
git clone https://github.com/jieshuo-ai/narrator-ai-cli.git
cd narrator-ai-cli
pip install -e .
```

### Verify

```bash
narrator-ai-cli --version
```

## Quick Start

### 1. Configure

```bash
# Interactive setup
narrator-ai-cli config init

# Or set individually
narrator-ai-cli config set server https://your-api-server.com
narrator-ai-cli config set app_key your_api_key

# Verify
narrator-ai-cli config show
```

### 2. Check Account

```bash
narrator-ai-cli user balance
```

### 3. Create a Narrated Video (Fast Path)

```bash
# Step 1: Pick a narration style template
narrator-ai-cli task narration-styles

# Step 2: Search movie info
narrator-ai-cli task search-movie "飞驰人生" --json

# Step 3: Create narration script
narrator-ai-cli task create fast-writing --json -d '{
  "learning_model_id": "narrator-20250916152104-DYsban",
  "target_mode": "1",
  "playlet_name": "飞驰人生",
  "confirmed_movie_json": { ... },
  "model": "flash"
}'

# Step 4: Poll until done
narrator-ai-cli task query <task_id> --json

# Step 5: Continue with clip-data, video-composing, magic-video...
```

## Command Reference

### Config

| Command | Description |
|---------|-------------|
| `config init` | Interactive setup (server URL + app key) |
| `config show` | Show current config (key masked) |
| `config set <key> <value>` | Set a config value |

### User

| Command | Description |
|---------|-------------|
| `user balance` | Query account balance |
| `user login` | Login with username/password |
| `user keys` | List sub API keys |
| `user create-key` | Create a sub API key |

### Task

| Command | Description |
|---------|-------------|
| `task types` | List task types (`-V` for details) |
| `task create <type> -d '{...}'` | Create a task |
| `task query <task_id>` | Query task status and results |
| `task list` | List tasks with filters |
| `task budget -d '{...}'` | Estimate points consumption |
| `task verify -d '{...}'` | Verify materials before task creation |
| `task search-movie "<name>"` | Search movie info for fast-writing |
| `task narration-styles` | List pre-built narration templates |
| `task templates` | List visual templates for magic-video |
| `task get-writing` | Retrieve generated narration script |
| `task save-writing -d '{...}'` | Save modified narration script |
| `task save-clip -d '{...}'` | Save modified clip data |

**Task Types:**

| Type | Workflow Position |
|------|-------------------|
| `popular-learning` | Standard Path Step 1 |
| `generate-writing` | Standard Path Step 2 |
| `fast-writing` | Fast Path Step 1 |
| `clip-data` | Standard Path Step 3 |
| `fast-clip-data` | Fast Path Step 2 |
| `video-composing` | Step 4 (Standard) / Step 3 (Fast) |
| `magic-video` | Optional final step (visual template) |
| `voice-clone` | Standalone |
| `tts` | Standalone |

### File

| Command | Description |
|---------|-------------|
| `file upload <path>` | Upload file (returns file_id) |
| `file list` | List uploaded files |
| `file info <file_id>` | Get file details |
| `file download <file_id>` | Get presigned download URL |
| `file storage` | Show storage usage |
| `file delete <file_id>` | Delete a file |

## Pre-built Narration Templates

Use these instead of running popular-learning. Pass the `learning_model_id` directly.

| Template | ID | Genre |
|----------|----|-------|
| 热血动作-困兽之斗解说 | `narrator-20250916152104-DYsban` | Action |
| 烧脑悬疑-栽赃陷害解说 | `narrator-20250916152053-nBcHXC` | Suspense |
| 励志成长-师生情谊解说 | `narrator-20250918141539-NnpZlD` | Inspirational |
| 爆笑喜剧-乌龙伪装解说 | `narrator-20250918183013-ktylCA` | Comedy |
| 灾难求生-绝境获救解说 | `narrator-20250919170450-ClVcgT` | Disaster |
| 悬疑惊悚-密室奇案解说 | `narrator-20250915161121-kwwIHs` | Thriller |
| 东方奇谈-都市修仙解说 | `narrator-20250915154420-YVDLiW` | Fantasy |
| 家庭伦理-偷听心声解说 | `narrator-20250915162937-zUrCtQ` | Family |
| 东方奇谈-情蛊拉扯解说 | `narrator-20250919100408-vyXstO` | Fantasy |
| 灾难求生-绝境反杀解说 | `narrator-20250919170037-ARppif` | Disaster |

Full template documentation: https://ceex7z9m67.feishu.cn/wiki/WLPnwBysairenFkZDbicZOfKnbc

## Data Flow

```
                     file upload / file list
                     -> video_file_id, srt_file_id, bgm_id

    Standard Path                          Fast Path
    ─────────────                          ─────────
    popular-learning (optional)            search-movie
    OUT: learning_model_id                 OUT: confirmed_movie_json
      OR use pre-built template                    │
              │                            fast-writing
              ▼                            IN:  learning_model_id + movie_json
    generate-writing                       OUT: task_id, file_ids[0]
    IN:  learning_model_id, episodes                │
    OUT: task_order_num, file_ids[0]       fast-clip-data
              │                            IN:  task_id, file_id, episodes
              ▼                            OUT: task_order_num
    clip-data                                       │
    IN:  order_num, bgm, dubbing                    │
    OUT: file_ids[0]                                │
              │                                     │
              ▼                                     ▼
         video-composing
         IN:  order_num (from writing step), bgm, dubbing
         OUT: task_id, video URLs
                    │
                    ▼
         magic-video (optional)
         IN:  task_id or file_id + template_name
         OUT: rendered video URLs
```

## JSON Output

All commands support `--json` for machine-readable output (recommended for AI agents):

```bash
narrator-ai-cli task list --json
narrator-ai-cli task query <task_id> --json
narrator-ai-cli file list --json
```

Request body can be passed as inline JSON or from a file:

```bash
narrator-ai-cli task create fast-writing -d '{"key": "value"}'
narrator-ai-cli task create fast-writing -d @params.json
```

## Environment Variables

Override config file values:

| Variable | Description |
|----------|-------------|
| `NARRATOR_SERVER` | API server URL |
| `NARRATOR_APP_KEY` | API key |
| `NARRATOR_TIMEOUT` | Request timeout in seconds (default: 30) |

## Project Structure

```
src/narrator_ai/
├── cli.py              # Main entry point
├── client.py           # HTTP client (httpx + SSE)
├── config.py           # Config management (~/.narrator-ai/config.yaml)
├── output.py           # Output formatting (JSON / Rich table)
├── commands/
│   ├── config_cmd.py   # config init/show/set
│   ├── user.py         # balance/login/keys
│   ├── task.py         # task workflow commands
│   └── file.py         # file upload/download/list
└── models/
    └── responses.py    # API response code constants
```

## For AI Agents

See [SKILL.md](SKILL.md) for a comprehensive machine-readable guide including:
- Complete data flow mappings (which output feeds into which input)
- Full parameter references for each task type
- Step-by-step workflow examples with exact commands
- Error handling guidance
