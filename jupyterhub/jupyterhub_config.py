# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os

## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Authenticator

# Original repo
# from jhub_cas_authenticator.cas_auth import CASAuthenticator
# c.JupyterHub.authenticator_class = CASAuthenticator
#
# # The CAS URLs to redirect (un)authenticated users to.
# c.CASAuthenticator.cas_login_url = 'https://cas.uvsq.fr/login'
# c.CASLocalAuthenticator.cas_logout_url = 'https://cas.uvsq/logout'
#
# # The CAS endpoint for validating service tickets.
# c.CASAuthenticator.cas_service_validate_url = 'https://cas.uvsq.fr/serviceValidate'
#
# # The service URL the CAS server will redirect the browser back to on successful authentication.
# c.CASAuthenticator.cas_service_url = 'https://%s/hub/login' % os.environ['HOST']
#

# Try admin users + auto-create in container
c.Authenticator.admin_users = { 'test' }
# c.LocalAuthenticator.create_system_users = True  # This works, BUT with basic config user not activated until passwd set manually it seems. https://stackoverflow.com/questions/49271206/password-for-default-system-user-created-in-jupyterhub

# Dummy auth - Needs hub > v1.0 (or pip install for older hub)
# See https://jupyterhub.readthedocs.io/en/stable/api/auth.html#dummyauthenticator and https://github.com/jupyterhub/dummyauthenticator
c.JupyterHub.authenticator_class = "dummy"
c.DummyAuthenticator.password = "testpass"

# Use Github
# from oauthenticator.github import GitHubOAuthenticator
# c.JupyterHub.authenticator_class = GitHubOAuthenticator


## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Updates for now containers 19/07/21
# See https://discourse.jupyter.org/t/why-does-jupyterhub-not-see-the-docker-network-i-have-created/5275/11
c.DockerSpawmer.use_internal_ip = True
c.DockerSpawner.remove = True

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'


## Services
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]
