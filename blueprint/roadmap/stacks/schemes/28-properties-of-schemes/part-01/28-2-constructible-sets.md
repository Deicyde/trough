---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyConstructible_iff_forall_affineOpens, AlgebraicGeometry.compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints, AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_mem_genericPoints, AlgebraicGeometry.Scheme.isCompact_inter_of_quasiSeparated, AlgebraicGeometry.Scheme.isRetrocompact_of_quasiSeparated, AlgebraicGeometry.spectralSpace_of_compactSpace_of_quasiSeparatedSpace, Topology.IsLocallyConstructible.isConstructible, AlgebraicGeometry.isRetrocompact_iff_forall_affineOpens
statement: formalized
proof: formalized
---

# 28.2 Constructible sets

Section 28.2 of the Stacks Project, [Tag 054B](https://stacks.math.columbia.edu/tag/054B). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 054C, a lemma

[Tag 054C](https://stacks.math.columbia.edu/tag/054C) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_iff_forall_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L69). References: SGA 3 VIB (3.7), “(iii), special case”.

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

**`AlgebraicGeometry.compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L91). The attribute's comment: “neighborhood\_disjoint”.

> A generic point of an irreducible component which is not in a
> locally constructible subset has an open neighbourhood disjoint from that subset.

```lean
public theorem compl_mem_nhds_of_isLocallyConstructible_of_mem_genericPoints
    {X : Scheme.{u}} {E : Set X} {ξ : X} (hE : IsLocallyConstructible E)
    (hξ : ξ ∈ genericPoints X) (hξE : ξ ∉ E) :
    Eᶜ ∈ 𝓝 ξ
```

**`AlgebraicGeometry.mem_nhds_of_isLocallyConstructible_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L123). The attribute's comment: “neighborhood\_contained”.

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

**`AlgebraicGeometry.Scheme.isCompact_inter_of_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/QuasiSeparatedRetrocompact.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/QuasiSeparatedRetrocompact.lean#L34). The attribute's comment: “first assertion; Stacks' quasi-separated scheme is a quasi-separated morphism to the terminal scheme”.

> Let `X` be a quasi-separated scheme, i.e. `X ⟶ Spec ℤ` (the morphism to the terminal
> scheme) is quasi-separated. The intersection of any two quasi-compact opens `U`, `V` of `X` is a
> quasi-compact open of `X`.

```lean
theorem isCompact_inter_of_quasiSeparated (X : Scheme) [QuasiSeparated (terminal.from X)]
    {U V : Set X} (hU : IsOpen U) (hU' : IsCompact U) (hV : IsOpen V) (hV' : IsCompact V) :
    IsOpen (U ∩ V) ∧ IsCompact (U ∩ V)
```

**`AlgebraicGeometry.Scheme.isRetrocompact_of_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/QuasiSeparatedRetrocompact.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/QuasiSeparatedRetrocompact.lean#L45). The attribute's comment: “second assertion; Stacks' quasi-separated scheme is a quasi-separated morphism to the terminal scheme”.

> Let `X` be a quasi-separated scheme, i.e. `X ⟶ Spec ℤ` (the morphism to the terminal
> scheme) is quasi-separated. Every quasi-compact open `U` of `X` is retrocompact in `X`: its
> intersection with every quasi-compact open of `X` is quasi-compact.

```lean
theorem isRetrocompact_of_quasiSeparated (X : Scheme) [QuasiSeparated (terminal.from X)]
    {U : Set X} (hU : IsOpen U) (hU' : IsCompact U) : IsRetrocompact U
```

## Tag 094L, a lemma

[Tag 094L](https://stacks.math.columbia.edu/tag/094L) in the Stacks Project.

**`AlgebraicGeometry.spectralSpace_of_compactSpace_of_quasiSeparatedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Constructible.lean#L137). References: SGA 4 IV (4.2.1), “special case”.

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

- [`Topology.IsLocallyConstructible.isConstructible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsLocallyConstructible.isConstructible#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch28.lean#L72) (StacksFrontier): “stated for any topological space; on a qcqs scheme its hypotheses are instances”. References: EGA 0 (9.1.12); EGA IV (1.8.1), “partial”; SGA 3 VIB (3.7), “partial, special case”.

## Tag 07ZL, a lemma

[Tag 07ZL](https://stacks.math.columbia.edu/tag/07ZL) in the Stacks Project.

**`AlgebraicGeometry.isRetrocompact_iff_forall_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean#L83). References: EGA IV (1.8.1), “retrocompact criterion”.

> **A subset of a scheme is retrocompact exactly when its intersection with every affine open
> is quasi-compact.**

```lean
theorem isRetrocompact_iff_forall_affineOpens (E : Set X) :
    IsRetrocompact E ↔ ∀ W : X.affineOpens, IsCompact (E ∩ (W : Set X))
```

## Tag 0F2M, a lemma

[Tag 0F2M](https://stacks.math.columbia.edu/tag/0F2M) in the Stacks Project.

**`AlgebraicGeometry.locallyFinite_iff_parts_isLocallyConstructible`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ConstructiblePartition.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ConstructiblePartition.lean#L154).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
