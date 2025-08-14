#!/bin/bash
cd "$(dirname "$0")"
. set_env.prod.sh
. venv/bin/activate
python3 send_msg.py