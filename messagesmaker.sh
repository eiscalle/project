#!/bin/bash
need_compile=$1
modules=(auth home series subtitles settings)

for module in ${modules[*]}
do
    cd ${module};
    if [ "$need_compile" == "-c" ];
    then
        ../manage.py compilemessages
    else
        ../manage.py makemessages --all
    fi
    cd ..
done