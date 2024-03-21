# ARPNC
## Advanced RPN Calculator

This is, as the name suggests, an RPN calculator. We make this because we want to make the reverse polish notation popular again. We are nostalgic about those early pocket calculators and computer systems. The main reason RPN became popular during the 1970s was its ability to streamline complex mathematical calculations... while still requiring fewer keystrokes compared to the infix notation. That's exactly what we're trying to achieve in this repo. We try to do away with everything that's not absolutely necessary. No square brackets, no curly braces, no semicolons... you get the idea, we hope!

We believe that RPN is a more natural and intuitive way to do math, and write simple programs. 

This is a valid program:

```
$ Hello, World! $ print
3 2 + 5 * factorial print
```

But anything more than a space is unnecessary. A single space is all that matters, and it matters a lot. For example, you can't skip the spaces after and before the `$` symbols when creating a string. But otherwise, this is an equally valid program:

```
$ Hello, World! $ print 3 2 + 5 * factorial print
```

This is a stack-based calculator, so the output is:

```
Hello, World!
15511210043330985984000000
ok
```

If you use the REPL, you don't have to say `print`. And in that mode, you also have the option to just hit **enter** after every input, just like the old calculators. Use the word `quit` to end the session. Here's a sample session:

```
Welcome to ARPNC v0.9
# 3
3.0
# 2
2.0
# +
5.0
# 2
2.0
# *
10.0
# quit
```

---

You can create functions, but all functions use the same stack. So, functions don't need to have arguments. Consider this:

```
( :sayHelloTo $ Hello $ printnn space printnn print ) $ Bob $ sayHelloTo
```

Because space is a part of the language, if you want to print a single space, you have to use the `space` keyword. It pushes a single space character to the stack.

There's a lot more you can do with this language. This is a completely valid program too(remember, the newlines are optional):

```
2 3.2 + 5 5.1 * - 2 * dup * dup print 2 * print 5 6 * print
13 25 - print
$ Now trying exponentiation $ print
2 -0.3 ** sin cos print
$ And now tan $ print
0.5 tan print
$ Hello, World! How's it going?? $ print
$ And now? $ dup print upper print
$ Newlines are only for humans, they don't matter $ print
2 dup log print log2 print 3 e 2 + print 2 sqrt print
$ Constants are supported, but no variables allowed $ print
. 3 2 1 sum @a set
. 3 2 1 product @b set
@b decr @c set @a @c + print
2.1 4 19 mod 9 * mod print
3 2 19 lsh rsh print
5 51 * dup dup dup print16 print8 print2 print
```

If you've used one of those HP calculators from the seventies, this syntax probably makes sense to you immediately. And if you haven't, try to think of this whole program as a bunch of push and pop operations on a stack. We're sure that you'll get it, and that you'll eventually love it. There's something awesome about this retro aesthetic.

We support operations on lists. Consider this program where we try to find the sum of a bunch of numbers:

```
. 4 5 6 10 15 sum print
```

The output of this program is:

```
40.0
ok
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
ok
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

Conditional statements generally need to make use of functions. This is because the `if` keyword merely forces the interpreter to skip the next token if there's a zero on the top of the stack. Here's an example:

```
( :sayYes $ Yes $ print ) ( :sayNo $ No $ print )
18 @votingAge set
19 @age set
$ Can vote? $ print
@votingAge @age > if sayYes
@votingAge @age < if sayNo
```

Recursion is allowed. Here's some simple code that can print the multiplication table of a user-provided number:

```
( :loop dup @v * print decr dup 0 < if loop )
$ Enter number : $ print
read @v set 10 loop drop
```

Note that you need to use the `readstr` keyword when you are expecting a string from the user. For example:

```
$ Enter name : $ print
readstr @name set 
$ Hello $ printnn space printnn @name print
```

If you think this language is too wordy, you can always "rename" keywords to minimize keystrokes:

```
( :p print ) ( :s set ) $ Is this better? $ @a s @a p
```

Take a look at the files in the **tests** directory for more examples.
