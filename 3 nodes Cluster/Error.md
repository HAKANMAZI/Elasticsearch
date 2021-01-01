Error 1) {"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}},"status":401}
Solved 1) there is no password 

Error 2) 
- cluster.initial_master_nodes: ["master1"]  doğru
- cluster.initial_master_nodes: ["master-1"] yanlış

Error 3)  
What is the default Username and Password for ElasticSearch 7.4.2 (when x-pack enabled)?
* bin/elasticsearch-setup-passwords interactive
* bin/elasticsearch-setup-passwords auto

Error 4) data1
java.lang.IllegalArgumentException: unknown setting [cluster.inital_master_nodes] please check that any required plugins are installed, or check the breaking changes documentation for removed settings
* he

