@echo off 
set nombre=%1
set anio=%date:~6,4%
set mes=%date:~3,2%
set dia=%date:~0,2%
set hora=%time:~0,8% 
@echo off 
set nombre=%1
"C:\Program Files (x86)\Irdeto Access\PIsys\Apps\SecureClientReporter.exe" 2 "\\172.16.126.193/shared/"%nombre%%anio%-%mes%-%dia%%hora%".txt" 1 1 f l /q
pause
exit