# Use the official NGINX image as the base
FROM nginx:alpine

# Install Certbot and its NGINX plugin
RUN apk add --no-cache certbot certbot-nginx bash

# Copy your NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf


# Expose ports
EXPOSE 80 443

# Command to start NGINX
CMD ["nginx", "-g", "daemon off;"]