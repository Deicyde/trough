---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyConstructible_iff_forall_affineOpens, AlgebraicGeometry.compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints, AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_mem_genericPoints, QuasiSeparatedSpace.inter_isCompact, IsCompact.isRetrocompact, AlgebraicGeometry.spectralSpace_of_compactSpace_of_quasiSeparatedSpace, Topology.IsLocallyConstructible.isConstructible, AlgebraicGeometry.isRetrocompact_iff_forall_affineOpens
statement: formalized
proof: formalized
---

# 28.2 Constructible sets

Section 28.2 of the Stacks Project, [Tag 054B](https://stacks.math.columbia.edu/tag/054B). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 054C, a lemma

[Tag 054C](https://stacks.math.columbia.edu/tag/054C) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_iff_forall_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L69). References: SGA 3 VIB (3.7), “(iii), special case”.

> A subset of a scheme is locally constructible if and only if
> its restriction to every affine open subscheme is constructible.

```lean
public theorem isLocallyConstructible_iff_forall_affineOpens
    {X : Scheme.{u}} (E : Set X) :
    Topology.IsLocallyConstructible E ↔
      ∀ U : X.affineOpens, Topology.IsConstructible ((U.1 : Set X) ↓∩ E)
```

## Tag 0AAW, a lemma

[Tag 0AAW](https://stacks.math.columbia.edu/tag/0AAW) in the Stacks Project.

**`AlgebraicGeometry.compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L91). The attribute's comment: “neighborhood_disjoint”.

> A generic point of an irreducible component which is not in a
> locally constructible subset has an open neighbourhood disjoint from that subset.

```lean
public theorem compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints
    {X : Scheme.{u}} {E : Set X} {ξ : X} (hE : IsLocallyConstructible E)
    (hξ : ξ ∈ genericPoints X) (hξE : ξ ∉ E) :
    Eᶜ ∈ 𝓝 ξ
```

**`AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L123). The attribute's comment: “neighborhood_contained”.

> A locally constructible set containing the generic point of an irreducible component
> contains an open neighbourhood of that point.

```lean
public theorem mem_nhds_of_isLocallyConstructible_of_mem_genericPoints
    {X : Scheme.{u}} {E : Set X} {ξ : X} (hE : IsLocallyConstructible E)
    (hξ : ξ ∈ genericPoints X) (hξE : ξ ∈ E) :
    E ∈ 𝓝 ξ
```

## Tag 054D, a lemma

[Tag 054D](https://stacks.math.columbia.edu/tag/054D) in the Stacks Project.

Declarations registered for the tag:

- [`QuasiSeparatedSpace.inter_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiSeparatedSpace.inter_isCompact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L69) (StacksFrontier): “(1) the intersection of two quasi-compact opens is quasi-compact; Stacks' quasi-separated scheme is `QuasiSeparatedSpace X` by `AlgebraicGeometry.quasiSeparatedSpace_iff_quasiSeparated`”.
- [`IsCompact.isRetrocompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCompact.isRetrocompact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L73) (StacksFrontier): “(2) every quasi-compact open is retrocompact”. References: EGA 0 (9.1.6), “partial”; SGA 3 VIA (2.6.3), “more general”; SGA 3 VIB (3.7), “partial”.

## Tag 094L, a lemma

[Tag 094L](https://stacks.math.columbia.edu/tag/094L) in the Stacks Project.

**`AlgebraicGeometry.spectralSpace_of_compactSpace_of_quasiSeparatedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L137). References: SGA 4 IV (4.2.1), “special case”.

> The underlying topological space of a quasi-compact and
> quasi-separated scheme is a spectral space: it is sober and quasi-compact, the quasi-compact
> opens form a basis, and any two of them meet in a quasi-compact open.

```lean
public instance spectralSpace_of_compactSpace_of_quasiSeparatedSpace (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] : SpectralSpace X
```

## Tag 054E, a lemma

[Tag 054E](https://stacks.math.columbia.edu/tag/054E) in the Stacks Project.

Declarations registered for the tag:

- [`Topology.IsLocallyConstructible.isConstructible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsLocallyConstructible.isConstructible#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L76) (StacksFrontier): “stated for any topological space; on a qcqs scheme its hypotheses are instances”. References: EGA 0 (9.1.12); EGA IV (1.8.1), “partial”; SGA 3 VIB (3.7), “partial, special case”.

## Tag 07ZL, a lemma

[Tag 07ZL](https://stacks.math.columbia.edu/tag/07ZL) in the Stacks Project.

**`AlgebraicGeometry.isRetrocompact_iff_forall_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean#L83). References: EGA IV (1.8.1), “retrocompact criterion”.

> **A subset of a scheme is retrocompact exactly when its intersection with every affine open
> is quasi-compact.**

```lean
theorem isRetrocompact_iff_forall_affineOpens (E : Set X) :
    IsRetrocompact E ↔ ∀ W : X.affineOpens, IsCompact (E ∩ (W : Set X))
```

## Tag 0F2M, a lemma

[Tag 0F2M](https://stacks.math.columbia.edu/tag/0F2M) in the Stacks Project.

**`AlgebraicGeometry.locallyFinite_iff_parts_isLocallyConstructible`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ConstructiblePartition.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ConstructiblePartition.lean#L154).

> A partition of a scheme into retrocompact parts is locally finite if and only if all its
> parts are locally constructible.

```lean
public lemma locallyFinite_iff_parts_isLocallyConstructible
    {X : Scheme.{u}} {P : Set (Set X)} (hP : IsTopologicalPartition P)
    (hP_retrocompact : ∀ S ∈ P, IsRetrocompact S) :
    LocallyFinite (fun S : P ↦ (S : Set X)) ↔
      ∀ S ∈ P, Topology.IsLocallyConstructible S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.2, Tag 054B](https://stacks.math.columbia.edu/tag/054B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
