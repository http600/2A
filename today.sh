#!/usr/bin/env bash
off=0
if [[ $# -gt 0 ]]; then
    off=$1
fi
today="$(date -r $(($(date +%s) + $off * 86400)) +%Y'W'%W'/'%m'-'%d)"
mkdir -p "${today}"
pushd "${today}"
touch "README.md"
for x in Lang Math English; do
    mkdir -p "${x}"
    pushd "${x}"
    touch README.md
    popd
done
popd
wk=${today%%/*}
touch "${wk}/README.md"
md_wk="#### ${wk}"
mmdd=${today##*/}
for x in Lang Math English; do
    mkdir -p "${x}"
    readme="${x}/README.md"
    touch "${readme}"
    grep -Fxq "${md_wk}" "${readme}"
    if [[ 1 -eq $(echo $?) ]]; then
        echo >>"${readme}"
        echo "${md_wk}" >>"${readme}"
    fi
    md_today='- ['"${mmdd}"'](../'"${today}"'/'"${x}"'/README.md)'
    grep -Fxq -- "${md_today}" "${readme}"
    if [[ 1 -eq $(echo $?) ]]; then
        echo "${md_today}" >>"${readme}"
    fi
done
