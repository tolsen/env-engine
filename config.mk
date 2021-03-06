# Populate the Makefile environment with variables and values from all
# .lime-config files found and read by config_engine.py. This environment will
# be inhereited by subprocesses

ENV_ENGINE_DIR ?= .
CONFIG_FILE ?= .lime-config-generated.mk

$(shell python $(ENV_ENGINE_DIR)/config_engine.py make > $(CONFIG_FILE) )

include $(CONFIG_FILE)
