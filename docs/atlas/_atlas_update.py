import os
import json

hostdir = os.path.dirname(__file__)
# docsdir = os.path.join(hostdir, '..', 'docs')
atlas_info_filename = os.path.join(hostdir, "_atlas_info.json")
atlas_pages_dirname = 'pages'
atlas_pages_dir = os.path.join(hostdir, atlas_pages_dirname)
atlas_url = 'https://github.com/rsbyrne/demonstration/tree/master/atlas'
atlas_pages_url = os.path.join(atlas_url, atlas_pages_dirname)

def make_page(path):
    path_to_model = os.path.dirname(path)
    filename = os.path.basename(path)
    command = 'jupyter nbconvert --to html ' + path
    os.system(command)

def save_atlas_info(atlas_info):
    atlas_info_items = sorted(atlas_info.items())
    filename = os.path.join(hostdir, "_atlas_info.json")
    with open(atlas_info_filename, 'w') as file:
        json.dump(atlas_info_items, file)

def load_atlas_info():
    if os.path.exists("_atlas_info.json"):
        with open(atlas_info_filename, 'r') as file:
            atlas_info_items = json.load(file)
        atlas_info = dict(atlas_info_items)
    else:
        atlas_info = {'pages': []}
    return atlas_info

def update_atlas():
    atlas_info = load_atlas_info()
    directories = os.listdir(atlas_pages_dir)
    for directory in sorted(directories):
        model_directory = os.path.join(atlas_pages_dir, directory)
        model_contents = os.listdir(model_directory)
        for filename in sorted(model_contents):
            name, extension = os.path.splitext(filename)
            if extension == '.ipynb':
                path_to_nb = os.path.join(atlas_pages_dir, directory, filename)
                make_page(path_to_nb)
                html_name = name + '.html'
                page_filename = os.path.join(atlas_pages_dir, directory, html_name)
                page_url = os.path.join(atlas_pages_url, directory, html_name),
                atlas_info['pages'].append(page_url)
                break
        atlas_info['pages'] = sorted(set(atlas_info['pages']))
    save_atlas_info(atlas_info)

update_atlas()
