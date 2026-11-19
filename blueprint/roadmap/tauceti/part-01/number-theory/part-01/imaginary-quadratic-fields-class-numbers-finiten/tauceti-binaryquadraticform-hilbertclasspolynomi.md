---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.hilbertClassPolynomial
statement: formalized
---

# TauCeti.BinaryQuadraticForm.hilbertClassPolynomial

The **Hilbert class polynomial** of discriminant `-n`: the product of `X - j(τ)` over the
roots `τ = (-b + i √n) / (2 a)` of the primitive reduced forms `a x² + b x y + c y²` of
discriminant `-n`. Each proper class of primitive positive definite forms contains exactly one
primitive reduced form, so the roots are the singular moduli of discriminant `-n`.

```lean
TauCeti.BinaryQuadraticForm.hilbertClassPolynomial (n : ℕ) [NeZero n] : Polynomial ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.hilbertClassPolynomial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.html#TauCeti.BinaryQuadraticForm.hilbertClassPolynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.hilbertClassPolynomial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.html#TauCeti.BinaryQuadraticForm.hilbertClassPolynomial)
- [Source of `TauCeti.BinaryQuadraticForm.hilbertClassPolynomial` in TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.lean#L171)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
