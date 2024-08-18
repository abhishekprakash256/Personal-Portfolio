# Use the official NGINX image as a base
FROM nginx:1.24-alpine

# Copy the custom NGINX configuration file to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP port
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
