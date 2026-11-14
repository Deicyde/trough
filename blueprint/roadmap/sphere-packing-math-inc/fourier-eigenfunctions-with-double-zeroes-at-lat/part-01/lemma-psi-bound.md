---
declaration: lemma
origin: cited
lean: MagicFunction.b.PsiBounds.exists_bound_norm_ψS_resToImagAxis_Ici_one
statement: formalized
proof: formalized
---

# psi-bound

There exist constants $C_I, C_S, C_T > 0$ such that

$$
\begin{aligned}
|\psi_I(z)| &\le C_I e^{2\pi \Im z},\qquad\text{(37)}\\
|\psi_T(z)| &\le C_T e^{2\pi \Im z},\qquad\text{(38)}\\
|\psi_S(z)| &\le C_S e^{- \pi \Im z}\qquad\text{(39)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The proof is similar to that of Lemma [phi0-bound](cor-phi0-bound.md), follows from Lemma [mod-div-disc-bound](lemma-mod-div-disc-bound.md) and the fact that the vanishing orders of the numerators of $\psi_I$, $\psi_T$, and $\psi_S$ at infinity are $0$, $0$ (i.e. not cusp forms), and $\frac{3}{2}$ respectively.

## Lean

Formalized as [`MagicFunction.b.PsiBounds.exists_bound_norm_ψS_resToImagAxis_Ici_one`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.PsiBounds.exists_bound_norm_ψS_resToImagAxis_Ici_one).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 526](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L526)
