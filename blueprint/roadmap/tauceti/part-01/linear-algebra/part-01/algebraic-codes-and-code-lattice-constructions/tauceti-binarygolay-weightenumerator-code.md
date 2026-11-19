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
- [Source of `TauCeti.BinaryGolay.weightEnumerator_code` in TauCeti/InformationTheory/Coding/Binary/Golay/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/InformationTheory/Coding/Binary/Golay/Basic.lean#L613)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AlgebraicCodingTheory/STATUS.md)
