# Use the official NGINX image as a base
FROM nginx:1.24-alpine

# Install Certbot and the NGINX plugin for Certbot
RUN apk add --no-cache certbot python3-certbot-nginx

# Copy custom NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the Certbot entrypoint script
COPY certbot-entrypoint.sh /usr/local/bin/certbot-entrypoint.sh
RUN chmod +x /usr/local/bin/certbot-entrypoint.sh

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Run the Certbot entrypoint script
ENTRYPOINT ["/usr/local/bin/certbot-entrypoint.sh"]
