---
declaration: theorem
origin: cited
lean: Matrix.nonempty_cartanRealization
statement: formalized
proof: formalized
---

# Matrix.nonempty_cartanRealization

Every square matrix admits a realization attaining the dimension bound, in a coordinate
space. In particular this constructs minimal rational realizations of singular Cartan matrices.

```lean
Matrix.nonempty_cartanRealization.{u_1, u_2} {I : Type u_1} {K : Type u_2} [Fintype I] [Field K]
  (A : Matrix I I K) :
  Nonempty (TauCeti.CartanRealization A (Fin (2 * Fintype.card I - A.rank) → K))
```

## Depends on

- [TauCeti.CartanRealization](tauceti-cartanrealization.md)

## Lean

Formalized in Tau Ceti as [`Matrix.nonempty_cartanRealization`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#Matrix.nonempty_cartanRealization).

## Sources

- [Tau Ceti documentation: `Matrix.nonempty_cartanRealization`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.html#Matrix.nonempty_cartanRealization)
- [Source of `Matrix.nonempty_cartanRealization` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L587)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KacMoody/STATUS.md)
