Error 1) {"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}},"status":401}
* There is no password 

Error 2) 
- cluster.initial_master_nodes: ["master1"]  doğru
- cluster.initial_master_nodes: ["master-1"] yanlış

Error 3)  
What is the default Username and Password for ElasticSearch 7.4.2 (when x-pack enabled)?
* bin/elasticsearch-setup-passwords interactive
* bin/elasticsearch-setup-passwords auto

Error 4) data1
java.lang.IllegalArgumentException: unknown setting [cluster.inital_master_nodes] please check that any required plugins are installed, or check the breaking changes documentation for removed settings
* cluster.inital_master_nodes değil **cluster.initial_master_nodes**

Error 5) 
Exception in thread "main" 2021-01-01 17:12:13,070 main ERROR No Log4j 2 configuration file found. Using default configuratio
Jan 01 17:12:13 data2 elasticsearch[3227]: SettingsException[Failed to load settings from [elasticsearch.yml]]; nested: JsonParseException[Duplicate field 'http.port'
* Duplicate field **'http.port'** yani iki kez tanımlanmış

