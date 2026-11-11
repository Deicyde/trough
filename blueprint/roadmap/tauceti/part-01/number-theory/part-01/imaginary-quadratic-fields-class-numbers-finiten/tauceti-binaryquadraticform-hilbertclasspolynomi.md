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
- [Source of `TauCeti.BinaryQuadraticForm.hilbertClassPolynomial` in TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/BinaryQuadraticForm/HilbertClassPolynomial.lean#L171)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
