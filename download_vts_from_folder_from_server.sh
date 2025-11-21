# !/bin/bash
#the following script is to download the entire folder from IES server

#IES server information
User="humaorong"
Host="140.109.81.186"

#path
remote_path="/scratch2/humaorong"
local_path="/drives/C/Users/carso/model_download_file"

#choose folder to download
echo "choose folders to download"
read  -a folder

#run scp to download folder
for folder in "${folder[@]}"
do
        #create folder at local
        mkdir -p "${local_path}/${folder}"
        scp -r  ${User}@${Host}:${remote_path}/${folder}/*.vts  ${local_path}/${folder}
done

echo "fininsh downloading vts files"
