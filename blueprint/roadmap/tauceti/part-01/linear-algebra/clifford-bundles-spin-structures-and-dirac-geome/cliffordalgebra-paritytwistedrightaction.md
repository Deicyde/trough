---
declaration: def
origin: cited
lean: CliffordAlgebra.parityTwistedRightAction
statement: formalized
---

# CliffordAlgebra.parityTwistedRightAction

The action of the opposite-sign Clifford algebra on the regular module of `Q`, extending
the operators `s ↦ involute s * ι Q v`. No definiteness or dimension hypothesis is needed.

```lean
CliffordAlgebra.parityTwistedRightAction.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommRing R]
  [AddCommGroup M] [_root_.Module R M] (Q : QuadraticForm R M) :
  CliffordAlgebra (-Q) →ₐ[R] Module.End R (CliffordAlgebra Q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.parityTwistedRightAction`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Basic.html#CliffordAlgebra.parityTwistedRightAction).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.parityTwistedRightAction`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Basic.html#CliffordAlgebra.parityTwistedRightAction)
- [Source of `CliffordAlgebra.parityTwistedRightAction` in TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Basic.lean#L64)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
