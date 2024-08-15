#!/bin/bash
set -e

# Start NGINX in the background
nginx &

# Obtain or renew the certificates
#certbot --nginx --non-interactive --agree-tos --email your-email@yourdomain.com --domains yourdomain.com,www.yourdomain.com
certbot --nginx -d meabhi.me

# Auto-renew certificates
while :; do
    certbot renew --quiet --no-self-upgrade
    sleep 12h
done
