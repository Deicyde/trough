---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Finset.affineCombination
mathlib_file: Mathlib/LinearAlgebra/AffineSpace/Combination.lean
---

# Barycenter

A weighted sum of the results of subtracting a default base point
from the given points, added to that base point, as an affine map on
the weights.  This is intended to be used when the sum of the weights
is 1, in which case it is an affine combination (barycenter) of the
points with the given weights; that condition is specified as a
hypothesis on those lemmas that require it.

```lean
Finset.affineCombination.{u_1, u_2, u_3, u_4} (k : Type u_1) {V : Type u_2} {P : Type u_3} [Ring k]
  [AddCommGroup V] [_root_.Module k V] [S : AddTorsor V P] {ι : Type u_4} (s : Finset ι)
  (p : ι → P) : (ι → k) →ᵃ[k] P
```

## Depends on

- [Affine function](affine-function.md)
- [Finite set](../../data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `Finset.affineCombination`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/Combination.html#Finset.affineCombination)
- [Source of `Finset.affineCombination` in Mathlib/LinearAlgebra/AffineSpace/Combination.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/Combination.lean#L343)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L434)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › General definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L247)
