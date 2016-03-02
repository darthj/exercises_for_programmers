package main

import "fmt"

func main() {
  fmt.Print("What is your name? ")
  var input string
  fmt.Scanf("%s", &input)

  fmt.Printf("Hello, %s, nice to meet you.\n", input)
}
