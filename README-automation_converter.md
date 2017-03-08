# ha
Home assistant has automation files in yaml that contain a description line that starts with  - alias.
Home assistant also has  group file that controls what is seen as a view or group on the front end.  That file uses the names described by 
alias for displaying them on the front end.  This script takes the automation file and parse out the alias line then formats it for the group
file.  It then copies the output to the clip board.
