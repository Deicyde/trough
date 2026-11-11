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
- [Source of `Submodule.natCard_mul_weightEnumerator_euclideanDual` in TauCeti/InformationTheory/Coding/MacWilliams/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/InformationTheory/Coding/MacWilliams/Basic.lean#L128)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
