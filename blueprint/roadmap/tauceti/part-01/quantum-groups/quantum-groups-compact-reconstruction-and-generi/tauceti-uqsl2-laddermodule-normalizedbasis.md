---
declaration: def
origin: cited
lean: TauCeti.UqSl2.LadderModule.normalizedBasis
statement: formalized
---

# TauCeti.UqSl2.LadderModule.normalizedBasis

The ladder basis divided by its positive lengths in the invariant metric.

```lean
TauCeti.UqSl2.LadderModule.normalizedBasis {q : ℝ} (hq : 0 < q) (hd : q - q⁻¹ ≠ 0) (m : ℕ) :
  Module.Basis (Fin (m + 1)) ℂ (TauCeti.UqSl2.LadderModule (↑q) m 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.LadderModule.normalizedBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LadderModule/NormalizedBasis.html#TauCeti.UqSl2.LadderModule.normalizedBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.LadderModule.normalizedBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LadderModule/NormalizedBasis.html#TauCeti.UqSl2.LadderModule.normalizedBasis)
- [Source of `TauCeti.UqSl2.LadderModule.normalizedBasis` in TauCeti/QuantumGroups/UqSl2/LadderModule/NormalizedBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/LadderModule/NormalizedBasis.lean#L47)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
