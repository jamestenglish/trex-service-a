#!/bin/bash
nose2 --plugin nose2.plugins.junitxml --junit-xml 
ls -la
mv nose2-junit.xml results
