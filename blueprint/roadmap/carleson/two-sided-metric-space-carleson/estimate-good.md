---
declaration: lemma
origin: cited
lean: estimate_good
statement: formalized
proof: formalized
---

# Estimate good

$$
\mu\left(\{x\in X: |T_r g(x)|>{\alpha}/2\}\right)
\le \frac{2^{2a^3+3a+2}c}{\alpha} \int |f(y)|\, d\mu(y).
$$

## Depends on

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)

## Proof

We estimate using monotonicity of the integral

$$
\mu\left(\{x\in X: |T_r g(x)|>{\alpha}/2\}\right)\leq \frac{4}{\alpha^2} \int |T_r g(y)|^2\, d\mu(y).
$$

Using [(11)](calderon-zygmund-weak-1-1.md) followed by [(51)](calderon-zygmund-decomposition.md) and [(52)](calderon-zygmund-decomposition.md), we estimate the right hand side above by

$$
\leq \frac{4\cdot 2^{2a^3}}{\alpha^2} \int |g(y)|^2\, d\mu(y)\leq \frac{2^{2a^3+3a+2}c}{\alpha} \int |g(y)|\, dy \le \frac{2^{2a^3+3a+2}c}{\alpha} \int |f(y)|\, d\mu(y).\qquad\text{(66)}
$$

## Lean

Formalized as [`estimate_good`](https://fpvandoorn.github.io/carleson/docs/find/#doc/estimate_good).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7869](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7869)
