$source = "https://nodejs.org/dist/v15.14.0/node-v15.14.0-x64.msi"
cd .\Downloads
$destination = 'D:\Downloads\nodejs.msi'

Invoke-WebRequest -Uri $source -OutFile $destination

$destination


