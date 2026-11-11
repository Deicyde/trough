---
declaration: theorem
origin: cited
lean: TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective
statement: formalized
proof: formalized
---

# Ideal representatives of the Picard group

The Picard classes of the ideals
`aℤ + ((-b + √(-n))/2)ℤ` of the primitive reduced forms `(a, b, c)` of discriminant `-n` are all
the elements of the Picard group of the order of discriminant `-n`, each exactly once.

```lean
TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  Function.Bijective fun f => TauCeti.BinaryQuadraticForm.picClass (-↑n) hn ⟨↑f, ⋯⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/ClassNumber.html#TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/ClassNumber.html#TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective)
- [Source of `TauCeti.BinaryQuadraticForm.picClass_primitiveReducedForms_bijective` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/ClassNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/ClassNumber.lean#L90)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
