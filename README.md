# TeslaMate 대한민국 수퍼차저 Geofence
## Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)
-->
## About TeslaMate 대한민국 수퍼차저 Geofence
<!--Wirte one paragraph of project description -->  
테슬라메이트에 등록하기 위한 SQL문들을 공유하는 리포입니다.
대한민국 수퍼차저만 다루고 있습니다.

## Overview
<!-- Write Overview about this project -->
**If you use this template, you can use this function**
- Issue Template
- Pull Request Template
- Commit Template
- Readme Template
- Contribute Template
- Pull Request Build Test(With Github Actions)

## Getting Started
**click `Use this template` and use this template!**
<!--
### Depencies
 Write about need to install the software and how to install them 
-->
### Installing
<!-- A step by step series of examples that tell you how to get a development 
env running

Say what the step will be

    Give the example

And repeat

    until finished
-->
1. 다음 명령어로 Teslamate DB에 접속 `$ docker exec -it teslamate_database psql -U teslamate`
2. 데이터베이스 이름이 다를 시, 다음 명령어로 조회 `$ docker ps` ex) db 이름 pi_database_1 -> `$ docker exec -it pi_database_1 psql -U teslamate `
3. 리포지토리의 supercharger_geofence.md 파일 내용을 복사하여 명령어 실행
<!--
## Deployment
 Add additional notes about how to deploy this on a live system
 -->
## Contributing
<!-- Write the way to contribute -->

## Authors
  - [ahndwon](https://github.com/ahndwon)

See also the list of [contributors](https://github.com/ahndwon/readmeTemplate/contributors)
who participated in this project.
<!--
## Used or Referenced Projects
 - [referenced Project](project link) - **LICENSE** - little-bit introduce
-->

## License

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
