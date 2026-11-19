---
declaration: theorem
origin: cited
lean: MeasurableSet.image_of_continuousOn_injOn_chartAt, MeasurableSet.image_of_continuousOn_injOn_chartedSpace
statement: formalized
proof: formalized
---

# Lusin–Souslin theorem in charts

Let `M` be a charted space modelled on a Polish space, with
its Borel measurable space, and let `N` be a charted space modelled on a Hausdorff space, in which
open sets are measurable. A map `M → N` which is continuous and injective on a measurable subset
`s` of the chart source at `α`, and maps `s` into the chart source at `β`, sends `s` to a measurable
set.

```lean
MeasurableSet.image_of_continuousOn_injOn_chartAt.{u_1, u_2, u_3, u_4} {H : Type u_1}
  [TopologicalSpace H] [PolishSpace H] {M : Type u_2} [TopologicalSpace M] [ChartedSpace H M]
  [MeasurableSpace M] [BorelSpace M] {H' : Type u_3} [TopologicalSpace H'] [T2Space H']
  {N : Type u_4} [TopologicalSpace N] [ChartedSpace H' N] [MeasurableSpace N]
  [OpensMeasurableSpace N] {Φ : M → N} {α : M} {β : N} {s : Set M} (hs : MeasurableSet s)
  (hcont : ContinuousOn Φ s) (hinj : Set.InjOn Φ s) (hsα : s ⊆ (chartAt H α).source)
  (hsβ : Set.MapsTo Φ s (chartAt H' β).source) : MeasurableSet (Φ '' s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasurableSet.image_of_continuousOn_injOn_chartAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Polish.html#MeasurableSet.image_of_continuousOn_injOn_chartAt).

## Other forms

**Lusin–Souslin theorem on charted spaces.** Formalized in Tau Ceti as [`MeasurableSet.image_of_continuousOn_injOn_chartedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Polish.html#MeasurableSet.image_of_continuousOn_injOn_chartedSpace).

```lean
MeasurableSet.image_of_continuousOn_injOn_chartedSpace.{u_1, u_2, u_3, u_4} (H : Type u_1)
  [TopologicalSpace H] [PolishSpace H] {M : Type u_2} [TopologicalSpace M] [ChartedSpace H M]
  [MeasurableSpace M] [BorelSpace M] (H' : Type u_3) [TopologicalSpace H'] [T2Space H']
  {N : Type u_4} [TopologicalSpace N] [ChartedSpace H' N] [MeasurableSpace N]
  [OpensMeasurableSpace N] [LindelofSpace M] {Φ : M → N} {s : Set M} (hs : MeasurableSet s)
  (hcont : ContinuousOn Φ s) (hinj : Set.InjOn Φ s) : MeasurableSet (Φ '' s)
```

## Sources

- [Tau Ceti documentation: `MeasurableSet.image_of_continuousOn_injOn_chartAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Polish.html#MeasurableSet.image_of_continuousOn_injOn_chartAt)
- [Source of `MeasurableSet.image_of_continuousOn_injOn_chartAt` in TauCeti/Geometry/Manifold/Polish.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Polish.lean#L40)
