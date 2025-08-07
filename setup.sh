#!/bin/bash

# This script is run by Streamlit during deployment.

# Find the path to the installed en_core_web_sm model
MODEL_PATH=$(python -c "import en_core_web_sm; print(en_core_web_sm.__path__[0])")

# Create a symbolic link named 'en_core_web_sm' in the root directory
# that points to the actual model path.
ln -s "${MODEL_PATH}" en_core_web_sm