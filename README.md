Isoworlds
============
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


This script handling Isoworlds storage by tag system. Looping every server folders and every Isoworlds, checking name and handling tag.
Run this on the directory that contains your server folder.
Remote server folder path: /Isoworlds
Servers path: /servers

Run this on the directory that contains your server folders ( /servers/ in this case ).

Remote server folder path: /Isoworlds
| Tag        | Folder name | Description  |
| ------------- | ------------- | ------------- |
| `@PUSH` | `uuid-Isoworld@PUSH` | If a world has been inactive for 15 minutes, preparing for push process |
| `@PUSHED` | `uuid-Isoworld@PUSHED` | If a region folder of the world has been pushed on the remote server, not anymore on world folder |
| `@PUSHED@PULL` | `uuid-Isoworld@PUSHED@PULL` | A player wants to go to this Isoworld, preparing for pull process |
| `No tag` | `uuid-Isoworld` | When world is ready, we set the it to his original name  |

Sponge only: On server start, Isoworlds plugin will move every IsoWorld folder in Isoworlds-SAS folder to prevent the loading. Then it will rename every untagged Isoworlds with @PUSH TAG, then Isoworlds-SAS will push them.
So when a server starts, there is no Isoworld to save space.
