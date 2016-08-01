#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

meta_upstream_uri = 'https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/scss/_variables.scss'


def fetch_meta():
    # Download & parse upstream meta file
    response = urllib.request.urlopen(meta_upstream_uri)
    _variables = response.read().decode('utf-8')

    icons_regex = re.compile('    "(.*)": (F[A-F0-9]*),?')
    icons_matches = icons_regex.findall(_variables)

    version_regex = re.compile('\$mdi-version:\s*"(.*)" *')
    version_matches = version_regex.findall(_variables)
    version = version_matches[0]

    if len(icons_matches) == 0:
        return None

    data = {
        'version': version,
        'icons': []
    }

    for match in icons_matches:
        data['icons'].append({
            'name': match[0],
            'codepoint': match[1]
        })

    return data
