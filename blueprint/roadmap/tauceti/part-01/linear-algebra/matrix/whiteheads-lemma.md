---
declaration: theorem
origin: cited
lean: TauCeti.fromBlocksGL_inv_mem_elementarySubgroup
statement: formalized
proof: formalized
---

# Whitehead's lemma

For an invertible matrix `u`, the block diagonal matrix `u ⊕ u⁻¹` is
elementary: it is the product of six block unipotent matrices,
`u ⊕ u⁻¹ = U(u) L(-u⁻¹) U(u) U(-1) L(1) U(-1)`.

```lean
TauCeti.fromBlocksGL_inv_mem_elementarySubgroup.{u_1, u_2} {A : Type u_1} [Ring A] {m : Type u_2}
  [DecidableEq m] [Fintype m] (u : GL m A) :
  TauCeti.fromBlocksGL (u, u⁻¹) ∈ TauCeti.elementarySubgroup (m ⊕ m) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fromBlocksGL_inv_mem_elementarySubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Elementary.html#TauCeti.fromBlocksGL_inv_mem_elementarySubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.fromBlocksGL_inv_mem_elementarySubgroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Elementary.html#TauCeti.fromBlocksGL_inv_mem_elementarySubgroup)
- [Source of `TauCeti.fromBlocksGL_inv_mem_elementarySubgroup` in TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Elementary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Elementary.lean#L252)
