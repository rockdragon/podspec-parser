#!/usr/bin/env bash

antlr4='java -jar /usr/local/lib/antlr-4.7.1-complete.jar'
${antlr4} -Dlanguage=Python3 cocoapods.g4
${antlr4} -Dlanguage=Python3 -visitor cocoapods.g4