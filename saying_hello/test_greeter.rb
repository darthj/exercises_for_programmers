require 'minitest/autorun'
require_relative 'greeter'

class TestGreeter < Minitest::Test
  def test_santa_is_greeted
    assert_equal "Hello, Santa, nice to meet you!", greet('Santa')
  end

  def test_name_has_no_surrounding_whitespace
    assert_equal "Trickster", sanitize_name("Trickster \n")
  end
end

