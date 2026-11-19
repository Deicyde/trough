---
declaration: def
origin: cited
lean: TauCeti.TriangleGroup.mirror
statement: formalized
---

# TauCeti.TriangleGroup.mirror

The mirror automorphism of `Δ(a, b, c)`, sending `x, y, z` to `y * x⁻¹ * y⁻¹`, `y⁻¹` and
`z⁻¹`. It is an involution (`TauCeti.TriangleGroup.mirror_mirror`). On the images of the
generators it is the mirror `(σ0, σ1, σinf) ↦ (σ1 σ0⁻¹ σ1⁻¹, σ1⁻¹, σinf⁻¹)` of permutation
triples.

```lean
TauCeti.TriangleGroup.mirror {a b c : ℕ} :
  TauCeti.TriangleGroup a b c ≃* TauCeti.TriangleGroup a b c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TriangleGroup.mirror`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/Basic.html#TauCeti.TriangleGroup.mirror).

## Sources

- [Tau Ceti documentation: `TauCeti.TriangleGroup.mirror`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/Basic.html#TauCeti.TriangleGroup.mirror)
- [Source of `TauCeti.TriangleGroup.mirror` in TauCeti/GroupTheory/TriangleGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/TriangleGroup/Basic.lean#L264)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
