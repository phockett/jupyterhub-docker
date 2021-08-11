# JupyterHub + ePSproc

Adapted from https://github.com/defeo/jupyterhub-docker (original notes below).

Main changes from original:

- Unversioned Hub + Lab containers (i.e. use updated containers).
- Set Lab to dummy auth method (use for local testing only!).
- Added Lab container version with [ePSproc](https://github.com/phockett/ePSproc) (see `docker-compose.ePSproc.yml` and `/jupyterlab-ePSproc`), currently set for dev branch.
- Added basic env test notebook.
- Set docker volume paths for local Synology machine (see `docker-compose*`).

Lab container currently uses Jupyter Stacks scipy notebook as base, https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook


---

# JupyterHub deployment in use at Université de Versailles

This is a [JupyterHub](https://jupyter.org/hub) deployment based on
Docker currently in use at [Université de
Versailles](https://jupyter.ens.uvsq.fr/).

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner);
- Central authentication to the University CAS server;
- User data persistence;
- HTTPS proxy.

## Learn more

This deployment is described in depth in [this blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).

### Adapt to your needs

This deployment is ready to clone and roll on your own server. Read
the [blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/) first,
to be sure you understand the configuration.

Then, if you like, clone this repository and apply (at least) the
following changes:

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In [`reverse-proxy/traefik.toml`](reverse-proxy/traefik.toml), edit
  the paths in `certFile` and `keyFile` and point them to your own TLS
  certificates. Possibly edit the `volumes` section in the
  `reverse-proyx` service in
  [`docker-compose.yml`](docker-compose.yml).
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *"Authenticator"* section according to your institution
  authentication server.  If in doubt, [read
  here](https://jupyterhub.readthedocs.io/en/stable/getting-started/authenticators-users-basics.html).

Other changes you may like to make:

- Edit [`jupyterlab/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like. Do not forget to change
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py)
  accordingly, in particular the *"user data persistence"* section.

### Run!

Once you are ready, build and launch the application with

```
docker-compose build
docker-compose up -d
```

Read the [Docker Compose manual](https://docs.docker.com/compose/) to
learn how to manage your application.

## Acknowledgements

<img src="https://opendreamkit.org/public/logos/Flag_of_Europe.svg" height="20"> Work partially funded by the EU H2020 project
[OpenDreamKit](https://opendreamkit.org/).
