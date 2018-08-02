# Choose your desired base image 
FROM jupyter/python2:latest
# Install python3 libraries
# RUN pip install pyqtgraph
# Install python2 libraries
RUN $CONDA_DIR/envs/python2/bin/pip install ipywidgets openpyxl xlrd xlwt
#
#Voor Peil_2_gekozen_peil moet fiona geupdate worden. 
RUN $CONDA_DIR/envs/python2/bin/pip install --upgrade fiona

