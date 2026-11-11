---
declaration: theorem
origin: cited
lean: TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron
statement: formalized
proof: formalized
---

# TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron

A compact polynomially convex set `K ⊆ ℂⁿ` lies in the interior of a polynomial polyhedron
contained in any given open neighbourhood `U` of `K`.

```lean
TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron.{u_1} {ι : Type u_1}
  {K : Set (ι → ℂ)} [Fintype ι] (hKc : TauCeti.IsPolynomiallyConvex K) (hK : IsCompact K)
  {U : Set (ι → ℂ)} (hU : IsOpen U) (hKU : K ⊆ U) :
  ∃ R s,
    0 < R ∧ K ⊆ interior (TauCeti.polynomialPolyhedron R s) ∧ TauCeti.polynomialPolyhedron R s ⊆ U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PolynomialHull/Basic.html#TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PolynomialHull/Basic.html#TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron)
- [Source of `TauCeti.IsPolynomiallyConvex.exists_subset_interior_polynomialPolyhedron` in TauCeti/Analysis/Complex/PolynomialHull/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PolynomialHull/Basic.lean#L411)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Hyperfunctions/STATUS.md)
