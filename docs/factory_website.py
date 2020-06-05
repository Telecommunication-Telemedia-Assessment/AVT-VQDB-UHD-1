#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 00:57:55 2020

@author: Boris Reif
"""
import json
import re
import csv
import os.path
import glob

SITES = ['source', 'test_1', 'test_2', 'test_3', 'test_4', 'videos']


class Website(object):
    Site = {}
    Data = {}

    def __init__(self):
        self.html = 'not used'

    @property
    def html(self):
        return self.__html

    @html.setter
    def html(self, html):
        self.__html = html

    @classmethod
    def get_site(cls):
        return cls.Site

    @classmethod
    def set_site(cls, site={}):
        cls.Site = site
        return cls.Site

    @classmethod
    def get_data(cls):
        return cls.Data

    @classmethod
    def set_data(cls, data={}):
        cls.Data = data
        return cls.Data

    @classmethod
    def print_data(cls):
        print(cls.Data)
        return cls.Data

    @classmethod
    def print_site(cls):
        print(cls.Site)
        return cls.Site

class Head(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Head -->
        <head>
            <title>''' + Website.Site['title'] + ''' Videos</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="author" content="Boris A. Reif">
            <meta name="description" content="This site contains the ''' + Website.Site['title'] + ''' videos">
            <link rel="stylesheet" href="./css/w3.css">
            <link href="./fonts/fontawesome-free-5.13.0-web/css/all.css" rel="stylesheet"> <!--load all styles -->
            <link href="./css/font.css" rel="stylesheet"> <!--load all styles -->
            '''
        '''
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        '''
        for i in Website.Site['css']:
            self.html += '''<link rel="stylesheet" href="'''
            self.html += i
            self.html += '''">'''
        self.html += '''<script src = "./javascript/sidebar.js"></script>'''
        for i in Website.Site['top_js']:
            self.html += '''<script src = "'''
            self.html += i
            self.html += '''></script>'''
        self.html += '''
        </head>
        <!-- END Head -->
        '''


# <!-- <span class="" onclick="document.getElementById('id01').style.display='block'">Contact</span> -->
class Anschrift(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Anschrift -->
            <p>Steve G&#246;ring</p>
            <p>Wissenschaftlicher Mitarbeiter
                <br>Telefon: 03677 69-2731
                <br>Fax: 03677 69-1255
                <br>Helmholtzbau, Raum H 3537
                <br>Email: <a href="mailto:steve.goering@tu-ilmenau.de?Subject=AVT-VQDB-UHD-1" target="_top">steve.goering@tu-ilmenau.de</a>
            </p>'''


class Modal_old(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Modal -->
            <div id="id01" class="w3-modal">
                <div class="w3-modal-content w3-card-4">
                    <header class="w3-container w3-black">
                        <span onclick="document.getElementById('id01').style.display='none'" class="w3-button w3-display-topright">&times;</span>
                        <h2>Contact:</h2>
                    </header>
                        <div class="w3-container">
                            ''' + Anschrift().html + '''
                        </div>
                    <footer class="w3-container w3-black">
                        <p>Fachgebiet Audiovisuelle Technik der TU Ilmenau</p>
                    </footer>
                </div>
            </div>
            <!-- END Modal -->
            '''

class Modal(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Modal -->
            <div id="id01" class="w3-modal">
                <div class="w3-modal-content w3-card-4">
                    <header class="w3-container w3-indigo">
                        <span onclick="document.getElementById('id01').style.display='none'" class="w3-button w3-display-topright">&times;</span>
                        <h3>Contact:</h3>
                    </header>
                        <div class="w3-container">
                            <h2>Audiovisual Technology Group (AVT) of TU Ilmenau</h2>
                            <ul>
                                <li><a href="https://www.tu-ilmenau.de/en/audio-visual-technology/" target="_blank">Webpage</a></li>
                                <li><a href="https://twitter.com/avt_imt?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @avt_imt</a>
                                <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></li>

                                <li><a href="https://github.com/Telecommunication-Telemedia-Assessment/" target="_blank">
                                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" style="height:1.5em" />
                                    Github</a>
                                </li>

                            </ul>
                        </div>
                    <footer class="w3-container w3-deep-orange">
                    </footer>
                </div>
            </div>
            <!-- END Modal -->
            '''


class Top(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Top menu -->
        <div class="w3-top">
            <div class="w3-white w3-xlarge" style="max-width:1200px;margin:auto">
            <div class="w3-button w3-padding-16 w3-left" onclick="w3_open()"><i class="fa fa-align-justify fa-1x"></i></div>
            <div class="w3-button w3-padding-16 w3-right" onclick="document.getElementById('id01').style.display='block'">Contact</div>
            <div class="w3-center w3-padding-16">AVT-VQDB-UHD-1 video quality database</div>''' + Modal().html + '''</div>
        </div><!-- END Top menu -->'''


class Sidebar(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Sidebar (hidden by default) -->
        <nav class="w3-sidebar w3-bar-block w3-card w3-top w3-xlarge w3-animate-left" style="display:none;z-index:2;width:40%;min-width:300px" id="mySidebar">
            <a href="javascript:void(0)" onclick="w3_close()" class="w3-bar-item w3-button">Close Menu</a>
            <a href="#videos" onclick="w3_close()" class="w3-bar-item w3-button">Videos</a>
            <a href="#authors" onclick="w3_close()" class="w3-bar-item w3-button">Authors</a>
            <a href="#paper" onclick="w3_close()" class="w3-bar-item w3-button">Paper</a>
            <a href="#copyright" onclick="w3_close()" class="w3-bar-item w3-button">Copyright</a>
            <a href="#links" onclick="w3_close()" class="w3-bar-item w3-button">Links</a>
            '''
        for i in SITES:
            self.html += '''<a href = "''' + Website.Site['folder'] + i + '''.html" onclick="w3_close()" class ="w3-bar-item w3-button"> '''
            self.html += i.replace("_", " ").title() + '''</a>'''
        self.html += '''</nav><!-- END Sidebar -->'''


class Pagination(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Pagination -->
            <div class="w3-center w3-padding-32">
            <div class="w3-bar">
        '''
        for i in SITES:
            self.html += '''<a href = "''' + Website.Site['folder'] + i + '''.html" class ="w3-bar-item w3-button '''
            if i == Website.Site['page']:
                self.html += '''w3-indigo"'''
            else:
                self.html += '''w3-hover-indigo"'''
            self.html += '''>''' + i.replace("_", " ").title() + '''</a>'''
        self.html += '''
            </div>
        </div>
        <!-- END Pagination -->
        '''


class Card(Website):
    def __init__(self, title=' ', dict={}):
        super().__init__()
        self.html = '''<!-- Card -->
        <div class="w3-card">
        <a href="''' + Website.Site['path'] + dict['path'] + '''">
            <img src="''' + dict['thumb'] + '''" alt="''' + dict['name'] + '''" style="width:100%;border:0;">
        </a>
        <div class="w3-container">
            <h6>''' + dict['name'] + '''</h6>
            <p>''' + title + ''' File<br>filename extension: ''' + dict['file_ending']
        if 'bit_rate' in dict.keys():
            self.html += '''<br>bit rate: ''' + dict['bit_rate']
            self.html += '''<br>target bit rate: ''' + dict['target_bit_rate']
            self.html += '''<br>height: ''' + dict['height']
            self.html += '''<br>width: ''' + dict['width']
            # self.html += '''<br>resolution: ''' + dict['resolution']
            self.html += '''<br>frame rate: ''' + dict['frame_rate']
            self.html += '''<br>codec: ''' + dict['codec']
            self.html += '''<br>MOS: ''' + dict['mos']
            self.html += '''<br>CI: ''' + dict['ci']
        # else:
        #     print('no bit_rate')
        self.html += '''</p>
        </div>
        </div>
        <!-- END Card -->
        '''


class Selection(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Selection Tags -->
            <span class="w3-large">Show all ...</span><br>
            <div id="my_buttons">
                <button class="btn active" onclick="filterSelection('all')">Show all</button>
            '''
        filter_set = set()
        ext_set = set()
        target_bit_rate_set = set()
        resolution_set = set()
        frame_rate_set = set()
        codec_set = set()
        for i in Website.Data:
            if 'filter_name' in Website.Data[i].keys():
                filter_set.add(Website.Data[i]['filter_name'])
            else:
                print('ERROR Selection filter_name', Website.Site['title'])
            if 'file_ending' in Website.Data[i].keys():
                ext_set.add(Website.Data[i]['file_ending'])
            else:
                print('ERROR Selection file_ending', Website.Site['title'])
            if 'target_bit_rate' in Website.Data[i].keys():
                target_bit_rate_set.add(Website.Data[i]['target_bit_rate'])
            if 'resolution' in Website.Data[i].keys():
                resolution_set.add(Website.Data[i]['resolution'])
            if 'frame_rate' in Website.Data[i].keys():
                frame_rate_set.add(Website.Data[i]['frame_rate'])
            if 'codec' in Website.Data[i].keys():
                codec_set.add(Website.Data[i]['codec'])
        if filter_set:
            for i in filter_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">'''
                self.html += re.sub('[_]', ' ', i).title()
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> film title</span>''' # tooltip
                self.html += '''</button>'''
        if ext_set:
            for i in ext_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">''' + i
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> file extension</span>''' # tooltip
                self.html += '''</button>'''
        if target_bit_rate_set:
            for i in target_bit_rate_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">''' + i
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> target bit rate</span>''' # tooltip
                self.html += '''</button>'''
        if frame_rate_set:
            for i in frame_rate_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">''' + i
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> frame rate</span>''' # tooltip
                self.html += '''</button>'''
        if codec_set:
            for i in codec_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">''' + i
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> codec</span>''' # tooltip
                self.html += '''</button>'''
        if resolution_set:
            for i in resolution_set:
                self.html += '''<button class="btn w3-tooltip" onclick="filterSelection(\'''' + i + '''\')">''' + i
                self.html += '''<span class="w3-text w3-tag w3-tiny w3-indigo"> resolution</span>''' # tooltip
                self.html += '''</button>'''
        self.html += '''
        </div>
        <!-- END Selection -->'''


class SelectionList(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Selection Tags -->
        <span class="w3-large">All categories</span><br>
        <div>'''
        filter_set = set()
        ext_set = set()
        target_bit_rate_set = set()
        resolution_set = set()
        frame_rate_set = set()
        codec_set = set()
        for i in Website.Data:
            if 'filter_name' in Website.Data[i].keys():
                filter_set.add(Website.Data[i]['filter_name'])
            else:
                print('ERROR Selection filter_name', Website.Site['title'])
            if 'file_ending' in Website.Data[i].keys():
                ext_set.add(Website.Data[i]['file_ending'])
            else:
                print('ERROR Selection file_ending', Website.Site['title'])
            if 'target_bit_rate' in Website.Data[i].keys():
                target_bit_rate_set.add(Website.Data[i]['target_bit_rate'])
            if 'resolution' in Website.Data[i].keys():
                resolution_set.add(Website.Data[i]['resolution'])
            if 'frame_rate' in Website.Data[i].keys():
                frame_rate_set.add(Website.Data[i]['frame_rate'])
            if 'codec' in Website.Data[i].keys():
                codec_set.add(Website.Data[i]['codec'])
        if filter_set:
            for i in filter_set:
                # self.html += '''<span class="w3-text w3-tag w3-tiny">''' + re.sub('[_]', ' ', i).title() + '''</span>''' # tooltip
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        if ext_set:
            for i in ext_set:
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        if target_bit_rate_set:
            for i in target_bit_rate_set:
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        if frame_rate_set:
            for i in frame_rate_set:
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        if codec_set:
            for i in codec_set:
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        if resolution_set:
            for i in resolution_set:
                self.html += '''<span class ="w3-tag w3-dark-grey w3-small w3-margin-bottom">''' + re.sub('[_]', ' ', i).title() + '''</span> '''
        self.html += '''
        </div>
        <!-- END Selection -->'''



class Copyright(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Copyright -->
            <p>This database consists of short term videos based on several short movies, that are either public available or created by TU Ilmenau. The tools provided in this repository can be used to download the shared videos that are used in the described video quality tests. In the following we specify the common filename prefix, to identify the source and corresponding licence of the video. This applies to encoded and source videos that are shared within this database. For example all files that can be downloaded with the prefix bigbuck_bunny are based on the Big Bucks Bunny content and follow the corresponding licence.</p>
            <br>
            <p>We are happy that it was possible to access and use all the external video sources.</p>
            <ul class="w3-ul w3-hoverable">
                <li>bigbuck_bunny: a short 8-10s cut from  <a href="https://peach.blender.org/about/">Big Bucks Bunny</a>: <a href="https://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0</a></li>
                <li>Sparks: two short 8-10s cuts from <a href="http://download.opencontent.netflix.com/?prefix=TechblogAssets/Sparks/">Netflix Sparks movie</a>: <a href="http://download.opencontent.netflix.com.s3.amazonaws.com/TechblogAssets/Sparks/sparks_license.txt">license</a></li>
                <li>water_netflix: two short 8-10s cuts from Netflix El Fuente: <a href="http://download.opencontent.netflix.com.s3.amazonaws.com/TechblogAssets/Sparks/sparks_license.txt">license</a></li>
            </ul>
                <p>Our own contents follows the <a href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)</a> licence.</p>
            <ul class="w3-ul w3-hoverable">
                <li>Dancers 8s</li>
                <li>Cutting Orange Tuil</li>
                <li>Debris</li>
                <li>Daydreamer</li>
                <li>Vegetables</li>
                <li>Giftmord</li>
            </ul>
            <!-- END Copyright -->
            '''


class Authors(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Authors -->
            <span class="w3-large" id="authors">Authors</span>
            <ul class="w3-ul w3-hoverable">
                <li class="w3-padding-16">
                    <a href="https://www.tu-ilmenau.de/mt-avt/personen/ramachandra-rao-rakesh-rao/" target="_blank">Rakesh Rao Ramachandra Rao</a><br>
                    <a href="https://www.tu-ilmenau.de/mt-avt/" target="_blank">TU Ilmenau, Fachgebiet Audiovisuelle Technik</a><br>
                    <a href="mailto:rakesh-rao.ramachandra-rao@tu-ilmenau.de?Subject=AVT-VQDB-UHD-1" target="_top">rakesh-rao.ramachandra-rao@tu-ilmenau.de</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://www.tu-ilmenau.de/mt-avt/personen/goering-steve/" target="_blank">Steve G&#246;ring</a><br>
                    <a href="https://www.tu-ilmenau.de/mt-avt/" target="_blank">TU Ilmenau, Fachgebiet Audiovisuelle Technik</a><br>
                    <a href="mailto:steve.goering@tu-ilmenau.de?Subject=AVT-VQDB-UHD-1" target="_top">steve.goering@tu-ilmenau.de</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://www.tu-ilmenau.de/mt-avt/personen/" target="_blank">Werner Robitza</a><br>
                    <a href="https://www.tu-ilmenau.de/mt-avt/" target="_blank">TU Ilmenau, Fachgebiet Audiovisuelle Technik</a><br>
                    <a href="mailto:werner.robitza@tu-ilmenau.de?Subject=AVT-VQDB-UHD-1" target="_top">werner.robitza@tu-ilmenau.de</a>
                </li>
                <li class="w3-padding-16">
                    Bernhard Feiten<br>
                    <a href="https://www.telekom.de" target="_blank">Deutsche Telekom, Technology & Innovation</a><br>
                    <a href="mailto:bernhard.feiten@telekom.de?Subject=AVT-VQDB-UHD-1" target="_top">bernhard.feiten@telekom.de</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://www.tu-ilmenau.de/mt-avt/personen/raake-alexander/" target="_blank">Alexander Raake</a><br>
                    <a href="https://www.tu-ilmenau.de/mt-avt/" target="_blank">TU Ilmenau, Fachgebiet Audiovisuelle Technik</a><br>
                    <a href="mailto:alexander.raake@tu-ilmenau.de?Subject=AVT-VQDB-UHD-1" target="_top">alexander.raake@tu-ilmenau.de</a>
                </li>
            </ul>
            <!-- END Authors -->
            '''


class Paper(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Paper -->
            <span class="w3-large" id="paper">Paper</span><br>
            <ul class="w3-ul w3-hoverable">
                <li class="w3-padding-16">
                    <span>If you use any of the data or code please cite the following paper</span><br>
                    <pre><code>
@inproceedings{rao2019Db,
  author = {
    Rakesh Rao Ramachandra Rao and
    Steve G&#246;ring and
    Werner Robitza and
    Bernhard Feiten and
    Alexander Raake
  },
  title = {AVT-VQDB-UHD-1:
    A Large Scale Video Quality
    Database for UHD-1
    },
    booktitle={2019 IEEE ISM},
    year = {2019},
    pages={1-8},
    volume={},
    month={Dec}
}
                    </code></pre>
                </li>
            </ul>
            <!-- END Paper -->
            '''


class Links(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<!-- Links -->
            <span class="w3-large" id="links">Links</span>
            <ul class="w3-ul w3-hoverable">
                <li class="w3-padding-16">
                    <a href="https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1" target="_blank">Visit Gitlab</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://ieeexplore.ieee.org/document/8959059" target="_blank">Visit IEEE</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://www.researchgate.net/publication/338201010_AVT-VQDB-UHD-1_A_Large_Scale_Video_Quality_Database_for_UHD-1" target="_blank">Visit ResearchGate</a>
                </li>
                <li class="w3-padding-16">
                    <a href="https://www.tu-ilmenau.de/en/audio-visual-technology/" target="_blank">Visit AVT</a>
                </li>
            </ul>
            <!-- END Links -->
            '''


class Footer(Website):
    def __init__(self, flag = 0):
        super().__init__()
        self.html = '''<!-- Footer -->
        <footer class="w3-row-padding w3-padding-32">
        <div class="w3-third" id="copyright">
            <h3>Copyright & Licences</h3>
            ''' + Copyright().html + '''<br>
            <p>Powered by <a href="https://www.tu-ilmenau.de" target="_blank">TU Ilmenau</a></p>
        </div>
        <div class="w3-third">
            <h3>Information</h3>
            ''' + Authors().html + '''<br>''' + Paper().html + '''
        </div>
        <div class="w3-third">
            <h3>Other</h3>
            '''
        if flag == 0:
            self.html += Selection().html
        elif flag == 1:
            self.html += SelectionList().html
        else:
            print('no selection tags')
        self.html += '''<br>''' + Links().html + '''
        </div>
        </footer>
        <!-- END Footer -->
        '''


class Grid(Website):
    def __init__(self):
        super().__init__()
        count = 0
        mod = 3
        # self.html = "<!--Rows" + str(count) + " -->".format(count=count)
        self.html = "<!--Rows-->"
        for i in Website.Data:
            file_ending = Website.Data[i]['file_ending']
            name = Website.Data[i]['filter_name']
            text = ''
            if 'bit_rate' in Website.Data[i].keys():
                target_bit_rate = Website.Data[i]['target_bit_rate']
                codec = Website.Data[i]['codec']
                frame_rate = Website.Data[i]['frame_rate']
                height = Website.Data[i]['height']
                width = Website.Data[i]['width']
                resolution = Website.Data[i]['resolution']
                text = ''' ''' + target_bit_rate + ''' ''' + codec + ''' ''' + frame_rate + ''' ''' + resolution
            if count % mod == 0:
                self.html += '''<div class="w3-row-padding w3-margin-top">'''
            self.html += '''<div class="w3-third filterDiv ''' + name + ''' ''' + file_ending
            self.html += text
            self.html += '''">''' + Card(title=Website.Site['title'], dict=Website.Data[i]).html + '''
            </div>
            '''
            if count % mod == mod-1:
                self.html += '</div>'
            count = count + 1


class Listing(Website):
    def __init__(self):
        super().__init__()
        self.html = '''<h2> List of all video segments </h2>'''
        self.html += '''<input type = "text" id = "myInput" onkeyup = "myFunction()" '''
        self.html += '''placeholder = "Search for videos.." title = "Type in a name">'''
        self.html += '''<ul id = "myUL">'''
        for i in Website.Data:
            self.html += '''<li>'''
            self.html += '''<a href="https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/''' + Website.Data[i]['path'] + '''">'''
            self.html += i + '''</a></li>'''
        self.html += '''</ul>'''


class WebsiteFactory(object):
    @staticmethod
    def create_website(site_type, **kwargs):
        try:
            return globals()[site_type.capitalize()](**kwargs)
        except Exception:
            print("SOME ERROR")
            return None

    @staticmethod
    def get_data(file_path_name):
        reader = csv.DictReader(open(file_path_name))
        dict = {}
        for row in reader:
            key = row.pop('video_name')
            if key in dict:
                pass
            dict[key] = row
        return dict


class SourceFactory:
    def create_test_site(self, num):
        site = {
            'page': SITES[num],  # name for pagination
            'title': re.sub('[_]', ' ', SITES[num]).title(),  # title of website (for meta tag)
            'folder': './',  # where to dump the website
            'files': ['./../test_' + str(num) + '.json'],  # list of  file path names to json location
            'css': ['./css/design.css', './css/filter.css'],  # list of  file path names to script location
            'top_js': [],  # list of  file path names to script location
            'bottom_js': ['./javascript/filter.js'],  # list of  file path names to script location
            'thumbs': os.listdir('./thumbs/new/'),  # get all the thumb names
            'fold_thumbs': './thumbs/new/',  # store the folder of thumbs
            'fold_videos': 'test_' + str(num) + '/',  # where are the videos?
            'path': 'https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/',  # path to  videos?
            'metadata': './../test_' + str(num) + '/metadata.csv', # '../test_' + num + '/metadata.csv',
            'mos_ci': './../test_' + str(num) + '/mos_ci.csv', # '../test_' + num + '/metadata.csv',
            'objective_scores': './../test_' + str(num) + '/objective_scores.csv' # '../test_' + num + '/metadata.csv'
        }
        print(site["files"])
        metadata = WebsiteFactory.get_data(site['metadata'])
        mos_ci = WebsiteFactory.get_data(site['mos_ci'])
        # objective_scores = WebsiteFactory.get_data(site['objective_scores'])
        data = {}
        if not site['files']:
            print('ERROR: no data')
        else:
            dat = []
            for j in site['files']:
                with open(j) as json_f:
                    dat += json.load(json_f)
            for i in dat:
                data[i] = {}
                data[i]['path'] = i
                video_name = re.sub(r"test\_\d/segments/", "", i, flags=re.I)
                data[i]['video_name'] = video_name
                data[i]['file_ending'] = i.split('.')[-1]
                data[i]['target_bit_rate'] = metadata[video_name]['video_target_bitrate']
                data[i]['height'] = metadata[video_name]['video_height']
                data[i]['width'] = metadata[video_name]['video_width']
                data[i]['frame_rate'] = metadata[video_name]['video_frame_rate']
                data[i]['bit_rate'] = metadata[video_name]['video_bitrate']
                data[i]['duration'] = metadata[video_name]['video_duration']
                data[i]['codec'] = metadata[video_name]['video_codec']
                # data[i]['codec'] = i.split('_')[-1].split('.')[0]  # nur bei test
                # data[i]['frame_rate'] = re.search('\d+.\d+fps', i).group()
                data[i]['resolution'] = re.search('\d+p', i).group()
                # data[i]['bit_rate'] = re.search('\d+kbps', i).group()
                # print(data[i]['bit_rate'])
                subs = re.sub(r"test\_\d/segments/|\_\d+kbps.+", "", i, flags=re.I)
                #print(site['page'] + '_' + video_name.split('.')[0] + '.jpg' )
                #print(site['page'] + '_' + os.path.splitext(video_name)[0] + '.jpg')
                # for s in site['thumbs']:
                #    result = re.search(subs, s)
                #    if result:
                data[i]['thumb'] = site['fold_thumbs'] + site['page'] + '_' + os.path.splitext(video_name)[0] + '.jpg'  # site['fold_thumbs']

                # data[i]['thumb'] = [y for y in thumbs if re.search(subs, y)][0] # not working anymore in python 3.8
                data[i]['filter_name'] = re.sub('[_]', ' ', subs)
                data[i]['name'] = re.sub('[_]', ' ', subs).title()
                data[i]['mos'] = mos_ci[video_name]['MOS']
                data[i]['ci'] = mos_ci[video_name]['CI']
        Website.Site = site
        Website.Data = data
        html = '''<!-- Videos -->
                <!DOCTYPE html>
                <html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
                '''
        website_obj = WebsiteFactory()
        html += website_obj.create_website('Head').html
        html += '''<!-- Body --><body>'''
        html += website_obj.create_website('Sidebar').html
        html += website_obj.create_website('Top').html
        html += '''<!-- !PAGE CONTENT! -->
                    <div class="w3-main w3-content w3-padding" id="videos" style="max-width:1200px;margin-top:100px">'''
        html += website_obj.create_website('Grid').html
        html += website_obj.create_website('Pagination').html
        html += website_obj.create_website('Footer').html
        html += '''</div>'''
        for i in site['bottom_js']:
            html += '''<script src="''' + i + '''"></script>'''
        html += '''</body><!-- END Body -->'''
        html += '''</html>'''
        return html

    def create_list_site(self):
        num = 5
        site = {
            'page': SITES[num],  # name for pagination
            'title': re.sub('[_]', ' ', SITES[num]).title(),  # title of website (for meta tag)
            'folder': './',  # where to dump the website
            'files': list(glob.glob('./../*.json')),  # list of  file path names to json location
            'css': ['./css/design.css', './css/listing.css'],  # list of  file path names to script location
            'top_js': [],  # list of  file path names to script location
            'bottom_js': ['./javascript/listing.js'],  # list of  file path names to script location
            'thumbs': None,  # get all the thumb names
            'fold_thumbs': None,  # store the folder of thumbs
            'fold_videos': 'test_' + str(num) + '/',  # where are the videos?
            'path': 'https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/',  # path to  videos?
            'metadata': None,
            'mos_ci': None,
            'objective_scores': None
        }
        # metadata = self.get_data(site['metadata'])
        # mos_ci = self.get_data(site['mos_ci'])
        # objective_scores = self.get_data(site['objective_scores'])
        data = {}
        if not site['files']:
            print('ERROR: no data')
        else:
            dat = []
            for j in site['files']:
                print(j)
                #j = '../' + j
                with open(j) as json_f:
                    # print(j)
                    dat += json.load(json_f)
            for i in dat:
                # print(i)
                data[i] = {}
                data[i]['path'] = i
                data[i]['file_ending'] = i.split('.')[-1]
                if 'src_videos' in i:
                    subs = re.sub(r"" + 'src_videos/' + "", "", i, flags=re.I).split('.')[0]
                    data[i]['filter_name'] = re.sub('[_]', ' ', subs)
                    data[i]['name'] = re.sub('[_]', ' ', subs).title()
                    pass
                else:
                    data[i]['codec'] = i.split('_')[-1].split('.')[0]  # nur bei test
                    # print(data[i]['codec'])
                    # print('Frame Rate: ', re.search('\d+.\d+fps', i).group())
                    data[i]['frame_rate'] = re.search('\d+.\d+fps', i).group()
                    data[i]['resolution'] = re.search('\d+p', i).group()
                    data[i]['bit_rate'] = re.search('\d+kbps', i).group()
                    subs = re.sub(r"test\_\d/segments/|\_\d+kbps.+", "", i, flags=re.I)
                    #for s in site['thumbs']:
                    #    result = re.search(subs, s)
                    #    if result:
                    #        data[i]['thumb'] = site['fold_thumbs'] + s
                        # data[i]['thumb'] = [y for y in thumbs if re.search(subs, y)][0] # not working anymore in python 3.8
                    data[i]['filter_name'] = re.sub('[_]', ' ', subs)
                    data[i]['name'] = re.sub('[_]', ' ', subs).title()
        Website.Site = site
        Website.Data = data
        html = '''<!-- Videos -->
                <!DOCTYPE html>
                <html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
                '''
        website_obj = WebsiteFactory()
        html += website_obj.create_website('Head').html
        html += '''<!-- Body --><body>'''
        html += website_obj.create_website('Sidebar').html
        html += website_obj.create_website('Top').html
        html += '''<!-- !PAGE CONTENT! -->
                    <div class="w3-main w3-content w3-padding" id="videos" style="max-width:1200px;margin-top:100px">'''
        html += website_obj.create_website('Listing').html
        html += website_obj.create_website('Pagination').html
        html += website_obj.create_website('Footer', flag = 1).html
        html += '''</div>'''
        for i in site['bottom_js']:
            html += '''<script src="''' + i + '''"></script>'''
        html += '''</body><!-- END Body -->'''
        html += '''</html>'''
        return html

    def create_source(self):
        site = {
            'page': SITES[0], # name for pagination
            'title': 'Source', # title of website (for meta tag)
            'folder': './', # where to dump the website
            'files': ['../src_videos.json'], # list of  file path names to json location
            'css': ['./css/design.css', './css/filter.css'], # list of  file path names to script location
            'top_js': [], # list of  file path names to script location
            'bottom_js': ['./javascript/filter.js'], # list of  file path names to script location
            'thumbs': os.listdir('./thumbs/new/'), # get all the thumb names
            'fold_thumbs': './thumbs/new/', # store the folder of thumbs
            'fold_videos': 'src_videos/', # where are the videos?
            'path': 'https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/',  # path to  videos?
            'metadata': None,
            'mos_ci': None,
            'objective_scores': None
        }
        data = {}
        if not site['files']:
            print('ERROR: no data')
        else:
            dat = []
            for j in site['files']:
                with open(j) as json_f:
                    dat += json.load(json_f)
            for i in dat:
                data[i] = {}
                data[i]['path'] = i
                data[i]['file_ending'] = i.split('.')[-1]
                subs = re.sub(r"" + site['fold_videos'] + "", "", i, flags=re.I).split('.')[0]
                #for s in site['thumbs']:
                #    result = re.search(subs, s)
                #    if result:
                #        data[i]['thumb'] = site['fold_thumbs'] + s
                video_name = re.sub(r"src_videos/", "", i, flags=re.I)
                # print(video_name)
                # print(site['fold_thumbs'] + 'src_videos_' + os.path.splitext(video_name)[0] + '.jpg')
                data[i]['thumb'] = site['fold_thumbs'] + 'src_videos_' + os.path.splitext(video_name)[0] + '.jpg'  # site['fold_thumbs']
                data[i]['filter_name'] = re.sub('[_]', ' ', subs)
                data[i]['name'] = re.sub('[_]', ' ', subs).title()
        Website.Site = site
        Website.Data = data
        html = '''<!-- Videos -->
        <!DOCTYPE html>
        <html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
        '''
        website_obj = WebsiteFactory()
        html += website_obj.create_website('Head').html
        html += '''<!-- Body --><body>'''
        html += website_obj.create_website('Sidebar').html
        html += website_obj.create_website('Top').html
        html += '''<!-- !PAGE CONTENT! -->
            <div class="w3-main w3-content w3-padding" id="videos" style="max-width:1200px;margin-top:100px">'''
        html += website_obj.create_website('Grid').html
        html += website_obj.create_website('Pagination').html
        html += website_obj.create_website('Footer').html
        html += '''</div>'''
        for i in site['bottom_js']:
            html += '''<script src="''' + i + '''"></script>'''
        html += '''</body><!-- END Body -->'''
        html += '''</html>'''
        return html

def main():
    source_obj = SourceFactory()
    f = open(SITES[0] + '.html', 'w+')
    f.write(source_obj.create_source())
    f.close()
    f = open(SITES[1] + '.html', 'w+')
    f.write(source_obj.create_test_site(1))
    f.close()
    f = open(SITES[2] + '.html', 'w+')
    f.write(source_obj.create_test_site(2))
    f.close()
    f = open(SITES[3] + '.html', 'w+')
    f.write(source_obj.create_test_site(3))
    f.close()
    f = open(SITES[4] + '.html', 'w+')
    f.write(source_obj.create_test_site(4))
    f.close()
    f = open(SITES[5] + '.html', 'w+')
    f.write(source_obj.create_list_site())
    f.close()

    # ="w3-tag w3-black w3-margin-bottom btn-small">Show all</span>

if __name__ == "__main__":
    main()
