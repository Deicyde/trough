---
declaration: proposition
origin: cited
lean: k_eq_zero
statement: formalized
proof: formalized
---

# Vanishing entropy

We have $k = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Application of BSG](lem-get-better.md)
- [Multidistance and Ruzsa distance, III](../multidistance/multidist-ruzsa-iii.md)
- [Lower bound on multidistance](../the-tau-functional/multidist-lower.md)
- [Distance bound](xi-z2-w-dist.md)
- [$\eta$](../the-tau-functional/eta-def-multi.md)
- [Nonnegativity](../multidistance/multidist-nonneg.md)
- [Zero-sum](zero-sum.md)
- [Mutual information bound](prop-52.md)

## Proof

For each value $W=w$, apply [Application of BSG](lem-get-better.md) (and [Zero-sum](zero-sum.md)) to

$$
T_1 = (Z_1 \,|\, W \mathop{=} w),\
T_2 = (Z_2 \,|\, W \mathop{=} w),\
T_3 = (Z_3 \,|\, W \mathop{=} w)
$$

with $Y_i=X_i$ and $\alpha=\eta/m$. Write

$$
\delta_w :=  \mathbb{I}[T_1 : T_2] + \mathbb{I}[T_1 : T_3] + \mathbb{I}[T_2 : T_3]
$$

for this choice, and note that

$$
\begin{aligned}
\delta_\ast := \sum_w p_W(w) \delta_w &= \mathbb{I}[Z_1 : Z_2 \,|\, W] + \mathbb{I}[Z_1 : Z_3 \,|\, W] + \mathbb{I}[Z_2 : Z_3 \,|\, W]\qquad\text{(8)}\\
& \leq 3 m (4m+1) \eta k
\end{aligned}
$$

by [Mutual information bound](prop-52.md). Write $U_w$ for the random variable guaranteed to exist by [Application of BSG](lem-get-better.md), so that [(6)](lem-get-better.md) gives

$$
d[U_w; U_w] \leq \Bigl( 2 + \frac{\alpha m}{2} \Bigr) \delta_w + \alpha \sum_{i=1}^m \bigl( d[X_i; T_2] - d[X_i; U_w] \bigr).\qquad\text{(9)}
$$

Let $(U_w)_I$ denote the tuple consisting of the same variable $U_w$ repeated $m$ times. By [Multidistance and Ruzsa distance, III](../multidistance/multidist-ruzsa-iii.md)

$$
D[(U_w)_I] \leq m d[U_w; U_w].\qquad\text{(10)}
$$

On the other hand, from [Lower bound on multidistance](../the-tau-functional/multidist-lower.md) one has

$$
D[(U_w)_I] \geq k - \eta \sum_{i=1}^m d[X_i;U_w].\qquad\text{(11)}
$$

Combining (9), (10) and (11) and averaging over $w$ (with weight $p_W(w)$), and recalling the value $\alpha=\eta/m$, gives

$$
m \Bigl( 2 + \frac{\eta}{2} \Bigr) \delta_\ast + \eta \sum_{i=1}^m d[X_i; Z_2 | W]
\geq k
$$

since the terms $d[X_i; U_w]$ cancel by our choice of $\alpha$. Substituting in [Distance bound](xi-z2-w-dist.md) and (8), and using the fact that $2 + \frac{\eta}{2} < 3$, we have

$$
3 m^2 (4m+1) (2+\frac{\eta}{2}) \eta k + \eta 8(m^3-m^2) k \geq k.
$$

From [$\eta$](../the-tau-functional/eta-def-multi.md) we have we have

$$
3 m^2 (4m+1) (2+\frac{\eta}{2}) \eta + \eta 8(m^3-m^2) < 1
$$

and hence $k \leq 0$. The claim now follows from [Nonnegativity](../multidistance/multidist-nonneg.md).

## Lean

Formalized as [`k_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/k_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 820](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L820)
