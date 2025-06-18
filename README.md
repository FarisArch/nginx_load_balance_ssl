# NGINX Load Balancing and SSL Termination
- NGINX Load balancing simply load balance the traffic between the servers that is defined in the upstream directive
- The load balancing is done through round-robin algorithm, meaning it will balance equally.
- NGINX SSL Termination basically offloads the SSL work of decrypting and encrypting to the proxy server in this case the NGINX server.
- This helps with increasing performance of the backend server since they do not need to perform the SSL handshake, instead just communicate with proxy server using HTTP.

- For this to work, you need generate a private key and certificate for the SSL server.
