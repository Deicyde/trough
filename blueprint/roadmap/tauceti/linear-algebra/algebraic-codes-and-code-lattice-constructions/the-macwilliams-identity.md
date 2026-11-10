---
declaration: theorem
origin: cited
lean: Submodule.natCard_mul_weightEnumerator_euclideanDual
statement: formalized
proof: formalized
---

# The MacWilliams identity

for a linear code `C` over a finite field `F` with `q`
elements, `#C · W_{C⊥}(X, Y) = W_C(X + (q - 1) Y, X - Y)` in `ℤ[X, Y]`.

```lean
Submodule.natCard_mul_weightEnumerator_euclideanDual.{u_1, u_4} {ι : Type u_1} [Fintype ι]
  {F : Type u_4} [Field F] [Finite F] [DecidableEq F] (C : Submodule F (ι → F)) :
  ↑(Nat.card ↥C) * (↑C.euclideanDual).weightEnumerator =
    (MvPolynomial.aeval
        ![MvPolynomial.X 0 + (↑(Nat.card F) - 1) * MvPolynomial.X 1,
          MvPolynomial.X 0 - MvPolynomial.X 1])
      (↑C).weightEnumerator
```

## Depends on

- [Set.weightEnumerator](set-weightenumerator.md)

## Lean

Formalized in Tau Ceti as [`Submodule.natCard_mul_weightEnumerator_euclideanDual`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/MacWilliams/Basic.html#Submodule.natCard_mul_weightEnumerator_euclideanDual).

## Sources

- [Tau Ceti documentation: `Submodule.natCard_mul_weightEnumerator_euclideanDual`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/MacWilliams/Basic.html#Submodule.natCard_mul_weightEnumerator_euclideanDual)
- [Source of `Submodule.natCard_mul_weightEnumerator_euclideanDual` in TauCeti/InformationTheory/Coding/MacWilliams/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/InformationTheory/Coding/MacWilliams/Basic.lean#L128)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AlgebraicCodingTheory/STATUS.md)
