import os, getpass

from shutil import move


user  = getpass.getuser()

root_dir  = '/Users/{}/Downloads/'.format(user)
compr_dir = '/Users/{}/Downloads/Compressed/'.format(user)
img_dir   = '/Users/{}/Downloads/Images/'.format(user)
vid_dir   = '/Users/{}/Downloads/Video/'.format(user)
music_dir = '/Users/{}/Downloads/Music/'.format(user)
doc_dir   = '/Users/{}/Downloads/Documents/'.format(user)
dev_dir   = '/Users/{}/Downloads/Dev_docs/'.format(user)
apk_dir   = '/Users/{}/Downloads/apk/'.format(user)
soft_dir  = '/Users/{}/Downloads/Programs/'.format(user)
others_dir= '/Users/{}/Downloads/Autres/'.format(user)


# extensions 
compr_type = ('.zip', '.rar')
img_type   = ('.svg','.png', '.jpeg', '.jpg' )
vid_type   = ('.avi', '.mp4', '.ts', '.mov')
music_type = ('.mp3')
doc_type   = ('DOC','txt', '.docx', '.xls', '.xlsx' ,'.pdf', '.doc', '.pptx', '.ppt')
dev_type   = ('.py', '.json', '.js', '.css', '.html','.jar')
apk_type   = ('.apk', '.xapk')
soft_type  = ('.exe', '.msi', '.dmg')

def getFiles(r):
	return [f for f in os.listdir(r) if os.path.isfile(r+f) and not f.__eq__(__file__)]

def movesFiles(files):
	
	for f in files:
		f1= root_dir+f
		
		if f.endswith(compr_type):
			try:
				move(f1, '{}/{}'.format(compr_dir, f))
				print("Fichier {} deplacé vers {}".format(f, compr_dir))
			except:
				pass
		elif f.endswith(img_type):
			try:
				move(f1, '{}/{}'.format(img_dir, f))
				print("Fichier {} deplacé vers {}".format(f, img_dir))
			except:
				pass
		elif f.endswith(vid_type):
			try:
				move(f1, '{}/{}'.format(vid_dir, f))
				print("Fichier {} deplacé vers {}".format(f, vid_dir))
			except:
				pass
		elif f.endswith(music_type):
			try:
				move(f1, '{}/{}'.format(music_dir, f))
				print("Fichier {} deplacé vers {}".format(f, music_dir))
			except:
				pass
		elif f.endswith(doc_type):
			try:
				move(f1, '{}/{}'.format(doc_dir, f))
				print("Fichier {} deplacé vers {}".format(f, doc_dir))
			except:
				pass
		elif f.endswith(dev_type):
			try:
				move(f1, '{}/{}'.format(dev_dir, f))
				print("Fichier {} deplacé vers {}".format(f, dev_dir))
			except:
				pass
		elif f.endswith(apk_type):
			try:	
				move(f1, '{}/{}'.format(apk_dir, f))
				print("Fichier {} deplacé vers {}".format(f, apk_dir))
			except:
				pass
		elif f.endswith(soft_type):
			try:
				move(f1, '{}/{}'.format(soft_dir, f))
				print("Fichier {} deplacé vers {}".format(f, soft_dir))
			except:
				pass
		else:
			try:
				move(f1, '{}/{}'.format(others_dir, f))
				print("Fichier {} deplacé vers {}".format(f, others_dir))
			except:
				pass


if __name__=="__main__":
	files = getFiles(root_dir)
	movesFiles(files)


