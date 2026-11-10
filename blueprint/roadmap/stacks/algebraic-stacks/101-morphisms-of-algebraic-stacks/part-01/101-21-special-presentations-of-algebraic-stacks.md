---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_openSubspace_isLocallyOfFinitePresentation_zeroLocus, AlgebraicGeometry.Stack.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular, AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite, AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero, AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_hasQuasiDMPresentation, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation_unconditional
statement: formalized
proof: formalized
---

# 101.21 Special presentations of algebraic stacks

Section 101.21 of the Stacks Project, [Tag 06MC](https://stacks.math.columbia.edu/tag/06MC). 7 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06MD, a lemma

[Tag 06MD](https://stacks.math.columbia.edu/tag/06MD) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubspace_isLocallyOfFinitePresentation_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFinitePresentation.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFinitePresentation.lean#L225). The attribute's comment: “the locally-of-finite-presentation conjunct ONLY: `V(f₁,…,f_r) ⟶ 𝒳` is locally of finite presentation. Flatness of it is NOT proved and no part of that conjunct is claimed. Local finite presentation of the closed immersion `V(f₁,…,f_r) ⟶ U`, which reduces to the surjectivity half of Stacks 03MB, is carried as a hypothesis.”.

> **Stacks 06MD, the locally-of-finite-presentation conjunct.** Let `𝒳` be an algebraic stack
> over `S`, let `U` be an algebraic space with a 1-morphism `f : U ⟶ 𝒳` which is flat and locally
> of finite presentation, let `Spec k ⟶ 𝒳` be a field-valued point, and let `F = U ×_𝒳 Spec k`
> with projection `p : F ⟶ U`. Let `f₁, …, f_r ∈ Γ(U, 𝒪_U)` and let `z` be a geometric point of
> `F` at which the `f_i` map to a regular sequence in `𝒪_{F, z̄}`. Then, after replacing `U` by an
> open subspace containing `p(z)`, the 1-morphism `V(f₁, …, f_r) ⟶ 𝒳` is locally of finite
> presentation.
>
> Only that conjunct is proved; flatness of `V(f₁, …, f_r) ⟶ 𝒳` is not claimed, and the
> implementation notes say why. The flatness and regular-sequence hypotheses of the source are
> recorded and unused — the conjunct proved here needs no shrinking of `U` either, so the open
> subspace produced is the whole of `U` and the stronger statement over an arbitrary open subspace
> is `AlgebraicGeometry.Stack.isLocallyOfFinitePresentation_zeroLocusOnOpenToStack`. Local finite
> presentation of the closed immersion `V(f₁, …, f_r) ⟶ U`, the hypothesis `hslice` of
> `AlgebraicGeometry.Space.isLocallyOfFinitePresentation_vanishingSubfunctor_comp` which reduces
> to the surjectivity half of Stacks 03MB, is carried.

```lean
theorem exists_openSubspace_isLocallyOfFinitePresentation_zeroLocus
    (_hflat : AlgebraicStacks.IsFlat B S hS f)
    (hfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (z : Space.GeometricPoint B S hS Fsp)
    (_hreg : FibreIsRegularSequenceAt.{u, w} B S hS 𝒳 U hU k hk toBase f g a Fsp hFsp eF z)
    (hslice : Space.IsLocallyOfFinitePresentation B S hS (chartZeroLocus B S hS U hU a).ι) :
    ∃ (V : Subfunctor U) (hV : Space.IsOpenSubspace B S hS V),
      Space.pointsMap B S hS Fsp
          (fibreSpaceProjection B S hS 𝒳 U hU k hk toBase f g Fsp eF) z.image ∈
        Set.range (Space.pointsMap B S hS V.toFunctor V.ι) ∧
      AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
        (zeroLocusOnOpenToStack.{u, w} B S hS 𝒳 U hU f a V hV)
```

**`AlgebraicGeometry.Stack.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFlatness.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFlatness.lean#L768).

> **Stacks 06MD.** Let `𝒳` be an algebraic stack over `S`, let `U` be an algebraic space with a
> 1-morphism `f : U ⟶ 𝒳` which is flat and locally of finite presentation, let `Spec k ⟶ 𝒳` be a
> field-valued point, and let `F = U ×_𝒳 Spec k` with projection `p : F ⟶ U`. Let
> `f₁, …, f_r ∈ Γ(U, 𝒪_U)` and let `z` be a geometric point of `F` at which the `f_i` map to a
> regular sequence in the étale local ring `𝒪_{F, z̄}`. Then, after replacing `U` by an open
> subspace containing `p(z)`, the 1-morphism `V(f₁, …, f_r) ⟶ 𝒳` is **flat and locally of finite
> presentation**.
>
> Nothing is carried. Local finite presentation holds over *every* open subspace,
> `AlgebraicGeometry.Stack.isLocallyOfFinitePresentation_zeroLocusOnOpenToStack`. For flatness the
> proof is the source's: base change along a smooth chart of `𝒳` by an algebraic space surjective
> on objects, apply the flatness half of **Stacks 06LW** to the morphism of algebraic spaces
> `U ×_𝒳 𝒲 ⟶ 𝒲` at the fibre which
> `AlgebraicGeometry.Stack.exists_chartFibre_isPullback_isRegular` produces, take the open subspace
> of `U` swept out by the open subspace Stacks 06LW returns — open because the projection
> `U ×_𝒳 𝒲 ⟶ 𝒲` is a base change of the smooth chart, hence flat and locally of finite
> presentation, hence open on points — and read flatness back point by point through the chart
> independence of **Stacks 0CIC**.

```lean
theorem exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular
    (hflat : AlgebraicStacks.IsFlat B S hS f)
    (hfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (z : Space.GeometricPoint B S hS Fsp)
    (hreg : FibreIsRegularSequenceAt.{u, w} B S hS 𝒳 U hU k hk toBase f g a Fsp hFsp eF z) :
    ∃ (V : Subfunctor U) (hV : Space.IsOpenSubspace B S hS V),
      Space.pointsMap B S hS Fsp
          (fibreSpaceProjection B S hS 𝒳 U hU k hk toBase f g Fsp eF) z.image ∈
        Set.range (Space.pointsMap B S hS V.toFunctor V.ι) ∧
      AlgebraicStacks.IsFlat B S hS
          (zeroLocusOnOpenToStack.{u, w} B S hS 𝒳 U hU f a V hV) ∧
        AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
          (zeroLocusOnOpenToStack.{u, w} B S hS 𝒳 U hU f a V hV)
```

## Tag 06ME, a lemma

[Tag 06ME](https://stacks.math.columbia.edu/tag/06ME) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtale.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtale.lean#L246). The attribute's comment: “after replacing the algebraic space by an open subspace containing the image of the given point of the fibre, a 1-morphism locally of finite type whose fibre over a field-valued point has dimension zero at that point is locally quasi-finite. The two clauses of Stacks 06M5 are carried, as the data `W` with `hW` (the open locus on which the 1-morphism is locally quasi-finite) and the hypothesis `hBaseChange` (that locus commutes with the base change along the field-valued point), since Stacks 06M5 is absent from this library; the deduction of the conclusion from them is proved”.

> **Stacks 06ME.** Let `𝒳` be an algebraic stack, let `U` be an algebraic space with a
> 1-morphism `f : U ⟶ 𝒳` which is locally of finite type, let `Spec k ⟶ 𝒳` be a field-valued
> point, and let `F = U ×_𝒳 Spec k` with projection `p : F ⟶ U` and structure 1-morphism
> `q : F ⟶ Spec k`. If `z ∈ |F|` has `dim_z(F) = 0` then, after replacing `U` by an open subspace
> containing `p(z)`, the 1-morphism `U ⟶ 𝒳` is locally quasi-finite.
>
> The proof is the source's. The open substack `W` is the locus `W(f)` of **Stacks 06M5** on which
> `f` is locally quasi-finite, carried as the data `W` together with `hW`; the compatibility of
> that locus with the base change along `g`, which is the second clause of Stacks 06M5, is carried
> as `hBaseChange`. Given those, the conclusion is exactly that `p(z) ∈ |W|`, and that follows
> because the fibre hypothesis puts `z` in an open substack of `F` which is locally quasi-finite
> over `Spec k`, hence inside the preimage of `|W|`.

```lean
theorem exists_openSubstack_isLocallyQuasiFinite
    (_hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (W : OpenSubstack (algebraicSpaceStack.{u, w} B S hS U hU))
    (hW : AlgebraicStacks.IsLocallyQuasiFinite B S hS (W.inclusion ≫ f))
    (hBaseChange : ∀ V : OpenSubstack (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g),
      AlgebraicStacks.IsLocallyQuasiFinite B S hS
          (V.inclusion ≫ fibreStructureMorphism B S hS 𝒳 U hU k hk toBase f g) →
        V.pointSet B S hS ⊆
          AlgebraicStacks.pointsMap B S hS
              (fibreProjection B S hS 𝒳 U hU k hk toBase f g) ⁻¹' W.pointSet B S hS)
    (z : AlgebraicStacks.points B S hS (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g))
    (hz : FibreIsLocallyQuasiFiniteNear.{u, w} B S hS 𝒳 U hU k hk toBase f g z) :
    AlgebraicStacks.pointsMap B S hS
        (fibreProjection B S hS 𝒳 U hU k hk toBase f g) z ∈ W.pointSet B S hS ∧
      AlgebraicStacks.IsLocallyQuasiFinite B S hS (W.inclusion ≫ f)
```

**`AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean#L422). The attribute's comment: “the source's own hypotheses, with the conclusion read on an open substack of the stack of the algebraic space: the 1-morphism is locally of finite type and the given point z of the fibre has dim_z(F) = 0, the dimension of Stacks 04N5 of a representing algebraic space Fsp of the fibre at z. Nothing is added and nothing is weakened. The proof is exists_openSubstack_isLocallyQuasiFinite_unconditional of ChartShrinkingQuasiFiniteEtaleUnconditional -- which states the same conclusion at the intermediate condition the source's own proof extracts from dim_z(F) = 0, that some open substack of the fibre containing z is locally quasi-finite over Spec k -- composed with the step the source's proof takes from dim_z(F) = 0 to that condition by Stacks 04NV, which is fibreIsLocallyQuasiFiniteNear_of_dimensionAtPoint_eq_zero above. The source's open subspace of the algebraic space is rendered here as an open substack of the stack of that space, with the same point set, both directions of that passage being proved as exists_openSubstack_algebraicSpaceStack_of_isOpenImmersion and exists_isOpenSubspace_property_eq_essImage; the conclusion read on an open subspace, as the source reads it, is exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero below. The point of the fibre is the image of z under the comparison spacePointMap of the representing equivalence, which bijective_spacePointMap_representing makes a bijection, so no point of the fibre is excluded by stating the hypothesis on Fsp”.

> **Stacks 06ME at the source's own hypothesis, with the conclusion read on an open substack.**
> Let `𝒳` be an algebraic stack, let `U` be an algebraic space with a 1-morphism `f : U ⟶ 𝒳`
> locally of finite type, let `Spec k ⟶ 𝒳` be a field-valued point, let `Fsp` represent the fibre
> `F = U ×_𝒳 Spec k` through `eF`, and let `z` be a point of `|Fsp|` with `dim_z(F) = 0` — the
> dimension of **Stacks 04N5** of the algebraic space `Fsp` at `z`. Then there is an open substack
> `W` of the algebraic stack of `U` whose point set contains `p(z)` and for which `W.inclusion ≫ f`
> is locally quasi-finite.
>
> This is `AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite_unconditional` with its
> fibre
> hypothesis `AlgebraicGeometry.Stack.FibreIsLocallyQuasiFiniteNear` replaced by the source's
> `dim_z(F) = 0`, through
> `AlgebraicGeometry.Stack.fibreIsLocallyQuasiFiniteNear_of_dimensionAtPoint_eq_zero`. Nothing is
> added and nothing is weakened: the finite-type hypothesis is the source's, and the hypothesis on
> `z` is the source's. The point of `|F|` is the image of `z` under the comparison
> `AlgebraicGeometry.Stack.spacePointMap` of the representing equivalence, which is a bijection by
> `AlgebraicGeometry.Stack.bijective_spacePointMap_representing`, so every point of `|F|` is
> reached.

```lean
theorem exists_openSubstack_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (z : Space.points B S hS Fsp)
    (hz : Space.dimensionAtPoint B S hS Fsp hFsp z = 0) :
    ∃ W : OpenSubstack (algebraicSpaceStack.{u, w} B S hS U hU),
      AlgebraicStacks.pointsMap B S hS
          (fibreProjection B S hS 𝒳 U hU k hk toBase f g)
          (spacePointMap B S hS Fsp
            (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g).val
            (representingEquivalence B S hS Fsp
              (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g).val eF).functor z) ∈
        W.pointSet B S hS ∧
        AlgebraicStacks.IsLocallyQuasiFinite B S hS (W.inclusion ≫ f)
```

**`AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean#L464). The attribute's comment: “the statement of the source, hypotheses and conclusion: the 1-morphism out of the algebraic space is locally of finite type, the given point z of the fibre has dim_z(F) = 0 -- the dimension of Stacks 04N5 of a representing algebraic space Fsp of the fibre at z -- and after replacing the algebraic space by an open subspace of Stacks 02YU, part (2), containing the image of z, the 1-morphism is locally quasi-finite, the replacement read as the composite of the 1-morphism of Stacks 0458 induced by that open subspace. Nothing is added and nothing is weakened. The proof is exists_isOpenSubspace_isLocallyQuasiFinite of ChartShrinkingOpenSubspace -- the same conclusion at the intermediate condition the source's own proof extracts from dim_z(F) = 0 -- composed with the step the source's proof takes from dim_z(F) = 0 to that condition by Stacks 04NV, which is fibreIsLocallyQuasiFiniteNear_of_dimensionAtPoint_eq_zero above. The point of the fibre is the image of z under the comparison spacePointMap of the representing equivalence, which bijective_spacePointMap_representing makes a bijection, so no point of the fibre is excluded by stating the hypothesis on Fsp”.

> **Stacks 06ME at the source's own hypothesis, with the conclusion read on an open subspace.**
> The statement of the source: with `f : U ⟶ 𝒳` locally of finite type and `z` a point of the
> fibre `F = U ×_𝒳 Spec k` at which the dimension of `F` is zero, there is an open subspace
> `V ⊆ U` of **Stacks 02YU**, part (2), whose point set contains `p(z)` and for which the
> composite of the 1-morphism of **Stacks 0458** induced by `V` with `f` is locally quasi-finite.
>
> This is `AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite` with its fibre
> hypothesis replaced by the source's, through
> `AlgebraicGeometry.Stack.fibreIsLocallyQuasiFiniteNear_of_dimensionAtPoint_eq_zero`. Both
> hypotheses are now the source's and the conclusion is the source's.

```lean
theorem exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (z : Space.points B S hS Fsp)
    (hz : Space.dimensionAtPoint B S hS Fsp hFsp z = 0) :
    ∃ (V : Subfunctor U) (hV : Space.IsOpenSubspace B S hS V),
      AlgebraicStacks.pointsMap B S hS
          (fibreProjection B S hS 𝒳 U hU k hk toBase f g)
          (spacePointMap B S hS Fsp
            (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g).val
            (representingEquivalence B S hS Fsp
              (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g).val eF).functor z) ∈
        spacePointMap B S hS U (algebraicSpaceStack.{u, w} B S hS U hU).val
            (BasedFunctor.id (fibredCategory B S hS U).val) ''
          Set.range (Space.pointsMap B S hS V.toFunctor V.ι) ∧
        AlgebraicStacks.IsLocallyQuasiFinite B S hS
          (algebraicSpaceStackMap.{u, w} B S hS hV.1 hU V.ι ≫ f)
```

## Tag 06MF, a theorem

[Tag 06MF](https://stacks.math.columbia.edu/tag/06MF) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationTheorem.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationTheorem.lean#L197). The attribute's comment: “the equivalence of (1) quasi-DM with (2) the existence of a surjective, flat, locally finitely presented, locally quasi-finite presentation by a scheme. Both implications are carried, as the hypotheses `hForward` (the structure theorem: Stacks 06MD, 06ME, 06G2, 06G3 are absent) and `hBackward` (Stacks 06MB part (2) is present but the repackaging of the Section 04XB local quasi-finiteness of the chart into its HasRelativeProperty form is absent)”.

> **Stacks 06MF.** An algebraic stack is quasi-DM exactly when there is a scheme of the site
> with a surjective, flat, locally finitely presented, locally quasi-finite 1-morphism to it.
>
> Both implications are carried; see
> `AlgebraicGeometry.Stack.ExistsQuasiDMPresentationOfIsAbsolutelyQuasiDM` and
> `AlgebraicGeometry.Stack.IsAbsolutelyQuasiDMOfHasQuasiDMPresentation`.

```lean
theorem isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation
    (hForward : ExistsQuasiDMPresentationOfIsAbsolutelyQuasiDM.{u, w} B S hS hZ)
    (hBackward : IsAbsolutelyQuasiDMOfHasQuasiDMPresentation.{u, w} B S hS hZ)
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ 𝒳 ↔
      HasQuasiDMPresentation.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_hasQuasiDMPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean#L374). The attribute's comment: “the implication (2) implies (1): a surjective, flat, locally finitely presented, locally quasi-finite presentation by a scheme of the site makes an algebraic stack quasi-DM”.

> An algebraic stack with a surjective, flat, locally finitely presented, locally quasi-finite
> presentation by a scheme of the site is quasi-DM: the implication (2) ⟹ (1).

```lean
theorem isAbsolutelyQuasiDM_of_hasQuasiDMPresentation (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h : HasQuasiDMPresentation.{u, w} B S hS 𝒳) :
    AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean#L500). The attribute's comment: “the equivalence of (1) quasi-DM with (2) the existence of a surjective, flat, locally finitely presented, locally quasi-finite presentation by a scheme. BOTH implications are proved and nothing is carried. (2) implies (1) is Stacks 06MB part (2), isAbsolutelyQuasiDM_of_hasQuasiDMPresentation; (1) implies (2) is the structure theorem, hasQuasiDMPresentation_of_isAbsolutelyQuasiDM, whose local half is the chart of exists_flat_isLocallyOfFinitePresentation_isLocallyQuasiFinite_chart_at_finiteTypePoint -- the smooth chart of 06FX with a closed point over the finite type point, the charted self-intersection of 04ZP and 04SW, the identity point of 04XH, and the slice cut out by a regular sequence in the etale local ring of a fibre (06LC, 06MD, 06LW) shrunk to be locally quasi-finite by 06M3 and 06ME -- and whose assembly is hasQuasiDMPresentation_of_forall_isLocallyQuasiFinite: the 1-morphism out of the coproduct W = coprod_x Z_x, the descent of the three properties along the summand inclusions, and surjectivity from the corollary of 06G2. The coproduct lies in the site by contains_sigma_of_forall_size_le, which the uniform bound 2 ^ 2 ^ size U_0 on the charts supplies -- the finite type points need not be below the cofinality of the site's cutoff, so contains_sigma_of_lt_cof does not apply”.

> An algebraic stack is quasi-DM exactly when there is a scheme of the site with a surjective,
> flat, locally finitely presented, locally quasi-finite 1-morphism to it.

```lean
theorem isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation_unconditional
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ 𝒳 ↔
      HasQuasiDMPresentation.{u, w} B S hS 𝒳
```

## Tag 06N0, a lemma

[Tag 06N0](https://stacks.math.columbia.edu/tag/06N0) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_division_identityArrowOpens_of_isoSpecField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IdentityArrowDivision.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IdentityArrowDivision.lean#L84). The attribute's comment: “the division of the groupoid of a flat field-valued presentation by the open and closed piece of its arrow scheme through the identity, with the quotient the spectrum of a field: the step of the proof which produces the field k_0 of invariants”.

> **Stacks 04S4 applied to the open and closed piece through the identity.**  A groupoid scheme
> whose object scheme is the spectrum of a field, whose arrow scheme is zero-dimensional and whose
> pre-relation is unramified, separated, locally of finite type and locally quasi-finite can be
> divided by the piece of its arrow scheme through the identity, and the quotient is the spectrum
> of a field.

```lean
theorem exists_division_identityArrowOpens_of_isoSpecField {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) (k : Type u) [Field k]
    (iso : G.objects.left ≅ Spec (.of k))
    [IsLocallyArtinian G.arrows.left]
    [LocallyOfFiniteType G.source.left] [LocallyOfFiniteType G.target.left]
    [Unramified (prod.lift G.target G.source).left]
    [IsSeparated (prod.lift G.target G.source).left]
    [LocallyOfFiniteType (prod.lift G.target G.source).left]
    [LocallyQuasiFinite (prod.lift G.target G.source).left]
    (u : G.objects.left) :
    ∃ (P : OpenFiniteSubgroupoid G)
      (D : Division G P.subgroupoid P.inclusion P.objects_eq),
      Set.range P.inclusion.mapArrows.left.base = {G.identity.left.base u} ∧
        IsField Γ(D.quotient.left, ⊤)
```

**`AlgebraicGeometry.Stack.hasSurjectiveEtaleFieldSpectrumCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCover.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCover.lean#L170). The attribute's comment: “a DM, locally Noetherian, reduced algebraic stack with a singleton point space admits a surjective etale 1-morphism from the spectrum of a field. The implication is carried as the hypothesis `hCover`: the source's first step is the direction (1) => (2) of Stacks 06MP, of which this library proves only the converse, and Stacks 06FF, 06LZ and 04S4 are absent too”.

> **Stacks 06N0.** A DM, locally Noetherian, reduced algebraic stack whose point space is a
> singleton admits a field `k` and a surjective étale 1-morphism `Spec k ⟶ 𝒵`.
>
> The implication is carried as the hypothesis `hCover`; see
> `AlgebraicGeometry.Stack.ExistsSurjectiveEtaleFieldCoverOfReducedSingletonDM` for exactly which
> cited inputs are absent and why no part of the chain can be run without them.

```lean
theorem hasSurjectiveEtaleFieldSpectrumCover
    (hCover : ExistsSurjectiveEtaleFieldCoverOfReducedSingletonDM.{u, w} B S hS hZ)
    (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (h𝒵 : IsReducedLocallyNoetherianSingletonDM.{u, w} B S hS hZ 𝒵) :
    HasSurjectiveEtaleFieldSpectrumCover.{u, w} B S hS 𝒵
```

**`AlgebraicGeometry.Stack.hasSurjectiveEtaleFieldSpectrumCover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCoverUnconditional.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCoverUnconditional.lean#L164). The attribute's comment: “a DM, locally Noetherian, reduced algebraic stack with a singleton point space admits a surjective etale 1-morphism from the spectrum of a field. The field-valued point comes in two steps: Stacks 06MP (1) => (2) supplies a surjective, flat, locally finitely presented xi : Spec k -> Z, and the groupoid (U, R, s, t, c) of that flat presentation, with U = Spec k and R = U x_Z U, is divided by the open and closed subgroupoid P through the identity, whose quotient U_bar = Spec k_0 is the spectrum of the field of invariants. The division is exists_division_identityArrowOpens_etale_pointGroupoid, on the four conclusions of Stacks 04S4 in exists_division; it is run at the de-realization of the self-intersection groupoid, whose object and arrow spaces are representable by isRepresentable_objects_pointGroupoid_fieldSpectrum and isRepresentable_arrows_pointGroupoid_fieldSpectrum, the latter being condition (2) of Stacks 06LZ read on the base site at the dimension bound dimension_relation_le_zero_fieldSpectrum, i.e. Stacks 06FF against the quasi-DM hypothesis through Stacks 050H part (5). Etaleness of U_bar -> Z follows the source's steps 6 and 8 rather than its Stacks 04XD reading: the divided groupoid is the restriction of the descended groupoid (U_bar, R_bar, s_bar, t_bar, c_bar) along the finite locally free surjection U -> U_bar, so [U/R] -> [U_bar/R_bar] is an equivalence by Stacks 046T (nonempty_isEquivalenceOver_quotientStackMap_realizationHom, whose clause (1) is full faithfulness of the evaluations of the descent morphism and whose clause (2) is that its map on objects is an fppf covering), [U/R] -> Z is an equivalence by Stacks 04WY (nonempty_isEquivalenceOver_canonicalMap), and s_bar is etale by Division.etale_descended_source, which is Stacks 047W at unramifiedness through etale_source_of_flat_of_isOpenImmersion_identity rather than the computation of Omega_{R_bar/U_bar} that Stacks 04R9 gives the source. Stacks 04M9 then makes the projection S_{U_bar} -> [U_bar/R_bar] of Stacks 044R etale (isRelativelyEtale_quotientStackProjection_realization), and two instances of Stacks 0457 carry that verdict across the equivalence with Z and down the universe lift of the source, giving quotientProjectionSchemeStackMap, which is etale in the sense of Stacks 0CIL by isEtale_of_isRelativelyEtale. The DM hypothesis enters only at the division, in the absolute form of Stacks 050D part (5), turned into DM-ness over S by Stacks 050N part (1)”.

> **Stacks 06N0.** A DM, locally Noetherian, reduced algebraic stack whose point space is a
> singleton admits a field `k` and a surjective étale 1-morphism `Spec k ⟶ 𝒵`.
>
> The field-valued point is produced in two steps. **Stacks 06MP**, part (1) ⟹ (2), gives a
> surjective, flat, locally finitely presented `ξ : Spec k ⟶ 𝒵`; and
> `AlgebraicGeometry.Stack.exists_isEtale_fieldSpectrum_cover_of_flat_fieldSpectrum_cover` divides
> the groupoid of that flat presentation by the open subgroupoid through the identity and returns
> an étale 1-morphism out of the spectrum of the field of invariants. Surjectivity of that
> 1-morphism is read off the point space: `|𝒵|` is a subsingleton and the algebraic stack of the
> spectrum of a field has a point. The DM hypothesis is used at the division, in the absolute form
> of **Stacks 050D** part (5), turned into DM-ness over `S` by **Stacks 050N** part (1).

```lean
theorem hasSurjectiveEtaleFieldSpectrumCover_unconditional
    (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (h𝒵 : IsReducedLocallyNoetherianSingletonDM.{u, w} B S hS hZ 𝒵) :
    HasSurjectiveEtaleFieldSpectrumCover.{u, w} B S hS 𝒵
```

## Tag 06N2, a lemma

[Tag 06N2](https://stacks.math.columbia.edu/tag/06N2) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isOpenSubspace_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingOpenSubspace.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingOpenSubspace.lean#L358). The attribute's comment: “the conclusion read on an open subspace of the algebraic space, as the source reads it: the composite of the 1-morphism of Stacks 0458 induced by an open subspace containing the image of the given point of the fibre with the given 1-morphism is etale. Nothing is added to exists_openSubstack_isEtale_unconditional: its open substack is carried to an open subspace with the same point set by exists_isOpenSubspace_property_eq_essImage, and the etaleness is carried across the Stacks 0506 factorization of that subspace's 1-morphism through the substack's inclusion by isEtale_comp_of_eq_essImage”.

> **Stacks 06N2, with the conclusion read on an open subspace of the chart.** Let `𝒳` be an
> algebraic stack, let `U` be an algebraic space with a 1-morphism `f : U ⟶ 𝒳` which is flat and
> locally of finite presentation, let `Spec k ⟶ 𝒳` be a field-valued point and let
> `F = U ×_𝒳 Spec k` with projection `p : F ⟶ U`. If `F ⟶ Spec k` is unramified at `z ∈ |F|` then
> there is an open subspace `V ⊆ U`, in the sense of **Stacks 02YU**, part (2), whose point set
> contains `p(z)` and for which the composite of the 1-morphism of **Stacks 0458** induced by `V`
> with `f` is étale.
>
> This is the source's own conclusion, obtained from
> `AlgebraicGeometry.Stack.exists_openSubstack_isEtale_unconditional` the way
> `AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite` is obtained from
> Stacks 06ME, with `AlgebraicGeometry.Stack.isEtale_comp_of_eq_essImage` for the transport.

```lean
theorem exists_isOpenSubspace_isEtale
    (hflat : AlgebraicStacks.IsFlat B S hS f)
    (hfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (z : AlgebraicStacks.points B S hS (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g))
    (hz : FibreIsUnramifiedNear.{u, w} B S hS 𝒳 U hU k hk toBase f g z) :
    ∃ (V : Subfunctor U) (hV : Space.IsOpenSubspace B S hS V),
      AlgebraicStacks.pointsMap B S hS
          (fibreProjection B S hS 𝒳 U hU k hk toBase f g) z ∈
        spacePointMap B S hS U (algebraicSpaceStack.{u, w} B S hS U hU).val
            (BasedFunctor.id (fibredCategory B S hS U).val) ''
          Set.range (Space.pointsMap B S hS V.toFunctor V.ι) ∧
        IsEtale B S hS (algebraicSpaceStackMap.{u, w} B S hS hV.1 hU V.ι ≫ f)
```

**`AlgebraicGeometry.Stack.exists_openSubstack_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtale.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtale.lean#L285). The attribute's comment: “after replacing the algebraic space by an open subspace containing the image of the given point of the fibre, a flat, locally finitely presented 1-morphism whose fibre over a field-valued point is unramified at that point is etale. Three inputs are carried: the data `W` with `hW` and the hypothesis `hBaseChange`, which are the two clauses of Stacks 06M5 at etaleness, absent from this library; and `hFibreEtale`, which is Stacks 06LU for 1-morphisms of algebraic stacks over the field-valued point, available in this library only for morphisms of algebraic spaces. The deduction of the conclusion from them is proved”.

> **Stacks 06N2.** Let `𝒳` be an algebraic stack, let `U` be an algebraic space with a
> 1-morphism `f : U ⟶ 𝒳` which is flat and locally of finite presentation, let `Spec k ⟶ 𝒳` be a
> field-valued point, and let `F = U ×_𝒳 Spec k` with projection `p : F ⟶ U` and structure
> 1-morphism `q : F ⟶ Spec k`. If `q` is unramified at `z ∈ |F|` then, after replacing `U` by an
> open subspace containing `p(z)`, the 1-morphism `U ⟶ 𝒳` is étale.
>
> The proof is the source's. The open substack `W` is the locus `W(f)` of **Stacks 06M5** on which
> `f` is étale, carried as the data `W` with `hW`, and its compatibility with the base change along
> `g` is carried as `hBaseChange`. The step from the source's pointwise hypothesis to étaleness of
> the fibre near `z` is **Stacks 06LU** — unramified plus flat plus locally of finite presentation
> gives étale — which the library has for morphisms of algebraic spaces
> (`AlgebraicGeometry.Space.isEtale_of_isFlat_of_isUnramified`) but not for 1-morphisms of
> algebraic stacks; it is carried as `hFibreEtale`, stated over `Spec k`, which is where the source
> applies it. Given those, the conclusion is that `p(z) ∈ |W|`.

```lean
theorem exists_openSubstack_isEtale
    (_hflat : AlgebraicStacks.IsFlat B S hS f)
    (_hfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (W : OpenSubstack (algebraicSpaceStack.{u, w} B S hS U hU))
    (hW : IsEtale B S hS (W.inclusion ≫ f))
    (hFibreEtale : ∀ V : OpenSubstack (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g),
      IsUnramified B S hS
          (V.inclusion ≫ fibreStructureMorphism B S hS 𝒳 U hU k hk toBase f g) →
        IsEtale B S hS
          (V.inclusion ≫ fibreStructureMorphism B S hS 𝒳 U hU k hk toBase f g))
    (hBaseChange : ∀ V : OpenSubstack (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g),
      IsEtale B S hS
          (V.inclusion ≫ fibreStructureMorphism B S hS 𝒳 U hU k hk toBase f g) →
        V.pointSet B S hS ⊆
          AlgebraicStacks.pointsMap B S hS
              (fibreProjection B S hS 𝒳 U hU k hk toBase f g) ⁻¹' W.pointSet B S hS)
    (z : AlgebraicStacks.points B S hS (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g))
    (hz : FibreIsUnramifiedNear.{u, w} B S hS 𝒳 U hU k hk toBase f g z) :
    AlgebraicStacks.pointsMap B S hS
        (fibreProjection B S hS 𝒳 U hU k hk toBase f g) z ∈ W.pointSet B S hS ∧
      IsEtale B S hS (W.inclusion ≫ f)
```

**`AlgebraicGeometry.Stack.exists_openSubstack_isEtale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtaleUnconditional.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtaleUnconditional.lean#L229). The attribute's comment: “after replacing the algebraic space by an open subspace containing the image of the given point of the fibre, a flat, locally finitely presented 1-morphism whose fibre over a field-valued point is unramified at that point is etale. Nothing is carried: the open substack is the locus W(P, f) of assertion (A) of Stacks 06M3 at P = unramified -- the entry of the list of Stacks 06M5 whose base-change clause holds for an arbitrary base change, which is why it and not the etale entry applies to a base change along a field-valued point -- produced by exists_isRelativePropertyLocus_of_hasRelativePropertyLocusOnSpaces from the entry-(3) instances of LocalSourceLemmaUnramified, and the conclusion that the image of the given point of the fibre lies in it is the maximality half of assertion (B) at the open substack the fibre hypothesis supplies. The comparison of the two renderings of unramifiedness, Stacks 0CIT against the relative notion of Stacks 04XB, is available in both directions for a 1-morphism representable by algebraic spaces, by hasSurjectiveEtaleSmoothDiagram_of_isRepresentableByAlgebraicSpaces, and needs nothing of Stacks 0CIA. Stacks 06LU for 1-morphisms of algebraic stacks is not carried but proved, and it is what turns the locus into the etaleness of the conclusion”.

> **Stacks 06N2.** Let `𝒳` be an algebraic stack, let `U` be an algebraic space with a
> 1-morphism `f : U ⟶ 𝒳` which is flat and locally of finite presentation, let `Spec k ⟶ 𝒳` be a
> field-valued point, and let `F = U ×_𝒳 Spec k` with projection `p : F ⟶ U` and structure
> 1-morphism `q : F ⟶ Spec k`. If `q` is unramified at `z ∈ |F|` then, after replacing `U` by an
> open subspace containing `p(z)`, the 1-morphism `U ⟶ 𝒳` is étale.
>
> The proof is the source's, and nothing is carried. The open substack `W` is the locus `W(𝒫, f)`
> of assertion (A) of **Stacks 06M3** at `𝒫 = ` **unramifiedness** — the entry of the list of
> **Stacks 06M5** whose base-change clause holds for an *arbitrary* base change, and so the entry
> that applies to the base change along a field-valued point. It exists by
> `AlgebraicGeometry.Stack.exists_isRelativePropertyLocus_of_hasRelativePropertyLocusOnSpaces` at
> the entry-(3) instances
> `AlgebraicGeometry.Stack.hasRelativePropertyLocusOnSpaces_isUnramified` and
> `AlgebraicGeometry.Stack.relativePropertyLocusBaseChange_isUnramified` of
> `StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaUnramified.lean`, the source's `𝒬` being
> local finite type, which `f` has because it is locally of finite presentation
> (**Stacks 0464**).
>
> The conclusion `p(z) ∈ |W|` is the maximality half of assertion (B),
> `AlgebraicGeometry.Stack.pointSet_subset_preimage_of_hasRelativeProperty`, at the open substack
> of `F` that the fibre hypothesis supplies. That step consumes unramifiedness in the relative
> sense of **Stacks 04XB** while the fibre hypothesis and the étaleness criterion are stated at
> `AlgebraicGeometry.Stack.IsUnramified` (**Stacks 0CIT**), and *both* directions of that
> comparison are available here because every 1-morphism in sight is representable by algebraic
> spaces: `AlgebraicGeometry.Stack.hasRelativeProperty_unramified_of_isUnramified` and
> `AlgebraicGeometry.Stack.isUnramified_of_hasRelativeProperty_unramified`, whose étale-smooth
> diagram comes from
> `AlgebraicGeometry.Stack.hasSurjectiveEtaleSmoothDiagram_of_isRepresentableByAlgebraicSpaces`
> and not from **Stacks 0CIA**. Given that comparison, an open `W` with `hW` and the base-change containment
> `hBaseChange` are not needed as hypotheses.
>
> Étaleness of `f|_W` is **Stacks 06LU** for 1-morphisms of algebraic stacks,
> `AlgebraicGeometry.Stack.isEtale_fullSubcategoryInclusion_comp_of_isUnramified`, applied to the
> restriction of `f` to `W`, which is flat and locally of finite presentation because `f` is.

```lean
theorem exists_openSubstack_isEtale_unconditional
    (hflat : AlgebraicStacks.IsFlat B S hS f)
    (hfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (z : AlgebraicStacks.points B S hS (fibreOverFieldPoint B S hS 𝒳 U hU k hk toBase f g))
    (hz : FibreIsUnramifiedNear.{u, w} B S hS 𝒳 U hU k hk toBase f g z) :
    ∃ W : OpenSubstack (algebraicSpaceStack.{u, w} B S hS U hU),
      AlgebraicStacks.pointsMap B S hS
          (fibreProjection B S hS 𝒳 U hU k hk toBase f g) z ∈ W.pointSet B S hS ∧
        IsEtale B S hS (W.inclusion ≫ f)
```

## Tag 06N3, a theorem

[Tag 06N3](https://stacks.math.columbia.edu/tag/06N3) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAbsolutelyDM_iff_isDeligneMumfordStack_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AbsolutelyDMEtaleChartAssembly.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AbsolutelyDMEtaleChartAssembly.lean#L737). The attribute's comment: “the equivalence of (1) DM with (2) Deligne-Mumford and (3) the existence of a surjective etale presentation by a scheme; (2) and (3) are the same condition here, since Stacks 03YO defines Deligne-Mumford that way. The implication (2) => (1) is proved, from Stacks 06MB part (1); the structure theorem (1) => (3) is PROVED, not carried, as existsEtalePresentationOfIsAbsolutelyDM of this file -- the chart at ONE finite type point with the uniform size bound (exists_isRelativelyEtale_chart_size_le_of_isFiniteTypePoint) fed to the family assembly existsEtalePresentationOfIsAbsolutelyDM_of_forall_exists_chart. The statement binds only the containment hZ of the terminal scheme, which the absolute Deligne-Mumford condition is stated at, and the algebraic stack 𝒳, and nothing stands for the structure theorem. The CHART CONSTRUCTION it runs on, the source's etale chart at each finite type point together with the site-membership of their coproduct, is isolated as ExistsEtaleChartFamilyOfIsAbsolutelyDM, and delivers the presentation by existsEtalePresentationOfIsAbsolutelyDM_of_existsEtaleChartFamily. Everything the source does after the charts is proved, in isDeligneMumfordStack_of_forall_isRelativelyEtale: the 1-morphism out of the coproduct W = ∐_x Z_x is exists_stackMap_comp_iso_sigmaOver_of_lt_cof, its surjectivity is exists_isSurjective_stackMap_of_finiteTypePoints_subset_iUnion_range (resting on 06R7 and the corollary of 06G2 rather than on any property of the assembled chart), and its relative etaleness is isRelativelyEtale_of_isColimit_of_forall_isRelativelyEtale, the descent of the relative property of 03YK along the summand inclusions. NO TAG of the construction is carried. Stacks 06N0 is hasSurjectiveEtaleFieldSpectrumCover_unconditional, at its own binders: the division of the groupoid of the flat field-valued presentation by the open and closed subgroupoid through the identity is exists_division_identityArrowOpens_of_isoSpecField, on identityOpenFiniteSubgroupoid and mono_prodLift_of_unramified; the two tags it rests on are proved -- all four conclusions of 04S4 are exists_division and condition (2) of 06LZ is isRepresentable_of_isLocallyOfFiniteType_over_field; the construction carrying the stack-level flat presentation to a GroupoidScheme is the de-realization of the self-intersection groupoid, on isRepresentable_objects_pointGroupoid_fieldSpectrum and isRepresentable_arrows_pointGroupoid_fieldSpectrum; and the etaleness of Spec k_0 -> Z is isOpenImmersion_descended_identity and etale_descended_source read off the presentation through the quotient stack of the divided groupoid, by isEtale_quotientProjectionSchemeStackMap across the 046T equivalence nonempty_isEquivalenceOver_quotientStackMap_realizationHom, rather than by 04XD. So the source's unramified field-valued point at a finite type point follows outright, by exists_relativelyUnramified_fieldSpectrum_point_of_isFiniteTypePoint, whose own binders are its statement's. The step before it is PROVED and not carried: the residual gerbe exists, by 06G3 (1) => (3) (existsLocallyOfFiniteTypeResidualGerbe, which needs neither Artin's theorem 06DC nor 04Y5 (2) => (3), cutting the gerbe out of the target instead), its inclusion is a monomorphism (AlgebraicStacks.isMonomorphism_fullSubcategoryInclusion) and the gerbe is a reduced, locally Noetherian, one-point DM algebraic stack, which is exactly the hypothesis of 06N0 (isReducedLocallyNoetherianSingletonDM_of_isResidualGerbeAt, by 06MZ at that monomorphism). So 06G3 (1) => (3) is not carried either. Stacks 06MP (1) => (2) and both halves of 06MM are available. What else is missing is the body of the source's argument at a single finite type point -- the affine V etale over F = U x_X Spec k, its closed point with residue field finite separable over k, the regular sequence, and the slicing -- of which two steps are available: from the source's phi(m_u) O_{V,v} = m_v of 02GF, the regular sequence is exists_mem_maximalIdeal_isRegular_ofList_eq_maximalIdeal_fiberStalk_of_smooth, which produces it GENERATING the maximal ideal of the fibre stalk and not merely cutting it to dimension zero (the fibre stalk of a smooth morphism is regular, so a minimal generating family selected inside phi(m_u) by exists_fn_mem_maximalIdeal_ofList_map_eq_maximalIdeal is regular by 00NQ), and the residue computation O_{T,v} = kappa(v) off it is map_maximalIdeal_comp_eq_of_ofList_eq_maximalIdeal_fiberStalk, read on the scheme-theoretic fibre by isField_fiberStalk_comp_of_ofList_eq_maximalIdeal_fiberStalk. Both clauses of 02GF that body needs are proved as well, each off the unramifiedness of F -> U that the monomorphy of Z_x -> X gives: the PRODUCTION of phi(m_u) O_{V,v} = m_v, and with it the sequence generating m_v, is exists_fn_mem_maximalIdeal_isRegular_ofList_eq_maximalIdeal_stalk_of_unramifiedAt (with exists_isAffineOpen_isRegular_ofList_eq_maximalIdeal_stalk_of_unramifiedAt reading it as regular functions on an affine open, the source's first shrinking), and its passage to the ETALE local ring where 06MD reads its hypothesis is exists_fn_isRegular_ofList_eq_maximalIdeal_etaleLocalRing_of_unramifiedAt across the faithful flatness of 05VP and the square of local rings of 05VU, with forall_isRegular_etaleLocalRingMap_germ_of_isRegular_chartLocalRing the same passage in the germ shape FibreIsRegularSequenceAt is written in, quantifier over etale neighbourhoods included (it costs nothing, by etaleLocalRingMap_etaleLocalRingGerm_eval_eq), so that the fibre hypothesis of 06MD is reduced to a regular sequence in the ordinary local ring of a scheme chart of the fibre; the SECOND clause of 02GF for the slice, the transport of the finite separability of kappa(v)/k along O_{V,v} ->> O_{T,v}, is unramifiedAt_comp_of_ofList_eq_maximalIdeal_fiberStalk, on bijective_residueFieldMap_of_isPreimmersion, with unramifiedAt_comp_of_ofList_eq_maximalIdeal_stalk the same statement at a generating sequence read in O_{V,v} -- where the sequence above is produced -- the two agreeing over a field-valued point of the base by ofList_eq_maximalIdeal_fiberStalk_of_ofList_eq_maximalIdeal. The SLICING POINT of that body is proved too, with everything both slicing lemmas read off it: exists_isClosed_isAffineOpen_isRegular_ofList_eq_maximalIdeal_finiteSeparable_of_unramified of SmoothSliceSeparablePoint takes an unramified q : V -> U of schemes with V nonempty and smooth over Spec k and returns the closed point v of 056U, the regularity of O_{V,v}, the sequence of regular functions on an affine open of U whose germs generate m_v as a regular sequence, and the residue field extension in the shape the criterion of 02GF reads it; the two come stated over DIFFERENT renderings of kappa(v) as an extension -- 056U through evaluation of global sections of Spec k, the criterion over kappa(pi v) through residueFieldMap -- and the reconciliation is finite_separable_residueFieldMap_of_finite_separable_Gammaevaluation of the same file, the two algebra structures sitting in one scalar tower by Gammaevaluation_naturality, with isRegularLocalRing_stalk_of_smooth_over_field the scheme form of the regularity (056S on stalks through 02IT) and unramifiedAt_comp_of_ofList_eq_maximalIdeal_stalk_over_field the unramifiedness of the slice with the hypothesis on the base discharged, the local ring of Spec k being the field itself. The slicing sequence in the etale local ring is likewise available off the hypotheses the assembly PRODUCES rather than off a chart square: exists_fn_isRegular_ofList_eq_maximalIdeal_etaleLocalRing_of_isUnramified of FibreSlicingSequenceFromIsUnramified asks only for Space.IsUnramified of the projection F -> U and regularity of F, discharging the chart-square hypotheses itself by unramified_chartMap_of_isUnramified (what Space.IsUnramified says, 03ZH part (1)) and isRegularLocalRing_chartLocalRing (06M1's etale-local regularity carried to a prescribed small etale neighbourhood by 03E8 and read on the stalk by 02IT). What remains of the body is its ASSEMBLY at one finite type point, and that is now exactly the identifications and the plumbing. The relative unramifiedness of exists_relativelyUnramified_fieldSpectrum_point_of_isFiniteTypePoint is NOT carried: read at a chart it is Space.IsUnramified of the projection F -> U of the fibre F = U x_X Spec k, by isUnramified_fibreSpaceProjection_of_relativeProperty of FibreProjectionUnramified, which carries the relative condition to the projection by 045C (hasRelativeProperty_baseChange_algebraicStacks) and reads it on the representing morphism by the 04XB bridge (hasRelativeProperty_iff_prop_representingMap); with the regularity of F that gives the slicing sequence in the etale local ring off the stack-level hypotheses alone, exists_fn_isRegular_ofList_eq_maximalIdeal_etaleLocalRing_fibre of the same file. Its companions are proved, the REGULARITY of F being hasEtaleLocalProperty_isRegular_fibreSpace of ChartFibreRegularity (06M1 at the structure morphism F -> Spec k, smooth by 075W because the chart is, by isSmooth_fibreStructureMorphism) in the form isRegularLocalRing_chartLocalRing consumes, and the NONEMPTINESS of F being exists_point_fibreOverFieldPoint_of_range_eq_singleton of the same file (04XH at a point of Spec k, which the singleton range of the field-valued point supplies). The GEOMETRIC POINT over the closed point of an etale chart of F is available too: every point of an etale chart is the chart point of a small etale neighbourhood of a geometric point of the space, by exists_chartGeometricPoint_chartPoint_eq of ChartSlicingGeometricPoint (03BX part (1) and exists_geometricRepresentative on the chart, pushed forward by ofChartGeometricPoint), and exists_chartGeometricPoint_isClosed_isRegularLocalRing_finiteSeparable of the same file puts the 056U closed point of a chart nonempty and smooth over Spec k, with its regular local ring and its finite separable residue field extension, at such a geometric point. The PLUMBING of the slice as a scheme of the site is proved too, in EtaleChartFamilySizeBound: a monomorphism of schemes into a chart U of the site makes its source an object of the site over U of size at most 2 ^ 2 ^ size U0 whenever size U <= size U0, which is the bound 06FX delivers (exists_siteObject_toScheme_map_eq_size_le), and with that bound uniform in the point exists_etaleChartFamily_of_forall_isFiniteTypePoint assembles the family of ExistsEtaleChartFamilyOfIsAbsolutelyDM with its site-membership conjunct, indexed by the points the substantial direction follows from the chart at ONE finite type point, by existsEtalePresentationOfIsAbsolutelyDM_of_forall_exists_chart, and nothing about the family, the index type or the coproduct is needed. Two further inputs are proved. The affine etale chart V of F through a prescribed point of |F|, with its scheme smooth over Spec k as a morphism of schemes, is exists_affine_smallEtale_smooth_chartScheme_at_point of AffineSmoothChartAtPoint, on exists_affine_etale_chart_at_point and on 03ZC part (1) read at the square against the IDENTITY chart of the representing object of Spec k (isEtaleChart_id), whose morphism of schemes is the chart's own structure morphism -- smooth_chartMap_of_isSmooth and smooth_toScheme_map_of_isSmooth_yoneda, the mirrors at smoothness of unramified_chartMap_of_isUnramified; with the 056U slicing point on it that is exists_affine_chartGeometricPoint_isClosed_isRegularLocalRing_finiteSeparable of the same file, and the space-level smoothness it consumes is isSmooth_fibreStructureMorphism read on the representing map by isSmooth_representingMap_of_isSmooth. And the shrinking of U that was to make the f_i global functions on the algebraic space U is NOT NEEDED: on a chart whose scheme is AFFINE the sequence may be chosen among the GLOBAL functions outright, the minimal generating family of exists_fn_mem_ofList_eq_maximalIdeal_of_span_eq being selectable inside any prescribed generating set and the global germs generating m_u because the stalk of an affine scheme is a localization of its global functions (span_image_preimage_germ_top_eq_maximalIdeal and exists_global_isRegular_ofList_eq_maximalIdeal_stalk_of_unramifiedAt of GlobalSlicingSequenceAffine), and a global function on the representing scheme IS a global section of the structure sheaf of the small etale site of a represented algebraic space, the identity chart being terminal there (representedUnitSection and eval_representedUnitSection of RepresentedGlobalSections, on isTerminal_idChart) -- no etale descent for O and nothing of 05B2 enters. The two together give the fibre hypothesis of 06MD and the generation the 02GF criterion reads, in exists_representedUnitSection_isRegular_etaleLocalRing_of_isAffine of FibreGlobalSlicingSequenceAffine, and that the 06FX chart is affine is recorded in the conclusion of exists_isClosed_smoothChart_size_le_of_isFiniteTypePoint. The PLUMBING of that body into existsEtalePresentationOfIsAbsolutelyDM_of_forall_exists_chart is PROVED, in exists_isRelativelyEtale_chart_size_le_of_isFiniteTypePoint of this file, from the following three inputs. The 06FX chart schemeStack U -> X is read as the 1-morphism algebraicSpaceStack (yoneda U) -> X that 06MD slices by algebraicSpaceStackChart of SchemeChartAsAlgebraicSpaceChart. The vanishing hypothesis of unramifiedAt_comp_of_ofList_eq_maximalIdeal_stalk_over_field, which asks for the chart of the slice to be identified with the zero scheme of the pulled-back functions, is supplied by definingIdealAt_vanishingSubspace_globalFunctionsMap_eq_ofList of FibreSliceChartZeroScheme, read at the chart by forall_unramifiedAt_toScheme_map_rep_snd_comp_of_eq_vanishingSubfunctor of ChartSliceUnramifiedFieldPoint and carried to the fibre hypothesis of 06N2 by exists_fibreIsUnramifiedNear_zeroLocusOnOpen_of_forall_germ_mem_maximalIdeal of SliceFibreSubspaceComparison. And the shrinking that turns the flat, locally finitely presented slice into a relatively etale chart BY A SCHEME OF THE SITE needs NEITHER an etale analogue of the relation-slice route NOR the missing direction of the open-substack correspondence: 06N2 read as exists_isOpenSubspace_isEtale_mem_range_pointsMap of EtaleChartStackPointMembership returns an open SUBSPACE of U, its point-set clause read off the singleton range of the field-valued point rather than off any bijectivity of spacePointMap, and exists_siteObject_isRelativelyEtale_chart_of_mem_range of EtaleChartOpenSubspaceSiteObject reads that subspace as a scheme of the site through a representing isomorphism. The FIBRE HYPOTHESIS of 06N2, FibreIsUnramifiedNear, is PROVED, in FibreUnramifiedNearSubstack, off the unramifiedness of the slice over Spec k at the sliced point as a morphism of schemes -- fibreIsUnramifiedNear_of_unramifiedAt. Two steps: that scheme-level statement is lifted to Space.IsUnramifiedAt of the structure morphism of the fibre read through a representing algebraic space Fsp, hence to an open subspace W of Fsp unramified over Spec k around the point (exists_isOpenSubspace_isUnramified_fibreSpace_of_unramifiedAt of FibreUnramifiedFromChart, off the chart criterion isUnramifiedAt_chartPoint_iff of UnramifiedAtChart, the mirror at unramifiedness of isFlatAt_chart_iff); and W is read as an OPEN SUBSTACK cut out by the ESSENTIAL IMAGE of S_W -> S_Fsp -> F, which is an open immersion by isOpenImmersion_algebraicSpaceStackMap_of_isOpenImmersion and isOpenImmersion_comp_of_quasiInverse, so 0506 both makes that essential image an open substack and factors the composite through it by an equivalence -- and that factorization is what carries all three of the things the clause needs. 003Z (2) upgrades it to an equivalence OVER THE SITE, so the open substack is represented by the algebraic space W (isRepresentableByAlgebraicSpace_essImage_of_isImmersion); the morphism of representing presheaves 04SW attaches to S_W -> F -> Spec k is computed outright to be W.iota followed by fibreSpaceStructureMorphism (representingMap_openSubspaceFibreMap_comp, on representingMap_associatedMap and representingMap_equivalenceOverInvMap), so the relative property of 03YK at unramifiedness holds of S_W -> Spec k by the 04XB bridge hasRelativeProperty_iff_prop_representingMap and transports to the open substack by 0457 (relativeProperty_of_equivalences_symm), the DM conjunct being 050E (3) at that representability; and the point-set membership is mem_range_pointsMap_openSubspaceFibreMap, on AlgebraicStacks.pointsMap_comp and pointsMap_eq_of_hom2. The open substack there is NOT the one exists_openSubstack_mem_pointSet_of_isOpenSubspace produces from the surjectivity half of 06FJ, which carries no representing datum. Invariance of Stack.IsUnramified under precomposition with an equivalence with NO representability hypothesis is not needed, and remains available only for a 1-morphism representable by algebraic spaces, where IsDM, IsFlat, IsSmooth and HasRelativeProperty have it outright. 056U, which gives that closed point at an affine etale chart of the algebraic space F, is formalized as dense_closedPoints_with_finite_separable_residueField_of_smooth, with its space-level form 07W4 as dense_setOf_class_finiteSeparable_of_isSmooth, which is stated over the base Spec k itself and so is not the form the assembly uses. 06MD is not missing either, in either conjunct: exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular carries the tag at the hypotheses the source states, so the slice may be cut the source's way and need not go through the relation-slice descent the 06MF chart uses; the hypothesis it consumes is the regular sequence read in the ETALE local ring of F at a geometric point, which is regular by 06M1 (isRegular_of_isSmooth_over_field). The flatness conjunct of 06MD is likewise not carried as the hypothesis ZeroLocusIsFlatOverSmoothChart of ChartSlicingRegularSequence. Stacks 06N2 is not missing: exists_openSubstack_isEtale is proved outright, the comparison of Stacks 0CIT with the relative notion of 04XB being available for a representable 1-morphism by hasSurjectiveEtaleSmoothDiagram_of_isRepresentableByAlgebraicSpaces, which needs nothing of Stacks 0CIA”.

> **Stacks 06N3.** An algebraic stack is DM exactly when it is Deligne–Mumford — equivalently,
> by **Stacks 03YO**, exactly when there is a scheme of the site carrying a representable,
> surjective, étale 1-morphism to it.
>
> Both directions are proved and nothing is assumed. The implication (2) ⟹ (1) — equivalently
> (3) ⟹ (1), these being the same condition here — is
> `AlgebraicGeometry.Stack.isAbsolutelyDM_of_isDeligneMumfordStack`, off part (1) of
> **Stacks 06MB**. The substantial direction (1) ⟹ (3) is
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM` of this file: the source's
> étale chart at one finite type point, with the size bound uniform in the point
> (`AlgebraicGeometry.Stack.exists_isRelativelyEtale_chart_size_le_of_isFiniteTypePoint`), fed to
> the family assembly
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM_of_forall_exists_chart`, which
> builds the index type, puts the coproduct in the site, and produces the surjective relatively
> étale 1-morphism out of it
> (`AlgebraicGeometry.Stack.isDeligneMumfordStack_of_forall_isRelativelyEtale`).
>
> The substantial direction, `AlgebraicGeometry.Stack.ExistsEtalePresentationOfIsAbsolutelyDM`,
> reduced to the chart construction `AlgebraicGeometry.Stack.ExistsEtaleChartFamilyOfIsAbsolutelyDM`,
> is proved and not carried as a hypothesis. The statement cannot be placed in
> `StacksFrontier.AlgebraicGeometry.Stacks.DeligneMumfordPresentationTheorem`:
> `StacksFrontier.AlgebraicGeometry.Stacks.EtaleChartFamilySizeBound`, which this file needs for the
> family assembly, imports that module, so naming
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM` there would be an import
> cycle.
>
> The attribute below records where each step of the source's argument is.

```lean
theorem isAbsolutelyDM_iff_isDeligneMumfordStack_unconditional
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.IsAbsolutelyDM B S hS hZ 𝒳 ↔
      IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val
```

**`AlgebraicGeometry.Stack.isAbsolutelyDM_iff_isDeligneMumfordStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationTheorem.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationTheorem.lean#L177). The attribute's comment: “the equivalence of (1) DM with (2) Deligne-Mumford and (3) the existence of a surjective etale presentation by a scheme; (2) and (3) are the same condition here, since Stacks 03YO defines Deligne-Mumford that way. Both implications are carried, as the hypotheses `hForward` (the structure theorem: Stacks 06MD, 06N0, 06N2, 06G2, 06G3 are absent) and `hBackward` (Stacks 06MB part (1) is present but the bridge from the Section 04XB form of an etale chart to the smooth-diagram flatness of Stacks 06PW is absent)”.

> **Stacks 06N3.** An algebraic stack is DM exactly when it is Deligne–Mumford — equivalently,
> by **Stacks 03YO**, exactly when there is a scheme of the site with a representable, surjective,
> étale 1-morphism to it.
>
> Both implications are carried; see
> `AlgebraicGeometry.Stack.ExistsEtalePresentationOfIsAbsolutelyDM` and
> `AlgebraicGeometry.Stack.IsAbsolutelyDMOfExistsEtalePresentation` for what each one stands for
> and why.

```lean
theorem isAbsolutelyDM_iff_isDeligneMumfordStack
    (hForward : ExistsEtalePresentationOfIsAbsolutelyDM.{u, w} B S hS hZ)
    (hBackward : IsAbsolutelyDMOfExistsEtalePresentation.{u, w} B S hS hZ)
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.IsAbsolutelyDM B S hS hZ 𝒳 ↔
      IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val
```

**`AlgebraicGeometry.Stack.isAbsolutelyDM_of_isDeligneMumfordStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean#L346). The attribute's comment: “the implication (2) => (1), equivalently (3) => (1), these being the same condition here: an algebraic stack admitting a surjective etale presentation by a scheme is DM”.

> A Deligne–Mumford algebraic stack is DM: the implication (2) ⟹ (1), equivalently (3) ⟹ (1),
> these being the same condition here.

```lean
theorem isAbsolutelyDM_of_isDeligneMumfordStack (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val) :
    AlgebraicStacks.IsAbsolutelyDM B S hS hZ 𝒳
```

## Tag 0CIA, a lemma

[Tag 0CIA](https://stacks.math.columbia.edu/tag/0CIA) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM_of_dm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean#L44). The attribute's comment: “part (1)”.

> **Stacks 0CIA, part (1).** Let `f : 𝒳 ⟶ 𝒴` be a DM 1-morphism of algebraic stacks. For every
> DM algebraic stack `𝒵` and 1-morphism `g : 𝒵 ⟶ 𝒴` there is a scheme with a surjective étale
> 1-morphism onto `𝒳 ×_{f, 𝒴, g} 𝒵`.

```lean
theorem isDeligneMumfordStack_twoFibreProduct_of_isDM_of_dm
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : Stack.IsDM B S hS f) (h𝒵 : IsAbsolutelyDM B S hS B.contains_terminal 𝒵) :
    Stack.IsDeligneMumfordStack.{u, w} B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean#L56). The attribute's comment: “part (2)”.

> **Stacks 0CIA, part (2).** Let `f : 𝒳 ⟶ 𝒴` be a DM 1-morphism of algebraic stacks. For every
> algebraic space `Z` and 1-morphism `g : Z ⟶ 𝒴` there is a scheme with a surjective étale
> 1-morphism onto `𝒳 ×_{f, 𝒴, g} Z`.

```lean
theorem isDeligneMumfordStack_twoFibreProduct_of_isDM_algebraicSpace
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : Stack.IsDM B S hS f)
    (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hZ : IsAlgebraicSpace B S hS Z)
    (g : Stack.algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒴) :
    Stack.IsDeligneMumfordStack.{u, w} B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean#L126). The attribute's comment: “part (1), the Deligne-Mumford condition on the 2-fibre product: the apex of the canonical square of a DM 1-morphism f and a 1-morphism out of a DM algebraic stack is itself a DM algebraic stack. This is the source's own argument for part (1) up to its closing appeal to Stacks 06N3; that appeal is made in `AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM`, which states part (1) in the source's existence form”.

> **A 2-fibre product of a Deligne–Mumford 1-morphism over a Deligne–Mumford algebraic stack
> is Deligne–Mumford.** The projection of the canonical square of `(f, g)` to `𝒵` is a base change
> of `f`, so it is Deligne–Mumford by Stacks 050F, and a stack Deligne–Mumford over a
> Deligne–Mumford stack is Deligne–Mumford by Stacks 050L.
>
> This is the first half of the argument for part (1) of Stacks 0CIA; the half left is the
> structure theorem Stacks 06N3, which turns the conclusion into a surjective étale presentation
> of the apex by a scheme and is applied in
> `AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM`.

```lean
theorem isAbsolutelyDM_twoFibreProduct_of_isDM
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : Stack.IsDM B S hS f) (h𝒵 : IsAbsolutelyDM B S hS hT 𝒵) :
    IsAbsolutelyDM B S hS hT (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_algebraicSpaceStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean#L148). The attribute's comment: “part (2), the Deligne-Mumford condition on the 2-fibre product: the apex of the canonical square of a DM 1-morphism f and a 1-morphism out of an algebraic space is a DM algebraic stack, with no hypothesis on the algebraic space. This is the source's own reduction of part (2) to part (1), up to the closing appeal to Stacks 06N3; that appeal is made in `AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_algebraicSpace`, which states part (2) in the source's existence form”.

> **A 2-fibre product of a Deligne–Mumford 1-morphism over an algebraic space is
> Deligne–Mumford.** The source's reduction of part (2) of Stacks 0CIA to part (1): an algebraic
> space is Deligne–Mumford when read as an algebraic stack, so no hypothesis beyond
> Deligne–Mumfordness of `f` is needed.
>
> As for `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_of_isDM`, what is
> left of Stacks 0CIA after this is one application of Stacks 06N3, made in
> `AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_algebraicSpace`.

```lean
theorem isAbsolutelyDM_twoFibreProduct_algebraicSpaceStack
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : Stack.IsDM B S hS f)
    (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hZ : IsAlgebraicSpace B S hS Z)
    (g : Stack.algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒴) :
    IsAbsolutelyDM B S hS hT (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean#L170). The attribute's comment: “part (1), in the source's existence form: a scheme with a surjective etale 1-morphism onto the 2-fibre product, with the substantial direction of Stacks 06N3 as the explicit hypothesis hForward (the structure theorem behind it, Stacks 06MD, 06N0, 06N2, 06G2, 06G3, is absent from the library). The Deligne-Mumford condition on the apex, which is the whole of the source's argument apart from that appeal, is proved unconditionally in `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_of_isDM`”.

> **Stacks 0CIA, part (1).** Let `f : 𝒳 ⟶ 𝒴` be a Deligne–Mumford 1-morphism of algebraic
> stacks. For every Deligne–Mumford algebraic stack `𝒵` over `𝒴` there is a scheme of the site
> with a surjective étale 1-morphism onto `𝒳 ×_{f, 𝒴, g} 𝒵`.
>
> The apex is a Deligne–Mumford algebraic stack by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_of_isDM`, and the
> presentation comes from the structure theorem Stacks 06N3, carried here as the hypothesis
> `hForward`.

```lean
theorem isDeligneMumfordStack_twoFibreProduct_of_isDM
    (hForward : Stack.ExistsEtalePresentationOfIsAbsolutelyDM.{u, w} B S hS hT)
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : Stack.IsDM B S hS f) (h𝒵 : IsAbsolutelyDM B S hS hT 𝒵) :
    Stack.IsDeligneMumfordStack.{u, w} B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSpecialPresentation.lean#L191). The attribute's comment: “part (2), in the source's existence form: a scheme with a surjective etale 1-morphism onto the 2-fibre product with an algebraic space, with the substantial direction of Stacks 06N3 as the explicit hypothesis hForward (the structure theorem behind it, Stacks 06MD, 06N0, 06N2, 06G2, 06G3, is absent from the library). The Deligne-Mumford condition on the apex is proved unconditionally in `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_twoFibreProduct_algebraicSpaceStack`”.

> **Stacks 0CIA, part (2).** Let `f : 𝒳 ⟶ 𝒴` be a Deligne–Mumford 1-morphism of algebraic
> stacks. For every algebraic space `Z` over `𝒴` there is a scheme of the site with a surjective
> étale 1-morphism onto `𝒳 ×_{f, 𝒴, g} Z`, with no further hypothesis on `Z`.
>
> This is part (1) applied to the algebraic space read as an algebraic stack, which is
> Deligne–Mumford by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isAbsolutelyDM_algebraicSpaceStack`.

```lean
theorem isDeligneMumfordStack_twoFibreProduct_algebraicSpace
    (hForward : Stack.ExistsEtalePresentationOfIsAbsolutelyDM.{u, w} B S hS hT)
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : Stack.IsDM B S hS f)
    (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hZ : IsAlgebraicSpace B S hS Z)
    (g : Stack.algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒴) :
    Stack.IsDeligneMumfordStack.{u, w} B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).pt.val.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.21, Tag 06MC](https://stacks.math.columbia.edu/tag/06MC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
