#/bin/sh

for x in $@
do
    echo $x
    base=${x%.tiff}
    #echo $base
    tiff2ps -e $x > "$base.eps"
done