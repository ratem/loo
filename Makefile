all: deps test

deps: specloud should-dsl ludibrio

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install --no-deps specloud 

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/hugobr/should-dsl/tarball/master

ludibrio:
	sudo easy_install ludibrio

path:
    export PYTHONPATH=..

test: unit acceptance

unit: path specloud should-dsl
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud spec
	@echo

