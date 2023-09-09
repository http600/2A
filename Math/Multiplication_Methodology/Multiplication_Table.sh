#!/usr/bin/env bash
echo '$$'
echo '\begin{align*}'
for i in {1..9}
do
    for ((j = 1; j <= i; ++j)) {
        echo -n "    ${j}"'{\times}'"${i}"' & = '"$((j * i)) & "
    }
    echo -n '\\';
    echo;
done;
echo '\end{align*}'
echo '$$'
