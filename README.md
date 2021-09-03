# httpbin

Serviço usado para exemplificar o uso de mTLS dentro do OKE através do Istio.

Na pasta certificados temos tanto os sertificados de cliente como de server.

Para realizar uma chamada precisamo executar o curl da seguinte fotma

- curl -v --key client.example.com.key --cert clientcom.crt https://httpbin.poc-cloud.cf -k

