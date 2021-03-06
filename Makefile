# Geometry3 Makefile
# 
VERSION= 0.1.0
PYTHON= python3
SETUP_PY= setup.py
TWINE= twine
PYPI= testpypi
TEMP= build dist

.PHONY: VERSION test readme bdist sdist release upload clean

all:
	@echo "VERSION=$(VERSION)"
	@echo "Targets:"
	@echo "	test    - run pytest"
	@echo "	bdist   - binary distribution"
	@echo "	sdist   - source distribution"
	@echo "	readme  - README rst checking"
	@echo "	release - VERSION=$(VERSION) readme bdist sdist"
	@echo "	upload  - release and upload to PYPI=$(PYPI)"
	@echo "	clean   - cleanup temporary files: TEMP=$(TEMP)"

VERSION:
	@echo $(VERSION) > $@

test: VERSION
	$(PYTHON) $(SETUP_PY) test

bdist: VERSION
	$(PYTHON) $(SETUP_PY) bdist_wheel

sdist: VERSION
	$(PYTHON) $(SETUP_PY) sdist

readme: VERSION README.rst
	$(PYTHON) $(SETUP_PY) check -r -s

release: VERSION readme bdist sdist


upload: release 
	$(TWINE) upload --repository ${PYPI} dist/*

clean:
	-@$(PYTHON) $(SETUP_PY) clean >& /dev/null
	@$(RM) -rf $(TEMP) *~ *.egg-info

