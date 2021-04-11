import web
import os, sys, random
import json
import pickle
import pdb
from images import *

# )
# types = [
#     'ori','mask','tradition',
#     'mvssnet_patch_casia','mvssnet_patch_defacto','mvssnet_patch_fullset',
#     'mvssnet_resize512_casia','mvssnet_resize512_defacto','mvssnet_resize512_fullset',
#     'mvssnet_resize1024_casia','mvssnet_resize1024_defacto','mvssnet_resize1024_fullset'
# ]
# types = [
#     'tampered', 'ori', 'mask', 'tradition',
#     'mvssnet_patch_casia', 'mvssnet_patch_defacto', 'mvssnet_patch_fullset',
#     'mvssnet_resize512_casia', 'mvssnet_resize512_defacto', 'mvssnet_resize512_fullset',
#     'mvssnet_resize1024_casia', 'mvssnet_resize1024_defacto', 'mvssnet_resize1024_fullset'
# ]
types = ['ori','seen','seen_mask','unseen','unseen_mask']
# types = [
#     'test_img', 'groundtruth',
#     'crcnn_448', 'gsrnet_448', 'mantranet448','mvssnet_casiav2_448','mvssnet_defacto_448', 'mvssnet_ps_448', 'mvssnet_fullset_448',
#     'crcnn_512', 'gsrnet_512', 'mantranet512','mvssnet_casiav2_512','mvssnet_defacto_512', 'mvssnet_ps_512', 'mvssnet_fullset_512'
# ]
pickel_path = '/data_activate/dongchengbo/cocovdcb_ori_sen_unseen_mask.pkl'

urls = [
    '/', 'index',
    '/search', 'ImageSearch',
    '/img/(.*)', 'images']
for each in types:
    urls.append('/%s/(.*)' % each)
    urls.append(each)
print(urls)
render = web.template.render('templates/')
config = json.load(open('config.json'))

max_hits = config['max_hits']
anno_file = config['anno_file']
pred_file = config['pred_file']
with open(pickel_path,'rb') as f:
    img_ori_mask_pd = pickle.load(f)

class index:
    
    def GET(self):
        input = web.input(query=None)
        resp = {'status':0, 'hits':0, 'content': []}

        if not input.query or input.query == 'random':
            selected = random.sample(web.img2info.keys(), max_hits)
            content = []
            for x in selected:
                info = web.img2info[x]
                info['id'] = x
                info['gt'] = web.img2gt.get(x,-1)
                content.append(info)           
        else:
            resp['status'] = 1
            resp['query'] = input.query
            descend = input.query.startswith('pos')
            ranklist = [(img_id, info['score']) for (img_id, info) in web.img2info.items()]
            ranklist.sort(key=lambda v:v[1], reverse=descend)
            resp['hits'] = len(ranklist)
            ranklist = ranklist[:max_hits]
            
            content = []
            for img_id, score in ranklist:
                info = web.img2info[img_id]
                info['id'] = img_id
                info['gt'] = web.img2gt.get(img_id,-1)
                content.append(info)

                
        resp['content'] = content
        resp['config'] = config
        return render.index(resp)

class ImageSearch:
    def POST(self):
        input = web.input()
        raise web.seeother('/?query=%s' % input.query)


if __name__ == "__main__":
    app = web.application(urls, globals())

    web.img2info = {}
    
    pred_dir = os.path.split(pred_file)[0]
    gradcam_dir = os.path.join(pred_dir, 'gradcam')

    for img_ in img_ori_mask_pd:
        #img_id = os.path.split(img_)[1].split('.')[0]
        img_id = str(img_)
        temp = img_ori_mask_pd[img_]
        values = []
        keys = []
        for i in range(len(types)):
            values.append(temp[i])
            keys.append(types[i])
        web.img2info[img_id] = dict(zip(keys,values))

    web.img2gt = {}
    for img_ in img_ori_mask_pd:
        img_id = str(img_)
        web.img2gt[img_id] = 1
    print ('nr of images: {}'.format(len(web.img2info)))
    app.run()
