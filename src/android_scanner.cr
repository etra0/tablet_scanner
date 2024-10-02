require "kemal"
VERSION = "0.1.0"

SERVER = {{ read_file("server.html") }}
INDEX = {{ read_file("index.html") }}
color = ""

get "/" do
  INDEX
end

get "/server" do
  SERVER
end

ws "/ws/server" do |socket, context|
  socket.on_message do |msg|
    color = msg
  end
end

ws "/ws/client" do |socket, context|
  while true
    socket.send color
    sleep 1
  end
end

Kemal.run
