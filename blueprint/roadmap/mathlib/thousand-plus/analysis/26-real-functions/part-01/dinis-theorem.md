---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Monotone.tendstoLocallyUniformly_of_forall_tendsto
mathlib_file: Mathlib/Topology/UniformSpace/Dini.lean
---

# Dini's theorem

**Dini's theorem**: if `F n` is a monotone increasing collection of continuous functions
converging pointwise to a continuous function `f`, then `F n` converges locally uniformly to `f`.

```lean
Monotone.tendstoLocallyUniformly_of_forall_tendsto.{u_1, u_2, u_3} {ι : Type u_1} {α : Type u_2}
  {G : Type u_3} [Preorder ι] [TopologicalSpace α] [NormedAddCommGroup G] [Lattice G]
  [HasSolidNorm G] [IsOrderedAddMonoid G] {F : ι → α → G} {f : α → G}
  (hF_cont : ∀ (i : ι), Continuous (F i)) (hF_mono : Monotone F) (hf : Continuous f)
  (h_tendsto : ∀ (x : α), Filter.Tendsto (fun x_1 => F x_1 x) Filter.atTop (nhds (f x))) :
  TendstoLocallyUniformly F f Filter.atTop
```

## Depends on

- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Sources

- [Mathlib documentation: `Monotone.tendstoLocallyUniformly_of_forall_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/Dini.html#Monotone.tendstoLocallyUniformly_of_forall_tendsto)
- [Source of `Monotone.tendstoLocallyUniformly_of_forall_tendsto` in Mathlib/Topology/UniformSpace/Dini.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/Dini.lean#L52)
- [1000+ theorems list: Q595466](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L608)
- [1000+ theorems project: Q595466](https://1000-plus.github.io/all.html?length=-1#Q595466)
- [Wikipedia: Dini's theorem](https://en.wikipedia.org/wiki/Dini's_theorem)
- [Wikidata: Q595466](https://www.wikidata.org/wiki/Q595466)
