# ๐ TeslaMate ๋ํ๋ฏผ๊ตญ ์ํผ์ฐจ์  Geofence โก๏ธ
<img src="./images/my_baby.PNG" height="400"></img>   
## ๐ Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)
-->
<br/><br/>

## ๐ About TeslaMate ๋ํ๋ฏผ๊ตญ ์ํผ์ฐจ์  Geofence
<!--Wirte one paragraph of project description -->  
ํ์ฌ๋ผ๋ฉ์ดํธ์ ๋ฑ๋กํ๊ธฐ ์ํ SQL๋ฌธ๋ค์ ๊ณต์ ํ๋ ๋ฆฌํฌ์๋๋ค.

๋ํ๋ฏผ๊ตญ ์ํผ์ฐจ์ ๋ง ๋ค๋ฃจ๊ณ  ์์ต๋๋ค.
<br/><br/><br/><br/>

## ๐ฅ Overview
๊ธฐ๋ณธ์ ์ผ๋ก ํ์ฌ๋ผ๋ฉ์ดํธ์๋ ์ํผ์ฐจ์  geofence๋ค์ด ๋ฑ๋ก๋์ด ์์ง ์์

์ผ์ผํ ๋ฑ๋กํด์ค์ผ ํ๋๋ฐ ํธํ๊ธฐ ํ๊ธฐ ์ํด SQL๋ฌธ์ ํตํด์๋ ๋ฑ๋กํ  ์ ์์ต๋๋ค.

์ํผ์ฐจ์  ์๊ฒฝ๋๋ ๊ตฌ๊ธ๋งต์์ ํ์ฌ๋ผ ๊ณตํ ์ํผ์ฐจ์ง ์ง๋์์ ์์น๋ฅผ ๋์กฐํ์ฌ ์ง์  ์๊ฒฝ๋๋ฅผ ์ถ์ถํ์ต๋๋ค.

๋ฐ๋ผ์ **์ค์ฐจ๊ฐ ์์ ์ ์์ผ๋ฏ๋ก ์ค์ฐจ ๋ฐ๊ฒฌ ์, ์ด์ ๋ถํ๋๋ ค์.**
<br/><br/><br/><br/>

## ๐Getting Started
**๋จผ์  ํ์ฌ๋ผ๋ฉ์ดํธ๊ฐ ํ์ํฉ๋๋ค!**
<br/><br/>

### ๐จ Installing
1. ๋ค์ ๋ช๋ น์ด๋ก Teslamate DB์ ์ ์  <br/>
`$ docker exec -it teslamate_database psql -U teslamate`

2. ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ด๋ฆ์ด ๋ค๋ฅผ ์, ๋ค์ ๋ช๋ น์ด๋ก ์กฐํ `$ docker ps` <br/>
 ex) db ์ด๋ฆ pi_database_1 -> `$ docker exec -it pi_database_1 psql -U teslamate `
 
3. ์ถํ ์ ๊ท ์ํผ์ฐจ์  ์ถ๊ฐ๋ฅผ ์ํ Table ์ name column Unique ์ค์ 
```
ALTER TABLE public.geofences
ADD CONSTRAINT name_unique UNIQUE (name);
```

4. ์ต์  [Release](https://github.com/ahndwon/teslamate-korea-supercharger-geofence/releases) ์ `supercharger_geofence_<YY-mm-dd>.md` ํ์ผ ๋ด์ฉ์ ๋ณต์ฌํ์ฌ ๋ช๋ น์ด ์คํ
<br/><br/>
๋ง์ฝ, ์๋์ ๊ฐ์ ์๋ฌ ๋ฐ์ ์, 
```
ERROR:  numeric field overflow
DETAIL:  A field with precision 6, scale 4 must round to an absolute value less than 10^2.
```

์๋ ALTER๋ฌธ์ ์คํํด์ฃผ์ธ์
```
ALTER TABLE charging_processes ALTER COLUMN cost TYPE numeric(8,2);
ALTER TABLE geofences ALTER COLUMN cost_per_unit TYPE numeric(7,4);
```
<br/><br/>

5. ์ถ๊ฐ๊ฐ ์ ๋์๋์ง ํ์ธ์ ์ํด์ , ๋ค์ ๋ช๋ น์ด ์คํ  <br/>
`$ SELECT * FROM geofences;`

6. ์ญ์  ํ๊ณ  ์ถ์ ์ง์คํ์ค๊ฐ ์๋ ๊ฒฝ์ฐ, ์ํ๋ ID๋ก ๋ค์ ๋ช๋ น์ด ์คํ  <br/>
`$ DELETE FROM geofences WHERE id = XX;`
 <br/><br/>
 #### ๐ ์ถ๊ฐ๋ Geofences
 <img src="./images/geofences_added.png" height="500"></img>   
 <br/><br/>
 
 
## ๐ฃ Roadmap
- [ ] ์๋ฐ์ดํธ ์๋ํ
- [ ] V2, V3 ๊ตฌ๋ถ์ ๋ฐ๋ฅธ ์ถฉ์  ์๊ธ ๊ณ์ฐ
- [ ] ๋ฐฐํฌ ์๋ํ
- [ ] multi region ์ง์
 <br/><br/>
 
## ๐ซ๐ซ Contributing
<!-- Write the way to contribute -->

## โ๏ธ Authors
  - [ahndwon](https://github.com/ahndwon)

See also the list of [contributors](https://github.com/ahndwon/teslamate-korea-supercharger-geofence/graphs/contributors)
who participated in this project.
<!--
## Used or Referenced Projects
 - [referenced Project](project link) - **LICENSE** - little-bit introduce
-->

## ๐ License

```
MIT License

Copyright (c) 2020 always0ne

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
