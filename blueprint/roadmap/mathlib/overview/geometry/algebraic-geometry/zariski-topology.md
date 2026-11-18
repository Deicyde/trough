# Zariski topology

The Zariski topology on the prime spectrum of a commutative (semi)ring is defined
via the closed sets of the topology: they are exactly those sets that are the zero locus
of a subset of the ring.

```lean
PrimeSpectrum.zariskiTopology.{u} {R : Type u} [CommSemiring R] : TopologicalSpace (PrimeSpectrum R)
```

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)
- [Prime spectrum](prime-spectrum.md)
- [Topological space](../../topology/general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `PrimeSpectrum.zariskiTopology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Spectrum/Prime/Topology.html#PrimeSpectrum.zariskiTopology)
- [Source of `PrimeSpectrum.zariskiTopology` in Mathlib/RingTheory/Spectrum/Prime/Topology.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/RingTheory/Spectrum/Prime/Topology.lean#L121)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L482)
