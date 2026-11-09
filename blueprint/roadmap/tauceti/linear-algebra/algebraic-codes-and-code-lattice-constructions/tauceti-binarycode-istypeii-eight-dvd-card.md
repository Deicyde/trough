---
declaration: theorem
origin: cited
lean: TauCeti.BinaryCode.IsTypeII.eight_dvd_card
statement: formalized
proof: formalized
---

# TauCeti.BinaryCode.IsTypeII.eight_dvd_card

A Type II binary code has length divisible by eight.

```lean
TauCeti.BinaryCode.IsTypeII.eight_dvd_card.{u_1} {ι : Type u_1} [Fintype ι]
  {C : TauCeti.LinearCode (ZMod 2) ι} (hC : TauCeti.BinaryCode.IsTypeII C) : 8 ∣ Fintype.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The MacWilliams identity](the-macwilliams-identity.md)
- [Set.weightEnumerator](set-weightenumerator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryCode.IsTypeII.eight_dvd_card`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Binary/TypeII.html#TauCeti.BinaryCode.IsTypeII.eight_dvd_card).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryCode.IsTypeII.eight_dvd_card`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Binary/TypeII.html#TauCeti.BinaryCode.IsTypeII.eight_dvd_card)
- [Source of `TauCeti.BinaryCode.IsTypeII.eight_dvd_card` in TauCeti/InformationTheory/Coding/Binary/TypeII.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/InformationTheory/Coding/Binary/TypeII.lean#L111)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AlgebraicCodingTheory/STATUS.md)
