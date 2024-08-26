# Use the official NGINX image as a base
FROM nginx:1.24-alpine

# Install dependencies
RUN apk add --no-cache certbot python3 py3-pip openssl bash

# Install Certbot and the NGINX plugin via pip
RUN pip install certbot-nginx

# Copy the custom NGINX configuration file to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Start NGINX and Certbot renewal process
CMD ["sh", "-c", "nginx -g 'daemon off;' & certbot --nginx --non-interactive --agree-tos --email abhishekprakash47@gmail.com -d www.meabhi.me && crond -f"]
