#!/bin/bash

# Faz odownload das páginas de usuários

#All
link="https://atcoder.jp/ranking/all?contestType=algo&f.Affiliation=&f.BirthYearLowerBound=0&f.BirthYearUpperBound=9999&f.CompetitionsLowerBound=0&f.CompetitionsUpperBound=9999&f.Country=BR&f.HighestRatingLowerBound=0&f.HighestRatingUpperBound=9999&f.RatingLowerBound=0&f.RatingUpperBound=9999&f.UserScreenName=&f.WinsLowerBound=0&f.WinsUpperBound=9999&page="

#Active
#link="https://atcoder.jp/ranking?contestType=algo&f.Affiliation=&f.BirthYearLowerBound=0&f.BirthYearUpperBound=9999&f.CompetitionsLowerBound=0&f.CompetitionsUpperBound=9999&f.Country=BR&f.HighestRatingLowerBound=0&f.HighestRatingUpperBound=9999&f.RatingLowerBound=0&f.RatingUpperBound=9999&f.UserScreenName=&f.WinsLowerBound=0&f.WinsUpperBound=9999&page="

for i in {1..12}; do
    wget "$link$i" -O $i.html
done

cat 1.html > data.html
rm 1.html
for i in {2..12}; do
    cat $i.html >> data.html
    rm $i.html
done
