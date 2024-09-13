$FormatEnumerationLimit = -1
# Set default encoding for all cmdlets
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# Set console encoding
$OutputEncoding = [System.Console]::OutputEncoding = [System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
