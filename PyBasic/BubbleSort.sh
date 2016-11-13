#!/bin/bash
array=(12 5 13 8 9 65)
# paramaters[] -> list[]
bubble(){
  list=("$@")
  local size=$((${#list[@]}-1)) i sorted=0 t
  until ((sorted)); do
  sorted=1
    for ((i=0;i<size;i++)); do
      if ((list[i] > list[i+1])); then
        sorted=0;
        t=${list[i]} list[i]=${list[i+1]} list[i+1]=$t
      fi
    done
  done
}
bubble "${array[@]}"
echo ${list[@]}