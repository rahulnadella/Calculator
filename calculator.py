"""
 Copyright (c) 2015, Rahul Nadella
 All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other
 materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""
The Calculator class is a simple implementation of a calculator
containing several generic math functions

version 1.0
"""


class Calculator(object):

  """
  The add function (often signified by the plus symbol "+") is one of the
  four elementary, mathematical operations of arithmetic, with the others
  being subtraction, multiplication and division. The addition of two
  whole numbers is the total amount of those quantities combined.
  """

  def add(self, a, b):
    return a + b

  """
  The subtract funciton is a mathematical operation that represents the
  operation of removing objects from a collection. It is signified by the
  minus sign (−). For example, in the picture on the right, there are
  5 − 2 apples—meaning 5 apples with 2 taken away, which is a total of
  3 apples.
  """

  def subtract(self, a, b):
    return a - b

  """
  The multiply function is the process of combining matrices, vectors,
  or other quantities under specific rules to obtain their product.
  """

  def multiply(self, a, b):
    return a * b

  """
  The divide function is the opposite of multiply function. When we know
  a multiplication fact we can find a division fact: Example: 3 × 5 = 15,
  so 15 / 5 = 3.
  """

  def divide(self, a, b):
    return a / b

  """
  The modulus function is an operation that finds the remainder after
  division of one number by another (sometimes called modulus).
  """

  def modulus(self, a, b):
    return a % b

  """
  The squared function is the result of multiplying a number by
  itself. The verb "to square" is used to denote this operation.
  Squaring is the same as raising to the power 2, and is denoted by a
  superscript 2; for instance, the square of 3 may be written as 32,
  which is the number 9.
  """

  def squared(self, a):
    return a ** 2

  """
  The cubed function is to multiply a number or a quantity by itself
  three times; raise to the third power. For example, five cubed is
  5 × 5 × 5. Noun. The product that results when a number or quantity
  is cubed. For example, the cube of 5 is 125.
  """

  def cubed(self, a):
    return a ** 3

  """
  The power function is a generic exponential function; for
  example 4^4 -> 4 x 4 x 4 x 4 = 256
  """

  def power(self, a, b):
    return a ** b

  """
  In mathematics, a square root of a number a is a number y such that
  y^2 = a, in other words, a number y whose square (the result of
  multiplying the number by itself, or y × y) is a. For example,
  4 and −4 are square roots of 16 because 42 = (−4)2 = 16.
  """

  def sqrt(self, a):
    return (a**0.5)

  """
  The root function is generic root function;
  for example cubic root -> √27 = 3
  """

  def root(self, a, b):
    return (a**(1 / b))

  """
  In mathematics, the absolute value (or modulus) |x| of a
  real number x is the non-negative value of x without regard
  to its sign. Namely, |x| = x for a positive x, |x| = −x for
  a negative x (in which case −x is positive), and |0| = 0.
  For example, the absolute value of 3 is 3, and the absolute
  value of −3 is also 3. The absolute value of a number may be
  thought of as its distance from zero.
  """

  def abs(self, a):
    if a <= 0:
      return -a
    else:
      return a
