---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff
statement: formalized
proof: formalized
---

# The infinite part of the conductor is the set of real signs

A real place `w` divides the
conductor of a finite-order Hecke character exactly when its real parity at `w` is one, that is,
when the character is nontrivial on the negative elements of `K_w`.

```lean
TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff.{u_1} {K : Type u_1}
  [Field K] [NumberField K] {χ : TauCeti.GlobalNumberFields.HeckeCharacter K} (hχ : χ.IsFiniteOrder)
  (w : { w // w.IsReal }) : w ∈ (χ.conductor hχ).infinitePart ↔ χ.infinityType.realParity w = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Finite-order Hecke characters are exactly the ray class characters](finite-order-hecke-characters-are-exactly-the-ra.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](isdedekinddomain-finiteadelering-sintegraladeles.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/RealParity.html#TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/RealParity.html#TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff)
- [Source of `TauCeti.GlobalNumberFields.HeckeCharacter.mem_conductor_infinitePart_iff` in TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/RealParity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/HeckeCharacter/RealParity.lean#L76)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/GlobalNumberFields/STATUS.md)
