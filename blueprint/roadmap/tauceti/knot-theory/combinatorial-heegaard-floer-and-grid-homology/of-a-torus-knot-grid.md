---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.two_mul_tau_torusLink
statement: formalized
proof: formalized
---

# `τ` of a torus knot grid

on the standard grid of the `(p + 1, q + 1)` torus knot,
`2 τ = -p q`.

```lean
TauCeti.GridDiagram.two_mul_tau_torusLink.{u_1} {p q : ℕ} (h : (p + 1).Coprime (q + 1))
  (K : Type u_1) [Field K] [CharP K 2] : 2 * ⋯.tau K = -(↑p * ↑q)
```

## Depends on

- [The invariant `τ` of a knot grid diagram](the-invariant-of-a-knot-grid-diagram.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.two_mul_tau_torusLink`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/TorusLink/Tau.html#TauCeti.GridDiagram.two_mul_tau_torusLink).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.two_mul_tau_torusLink`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/TorusLink/Tau.html#TauCeti.GridDiagram.two_mul_tau_torusLink)
- [Source of `TauCeti.GridDiagram.two_mul_tau_torusLink` in TauCeti/KnotTheory/Grid/TorusLink/Tau.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/TorusLink/Tau.lean#L54)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
