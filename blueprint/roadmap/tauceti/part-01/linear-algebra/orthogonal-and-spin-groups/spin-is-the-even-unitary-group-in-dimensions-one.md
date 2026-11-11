---
declaration: theorem
origin: cited
lean: CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup
statement: formalized
proof: formalized
---

# Spin is the even unitary group in dimensions one to five

For a nondegenerate quadratic
space of dimension between one and five, the even unitary carrier lies in the Lipschitz group.
Dimension zero is excluded, and the exclusion is not decoration: there the Lipschitz group is
trivial while the even unitary carrier is `μ₂`. The bound five is sharp, by
`CliffordAlgebra.not_evenUnitaryGroup_le_lipschitzGroup_of_six_le_finrank`.

```lean
CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup.{u, v} {K : Type u} {V : Type v} [Field K]
  [AddCommGroup V] [_root_.Module K V] [Invertible 2] (Q : QuadraticForm K V)
  (hQ : QuadraticMap.Nondegenerate) (hV0 : 0 < Module.finrank K V) (hV : Module.finrank K V ≤ 5) :
  CliffordAlgebra.evenUnitaryGroup Q ≤ lipschitzGroup Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Five.html#CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Five.html#CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup)
- [Source of `CliffordAlgebra.evenUnitaryGroup_le_lipschitzGroup` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Five.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Five.lean#L123)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)
