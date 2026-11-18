---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic
statement: formalized
---

# TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic

Proper classes of primitive forms of positive nonsquare discriminant `D` are in bijection
with the narrow Picard group of the quadratic order of discriminant `D`, via
`properClassToNarrowPic`.

```lean
TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic (D : ℤ) (hD : D % 4 = 0 ∨ D % 4 = 1)
  [Fact ¬IsSquare D] (hpos : 0 < D) :
  MulAction.orbitRel.Quotient (Matrix.SpecialLinearGroup (Fin 2) ℤ)
      ↥(TauCeti.BinaryQuadraticForm.primitiveForms D) ≃
    TauCeti.GlobalNumberFields.NarrowPic (TauCeti.QuadraticOrder.numberFieldOrder D hD)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.html#TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.html#TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic)
- [Source of `TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.lean#L119)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
