---
declaration: lemma
origin: cited
lean: cotlar_set_F₁, cotlar_set_F₂
statement: formalized
proof: formalized
---

# Cotlar sets

Assume that [(3)](two-sided-metric-space-carleson.md) holds. Let $0\lt r\le R$ and $x\in X$. Let $g:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. Then the measure $|F_1|$ of the set $F_1$ of all $x'\in B(x,\frac {R} 4)$ such that

$$
|T_rg(x')|> 4 M(T_rg)(x)\qquad\text{(30)}
$$

is less than or equal to $\mu(B(x,\frac{R}{4}))/4$. Moreover, the measure $|F_2|$ of the set $F_2$ of all $x'\in B(x,\frac {R} 4)$ such that

$$
|T_r(g\mathbf{1}_{B(x,\frac {R} 2)})(x')| > 2^{a^3 + 20a + 2} Mg(x)\qquad\text{(31)}
$$

is less than or equal to $\mu(B(x,\frac{R}{4}))/4$.

## Depends on

- [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md)

## Proof

Let $r$, $R$, $x$ and $g$ be given. If $M(T_rg)(x)=0$, then $T_rg$ is zero almost everywhere and the estimate on $|F_1|$ is trivial. Assume $M(T_rg)(x)>0$. We have with (30)

$$
M(T_rg)(x)\ge
\frac 1{\mu(B(x,\frac{R}{4}))}\int_{B(x,\frac{R}{4})}|T_rg(x')|\, dx'
$$

$$
\ge
\frac 1{\mu(B(x,\frac{R}{4}))}\int_{F_1} 4 M(T_rg)(x)\, dx' \,.
$$

Dividing by $M(T_rg)(x)$ gives

$$
1\ge \frac{4}{\mu(B(x,\frac{R}{4}))} |F_1|\, .
$$

This gives the desired bound for the measure of $F_1$. We turn to the set $F_2$. Similarly as above we may assume $Mg(x)>0$. The set $F_2$ is then estimated with [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md) by

$$
\frac {2^{a^3+19a}}{2^{a^3 + 20a + 2}Mg(x)}\int |g\mathbf{1}_{B(x,\frac {R}2)}|(y)\, d\mu(y)
$$

$$
\le \frac {1}{2^{a+2} Mg(x)}\mu(B(x,\frac {R}{2})) Mg(x) \le \frac{\mu(B(x,\frac {R}{4}))}{4} \,.
$$

This gives the desired bound for the measure of $F_2$.

## Lean

Formalized as [`cotlar_set_F₁`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cotlar_set_F₁), [`cotlar_set_F₂`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cotlar_set_F₂).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7294](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7294)
