format:
	isort --multi-line=3 --trailing-comma -force-grid-wrap=0 --use-parentheses --line-width=120 .
	black -S --line-length=120 .
	autopep8 --in-place -r .
	autoflake --in-place -r --remove-unused-variables --remove-all-unused-imports .
