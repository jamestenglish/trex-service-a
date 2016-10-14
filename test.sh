nose2 --plugin nose2.plugins.junitxml --junit-xml > /dev/null
ls -la
mv nose2-junit.xml results
