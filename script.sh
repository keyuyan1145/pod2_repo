#!/bin/sh

# if [ $# -eq 0 ]
#   then
#     echo "Copying which file?"
#     exit 1
# fi

echo "Fetching from upstream"
git fetch upstream

echo "Merging changes"
git merge upstream/main --allow-unrelated-histories -m "merge with upstream"

echo "week_dir: "
read week_dir

echo "daily_dir: "
read daily_dir

student_folder=`ls -d */ | grep -v '^week'`

for f in $student_folder
do
    # student=${f::-1}
    # echo $student
    # cat ${folder_path}/${filename} "${f}${student}_${filename}"
    path=$f$week_dir
    echo $path
    [ ! -d $path ] && mkdir $path
    # mkdir "$path${daily_dir}"
    cp -r $week_dir$daily_dir $path${daily_dir}
    # mv "${f}${file}" "${f}${student}_${file}"
done


# echo "Pushing challenges to pod repo"
# git add *
# commit_msg="challenge folder added for ${week_dir}${daily_dir}"
# git commit -m commit_msg
# git push
