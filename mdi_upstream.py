#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re
import json

upstream_version_url = 'https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/scss/_variables.scss'
upstream_meta_url = 'http://cdn.materialdesignicons.com/{}/meta.json'


def get_latest_version():
    # Download & parse upstream meta file
    response = urllib.request.urlopen(upstream_version_url)
    _variables = response.read().decode('utf-8')

    version_regex = re.compile('\$mdi-version:\s*"(.*)" *')
    version_matches = version_regex.findall(_variables)
    return version_matches[0]


def fetch_meta():
    version = get_latest_version()
    meta_url = upstream_meta_url.format(version)

    # Download & parse upstream meta file
    response = urllib.request.urlopen(meta_url)
    icons = json.loads(response.read().decode('utf-8'))

    if len(icons) == 0:
        return None

    data = {
        'version': version,
        'icons': []
    }

    for icon in icons:
        data['icons'].append({
            'id': icon['id'],
            'name': icon['name'],
            'codepoint': icon['codepoint'],
            'aliases': icon['aliases'],
            'author': icon.get('author', None),  # Author is not available right now
            'version': icon.get('version', None)  # Same
        })

    return data
