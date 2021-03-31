import os

class TextReader:
    def __init__(self, collection, rootpath=os.path.join(os.environ['HOME'], 'VisualSearch')):
        self.im2cap = {}
        cap_file = os.path.join(rootpath, collection, 'TextData', '%s.rawcaption.txt'%collection)
        for line in open(cap_file):
            img_id, rawcap = line.strip().split('\t', 1)
            self.im2cap[img_id] = rawcap
        print ('%s, %d captions' % (collection, len(self.im2cap)))

    def lookup(self, img_id):
        return self.im2cap[img_id]


if __name__ == '__main__':
    tr = TextReader('gcc11val', '/data/xirong/VisualSearch')
   
