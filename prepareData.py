import pandas as pd
import numpy as np

universityDataRawDf = pd.read_csv('./universities_data_raw.csv')
universityRankingDf = pd.read_json('./universities_ranking.json')

universityRankingDf = universityRankingDf[universityRankingDf['location'] == 'United States']
universityRankingDf = universityRankingDf[['rank', 'name']]
universityRankingDf = universityRankingDf.rename(columns={'rank': 'Ranking', 'name': 'Name'})

universityDataDf = universityDataRawDf.merge(universityRankingDf, on='Name', how='left')

print(universityDataDf.shape)

universityDataDf['Ranking'] = universityDataDf['Ranking'].fillna('1501+')
universityDataDf['Ranking'] = universityDataDf.apply(lambda x: x['Ranking'].replace('=', ''), axis=1)
universityDataDf['Ranking display'] = np.where(universityDataDf['Ranking'] == '1501+', '1500+', 'top 1500')

universityDataDf = universityDataDf[[
                    'Name', 'Ranking', 'Ranking display', 'Applicants total', 'Admissions total',
                    'Enrolled total', 'Tuition and fees, 2013-14', 'Control of institution',
                    'Total price for in-state students living on campus 2013-14',
                    'Total price for out-of-state students living on campus 2013-14']]

universityDataDf = universityDataDf.rename(columns={'Tuition and fees, 2013-14': 'Tuition and fees',
                   'Total price for in-state students living on campus 2013-14':
                   'Total price for in-state students living on campus',
                   'Total price for out-of-state students living on campus 2013-14':
                   'Total price for out-of-state students living on campus'})
           
print(universityDataDf.shape)
print(universityDataDf['Ranking display'].unique())
print(universityDataDf['Ranking display'].value_counts())
universityDataDf.to_csv('./university_data.csv', index=False)

