# Choose your desired base image 
FROM hhnk_jupyter:latest
# Install python3 libraries
RUN pip install --upgrade pip
RUN pip install fiona==1.8a1 folium descartes apscheduler
# RUN pip install pyqtgraph
# Install python2 libraries
# RUN conda install -n python2 rtree
RUN $CONDA_DIR/envs/python2/bin/pip install --upgrade pip, threedigrid
RUN $CONDA_DIR/envs/python2/bin/pip install requests clint descartes apscheduler, tqdm
#
#Voor Peil_2_gekozen_peil moet fiona geupdate worden. 
