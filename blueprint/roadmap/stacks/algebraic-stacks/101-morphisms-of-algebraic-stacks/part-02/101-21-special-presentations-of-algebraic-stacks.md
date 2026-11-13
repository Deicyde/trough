---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular, AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero, AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation_unconditional, AlgebraicGeometry.Stack.hasSurjectiveEtaleFieldSpectrumCover_unconditional, AlgebraicGeometry.Stack.exists_isOpenSubspace_isEtale, AlgebraicGeometry.Stack.exists_openSubstack_isEtale_unconditional, AlgebraicGeometry.Stack.isAbsolutelyDM_iff_isDeligneMumfordStack_unconditional
statement: formalized
proof: formalized
---

# 101.21 Special presentations of algebraic stacks

Section 101.21 of the Stacks Project, [Tag 06MC](https://stacks.math.columbia.edu/tag/06MC). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06MD, a lemma

[Tag 06MD](https://stacks.math.columbia.edu/tag/06MD) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_zeroLocus_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFlatness.lean, line 769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChartSlicingFlatness.lean#L769). The attribute's comment: “the full statement: an open V ∋ p(z) with V(f₁,…,f\_r) ∩ V ⟶ 𝒳 flat and locally of finite presentation”.

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

**`AlgebraicGeometry.Stack.exists_openSubstack_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean#L430). The attribute's comment: “the source's own hypotheses, with the conclusion read on an open substack of the stack of the algebraic space: the 1-morphism is locally of finite type and the given point z of the fibre has dim\_z(F) = 0, the dimension of Stacks 04N5 of a representing algebraic space Fsp of the fibre at z. Nothing is added and nothing is weakened. The proof is exists\_openSubstack\_isLocallyQuasiFinite\_unconditional of ChartShrinkingQuasiFiniteEtaleUnconditional -- which states the same conclusion at the intermediate condition the source's own proof extracts from dim\_z(F) = 0, that some open substack of the fibre containing z is locally quasi-finite over Spec k -- composed with the step the source's proof takes from dim\_z(F) = 0 to that condition by Stacks 04NV, which is fibreIsLocallyQuasiFiniteNear\_of\_dimensionAtPoint\_eq\_zero above. The source's open subspace of the algebraic space is rendered here as an open substack of the stack of that space, with the same point set, both directions of that passage being proved as exists\_openSubstack\_algebraicSpaceStack\_of\_isOpenImmersion and exists\_isOpenSubspace\_property\_eq\_essImage; the conclusion read on an open subspace, as the source reads it, is exists\_isOpenSubspace\_isLocallyQuasiFinite\_of\_dimensionAtPoint\_eq\_zero below. The point of the fibre is the image of z under the comparison spacePointMap of the representing equivalence, which bijective\_spacePointMap\_representing makes a bijection, so no point of the fibre is excluded by stating the hypothesis on Fsp”.

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

**`AlgebraicGeometry.Stack.exists_isOpenSubspace_isLocallyQuasiFinite_of_dimensionAtPoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FibreQuasiFiniteNearSubstack.lean#L472). The attribute's comment: “the statement of the source, hypotheses and conclusion: the 1-morphism out of the algebraic space is locally of finite type, the given point z of the fibre has dim\_z(F) = 0 -- the dimension of Stacks 04N5 of a representing algebraic space Fsp of the fibre at z -- and after replacing the algebraic space by an open subspace of Stacks 02YU, part (2), containing the image of z, the 1-morphism is locally quasi-finite, the replacement read as the composite of the 1-morphism of Stacks 0458 induced by that open subspace. Nothing is added and nothing is weakened. The proof is exists\_isOpenSubspace\_isLocallyQuasiFinite of ChartShrinkingOpenSubspace -- the same conclusion at the intermediate condition the source's own proof extracts from dim\_z(F) = 0 -- composed with the step the source's proof takes from dim\_z(F) = 0 to that condition by Stacks 04NV, which is fibreIsLocallyQuasiFiniteNear\_of\_dimensionAtPoint\_eq\_zero above. The point of the fibre is the image of z under the comparison spacePointMap of the representing equivalence, which bijective\_spacePointMap\_representing makes a bijection, so no point of the fibre is excluded by stating the hypothesis on Fsp”.

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

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_iff_hasQuasiDMPresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordPresentationUnconditional.lean#L489). The attribute's comment: “the equivalence of (1) quasi-DM with (2) the existence of a scheme W of the site and a surjective, flat, locally finitely presented, locally quasi-finite 1-morphism from W; both implications are proved. (2) implies (1) is Stacks 06MB part (2); (1) implies (2) builds a flat, locally finitely presented, locally quasi-finite chart at each finite type point and takes the coproduct of these charts, which is surjective by Stacks 06G2. Quasi-DM is the absolute notion of Stacks 050D, so the site contains the terminal scheme (hZ)”.

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

**`AlgebraicGeometry.Stack.hasSurjectiveEtaleFieldSpectrumCover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCoverUnconditional.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordSingletonEtaleCoverUnconditional.lean#L163). The attribute's comment: “a DM, locally Noetherian, reduced algebraic stack with a singleton point space admits a surjective etale 1-morphism from the spectrum of a field. The field-valued point comes in two steps: Stacks 06MP (1) => (2) supplies a surjective, flat, locally finitely presented xi : Spec k -> Z, and the groupoid (U, R, s, t, c) of that flat presentation, with U = Spec k and R = U x\_Z U, is divided by the open and closed subgroupoid P through the identity, whose quotient U\_bar = Spec k\_0 is the spectrum of the field of invariants. The division is exists\_division\_identityArrowOpens\_etale\_pointGroupoid, on the four conclusions of Stacks 04S4 in exists\_division; it is run at the de-realization of the self-intersection groupoid, whose object and arrow spaces are representable by isRepresentable\_objects\_pointGroupoid\_fieldSpectrum and isRepresentable\_arrows\_pointGroupoid\_fieldSpectrum, the latter being condition (2) of Stacks 06LZ read on the base site at the dimension bound dimension\_relation\_le\_zero\_fieldSpectrum, i.e. Stacks 06FF against quasi-DM-ness through Stacks 050H part (5). Etaleness of U\_bar -> Z follows the source's steps 6 and 8 rather than its Stacks 04XD reading: the divided groupoid is the restriction of the descended groupoid (U\_bar, R\_bar, s\_bar, t\_bar, c\_bar) along the finite locally free surjection U -> U\_bar, so [U/R] -> [U\_bar/R\_bar] is an equivalence by Stacks 046T (nonempty\_isEquivalenceOver\_quotientStackMap\_realizationHom, whose clause (1) is full faithfulness of the evaluations of the descent morphism and whose clause (2) is that its map on objects is an fppf covering), [U/R] -> Z is an equivalence by Stacks 04WY (nonempty\_isEquivalenceOver\_canonicalMap), and s\_bar is etale by Division.etale\_descended\_source, which is Stacks 047W at unramifiedness through etale\_source\_of\_flat\_of\_isOpenImmersion\_identity rather than the computation of Omega\_\{R\_bar/U\_bar} that Stacks 04R9 gives the source. Stacks 04M9 then makes the projection S\_\{U\_bar} -> [U\_bar/R\_bar] of Stacks 044R etale (isRelativelyEtale\_quotientStackProjection\_realization), and two instances of Stacks 0457 move that verdict across the equivalence with Z and down the universe lift of the source, giving quotientProjectionSchemeStackMap, which is etale in the sense of Stacks 0CIL by isEtale\_of\_isRelativelyEtale. DM-ness enters at the division, in the absolute form of Stacks 050D part (5), turned into DM-ness over S by Stacks 050N part (1)”.

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

**`AlgebraicGeometry.Stack.exists_isOpenSubspace_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingOpenSubspace.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingOpenSubspace.lean#L358). The attribute's comment: “the conclusion read on an open subspace of the algebraic space, as the source reads it: the composite of the 1-morphism of Stacks 0458 induced by an open subspace containing the image of the given point of the fibre with the given 1-morphism is etale. Nothing is added to exists\_openSubstack\_isEtale\_unconditional: its open substack is carried to an open subspace with the same point set by exists\_isOpenSubspace\_property\_eq\_essImage, and the etaleness is carried across the Stacks 0506 factorization of that subspace's 1-morphism through the substack's inclusion by isEtale\_comp\_of\_eq\_essImage”.

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

**`AlgebraicGeometry.Stack.exists_openSubstack_isEtale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtaleUnconditional.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChartShrinkingQuasiFiniteEtaleUnconditional.lean#L228). The attribute's comment: “after replacing the algebraic space by an open subspace containing the image of the given point of the fibre, a flat, locally finitely presented 1-morphism whose fibre over a field-valued point is unramified at that point is etale. Nothing is carried: the open substack is the locus W(P, f) of assertion (A) of Stacks 06M3 at P = unramified -- the entry of the list of Stacks 06M5 whose base-change clause holds for an arbitrary base change, which is why it and not the etale entry applies to a base change along a field-valued point -- produced by exists\_isRelativePropertyLocus\_of\_hasRelativePropertyLocusOnSpaces from the entry-(3) instances of LocalSourceLemmaUnramified, and the conclusion that the image of the given point of the fibre lies in it is the maximality half of assertion (B) at the open substack the fibre hypothesis supplies. The comparison of the two renderings of unramifiedness, Stacks 0CIT against the relative notion of Stacks 04XB, is available in both directions for a 1-morphism representable by algebraic spaces, by hasSurjectiveEtaleSmoothDiagram\_of\_isRepresentableByAlgebraicSpaces, and needs nothing of Stacks 0CIA. Stacks 06LU for 1-morphisms of algebraic stacks is not carried but proved, and it is what turns the locus into the etaleness of the conclusion”.

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
> and not from **Stacks 0CIA**.
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

**`AlgebraicGeometry.Stack.isAbsolutelyDM_iff_isDeligneMumfordStack_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AbsolutelyDMEtaleChartAssembly.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AbsolutelyDMEtaleChartAssembly.lean#L512). The attribute's comment: “the equivalence of (1) DM, (2) Deligne-Mumford and (3) the existence of a surjective etale morphism from a scheme, (2) and (3) being the same condition by the definition 03YO; (2) => (1) is isAbsolutelyDM\_of\_isDeligneMumfordStack (06MB part (1)) and (1) => (3) is existsEtalePresentationOfIsAbsolutelyDM, the etale chart at each finite type point followed by the disjoint union of the charts”.

> **Stacks 06N3.** Let `𝒳` be an algebraic stack. The following are equivalent: (1) `𝒳` is DM,
> (2) `𝒳` is Deligne–Mumford, and (3) there is a scheme `W` with a surjective étale 1-morphism
> `W ⟶ 𝒳`.
>
> As in the source, (3) is the definition of (2) (**Stacks 03YO**,
> `AlgebraicGeometry.Stack.IsDeligneMumfordStack`: a scheme of the site carrying a 1-morphism to
> `𝒳` that is representable by algebraic spaces, surjective and étale), so the three conditions
> are the single equivalence below. Condition (1) is the absolute DM property of **Stacks 050D**,
> part (5), which is DM over `Spec ℤ`; the argument `hZ` records that the site contains the
> terminal scheme, which is what that definition is stated at, and it always holds
> (`AlgebraicGeometry.BigFppfSite.contains_terminal`).
>
> The implication (2) ⟹ (1) is `AlgebraicGeometry.Stack.isAbsolutelyDM_of_isDeligneMumfordStack`,
> off part (1) of **Stacks 06MB**. The implication (1) ⟹ (3) is
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM` of this file: the source's
> étale chart at each finite type point, with a size bound uniform in the point
> (`AlgebraicGeometry.Stack.exists_isRelativelyEtale_chart_size_le_of_isFiniteTypePoint`), and
> the disjoint union of these charts
> (`AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM_of_forall_exists_chart`).

```lean
theorem isAbsolutelyDM_iff_isDeligneMumfordStack_unconditional
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.IsAbsolutelyDM B S hS hZ 𝒳 ↔
      IsDeligneMumfordStack.{u, w} B S hS 𝒳.val.val
```

## Tag 0CIA, a lemma

[Tag 0CIA](https://stacks.math.columbia.edu/tag/0CIA) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM_of_dm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean#L46). The attribute's comment: “part (1), unconditional: the apex is DM by Stacks 050F and 050L (isAbsolutelyDM\_twoFibreProduct\_of\_isDM) and the presentation comes from the proved substantial direction of Stacks 06N3, existsEtalePresentationOfIsAbsolutelyDM”.

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

**`AlgebraicGeometry.Stack.AlgebraicStacks.isDeligneMumfordStack_twoFibreProduct_of_isDM_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordFibreProductPresentation.lean#L59). The attribute's comment: “part (2), unconditional and with no hypothesis on the algebraic space Z: Z read as an algebraic stack is DM (isAbsolutelyDM\_algebraicSpaceStack), so part (1) applies”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.21, Tag 06MC](https://stacks.math.columbia.edu/tag/06MC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
