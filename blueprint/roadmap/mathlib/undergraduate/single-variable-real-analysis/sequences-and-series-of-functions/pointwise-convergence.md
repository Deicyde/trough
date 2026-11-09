# Pointwise convergence

Mathlib states this as `tendsto_pi_nhds`.

```lean
tendsto_pi_nhds.{v, u_2, u_3} {Y : Type v} {ι : Type u_2} {A : ι → Type u_3}
  [T : (i : ι) → TopologicalSpace (A i)] {f : Y → (i : ι) → A i} {g : (i : ι) → A i}
  {u : Filter Y} :
  Filter.Tendsto f u (nhds g) ↔ ∀ (x : ι), Filter.Tendsto (fun i => f i x) u (nhds (g x))
```

## Depends on

- [Limit of a map with respect to filters](../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Topological space](../../../overview/topology/general-topology/part-01/topological-space.md)

## Proof depends on

- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)

## Sources

- [Mathlib documentation: `tendsto_pi_nhds`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Constructions.html#tendsto_pi_nhds)
- [Source of `tendsto_pi_nhds` in Mathlib/Topology/Constructions.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Constructions.lean#L818)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L349)
