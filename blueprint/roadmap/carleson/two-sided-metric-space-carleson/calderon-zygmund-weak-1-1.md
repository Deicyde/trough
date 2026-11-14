---
declaration: lemma
origin: cited
lean: czOperator_weak_1_1
statement: formalized
proof: formalized
---

# Calderon-Zygmund Weak (1, 1)

Let $f:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure and assume for some $r>0$ that for every bounded measurable function $g:X\to{\mathbb{C}}$ supported on a set of finite measure,

$$
\|T_rg\|_{2}\le 2^{a^3} \|g\|_2.\qquad\text{(11)}
$$

Then for all $\alpha>0$, we have

$$
\mu\left(\{x\in X: |T_r f(x)|>\alpha\}\right)\le \frac{2^{a^3 + 19a}}{\alpha} \int |f(y)|\, d\mu(y).\qquad\text{(12)}
$$

## Depends on

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)
- [Estimate bad](estimate-bad.md)
- [Estimate good](estimate-good.md)

## Proof

*Proof of Calderon-Zygmund Weak (1, 1).* It follows by the triangle inequality and subadditivity of $\mu$ that

$$
\mu\left(\{x\in X: |T_r f(x)|>\alpha\}\right)
$$

$$
\le \mu\left(\{x\in X: |T_r g(x)|>{\alpha}/2\}\right) +  \mu\left(\{x\in X: |T_r b(x)|>{\alpha}/2\}\right).\qquad\text{(13)}
$$

Using [Estimate good](estimate-good.md), [Estimate bad](estimate-bad.md) and the definition [(61)](README.md) of $c$, we get

$$
\begin{aligned}
\le& \frac{2^{2a^3+3a+2}c + \frac{2^{5a}}{c} + 2^{a^3+9a+4}}{\alpha} \int |f(y)|\, d\mu(y) \\
=& \frac{2^{a^3-9a-2} + 2^{a^3+17a+4} + 2^{a^3+9a+4}}{\alpha} \int |f(y)|\, d\mu(y) \\
\le& \frac{2^{a^3 + 19a}}{\alpha} \int |f(y)|\, d\mu(y).
\end{aligned}
$$

## Lean

Formalized as [`czOperator_weak_1_1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/czOperator_weak_1_1).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7068](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7068)
