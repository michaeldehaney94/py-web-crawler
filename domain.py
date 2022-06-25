from urllib.parse import urlparse


# This extract domain name of website
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        # return the result 2 positions back and after the dot one position back
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
