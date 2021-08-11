FROM jupyter/scipy-notebook


USER $NB_UID


ENV CPATH=$CONDA_DIR/include


# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
