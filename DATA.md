# Data fields

The figure input uses these named columns (column order is immaterial):
`PaperID`, `Year`, `C5`, `Citation_Count`, `hit`, `Reference_Count`, `Team_Size`, `Institution_Count`, `Country_Count`, `Title_Length`, `Atyp_10pct_Z`, `Novelty_percentile`, `Disruption`, `Disruption_percentile`, `RaoStirling`, `NIH_Count`, `NSF_Count`, `Patent_Count`, `Newsfeed_Count`, `Tweet_Count`, `NCT_Count`, `TeamAgeDiversity`, `Team_Diversity_Gini`, `TeamAgeMean`, `TeamAgeMax`, `TeamAgeMin`, `Reference_Age_Mean`, `Reference_Age_Std`, `FieldID`, `FieldName`, `FieldID2`, `FieldName2`, `JournalID`.

The regression input additionally uses `AvgPastPubs`, `Funding`, `TeamAgeMean2`, `TeamAgeDiversity2`, and `RaoStirling_percentile`, together with the named age, disruption, reference, citation, team, year, and field columns in the formulas. Squared terms and percentile definitions must match the prepared study data. Positive counts are required where a formula uses `log(count)` without adding 1.
