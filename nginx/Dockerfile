# Use the official NGINX image as a base
FROM nginx:1.24-alpine

# Install Certbot and dependencies
RUN apk add --no-cache certbot python3-certbot-nginx openssl bash
# Copy the custom NGINX configuration file to /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Obtain and install the SSL certificate during build
# (Replace `yourdomain.com` with your actual domain name)
RUN certbot certonly --non-interactive --nginx --agree-tos --email abhishekprakash47@gmail.com -d meabhi.me

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
