---
declaration: theorem
origin: cited
lean: book.irrational.e_pow_2_irrational
statement: formalized
---

# e_pow_2_irrational

$e^2$ is irrational.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [e_irrational](e-irrational.md)

## Proof

Now one might be led to think that this simple multiply-by-$n!$ trick is not sufficient to show that $e^2$ is irrational. This is a stronger statement: $\sqrt{2}$ is an example of a number which is irrational, but whose square is not. From John Cosgrave we have learned that with two nice ideas/observations (let's call them “tricks”) one can get two steps further nevertheless: Each of the tricks is sufficient to show that $e^2$ is irrational, the combination of both of them even yields the same for $e^4$. The first trick may be found in a one page paper by J. Liouville from 1840 — and the second one in a two page “addendum” which Liouville published on the next two journal pages.

Why is $e^2$ irrational? What can we derive from $e^2 = \frac{a}{b}$? According to Liouville we should write this as

$$
b e = a e^{-1},
$$

substitute the series

$$
e = 1 + \frac{1}{1} + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \cdots
$$

and

$$
e^{-1} = 1 - \frac{1}{1} + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} \pm \cdots,
$$

and then multiply by $n!$, for a sufficiently large even $n$. Then we see that $n! b e$ is nearly integral:

$$
n! b \left( 1 + \frac{1}{1} + \frac{1}{2} + \frac{1}{6} + \dots + \frac{1}{n!} \right)
$$

is an integer, and the rest

$$
n! b \left( \frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \dots \right)
$$

is approximately $\frac{b}{n}$: It is larger than $\frac{b}{n+1}$ but smaller than $\frac{b}{n}$, as we have seen above.

At the same time $n! a e^{-1}$ is nearly integral as well: Again we get a large integral part, and then a rest

$$
(-1)^{n+1} n! a \left( \frac{1}{(n+1)!} - \frac{1}{(n+2)!} + \frac{1}{(n+3)!} \mp \cdots \right),
$$

and this is approximately $(-1)^{n+1} \frac{a}{n}$. More precisely: for even $n$ the rest is larger than $-\frac{a}{n}$, but smaller than

$$
-a \left( \frac{1}{n+1} - \frac{1}{(n+1)^2} - \frac{1}{(n+1)^3} - \cdots \right) = - \frac{a}{n+1} \left( 1 - \frac{1}{n} \right) < 0.
$$

But this cannot be true, since for large even $n$ it would imply that $n! a e^{-1}$ is just a bit smaller than an integer, while $n! b e$ is a bit larger than an integer, so $n! a e^{-1} = n! b e$ cannot hold.

## Lean

Stated as [`book.irrational.e_pow_2_irrational`](https://mo271.github.io/FormalBook/docs/find/#doc/book.irrational.e_pow_2_irrational); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter08.tex, line 37](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter08.tex#L37)
