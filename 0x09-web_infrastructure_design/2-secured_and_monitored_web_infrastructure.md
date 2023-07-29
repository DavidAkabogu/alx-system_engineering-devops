Server 1: This server will host the Nginx web server and act as the primary web server, responsible for serving HTTP/HTTPS requests.

Server 2: This server will also host the Nginx web server and serve as the secondary web server, providing redundancy and high availability.

Server 3: This server will host the application server (e.g., PHP, Python, Ruby), responsible for handling dynamic content and interactions with the database.

Load Balancer (with SSL termination): The load balancer will distribute incoming HTTPS requests across the two web servers. It will also handle SSL termination, decrypting incoming HTTPS traffic and forwarding it to the web servers as plain HTTP.

SSL Certificate: An SSL certificate will be installed on the load balancer to enable HTTPS for the website. This ensures encrypted communication between the users' browsers and the web servers, enhancing security and protecting sensitive data.

Firewalls: Each server will have its own firewall to control incoming and outgoing network traffic. Firewalls help protect the servers from unauthorized access and potential security threats.

Monitoring Clients (Data Collectors): Each server will have a monitoring client installed, acting as a data collector to gather server performance metrics, log data, and other relevant information. The collected data will be sent to a centralized monitoring service like Sumo Logic or other monitoring services.

Explanation of Specifics:

Firewalls: Firewalls are added to each server to restrict and control network traffic. They act as a barrier between the servers and the outside world, allowing only authorized traffic to pass through and blocking potential threats.

HTTPS: Serving traffic over HTTPS is essential for security. HTTPS encrypts data transmitted between users' browsers and the servers, preventing unauthorized interception and ensuring data integrity.

Monitoring: Monitoring is used to keep track of the servers' health, performance, and security. It helps identify potential issues, track resource utilization, and ensure the infrastructure operates optimally.

Monitoring Tool and Data Collection: The monitoring tool (e.g., Sumo Logic) is a centralized service that collects data from the monitoring clients on each server. It processes and analyzes the data to generate performance metrics, logs, and alerts.

Monitoring Web Server QPS: To monitor the web server's queries per second (QPS), the monitoring tool would track the incoming requests to the web servers over a specific time frame and calculate the average QPS.

Issues with the Infrastructure:

Terminating SSL at the Load Balancer Level: Terminating SSL at the load balancer means the traffic between the load balancer and web servers is in plain HTTP. This creates a security risk since the internal communication is not encrypted. Ideally, SSL termination should occur on the web servers themselves.

Single MySQL Server Accepting Writes: Having only one MySQL server capable of accepting writes creates a Single Point of Failure (SPOF). If the database server fails, the website will lose write functionality, leading to downtime and data inconsistency.

Servers with All the Same Components: Having servers with identical components (database, web server, application server) can be a problem for scalability and redundancy. It is better to have separate database nodes in a cluster to distribute the database workload and improve fault tolerance.

To address these issues, we can implement SSL termination on the web servers, set up a MySQL cluster with multiple nodes, and consider diversifying server components for better scalability and high availability. Additionally, we should ensure that the monitoring setup includes all critical components and is properly configured to detect and respond to potential issues proactively.