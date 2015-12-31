
def greet(name = nil)
  name ||= prompt_for_name

  greeting(sanitize_name(name))
end

def greeting(name)
  "Hello, " + name + ", nice to meet you!"
end

def prompt_for_name
  gets
end

def sanitize_name(name)
  name.chomp.strip
end

if $0 == 'greeter.rb'
  puts "What is your name?"

  puts greet
end
