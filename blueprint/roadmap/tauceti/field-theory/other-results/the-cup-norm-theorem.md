---
declaration: theorem
origin: cited
lean: TauCeti.cup_kummerClass_eq_zero_iff
statement: formalized
proof: formalized
---

# The cup-norm theorem

For units `a` and `b` of a field in which `2` is invertible, the cup
product `(a) ∪ (b) ∈ H²(G_K, 𝔽₂)` of their Kummer classes vanishes if and only if the norm
equation `b = x² - a y²` has a solution in `K`.

```lean
TauCeti.cup_kummerClass_eq_zero_iff.{u} {K : Type u} [Field K] [Invertible 2] (a b : Kˣ) :
  (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1) (TauCeti.kummerClass a))
        (TauCeti.kummerClass b) =
      0 ↔
    ∃ x y, ↑b = x ^ 2 - ↑a * y ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The comparison isomorphism `Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous cohomology, for `K` in any universe](../../number-theory/part-01/quadratic-forms-and-cohomological-invariants/the-comparison-isomorphism-br-k-h2-cont-g-k-ks-x.md)
- [The Skolem-Noether theorem](../../algebra/central-simple/the-skolem-noether-theorem.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](../../number-theory/part-01/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cup_kummerClass_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/MuTwo/CupNorm.html#TauCeti.cup_kummerClass_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.cup_kummerClass_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/MuTwo/CupNorm.html#TauCeti.cup_kummerClass_eq_zero_iff)
- [Source of `TauCeti.cup_kummerClass_eq_zero_iff` in TauCeti/FieldTheory/GaloisCohomology/MuTwo/CupNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/MuTwo/CupNorm.lean#L100)
