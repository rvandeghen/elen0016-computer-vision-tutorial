import os
from cytomine import Cytomine
from cytomine.models import *

my_local_path = "images"
host = "https://learn.cytomine.be"
public_key = 'your_key'
private_key = 'your_key'
conn = Cytomine.connect(host, public_key, private_key)

print(conn.current_user)

projects = ProjectCollection().fetch()
for project in projects:
    
    image_instances = ImageInstanceCollection().fetch_with_filter("project", project.id)
    path = os.path.join(my_local_path, project.name, image_instances[0].originalFilename)
    image_instances[0].download(path, override=False)