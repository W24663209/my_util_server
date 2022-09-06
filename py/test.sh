starttime=`date +'%Y-%m-%d %H:%M:%S'`
/usr/bin/svn checkout svn://120.77.15.218/project/parkinglock-master --username=wzt --password=wzt123456 .
/home/soft/maven/apache-maven-3.8.6/bin/mvn clean package -Dmaven.test.skip -P test
mv /tmp/parkinglock/parkinglock-quartz/target/parkinglock-quartz.jar /home/parkinglock/quartz
cd /home/parkinglock/quartz
ps x | grep java | grep parkinglock-quartz | grep -v grep | awk '{print $1}'|xargs -r kill -9
mv debug* backLog/
build_time=$(date +%Y%m%d_%H%M)
java -jar parkinglock-quartz.jar > debug_$build_time.log 2>&1 &
python3 /home/tail.py debug_$build_time.log
endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo $starttime   $endtime
start_seconds=$(date --date="$starttime" +%s);
end_seconds=$(date --date="$endtime" +%s);
echo "本次运行时间： "$((end_seconds-start_seconds))"s"