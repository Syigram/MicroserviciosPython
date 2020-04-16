FROM node:10.9.0-alpine

# Port to expose
EXPOSE 3000

# PROJECTHOME Variable
ARG PROJECTHOME=/home/prodigious/form_ui

# Create project dir and update WORKDIR
RUN mkdir -p $PROJECTHOME
WORKDIR $PROJECTHOME

# Copy dependencies file
COPY package.json .
COPY package-lock.json .

# Install dependencies
RUN npm install

# Copy directories
COPY public public
COPY src src

CMD ["npm", "start"]
