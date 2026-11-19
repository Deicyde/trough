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
- [Source of `TauCeti.GlobalNumberFields.HeckeCharacter.isFiniteOrder_iff_exists_rayClassCharacter` in TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/FiniteOrder.lean#L79)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/GlobalNumberFields/STATUS.md)
