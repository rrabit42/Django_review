# 먼저 현재 프로젝트 dir에 빈 data_mysql dir 생성하고
# cmd에서 할 때 프로젝트 위치로 cd 해야하는거 알지?

docker run ^
--rm -it ^
--publish 13306:3306 ^
--env MYSQL_DATABASE="askcompany_db" ^
--env MYSQL_ROOT_PASSWORD="qwer1234" ^
--volume %cd%\data_mysql:/var/lib/mysql ^
mysql:5