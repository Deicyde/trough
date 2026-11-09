# Heine-Cantor theorem

Heine-Cantor: a continuous function on a compact uniform space is uniformly
continuous.

```lean
CompactSpace.uniformContinuous_of_continuous.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [UniformSpace α] [UniformSpace β] [CompactSpace α] {f : α → β} (h : Continuous f) :
  UniformContinuous f
```

## Depends on

- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Uniform space](uniform-space.md)

## Sources

- [Mathlib documentation: `CompactSpace.uniformContinuous_of_continuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/HeineCantor.html#CompactSpace.uniformContinuous_of_continuous)
- [Source of `CompactSpace.uniformContinuous_of_continuous` in Mathlib/Topology/UniformSpace/HeineCantor.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/UniformSpace/HeineCantor.lean#L39)
- [Mathlib overview: Topology › Uniform notions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L245)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L419)
- [1000+ theorems list: Q765987](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L863)
- [1000+ theorems project: Q765987](https://1000-plus.github.io/all.html?length=-1#Q765987)
- [Wikipedia: Heine–Cantor theorem](https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem)
- [Wikidata: Q765987](https://www.wikidata.org/wiki/Q765987)
