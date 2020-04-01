FROM docker.io/ajay2307/jupyterhub:kc

USER root

RUN rm -rf .jupyter/jupyterhub_config.py

COPY jupyterhub_config_home.py .jupyter/jupyterhub_config.py

RUN rm -rf /opt/app-root/etc/jupyterhub_config.py

COPY jupyterhub_config_etc.py /opt/app-root/etc/jupyterhub_config.py

RUN rm -rf /opt/app-root/configs/jupyterhub_config.py

COPY jupyterhub_config_cfg_map.py /opt/app-root/configs/jupyterhub_config.py 
