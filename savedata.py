import os
from distutils.file_util import write_file


# auto created directory for web data scrapped
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Now creating the directory ' + directory + '....')
        os.makedirs(directory)


# creates two files - (1)queue for websites being crawled (2)websites that has already been crawled
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    # checks if files exist
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# write to file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# add data to file
def append_to_file(path, data):
    with open(path, 'a') as f:
        # each new information will be printed on a new line
        f.write(data, '\n')


def delete_file_contents(path):
    open(path, 'w').close()


# these two functions are implemented to reduce latency
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for ln in sorted(links):
            f.write(ln + '\n')
