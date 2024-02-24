1. Firewalls:
Purpose: Firewalls are added to enforce security policies and control incoming and outgoing network traffic. They act as a barrier between a trusted internal network and untrusted external networks.
Why 3 Firewalls?: Each firewall provides an additional layer of security, creating a defense-in-depth strategy. They can be configured to filter traffic, block unauthorized access, and prevent malicious attacks.
2. SSL Certificate and HTTPS:
Purpose: SSL certificate and HTTPS encryption are crucial for securing data transmission between the client (browser) and the server.
Why HTTPS?: HTTPS encrypts data exchanged between the client and the server, protecting sensitive information such as login credentials, payment details, and personal data from eavesdropping and tampering.
3. Monitoring:
Purpose: Monitoring is used to ensure the availability, performance, and security of the infrastructure and applications.
Why Monitoring?: Monitoring helps detect and diagnose issues proactively, optimize performance, and ensure compliance with service level agreements (SLAs).
Data Collection: Monitoring clients, such as Sumo Logic, collect data from various sources including logs, metrics, and traces. They aggregate, analyze, and visualize this data to provide insights into the health and performance of the infrastructure.
Issues with the Infrastructure:
SSL Termination at Load Balancer Level:

SSL termination at the load balancer exposes decrypted traffic within the internal network, potentially exposing sensitive information to unauthorized access.
A better approach is to terminate SSL at the web server level to encrypt traffic end-to-end.
Single MySQL Server for Writes:

Having only one MySQL server capable of accepting writes creates a single point of failure (SPOF). If the server fails, it disrupts write operations and may lead to data inconsistency.
Implementing a Primary-Replica (Master-Slave) cluster or using a database management system with built-in replication can improve fault tolerance and data redundancy.
Homogeneous Servers:

Deploying servers with identical components (database, web server, application server) increases vulnerability to widespread failures.
Diversifying server configurations and distributing components across multiple servers can mitigate risks associated with single points of failure.
