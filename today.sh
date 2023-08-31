#!/usr/bin/env bash

today="$(date +%Y'W'%W'/'%m'-'%d)"
mkdir -p "${today}"
pushd "${today}"
for x in Lang Math English
do
    mkdir -p "${x}"
    pushd "${x}"
    touch README.md
    popd
done
popd
wk=${today%%/*}
md_wk="#### ${wk}"
mmdd=${today##*/}
for x in Lang Math English
do
    mkdir -p "${x}"
    touch "${x}/README.md"
    readme="${x}/README.md"
    grep -Fxq "${md_wk}" "${readme}"
    if [[ 1 -eq $(echo $?) ]]
    then
        echo >> "${readme}"
        echo "${md_wk}" >> "${readme}"
    fi
    md_today='- ['"${mmdd}"'](../'"${today}"'/'"${x}"'/README.md)'
    grep -Fxq -- "${md_today}" "${readme}"
    if [[ 1 -eq $(echo $?) ]]
    then
        echo "${md_today}" >> "${readme}"
    fi
done
