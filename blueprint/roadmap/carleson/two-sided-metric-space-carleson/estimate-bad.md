---
declaration: lemma
origin: cited
lean: estimate_bad
statement: formalized
proof: formalized
---

# Estimate bad

We have

$$
\mu\left({\{x\in X: |T_r b(x)|>\alpha/2\}}\right) \le  \frac{\frac{2^{5a}}{c} + 2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y) \,.
$$

## Depends on

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)
- [Estimate bad partial](estimate-bad-partial.md)
- [Estimate F set](estimate-f-set.md)

## Proof

We estimate

$$
\mu\left(\{x\in X: |T_r b(x)|>\alpha/2\}\right)
$$

$$
\le \mu (\Omega) +  \mu\left(\{x\in X\setminus\Omega: |T_r b(x)|>{\alpha}/2\}\right)\,.\qquad\text{(79)}
$$

Using [(64)](README.md) and [(56)](calderon-zygmund-decomposition.md), we conclude that

$$
\mu(\Omega) \le \sum_{j} \mu (B_{6,j})
\le 2^a \sum_j \mu(B_{3,j}) \le \frac{2^{5a}}{c\alpha} \int |f(y)|\, d\mu(y)\,.\qquad\text{(80)}
$$

It follows from [Estimate bad partial](estimate-bad-partial.md) and the triangle inequality that

$$
\mu({\{x\in X\setminus\Omega: |T_r b(x)|>\alpha/2\}}) \le \mu(\{x\in X\setminus\Omega: F(x)> \alpha/8\})\,.\qquad\text{(81)}
$$

The claim now follows from [Estimate F set](estimate-f-set.md).

## Lean

Formalized as [`estimate_bad`](https://fpvandoorn.github.io/carleson/docs/find/#doc/estimate_bad).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8071](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8071)
