# Choose your desired base image 
FROM jupyter/python2:latest
# Install python3 libraries
RUN pip install fiona==1.8a1 folium descartes
# RUN pip install pyqtgraph
# Install python2 libraries
# RUN conda install -n python2 rtree
RUN $CONDA_DIR/envs/python2/bin/pip install requests clint descartes
#
#Voor Peil_2_gekozen_peil moet fiona geupdate worden. 
# RUN $CONDA_DIR/envs/python2/bin/pip install --upgrade fiona

