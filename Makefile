## -----------------------------------------------------------------------
## This Makefile contains a targets for test framework installation, development and running.
## Available targets listed below:
## -----------------------------------------------------------------------

# Versions
PYTHON_MINIMAL_VERSION = 3.8

# Paths
CUR_PATH = $(shell pwd)
ALLURE_RESULTS_PATH = $(CUR_PATH)/allure-results
ALLURE_GENERATED_REPORT_PATH = $(CUR_PATH)/allure-report
VIRTUAL_ENV ?= $(CUR_PATH)/.venv
VENV_ACTIVATE = $(VIRTUAL_ENV)/bin/activate

# Check Python
PYTHON_MINIMAL_MAIN_VERSION = $(shell echo $(PYTHON_MINIMAL_VERSION) | cut -f1 -d.)
PYTHON_MINIMAL_MAJ_VERSION = $(shell echo $(PYTHON_MINIMAL_VERSION) | cut -f2 -d.)
PYTHON_CUR_VERSION = $(strip $(shell python3 -V 2>&1 | grep -Po '(?<=Python )(.+)'))
PYTHON_CUR_MAIN_VERSION = $(shell echo $(PYTHON_CUR_VERSION) | cut -f1 -d.)
PYTHON_CUR_MAJ_VERSION = $(shell echo $(PYTHON_CUR_VERSION) | cut -f2 -d.)
CHECK_PYTHON_VERSION := $(shell [ $(PYTHON_CUR_MAIN_VERSION) -ge $(PYTHON_MINIMAL_MAIN_VERSION) -a $(PYTHON_CUR_MAJ_VERSION) -ge $(PYTHON_MINIMAL_MAJ_VERSION) ] && echo true)

# Other
SHELL = /bin/bash

# Update PATH to work via virtual environment
export PATH := $(VIRTUAL_ENV)/bin:$(PATH)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Help
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Check if virtual environment exist
$(VENV_ACTIVATE):
ifeq ($(CHECK_PYTHON_VERSION), )
	$(error [ERROR] Python$(PYTHON_MINIMAL_VERSION) or higher expected!)
endif
	python3 -m venv $(VIRTUAL_ENV)

## help                 : Show this message
help: Makefile
	@sed -n 's/^##//p' $<

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Targets
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## install                   : Install requirements
install: $(VENV_ACTIVATE)
	@echo Instalation start
	python3 -m venv $(VIRTUAL_ENV)  &&\
	pip install poetry  &&\
	poetry config virtualenvs.create false  &&\
	poetry install  &&\
	playwright install


## test                      : Run pytest
test:
	pytest tests --alluredir=$(ALLURE_RESULTS_PATH) -p no:cacheprovider

## generate-allure-report    : Generate and open HTML allure report in GoogleChrome
generate-allure-report:
	mkdir -p $(ALLURE_GENERATED_REPORT_PATH)
	if [ -d $(ALLURE_GENERATED_REPORT_PATH)/history ]; then cp -r $(ALLURE_GENERATED_REPORT_PATH)/history $(ALLURE_GENERATED_REPORT_PATH); fi
	allure generate $(ALLURE_RESULTS_PATH) --report-dir $(ALLURE_GENERATED_REPORT_PATH)/html

## allure-report             : Open allure report
.PHONY: allure-report
allure-report:
	google-chrome --disable-web-security --user-data-dir="$(ALLURE_GENERATED_REPORT_PATH)/chrome_files" $(ALLURE_GENERATED_REPORT_PATH)/html/index.html

## black                     : Style code with Black
black:
	cd $(CUR_PATH) && black . --line-length 120


## black-diff                : Show code style diff with colored diff
black-diff:
	cd $(CUR_PATH) && black . --line-length 120 --diff --color

## -----------------------------------------------------------------------
