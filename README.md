# Data Wrangler (DW)

A simple python package with convenient methods for data cleaning and transformations.

## Classes
The DW package includes the following packages 

### DataWrangler

|Methods | Description|
|--------|------------|
|remove_pii| A list called pii_info is compiled as a regular expression pattern that is used to remove sensitive information. A cleaned string called no_pii is returned with the removed PII. |
|insert_space| Takes a string and index argument to add spacing in a string at a given index. |
|check_spacing| Checks for spacing in front and end of string by gettting the index of the found word and subtracting 1 for the front space and adding the length of the word to the index for the rear spacing. The insert_space method is used if a space should exist where there is none -- front or back. |


### XmlToCsvWriter