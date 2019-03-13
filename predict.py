Last login: Mon Mar  4 22:22:53 on ttys000
GIXdeMacBook-Pro:~ gix-thu$ ssh pi@0.tcp.ngrok.io -p14265
Warning: Permanently added the ECDSA host key for IP address '[18.216.53.253]:14265' to the list of known hosts.
pi@0.tcp.ngrok.io's password: 
Linux raspberrypi 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Mar  4 22:17:47 2019 from ::1
pi@raspberrypi:~ $ pip install azure-cognitiveservices-vision-customvision
Collecting azure-cognitiveservices-vision-customvision
  Downloading https://files.pythonhosted.org/packages/20/a4/869552805373199b1dc026c5317e9e936d2e0302e2c09636d917a89b9d2d/azure_cognitiveservices_vision_customvision-0.4.0-py2.py3-none-any.whl (93kB)
    100% |████████████████████████████████| 102kB 1.5MB/s 
Collecting azure-common~=1.1 (from azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/c3/f8/46248b201fd38b7e93c6da644e2fc3bc5a39118f253562751fd295a8cc77/azure_common-1.1.18-py2.py3-none-any.whl
Collecting azure-cognitiveservices-vision-nspkg; python_version < "3.0" (from azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/0f/45/0bbd380b5ff5802eb60598cc79777d21dbd04065fb703c145dc5a8d55b41/azure_cognitiveservices_vision_nspkg-3.0.1-py2-none-any.whl
Collecting msrest>=0.5.0 (from azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/eb/96/1cf56e4cfd221b7f6eb6ab096dc23b0d21361393f0784276531e49b0b2a1/msrest-0.6.4-py2.py3-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 1.6MB/s 
Collecting azure-nspkg; python_version < "3.0" (from azure-common~=1.1->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/c2/95/af354f2f415d250dafe26a5d94230558aa8cf733a9dcbf0d26cd61f5a9b8/azure_nspkg-3.0.2-py2-none-any.whl
Collecting azure-cognitiveservices-nspkg>=3.0.0 (from azure-cognitiveservices-vision-nspkg; python_version < "3.0"->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/95/1b/037d2b67baaac5fd218974d830944f0f3ec03de53d75d4a179f24e859e18/azure_cognitiveservices_nspkg-3.0.1-py2-none-any.whl
Collecting isodate>=0.6.0 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/9b/9f/b36f7774ff5ea8e428fdcfc4bb332c39ee5b9362ddd3d40d9516a55221b2/isodate-0.6.0-py2.py3-none-any.whl (45kB)
    100% |████████████████████████████████| 51kB 1.8MB/s 
Collecting enum34>=1.0.4; python_version < "3.4" (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
Collecting typing; python_version < "3.5" (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/cc/3e/29f92b7aeda5b078c86d14f550bf85cff809042e3429ace7af6193c3bc9f/typing-3.6.6-py2-none-any.whl
Collecting certifi>=2017.4.17 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/9f/e0/accfc1b56b57e9750eba272e24c4dddeac86852c2bebd1236674d7887e8a/certifi-2018.11.29-py2.py3-none-any.whl (154kB)
    100% |████████████████████████████████| 163kB 1.0MB/s 
Collecting requests-oauthlib>=0.5.0 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/c2/e2/9fd03d55ffb70fe51f587f20bcf407a6927eb121de86928b34d162f0b1ac/requests_oauthlib-1.2.0-py2.py3-none-any.whl
Collecting requests~=2.16 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl (57kB)
    100% |████████████████████████████████| 61kB 1.3MB/s 
Collecting six (from isodate>=0.6.0->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.5.0->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/16/95/699466b05b72b94a41f662dc9edf87fda4289e3602ecd42d27fcaddf7b56/oauthlib-3.0.1-py2.py3-none-any.whl (142kB)
    100% |████████████████████████████████| 143kB 1.2MB/s 
Collecting urllib3<1.25,>=1.21.1 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 122kB 1.2MB/s 
Collecting idna<2.9,>=2.5 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 1.6MB/s 
Collecting chardet<3.1.0,>=3.0.2 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% |████████████████████████████████| 143kB 1.1MB/s 
Installing collected packages: azure-nspkg, azure-common, azure-cognitiveservices-nspkg, azure-cognitiveservices-vision-nspkg, six, isodate, enum34, typing, certifi, oauthlib, urllib3, idna, chardet, requests, requests-oauthlib, msrest, azure-cognitiveservices-vision-customvision
Successfully installed azure-cognitiveservices-nspkg-3.0.1 azure-cognitiveservices-vision-customvision-0.4.0 azure-cognitiveservices-vision-nspkg-3.0.1 azure-common-1.1.18 azure-nspkg-3.0.2 certifi-2018.11.29 chardet-3.0.4 enum34-1.1.6 idna-2.8 isodate-0.6.0 msrest-0.6.4 oauthlib-3.0.1 requests-2.21.0 requests-oauthlib-1.2.0 six-1.12.0 typing-3.6.6 urllib3-1.24.1
pi@raspberrypi:~ $ python
Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named cv2
>>> import numpy
>>> from PIL import Image
>>> exit()
pi@raspberrypi:~ $ pip install opencv-python 
Collecting opencv-python
  Could not find a version that satisfies the requirement opencv-python (from versions: )
No matching distribution found for opencv-python
pi@raspberrypi:~ $ sudo pip install opencv-python 
Collecting opencv-python
  Could not find a version that satisfies the requirement opencv-python (from versions: )
No matching distribution found for opencv-python
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import PIL from Image
  File "<stdin>", line 1
    import PIL from Image
                  ^
SyntaxError: invalid syntax
>>> from PIL import Image
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/dist-packages/cv2/__init__.py", line 3, in <module>
    from .cv2 import *
ImportError: libcblas.so.3: cannot open shared object file: No such file or directory
>>> exit()
pi@raspberrypi:~ $ pip3 install azure-cognitiveservices-vision-customvision
Collecting azure-cognitiveservices-vision-customvision
  Using cached https://files.pythonhosted.org/packages/20/a4/869552805373199b1dc026c5317e9e936d2e0302e2c09636d917a89b9d2d/azure_cognitiveservices_vision_customvision-0.4.0-py2.py3-none-any.whl
Collecting msrest>=0.5.0 (from azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/eb/96/1cf56e4cfd221b7f6eb6ab096dc23b0d21361393f0784276531e49b0b2a1/msrest-0.6.4-py2.py3-none-any.whl
Collecting azure-common~=1.1 (from azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/c3/f8/46248b201fd38b7e93c6da644e2fc3bc5a39118f253562751fd295a8cc77/azure_common-1.1.18-py2.py3-none-any.whl
Collecting isodate>=0.6.0 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/9b/9f/b36f7774ff5ea8e428fdcfc4bb332c39ee5b9362ddd3d40d9516a55221b2/isodate-0.6.0-py2.py3-none-any.whl
Collecting requests~=2.16 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/9f/e0/accfc1b56b57e9750eba272e24c4dddeac86852c2bebd1236674d7887e8a/certifi-2018.11.29-py2.py3-none-any.whl
Collecting requests-oauthlib>=0.5.0 (from msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/c2/e2/9fd03d55ffb70fe51f587f20bcf407a6927eb121de86928b34d162f0b1ac/requests_oauthlib-1.2.0-py2.py3-none-any.whl
Collecting six (from isodate>=0.6.0->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting idna<2.9,>=2.5 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting urllib3<1.25,>=1.21.1 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.5.0->msrest>=0.5.0->azure-cognitiveservices-vision-customvision)
  Using cached https://files.pythonhosted.org/packages/16/95/699466b05b72b94a41f662dc9edf87fda4289e3602ecd42d27fcaddf7b56/oauthlib-3.0.1-py2.py3-none-any.whl
Installing collected packages: six, isodate, idna, urllib3, chardet, certifi, requests, oauthlib, requests-oauthlib, msrest, azure-common, azure-cognitiveservices-vision-customvision
Successfully installed azure-cognitiveservices-vision-customvision-0.4.0 azure-common-1.1.18 certifi-2018.11.29 chardet-3.0.4 idna-2.8 isodate-0.6.0 msrest-0.6.4 oauthlib-3.0.1 requests-2.21.0 requests-oauthlib-1.2.0 six-1.12.0 urllib3-1.24.1
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
>>> from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region
>>> from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/dist-packages/cv2/__init__.py", line 3, in <module>
    from .cv2 import *
ImportError: libcblas.so.3: cannot open shared object file: No such file or directory
>>> exit()
pi@raspberrypi:~ $ sudo apt-get install libcblas-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libcblas3 libf2c2
The following NEW packages will be installed:
  libcblas-dev libcblas3 libf2c2
0 upgraded, 3 newly installed, 0 to remove and 12 not upgraded.
Need to get 279 kB of archives.
After this operation, 1,032 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libf2c2 armhf 20130926-2 [108 kB]
Get:2 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libcblas3 armhf 3.2.1+dfsg-1 [84.3 kB]
Get:3 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libcblas-dev armhf 3.2.1+dfsg-1 [87.1 kB]
Fetched 279 kB in 1s (178 kB/s)         
Selecting previously unselected package libf2c2:armhf.
(Reading database ... 80858 files and directories currently installed.)
Preparing to unpack .../libf2c2_20130926-2_armhf.deb ...
Unpacking libf2c2:armhf (20130926-2) ...
Selecting previously unselected package libcblas3.
Preparing to unpack .../libcblas3_3.2.1+dfsg-1_armhf.deb ...
Unpacking libcblas3 (3.2.1+dfsg-1) ...
Selecting previously unselected package libcblas-dev.
Preparing to unpack .../libcblas-dev_3.2.1+dfsg-1_armhf.deb ...
Unpacking libcblas-dev (3.2.1+dfsg-1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Setting up libf2c2:armhf (20130926-2) ...
Setting up libcblas3 (3.2.1+dfsg-1) ...
Setting up libcblas-dev (3.2.1+dfsg-1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
pi@raspberrypi:~ $ sudo apt-get install libhdf5-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  hdf5-helpers libaec-dev libaec0 libhdf5-100 libhdf5-cpp-100 libjpeg-dev
  libjpeg62-turbo-dev libsz2
Suggested packages:
  libhdf5-doc
The following NEW packages will be installed:
  hdf5-helpers libaec-dev libaec0 libhdf5-100 libhdf5-cpp-100 libhdf5-dev
  libjpeg-dev libjpeg62-turbo-dev libsz2
0 upgraded, 9 newly installed, 0 to remove and 12 not upgraded.
Need to get 3,728 kB of archives.
After this operation, 13.3 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf hdf5-helpers armhf 1.10.0-patch1+docs-3+deb9u1 [36.0 kB]
Get:2 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libaec0 armhf 0.3.2-1 [19.4 kB]
Get:3 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libsz2 armhf 0.3.2-1 [5,836 B]
Get:4 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libhdf5-100 armhf 1.10.0-patch1+docs-3+deb9u1 [1,201 kB]
Get:5 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libhdf5-cpp-100 armhf 1.10.0-patch1+docs-3+deb9u1 [119 kB]
Get:6 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libjpeg62-turbo-dev armhf 1:1.5.1-2 [181 kB]
Get:7 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libjpeg-dev all 1:1.5.1-2 [56.1 kB]
Get:8 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libaec-dev armhf 0.3.2-1 [17.6 kB]
Get:9 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libhdf5-dev armhf 1.10.0-patch1+docs-3+deb9u1 [2,093 kB]
Fetched 3,728 kB in 4s (869 kB/s)      
Selecting previously unselected package hdf5-helpers.
(Reading database ... 80881 files and directories currently installed.)
Preparing to unpack .../0-hdf5-helpers_1.10.0-patch1+docs-3+deb9u1_armhf.deb ...
Unpacking hdf5-helpers (1.10.0-patch1+docs-3+deb9u1) ...
Selecting previously unselected package libaec0:armhf.
Preparing to unpack .../1-libaec0_0.3.2-1_armhf.deb ...
Unpacking libaec0:armhf (0.3.2-1) ...
Selecting previously unselected package libsz2:armhf.
Preparing to unpack .../2-libsz2_0.3.2-1_armhf.deb ...
Unpacking libsz2:armhf (0.3.2-1) ...
Selecting previously unselected package libhdf5-100:armhf.
Preparing to unpack .../3-libhdf5-100_1.10.0-patch1+docs-3+deb9u1_armhf.deb ...
Unpacking libhdf5-100:armhf (1.10.0-patch1+docs-3+deb9u1) ...
Selecting previously unselected package libhdf5-cpp-100:armhf.
Preparing to unpack .../4-libhdf5-cpp-100_1.10.0-patch1+docs-3+deb9u1_armhf.deb ...
Unpacking libhdf5-cpp-100:armhf (1.10.0-patch1+docs-3+deb9u1) ...
Selecting previously unselected package libjpeg62-turbo-dev:armhf.
Preparing to unpack .../5-libjpeg62-turbo-dev_1%3a1.5.1-2_armhf.deb ...
Unpacking libjpeg62-turbo-dev:armhf (1:1.5.1-2) ...
Selecting previously unselected package libjpeg-dev.
Preparing to unpack .../6-libjpeg-dev_1%3a1.5.1-2_all.deb ...
Unpacking libjpeg-dev (1:1.5.1-2) ...
Selecting previously unselected package libaec-dev:armhf.
Preparing to unpack .../7-libaec-dev_0.3.2-1_armhf.deb ...
Unpacking libaec-dev:armhf (0.3.2-1) ...
Selecting previously unselected package libhdf5-dev.
Preparing to unpack .../8-libhdf5-dev_1.10.0-patch1+docs-3+deb9u1_armhf.deb ...
Unpacking libhdf5-dev (1.10.0-patch1+docs-3+deb9u1) ...
Setting up libaec0:armhf (0.3.2-1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Processing triggers for man-db (2.7.6.1-2) ...
Setting up libjpeg62-turbo-dev:armhf (1:1.5.1-2) ...
Setting up hdf5-helpers (1.10.0-patch1+docs-3+deb9u1) ...
Setting up libsz2:armhf (0.3.2-1) ...
Setting up libhdf5-100:armhf (1.10.0-patch1+docs-3+deb9u1) ...
Setting up libaec-dev:armhf (0.3.2-1) ...
Setting up libjpeg-dev (1:1.5.1-2) ...
Setting up libhdf5-cpp-100:armhf (1.10.0-patch1+docs-3+deb9u1) ...
Setting up libhdf5-dev (1.10.0-patch1+docs-3+deb9u1) ...
update-alternatives: using /usr/lib/arm-linux-gnueabihf/pkgconfig/hdf5-serial.pc to provide /usr/lib/arm-linux-gnueabihf/pkgconfig/hdf5.pc (hdf5.pc) in auto mode
Processing triggers for libc-bin (2.24-11+deb9u4) ...
pi@raspberrypi:~ $ sudo apt-get install libhdf5-serial-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  libhdf5-serial-dev
0 upgraded, 1 newly installed, 0 to remove and 12 not upgraded.
Need to get 27.7 kB of archives.
After this operation, 37.9 kB of additional disk space will be used.
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libhdf5-serial-dev all 1.10.0-patch1+docs-3+deb9u1 [27.7 kB]
Fetched 27.7 kB in 0s (54.4 kB/s)       
Selecting previously unselected package libhdf5-serial-dev.
(Reading database ... 81105 files and directories currently installed.)
Preparing to unpack .../libhdf5-serial-dev_1.10.0-patch1+docs-3+deb9u1_all.deb ...
Unpacking libhdf5-serial-dev (1.10.0-patch1+docs-3+deb9u1) ...
Setting up libhdf5-serial-dev (1.10.0-patch1+docs-3+deb9u1) ...
pi@raspberrypi:~ $ sudo apt-get install libatlas-base-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  gfortran gfortran-6 libatlas-dev libatlas3-base libblas-dev
  libgfortran-6-dev
Suggested packages:
  gfortran-doc gfortran-6-doc libgfortran3-dbg libcoarrays-dev libblas-doc
  liblapack-doc liblapack-dev liblapack-doc-man
The following NEW packages will be installed:
  gfortran gfortran-6 libatlas-base-dev libatlas-dev libatlas3-base
  libblas-dev libgfortran-6-dev
0 upgraded, 7 newly installed, 0 to remove and 12 not upgraded.
Need to get 10.2 MB of archives.
After this operation, 48.4 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libgfortran-6-dev armhf 6.3.0-18+rpi1+deb9u1 [199 kB]
Get:2 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf gfortran-6 armhf 6.3.0-18+rpi1+deb9u1 [5,421 kB]
Get:3 http://raspbian.raspberrypi.org/raspbian stretch/main armhf gfortran armhf 4:6.3.0-4 [1,352 B]
Get:4 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libatlas3-base armhf 3.10.3-1+rpi1 [1,920 kB]
Get:5 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libblas-dev armhf 3.7.0-2 [114 kB]
Get:6 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libatlas-dev armhf 3.10.3-1+rpi1 [65.9 kB]
Get:7 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libatlas-base-dev armhf 3.10.3-1+rpi1 [2,528 kB]
Fetched 10.2 MB in 3s (2,897 kB/s)       
Selecting previously unselected package libgfortran-6-dev:armhf.
(Reading database ... 81110 files and directories currently installed.)
Preparing to unpack .../0-libgfortran-6-dev_6.3.0-18+rpi1+deb9u1_armhf.deb ...
Unpacking libgfortran-6-dev:armhf (6.3.0-18+rpi1+deb9u1) ...
Selecting previously unselected package gfortran-6.
Preparing to unpack .../1-gfortran-6_6.3.0-18+rpi1+deb9u1_armhf.deb ...
Unpacking gfortran-6 (6.3.0-18+rpi1+deb9u1) ...
Selecting previously unselected package gfortran.
Preparing to unpack .../2-gfortran_4%3a6.3.0-4_armhf.deb ...
Unpacking gfortran (4:6.3.0-4) ...
Selecting previously unselected package libatlas3-base.
Preparing to unpack .../3-libatlas3-base_3.10.3-1+rpi1_armhf.deb ...
Unpacking libatlas3-base (3.10.3-1+rpi1) ...
Selecting previously unselected package libblas-dev.
Preparing to unpack .../4-libblas-dev_3.7.0-2_armhf.deb ...
Unpacking libblas-dev (3.7.0-2) ...
Selecting previously unselected package libatlas-dev.
Preparing to unpack .../5-libatlas-dev_3.10.3-1+rpi1_armhf.deb ...
Unpacking libatlas-dev (3.10.3-1+rpi1) ...
Selecting previously unselected package libatlas-base-dev.
Preparing to unpack .../6-libatlas-base-dev_3.10.3-1+rpi1_armhf.deb ...
Unpacking libatlas-base-dev (3.10.3-1+rpi1) ...
Setting up libatlas3-base (3.10.3-1+rpi1) ...
update-alternatives: using /usr/lib/atlas-base/atlas/libblas.so.3 to provide /usr/lib/libblas.so.3 (libblas.so.3) in auto mode
update-alternatives: using /usr/lib/atlas-base/atlas/liblapack.so.3 to provide /usr/lib/liblapack.so.3 (liblapack.so.3) in auto mode
Setting up libgfortran-6-dev:armhf (6.3.0-18+rpi1+deb9u1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Processing triggers for man-db (2.7.6.1-2) ...
Setting up gfortran-6 (6.3.0-18+rpi1+deb9u1) ...
Setting up gfortran (4:6.3.0-4) ...
update-alternatives: using /usr/bin/gfortran to provide /usr/bin/f95 (f95) in auto mode
update-alternatives: using /usr/bin/gfortran to provide /usr/bin/f77 (f77) in auto mode
Setting up libblas-dev (3.7.0-2) ...
update-alternatives: using /usr/lib/libblas/libblas.so to provide /usr/lib/libblas.so (libblas.so) in auto mode
Setting up libatlas-dev (3.10.3-1+rpi1) ...
Setting up libatlas-base-dev (3.10.3-1+rpi1) ...
update-alternatives: using /usr/lib/atlas-base/atlas/libblas.so to provide /usr/lib/libblas.so (libblas.so) in auto mode
update-alternatives: using /usr/lib/atlas-base/atlas/liblapack.so to provide /usr/lib/liblapack.so (liblapack.so) in auto mode
pi@raspberrypi:~ $ sudo apt-get install libjasper-dev 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libjasper1
Suggested packages:
  libjasper-runtime
The following NEW packages will be installed:
  libjasper-dev libjasper1
0 upgraded, 2 newly installed, 0 to remove and 12 not upgraded.
Need to get 611 kB of archives.
After this operation, 1,207 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://raspbian-us.ngc292.space/raspbian stretch/main armhf libjasper1 armhf 1.900.1-debian1-2.4+deb8u1 [110 kB]
Get:2 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libjasper-dev armhf 1.900.1-debian1-2.4+deb8u1 [501 kB]
Fetched 611 kB in 1s (561 kB/s)                                          
Selecting previously unselected package libjasper1:armhf.
(Reading database ... 81366 files and directories currently installed.)
Preparing to unpack .../libjasper1_1.900.1-debian1-2.4+deb8u1_armhf.deb ...
Unpacking libjasper1:armhf (1.900.1-debian1-2.4+deb8u1) ...
Selecting previously unselected package libjasper-dev.
Preparing to unpack .../libjasper-dev_1.900.1-debian1-2.4+deb8u1_armhf.deb ...
Unpacking libjasper-dev (1.900.1-debian1-2.4+deb8u1) ...
Setting up libjasper1:armhf (1.900.1-debian1-2.4+deb8u1) ...
Setting up libjasper-dev (1.900.1-debian1-2.4+deb8u1) ...
pi@raspberrypi:~ $ sudo apt-get install libqtgui4 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libjpeg8 libmng1 libqt4-dbus libqt4-xml libqtcore4 libqtdbus4 qdbus
  qt-at-spi qtchooser qtcore4-l10n
Suggested packages:
  qt4-qtconfig
The following NEW packages will be installed:
  libjpeg8 libmng1 libqt4-dbus libqt4-xml libqtcore4 libqtdbus4 libqtgui4
  qdbus qt-at-spi qtchooser qtcore4-l10n
0 upgraded, 11 newly installed, 0 to remove and 12 not upgraded.
Need to get 6,239 kB of archives.
After this operation, 22.0 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libjpeg8 armhf 8d1-2 [108 kB]
Get:2 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libmng1 armhf 1.0.10+dfsg-3.1 [164 kB]
Get:3 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf qtcore4-l10n all 4:4.8.7+dfsg-11+rpi1 [662 kB]
Get:4 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqtcore4 armhf 4:4.8.7+dfsg-11+rpi1 [1,366 kB]
Get:5 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqt4-xml armhf 4:4.8.7+dfsg-11+rpi1 [126 kB]
Get:6 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqtdbus4 armhf 4:4.8.7+dfsg-11+rpi1 [193 kB]
Get:7 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf qtchooser armhf 63-g13a3d08-1 [21.9 kB]
Get:8 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf qdbus armhf 4:4.8.7+dfsg-11+rpi1 [72.2 kB]
Get:9 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqt4-dbus armhf 4:4.8.7+dfsg-11+rpi1 [52.8 kB]
Get:10 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqtgui4 armhf 4:4.8.7+dfsg-11+rpi1 [3,426 kB]
Get:11 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf qt-at-spi armhf 0.4.0-5 [47.4 kB]
Fetched 6,239 kB in 5s (1,232 kB/s)  
Selecting previously unselected package libjpeg8:armhf.
(Reading database ... 81399 files and directories currently installed.)
Preparing to unpack .../00-libjpeg8_8d1-2_armhf.deb ...
Unpacking libjpeg8:armhf (8d1-2) ...
Selecting previously unselected package libmng1:armhf.
Preparing to unpack .../01-libmng1_1.0.10+dfsg-3.1_armhf.deb ...
Unpacking libmng1:armhf (1.0.10+dfsg-3.1) ...
Selecting previously unselected package qtcore4-l10n.
Preparing to unpack .../02-qtcore4-l10n_4%3a4.8.7+dfsg-11+rpi1_all.deb ...
Unpacking qtcore4-l10n (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package libqtcore4:armhf.
Preparing to unpack .../03-libqtcore4_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqtcore4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package libqt4-xml:armhf.
Preparing to unpack .../04-libqt4-xml_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqt4-xml:armhf (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package libqtdbus4:armhf.
Preparing to unpack .../05-libqtdbus4_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqtdbus4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package qtchooser.
Preparing to unpack .../06-qtchooser_63-g13a3d08-1_armhf.deb ...
Unpacking qtchooser (63-g13a3d08-1) ...
Selecting previously unselected package qdbus.
Preparing to unpack .../07-qdbus_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking qdbus (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package libqt4-dbus:armhf.
Preparing to unpack .../08-libqt4-dbus_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqt4-dbus:armhf (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package libqtgui4:armhf.
Preparing to unpack .../09-libqtgui4_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqtgui4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Selecting previously unselected package qt-at-spi:armhf.
Preparing to unpack .../10-qt-at-spi_0.4.0-5_armhf.deb ...
Unpacking qt-at-spi:armhf (0.4.0-5) ...
Setting up qtcore4-l10n (4:4.8.7+dfsg-11+rpi1) ...
Setting up qtchooser (63-g13a3d08-1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Setting up libqtcore4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Processing triggers for man-db (2.7.6.1-2) ...
Setting up libqt4-xml:armhf (4:4.8.7+dfsg-11+rpi1) ...
Setting up libjpeg8:armhf (8d1-2) ...
Setting up libmng1:armhf (1.0.10+dfsg-3.1) ...
Setting up libqtdbus4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Setting up libqtgui4:armhf (4:4.8.7+dfsg-11+rpi1) ...
Setting up qdbus (4:4.8.7+dfsg-11+rpi1) ...
Setting up libqt4-dbus:armhf (4:4.8.7+dfsg-11+rpi1) ...
Setting up qt-at-spi:armhf (0.4.0-5) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
pi@raspberrypi:~ $ sudo apt-get install libqt4-test
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  vlc-plugin-notify vlc-plugin-samba vlc-plugin-video-splitter
  vlc-plugin-visualization
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  libqt4-test
0 upgraded, 1 newly installed, 0 to remove and 12 not upgraded.
Need to get 97.7 kB of archives.
After this operation, 248 kB of additional disk space will be used.
Get:1 http://mirror.web-ster.com/raspbian/raspbian stretch/main armhf libqt4-test armhf 4:4.8.7+dfsg-11+rpi1 [97.7 kB]
Fetched 97.7 kB in 0s (177 kB/s) 
Selecting previously unselected package libqt4-test:armhf.
(Reading database ... 81578 files and directories currently installed.)
Preparing to unpack .../libqt4-test_4%3a4.8.7+dfsg-11+rpi1_armhf.deb ...
Unpacking libqt4-test:armhf (4:4.8.7+dfsg-11+rpi1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
Setting up libqt4-test:armhf (4:4.8.7+dfsg-11+rpi1) ...
Processing triggers for libc-bin (2.24-11+deb9u4) ...
pi@raspberrypi:~ $ sudo pip3 install opencv-python
Requirement already satisfied: opencv-python in /usr/local/lib/python3.5/dist-packages
Requirement already satisfied: numpy>=1.12.1 in /usr/lib/python3/dist-packages (from opencv-python)
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> exit()
pi@raspberrypi:~ $ lsusb
Bus 001 Device 004: ID 0424:7800 Standard Microsystems Corp. 
Bus 001 Device 003: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
pi@raspberrypi:~ $ ls
Desktop    Music                                         Public
Documents  node-red-static                               Templates
Downloads  pic_9dfc36bf-7e14-4fdb-b7de-65f73c06b67c.jpg  Videos
MagPi      Pictures
pi@raspberrypi:~ $ cd Desktop/
pi@raspberrypi:~/Desktop $ vi predict.py

     print (obj_loc)
     strprint="Objects too close to the baby:"
     if "Baby" in obj:
             baby_index=obj.index('Baby')
             baby_loc=obj_loc[baby_index]
             for dist in obj_loc:
                 print (abs(baby_loc-dist))
          
                 if (abs(baby_loc-dist)<400 and abs(baby_loc-dist)>0):
                     strprint=strprint+ " "+ obj[obj_loc.index(dist)]
     print (strprint)
     cv2.imshow("response.jpg",im)
    
     fps = cap.get(cv2.CAP_PROP_FPS)
     print ("Frames per second using video.get(cv2.CAP_PROP_FPS): {0}".format(fps))
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"predict.py" [New File]
