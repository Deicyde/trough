---
declaration: theorem
origin: cited
lean: FreeGroup.posSemidef_pow_norm_inv_mul
statement: formalized
proof: formalized
---

# Haagerup's lemma

For `|r| ≤ 1`, the function `g ↦ r ^ norm g` on a free group is positive
definite: the kernel `(g, h) ↦ r ^ norm (g⁻¹ * h)` is positive semidefinite.

```lean
FreeGroup.posSemidef_pow_norm_inv_mul.{u_1, u_2} {α : Type u_1} [DecidableEq α] {𝕜 : Type u_2}
  [RCLike 𝕜] {r : ℝ} (hr : |r| ≤ 1) : Matrix.PosSemidef fun g h => ↑(r ^ (g⁻¹ * h).norm)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Haagerup's cocycle identity](haagerups-cocycle-identity.md)

## Lean

Formalized in Tau Ceti as [`FreeGroup.posSemidef_pow_norm_inv_mul`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.html#FreeGroup.posSemidef_pow_norm_inv_mul).

## Sources

- [Tau Ceti documentation: `FreeGroup.posSemidef_pow_norm_inv_mul`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.html#FreeGroup.posSemidef_pow_norm_inv_mul)
- [Source of `FreeGroup.posSemidef_pow_norm_inv_mul` in TauCeti/GroupTheory/FreeGroup/GeodesicEdges.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.lean#L297)
