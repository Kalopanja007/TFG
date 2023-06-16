#!/bin/bash

for i in {1..100}
do
	echo ${i}
	#docker run --rm --name BORRAR_$i --network dev_ops_tfg_default base_img_borrar sh -c "sudo chmod a+r /BORRAR && scp /BORRAR parent:~/BORRAR_${i}" &
	docker run --rm --name BORRAR_$i --network dev_ops_tfg_default base_img_borrar sh -c "scp ../BORRAR parent:./BORRAR_${i}" &
	#docker run --rm --name BORRAR_$i --network dev_ops_tfg_default base_img_borrar sh -c "scp /bash_n_ssh.sh parent:~/BORRAR_${i}" &

done
