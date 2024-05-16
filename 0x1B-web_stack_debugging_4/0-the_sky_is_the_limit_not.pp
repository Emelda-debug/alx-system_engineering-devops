#increase number of traffic on nginx server it can handle
#increase default ULIMIT
exec {'fix-for-nginx':
	#modify ULIMIT VALUE
	command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
	path    => '/usr/local/bin/:/bin/',
	}
#->
# Restart Nginx
exec { 'nginx-restart':
	command => '/etc/init.d/nginx restart'
	#specify path for init.d script
	path	=> '/etc/init.d/',
}

