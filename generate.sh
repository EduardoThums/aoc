#!/usr/bin/env bash

YEAR=${1:?"missing year param"}
DAY=${2:?"missing day"}

mkdir -p "$YEAR"
mkdir -p "$YEAR/day$DAY"

cp base.py "$YEAR/day$DAY/part_1.py"
