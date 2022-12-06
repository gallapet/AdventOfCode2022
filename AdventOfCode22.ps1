$day = Read-host "What day are you on?"

New-Item -Path "Day$day" -ItemType Directory
New-Item -Path ".\Day$day\sample.txt" -ItemType File
New-Item -Path ".\Day$day\inputDay$day.txt" -ItemType File

Copy-Item "template.py" -Destination ".\Day$day"
Rename-Item ".\Day$day\template.py" "day$day.py"

(Get-Content -Path ".\Day$day\day$day.py" -Raw) -replace 'inputDayX.txt', "inputDay$day.txt" | Set-Content -Path ".\Day$day\day$day.py"