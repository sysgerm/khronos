# Intro

```
 .S    S.    .S    S.    .S_sSSs      sSSs_sSSs     .S_sSSs      sSSs_sSSs      sSSs  
.SS    SS.  .SS    SS.  .SS~YS%%b    d%%SP~YS%%b   .SS~YS%%b    d%%SP~YS%%b    d%%SP  
S%S    S&S  S%S    S%S  S%S   `S%b  d%S'     `S%b  S%S   `S%b  d%S'     `S%b  d%S'    
S%S    d*S  S%S    S%S  S%S    S%S  S%S       S%S  S%S    S%S  S%S       S%S  S%|     
S&S   .S*S  S%S SSSS%S  S%S    d*S  S&S       S&S  S%S    S&S  S&S       S&S  S&S     
S&S_sdSSS   S&S  SSS&S  S&S   .S*S  S&S       S&S  S&S    S&S  S&S       S&S  Y&Ss    
S&S~YSSY%b  S&S    S&S  S&S_sdSSS   S&S       S&S  S&S    S&S  S&S       S&S  `S&&S   
S&S    `S%  S&S    S&S  S&S~YSY%b   S&S       S&S  S&S    S&S  S&S       S&S    `S*S  
S*S     S%  S*S    S*S  S*S   `S%b  S*b       d*S  S*S    S*S  S*b       d*S     l*S  
S*S     S&  S*S    S*S  S*S    S%S  S*S.     .S*S  S*S    S*S  S*S.     .S*S    .S*P  
S*S     S&  S*S    S*S  S*S    S&S   SSSbs_sdSSS   S*S    S*S   SSSbs_sdSSS   sSS*S   
S*S     SS  SSS    S*S  S*S    SSS    YSSP~YSSY    S*S    SSS    YSSP~YSSY    YSS'    
SP                 SP   SP                         SP                                 
Y                  Y    Y                          Y                                  
                                                                                      
```

Github enumeration tool written in python.

# Setup

1. Clone the repository 

```bash
git clone https://github.com/sysgerm/khronos.git
```

2. Install TOR

**Linux**

```bash
sudo apt install tor (debian)
sudo dnf install tor (fedora)
sudo pacman -S tor (arch)
```

3. Start tor service 

```bash
sudo service tor start
```

5. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

5. Run script

```bash
python3 khronos.py
```

You can verify that TOR is up and running by looking at the IP you are getting in your terminal output, if it is not your public IP, all is working good.

## FAQ

*I am getting rate limited, what should I do?*

You can get a new TOR IP address using the following command:

```bash
sudo service tor reload
```

## Optional

If you want to have your ouput stored somewhere, you can always input a webhook to redirect the data to.

### IMPORTANT 

**I am not responsible for any actions u take with this tool.**
