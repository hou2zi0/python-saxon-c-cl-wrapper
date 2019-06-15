# python-saxon-c-cl-wrapper
Wrapps interaction with the Saxon C jars on the command line in a Python class for easier  usage of XPath 3.0, XQuery 3.0, and XSLT 3.0, f.e. in Jupyter Notebooks.

Because the class is only a thin wrapper to the Saxon CLI the methods are rather slow.

An example Jupyter notebook may be found [here](https://github.com/hou2zi0/python-saxon-c-cl-wrapper/blob/master/Example.ipynb).

## Usage

Download the `Py3SaxCCLIWrapper` folder or clone the repository into a section of your file system where Python 3 will look for modules. Maybe you will have to point Python to the location with the following lines of code:
```python
import sys
sys.path.append(r'./path/to/module/folder')
```
Download the `Saxon9 Home Edition jars` [here](https://www.saxonica.com/download/c.xml) and put them somewhere in your user directory, e.g.:
```
/Users/user/saxon/saxon9he.jar
```
Import the wrapper class:
```python
from Py3SaxCCLIWrapper import SaxWrapper as SW
```
The `__init__.py` will try to auto detect the location of the `Saxon jars`.
Then, instantiate the main class with a path to an XML file:
```python
PMS = SW.PyMiniSaxon(file='/Users/max/test.xml')
```
Now you can call f.e. the XPath method on the previously specified XML file:
```python
PMS.XPath('//b[@id="x"]')
```
Now every method will work on this XML file, unless a specific string input is specified when the XPath, XQuery, or XSLT method is called:
```python
PMS.XSLT('/Users/max/test.xsl', fromString=fromString)
```

## Available methods

|Method|Input|Output|
|---|---|---|
|XPath|XPath query as string, file path to source or string|string|
|XQuery|file path to XQuery file, file path to source or string|string|
|XSLT|file path to XSLT file, file path to source or string|string|
|count|XPath query as string|Integer|
|countDistinct|XPath query as string|Integer|
|count|XPath query as string|Integer|
|findAllTextNodesOf|XPath query as string|List of strings|
|findAllNodes|XPath query as string|List of strings|



## ToDo

* Refactor 
* Add more methods
