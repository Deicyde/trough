---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: iteratedDeriv
mathlib_file: Mathlib/Analysis/Calculus/IteratedDeriv/Defs.lean
---

# Higher-order derivatives of functions

The `n`-th iterated derivative of a function from `𝕜` to `F`, as a function from `𝕜` to `F`.

```lean
iteratedDeriv.{u_1, u_2} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (n : ℕ) (f : 𝕜 → F) (x : 𝕜) : F
```

## Depends on

- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Multilinear map](../../../overview/linear-algebra/fundamentals/multilinear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `iteratedDeriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/IteratedDeriv/Defs.html#iteratedDeriv)
- [Source of `iteratedDeriv` in Mathlib/Analysis/Calculus/IteratedDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/IteratedDeriv/Defs.lean#L54)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L320)
