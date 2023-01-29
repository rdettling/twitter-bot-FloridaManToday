# Florida Man Twitter Bot Shell Script

#!/bin/sh

# Globals

FILE=floridaman.txt
DATE=$(date | cut -d ' ' -f2)
NUM=$(date | cut -d ' ' -f4)
# Functions

usage() {
    cat 1>&2 << EOF
Usage: $(basename $0)

EOF
    exit $1
}

all() {
    # if [ "$DATE" -eq "Jan" ]; then DATE=January
    # fi
    case $DATE in
        "Jan") DATE=January
        ;;
        "Feb") DATE=February
        ;;
        "Mar") DATE=March
        ;;
        "Apr") DATE=April
        ;;
        "Jun") DATE=June
        ;;
        "Jul") DATE=July
        ;;
        "Aug") DATE=August
        ;;
        "Sep") DATE=September
        ;;
        "Oct") DATE=October
        ;;
        "Nov") DATE=November
        ;;
        "Dec") DATE=December
        ;;
    esac
    HEADLINE=$(cat $FILE | grep "$DATE.* $NUM:" | cut -d ':' -f2,3)
    echo "Today ($DATE $NUM) in $HEADLINE"

}

# Filter Pipeline(s)
all
