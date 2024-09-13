$user = Get-ADUser -Filter {UserPrincipalName -eq "testuser@production.awpe" -and EmployeeNumber -eq "164773"}

# Reset the user's password
Set-ADAccountPassword -Identity $user -Reset -NewPassword (ConvertTo-SecureString "HwsE1234" -AsPlainText -Force)

# Require the user to change the password at next logon
Set-ADUser -Identity $user -ChangePasswordAtLogon $true

# Enable the user account if it's disabled
Enable-ADAccount -Identity $user
