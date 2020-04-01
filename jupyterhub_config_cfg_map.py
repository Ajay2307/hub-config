# The JupyterLab user interface
c.Spawner.default_url = '/lab'
 
# Jupyterhub Log level
c.JupyterHub.log_level = 'DEBUG'
c.Spawner.http_timeout = 1800000
c.Authenticator.auto_login = True
'''
c.KubeSpawner.profile_list = [
    {
        'display_name': 'Minimal Python Notebook',
        'kubespawner_override': {
          #  'image_spec': 'notebook:minimal',
           #'image_spec': 'notebook:min-git',
         #'image_spec': 'notebook:lib16',
          # 'image_spec': 'notebook:lib40',
         # 'image_spec': 'note:v4',
         'image_spec': 'note:minimal-lib',
          # 'image_spec': 's2i-nb:v1',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'Data Science Notebook',
        'kubespawner_override': {
          # 'image_spec': 'note:ds',
          # 'image_spec': 'notebook:ds-git',
          'image_spec': 'note:ds4',
            'supplemental_gids': [100]
        }
    },
    {
        'display_name': 'R - Notebook',
        'kubespawner_override': {
            #'image_spec': 'notebook:r-nb',
             'image_spec': 'notebook:r-nb-git',
            'supplemental_gids': [100]
        },
    }
]
c.KubeSpawner.supplemental_gids = [100]
'''
#Persistant storage
c.KubeSpawner.user_storage_pvc_ensure = True
c.KubeSpawner.pvc_name_template = 'iventura-nb-{username}'
c.KubeSpawner.user_storage_capacity = '1Gi'
  
c.KubeSpawner.volumes = [
    {
        'name': 'data',
        'persistentVolumeClaim': {
            'claimName': c.KubeSpawner.pvc_name_template
        }
    }
]
  
c.KubeSpawner.volume_mounts = [
    {
        'name': 'data',
      # 'mountPath': '/home/iventura'
       'mountPath': '/opt/app-root/src'
    }
]
