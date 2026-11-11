---
declaration: theorem
origin: cited
lean: TauCeti.BinaryGolay.weightEnumerator_code
statement: formalized
proof: formalized
---

# TauCeti.BinaryGolay.weightEnumerator_code

The homogeneous weight enumerator is
`X²⁴ + 759 X¹⁶Y⁸ + 2576 X¹²Y¹² + 759 X⁸Y¹⁶ + Y²⁴`.

```lean
TauCeti.BinaryGolay.weightEnumerator_code :
  (↑TauCeti.BinaryGolay.code).weightEnumerator =
    MvPolynomial.X 0 ^ 24 + 759 * MvPolynomial.X 0 ^ 16 * MvPolynomial.X 1 ^ 8 +
          2576 * MvPolynomial.X 0 ^ 12 * MvPolynomial.X 1 ^ 12 +
        759 * MvPolynomial.X 0 ^ 8 * MvPolynomial.X 1 ^ 16 +
      MvPolynomial.X 1 ^ 24
```

## Depends on

- [Set.weightEnumerator](set-weightenumerator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryGolay.weightEnumerator_code`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Binary/Golay/Basic.html#TauCeti.BinaryGolay.weightEnumerator_code).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryGolay.weightEnumerator_code`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Binary/Golay/Basic.html#TauCeti.BinaryGolay.weightEnumerator_code)
- [Source of `TauCeti.BinaryGolay.weightEnumerator_code` in TauCeti/InformationTheory/Coding/Binary/Golay/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/InformationTheory/Coding/Binary/Golay/Basic.lean#L603)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
