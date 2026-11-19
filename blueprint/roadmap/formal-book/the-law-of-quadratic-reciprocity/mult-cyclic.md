---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.mult_cyclic
statement: formalized
---

# mult_cyclic

The multiplicative group of a finite field is cyclic.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $F^*$ be the multiplicative group of the field $F$, with $|F^*| = n$. Writing $\operatorname{ord}(a)$ for the order of an element, that is, the smallest positive integer $k$ such that $a^k = 1$, we want to find an element $a \in F^*$ with $\operatorname{ord}(a) = n$. If $\operatorname{ord}(b) = d$, then by Lagrange's theorem, $d$ divides $n$. Classifying the elements according to their order, we have

$$
n = \sum_{d \mid n} \psi(d), \quad \text{where } \psi(d) = \#\{b\in F^*: \operatorname{ord}(b) = d\}.\qquad\text{(4)}
$$

If $\operatorname{ord}(b) = d$, then every element $b^i$ ($i = 1, \dots, d$) satisfies $(b^i)^d = 1$ and is therefore a root of the polynomial $x^d - 1$. But, since $F$ is a field, $x^d - 1$ has at most $d$ roots, and so the elements $b, b^2, \dots, b^d = 1$ are precisely these roots. In particular, every element of order $d$ is of the form $b^i$.

On the other hand, it is easily checked that $\operatorname{ord}(b^i) = \frac{d}{(i, d)}$, where $(i, d)$ denotes the greatest common divisor of $i$ and $d$. Hence $\operatorname{ord}(b^i) = d$ if and only if $(i, d) = 1$, that is, if $i$ and $d$ are relatively prime. Denoting *Euler's function* by $\varphi(d) = \#\{i : 1 \le i \le d, (i, d) = 1\}$, we thus have $\psi(d) = \varphi(d)$ whenever $\psi(d) > 0$. Looking at (4) we find

$$
n = \sum_{d \mid n} \psi(d) \le \sum_{d \mid n} \varphi(d).
$$

But as we are going to show that

$$
\sum_{d \mid n} \varphi(d) = n,\qquad\text{(5)}
$$

we must have $\psi(d) = \varphi(d)$ for all $d$. In particular, $\psi(n) = \varphi(n) \ge 1$, and so there is an element of order $n$.

The following (folklore) proof of (5) belongs in the Book as well. Consider the $n$ fractions

$$
\frac{1}{n}, \frac{2}{n}, \dots, \frac{k}{n}, \dots, \frac{n}{n},
$$

reduce them to the lowest term $\frac{k}{n} = \frac{i}{d}$ with $1 \le i \le d$, $(i, d) = 1$, $d \mid n$, and check that the denominator $d$ appears precisely $\varphi(d)$ times.

## Lean

Stated as [`book.quadratic_reciprocity.mult_cyclic`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.mult_cyclic); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 122](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L122)
