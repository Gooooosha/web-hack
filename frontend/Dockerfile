# Используем базовый образ Node.js для сборки React приложения
FROM node:latest AS build

# Установка директории приложения в контейнере
WORKDIR /app

# Копирование зависимостей и установка их
COPY package.json package-lock.json ./
RUN npm install
RUN npm install axios

# Копирование остальных файлов в контейнер
COPY . .

# Сборка React приложения
RUN npm run build

# Используем образ Nginx для развертывания React приложения
FROM nginx:latest

# Копирование собранного React приложения из предыдущего этапа
COPY --from=build /app/dist /usr/share/nginx/html

# Экспонируем порт 80 для доступа к приложению
EXPOSE 80

# Команда для запуска Nginx внутри контейнера
CMD ["nginx", "-g", "daemon off;"]
