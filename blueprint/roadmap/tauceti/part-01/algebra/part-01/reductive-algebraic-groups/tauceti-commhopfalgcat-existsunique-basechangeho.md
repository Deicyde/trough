---
declaration: theorem
origin: cited
lean: TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff

Along a Galois extension `L / k`, a Hopf ideal of `L ⊗[k] H` is the base change of a Hopf ideal
of `H` exactly when it is stable under the scalar-factor Galois action, and that Hopf ideal of `H`
is then unique. Geometrically, a closed subgroup of the base-changed group is defined over `k`
exactly when it is stable under `Gal(L / k)`.

```lean
TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff.{u, v, w} {k : Type u} {L : Type w}
  [Field k] [Field L] [Algebra k L] [IsGalois k L] {H : CommHopfAlgCat k}
  (I : TauCeti.HopfIdeal L ↑(TauCeti.CommHopfAlgCat.baseChange H)) :
  (∃! J, TauCeti.CommHopfAlgCat.baseChangeHopfIdeal J = I) ↔
    ∀ (σ : Gal(L/k)), ∀ x ∈ I, (TensorProduct.map σ.toLinearMap LinearMap.id) x ∈ I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Descent.html#TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Descent.html#TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff)
- [Source of `TauCeti.CommHopfAlgCat.existsUnique_baseChangeHopfIdeal_eq_iff` in TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/HopfIdeal/Descent.lean#L136)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
