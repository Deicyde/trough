---
declaration: theorem
origin: cited
lean: tau_strictly_decreases
statement: formalized
proof: formalized
---

# $\tau$-decrement

Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Constructing good variables, II](construct-good.md)
- [Key identity](key-ident.md)
- [Bound on conditional mutual informations](uvw-s.md)
- [Bound on distance increments](total-dist.md)
- [First estimate](../first-estimate/first-estimate.md)

## Proof

Set $k := d[X_1;X_2]$. Applying [Constructing good variables, II](construct-good.md) with any random variables $(T_1,T_2,T_3)$ such that $T_1+T_2+T_3=0$ holds identically, we deduce that

$$
k \leq \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_1;T_j] - d[X^0_i;X_i]) \biggr).
$$

Note that $\delta$ is still defined by [(1)](README.md) and thus depends on $T_1,T_2,T_3$. In particular we may apply this for

$$
T_1 = (U | S = s),\qquad T_2 = (V | S = s), \qquad T_3 = (W | S = s)
$$

for $s$ in the range of $S$ (which is a valid choice by [Key identity](key-ident.md)) and then average over $s$ with weights $p_S(s)$, to obtain

$$
k \leq \tilde \delta + \frac{\eta}{3} \biggl( \tilde \delta + \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \bigl(  d[X^0_i;A|S] - d[X^0_i;X_i]\bigr) \biggr),
$$

where

$$
\tilde \delta :=  \mathbb{I}[U : V | S] + \mathbb{I}[V : W | S] + \mathbb{I}[W : U | S].
$$

Putting this together with [Bound on conditional mutual informations](uvw-s.md) and [Bound on distance increments](total-dist.md), we conclude that

$$
\begin{aligned}
k &\leq \Bigl(1+\frac{\eta}{3}\Bigr)\Bigl(6\eta k-\frac{1-5\eta}{1-\eta}(2\eta k-I_1)\Bigr)+\frac{\eta}{3}\Bigl((6-3\eta)k+3(2\eta k-I_1)\Bigr)\\
&= (8\eta + \eta^2) k - \biggl( \frac{1 - 5 \eta}{1-\eta}\Bigl(1 + \frac{\eta}{3}\Bigr) -  \eta \biggr)(2 \eta k - I_1)\\
&\leq (8 \eta + \eta^2) k
\end{aligned}
$$

since the quantity $2 \eta k - I_1$ is non-negative (by [First estimate](../first-estimate/first-estimate.md)), and its coefficient in the above expression is non-positive provided that $\eta(2\eta + 17) \le 3$, which is certainly the case with [Definition eta-def](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L3). Moreover, from [Definition eta-def](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L3) we have $8 \eta + \eta^2 < 1$. It follows that $k=0$, as desired.

## Lean

Formalized as [`tau_strictly_decreases`](https://teorth.github.io/pfr/docs/find/#doc/tau_strictly_decreases).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 382](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L382)
