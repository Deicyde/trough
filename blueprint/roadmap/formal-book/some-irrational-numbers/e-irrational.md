---
declaration: theorem
origin: cited
lean: book.irrational.e_irrational
statement: formalized
---

# e_irrational

$e$ is irrational.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

To start with, it is rather easy to see (as did Fourier in 1815) that $e = \sum_{k \ge 0} \frac{1}{k!}$ is irrational. Indeed, if we had $e = \frac{a}{b}$ for integers $a$ and $b > 0$, then we would get

$$
n! b e = n! a
$$

for *every* $n \ge 0$. But this cannot be true, because on the right-hand side we have an integer, while the left-hand side with

$$
e = 1 + \frac{1}{1!} + \frac{1}{2!} + \dots + \frac{1}{n!} + \frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \frac{1}{(n+3)!} + \dots
$$

decomposes into an integral part

$$
b n! \left( 1 + \frac{1}{1!} + \frac{1}{2!} + \dots + \frac{1}{n!} \right)
$$

and a second part

$$
b \left( \frac{1}{n+1} + \frac{1}{(n+1)(n+2)} + \frac{1}{(n+1)(n+2)(n+3)} + \dots \right)
$$

which is *approximately* $\frac{b}{n}$, so that for large $n$ it certainly cannot be integral: It is larger than $\frac{b}{n+1}$ and smaller than $\frac{b}{n}$, as one can see from a comparison with a geometric series:

$$
\begin{aligned}
\frac{1}{n+1} &< \frac{1}{n+1} + \frac{1}{(n+1)(n+2)} + \frac{1}{(n+1)(n+2)(n+3)} + \dots \\
&< \frac{1}{n+1} + \frac{1}{(n+1)^2} + \frac{1}{(n+1)^3} + \dots = \frac{1}{n}.
\end{aligned}
$$

## Lean

Stated as [`book.irrational.e_irrational`](https://mo271.github.io/FormalBook/docs/find/#doc/book.irrational.e_irrational); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter08.tex, line 4](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter08.tex#L4)
