---
declaration: theorem
origin: cited
lean: harmonic_geometric_arithmetic₁
statement: formalized
proof: formalized
---

# First proof

Let $a_1, \dots, a_n$ be positive real numbers, then

$$
\frac{n}{\frac{1}{a_1}+\dots+\frac{1}{a_n}} \le
\sqrt[n]{a_1a_2\dots a_n} \le
\frac{a_1+\dots+ a_n}{n}
$$

with equality in both cases if and only if all $a_i$'s are equal.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The following beautiful nonstandard induction proof is attributed to Cauchy. Let $P(n)$ be the statement of the second inequality, written in the form

$$
a_1 a_2 \cdots a_n \le \left(\frac{a_1 + \cdots + a_n}{n}\right)^n.
$$

For $n=2$, we have $a_1 a_2 \le \left(\frac{a_1+a_2}{2}\right)^2 \iff (a_1-a_2)^2 \ge 0$, which is true. Now we proceed in the following two steps:

- (A) $P(n) \implies P(n-1)$
- (B) $P(n)$ and $P(2) \implies P(2n)$

which will clearly imply the full result.

To prove (A), set $A := \frac{\sum_{k=1}^{n-1} a_k}{n-1}$, then

$$
\left(\prod_{k=1}^{n-1} a_k\right) A \stackrel{P(n)}{\le} \left(\frac{\sum_{k=1}^{n-1} a_k + A}{n}\right)^n = \left(\frac{(n-1)A + A}{n}\right)^n = A^n
$$

and hence $\prod_{k=1}^{n-1} a_k \le A^{n-1}$.

For (B), we see

$$
\prod_{k=1}^{2n} a_k = \left(\prod_{k=1}^{n} a_k\right)\left(\prod_{k=n+1}^{2n} a_k\right)
\stackrel{P(n)}{\le} \left(\frac{\sum_{k=1}^{n} a_k}{n}\right)^n \left(\frac{\sum_{k=n+1}^{2n} a_k}{n}\right)^n
\stackrel{P(2)}{\le} \left(\frac{\sum_{k=1}^{2n} a_k}{2n}\right)^{2n}.
$$

The condition for equality is derived just as easily.

The left-hand inequality, between the harmonic and the geometric mean, follows now by considering $\frac{1}{a_1}, \dots, \frac{1}{a_n}$.

## Lean

Formalized as [`harmonic_geometric_arithmetic₁`](https://mo271.github.io/FormalBook/docs/find/#doc/harmonic_geometric_arithmetic₁).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 27](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L27)
