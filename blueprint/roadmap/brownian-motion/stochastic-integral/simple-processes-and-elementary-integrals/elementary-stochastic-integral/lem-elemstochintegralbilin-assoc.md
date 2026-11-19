---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.integral_assoc
statement: formalized
proof: formalized
---

# elemStochIntegralBilin_assoc

Let $E, F, G, H, I, J$ be normed real vector spaces. Let $B_1 : E \times H \to I$, $B_2 : F \times G \to H$, $B_3 : E \times F \to J$ and $B_4 : J \times G \to I$ be continuous bilinear maps such that for all $x \in E$, $y \in F$ and $z \in G$, $B_1(x, B_2(y, z)) = B_4(B_3(x, y), z)$. Then for every simple process $V$ with values in $E$, simple process $W$ with values in $F$, and stochastic process $X$ with values in $G$, we have

$$
\begin{aligned}
V \bullet_{B_1} (W \bullet_{B_2} X)
&= B_3(V, W) \bullet_{B_4} X
\: .
\end{aligned}
$$

## Depends on

- [Elementary stochastic integral](def-elemstochintegralbilin.md)
- [simpleProcess_map2](lem-simpleprocess-map2.md)

## Proof depends on

- [elemStochIntegral_linear](lem-elemstochintegral-linear.md)

## Proof

Unfold definitions, use linearity.

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.integral_assoc`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_assoc).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 471](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L471)
