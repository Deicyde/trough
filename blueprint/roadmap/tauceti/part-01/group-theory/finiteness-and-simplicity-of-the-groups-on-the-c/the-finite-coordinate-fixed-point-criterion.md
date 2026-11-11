---
declaration: theorem
origin: cited
lean: TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow
statement: formalized
proof: formalized
---

# The finite-coordinate fixed-point criterion

Let `ρ` embed a group `G` in the square
matrices over an integral domain, and let `F` be an endomorphism of `G`. If an iterate `F^[r]`
raises every matrix coordinate to the power `m > 1`, then the fixed subgroup of `F` is finite: the
coordinates of a fixed point are roots of `X ^ m - X`.

```lean
TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow.{u_1, u_2, u_3} {G : Type u_1} [Group G]
  {n : Type u_2} [Finite n] {K : Type u_3} [CommRing K] [IsDomain K] (ρ : G → Matrix n n K)
  (hρ : Function.Injective ρ) (F : G →* G) (r : ℕ) {m : ℕ} (hm : 1 < m)
  (hF : ∀ (g : G) (i j : n), ρ ((⇑F)^[r] g) i j = ρ g i j ^ m) : Finite ↥(TauCeti.fixedSubgroup F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedSubgroup/MatrixCoordinates.html#TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FixedSubgroup/MatrixCoordinates.html#TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow)
- [Source of `TauCeti.finite_fixedSubgroup_of_iterate_apply_eq_pow` in TauCeti/GroupTheory/FixedSubgroup/MatrixCoordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FixedSubgroup/MatrixCoordinates.lean#L61)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
