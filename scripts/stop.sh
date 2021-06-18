kill $(ps aux | grep 'sudo python3' | grep '[0-9]*' -o | head -1)
