# etapa de compilación
FROM oven/bun:1 as build-stage
WORKDIR /app
COPY package*.json ./
RUN bun install
COPY . .
RUN bun run build

# etapa de producción
FROM nginx:latest as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]