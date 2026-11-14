---
declaration: theorem
origin: cited
lean: chapter2.bound_binomial_coeff
statement: formalized
---

# estimate_binomial_coefficient

$$
\binom{n}{k} \le \frac{n^k}{k!} \le \frac{n^k}{2^{k - 1}}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$$
\binom{n}{k} = \frac{n (n-1) \cdots (n-k+1)}{k!} \le \frac{n^k}{k!} \le \frac{n^k}{2^{k-1}}. \qedhere
$$

## Lean

Stated as [`chapter2.bound_binomial_coeff`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter2.bound_binomial_coeff); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter02.tex, line 163](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter02.tex#L163)
