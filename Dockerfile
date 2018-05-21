FROM centos/systemd

RUN http_proxy="http://reformmgmtproxyout.reform.hmcts.net:8080/" yum -y update
RUN http_proxy="http://reformmgmtproxyout.reform.hmcts.net:8080/" yum -y install systemd-sysv iproute sudo; yum clean all;
