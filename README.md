# ARPNC
## Advanced RPN Calculator

This is, as the name suggests, an RPN calculator. We make this because we want to make the reverse polish notation popular again. We are nostalgic about those early pocket calculators and computer systems. The main reason RPN became popular during the 1970s was its ability to streamline complex mathematical calculations... while still requiring fewer keystrokes compared to the infix notation. That's exactly what we're trying to achieve in this repo. We try to do away with everything that's not absolutely necessary. No square brackets, no curly braces, no semicolons... you get the idea, we hope! We strongly believe that operator precedence and nested parentheses are hallmarks of a suboptimal language.

We believe that RPN is a more natural and intuitive way to do math, and write simple programs. 

This is a valid program:

```
$ Hello, World! $ print
3 2 + 5 * print
```

But anything more than a space is unnecessary. A single space is all that matters. This is an equally valid program:

```
$ Hello, World! $ print 3 2 + 5 * print
```

This is a stack-based calculator, so the output is:

```
Hello, World!
25.0
Empty stack
```

You can create functions, but all functions use the same stack. So, functions don't need to have arguments. Consider this:

```
( :sayHelloTo $ Hello $ printnn space printnn print ) $ Bob $ sayHelloTo
```

Note that space is a part of the language. If you want to print a single space, you have to use the `space` keyword. It pushes a single space character to the stack.

There's a lot more you can do with this language. This is a completely valid program too(remember, the newlines are optional):

```
2 3.2 + 5 5.1 * - 2 * dup * dup print 2 * print 5 6 * print
13 25 - print
$ Now trying exponentiation $ print
2 -0.3 ** sin cos print
$ Hello, World! How's it going?? $ print
$ And now? $ dup print upper print
$ Newlines are only for humans, they don't matter $ print
2 log print 2 log2 print 3 e 2 + print 2 sqrt print
```

If you've used one of those HP calculators from the seventies, this syntax probably makes sense to you immediately. And if you haven't, try to think of this whole program as a bunch of push and pop operations on a stack. We're sure that you'll get it, and that you'll eventually love it. There's something awesome about this retro aesthetic.

We support operations on lists. Consider this program where we try to find the sum of a bunch of numbers:

```
. 4 5 6 10 15 sum print
```

The output of this program is:

```
40.0
Empty stack
```

We support comparison operators too. Take a look at this:

```
$ Is 33 greater than 32? $ print
32 33 > print
$ Is 33 lesser than 32? $ print
32 33 < print
$ Is 555 equal to 555? $ print
555 555 == print
```

The output is, as you might have expected, this:

```
Is 33 greater than 32?
1
Is 33 lesser than 32?
0
Is 555 equal to 555?
1
Empty stack
```

Now, here's a test. Can you tell what's happening here:

```
5 . 2 3 5 4 2 product + 3 * print . 10 20 30 sum print
```

We support constants, but not variables. All constants must have @ as the prefix.

```
2 3 + @a set
5 6 * @b set
@a @b + print
```

If you think this language is too wordy, you can "rename" keywords to minimize keystrokes:

```
( :p print ) ( :s set ) $ Is this better? $ @a s @a p
```
