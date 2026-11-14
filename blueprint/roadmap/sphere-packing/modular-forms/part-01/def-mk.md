---
declaration: definition
origin: cited
lean: ModularForm
statement: formalized
---

# Mk

Let $\Gamma$ denote a subgroup of $\mathrm{SL}_2(\mathbb{Z})$, then a modular form of level $\Gamma$ and weight $k \in \mathbb{Z}$ is a function $f : \mathbb{H} \to \mathbb{C}$ such that:

1. For all $\gamma \in \Gamma$ we have $f\mid_k \gamma = f$ (such functions are called slash invariant).
2. $f$ is holomorphic on $\mathbb{H}$.
3. For all $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, there exist $A, B \in \mathbb{R}$ such that for all $z \in \mathbb{H}$, with $A \le \mathrm{Im}(z)$, we have $|(f \mid_k \gamma) (z) |\le B$. Here $| - |$ denotes the standard complex absolute value.

This defines a complex vector space which we denote by $M_{k}(\Gamma)$.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ModularForm`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularForm).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 94](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L94)
