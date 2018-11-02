for D in `find $1  -mindepth 1 -type f`
do
    FILE=$(basename $D)
    NOEXT="${FILE%%.*}"
    python yolo_video.py --input $1/$FILE --output $2/$NOEXT.avi --boxes $3/$NOEXT.npy --show_output
done
