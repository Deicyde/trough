---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.posDefProperClassToPic
statement: formalized
---

# The Picard class of a proper class of primitive positive definite forms

, the class of
`aℤ + ((-b + √(-n))/2)ℤ` in the Picard group of the quadratic order of discriminant `-n`.

```lean
TauCeti.BinaryQuadraticForm.posDefProperClassToPic (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  TauCeti.BinaryQuadraticForm.PosDefProperClass n →
    TauCeti.GlobalNumberFields.Pic (TauCeti.QuadraticOrder.numberFieldOrder (-↑n) hn)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.posDefProperClassToPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.html#TauCeti.BinaryQuadraticForm.posDefProperClassToPic).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.posDefProperClassToPic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.html#TauCeti.BinaryQuadraticForm.posDefProperClassToPic)
- [Source of `TauCeti.BinaryQuadraticForm.posDefProperClassToPic` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.lean#L134)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
