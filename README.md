IsoWorlds
============
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


This script handling IsoWorlds storage by tag system. Looping every server folders and every IsoWorlds, checking name and handling tag.

| Tag        | Folder name | Description  |
| ------------- | ------------- | ------------- |
| `@PUSH` | `uuid-Isoworld@PUSH` | If a world has been inactive for 15 minutes, preparing for push process |
| `@PUSHED` | `uuid-Isoworld@PUSHED` | If a region folder of the world has been pushed on the remote server, not anymore on world folder |
| `@PUSHED@PULL` | `uuid-Isoworld@PUSHED@PULL` | A player wants to go to this Isoworld, preparing for pull process |
| `No tag` | `uuid-Isoworld` | When world is ready, we set the it to his original name  |

On server start, IsoWorlds plugin will move every IsoWorld folder in ISOWORLDS-SAS FOLDER to prevent the loading. Then it will rename every untagged IsoWorlds with @PUSH TAG, then IsoWorlds-SAS will push them.
