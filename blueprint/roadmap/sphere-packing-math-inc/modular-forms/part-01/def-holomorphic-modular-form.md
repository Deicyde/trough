---
declaration: definition
origin: cited
lean: ModularForm
statement: formalized
---

# holomorphic-modular-form

Let $\Gamma$ denote a subgroup of $\mathrm{SL}_2(\mathbb{Z})$, then a modular form of level $\Gamma$ and weight $k \in \mathbb{Z}$ is a function $f : \mathbb{H} \to \mathbb{C}$ such that:

1. For all $\gamma \in \Gamma$ we have $f\mid_k \gamma = f$ (such functions are called slash invariant).
2. $f$ is holomorphic on $\mathbb{H}$.
3. For all $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, there exist $A, B \in \mathbb{R}$ such that for all $z \in \mathbb{H}$, with $A \le \mathrm{Im}(z)$, we have $|(f \mid_k \gamma) (z) |\le B$. Here $| - |$ denotes the standard complex absolute value.

## Depends on

- [congruence-subgroup](def-congruence-subgroup.md)

## Lean

Formalized as [`ModularForm`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularForm).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 88](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L88)
