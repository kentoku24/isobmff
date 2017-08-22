#!/usr/bin/env python
# -*- coding: utf-8 -*-
import isobmff

"""
ftyp
meta
  hdlr
  dinf
    dref
  iloc
  iinf
  pitm
"""
if __name__ == "__main__":
    media_file = isobmff.MediaFile()
    #media_file.read('autumn_1440x960.heic')
    #media_file.read('cheers_1440x960.heic')
    media_file.read('C001.heic')
    print(media_file)
