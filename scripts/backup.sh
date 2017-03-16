 #!/bin/bash
#Purpose = Backup of Important Data
#Created on 17-1-2012
#Author = Hafiz Haider
#Version 1.0
#START
TIME=`date +%b-%d-%y`            # This Command will add date in Backup File Name.
FILENAME=backup-$TIME.tar.gz    # Here i define Backup file name format.
#THISDIR=$(dirname $PWD)
if [ -z ${OPENSHIFT_REPO_DIR+x} ]; then THISDIR=$(dirname $PWD); else THISDIR=$OPENSHIFT_REPO_DIR; fi
echo $THISDIR
SRCDIR=$THISDIR"/wsgi/scouter"                  # Location of Important Data Directory (Source of backup).
DESDIR=$THISDIR"/backups"            # Destination of backup file.
echo $SRCDIR
echo tar -cpzf "$DESDIR/$FILENAME" "$SRCDIR"
tar -cpzf "$DESDIR/$FILENAME" "$SRCDIR"
#END