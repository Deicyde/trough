---
declaration: theorem
origin: cited
lean: TauCeti.GridLink.two_mul_tau_toGridLink_torusLink
statement: formalized
proof: formalized
---

# TauCeti.GridLink.two_mul_tau_toGridLink_torusLink

The knot presented by the standard `(p + 1, q + 1)` torus grid has `2τ = -pq`.
The negative sign follows the definition of `τ` as minus the maximal non-torsion degree.

```lean
TauCeti.GridLink.two_mul_tau_toGridLink_torusLink.{u_1} (K : Type u_1) [Field K] [CharP K 2]
  {p q : ℕ} (h : (p + 1).Coprime (q + 1)) : 2 * ⋯.tau K = -(↑p * ↑q)
```

## Depends on

- [TauCeti.GridLink.IsKnot.tau](tauceti-gridlink-isknot-tau.md)

## Proof depends on

- [Invariance of `GH⁻` under grid moves](invariance-of-gh-under-grid-moves.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GridLink.two_mul_tau_toGridLink_torusLink`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Move/Tau.html#TauCeti.GridLink.two_mul_tau_toGridLink_torusLink).

## Sources

- [Tau Ceti documentation: `TauCeti.GridLink.two_mul_tau_toGridLink_torusLink`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Move/Tau.html#TauCeti.GridLink.two_mul_tau_toGridLink_torusLink)
- [Source of `TauCeti.GridLink.two_mul_tau_toGridLink_torusLink` in TauCeti/KnotTheory/Grid/Move/Tau.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/Move/Tau.lean#L75)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
