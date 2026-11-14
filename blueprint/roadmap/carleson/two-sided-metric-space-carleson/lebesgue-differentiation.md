---
declaration: lemma
origin: cited
lean: lebesgue_differentiation
statement: formalized
proof: formalized
---

# Lebesgue differentiation

Let $f$ be a bounded measurable function supported on a set of finite measure. Then for $\mu$ almost every $x$, we have

$$
\lim_{n\to \infty} \frac{1}{\mu(B_n)}\int_{B_n} f(y)\, dy= f(x),
$$

where $\{B_n\}_{n\geq 1}$ is a sequence of balls with radii $r_n>0$ such that $x\in B_n$ for each $n\geq 1$ and

$$
\lim_{n\to \infty} r_n=0 \,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This follows from the Lebesgue differentiation theorem, which is already formalized in Lean.

## Lean

Formalized as [`lebesgue_differentiation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/lebesgue_differentiation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7576](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7576)
