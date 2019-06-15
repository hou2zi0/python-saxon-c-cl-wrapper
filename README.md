# python-saxon-c-cl-wrapper
Wrapps interaction with the Saxon C jars on the command line in a Python class for ease of usage, f.e. in Jupyter Notebooks.

## Usage

Download the `Py3SaxCCLIWrapper` folder or clone the repository into a section of your file system where Python 3 will look for modules. Maybe you will have to point Python to the location with the following lines of code:
```python
import sys
sys.path.append(r'./path/to/module/folder')
```
Download the `Saxon9 Home Edition jars` here and put them somewhere in your user directory, e.g.:
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
