@echo off
ctty nul

:: Update the diagnostics if necessary and remove the update packages if successful 
if not exist \diags\nul md \diags 
cd \diags  
if not exist ..\GUI.EXE goto MDM2
  echo Extracting updated GUI ...
  ..\GUI.EXE  -o > NUL
  if ERRORLEVEL 1 goto error
  del ..\GUI.EXE
:MDM2
 if not exist ..\MDM2.EXE goto MDM3
  echo Extracting updated MDM2 ...
  ..\MDM2.EXE -o > NUL
  if ERRORLEVEL 1 goto error
  del ..\MDM2.EXE
:MDM3
 if not exist ..\MDM3.EXE goto MDM4
  echo Extracting updated MDM3 ...
  ..\MDM3.EXE -o > NUL
  if ERRORLEVEL 1 goto error
  del ..\MDM3.EXE
:MDM4
 if not exist ..\MDM4.EXE goto MDM5
  echo Extracting updated MDM4 ...
  ..\MDM4.EXE -o > NUL
  if ERRORLEVEL 1 goto error
  del ..\MDM4.EXE
:MDM5
cd ..

:: Run DellDiag
cd \Diags
delldiag.com
:: Utility partition reboot
if exist reboot.com reboot 1
goto loop

:error
ctty con
cls
echo Error completing the diagnostics update! Reboot the 
echo computer then update the diagnostic partition again.

:loop
goto loop
