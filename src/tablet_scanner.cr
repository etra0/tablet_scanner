require "kemal"
require "socket"

SERVER = {{ read_file("front/server.html") }}
INDEX = {{ read_file("front/index.html") }}
color = ""

get "/" do
  INDEX
end

get "/server" do
  SERVER
end

post "/color" do |env|
  puts "Received #{env.params.json}"
  color = env.params.json["color"]
end

get "/color" do |env|
  { "color" => color }.to_json
end

Kemal.run
