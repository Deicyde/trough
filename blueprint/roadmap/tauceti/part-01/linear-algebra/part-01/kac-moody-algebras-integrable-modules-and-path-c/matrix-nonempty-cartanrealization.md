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
- [Source of `Matrix.nonempty_cartanRealization` in TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/Cartan/Realization/Basic.lean#L599)
- [Tau Ceti roadmap status: Kac–Moody algebras, integrable modules and path crystals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KacMoody/STATUS.md)
