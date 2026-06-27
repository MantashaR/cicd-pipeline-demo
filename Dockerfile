# Lightweight production image: nginx serving the static site.
FROM nginx:1.27-alpine

# Replace the default nginx config with ours.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the static site into nginx's web root.
COPY site/ /usr/share/nginx/html/

EXPOSE 80

# Basic container healthcheck — useful talking point in interviews.
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1
