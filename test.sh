nose2 --plugin nose2.plugins.junitxml --junit-xml
mv nose2-junit.xml results
python app.py
