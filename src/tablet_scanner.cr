require "kemal"
require "socket"

module Kemal
  # monkey patch display message...
  def self.display_startup_message(config, server)
    domains = Socket::Addrinfo.resolve(System.hostname, 3000, type: Socket::Type::STREAM, protocol: Socket::Protocol::TCP)
    domains.each do |h|
      puts "Open http://#{h.ip_address}/ on your tablet"
      puts "Open http://#{h.ip_address}/server on your laptop!"
      puts
      puts "----------"
      puts
    end
  end
end

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
  color = env.params.json["color"]
end

get "/color" do |env|
  { "color" => color }.to_json
end

Kemal.config.env = "production"
Kemal.run
