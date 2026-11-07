---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter
statement: formalized
proof: formalized
---

# Finite-order Hecke characters are exactly the ray class characters

a Hecke character has
finite order exactly when it is the pullback of a ray class character of some modulus.

```lean
TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter.{u_1}
  {K : Type u_1} [Field K] [NumberField K] (χ : TauCeti.GlobalNumberFields.HeckeCharacter K) :
  χ.IsFiniteOrder ↔ ∃ 𝔪 η, (TauCeti.GlobalNumberFields.HeckeCharacter.ofRayClassCharacter 𝔪) η = χ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](isdedekinddomain-finiteadelering-sintegraladeles.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.html#TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.html#TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter)
- [Source of `TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter` in TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.lean#L79)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/GlobalNumberFields/STATUS.md)
