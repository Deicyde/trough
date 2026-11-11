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
- [Source of `TauCeti.diracClifford_spinGroup` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L253)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
