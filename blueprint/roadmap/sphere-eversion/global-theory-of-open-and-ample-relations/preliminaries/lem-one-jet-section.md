---
declaration: lemma
origin: cited
lean: ContMDiff.oneJetExt
statement: formalized
proof: formalized
---

# one_jet_section

For every smooth map $f \!: M → N$,

1. $j^1f$ is smooth
2. $j^1f$ is a section of $J^1(M, N) → M$

## Depends on

- [one_jet_space](def-one-jet-space.md)
- [one_jet_extension](def-one-jet-extension.md)

## Proof

Points 2 and 3 are obvious by construction.

To show that $j^1f$ is smooth, suppose that $M$ is modelled over $E$ with charts $C_x : M \to E$ and coordinate change functions $C_{x,x'}=C_{x'}C_x^{-1} : E \to E$ and similarly let $C'_y$ be charts for $N$. By construction of the 1-jet bundle, we need to check that for each $x_0$ the map

$$
x\mapsto TC'_{f(x),f(x_0)}\circ T(C'_{f(x)}fC_x^{-1})\circ
T_{C_{x_0}(x)}(C_{x_0,x}): M \to L(E,E)
$$

is smooth at $x_0$ (we occasionally omit the point where the tangent maps are taken). For $x$ close to $x_0$ the coordinate changes are smooth, so we can write

$$
\begin{aligned}
TC'_{f(x),f(x_0)}\circ T(C'_{f(x)}fC_x^{-1})\circ T(C_{x_0,x})
&= T_{C_{x_0}(x)}(C'_{f(x),f(x_0)}C'_{f(x)}fC_x^{-1}C_{x_0,x})\\
&= T_{C_{x_0}(x)}(C'_{f(x_0)}fC_{x_0})
\end{aligned}
$$

This is smooth since $C'_{f(x_0)}fC_{x_0}$ is smooth.

## Lean

Formalized as [`ContMDiff.oneJetExt`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/ContMDiff.oneJetExt).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 331](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L331)
