---
declaration: theorem
origin: cited
lean: BialgHom.algebraEtale_coinvariants_centralizer_normalizer
statement: formalized
proof: formalized
---

# BialgHom.algebraEtale_coinvariants_centralizer_normalizer

The represented quotient of the scheme normalizer by the scheme centralizer
is étale, retaining the full subgroup schemes even when `D(X)` is nonreduced.

```lean
BialgHom.algebraEtale_coinvariants_centralizer_normalizer.{u} {k : Type u} [Field k] [IsAlgClosed k]
  {H : TauCeti.FiniteTypeCommHopfAlgCat k} {X : Type u} [CommGroup X]
  (π : ↑H.obj →ₐc[k] MonoidAlgebra k X) (hπ : Function.Surjective ⇑π)
  [IsReduced ↑(H.quotient (π.normalizerHopfIdeal hπ)).obj] :
  Algebra.Etale k
    ↥(π.centralizerHopfIdeal.map
          (Bialgebra.Quotient.mkBialgHom (π.normalizerHopfIdeal hπ).toIdeal)).coinvariants
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`BialgHom.algebraEtale_coinvariants_centralizer_normalizer`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/Quotient.html#BialgHom.algebraEtale_coinvariants_centralizer_normalizer).

## Sources

- [Tau Ceti documentation: `BialgHom.algebraEtale_coinvariants_centralizer_normalizer`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/Quotient.html#BialgHom.algebraEtale_coinvariants_centralizer_normalizer)
- [Source of `BialgHom.algebraEtale_coinvariants_centralizer_normalizer` in TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/Quotient.lean#L73)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
