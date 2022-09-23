#!/usr/bin/env python
from datetime import date
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
startYear = 2015
endYear = date.today().year
endMonth = date.today().month

kw_list = ["bitcoin"]
# weekly
pytrends.build_payload(kw_list, cat=0, timeframe='2015-01-01 2018-12-31', geo='', gprop='')
df = pytrends.interest_over_time().drop('isPartial',axis=1)
df.to_csv('./google_trend_weekly.csv')
# more than 5 years -> result monthly
pytrends.build_payload(kw_list, cat=0, timeframe=('2019-01-01 ' + date.today().strftime('%Y-%m-%d')), geo='', gprop='')
df = pytrends.interest_over_time().drop('isPartial',axis=1)
df.to_csv('./google_trend_weekly.csv', mode='a', header=False)

# daily
for i in range(endYear - startYear + 1):
    pytrends.build_payload(kw_list, cat=0,
     timeframe=(str(startYear + i) + '-01-01 '
     + str(startYear + i) + '-05-31'), geo='', gprop='')
    df = pytrends.interest_over_time().drop('isPartial',axis=1)
    df.to_csv('./google_trend_daily.csv', mode='a', header=False)
    # more than 8 months -> result weekly
    pytrends.build_payload(kw_list, cat=0,
     timeframe=(str(startYear + i) + '-06-01 '
     + str(startYear + i) + '-12-31'), geo='', gprop='')
    df = pytrends.interest_over_time().drop('isPartial',axis=1)
    df.to_csv('./google_trend_daily.csv', mode='a', header=False)
# this year
if endMonth > 6:
    pytrends.build_payload(kw_list, cat=0, timeframe=(str(endYear) + '-01-01 ' + str(endYear) + '-05-31'), geo='', gprop='')
    df = pytrends.interest_over_time().drop('isPartial',axis=1)
    df.to_csv('./google_trend_daily.csv', mode='a', header=False)
    pytrends.build_payload(kw_list, cat=0, timeframe=(str(endYear) + '-06-01 ' + date.today().strftime('%Y-%m-%d')), geo='', gprop='')
    df = pytrends.interest_over_time().drop('isPartial',axis=1)
    df.to_csv('./google_trend_daily.csv', mode='a', header=False)
else:
    pytrends.build_payload(kw_list, cat=0, timeframe=(str(endYear) + '-01-01 ' + date.today().strftime('%Y-%m-%d')), geo='', gprop='')
    df = pytrends.interest_over_time().drop('isPartial',axis=1)
    df.to_csv('./google_trend_daily.csv', mode='a', header=False)