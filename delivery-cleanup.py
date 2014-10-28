#!/usr/bin/python

# this script copies the working folders and removes files not needed for final delivery

import os
import sys
import shutil

def scandirs(path):

	# this will be the new folder that working files are copied to
	deliverables_path = os.path.join(path, 'deliverables')
	archive_file_name = 'deliverables'
	archive_type = 'zip'

	# try to deliverables path if it exists already
	try:
		shutil.rmtree(deliverables_path)

	except FileNotFoundError:
		print("could not delete " + deliverables_path)

	# copy working files
	shutil.copytree(path, deliverables_path)

	print("copied to " + deliverables_path)

	# now delete junk
	for root, dirs, files in os.walk(deliverables_path):

		for currentFile in files:
			exts=('.swf', '.jpg', '.png')
			if not any(currentFile.lower().endswith(ext) for ext in exts):
				path = os.path.join(root, currentFile)
				print("delete file: " + path)
				os.remove(path)

		for currentDir in dirs:
			if "assets" in currentDir:
				print("delete dir: " + currentDir)
				shutil.rmtree(os.path.join(root, currentDir))

	# zip up the new folder
	shutil.make_archive(archive_file_name, archive_type, deliverables_path)


scandirs('./')
