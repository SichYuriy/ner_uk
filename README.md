#Project Management
## init:
```shell script
pip install invoke
```
## build:
```shell script
invoke build
```
## run:
```shell script
invoke run
```
or 
```shell script
invoke build run
```

## ALTERNANIVE:
## build:
```shell script
python -m venv venv
venv\Scripts\pip.exe install -r requirements.txt
```

## run

```shell script
venv\Scripts\python.exe main.py
```

# Run Configuration:
```text
1. DEFAULT_DICTIONARY_URL - vesum text file url
default value: https://dl.dropboxusercontent.com/s/6egyjiexh12z23b/dict_corp_lt.txt?dl=0
2. VESUM_DB_NAME - mongo db name 
default value: natasha-uk-database
3. VESUM_MONGO_DB_URL - mongo db url
default value: localhost:27017
4. PORT - port to run
default value: 5000
```

# How to build VESUM txt file:
1) git clone https://github.com/brown-uk/dict_uk.git
2) cd dict_uk
3) gradlew expand
4) out/dict_corp_lt.txt - згенерований словник 

# Usage examples

```http request
POST http://localhost:8100/extract-all-uk?extract_tokens=true

["Князь Володимир народився 20 лютого 1054 року у Чернігові"]

## other urls:
http://localhost:8100/extract-persons-uk?extract_tokens=true
http://localhost:8100/extract-locations-uk?extract_tokens=true
http://localhost:8100/extract-dates-uk?extract_tokens=true
```