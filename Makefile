w-install:
	python -m venv .dataenv
	call .dataenv\Scripts\activate
	pip install pyinstaller tqdm rapidfuzz
	
install:
	python3 -m venv .dataenv
	source .dataenv/bin/activate
	pip install pyinstaller tqdm rapidfuzz

w-builds:
	pyinstaller --onefile --console --name="search-uri" --icon=icons/myicon.ico --hidden-import=tqdm --version-file="version.txt" main.py
builds:
	pyinstaller --onefile --console --name="search-uri" --hidden-import=tqdm --version-file="version.txt" main.py
	#--icon=icons/myicon.ico

disable:
	deactivate

dev:
	python3 main.py
