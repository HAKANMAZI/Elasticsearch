Error 1)
{"error":{"root_cause":[{"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}}],"type":"security_exception","reason":"missing authentication credentials for REST request [/]","header":{"WWW-Authenticate":"Basic realm=\"security\" charset=\"UTF-8\""}},"status":401}
Solved 1) there is no password 

Error 2) 
cluster.initial_master_nodes: ["master1"]  doğru
cluster.initial_master_nodes: ["master-1"] yanlış