---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one
statement: formalized
proof: formalized
---

# A proper Morse function without critical points of index one forces simple connectivity

A connected manifold carrying a proper Morse function, bounded below, with no critical point of
Morse index one is simply connected.

```lean
TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} [ConnectedSpace M]
  (hf : TauCeti.IsMorse I f) (hp : IsProperMap f) (hbdd : BddBelow (Set.range f))
  (hd : ∀ p ∈ TauCeti.criticalPoints I f, TauCeti.manifoldMorseIndex I f p ≠ 1) :
  SimplyConnectedSpace M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Milnor's cell attachment theorem, in pushout form](milnors-cell-attachment-theorem-in-pushout-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/FundamentalGroup.html#TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/FundamentalGroup.html#TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one)
- [Source of `TauCeti.IsMorse.simplyConnectedSpace_of_manifoldMorseIndex_ne_one` in TauCeti/Geometry/Manifold/Morse/FundamentalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/FundamentalGroup.lean#L144)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
