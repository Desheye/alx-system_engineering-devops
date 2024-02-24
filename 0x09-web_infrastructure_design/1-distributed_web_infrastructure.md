1. Components:
2 Servers: We'll have two physical servers to distribute the load and increase redundancy.
1 Load Balancer (HAproxy): It distributes incoming traffic across multiple servers to improve reliability and scalability.
1 Web Server (Nginx): Serves static content, handles SSL termination, and forwards dynamic requests to the application server.
1 Application Server: Executes application logic and interacts with the database.
1 Database (MySQL): Stores application data.


2. Distribution Algorithm:
We'll configure the HAProxy load balancer with a round-robin distribution algorithm. This algorithm evenly distributes incoming requests among the available servers, ensuring each server gets its fair share of traffic.

3. Active-Active vs. Active-Passive Setup:
We'll configure HAProxy for an Active-Active setup. In an Active-Active setup, both load balancers are actively distributing traffic, providing redundancy and load balancing. In contrast, Active-Passive setup has one active load balancer and another in standby, which only becomes active if the primary one fails.

4. Database Primary-Replica Cluster:
The MySQL database will be set up as a Primary-Replica (Master-Slave) cluster. In this setup, the Primary node (Master) handles write operations, while the Replica nodes (Slaves) replicate data from the Primary node and handle read operations. This setup improves data redundancy and read scalability.

5. Application-Database Interaction:
The application interacts with the Primary node for write operations (inserts, updates, deletes) to ensure data consistency and integrity.
For read operations, the application can interact with either the Primary or Replica nodes. However, directing read traffic to Replica nodes reduces the load on the Primary node and improves overall performance.


Issues with the Infrastructure:
Single Point of Failure (SPOF):

The web server, application server, and database are all potential single points of failure. If any of these components fail, it could lead to downtime or degraded performance.
Lack of redundancy in the load balancer setup. If the load balancer fails, traffic distribution will be disrupted.
Security Issues:

Lack of firewall protection exposes the servers to potential security threats and unauthorized access.
Lack of HTTPS encryption leaves data transmission vulnerable to interception and tampering.
No Monitoring:

Without monitoring tools, it's challenging to identify performance bottlenecks, security breaches, or system failures proactively.
Monitoring is crucial for maintaining system health, identifying issues, and ensuring high availability and performance.
