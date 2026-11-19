---
declaration: def
origin: cited
lean: WeierstrassCurve.VariableChange.semidirectProductEquiv
statement: formalized
---

# WeierstrassCurve.VariableChange.semidirectProductEquiv

The full coordinate-change group is the semidirect product of the Heisenberg group
and the units. This is an isomorphism over every commutative ring, including the zero ring.

```lean
WeierstrassCurve.VariableChange.semidirectProductEquiv.{u_1} (R : Type u_1) [CommRing R] :
  TauCeti.HeisenbergGroup R ⋊[WeierstrassCurve.VariableChange.heisenbergAction R] Rˣ ≃*
    WeierstrassCurve.VariableChange R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.VariableChange.semidirectProductEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/SemidirectProduct.html#WeierstrassCurve.VariableChange.semidirectProductEquiv).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.VariableChange.semidirectProductEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/SemidirectProduct.html#WeierstrassCurve.VariableChange.semidirectProductEquiv)
- [Source of `WeierstrassCurve.VariableChange.semidirectProductEquiv` in TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/SemidirectProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/SemidirectProduct.lean#L116)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
