---
declaration: theorem
origin: cited
lean: TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective
statement: formalized
proof: formalized
---

# Distinct proper classes of primitive positive definite forms have distinct Picard classes

This is the injective half of the correspondence between proper classes of primitive positive
definite forms of discriminant `-n` and the Picard group of the order of discriminant `-n`.

```lean
TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  Function.Injective (TauCeti.BinaryQuadraticForm.posDefProperClassToPic n hn)
```

## Depends on

- [The Picard class of a proper class of primitive positive definite forms](the-picard-class-of-a-proper-class-of-primitive.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.html#TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.html#TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective)
- [Source of `TauCeti.BinaryQuadraticForm.posDefProperClassToPic_injective` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/Class.lean#L147)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
