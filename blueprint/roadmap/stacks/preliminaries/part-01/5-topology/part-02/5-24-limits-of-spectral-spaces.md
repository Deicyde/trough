---
declaration: section
origin: cited
lean: SpectralLimits.isCompact_limitSubset, SpectralLimits.compactSpace_limit, SpectralLimits.nonempty_limitSet_inter_of_isClosed_constructible, SpectralLimits.nonempty_limitSet, SpectralLimits.preimage_limit_π_subset_iff_exists_map_preimage_subset, descend_isConstructible, descend_isConstructible_isOpen, descend_isConstructible_isClosed
statement: formalized
proof: formalized
---

# 5.24 Limits of spectral spaces

Section 5.24 of the Stacks Project, [Tag 0A2U](https://stacks.math.columbia.edu/tag/0A2U). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A2V, a lemma

[Tag 0A2V](https://stacks.math.columbia.edu/tag/0A2V) in the Stacks Project.

**`SpectralLimits.isCompact_limitSubset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitQuasiCompact.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitQuasiCompact.lean#L133). The attribute's comment: “part (1)”.

> **Stacks 0A2V (1).** For a diagram of spectral spaces along spectral maps and subsets
> `Z j ⊆ F.obj j` closed in the constructible topology, the subset
> `{x ∈ lim F | ∀ j, π j x ∈ Z j}` of the limit is quasi-compact for the limit topology.

```lean
theorem isCompact_limitSubset
    (hF : ∀ {j i : J} (a : j ⟶ i), IsSpectralMap (F.map a).hom) (Z : ∀ j, Set (F.obj j))
    (hZ_closed : ∀ j, @IsClosed _ (constructibleTopology (F.obj j)) (Z j)) :
    IsCompact (limitSubset F Z)
```

**`SpectralLimits.compactSpace_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitQuasiCompact.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitQuasiCompact.lean#L173). The attribute's comment: “part (2)”.

> **Stacks 0A2V (2).** The limit of a diagram of spectral spaces along spectral maps is
> quasi-compact. This is part (1) with `Z j = univ`.

```lean
theorem compactSpace_limit (hF : ∀ {j i : J} (a : j ⟶ i), IsSpectralMap (F.map a).hom) :
    CompactSpace ((limit F : TopCat.{max v u}))
```

## Tag 0A2W, a lemma

[Tag 0A2W](https://stacks.math.columbia.edu/tag/0A2W) in the Stacks Project.

**`SpectralLimits.nonempty_limitSet_inter_of_isClosed_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitNonempty.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitNonempty.lean#L135). The attribute's comment: “part (1)”.

> A compatible cofiltered system of nonempty constructibly closed subsets of a spectral diagram
> has nonempty limit.

```lean
theorem nonempty_limitSet_inter_of_isClosed_constructible [IsCofiltered I]
    (Z : ∀ i, Set (F.obj i)) (hZ_ne : ∀ i, (Z i).Nonempty)
    (hZ_cl : ∀ i, @IsClosed (F.obj i) (constructibleTopology (F.obj i)) (Z i))
    (hZ_comp : ∀ ⦃j i : I⦄ (a : j ⟶ i), F.map a '' Z j ⊆ Z i) :
    { x : ∀ i, F.obj i | x ∈ limitSet F ∧ ∀ i, x i ∈ Z i }.Nonempty
```

**`SpectralLimits.nonempty_limitSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitNonempty.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitNonempty.lean#L168). The attribute's comment: “part (2)”.

> The cofiltered limit of a diagram of nonempty spectral spaces is nonempty.

```lean
theorem nonempty_limitSet [IsCofiltered I] (hX_ne : ∀ i, Nonempty (F.obj i)) :
    (limitSet F).Nonempty
```

## Tag 0A2X, a lemma

[Tag 0A2X](https://stacks.math.columbia.edu/tag/0A2X) in the Stacks Project.

**`SpectralLimits.preimage_limit_π_subset_iff_exists_map_preimage_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitConstructible.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitConstructible.lean#L250).

> Let `J` be a small cofiltered category and let `F : J ⥤ TopCat` be a diagram of spectral
> spaces such that, for every morphism `a : j ⟶ i` in `J`, the underlying map
> `F.map a : F.obj j → F.obj i` is a spectral map. Let `X := limit F` with projections
> `π_i := limit.π F i : X → F.obj i`. For every object `i : J` and any subsets `E, G ⊂ F.obj i`
> where `E` is closed in the constructible topology and `G` is open in the constructible topology,
> we have
> `π_i ⁻¹' E ⊆ π_i ⁻¹' G ↔ ∃ (j : J) (a : j ⟶ i), (F.map a) ⁻¹' E ⊆ (F.map a) ⁻¹' G`.

```lean
theorem preimage_limit_π_subset_iff_exists_map_preimage_subset
    {J : Type u} [SmallCategory J] [IsCofiltered J]
    (F : J ⥤ TopCat.{u})
    (hF_spec : ∀ j, SpectralSpace (F.obj j))
    (hF_map : ∀ {i j : J} (a : j ⟶ i), IsSpectralMap (F.map a))
    (i : J) (E G : Set (F.obj i))
    (hE : @IsClosed _ (constructibleTopology (F.obj i)) E)
    (hG : @IsOpen _ (constructibleTopology (F.obj i)) G) :
    ((limit.π F i) ⁻¹' E ⊆ (limit.π F i) ⁻¹' G) ↔
      (∃ (j : J) (a : j ⟶ i), (F.map a) ⁻¹' E ⊆ (F.map a) ⁻¹' G)
```

## Tag 0A2Y, a lemma

[Tag 0A2Y](https://stacks.math.columbia.edu/tag/0A2Y) in the Stacks Project.

**`descend_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/DescentConstructible.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/DescentConstructible.lean#L108). References: EGA IV (8.3.11), “partial”.

> For a cofiltered diagram `D` of spectral spaces with spectral transition maps, every
> constructible subset `E` of the inverse limit `D.invLimit` is the preimage under some projection
> `D.projFun i` of a constructible subset of `D.F.obj i`.

```lean
theorem descend_isConstructible
    {E : Set D.invLimit} (hE : IsConstructible E) :
    ∃ (i : J) (E_i : Set (D.F.obj i)), IsConstructible E_i ∧ D.projFun i ⁻¹' E_i = E
```

**`descend_isConstructible_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/DescentConstructible.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/DescentConstructible.lean#L168). The attribute's comment: “open refinement”. References: EGA IV (8.3.12), “open case”; EGA IV (8.3.11), “partial”.

> If the constructible subset of the inverse limit is moreover open, the constructible subset it
> descends from on the factor can be chosen open.

```lean
theorem descend_isConstructible_isOpen
    {E : Set D.invLimit} (hE : IsConstructible E) (hEopen : IsOpen E) :
    ∃ (i : J) (E_i : Set (D.F.obj i)),
      IsConstructible E_i ∧ IsOpen E_i ∧ D.projFun i ⁻¹' E_i = E
```

**`descend_isConstructible_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/DescentConstructible.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/DescentConstructible.lean#L179). The attribute's comment: “closed refinement”. References: EGA IV (8.3.12), “resp. closed case”; EGA IV (8.3.11), “partial”.

> If the constructible subset of the inverse limit is moreover closed, the constructible subset
> it descends from on the factor can be chosen closed.

```lean
theorem descend_isConstructible_isClosed
    {E : Set D.invLimit} (hE : IsConstructible E) (hEcl : IsClosed E) :
    ∃ (i : J) (E_i : Set (D.F.obj i)),
      IsConstructible E_i ∧ IsClosed E_i ∧ D.projFun i ⁻¹' E_i = E
```

## Tag 0A2Z, a lemma

[Tag 0A2Z](https://stacks.math.columbia.edu/tag/0A2Z) in the Stacks Project.

**`spectralDiagram_invLimit_spectralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/InverseLimits.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/InverseLimits.lean#L542). The attribute's comment: “inverse limit is spectral”.

> **Stacks 0A2Z** (inverse limit is spectral).
> The inverse limit of a cofiltered diagram of spectral spaces with spectral transition maps is
> a spectral topological space.

```lean
theorem spectralDiagram_invLimit_spectralSpace
    {J : Type v} [Category.{v'} J] [IsCofiltered J] (D : SpectralDiagram.{v, u} J) :
    SpectralSpace D.invLimit
```

**`spectralDiagram_proj_isSpectralMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/InverseLimits.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/InverseLimits.lean#L551). The attribute's comment: “projections are spectral”.

> **Stacks 0A2Z** (projections are spectral).
> Each projection from the inverse limit of a cofiltered diagram of spectral spaces to a
> component of the diagram is a spectral map.

```lean
theorem spectralDiagram_proj_isSpectralMap
    {J : Type v} [Category.{v'} J] [IsCofiltered J] (D : SpectralDiagram.{v, u} J) (j : J) :
    IsSpectralMap (D.projFun j)
```

## Tag 0A30, a lemma

[Tag 0A30](https://stacks.math.columbia.edu/tag/0A30) in the Stacks Project.

**`SpectralLimits.descent_of_quasiCompact_opens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitOpenDescent.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitOpenDescent.lean#L179). The attribute's comment: “part (1): descent of quasi-compact opens”.

> For every quasi-compact open `U` of the limit `lim F`, there exist an index `i` and a
> quasi-compact open `Ui` of `F.obj i` whose preimage under the projection equals `U`.

```lean
theorem descent_of_quasiCompact_opens
    [∀ i, SpectralSpace (F.obj i)]
    (hF : ∀ ⦃i j : J⦄ (a : i ⟶ j), IsSpectralMap (F.map a))
    (U : Set ((limit F : TopCat))) (hUopen : IsOpen U) (hUcpt : IsCompact U) :
    ∃ (i : J) (Ui : Set (F.obj i)), IsOpen Ui ∧ IsCompact Ui ∧
      (limit.π F i) ⁻¹' Ui = U
```

**`SpectralLimits.descent_of_inclusions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitOpenDescent.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitOpenDescent.lean#L325). The attribute's comment: “part (2): descent of inclusions”.

> If two quasi-compact opens `Ui ⊆ F.obj i` and `Uj ⊆ F.obj j` have nested preimages in the
> limit, the inclusion already holds after pulling back along a span `a : k ⟶ i`, `b : k ⟶ j`.

```lean
theorem descent_of_inclusions
    [∀ i, SpectralSpace (F.obj i)]
    (hF : ∀ ⦃i j : J⦄ (a : i ⟶ j), IsSpectralMap (F.map a))
    (i j : J) (Ui : Set (F.obj i)) (Uj : Set (F.obj j))
    (hUi_open : IsOpen Ui) (hUi_cpt : IsCompact Ui)
    (hUj_open : IsOpen Uj) (hUj_cpt : IsCompact Uj)
    (h : (limit.π F i) ⁻¹' Ui ⊆ (limit.π F j) ⁻¹' Uj) :
    ∃ (k : J) (a : k ⟶ i) (b : k ⟶ j),
      (F.map a) ⁻¹' Ui ⊆ (F.map b) ⁻¹' Uj
```

**`SpectralLimits.descent_of_finite_unions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitOpenDescent.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitOpenDescent.lean#L387). The attribute's comment: “part (3): descent of finite unions”.

> If, in the limit, the preimage of a quasi-compact open `Ui` equals the union of the preimages
> of finitely many quasi-compact opens `U s` (`s : Fin n`), then this equality already holds after
> pulling back along some `j ⟶ i`.

```lean
theorem descent_of_finite_unions
    [∀ i, SpectralSpace (F.obj i)]
    (hF : ∀ ⦃i j : J⦄ (a : i ⟶ j), IsSpectralMap (F.map a))
    (i : J) (n : ℕ) (Ui : Set (F.obj i)) (U : Fin n → Set (F.obj i))
    (hUi_open : IsOpen Ui) (hUi_cpt : IsCompact Ui)
    (hU : ∀ s, IsOpen (U s) ∧ IsCompact (U s))
    (h : (limit.π F i) ⁻¹' Ui = ⋃ s, (limit.π F i) ⁻¹' (U s)) :
    ∃ (j : J) (a : j ⟶ i),
      (F.map a) ⁻¹' Ui = ⋃ s, (F.map a) ⁻¹' (U s)
```

**`SpectralLimits.descent_of_finite_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitOpenDescent.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitOpenDescent.lean#L420). The attribute's comment: “part (4): descent of finite intersections”.

> If, in the limit, the preimage of a quasi-compact open `Ui` equals the intersection of the
> preimages of finitely many quasi-compact opens `U s` (`s : Fin n`), then this equality already
> holds after pulling back along some `j ⟶ i`.

```lean
theorem descent_of_finite_intersections
    [∀ i, SpectralSpace (F.obj i)]
    (hF : ∀ ⦃i j : J⦄ (a : i ⟶ j), IsSpectralMap (F.map a))
    (i : J) (n : ℕ) (Ui : Set (F.obj i)) (U : Fin n → Set (F.obj i))
    (hUi_open : IsOpen Ui) (hUi_cpt : IsCompact Ui)
    (hU : ∀ s, IsOpen (U s) ∧ IsCompact (U s))
    (h : (limit.π F i) ⁻¹' Ui = ⋂ s, (limit.π F i) ⁻¹' (U s)) :
    ∃ (j : J) (a : j ⟶ i),
      (F.map a) ⁻¹' Ui = ⋂ s, (F.map a) ⁻¹' (U s)
```

## Tag 0A31, a lemma

[Tag 0A31](https://stacks.math.columbia.edu/tag/0A31) in the Stacks Project.

**`SpectralSubset.characterizations_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean#L282). The attribute's comment: “equivalence of the five characterizations”.

> **Stacks 0A31, the equivalence.** For a subset `W` of a spectral space the five conditions
> (1) intersection of constructibles and stable under generalization, (2) quasi-compact and stable
> under generalization, (3) the generalizations of a quasi-compact set, (4) an intersection of
> quasi-compact opens, (5) a directed intersection of quasi-compact opens, are all equivalent.

```lean
theorem characterizations_equiv [SpectralSpace X] (W : Set X) :
    (IsStableInterConstructible W ↔ IsStableCompact W) ∧
      (IsStableCompact W ↔ IsGeneralizationsOfCompact W) ∧
        (IsGeneralizationsOfCompact W ↔ IsInterCompactOpen W) ∧
          (IsInterCompactOpen W ↔ IsDirectedInterCompactOpen W)
```

**`SpectralSubset.spectralSpace_of_isStableCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean#L301). The attribute's comment: “conclusion (a): W is spectral”.

> Conclusion (a): under the equivalent conditions, `W` (with the
> subspace topology) is itself a spectral space.

```lean
theorem spectralSpace_of_isStableCompact [SpectralSpace X] (W : Set X) (h : IsStableCompact W) :
    SpectralSpace W
```

**`SpectralSubset.exists_homeomorph_invLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean#L358). The attribute's comment: “conclusion (b): W ≅ lim U_i”.

> Conclusion (b): the canonical map `W → InvLimit U` is a homeomorphism.

```lean
theorem exists_homeomorph_invLimit
    {I : Type*} [Nonempty I] (U : I → Set X)
    (hdir : ∀ i j, ∃ k, U k ⊆ U i ∩ U j)
    (W : Set X) (hWeq : W = ⋂ i, U i) :
    ∃ φ : W ≃ₜ InvLimit U,
      ∀ w : W, ∀ i, ((φ w).1 i : X) = (w : X)
```

**`SpectralSubset.exists_subset_of_subset_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/QuasiCompactOpenInter.lean#L396). The attribute's comment: “conclusion (c): some U_i ⊆ V”.

> Conclusion (c): with the family `U_i` from condition (5), every open
> subset `V` of `X` containing `W` contains some `U_i`.

```lean
theorem exists_subset_of_subset_isOpen [SpectralSpace X]
    {I : Type*} [Nonempty I] (U : I → Set X)
    (hU : ∀ i, IsOpen (U i) ∧ IsCompact (U i))
    (hdir : ∀ i j, ∃ k, U k ⊆ U i ∩ U j)
    (W : Set X) (hWeq : W = ⋂ i, U i)
    (V : Set X) (hVopen : IsOpen V) (hWV : W ⊆ V) :
    ∃ i, U i ⊆ V
```

## Tag 0AP0, a lemma

[Tag 0AP0](https://stacks.math.columbia.edu/tag/0AP0) in the Stacks Project.

**`isLimit_diffLimitCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitGeneralizations.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitGeneralizations.lean#L350).

> **Stacks 0AP0**.
> For a spectral space `X`, a monotone family `U` indexed by a nonempty codirected order and
> `specGen E = ⋂ i, U i`, the cone `diffLimitCone` with apex `specGen E \ E` is a limit cone of
> the diagram `(U i \ E)_i`: the canonical map `specGen E \ E ⟶ lim_i (U i \ E)` is a
> homeomorphism.

```lean
theorem isLimit_diffLimitCone [SpectralSpace X] [Nonempty I] [IsCodirectedOrder I]
    {E : Set X}
    (hmono : ∀ ⦃i j : I⦄, i ≤ j → U i ⊆ U j)
    (hWeq : specGen E = ⋂ i, U i) :
    Nonempty (IsLimit (diffLimitCone U E hmono (fun i => hWeq ▸ Set.iInter_subset U i)))
```

**`isSpectral_specGen_diff_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Spectral/LimitGeneralizations.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Spectral/LimitGeneralizations.lean#L364).

> **Stacks 0AP0**.
> If `X` is a spectral space and `E ⊆ X` is a constructible subset, then the set
> `specGen E \ E` of points specializing into `E` but not lying in `E`, equipped with the
> subspace topology, is a spectral space.

```lean
theorem isSpectral_specGen_diff_constructible [SpectralSpace X] {E : Set X}
    (hE : Topology.IsConstructible E) : SpectralSpace ↥(specGen E \ E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.24, Tag 0A2U](https://stacks.math.columbia.edu/tag/0A2U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
