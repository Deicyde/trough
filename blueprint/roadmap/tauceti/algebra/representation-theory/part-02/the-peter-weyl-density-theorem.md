---
declaration: theorem
origin: cited
lean: TauCeti.dense_representativeSubmodule
statement: formalized
proof: formalized
---

# The Peter-Weyl density theorem

The representative ring `𝓡(G)` of a compact group is
uniformly dense in `C(G, 𝕜)`. Hausdorffness is not needed: the mollifiers the proof runs on are
built without it.

```lean
TauCeti.dense_representativeSubmodule.{u_1, u_2} (𝕜 : Type u_1) (G : Type u_2) [RCLike 𝕜] [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] :
  Dense ↑(TauCeti.representativeSubmodule 𝕜 G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The spectral theorem for a symmetric convolution operator](the-spectral-theorem-for-a-symmetric-convolution.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_representativeSubmodule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/RepresentativeDensity.html#TauCeti.dense_representativeSubmodule).

## Sources

- [Tau Ceti documentation: `TauCeti.dense_representativeSubmodule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/RepresentativeDensity.html#TauCeti.dense_representativeSubmodule)
- [Source of `TauCeti.dense_representativeSubmodule` in TauCeti/RepresentationTheory/Compact/RepresentativeDensity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Compact/RepresentativeDensity.lean#L111)
