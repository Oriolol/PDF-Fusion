# PDF fusion #

Python script for merging pdf files

## Software Requirements ##
  * Python 3.9 or higher
  * [pypdf](https://pypi.org/project/pypdf/)

## Usage ##

First, place the files you want to merge into the Input directory.

```bash
python3 pdf_fusion.py <output_name.pdf> <input1.pdf> <input2.pdf> ... <inputN.pdf>
```
The first argument is the name that will be given to the produced pdf. All the following arguments are the pdf files to merge, appearing in the order of the inputs.
The resulting pdf will appear in the Output directory.
