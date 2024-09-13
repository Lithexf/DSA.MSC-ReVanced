New-ADUser -Name "Test User" -GivenName "Test" -Surname "User" -SamAccountName "testuser" -UserPrincipalName "testuser@production.awpe" -Path "OU=USERS,OU=IFIX,OU=PTS,OU=PRODUCTION,DC=PRODUCTION,DC=AWPE" -AccountPassword (ConvertTo-SecureString "HwsE1234" -AsPlainText -Force) -Enabled $true -EmployeeNumber 164773 -DisplayName "Test User"

$user = Get-ADUser -Filter {UserPrincipalName -eq "testuser@production.awpe" -and EmployeeNumber -eq "164773"}

Add-ADGroupMember -Identity "C_LYNX_K2_OPERATOR" -Members $user
Add-ADGroupMember -Identity "IFIX_Users" -Members $user
Add-ADGroupMember -Identity "FIX Application Feature - WorkSpace Runtime Exit" -Members $user
Add-ADGroupMember -Identity "FIX Application Feature - iFIX - System Shutdown" -Members $user
Add-ADGroupMember -Identity "FIX Application Feature - WorkSpace Runtime" -Members $user
Add-ADGroupMember -Identity "FIX Security Group - PTS_OPERATOR" -Members $user






