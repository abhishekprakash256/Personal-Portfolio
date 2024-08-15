# Use the official NGINX image as a base
FROM nginx:1.24-alpine

# Copy custom NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
