# Makefile for running the Google Play scraper


.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(QUERY)" ]; then \
		echo 'Error: A query string is required. Use make scrape QUERY="<query>" [CATEGORY="<category>"]'; \
		exit 1; \
	else \
		poetry run python -m google_play_scraper --query="$(QUERY)" $(if $(CATEGORY),--category="$(CATEGORY)"); \
	fi
