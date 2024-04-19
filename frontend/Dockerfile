# Stage 1 - сборка приложения
FROM node:14-alpine as build

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend .
RUN npm run build

# Проверяем содержимое каталога dist
RUN ls -l /app/frontend/dist

# Stage 2 - создаем минимальный образ для запуска приложения
FROM nginx:alpine

COPY --from=build /app/frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
