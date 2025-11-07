env:
	conda env create -f environment.yml 2>/dev/null || conda env update -f environment.yml --prune
clean:
	rm -rf figures/* audio/* _build/*

html:
	myst build --html