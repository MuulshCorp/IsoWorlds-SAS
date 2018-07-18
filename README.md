IsoWorlds
============
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


This script handling IsoWorlds storage by tag system. Looping every server folders and every IsoWorlds, checking name and handling tag.
Tags:
- No tag, ignore: uuid-IsoWorld
- @PUSH: uuid-IsoWorld@PUSH. IsoWorlds-SAS will detect start push process to remote server. IsoWorlds plugin added @PUSH tag on unload process after X minutes of inactivity.
- @PUSHED: uuid-IsoWorld@PUSHED. IsoWorlds-SAS pushed successfully, then deleted region folder and replaced @PUSH tag with @PUSHED tag.
- @PUSHED@PULL: uuid-IsoWorld@PUSHED@PULL. IsoWorlds-SAS will detect pull process from remote server and copy region folder from remote to local targeted IsoWorld folder. IsoWorlds plugin added @PULL task when a trusted player tried to go in this IsoWorld.
- @PULLED: uuid-IsoWorld@PUSHED@PULL. IsoWorlds-SAS pulled successfully, then replaced @PUSHED@PULL tag with @PULLED tag so the IsoWorlds plugin is able to detect a successfully pulled IsoWorld.
- No tag: uuid-IsoWorld, plugin deleted @PULLED tag and will load it on server.

On server start, IsoWorlds plugin will move every IsoWorld folder in ISOWORLDS-SAS FOLDER to prevent the loading. Then it will renamed every untagged IsoWorlds with @PUSH TAG, then IsoWorlds-SAS will push them.

