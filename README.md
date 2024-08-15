# flextext converters
Converters to and from flextext interlinear format


### Toolbox to FieldWorks Converter - Developer Instructions
* All converter files are located in the "toolbox" package
`flextext-converters/src/toolbox`

* Must have python version >= 3.12.2 installed</li>
* Install requirements with `pip install -r requirements.txt --user`
* Install tox `python -m pip install --user tox`
* Run tests and linting: `python -m tox`
* Run the converter: `python src/toolbox/main.py` and follow instructions
* Notes
  * marker files are used to parse Toolbox files
  * json marker files are created when user specifies the type of each marker
  * Toolbox files are the files to be converted
  * FlexText files are the output of the converter
