# pynetbox-stubs

Project that contains Python stub files for [pynetbox](https://github.com/netbox-community/pynetbox) in order to allow type checking code that uses pynetbox with [mypy](http://mypy-lang.org/)

This module also includes stubs for the following NetBox plugins:

* [netbox-bgp](https://github.com/k01ek/netbox-bgp)

# Installation

```shell
pip install git+https://github.com/interdotlink/pynetbox-stubs.git#egg=pynetbox-stubs
```

# Example

Enables autocompletion: 

![](pynetbox-stubs.gif)

# Development & Contributing

You'll need a local netbox running on port `8080`, then run

```shell
make openapi.json
python -m venv venv
. venv/bin/activate 
pip install -r requirements.txt
tox -e gen,fixlint
```

Before raising a PR make sure that tox tests are passing:

```shell
pip install tox
tox
````

## TODOs:

Right now, this project is still unfinished:

* [x] make stubs for `pynetbox.models.*`
* [x] `pynetbox.core.query`
* [X] `pynetbox.core.app.PluginsApp`
* [x] `POST`, `POST`, `PATCH` parameters
* [x] Detail routes like `/ipam/ip-ranges/{id}/available-ips/`
* [ ] Custom fields