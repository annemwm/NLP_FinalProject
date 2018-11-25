# NLP Final Project

Machine translation between English and Inuktitut

## Morphological Parser
To compile jar wrappers for java:
```
rm Morph_Parsed.txt

cd Parser

javac -cp Uqailaut.jar MorphologicalParser.java

java -cp .:Uqailaut.jar:junit.jar MorphologicalParser
```
This will write the Morphological parse to Morph_Parsed.txt
