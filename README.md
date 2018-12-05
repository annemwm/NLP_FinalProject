# NLP Final Project

Machine translation between English and Inuktitut

## Morphological Parser
It is not recommended to try to parse the entire Hansard in this way. The NRC Uqailaut parser is a fairly slow piece of software and relatively prone to errors, so it can take upwards of several days to parse the Hansard corpus.

To compile and run jar wrapper for Uqailuat:
```
rm Morph_Parsed.txt

cd Parser

javac -cp Uqailaut.jar MorphologicalParser.java

java -cp .:Uqailaut.jar:junit.jar MorphologicalParser (Start_Line)
```
This will write the Morphological parse to Morph_Parsed.txt


Source code For NRC Uqailaut Parser can be found at http://www.inuktitutcomputing.ca
