# NLP Final Project

Machine translation between English and Inuktitut

## Parser
To compile jar wrappers for java:
```
cd Parser

javac -cp Uqailaut.jar MorphologicalParser.java

java -cp .:Uqailaut.jar:junit.jar MorphologicalParser
```
This will write the Morphological parse to Morph_Parsed.txt
