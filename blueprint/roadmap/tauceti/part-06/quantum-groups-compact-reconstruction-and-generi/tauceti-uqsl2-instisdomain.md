---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.instIsDomain
statement: formalized
proof: formalized
---

# TauCeti.UqSl2.instIsDomain

For a nonzero parameter, `UqSl2 q` is a domain: both twists of its Ore tower are injective,
and an Ore extension of a domain by an injective twist is a domain. In particular the
presentation is nontrivial.

```lean
TauCeti.UqSl2.instIsDomain (q : ℂ) [Fact (q ≠ 0)] : IsDomain (TauCeti.UqSl2 q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.OreExtension](tauceti-oreextension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.instIsDomain`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/OreTower.html#TauCeti.UqSl2.instIsDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.instIsDomain`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/OreTower.html#TauCeti.UqSl2.instIsDomain)
- [Source of `TauCeti.UqSl2.instIsDomain` in TauCeti/QuantumGroups/UqSl2/OreTower.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/OreTower.lean#L347)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
