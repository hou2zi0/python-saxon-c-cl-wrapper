from . import SAXONPATH
from pathlib import Path
import subprocess as sub

class PyMiniSaxon:
    def __init__(self, saxonpath=SAXONPATH, file=False, def_ns=False):
        self.setSaxonPath(saxonpath)
        self.setSourceFromFile(file)


    # https://dbader.org/blog/python-repr-vs-str
    def __repr__(self):
        return (f'{self.__class__.__name__}({self.saxonpath!r}, {self.file!r})')

    def __str__(self):
        return f'a simple Saxon-C XML Interaction Object'

    # Set the file pathes
    def setSaxonPath(self, saxonpath):
        if Path(f'{saxonpath}').is_file():
            # file exists
            self.saxonpath = f'{saxonpath}'
        else:
            print(f'Saxon Path error: "{saxonpath}" is not a correct path.')
            self.saxonpath = ""
            #return False

    def setSourceFromFile(self, file):
        if Path(f'{file}').is_file():
            # file exists
            self.file = file
        else:
            print(f'File Path error: "{file}" is not a correct path.')
            self.file = ""

    #def setSourceFromString(self, file):
    #    if Path(f'{file}').is_file():
    #        # file exists
    #        self.file = file
    #    else:
    #        print(f'File Path error: "{file}" is not a correct path.')
    #        self.file = ""

    # XPath, XQuery, XSLT methods
    def XPath(self, node, fromString=False):
        querystring = f'{node}'

        if (self.saxonpath != '' and self.file != '' ):
            if (fromString == False):
                querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-qs:{querystring}'],
                       capture_output=True,
                       text=True)
            else:
                querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-qs:parse-xml-fragment("{fromString}"){querystring}'],
                       capture_output=True,
                       text=True)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            print(f'The query {node} returned {querystring_result.stdout[38:]} items.')
            return str(querystring_result.stdout[38:])
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None

    def XQuery(self, xquery_file, fromString=False):
        if Path(f'{xquery_file}').is_file() == False:
            print(f'XQuery file path error: "{xquery_file}" is not a correct path.')
            return ''

        if (self.saxonpath != '' and self.file != '' ):
            if (fromString == False):
                querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-q:{xquery_file}'],
                       capture_output=True,
                       text=True)
            else:
                querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:-', f'-q:{xquery_file}'],
                       capture_output=True,
                       text=True,
                       input=fromString)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            print(f'The query {node} returned {querystring_result.stdout[38:]} items.')
            return str(querystring_result.stdout[38:])
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None

    def XSLT(self, xslt_file, fromString=False):
        if Path(f'{xslt_file}').is_file() == False:
            print(f'XQuery file path error: "{xslt_file}" is not a correct path.')
            return ''

        if (self.saxonpath != '' and self.file != '' ):
            if (fromString == False):
                querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Transform', f'-s:file:{self.file}', f'-xsl:{xslt_file}'],
                       capture_output=True,
                       text=True)
            else:
                querystring_result = sub.run([ 'java', '-cp', self.saxonpath, 'net.sf.saxon.Transform', f'-s:-', f'-xsl:{xslt_file}' ],
                       capture_output=True,
                       text=True,
                       input=fromString)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            print(f'The transformation {xslt_file} returned:\n{querystring_result.stdout[38:]}')
            return str(querystring_result.stdout[38:])
        else:
            print(f'The transformation {xslt_file} raised an error: {querystring_result.stderr}')
            return None

    # Main XPath func methods
    def count(self, node):
        querystring = f'count({node})'
        if (self.saxonpath != '' and self.file != '' ):
            querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-qs:{querystring}'],
                   capture_output=True,
                   text=True)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            print(f'The query {node} returned {querystring_result.stdout[38:]} items.')
            return int(querystring_result.stdout[38:])
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None

    def countDistinct(self, node):
        querystring = f'count(distinct-values({node}))'
        if (self.saxonpath != '' and self.file != '' ):
            querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-qs:{querystring}'],
                   capture_output=True,
                   text=True)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            print(f'The query {node} returned {querystring_result.stdout[38:]} items.')
            return int(querystring_result.stdout[38:])
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None

    def findAllTextNodesOf(self, node):
        querystring = f'{node}'
        if (self.saxonpath != '' and self.file != '' ):
            querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-qs:string-join({querystring},"@@@")'],
                   capture_output=True,
                   text=True)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            return_value = querystring_result.stdout[38:].split('@@@')
            return_string = "; ".join(return_value)
            print(f'The query {node} returned {return_string} items.')
            return return_value
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None

    def findAllNodes(self, node):
        querystring = f'{node}'
        if (self.saxonpath != '' and self.file != '' ):
            querystring_result = sub.run(['java', '-cp', self.saxonpath, 'net.sf.saxon.Query', f'-s:file:{self.file}', f'-qs:{querystring}'],
                   capture_output=True,
                   text=True)
        else:
            if (self.saxonpath != ''):
                print(f'Saxon Path error: {saxonpath} is not a correct path.')
            else:
                print(f'File Path error: {file} is not a correct path.')

        if (querystring_result.stderr == ''):
            return_value = self.splitNodeList(querystring_result.stdout[38:])
            return_string = querystring_result.stdout[38:]
            print(f'The query {node} returned {return_string} items.')
            return return_value
        else:
            print(f'The query {node} raised an error: {querystring_result.stderr}')
            return None



    ####
    # Helper methods
    ####
    def splitNodeList(self, thestring):
        lst = []
        Level = 0

        for i,c in enumerate(thestring):
            if c == '<' and thestring[i+1] != '/':
                Level += 1
                if Level == 1:
                    lst.append(i)
            elif c == '/' and thestring[i-1] == '<':
                Level -= 1

        out_list = []
        for i,item in enumerate(lst):
            try:
                out_list.append(thestring[item:lst[i+1]])
            except:
                out_list.append(thestring[item:])
        if (bool(out_list) == False):
            out_list.append(thestring)
        return out_list
