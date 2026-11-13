---
declaration: section
origin: cited
lean: Topology.isConstructible_iff_exists_finset_biUnion_inter_compl, IsConstructibleStratified.iUnion, IsConstructibleStratified.iInter, IsConstructibleStratified.compl, Topology.IsConstructible.iUnion, Topology.IsConstructible.iInter, Topology.IsConstructible.compl, main_theorem053W
statement: formalized
proof: formalized
---

# 5.15 Constructible sets

Section 5.15 of the Stacks Project, [Tag 04ZC](https://stacks.math.columbia.edu/tag/04ZC). 10 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 005G, a definition

[Tag 005G](https://stacks.math.columbia.edu/tag/005G) in the Stacks Project.

**`Topology.isConstructible_iff_exists_finset_biUnion_inter_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/NormalForm.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/NormalForm.lean#L42). The attribute's comment: “(1)”. References: EGA 0 (9.1.3); EGA 0 (9.1.2); SGA 3 VIB (3.7).

> **Stacks 005G(1)**.
> A subset `s` of a topological space `X` is constructible if and only if it is a finite union of
> subsets of the form `U ∩ Vᶜ` with `U, V ⊆ X` open and retrocompact in `X`. The finite union is
> encoded by a `Finset` of pairs `(U, V)`.

```lean
theorem Topology.isConstructible_iff_exists_finset_biUnion_inter_compl {s : Set X} :
    Topology.IsConstructible s ↔
      ∃ t : Finset (Set X × Set X),
        (∀ p ∈ t, IsOpen p.1 ∧ IsRetrocompact p.1 ∧ IsOpen p.2 ∧ IsRetrocompact p.2) ∧
        s = ⋃ p ∈ t, p.1 ∩ p.2ᶜ
```

## Tag 005H, a lemma

[Tag 005H](https://stacks.math.columbia.edu/tag/005H) in the Stacks Project.

**`IsConstructibleStratified.iUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/BooleanNormalForm.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/BooleanNormalForm.lean#L39). The attribute's comment: “finite unions of constructible sets, in the normal form of 005G(1)”.

> **Stacks 005H** (finite unions).
> A finite union of subsets of `X` that are each a finite union of sets `U ∩ Vᶜ` with `U, V`
> open and retrocompact in `X` is again such a finite union.

```lean
theorem IsConstructibleStratified.iUnion [Finite ι] {f : ι → Set X}
    (hf : ∀ i, IsConstructibleStratified (f i)) :
    IsConstructibleStratified (⋃ i, f i)
```

**`IsConstructibleStratified.iInter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/BooleanNormalForm.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/BooleanNormalForm.lean#L50). The attribute's comment: “finite intersections of constructible sets, in the normal form of 005G(1)”.

> **Stacks 005H** (finite intersections).
> A finite intersection of subsets of `X` that are each a finite union of sets `U ∩ Vᶜ` with
> `U, V` open and retrocompact in `X` is again such a finite union.

```lean
theorem IsConstructibleStratified.iInter [Finite ι] {f : ι → Set X}
    (hf : ∀ i, IsConstructibleStratified (f i)) :
    IsConstructibleStratified (⋂ i, f i)
```

**`IsConstructibleStratified.compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/BooleanNormalForm.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/BooleanNormalForm.lean#L61). The attribute's comment: “complements of constructible sets, in the normal form of 005G(1)”.

> **Stacks 005H** (complements).
> The complement of a finite union of sets `U ∩ Vᶜ` with `U, V` open and retrocompact in `X` is
> again such a finite union.

```lean
theorem IsConstructibleStratified.compl {s : Set X} (hs : IsConstructibleStratified s) :
    IsConstructibleStratified sᶜ
```

Declarations registered for the tag:

- [`Topology.IsConstructible.iUnion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsConstructible.iUnion#doc) registered with `add_to_stacks` in [StacksCore/Topology/Constructible/Boolean.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Constructible/Boolean.lean#L23) (StacksCore): “a finite union of constructible sets is constructible”. References: EGA 0 (9.1.2), “finite unions”.
- [`Topology.IsConstructible.iInter`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsConstructible.iInter#doc) registered with `add_to_stacks` in [StacksCore/Topology/Constructible/Boolean.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Constructible/Boolean.lean#L26) (StacksCore): “a finite intersection of constructible sets is constructible”. References: EGA 0 (9.1.2), “partial”.
- [`Topology.IsConstructible.compl`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsConstructible.compl#doc) registered with `add_to_stacks` in [StacksCore/Topology/Constructible/Boolean.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Constructible/Boolean.lean#L28) (StacksCore): “the complement of a constructible set is constructible”. References: EGA 0 (9.1.2), “partial”.

## Tag 053W, a lemma

[Tag 053W](https://stacks.math.columbia.edu/tag/053W) in the Stacks Project.

**`main_theorem053W`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/FromRetrocompactCover.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/FromRetrocompactCover.lean#L81). References: EGA 0 (9.1.9); EGA 0 (9.1.8), “(i) for retrocompact U”.

> **Stacks 053W**.
> For a finite covering `V : Fin m → Set X` of `X` by retrocompact open subsets, a subset
> `E ⊆ X` is constructible in `X` if and only if `E ∩ V j` is constructible in `V j` for
> every `j`.

```lean
theorem main_theorem053W
    {X : Type*} [TopologicalSpace X]
    {m : ℕ} (V : Fin m → Set X)
    (hVopen : ∀ j, IsOpen (V j))
    (hVretro : ∀ j, IsRetrocompact (V j))
    (hVcover : ⋃ j, V j = Set.univ)
    (E : Set X) :
    IsConstructibleIn E ↔ ∀ j, IsConstructibleInSubspace E (V j)
```

## Tag 09YF, a lemma

[Tag 09YF](https://stacks.math.columbia.edu/tag/09YF) in the Stacks Project.

**`isConstructible_subtype_preimage_of_isRetrocompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/Restrict.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/Restrict.lean#L85). References: EGA 0 (9.1.8), “T retrocompact, qc basis”; EGA 0 (9.1.9), “partial”; EGA 0 (9.2.1), “partial”; SGA 3 VIB (4.2), “partial”.

> **Stacks 09YF**.
> If `T ⊆ X` is retrocompact, quasi-compact opens form a basis for the topology on `X`, and
> `E` is constructible in `X`, then `E ∩ T`, as a subset of the subspace `T`, is constructible
> in `T`.

```lean
theorem isConstructible_subtype_preimage_of_isRetrocompact
    {X : Type*} [TopologicalSpace X]
    (T : Set X) (E : Set X)
    (hT : IsRetrocompact T)
    (hbasis : TopologicalSpace.IsTopologicalBasis {U : Set X | IsOpen U ∧ IsCompact U})
    (hE : Topology.IsConstructible E) :
    Topology.IsConstructible (X := T) (Subtype.val ⁻¹' E)
```

## Tag 09YH, a lemma

[Tag 09YH](https://stacks.math.columbia.edu/tag/09YH) in the Stacks Project.

**`isRetrocompact_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/Retrocompact.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/Retrocompact.lean#L84). References: EGA 0 (9.1.4); EGA 0 (9.1.13), “globally constructible”; EGA 0 (9.1.5), “necessity direction”.

> **Stacks 09YH**.
> Every constructible subset of a topological space is retrocompact.

```lean
theorem isRetrocompact_of_isConstructible {E : Set X} (h : IsConstructibleViaCompactOpens E) :
    IsRetrocompact E
```

## Tag 09YI, a lemma

[Tag 09YI](https://stacks.math.columbia.edu/tag/09YI) in the Stacks Project.

**`isConstructible_preimage_subtypeVal_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/MeetConstructible.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/MeetConstructible.lean#L205). References: EGA 0 (9.1.8), “partial”; EGA 0 (9.2.1), “partial”; SGA 3 VIB (4.2), “partial”.

> **Stacks 09YI.** Let `X` be a topological space whose topology has a basis
> of quasi-compact opens. For two constructible subsets `E, E'` of `X`, the
> intersection `E ∩ E'` is constructible in `E` (i.e. its image as a subset of
> the subspace `E ⊆ X`).
>
> Equivalently in Lean: the preimage `(Subtype.val : E → X) ⁻¹' E'` is
> constructible in the subspace topology of `E`.

```lean
theorem isConstructible_preimage_subtypeVal_of_isConstructible
    [PrespectralSpace X] {E E' : Set X}
    (hE : IsConstructible E) (hE' : IsConstructible E') :
    IsConstructible ((Subtype.val : E → X) ⁻¹' E')
```

## Tag 09YJ, a lemma

[Tag 09YJ](https://stacks.math.columbia.edu/tag/09YJ) in the Stacks Project.

**`isConstructibleSet_of_isConstructibleSet_in_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/InConstructible.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/InConstructible.lean#L306). References: EGA 0 (9.1.8), “(ii), sufficiency”; EGA 0 (9.2.1), “partial”; SGA 3 VIB (3.7), “partial”.

> Let `X` be a topological space with a basis
> of quasi-compact opens. Let `E ⊆ X` be constructible in `X`, and let
> `F ⊆ E` be constructible in the topological subspace `E`. Then `F`, viewed
> as a subset of `X` via the inclusion `Subtype.val : E → X`, is
> constructible in `X`.

```lean
theorem isConstructibleSet_of_isConstructibleSet_in_constructible
    (hX : PrespectralSpace X)
    {E : Set X} (hE : IsConstructibleSet E)
    {F : Set ↥E} (hF : IsConstructibleSet F) :
    IsConstructibleSet (Subtype.val '' F : Set X)
```

## Tag 0F2K, a lemma

[Tag 0F2K](https://stacks.math.columbia.edu/tag/0F2K) in the Stacks Project.

**`main_theorem0F2K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/LocallyClosedQuasiCompact.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/LocallyClosedQuasiCompact.lean#L130). References: EGA 0 (9.1.5), “special case”; EGA IV (1.8.1), “partial”.

> **Stacks 0F2K**.
> In a quasi-compact space having a basis of quasi-compact opens closed under pairwise
> intersections, a locally closed subset `T ⊆ X` that is quasi-compact and whose complement
> `Tᶜ` is retrocompact in `X` is constructible in `X`.

```lean
theorem main_theorem0F2K
    [CompactSpace X]
    (B : Set (Set X))
    (hB : TopologicalSpace.IsTopologicalBasis B)
    (_hBcompact : ∀ U ∈ B, IsCompact U)
    (hBinter : ∀ U ∈ B, ∀ V ∈ B, IsCompact (U ∩ V))
    (T : Set X)
    (hTlc : IsLocallyClosed T)
    (hTqc : IsCompact T)
    (hTcRetro : IsRetrocompact Tᶜ) :
    IsConstructibleStratified T
```

## Tag 09YK, a lemma

[Tag 09YK](https://stacks.math.columbia.edu/tag/09YK) in the Stacks Project.

**`isConstructible_iff_isConstructible_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/LocalOnCover.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/LocalOnCover.lean#L221). References: EGA 0 (9.1.9), “special case”; EGA 0 (9.2.1), “more general”.

> **Stacks 09YK**.
> For `X` a topological space whose topology has a basis of quasi-compact opens and
> `E₁, …, Eₘ` a finite family of constructible subsets covering `X`, a subset `S ⊆ X` is
> constructible in `X` if and only if its preimage in each `Eⱼ` is constructible in `Eⱼ`.

```lean
theorem isConstructible_iff_isConstructible_preimage
    (h_basis : IsTopologicalBasis { U : Set X | IsOpen U ∧ IsCompact U })
    {m : ℕ} (E : Fin m → Set X)
    (hE_cons : ∀ j, IsConstructible (E j))
    (hcover : (⋃ j, E j) = Set.univ)
    (S : Set X) :
    IsConstructible S ↔
      ∀ j, IsConstructible ((Subtype.val : ↥(E j) → X) ⁻¹' S)
```

## Tag 005K, a lemma

[Tag 005K](https://stacks.math.columbia.edu/tag/005K) in the Stacks Project.

**`Topology.IsConstructible.exists_isOpen_inter_closure_singleton_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/ConstructibleImage.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/GenericFinitePresentation/ConstructibleImage.lean#L494). The attribute's comment: “constructible case, (3) ⇒ (1)”.

> Every point of a constructible set has an open neighbourhood whose intersection with
> the closure of the point lies in the set.

```lean
theorem Topology.IsConstructible.exists_isOpen_inter_closure_singleton_subset {X : Type*}
    [TopologicalSpace X] {s : Set X} (hs : IsConstructible s) {x : X} (hx : x ∈ s) :
    ∃ U, IsOpen U ∧ x ∈ U ∧ U ∩ closure {x} ⊆ s
```

**`open_dense_iff_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/IrreducibleMeet.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/IrreducibleMeet.lean#L143). References: EGA 0 (9.2.2); SGA 1 IV (6.1), “necessity”.

> **Stacks 005K**.
> For irreducible `Z` and `E` a finite union of locally closed subsets, the intersection
> `E ∩ Z` contains an open dense subset of `Z` if and only if it is dense in `Z`.

```lean
theorem open_dense_iff_dense
    {Z : Set X} (hZ : IsIrreducible Z)
    {E : Set X} (hE : IsFiniteUnionLocallyClosed E) :
    (∃ V : Set X, IsOpenDenseSubsetOf V Z ∧ V ⊆ E ∩ Z) ↔ Z ⊆ closure (E ∩ Z)
```

**`tfae_with_generic_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/IrreducibleMeet.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Constructible/IrreducibleMeet.lean#L162). References: EGA 0 (9.2.2), “Z has a generic point”; EGA 0 (2.1.4), “partial”; EGA 0 (9.2.5), “more general”; EGA I (7.1.4), “partial”; EGA IV (8.1.3), “partial”; SGA 1 IV (6.3), “special case”; SGA 1 IV (6.4), “(b)”.

> **Stacks 005K**.
> For irreducible `Z` with generic point `ξ` and `E` a finite union of locally closed subsets,
> the existence of an open dense subset of `Z` inside `E ∩ Z`, the density of `E ∩ Z` in `Z`,
> and the membership `ξ ∈ E` are equivalent.

```lean
theorem tfae_with_generic_point
    {Z : Set X} (hZ : IsIrreducible Z)
    {E : Set X} (hE : IsFiniteUnionLocallyClosed E)
    {ξ : X} (hξ : IsGenericPoint ξ Z) :
    [ (∃ V : Set X, IsOpenDenseSubsetOf V Z ∧ V ⊆ E ∩ Z),
      Z ⊆ closure (E ∩ Z),
      ξ ∈ E ].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.15, Tag 04ZC](https://stacks.math.columbia.edu/tag/04ZC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
