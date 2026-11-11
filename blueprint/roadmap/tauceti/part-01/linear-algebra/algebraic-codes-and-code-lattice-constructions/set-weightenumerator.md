---
declaration: def
origin: cited
lean: Set.weightEnumerator
statement: formalized
---

# Set.weightEnumerator

The homogeneous Hamming weight enumerator `W_C(X, Y) = ∑_w A_w(C) X^(n-w) Y^w`, where `n`
is the length, `A_w(C)` is the weight distribution, and the variables `0, 1` are `X, Y`.

```lean
Set.weightEnumerator.{u_1, u_2} {ι : Type u_1} {β : ι → Type u_2} [Fintype ι] [(i : ι) → Zero (β i)]
  [(i : ι) → DecidableEq (β i)] (C : Set ((i : ι) → β i)) : MvPolynomial (Fin 2) ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Set.weightEnumerator`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Weight/Enumerator.html#Set.weightEnumerator).

## Sources

- [Tau Ceti documentation: `Set.weightEnumerator`](https://taucetiproject.org/docs/TauCeti/InformationTheory/Coding/Weight/Enumerator.html#Set.weightEnumerator)
- [Source of `Set.weightEnumerator` in TauCeti/InformationTheory/Coding/Weight/Enumerator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/InformationTheory/Coding/Weight/Enumerator.lean#L113)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
