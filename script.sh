#!/bin/bash

# Faz o download das páginas de usuários

for i in {1..7}; do
    wget "https://atcoder.jp/ranking?contestType=algo&f.Affiliation=&f.BirthYearLowerBound=0&f.BirthYearUpperBound=9999&f.CompetitionsLowerBound=0&f.CompetitionsUpperBound=9999&f.Country=BR&f.HighestRatingLowerBound=0&f.HighestRatingUpperBound=9999&f.RatingLowerBound=0&f.RatingUpperBound=9999&f.UserScreenName=&f.WinsLowerBound=0&f.WinsUpperBound=9999&page=$i" -O $i.html

done

cat 1.html > data.html
rm 1.html
for i in {2..7}; do
    cat $i.html >> data.html
    rm $i.html
done
