---
declaration: def
origin: cited
lean: TauCeti.discreteEnergyStrictSublevel
statement: formalized
---

# TauCeti.discreteEnergyStrictSublevel

The set of interior vertex tuples `x` with fixed endpoints `p,q` whose energy
`discreteEnergy t (Fin.cons p (Fin.snoc x q))` is strictly less than `c`.

```lean
TauCeti.discreteEnergyStrictSublevel.{u_1} {M : Type u_1} [PseudoMetricSpace M] {n : ℕ}
  (t : Fin (n + 2) → ℝ) (p q : M) (c : ℝ) : Set (Fin n → M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.discreteEnergyStrictSublevel`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/DiscreteEnergy/Basic.html#TauCeti.discreteEnergyStrictSublevel).

## Sources

- [Tau Ceti documentation: `TauCeti.discreteEnergyStrictSublevel`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/DiscreteEnergy/Basic.html#TauCeti.discreteEnergyStrictSublevel)
- [Source of `TauCeti.discreteEnergyStrictSublevel` in TauCeti/Topology/MetricSpace/DiscreteEnergy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/MetricSpace/DiscreteEnergy/Basic.lean#L202)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
