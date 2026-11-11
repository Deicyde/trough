---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic
statement: formalized
---

# TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic

Proper classes of primitive positive-discriminant forms are in bijection with the
consumed narrow Picard group through the original sign-corrected map.

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
- [Source of `TauCeti.BinaryQuadraticForm.properClassEquivNarrowPic` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Narrow/Equivalence.lean#L104)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
