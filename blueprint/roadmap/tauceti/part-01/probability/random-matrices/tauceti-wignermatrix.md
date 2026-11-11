---
declaration: def
origin: cited
lean: TauCeti.wignerMatrix
statement: formalized
---

# TauCeti.wignerMatrix

The normalised Wigner matrix `Wₙ/√n` built from the top-left `n × n` corner of an infinite
array: complex entries `ξ` above the diagonal, their conjugates below it, and real entries `η` on
it. A real symmetric Wigner matrix is the case of real-valued `ξ`.

```lean
TauCeti.wignerMatrix.{u_1} {Ω : Type u_1} (ξ : TauCeti.StrictUpper → Ω → ℂ) (η : ℕ → Ω → ℝ) (n : ℕ)
  (ω : Ω) : Matrix (Fin n) (Fin n) ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.wignerMatrix`](https://taucetiproject.org/docs/TauCeti/Probability/RandomMatrix/Wigner.html#TauCeti.wignerMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.wignerMatrix`](https://taucetiproject.org/docs/TauCeti/Probability/RandomMatrix/Wigner.html#TauCeti.wignerMatrix)
- [Source of `TauCeti.wignerMatrix` in TauCeti/Probability/RandomMatrix/Wigner.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/RandomMatrix/Wigner.lean#L69)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
