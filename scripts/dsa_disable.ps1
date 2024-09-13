$user = Get-ADUser -Filter {UserPrincipalName -eq "testuser@production.awpe" -and EmployeeNumber -eq "164773"}

Set-ADUser -Identity $user -Enabled $false