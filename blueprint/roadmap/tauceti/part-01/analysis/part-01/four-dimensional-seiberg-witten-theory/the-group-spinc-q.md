---
declaration: abbrev
origin: cited
lean: CliffordAlgebra.spinCGroup
statement: formalized
---

# The group `Spinᶜ(Q)`

the quotient `(Spin(Q) × U(1)) / {1, (-1, -1)}`. For
`Q v = -‖v‖²` on a real inner product space of dimension `n`, this is `Spinᶜ(n)`, the structure
group of a `Spinᶜ` structure.

```lean
CliffordAlgebra.spinCGroup.{u_1} {M : Type u_1} [AddCommGroup M] [_root_.Module ℝ M]
  (Q : QuadraticForm ℝ M) (hQ : Q ≠ 0) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.spinCGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinC.html#CliffordAlgebra.spinCGroup).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.spinCGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinC.html#CliffordAlgebra.spinCGroup)
- [Source of `CliffordAlgebra.spinCGroup` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinC.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinC.lean#L152)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
