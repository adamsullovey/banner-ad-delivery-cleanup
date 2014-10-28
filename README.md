clean-banner-add-delivery
=========================

A reoccuring task when finishing up a banner ad campaign is pulling the final .swf and backup images out of the project folders and getting them ready to zip up. Time to automate!

Assuming a directory structure like this:

<pre>
project
  ├───120x600
  │   ├───assets
  │   └───assets fr
  ├───468x60
  │   ├───assets
  │   └───assets fr
  └───620x286
      ├───assets
      └───assets fr
</pre>

where folders like 120x600 and the assets folder contain files like .fla, .swf, .jpg, .txt, and other stuff, running

`python delivery-cleanup.py`

copy the directory tree into a deliverables folder, and then try to delete the following:
 * anything that isn't a .swf, .jpg, .png
 * assets folders
 
The result is a deliverables folder with the same structure minus the working files and assets folders, ready to zip and send to whoever needs .swf files and backup images.

<pre>
project
  ├───120x600
  │   ├───assets
  │   └───assets fr
  ├───468x60
  │   ├───assets
  │   └───assets fr
  ├───620x286
  │   ├───assets
  │   └───assets fr
  ├───deliverables.zip
  └───deliverables
      ├───120x600
      ├───468x60
      └───620x286
</pre>
