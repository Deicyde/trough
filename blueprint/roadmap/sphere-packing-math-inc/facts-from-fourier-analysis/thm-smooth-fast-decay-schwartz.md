---
declaration: theorem
origin: cited
lean: RadialSchwartz.Bridge.schwartzMap_norm_sq_of_contDiff_decay_nonneg
statement: formalized
proof: formalized
---

# smooth-fast-decay-schwartz

Assume $f : \mathbb{R} \to \mathbb{C}$ is smooth on $[0, \infty)$ and for all $k, n \in \mathbb{N}$, there exists $C \in \mathbb{R}$ such that

$$
x^{\frac{k}{2}} \cdot |f^{(n)}(x)| \leq C.
$$

Then, for all $d \in \mathbb{N}$, the function

$$
f_d : \mathbb{R}^d \to \mathbb{C}, \quad f_d(x) := f(\|x\|^2)
$$

is a Schwartz function.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is formalized in Lean as `RadialSchwartz.Bridge.schwartzMap_norm_sq_of_contDiff_decay_nonneg`.

## Lean

Formalized as [`RadialSchwartz.Bridge.schwartzMap_norm_sq_of_contDiff_decay_nonneg`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/RadialSchwartz.Bridge.schwartzMap_norm_sq_of_contDiff_decay_nonneg).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 62](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L62)
