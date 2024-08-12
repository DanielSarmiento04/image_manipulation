FROM oven/bun:1 AS build
WORKDIR /app
COPY . .
RUN bun i

RUN export NODE_OPTIONS="--max-old-space-size=8192"

RUN bun run build

FROM nginx:alpine AS runtime

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 8080