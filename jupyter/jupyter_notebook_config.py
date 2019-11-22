## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = 'sha1:0d66933b7f09:57bbf8501b575f04b00239dd499098a02ace3503'

