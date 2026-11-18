---
declaration: theorem
origin: cited
lean: TauCeti.diracClifford_spinGroup
statement: formalized
proof: formalized
---

# TauCeti.diracClifford_spinGroup

The Clifford representation restricts on `Spin(3,1)` to the Weyl action.

```lean
TauCeti.diracClifford_spinGroup (s : ↥(spinGroup (TauCeti.realCliffordForm 3 1))) :
  TauCeti.diracClifford ↑s = TauCeti.diracWeyl s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.diracClifford_spinGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracClifford_spinGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.diracClifford_spinGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracClifford_spinGroup)
- [Source of `TauCeti.diracClifford_spinGroup` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L253)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
