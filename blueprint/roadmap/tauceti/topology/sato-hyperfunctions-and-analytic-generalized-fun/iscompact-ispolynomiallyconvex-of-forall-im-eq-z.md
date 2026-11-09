---
declaration: theorem
origin: cited
lean: IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero
statement: formalized
proof: formalized
---

# IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero

Every compact subset of the real locus `ℝⁿ ⊆ ℂⁿ` is polynomially convex.

```lean
IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero.{u_1} {ι : Type u_1} {K : Set (ι → ℂ)}
  [Finite ι] (hK : IsCompact K) (hreal : ∀ w ∈ K, ∀ (i : ι), (w i).im = 0) :
  TauCeti.IsPolynomiallyConvex K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PolynomialHull/Basic.html#IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero).

## Sources

- [Tau Ceti documentation: `IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PolynomialHull/Basic.html#IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero)
- [Source of `IsCompact.isPolynomiallyConvex_of_forall_im_eq_zero` in TauCeti/Analysis/Complex/PolynomialHull/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PolynomialHull/Basic.lean#L282)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Hyperfunctions/STATUS.md)
