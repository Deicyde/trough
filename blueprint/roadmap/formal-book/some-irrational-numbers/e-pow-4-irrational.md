---
declaration: theorem
origin: cited
lean: book.irrational.e_pow_4_irrational
statement: formalized
---

# e_pow_4_irrational

$e^4$ is irrational.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Little Lemma](little-lemma.md)
- [e_pow_2_irrational](e-pow-2-irrational.md)

## Proof

In order to show that $e^4$ is irrational, we now courageously assume that $e^4 = \frac{a}{b}$ were rational, and write this as

$$
b e^2 = a e^{-2}.
$$

We could now try to multiply this by $n!$ for some large $n$, and collect the non-integral summands, but this leads to nothing useful: The sum of the remaining terms on the left-hand side will be approximately $b \frac{2^{n+1}}{n}$, on the right side $(-1)^{n+1} a \frac{2^{n+1}}{n}$, and both will be very large if $n$ gets large.

So one has to examine the situation a bit more carefully, and make two little adjustments to the strategy: First we will not take an *arbitrary* large $n$, but a large power of two, $n = 2^m$; and secondly we will not multiply by $n!$, but by $\frac{n!}{2^{n-1}}$. Then we need the little lemma [Little Lemma](little-lemma.md), a special case of Legendre's theorem (see page 10).

Let's get back to $b e^2 = a e^{-2}$. We are looking at

$$
b \frac{n!}{2^{n-1}} e^2 = a \frac{n!}{2^{n-1}} e^{-2}\qquad\text{(1)}
$$

and substitute the series

$$
e^2 = 1 + \frac{2}{1} + \frac{4}{2} + \frac{8}{6} + \dots + \frac{2^r}{r!} + \dots
$$

and

$$
e^{-2} = 1 - \frac{2}{1} + \frac{4}{2} - \frac{8}{6} \pm \dots + (-1)^r \frac{2^r}{r!} + \dots
$$

For $r \le n$ we get integral summands on both sides, namely

$$
b \frac{n!}{2^{n-1}} \frac{2^r}{r!} \quad \text{resp.} \quad (-1)^r a \frac{n!}{2^{n-1}} \frac{2^r}{r!},
$$

where for $r > 0$ the denominator $r!$ contains the prime factor $2$ at most $r-1$ times, while $n!$ contains it *exactly* $n-1$ times. (So for $r > 0$ the summands are even.)

And since $n$ is even (we assume that $n = 2^m$), the series that we get for $r \ge n+1$ are

$$
2b \left( \frac{2}{n+1} + \frac{4}{(n+1)(n+2)} + \frac{8}{(n+1)(n+2)(n+3)} + \dots \right)
$$

resp.

$$
2a \left( - \frac{2}{n+1} + \frac{4}{(n+1)(n+2)} - \frac{8}{(n+1)(n+2)(n+3)} \pm \dots \right).
$$

These series will for large $n$ be roughly $\frac{4b}{n}$ resp. $-\frac{4a}{n}$, as one sees again by comparison with geometric series. For large $n = 2^m$ this means that the left-hand side of (1) is a bit larger than an integer, while the right-hand side is a bit smaller — contradiction!

## Lean

Stated as [`book.irrational.e_pow_4_irrational`](https://mo271.github.io/FormalBook/docs/find/#doc/book.irrational.e_pow_4_irrational); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter08.tex, line 110](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter08.tex#L110)
