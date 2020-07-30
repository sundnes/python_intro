#visit all folders and run all py-files
#creates a few plots that must be closed,
#and gives errors for files that need command-line
#arguments, but useful to check that things work

for folder in chapter*
do
  echo 'Running files in' $folder ':'
  cd $folder
  for file in *.py
  do
    echo $file ':'
    python $file
  done
  cd ..
done
