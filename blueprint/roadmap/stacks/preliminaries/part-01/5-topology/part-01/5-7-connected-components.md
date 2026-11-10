---
declaration: section
origin: cited
lean: ConnectedSpace, connectedComponent, isConnected_connectedComponent, IsConnected.image, IsConnected.closure, isClosed_connectedComponent, IsConnected.subset_connectedComponent, connectedComponent_eq
statement: formalized
proof: formalized
---

# 5.7 Connected components

Section 5.7 of the Stacks Project, [Tag 004R](https://stacks.math.columbia.edu/tag/004R). 11 tags here are carried by 5 declarations of the repository (2 in StacksCore and 3 in StacksFrontier) and 20 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 004S, a definition

[Tag 004S](https://stacks.math.columbia.edu/tag/004S) in the Stacks Project.

Declarations registered for the tag:

- [`ConnectedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ConnectedSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Basic.lean#L10) (StacksCore): “1”. References: EGA I (2.1.8); SGA 4 XV (1.3).
- [`connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Basic.lean#L11) (StacksCore): “2”. References: SGA 3 VIA (2.1), “partial”; SGA 3 VIA (2.3); SGA 3 VIB (3.1), “more general”.
- [`isConnected_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isConnected_connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Basic.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Basic.lean#L12) (StacksCore): “2”.

## Tag 0376, a lemma

[Tag 0376](https://stacks.math.columbia.edu/tag/0376) in the Stacks Project.

Declarations registered for the tag:

- [`IsConnected.image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsConnected.image#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Image.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Image.lean#L19) (StacksCore): “the image of a connected set under a continuous map is connected”.

## Tag 004T, a lemma

[Tag 004T](https://stacks.math.columbia.edu/tag/004T) in the Stacks Project.

Declarations registered for the tag:

- [`IsConnected.closure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsConnected.closure#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L33) (StacksCore): “(1)”.
- [`isClosed_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isClosed_connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L34) (StacksCore): “(2)”. References: SGA 3 VIA (2.1), “more general”; SGA 3 X (5.11.0), “more general”.
- [`IsConnected.subset_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsConnected.subset_connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L35) (StacksCore): “(3)”.
- [`connectedComponent_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=connectedComponent_eq#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L36) (StacksCore): “(3), (4): uniqueness”.
- [`mem_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=mem_connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L37) (StacksCore): “(4)”.
- [`connectedComponent_disjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=connectedComponent_disjoint#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/Components.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/Components.lean#L38) (StacksCore): “(4): disjointness”.

## Tag 0FIY, a remark

[Tag 0FIY](https://stacks.math.columbia.edu/tag/0FIY) in the Stacks Project.

**`exists_connectedComponent_ne_quasiComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/QuasiComponent.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/QuasiComponent.lean#L346).

> **Stacks 0FIY** (Engelking, Example 6.1.24). In general the connected component `Z` of a
> point and its quasi-component `E` — the intersection of all clopen sets containing it — are
> different, even though `Z ⊆ E` always holds (`connectedComponent_subset_quasiComponent`).
>
> The witness is `Engelking`, the space `{x, y, z 0, z 1, …}` with basis of opens `{z n}`,
> `{x} ∪ {z n, z (n+1), …}` and `{y} ∪ {z n, z (n+1), …}`, at the point `x`: there
> `Z = {x}` while `E = {x, y}`.

```lean
theorem exists_connectedComponent_ne_quasiComponent :
    ∃ (X : Type) (_ : TopologicalSpace X) (x : X),
      connectedComponent x ≠ quasiComponent x
```

## Tag 0377, a lemma

[Tag 0377](https://stacks.math.columbia.edu/tag/0377) in the Stacks Project.

**`connectedComponentsMap_bijective_of_isClosed_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Connected/ConnectedFibres.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/ConnectedFibres.lean#L29).

> **Stacks 0377.** Let `f : X → Y` be a map of topological spaces such that all fibres of `f` are
> connected and a subset `T ⊆ Y` is closed if and only if `f ⁻¹' T` is closed. Then `f` induces a
> bijection between the sets of connected components of `X` and `Y`.

```lean
theorem connectedComponentsMap_bijective_of_isClosed_iff
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] {f : X → Y}
    (hfib : ∀ y, IsConnected (f ⁻¹' {y}))
    (hcl : ∀ T : Set Y, IsClosed (f ⁻¹' T) ↔ IsClosed T) :
    Function.Bijective
      ((Topology.isCoinducing_iff_isClosed.mpr hcl).continuous.connectedComponentsMap)
```

## Tag 0378, a lemma

[Tag 0378](https://stacks.math.columbia.edu/tag/0378) in the Stacks Project.

**`bijective_connectedComponentsMap_of_isOpenMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Connected/OpenConnectedFibres.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/OpenConnectedFibres.lean#L30).

> **Stacks 0378.** A continuous open map with connected fibres induces a bijection between the
> sets of connected components.

```lean
theorem bijective_connectedComponentsMap_of_isOpenMap
    (f : X → Y) (hf_cont : Continuous f) (hf_open : IsOpenMap f)
    (hf_fib : ∀ y : Y, IsConnected (f ⁻¹' {y})) :
    Function.Bijective (hf_cont.connectedComponentsMap)
```

## Tag 07VB, a lemma

[Tag 07VB](https://stacks.math.columbia.edu/tag/07VB) in the Stacks Project.

**`finite_fibre_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/FiniteFibres.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/FiniteFibres.lean#L40).

> **Stacks 07VB.** If `f : X → Y` is a continuous open and closed map between nonempty
> topological spaces, `Y` is connected, and some fibre `f ⁻¹' {y}` is finite, then `X` has finitely
> many connected components and their number is at most the cardinality of the fibre.

```lean
theorem finite_fibre_connectedComponents
    {X Y : Type u} [TopologicalSpace X] [TopologicalSpace Y]
    [Nonempty X] [Nonempty Y]
    (f : X → Y)
    (hY_conn : ConnectedSpace Y)
    (hf_open : IsOpenMap f) (hf_closed : IsClosedMap f)
    (y : Y) (hy_fin : (f ⁻¹' {y}).Finite) :
    Finite (ConnectedComponents X) ∧
      Nat.card (ConnectedComponents X) ≤ (f ⁻¹' {y}).ncard
```

**`connectedComponent_clopen_and_image_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/FiniteFibres.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/FiniteFibres.lean#L90). The attribute's comment: “corollary”. References: SGA 3 X (9.7.3), “more general”.

> **Stacks 07VB**, corollary. Under the hypotheses of `finite_fibre_connectedComponents`, every
> connected component `T` of `X` is open and closed in `X`, its image `f '' T` is a nonempty open and
> closed subset of `Y`, and hence equals all of `Y`.

```lean
theorem connectedComponent_clopen_and_image_eq_univ
    {X Y : Type u} [TopologicalSpace X] [TopologicalSpace Y]
    [Nonempty X] [Nonempty Y]
    (f : X → Y)
    (hY_conn : ConnectedSpace Y)
    (hf_open : IsOpenMap f) (hf_closed : IsClosedMap f)
    (y : Y) (hy_fin : (f ⁻¹' {y}).Finite)
    (T : Set X) (hT : ∃ x : X, T = connectedComponent x) :
    IsOpen T ∧ IsClosed T ∧ (f '' T).Nonempty ∧ IsOpen (f '' T) ∧
      IsClosed (f '' T) ∧ f '' T = Set.univ
```

## Tag 04MC, a definition

[Tag 04MC](https://stacks.math.columbia.edu/tag/04MC) in the Stacks Project.

Declarations registered for the tag:

- [`TotallyDisconnectedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TotallyDisconnectedSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/TotallyDisconnected.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/TotallyDisconnected.lean#L10) (StacksCore).
- [`totallyDisconnectedSpace_iff_connectedComponent_singleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=totallyDisconnectedSpace_iff_connectedComponent_singleton#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/TotallyDisconnected.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/TotallyDisconnected.lean#L11) (StacksCore).

## Tag 08ZL, a lemma

[Tag 08ZL](https://stacks.math.columbia.edu/tag/08ZL) in the Stacks Project.

Declarations registered for the tag:

- [`ConnectedComponents.totallyDisconnectedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ConnectedComponents.totallyDisconnectedSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/ComponentSpace.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/ComponentSpace.lean#L22) (StacksCore): “π₀(X) is totally disconnected”.
- [`Continuous.connectedComponentsLift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.connectedComponentsLift#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/ComponentSpace.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/ComponentSpace.lean#L23) (StacksCore): “factorization: the induced map on π₀(X)”.
- [`Continuous.connectedComponentsLift_continuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.connectedComponentsLift_continuous#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/ComponentSpace.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/ComponentSpace.lean#L24) (StacksCore): “factorization: the induced map is continuous”.
- [`Continuous.connectedComponentsLift_comp_coe`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.connectedComponentsLift_comp_coe#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/ComponentSpace.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/ComponentSpace.lean#L26) (StacksCore): “factorization: the induced map lifts the original one”.

## Tag 04MD, a definition

[Tag 04MD](https://stacks.math.columbia.edu/tag/04MD) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyConnectedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyConnectedSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/LocallyConnected.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/LocallyConnected.lean#L26) (StacksCore). References: SGA 3 VIA (2.3); SGA 4 IV (7.6).

## Tag 04ME, a lemma

[Tag 04ME](https://stacks.math.columbia.edu/tag/04ME) in the Stacks Project.

Declarations registered for the tag:

- [`IsOpen.locallyConnectedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsOpen.locallyConnectedSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/LocallyConnected.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/LocallyConnected.lean#L28) (StacksCore): “(1) an open subset of a locally connected space is locally connected”.
- [`isOpen_connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isOpen_connectedComponent#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/LocallyConnected.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/LocallyConnected.lean#L30) (StacksCore): “(2) the connected components are open”. References: SGA 3 VIA (2.3), “partial”.
- [`LocallyConnectedSpace.open_connected_basis`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyConnectedSpace.open_connected_basis#doc) registered with `add_to_stacks` in [StacksCore/Topology/Connected/LocallyConnected.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Connected/LocallyConnected.lean#L31) (StacksCore): “in particular, a fundamental system of open connected neighbourhoods”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.7, Tag 004R](https://stacks.math.columbia.edu/tag/004R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
