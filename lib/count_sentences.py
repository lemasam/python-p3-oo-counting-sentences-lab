#!/usr/bin/env python3
import re
class MyString:
      def __init__(self, value = ""):
        self._value = value
    
      def get_value(self):
        return self._value

      def set_value(self, stringVal):
        if (type(stringVal) == str):
          self._value = stringVal
        else:
          print("The value must be a string.")

      value = property(get_value, set_value)

      def is_sentence(self):
        return self._value.endswith(".")

      def is_question(self):
        return self._value.endswith("?")

      def is_exclamation(self):
        return self._value.endswith("!")

      def count_sentences(self):
        # Split the string using regular expressions to handle multiple sentence-ending punctuation
          sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings and return the count of non-empty sentences
          return len([sentence for sentence in sentences if sentence.strip() != ""])
pass
