FROM nginx:stable-alpine
COPY --from=build ./site/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]