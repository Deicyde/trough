---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic
statement: formalized
---

# TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic

Proper classes of primitive positive definite forms of discriminant `-n` are in
bijection with the Picard group of the quadratic order of discriminant `-n`.

```lean
TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  TauCeti.BinaryQuadraticForm.PosDefProperClass n ≃
    TauCeti.GlobalNumberFields.Pic (TauCeti.QuadraticOrder.numberFieldOrder (-↑n) hn)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/PicEquivalence.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/PicEquivalence.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic)
- [Source of `TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/PicEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/PicEquivalence.lean#L53)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
