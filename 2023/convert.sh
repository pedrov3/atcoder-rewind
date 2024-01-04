for i in *.svg; do
    name=${i%.svg}
    svgexport $i $name.png 1024:1024
    #inkscape -w 1024 -h 1024 $i -o $name.jpg
done

