# Choose your desired base image 
FROM hhnk_jupyter:latest
# Install python3 libraries
# RUN pip install numpy --upgrade pip numpy --upgrade
RUN pip install fiona==1.8a1 folium descartes apscheduler xlrd xlwt plotly lizard_connector

# RUN pip install pyqtgraph
# Install python2 libraries
# RUN conda install -n python2 rtree
RUN $CONDA_DIR/envs/python2/bin/pip install --upgrade pip threedigrid numpy
RUN $CONDA_DIR/envs/python2/bin/pip install requests clint descartes apscheduler tqdm folium xlrd xlwt plotly lizard_connector

#
#Voor Peil_2_gekozen_peil moet fiona geupdate worden. 
