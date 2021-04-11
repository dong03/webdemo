import web
import os
import json


cType = {"png":"images/png",
         "jpg":"images/jpeg",
         "jpeg":"images/jpeg",
         "gif":"images/gif",
         "ico":"images/x-icon"}

DEFAULT_EXT = 'jpg'


class images:
    def get_local(self, name):
        img_path = web.img2info[name]['img_path']
        #print (img_path)
        return img_path

    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension
        if name.find('.')<0:
            ext = DEFAULT_EXT
        imfile = self.get_local(name)
        try:
            web.header("Content-Type", cType[ext]) # Set the Header
            return open(imfile,"rb").read() # Notice 'rb' for reading images
        except:
            raise web.notfound()

class gradcams(images):
    def get_local(self, name):
        img_path = web.img2info[name]['gradcam']
        print (img_path)
        return img_path

class gradcampps(images):
    def get_local(self, name):
        img_path = web.img2info[name]['gradcampp']
        #print (img_path)
        return img_path

class test_img(images):
    def get_local(self, name):
        img_path = web.img2info[name]['test_img']
        #print (img_path)
        return img_path

class groundtruth(images):
    def get_local(self, name):
        img_path = web.img2info[name]['groundtruth']
        #print (img_path)
        return img_path

class crcnn_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['crcnn_448']
        #print (img_path)
        return img_path

class gsrnet_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['gsrnet_448']
        #print (img_path)
        return img_path

class mantranet448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mantranet448']
        #print (img_path)
        return img_path

class mvssnet_casiav2_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_casiav2_448']
        #print (img_path)
        return img_path

class mvssnet_defacto_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_defacto_448']
        #print (img_path)
        return img_path

class mvssnet_ps_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_ps_448']
        #print (img_path)
        return img_path

class mvssnet_fullset_448(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_ps_448']
        #print (img_path)
        return img_path


class crcnn_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['crcnn_512']
        # print (img_path)
        return img_path


class gsrnet_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['gsrnet_512']
        # print (img_path)
        return img_path


class mantranet512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mantranet512']
        # print (img_path)
        return img_path


class mvssnet_casiav2_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_casiav2_512']
        # print (img_path)
        return img_path


class mvssnet_defacto_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_defacto_512']
        # print (img_path)
        return img_path


class mvssnet_ps_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_ps_512']
        # print (img_path)
        return img_path


class mvssnet_fullset_512(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_fullset_512']
        # print (img_path)
        return img_path

class tampered(images):
    def get_local(self, name):
        img_path = web.img2info[name]['tampered']
        #print (img_path)
        return img_path

class ori(images):
    def get_local(self, name):
        img_path = web.img2info[name]['ori']
        return img_path

class seen(images):
    def get_local(self, name):
        img_path = web.img2info[name]['seen']
        return img_path

class seen_mask(images):
    def get_local(self, name):
        img_path = web.img2info[name]['seen_mask']
        return img_path

class unseen(images):
    def get_local(self, name):
        img_path = web.img2info[name]['unseen']
        return img_path

class unseen_mask(images):
    def get_local(self, name):
        img_path = web.img2info[name]['unseen_mask']
        return img_path

class mask(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mask']
        return img_path

class tradition(images):
    def get_local(self, name):
        img_path = web.img2info[name]['tradition']
        return img_path

class mvssnet_patch_casia(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_patch_casia']
        return img_path


class mvssnet_patch_defacto(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_patch_defacto']
        return img_path

class mvssnet_patch_fullset(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_patch_fullset']
        return img_path

class mvssnet_resize512_casia(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize512_casia']
        return img_path


class mvssnet_resize512_defacto(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize512_defacto']
        return img_path

class mvssnet_resize512_fullset(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize512_fullset']
        return img_path

class mvssnet_resize1024_casia(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize1024_casia']
        return img_path

class mvssnet_resize1024_defacto(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize1024_defacto']
        return img_path

class mvssnet_resize1024_fullset(images):
    def get_local(self, name):
        img_path = web.img2info[name]['mvssnet_resize1024_fullset']
        return img_path

class queryimages (images):
    def get_local(self, name):
        #print im2path(testCollection, name, True)
        return im2path(testCollection, name, True)
            
class bigimages (images):
    def get_local(self, name):
        return im2path(name, True)

            
if __name__ == '__main__':
    im = bigimages()
    im.GET('4362444639.jpg')

