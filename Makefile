w-install:
	python -m venv .dataenv
	call .dataenv\Scripts\activate
	pip install pyinstaller
	
install:
	python3 -m venv .dataenv
	source .dataenv/bin/activate
	pip install pyinstaller

w-builds:
	pyinstaller --onefile --name="search-uri" --icon=icons/myicon.ico --version-file="version.txt" main.py
builds:
	pyinstaller --onefile --name="search-uri" --version-file="version.txt" main.py
	#--icon=icons/myicon.ico

disable:
	deactivate

dev:
	python3 main.py
