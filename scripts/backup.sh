 #!/bin/bash
#Purpose = Backup of Important Data
#Created on 17-1-2012
#Author = Hafiz Haider
#Version 1.0
#START
echo "$PWD"
TIME=`date +%b-%d-%y`            # This Command will add date in Backup File Name.
FILENAME=backup-$TIME.tar.gz    # Here i define Backup file name format.
SRCDIR="$(dirname $PWD)/wsgi/scouter"                  # Location of Important Data Directory (Source of backup).
DESDIR="$(dirname $PWD)/backups"            # Destination of backup file.
echo $SRCDIR
echo tar -cpzf "$DESDIR/$FILENAME" "$SRCDIR"
tar -cpzf "$DESDIR/$FILENAME" "$SRCDIR"
#END