---
declaration: theorem
origin: cited
lean: TauCeti.length_quotient_lsmul_le_finrank_mul_ord
statement: formalized
proof: formalized
---

# Krull–Akizuki's length bound

For any `A`-submodule `M` of a finite-dimensional
`K`-vector space `V` — finitely generated or not — and any nonzero `a : A`,
`length (M ⧸ aM) ≤ dim_K V * ord_A a`.

```lean
TauCeti.length_quotient_lsmul_le_finrank_mul_ord.{u_1, u_2, u_3} {A : Type u_1} [CommRing A]
  [IsDomain A] {K : Type u_2} [Field K] [Algebra A K] [IsFractionRing A K] {V : Type u_3}
  [AddCommGroup V] [_root_.Module K V] [_root_.Module A V] [IsScalarTower A K V]
  [IsNoetherianRing A] [Ring.KrullDimLE 1 A] [Module.Finite K V] (M : Submodule A V) (a : A)
  (ha : a ≠ 0) :
  Module.length A (↥M ⧸ ((LinearMap.lsmul A ↥M) a).range) ≤ ↑(Module.finrank K V) * Ring.ord A a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.length_quotient_lsmul_le_finrank_mul_ord`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.length_quotient_lsmul_le_finrank_mul_ord).

## Sources

- [Tau Ceti documentation: `TauCeti.length_quotient_lsmul_le_finrank_mul_ord`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.html#TauCeti.length_quotient_lsmul_le_finrank_mul_ord)
- [Source of `TauCeti.length_quotient_lsmul_le_finrank_mul_ord` in TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/IntegralClosure/NormalizationFinite.lean#L265)
