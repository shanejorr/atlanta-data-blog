# Get student growth metric data and export to parquet

# 2023 CCRPI for school and state
# only the progress indicator by subject
progress_indicator_2023_all = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Accountability/CCRPI/Scoring%20by%20Component/2023%20CCRPI%20Scoring%20by%20Component_12_14_23.xlsx"
# aggregate of all CCRPI components
ccrpi_components_2023_all = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Accountability/CCRPI/Scoring%20by%20Component/2023%20CCRPI%20Scoring%20by%20Component_12_14_23.xlsx"

# Median student growth percentiles for end of course and end of grade
# school and state are in different files
sgp_2023_eoc_school = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Student%20Growth%20Model/End%20of%20Course/SGP_EOC_Aggs_School_Level_2023.xlsx"
sgp_2023_eog_school = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Student%20Growth%20Model/End%20of%20Grade/SGP_EOG_Aggs_School_Level_2023.xlsx"

sgp_2023_eoc_state = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Student%20Growth%20Model/End%20of%20Course/SGP_EOC_Aggs_State_Level_2023.xlsx"
sgp_2023_eog_state = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Student%20Growth%20Model/End%20of%20Grade/SGP_EOG_Aggs_State_Level_2023.xlsx"

# Georgia Milestones Assessment System (GMAS) EOC and EOG
gmas_eoc_2023_school = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Milestones/End%20of%20Course/Full-Year_2023_EOC-School_Level.xlsx"
gmas_eog_2023_school = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Milestones/End%20of%20Grade/Spring_2023_EOG-School_Level-All%20Grades.xlsx"

gmas_eoc_2023_state = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Milestones/End%20of%20Course/Full-Year_2023_EOC-System_Level.xlsx"
gmas_eog_2023_state = "https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Performance/Georgia%20Milestones/End%20of%20Grade/Spring_2023_EOG-State_Level-All%20Grades.xlsx"

# attendance
attendance_2023_all = 'https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Whole%20Child/Attendance%20Dashboard/Attendance%20Dashboard%20Data%20-%202023.xlsx'

# demographics
demo_free_lunch_2023_school = 'https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Demographics/Free%20Reduced%20Lunch/Free%20Reduced%20Lunch%20(FRL)%20Fiscal%20Year2023%20School.csv'
demo_race_2023_school = 'https://stgadoegidatadownloads.blob.core.windows.net/datadownloads/Student%20Demographics/Enrollment%20March/Gender%20Race%20Ethnicity/FTE%20Enrollment%20by%20Race_Ethnicity%20and%20Gender%20Fiscal%20Year2023-3%20School.csv'