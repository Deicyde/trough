---
declaration: lemma
origin: cited
lean: cotlar_control
statement: formalized
proof: formalized
---

# Cotlar control

Let $0\lt r\le R$ and $x\in X$. Let $g:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. Then for all $x'\in X$ with $\rho(x,x')\le\frac {R}{4}$ we have

$$
\left|T_R g(x)
\right|\le
|T_r(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')| +
2^{a^3 + 4a + 1} Mg(x)\, .\qquad\text{(24)}
$$

## Depends on

- [estimate x shift](estimate-x-shift.md)

## Proof

Let $x$ and $x'$ be given with $\rho(x,x')\le\frac {R}{4}$. By [estimate x shift](estimate-x-shift.md), we estimate the left-hand-side of (24) by

$$
|T_R(g)(x')|+
2^{a^3 + 2a + 2} Mg(x)\,.\qquad\text{(25)}
$$

We have

$$
T_R(g)(x')=
\int_{R\le\rho(x',y)} K(x',y) g(y) \, d\mu(y)\, .\qquad\text{(26)}
$$

On the domain $R\le\rho(x',y)$, we have $\frac {R}2\le\rho(x,y)$. Hence we may write for (26)

$$
T_R(g)(x')=\int_{R\le\rho(x',y)} K(x',y) (g-g\mathbf{1}_{B(x,\frac {R} 2)})(y) \,d\mu(y)
$$

$$
=T_R(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')\, .\qquad\text{(27)}
$$

Combining the estimate (25) with the identification (27), we obtain

$$
\left|T_R g(x)
\right|\le
|T_R(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')|+
2^{a^3 + 2a + 2} Mg(x)\, .\qquad\text{(28)}
$$

We have

$$
(T_r-T_R)(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')
$$

$$
= \int_{B(x',R)\setminus B(x',r)} K(x',y) (g-g\mathbf{1}_{B(x,\frac {R} 2)})(y) \,d\mu(y)
$$

$$
= \int_{B(x',R)\setminus (B(x',r) \cup B(x,\frac{R}{2}))} K(x',y) g(y) \,d\mu(y)\qquad\text{(29)}
$$

As $\frac{R}{2}\le\rho(x,y)$ together with $\rho(x,x')\le\frac {R}{4}$ implies $\frac {R}{4}\le\rho(x',y)$, we can estimate the absolute value of (29) with [(14)](../introduction/README.md) by

$$
\begin{aligned}
\le &\frac{2^{a^3}}{\mu(B(x',\frac{R}{4}))} \int_{B(x,2R)\setminus B(x',\frac{R}{4})}
|g(y)|\, d\mu(y) \\
\le &\frac{2^{a^3+a}}{\mu(B(x',\frac{R}{2}))} \int_{B(x,2R)}
|g(y)|\, d\mu(y) \\
\le &2^{a^3+a} \frac{\mu(B(x,2R))}{\mu(B(x,\frac{R}{4}))} Mg(x) \le 2^{a^3 + 4a} Mg(x)\, .
\end{aligned}
$$

By the triangle inequality, (24) follows now from (28) and the estimate for (29).

## Lean

Formalized as [`cotlar_control`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cotlar_control).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7225](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7225)
