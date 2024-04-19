# Stage 1 - установка зависимостей и сборка приложения React
FROM node:14-alpine as build

# Устанавливаем рабочую директорию в /app/frontend
WORKDIR /app/frontend

# Копируем файлы package.json и package-lock.json для установки зависимостей
COPY frontend/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы из текущего каталога в рабочую директорию в контейнере
COPY frontend .

# Собираем приложение React
RUN npm run build

# Stage 2 - создаем минимальный образ для запуска приложения
FROM nginx:alpine

# Копируем собранные статические файлы из предыдущего stage в папку /usr/share/nginx/html в образе nginx
COPY --from=build /app/frontend/build /usr/share/nginx/html

# Экспонируем порт 80 для веб-сервера nginx
EXPOSE 80

# Запускаем nginx в фоновом режиме при запуске контейнера
CMD ["nginx", "-g", "daemon off;"]
