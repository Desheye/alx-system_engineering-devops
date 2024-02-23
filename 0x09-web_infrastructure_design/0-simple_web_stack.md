Server: We’ll use a single server to host the entire website.
Web Server (Nginx): The web server will handle incoming HTTP requests and serve static content like HTML, CSS, and images.
Application Server: This server will process dynamic content, execute application code, and interact with the database.
Application Files (Code Base): The application files contain your website’s code, such as PHP, Python, or Node.js scripts.
Database (MySQL): The database will store and retrieve data for your website.
Now, let’s walk through the steps when a user wants to access your website:

The user enters www.foobar.com in their web browser.
The browser performs a DNS query to discover the IP address associated with the domain name. In this case, the DNS entry for www.foobar.com points to the server’s IP address (e.g., 8.8.8.8).
The server houses the entire website, including both static and dynamic content.
The user’s computer sends HTTP requests to the web server (Nginx). The web server processes these requests and delivers the appropriate response (usually an HTML page).
The web server acts as a middleman between the user and the application server. The application server processes dynamic content (e.g., user authentication, form submissions) and runs the application code.
To retrieve relevant data, the application server communicates with the database (MySQL). It fetches information and provides it to the web server for inclusion in the response sent to the user’s browser.
The communication between the server and the user’s computer happens using the Internet Protocol (IP).
However, there are some limitations with this infrastructure:

Single Point of Failure (SPOF): Since we rely on a single server, if it goes down, the website becomes inaccessible. Server maintenance (e.g., deploying new code) may cause temporary downtime.
Limited Scalability: Handling a sudden increase in traffic can be challenging with this setup.
