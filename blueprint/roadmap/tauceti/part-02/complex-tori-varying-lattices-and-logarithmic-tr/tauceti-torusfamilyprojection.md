---
declaration: def
origin: cited
lean: TauCeti.torusFamilyProjection
statement: formalized
---

# TauCeti.torusFamilyProjection

The projection `(Y × E)/Λ → Y` of the family of tori to its parameter space, descended from
`Prod.fst` along the period translation action.

```lean
TauCeti.torusFamilyProjection.{u_4, u_5, u_6} {Y : Type u_4} {Λ : Type u_5} [AddCommGroup Λ]
  {E : Type u_6} [AddCommGroup E] (P : Y → Λ →ₗ[ℤ] E) : AddAction.orbitRel.Quotient Λ (Y × E) → Y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyProjection`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.torusFamilyProjection).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyProjection`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.torusFamilyProjection)
- [Source of `TauCeti.torusFamilyProjection` in TauCeti/Algebra/Module/ZLattice/Family/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Family/Basic.lean#L282)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
