---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.strictTransformSheaf, AlgebraicGeometry.Space.strictTransform, AlgebraicGeometry.Space.isEtale_baseChange_blowup_of_isEtale, AlgebraicGeometry.Space.exists_isEtale_strictTransformSheaf_restriction, AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_of_isBlowupAlong, AlgebraicGeometry.Space.exists_strictTransform_eq_preimage, AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_strictTransformSheaf_iso, AlgebraicGeometry.Space.isBlowupAlong_strictTransform
statement: formalized
proof: formalized
---

# 71.18 Strict transform

Section 71.18 of the Stacks Project, [Tag 0861](https://stacks.math.columbia.edu/tag/0861). 10 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0862, a definition

[Tag 0862](https://stacks.math.columbia.edu/tag/0862) in the Stacks Project.

**`AlgebraicGeometry.Space.strictTransformSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransform.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransform.lean#L252). The attribute's comment: “strict transform of a module”.

> **Stacks 0862, part (1).** The strict transform of an `𝒪_X`-module `F` along a morphism
> `b : A' ⟶ A` relative to a subspace `E ⊆ A'`: pull `F` back to `X ×_A A'` along `pr_X` and divide
> out the submodule of those sections that are supported on `|pr_{A'}^{-1}E|`.
>
> Stated for an arbitrary morphism `b` together with an arbitrary subspace `E` of its source, this
> specializes to the strict transform with respect to the blowup of `A` in a closed subspace
> `Z ⊆ A` on taking `b` that blowup and `E = b^{-1}Z` its exceptional divisor.  Stacks 0862 states
> the construction for a quasi-coherent `F`, which is the case it is applied in; the construction
> itself uses nothing of `F`, so no quasi-coherence hypothesis is carried here.
>
> Quasi-coherence of the strict transform is *not* asserted: it would need the preamble of the
> section containing Stacks 0862 — that `E` is an effective Cartier divisor, that its preimage is
> locally principal, and that the complement of the latter has an affine inclusion — none of which
> is available for algebraic spaces, together with quasi-coherence of a cokernel on the small étale
> site.  See the module documentation.

```lean
noncomputable def strictTransformSheaf (E : Subfunctor A'.1)
    (F : Modules.{u, u} B S hS X.1 X.2) :
    Modules.{u, u} B S hS (strictTransformPullback B S hS f b).1
      (strictTransformPullback B S hS f b).2
```

**`AlgebraicGeometry.Space.strictTransform`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransform.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransform.lean#L316). The attribute's comment: “strict transform of a space”.

> **Stacks 0862, part (2).** The strict transform of an algebraic space `f : X ⟶ A` over `A`
> along a morphism `b : A' ⟶ A` relative to a subspace `E ⊆ A'`: the closed subspace of `X ×_A A'`
> determined by the ideal of those sections of `𝒪_{X ×_A A'}` that are supported on
> `|pr_{A'}^{-1}E|`.
>
> Stated for an arbitrary morphism `b` together with an arbitrary subspace `E` of its source, this
> specializes to the strict transform with respect to the blowup of `A` in a closed subspace
> `Z ⊆ A` on taking `b` that blowup and `E = b^{-1}Z` its exceptional divisor.
>
> The closed subspace is realized as the infimum of those closed subspaces whose defining ideal is
> dominated by that ideal of supported sections, which is a closed subspace unconditionally, and
> which coincides with the closed subspace cut out by the ideal whenever the latter exists, by
> `AlgebraicGeometry.Space.strictTransformSubfunctor_eq_of_definingIdealSheaf_eq`.
>
> Quasi-coherence of the defining ideal is *not* asserted: it would need the preamble of the
> section containing Stacks 0862 — that `E` is an effective Cartier divisor, that its preimage is
> locally principal, and that the complement of the latter has an affine inclusion — none of which
> is available for algebraic spaces.  See the module documentation.

```lean
noncomputable def strictTransform (E : Subfunctor A'.1) :
    ClosedSubspaces B S hS (strictTransformPullback B S hS f b).1
```

## Tag 0863, a lemma

[Tag 0863](https://stacks.math.columbia.edu/tag/0863) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_baseChange_blowup_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupEtaleLocalization.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupEtaleLocalization.lean#L160). The attribute's comment: “part (1): the blowup localizes étale-locally, and the induced morphisms are étale”.

> **Stacks 0863, part (1).** Let `Z ⊆ 𝔅` be a closed subspace of an algebraic space over `S`,
> let `b : 𝔅' ⟶ 𝔅` be the blowup of `𝔅` in `Z` and let `f : X ⟶ 𝔅` be an algebraic space over
> `𝔅`.  Let
>
> ```
> U ⟶ X
> ↓     ↓
> 𝒱 ⟶ 𝔅
> ```
>
> be a commutative square with étale horizontal arrows, and let `v' : 𝒱' ⟶ 𝒱` be the blowup of
> `𝒱` in the inverse image `Z ×_𝔅 𝒱` of `Z`.  Then:
>
> * `𝒱' = 𝒱 ×_𝔅 𝔅'`, by a cartesian square over `v` and `b`;
> * the resulting morphism `m : 𝒱' ⟶ 𝔅'` is étale;
> * the induced morphism `U ×_𝒱 𝒱' ⟶ X ×_𝔅 𝔅'` is étale.
>
> The first assertion is Stacks 085S applied to `v`, which is flat because it is étale.  The
> second is the base change of an étale morphism along `b`.  For the third,
> `U ×_𝒱 𝒱' = (X ×_𝔅 𝔅') ×_X U`, so the morphism is a base change of the étale morphism
> `u : U ⟶ X`.

```lean
theorem isEtale_baseChange_blowup_of_isEtale
    {𝔅 X 𝒱 U B' V' W W' : AlgebraicSpaces B S hS}
    {Z : ClosedSubspaces B S hS 𝔅.1} {b : B' ⟶ 𝔅} (hb : IsBlowupAlong B S hS Z b)
    {f : X ⟶ 𝔅} {v : 𝒱 ⟶ 𝔅} (hv : IsEtale B S hS v.hom)
    {u : U ⟶ X} (hu : IsEtale B S hS u.hom) {w : U ⟶ 𝒱} (hcomm : u ≫ f = w ≫ v)
    {v' : V' ⟶ 𝒱} (hv' : IsBlowupAlong B S hS (preimageClosedSubspace v Z) v')
    {pX : W ⟶ X} {pB' : W ⟶ B'} (sq : IsPullback pX pB' f b)
    {qU : W' ⟶ U} {qV' : W' ⟶ V'} (sq' : IsPullback qU qV' w v') :
    ∃ m : V' ⟶ B', IsPullback v' m v b ∧ IsEtale B S hS m.hom ∧
      ∃ can : W' ⟶ W, can ≫ pX = qU ≫ u ∧ can ≫ pB' = qV' ≫ m ∧
        IsEtale B S hS can.hom
```

**`AlgebraicGeometry.Space.exists_isEtale_strictTransformSheaf_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupEtaleLocalization.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupEtaleLocalization.lean#L241). The attribute's comment: “part (3): the strict transform of a module restricts to the strict transform of its restriction; stated for an arbitrary module, the source's quasi-coherence being unused”.

> **Stacks 0863, part (3).** In the situation of part (1), let `F` be an `𝒪_X`-module.  Then
> there are `m : 𝒱' ⟶ 𝔅'` presenting `𝒱' = 𝒱 ×_𝔅 𝔅'` and a morphism
> `can : U ×_𝒱 𝒱' ⟶ X ×_𝔅 𝔅'` over `u : U ⟶ X` and over `m`, and `can` is étale and pulls the
> strict transform of `F` relative to the blowup `b : 𝔅' ⟶ 𝔅` of `𝔅` in `Z` back to the strict
> transform of `F|_U` relative to the blowup `v' : 𝒱' ⟶ 𝒱` of `𝒱` in `Z ×_𝔅 𝒱`.
>
> The two commutations `can ≫ pr_X = pr_U ≫ u` and `can ≫ pr_{𝔅'} = pr_{𝒱'} ≫ m` say that `can`
> is *the* canonical morphism of the tag, the universal property of `X ×_𝔅 𝔅'` determining it
> from them; so pulling back along it is the restriction to `U ×_𝒱 𝒱'` that the tag speaks of.
>
> Here the strict transform is the one of Stacks 0862,
> `AlgebraicGeometry.Space.strictTransformSheaf`, taken with respect to the blowup together with
> its exceptional divisor `b^{-1}Z`, respectively `v'^{-1}(v^{-1}Z)`; the fibre products are the
> ones of `AlgebraicGeometry.AlgebraicSpaces.fiberProduct`, and `F|_U` is the pullback `u^*F` of
> Stacks 03LU, which for the étale `u` is restriction of sections by Stacks 03LW.
>
> `m`, `can` and their properties come from part (1),
> `AlgebraicGeometry.Space.isEtale_baseChange_blowup_of_isEtale`, applied to the two canonical
> cartesian squares; the identification of the strict transforms is
> `AlgebraicGeometry.Space.strictTransformSheafEtaleRestrictionIso`, whose hypothesis on the
> exceptional divisors is `AlgebraicGeometry.Space.range_pointsMap_preimage_exceptional`.
>
> No quasi-coherence of `F` is assumed: the source assumes it because that is the case the tag is
> applied in, and neither the construction of the strict transform nor this comparison uses it.

```lean
theorem exists_isEtale_strictTransformSheaf_restriction
    {𝔅 X 𝒱 U B' V' : AlgebraicSpaces B S hS}
    {Z : ClosedSubspaces B S hS 𝔅.1} {b : B' ⟶ 𝔅} (hb : IsBlowupAlong B S hS Z b)
    {f : X ⟶ 𝔅} {v : 𝒱 ⟶ 𝔅} (hv : IsEtale B S hS v.hom)
    {u : U ⟶ X} (hu : IsEtale B S hS u.hom) {w : U ⟶ 𝒱} (hcomm : u ≫ f = w ≫ v)
    {v' : V' ⟶ 𝒱} (hv' : IsBlowupAlong B S hS (preimageClosedSubspace v Z) v')
    (F : Modules.{u, u} B S hS X.1 X.2) :
    ∃ (m : V' ⟶ B') (can : strictTransformPullback B S hS w v' ⟶
        strictTransformPullback B S hS f b),
      IsPullback v' m v b ∧ IsEtale B S hS can.hom ∧
        can ≫ strictTransformPullbackToSource B S hS f b =
          strictTransformPullbackToSource B S hS w v' ≫ u ∧
        can ≫ strictTransformPullbackToBlowUp B S hS f b =
          strictTransformPullbackToBlowUp B S hS w v' ≫ m ∧
        Nonempty ((modulePullback B S hS can).obj
            (strictTransformSheaf B S hS f b (preimageClosedSubspace b Z).1 F) ≅
          strictTransformSheaf B S hS w v'
            (preimageClosedSubspace v' (preimageClosedSubspace v Z)).1
            ((modulePullback B S hS u).obj F))
```

**`AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_of_isBlowupAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtale.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtale.lean#L359). The attribute's comment: “part (2), for the blowups of 085Q themselves: the strict transform of an étale chart U is the base change along u of the strict transform of X”.

> **Stacks 0863, part (2).** Let `Z ⊆ 𝔅` be a closed subspace of an algebraic space over `S`,
> let `b : 𝔅' ⟶ 𝔅` be the blowup of `𝔅` in `Z`, let `f : X ⟶ 𝔅` be an algebraic space over `𝔅`,
> let
>
> ```
> U ⟶ X
> ↓     ↓
> 𝒱 ⟶ 𝔅
> ```
>
> be a commutative square with étale horizontal arrows and let `v' : 𝒱' ⟶ 𝒱` be the blowup of
> `𝒱` in the inverse image `Z ×_𝔅 𝒱`.  Then the strict transform `U'` of `U` with respect to `v'`
> is `X' ×_X U`, where `X'` is the strict transform of `X` with respect to `b`.
>
> Precisely: there are `m : 𝒱' ⟶ 𝔅'` presenting `𝒱' = 𝒱 ×_𝔅 𝔅'` and an étale
> `can : U ×_𝒱 𝒱' ⟶ X ×_𝔅 𝔅'` over `u` and over `m`, sitting in a cartesian square that presents
> `U ×_𝒱 𝒱' = (X ×_𝔅 𝔅') ×_X U`, and `U'` is the inverse image of `X'` along `can` — which under
> that presentation is the base change of `X'` along `u`.
>
> **No hypothesis beyond the source's is carried, and in particular being a blowup is not
> assumed.**  The two blowups are the ones Tag 085Q constructs,
> `AlgebraicGeometry.Space.blowUpAlongHom'` for `𝔅` in `Z` and for `𝒱` in `Z ×_𝔅 𝒱`; that each
> of them *is* the blowup, in the sense of the universal property of Stacks 085U, is
> `AlgebraicGeometry.Space.isBlowupAlong_blowUpAlongHom'`.  The arguments `P`, `P'` and the six
> `B.Contains` side conditions are the construction data Tag 085Q itself takes — an étale
> presentation of the space being blown up and the set-theoretic conditions on the three relative
> `Proj`s that `AlgebraicGeometry.Space.relativeProjChartOfSituation` asks for — and nothing is
> assumed about `Z` beyond being a closed subspace.
>
> The two halves of the argument are as in
> `AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_of_isEtale`: the étale comparison
> of the ideals of supported sections, and that the strict transform of `X` is honestly cut out
> by that ideal, which comes from the exceptional divisor `b^{-1}Z` being an effective Cartier
> divisor — one half of the universal property of Stacks 085U.

```lean
theorem exists_strictTransform_eq_preimage_of_isBlowupAlong
    {Z : ClosedSubspaces B S hS Bl.obj} (P : Presentation B S hS Bl.obj Bl.property)
    (hcU : B.Contains (reesChartSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    {f : X ⟶ Bl} {v : Vv ⟶ Bl} (hv : IsEtale B S hS v.hom)
    {u : U ⟶ X} (hu : IsEtale B S hS u.hom) {w : U ⟶ Vv} (hcomm : u ≫ f = w ≫ v)
    (P' : Presentation B S hS Vv.obj Vv.property)
    (hcU' : B.Contains (reesChartSituation (centreIdeal (preimageClosedSubspace v Z))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace v Z)) P').relativeProj)
    (hcR' : B.Contains (reesRelationSituation (centreIdeal (preimageClosedSubspace v Z))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace v Z)) P').relativeProj)
    (hcRR' : B.Contains (reesDoubleSituation (centreIdeal (preimageClosedSubspace v Z))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace v Z)) P').relativeProj) :
    ∃ (m : blowUpAlong' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR' ⟶
        blowUpAlong' Z P hcU hcR hcRR)
      (can : strictTransformPullback B S hS w
          (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR') ⟶
        strictTransformPullback B S hS f (blowUpAlongHom' Z P hcU hcR hcRR)),
      IsPullback (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR') m v
          (blowUpAlongHom' Z P hcU hcR hcRR) ∧
        IsEtale B S hS can.hom ∧
        can ≫ strictTransformPullbackToSource B S hS f (blowUpAlongHom' Z P hcU hcR hcRR) =
          strictTransformPullbackToSource B S hS w
            (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR') ≫ u ∧
        can ≫ strictTransformPullbackToBlowUp B S hS f (blowUpAlongHom' Z P hcU hcR hcRR) =
          strictTransformPullbackToBlowUp B S hS w
            (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR') ≫ m ∧
        IsPullback can
          (strictTransformPullbackToSource B S hS w
            (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR'))
          (strictTransformPullbackToSource B S hS f (blowUpAlongHom' Z P hcU hcR hcRR)) u ∧
        strictTransformSubfunctor B S hS w
            (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR')
            (preimageClosedSubspace
              (blowUpAlongHom' (preimageClosedSubspace v Z) P' hcU' hcR' hcRR')
              (preimageClosedSubspace v Z)).1 =
          (strictTransformSubfunctor B S hS f (blowUpAlongHom' Z P hcU hcR hcRR)
            (preimageClosedSubspace (blowUpAlongHom' Z P hcU hcR hcRR) Z).1).preimage
            can.hom
```

**`AlgebraicGeometry.Space.exists_strictTransform_eq_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtaleUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtaleUnconditional.lean#L122). The attribute's comment: “part (2): the strict transform of an étale chart U is the base change along u of the strict transform of X, for an arbitrary blowup and with no assumed inputs”.

> **Stacks 0863, part (2).** Let `Z ⊆ 𝔅` be a closed subspace of an algebraic space over `S`,
> let `b : 𝔅' ⟶ 𝔅` be the blowup of `𝔅` in `Z`, let `f : X ⟶ 𝔅` be an algebraic space over `𝔅`,
> let
>
> ```
> U ⟶ X
> ↓     ↓
> 𝒱 ⟶ 𝔅
> ```
>
> be a commutative square with étale horizontal arrows and let `v' : 𝒱' ⟶ 𝒱` be the blowup of
> `𝒱` in the inverse image `Z ×_𝔅 𝒱`.  Then the strict transform `U'` of `U` with respect to `v'`
> is `X' ×_X U`, where `X'` is the strict transform of `X` with respect to `b`.
>
> Precisely: there are `m : 𝒱' ⟶ 𝔅'` presenting `𝒱' = 𝒱 ×_𝔅 𝔅'` and an étale
> `can : U ×_𝒱 𝒱' ⟶ X ×_𝔅 𝔅'` over `u` and over `m`, sitting in a cartesian square that presents
> `U ×_𝒱 𝒱' = (X ×_𝔅 𝔅') ×_X U`, and `U'` is the inverse image of `X'` along `can` — which under
> that presentation is the base change of `X'` along `u`.
>
> **No hypothesis beyond the source's is carried.**  The existence of a closed subspace cut out by
> the ideal of sections supported on the exceptional preimage, which is all that
> `AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_of_isEtale` asks for beyond the
> étale comparison of those ideals, comes from the exceptional divisor `b^{-1}Z` being an
> effective Cartier divisor on `𝔅'`; and that is one half of the universal property of Stacks
> 085U, so `hb` supplies it.

```lean
theorem exists_strictTransform_eq_preimage
    {Z : ClosedSubspaces B S hS Bl.1} {b : B' ⟶ Bl} (hb : IsBlowupAlong B S hS Z b)
    {f : X ⟶ Bl} {v : Vv ⟶ Bl} (hv : IsEtale B S hS v.hom)
    {u : U ⟶ X} (hu : IsEtale B S hS u.hom) {w : U ⟶ Vv} (hcomm : u ≫ f = w ≫ v)
    {v' : V' ⟶ Vv} (hv' : IsBlowupAlong B S hS (preimageClosedSubspace v Z) v') :
    ∃ (m : V' ⟶ B') (can : strictTransformPullback B S hS w v' ⟶
        strictTransformPullback B S hS f b),
      IsPullback v' m v b ∧ IsEtale B S hS can.hom ∧
        can ≫ strictTransformPullbackToSource B S hS f b =
          strictTransformPullbackToSource B S hS w v' ≫ u ∧
        can ≫ strictTransformPullbackToBlowUp B S hS f b =
          strictTransformPullbackToBlowUp B S hS w v' ≫ m ∧
        IsPullback can (strictTransformPullbackToSource B S hS w v')
          (strictTransformPullbackToSource B S hS f b) u ∧
        strictTransformSubfunctor B S hS w v'
            (preimageClosedSubspace v' (preimageClosedSubspace v Z)).1 =
          (strictTransformSubfunctor B S hS f b
            (preimageClosedSubspace b Z).1).preimage can.hom
```

**`AlgebraicGeometry.Space.exists_strictTransform_eq_preimage_strictTransformSheaf_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtaleUnconditional.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupStrictTransformSpaceEtaleUnconditional.lean#L163). The attribute's comment: “parts (2) and (3) for one and the same comparison morphism, for an arbitrary blowup and with no assumed inputs”.

> **Stacks 0863, parts (2) and (3).** In the situation of part (1) there are `m : 𝒱' ⟶ 𝔅'`
> presenting `𝒱' = 𝒱 ×_𝔅 𝔅'` and an étale `can : U ×_𝒱 𝒱' ⟶ X ×_𝔅 𝔅'` over `u` and over `m`,
> sitting in a cartesian square that presents `U ×_𝒱 𝒱' = (X ×_𝔅 𝔅') ×_X U`, such that
>
> * the strict transform `U'` of `U` with respect to `v'` is the inverse image of the strict
>   transform `X'` of `X` with respect to `b` along `can`, which is part (2); and
> * for every `𝒪_X`-module `F` the pullback along `can` of the strict transform of `F` with
>   respect to `b` is the strict transform of `F|_U` with respect to `v'`, which is part (3).
>
> Both for the *same* `m` and the same `can`: the two parts are read off the single comparison
> morphism that part (1), `AlgebraicGeometry.Space.isEtale_baseChange_blowup_of_isEtale`,
> returns for the two canonical cartesian squares.  This is what a consumer of the tag needs, the
> two parts separately leaving the two copies of `can` unidentified.
>
> No hypothesis beyond the source's is carried, and no quasi-coherence of `F`; see
> `AlgebraicGeometry.Space.exists_strictTransform_eq_preimage` and
> `AlgebraicGeometry.Space.exists_isEtale_strictTransformSheaf_restriction`.

```lean
theorem exists_strictTransform_eq_preimage_strictTransformSheaf_iso
    {Z : ClosedSubspaces B S hS Bl.1} {b : B' ⟶ Bl} (hb : IsBlowupAlong B S hS Z b)
    {f : X ⟶ Bl} {v : Vv ⟶ Bl} (hv : IsEtale B S hS v.hom)
    {u : U ⟶ X} (hu : IsEtale B S hS u.hom) {w : U ⟶ Vv} (hcomm : u ≫ f = w ≫ v)
    {v' : V' ⟶ Vv} (hv' : IsBlowupAlong B S hS (preimageClosedSubspace v Z) v') :
    ∃ (m : V' ⟶ B') (can : strictTransformPullback B S hS w v' ⟶
        strictTransformPullback B S hS f b),
      IsPullback v' m v b ∧ IsEtale B S hS can.hom ∧
        can ≫ strictTransformPullbackToSource B S hS f b =
          strictTransformPullbackToSource B S hS w v' ≫ u ∧
        can ≫ strictTransformPullbackToBlowUp B S hS f b =
          strictTransformPullbackToBlowUp B S hS w v' ≫ m ∧
        IsPullback can (strictTransformPullbackToSource B S hS w v')
          (strictTransformPullbackToSource B S hS f b) u ∧
        strictTransformSubfunctor B S hS w v'
            (preimageClosedSubspace v' (preimageClosedSubspace v Z)).1 =
          (strictTransformSubfunctor B S hS f b
            (preimageClosedSubspace b Z).1).preimage can.hom ∧
        ∀ F : Modules.{u, u} B S hS X.1 X.2,
          Nonempty ((modulePullback B S hS can).obj
              (strictTransformSheaf B S hS f b (preimageClosedSubspace b Z).1 F) ≅
            strictTransformSheaf B S hS w v'
              (preimageClosedSubspace v' (preimageClosedSubspace v Z)).1
              ((modulePullback B S hS u).obj F))
```

## Tag 0864, a lemma

[Tag 0864](https://stacks.math.columbia.edu/tag/0864) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformIsBlowup.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformIsBlowup.lean#L347). The attribute's comment: “part (1): the strict transform of X is the blowup of X in the inverse image of the centre, for an arbitrary blowup of the base and with no assumed inputs”.

> **Stacks 0864, clause (1).**  Let `S` be a scheme, let `A` be an algebraic space over `S`,
> let `Z ⊆ A` be a closed subspace, let `b : A' ⟶ A` be the blowup of `A` in `Z` and let
> `f : X ⟶ A` be an algebraic space over `A`.  Then the strict transform `X'` of `X` — the closed
> subspace of `X ×_A A'` of Stacks 0862, clause (2) — with its morphism
> `X' ⟶ X ×_A A' ⟶ X`, **is the blowup of `X` in the inverse image `f⁻¹Z`.**
>
> No hypothesis beyond `b` being the blowup of `A` in `Z` is carried: in particular no second
> blowup is assumed to exist, and nothing is assumed of `f`.
>
> Both halves of the universal property of Stacks 085U are checked.  Membership in the category
> `𝒞` is `AlgebraicGeometry.Space.isPullbackDefined_strictTransform_of_isBlowupAlong`.  For
> finality, an object `y : Y ⟶ X` of `𝒞` gives a morphism `Y ⟶ X ×_A A'` with components `y` and
> the classifying morphism of `b`, which factors through `X'` by
> `AlgebraicGeometry.Space.exists_comp_eq_strictTransformSpaceι`; and the factorization is unique
> because `X' ⟶ X ×_A A'` is a monomorphism, `X ×_A A'` is a fibre product and the classifying
> morphism of `b` is unique.

```lean
theorem isBlowupAlong_strictTransform (hb : IsBlowupAlong B S hS Z b) :
    IsBlowupAlong B S hS (preimageClosedSubspace f Z)
      (strictTransformSpaceι B S hS f b (preimageClosedSubspace b Z).1 ≫
        strictTransformPullbackToSource B S hS f b)
```

**`AlgebraicGeometry.Space.exists_strictTransformSheafIso_modulePushforward_strictTransformSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformSheafBlowupComparison.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformSheafBlowupComparison.lean#L641). The attribute's comment: “part (2): the strict transform of a module is the direct image, along the closed immersion of the strict transform of X into X ×\_A A', of the strict transform of that module relative to the blowup X' ⟶ X, by the isomorphism carrying the quotient map onto the first to the canonical comparison; for an arbitrary blowup of the base, an arbitrary module, and with no assumed inputs”.

> **Stacks 0864, clause (2).**  Let `S` be a scheme, let `A` be an algebraic space over `S`,
> let `Z ⊆ A` be a closed subspace, let `b : A' ⟶ A` be the blowup of `A` in `Z`, let `f : X ⟶ A`
> be an algebraic space over `A` and let `F` be an `𝒪_X`-module.  Then the strict transform `F'` of
> `F` — the quotient of `pr_X^*F` by its sections supported on the exceptional preimage — **is the
> direct image, along the closed immersion `X' ⟶ X ×_A A'` of the strict transform of `X`, of the
> strict transform of `F` relative to the blowup `X' ⟶ X` of `X` in `f⁻¹Z`.**
>
> The isomorphism carries the quotient map onto `F'` to the canonical comparison
> `AlgebraicGeometry.Space.strictTransformSheafPushforwardComparison`, and since that quotient map
> is an epimorphism there is exactly one isomorphism which does; that is the sense in which the
> isomorphism of clause (2) is canonical.
>
> That `X' ⟶ X` is the blowup of `X` in `f⁻¹Z`, which is what makes the strict transform of `F`
> relative to it the one clause (2) speaks of, is clause (1),
> `AlgebraicGeometry.Space.isBlowupAlong_strictTransform`; the statement is otherwise
> `AlgebraicGeometry.Space.exists_strictTransformSheafIso_modulePushforward_of_isBlowupAlong` at
> `i` the closed immersion of the strict transform.
>
> No hypothesis beyond `b` being the blowup of `A` in `Z` is carried: in particular no second
> blowup is assumed to exist, nothing is assumed of `f`, and `F` is an arbitrary `𝒪_X`-module —
> the Stacks Project states clause (2) for a quasi-coherent `F`, and the argument uses nothing of
> `F`.  See the module documentation.

```lean
theorem exists_strictTransformSheafIso_modulePushforward_strictTransformSpace
    (hb : IsBlowupAlong B S hS Z b) (F : Modules.{u, u} B S hS X.1 X.2) :
    ∃ e : strictTransformSheaf B S hS f b (preimageClosedSubspace b Z).1 F ≅
        (modulePushforward B S hS
            (strictTransformSpaceι B S hS f b (preimageClosedSubspace b Z).1)).obj
          (strictTransformSheafOver B S hS
            (strictTransformSpaceι B S hS f b (preimageClosedSubspace b Z).1 ≫
              strictTransformPullbackToSource B S hS f b)
            (preimageClosedSubspace
              (strictTransformSpaceι B S hS f b (preimageClosedSubspace b Z).1 ≫
                strictTransformPullbackToSource B S hS f b)
              (preimageClosedSubspace f Z)) F),
      strictTransformSheafQuotient B S hS f b (preimageClosedSubspace b Z).1 F ≫ e.hom =
        strictTransformSheafPushforwardComparison B S hS f b Z
          (strictTransformSpaceι B S hS f b (preimageClosedSubspace b Z).1) F
```

## Tag 0865, a lemma

[Tag 0865](https://stacks.math.columbia.edu/tag/0865) in the Stacks Project.

**`AlgebraicGeometry.Space.strictTransformSubfunctor_eq_top_of_isFlatAt_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean#L101). The attribute's comment: “part (1), with no assumed inputs”.

> **Stacks 0865, part (1).** Let `Z ⊆ A` be a closed subspace of an algebraic space over `S`,
> let `b : A' ⟶ A` be the blowup of `A` in `Z` and let `f : X ⟶ A` be an algebraic space over
> `A`.  If `X` is flat over `A` at every point lying over `Z`, then the strict transform of `X`
> with respect to `b` is the whole base change `X ×_A A'`.
>
> The hypotheses are the source's and nothing else.  The ideal of sections of `𝒪_{X ×_A A'}`
> supported on the exceptional preimage vanishes on every étale chart,
> `AlgebraicGeometry.Space.strictTransformIdealSubmodule_eq_bot_of_isFlatAt`; the strict
> transform is then the whole base change by Stacks 03MB, in the form
> `AlgebraicGeometry.Space.strictTransformSubfunctor_eq_top_of_forall_definingIdealAt_eq_bot`.
>
> The source reduces part (1) to the case of schemes by étale localization, Stacks 0863 parts (2)
> and (3), which this library does not have; the route taken instead is native to algebraic
> spaces and runs through the étale charts of the fibre product.  See the module documentation of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatAtPointBaseChange.lean`.
>
> The conditional form of this statement in
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformProperties.lean` keeps the name
> without the suffix `_unconditional`; the suffix marks the same conclusion with that form's
> assumed input discharged, and the tag is registered here.

```lean
theorem strictTransformSubfunctor_eq_top_of_isFlatAt_unconditional (Z : ClosedSubspaces B S hS A.1)
    (hb : IsBlowupAlong B S hS Z b)
    (hflat : ∀ x : points B S hS X.1,
      pointsMap B S hS X.1 f.hom x ∈ Set.range (pointsMap B S hS Z.1.toFunctor Z.1.ι) →
        IsFlatAt B S hS f.hom x) :
    strictTransformSubfunctor B S hS f b (Z.1.preimage b.hom) = ⊤
```

**`AlgebraicGeometry.Space.isIso_strictTransformSheafQuotient_of_isFlatOverAtGeometricPoint_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean#L136). The attribute's comment: “part (2), with no assumed inputs”.

> **Stacks 0865, part (2).** In the situation of part (1), let `F` be a quasi-coherent
> `𝒪_X`-module which is flat over `A` at every point lying over `Z`.  Then the canonical quotient
> map `pr_X^*F ⟶ F'` onto the strict transform of `F` is an isomorphism, so the strict transform
> of `F` is `pr_X^*F`.
>
> The hypotheses are the source's and nothing else: `b` is the blowup of `A` in `Z` in the sense
> of the universal property of Stacks 085U, `F` is quasi-coherent, and `F` is flat over `A` at the
> points above `Z` — read at geometric points, condition (2) of Stacks 05VU,
> `AlgebraicGeometry.Space.IsFlatOverAtGeometricPoint`, a geometric point lying over `Z` when its
> underlying point of `|X|` does.
>
> The submodule of sections of `pr_X^*F` supported on the exceptional preimage vanishes,
> `Space.supportedSections_exceptionalPreimage_ι_eq_zero_of_isFlatOverAtGeometricPoint`;
> the strict transform is the cokernel of its inclusion, so the quotient map is the cokernel
> projection of a zero morphism and hence invertible.
>
> The source reduces part (2) to the case of schemes by étale localization, Stacks 0863 parts (2)
> and (3); the route taken instead is native to algebraic spaces and runs through the étale charts
> of the fibre product, exactly as for part (1).  See the module documentation of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleSupportedSections.lean`.
>
> The conditional form of this statement in
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformProperties.lean` keeps the name
> without the suffix `_unconditional`; the suffix marks the same conclusion with that form's
> assumed input discharged, and the tag is registered here.

```lean
theorem isIso_strictTransformSheafQuotient_of_isFlatOverAtGeometricPoint_unconditional
    (Z : ClosedSubspaces B S hS A.1) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hb : IsBlowupAlong B S hS Z b)
    (hflat : ∀ xbar : GeometricPoint B S hS X.1,
      pointsMap B S hS X.1 f.hom xbar.image ∈
          Set.range (pointsMap B S hS Z.1.toFunctor Z.1.ι) →
        IsFlatOverAtGeometricPoint B S hS f F xbar) :
    IsIso (strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) F)
```

## Tag 0866, a lemma

[Tag 0866](https://stacks.math.columbia.edu/tag/0866) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_modulePushforward_strictTransformSheaf_iso_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformAffinePushforward.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformAffinePushforward.lean#L108). The attribute's comment: “the hypotheses are the tag's own -- a blowup of the ambient space along a closed subspace, an affine morphism of algebraic spaces over it, and a quasi-coherent module -- and the base-change isomorphism of the base-change clause of Stacks 07U8, Stacks 02KG for an affine morphism of algebraic spaces, is proved on the way”.

> **Stacks 0866.** Let `Z ⊆ A` be a closed subspace of an algebraic space over `S`, let
> `b : A' ⟶ A` be the blowup of `A` in `Z`, let `g : X ⟶ Y` be an affine morphism of algebraic
> spaces over `A`, let `F` be an `𝒪_X`-module and let `g' : X ×_A A' ⟶ Y ×_A A'` be the base
> change of `g`.  Then `g'_*` of the strict transform of `F` relative to `b` is the strict
> transform of `g_* F`, compatibly with the two quotient maps and the base-change comparison.
>
> `F` is quasi-coherent, which is the tag's own hypothesis on it.
>
> The hypotheses are the tag's own, and the three inputs the argument runs on are all proved.
>
> The base-change isomorphism `α : g'_* pr_X^*F ≅ pr_Y^* g_*F` — the base-change clause of
> Stacks 07U8, that is Stacks 02KG for an affine morphism of algebraic spaces — is
> `AlgebraicGeometry.Space.nonempty_iso_modulePushforward_modulePullback_of_isAffineHom` at the
> cartesian square of the two ambient base changes along `b`.
>
> The identification `β` of the direct image of the sections supported on the exceptional
> preimage with the sections of `pr_Y^*(g_*F)` supported there, compatibly with `α`, is
> Stacks 085B transported along `α`,
> `AlgebraicGeometry.Space.exists_iso_modulePushforward_supportedSectionsSubmodule_of_eq_preimage`,
> together with the identification of the exceptional preimage upstairs as the inverse image of the
> one downstairs, `AlgebraicGeometry.Space.exceptionalPreimageSet_comp_eq_preimage`.
>
> Right exactness of `g'_*` on the sequence at hand — that the direct image along the affine
> morphism `g'` preserves the cokernel defining the strict transform, which is the use the
> Stacks Project makes of Stacks 01SB — is
> `AlgebraicGeometry.Space.preservesCokernel_submoduleι_modulePushforward_of_isAffineHom`, applied
> to the base change `g'` of `g`, which is affine by Stacks 03WI; its two quasi-coherence inputs
> are quasi-coherence of `pr_X^*F`, which is Stacks 03GA, and quasi-coherence of the submodule of
> sections supported on the exceptional preimage, which is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_supportedSections_exceptionalPreimage` above, the
> exceptional divisor of a blowup being an effective Cartier divisor and hence locally principal.
>
> What this proof does is the argument of the Stacks Project: the strict transform is a cokernel,
> right exactness of the affine direct image carries it through `g'_*`, and `α` identifies the
> resulting cokernel with the cokernel defining the strict transform of `g_* F`.

```lean
theorem exists_modulePushforward_strictTransformSheaf_iso_unconditional
    (Z : ClosedSubspaces B S hS A.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hb : IsBlowupAlong B S hS Z b) (hg : IsAffineHom B S hS g.hom) :
    ∃ (α : (modulePushforward B S hS (strictTransformPullbackMap B S hS g f b)).obj
              ((modulePullback B S hS
                (strictTransformPullbackToSource B S hS (g ≫ f) b)).obj F) ≅
            (modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).obj
              ((modulePushforward B S hS g).obj F))
        (e : (modulePushforward B S hS (strictTransformPullbackMap B S hS g f b)).obj
              (strictTransformSheaf B S hS (g ≫ f) b (Z.1.preimage b.hom) F) ≅
            strictTransformSheaf B S hS f b (Z.1.preimage b.hom)
              ((modulePushforward B S hS g).obj F)),
      (modulePushforward B S hS (strictTransformPullbackMap B S hS g f b)).map
            (strictTransformSheafQuotient B S hS (g ≫ f) b (Z.1.preimage b.hom) F) ≫ e.hom =
        α.hom ≫ strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom)
          ((modulePushforward B S hS g).obj F)
```

## Tag 0867, a lemma

[Tag 0867](https://stacks.math.columbia.edu/tag/0867) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_sumClosedSubspaces_and_strictTransformSheaf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupCentreEnlargedByDivisorUnconditional.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupCentreEnlargedByDivisorUnconditional.lean#L112). The attribute's comment: “both parts: (1) the blowup of the space in Z is the blowup in Z + D; (2) for a module on an algebraic space over the base with no nonzero sections supported on the inverse image of D, the strict transforms for the centres Z and Z + D agree; stated for every module, quasi-coherent or not”.

> **Stacks 0867.** Let `S` be a scheme, let `𝔅` be an algebraic space over `S`, let
> `Z ⊆ 𝔅` be a closed subspace, let `D ⊆ 𝔅` be an effective Cartier divisor, let `Z + D` be the
> closed subspace cut out by the product of the ideal sheaves of `Z` and `D`, and let
> `b : B' ⟶ 𝔅` be the blowup of `𝔅` in `Z`.
>
> 1. `b` is also the blowup of `𝔅` in `Z + D`; so every blowup of `𝔅` in `Z + D` is isomorphic
>    to `b` over `𝔅`
>    (`AlgebraicGeometry.Space.exists_iso_blowup_sumClosedSubspaces_of_isEffectiveCartierDivisor`).
> 2. For every morphism of algebraic spaces `f : X ⟶ 𝔅` and every `𝒪_X`-module `F` whose subsheaf
>    of sections supported on `|f⁻¹D|` is zero, the strict transform of `F` relative to the
>    blowup of `𝔅` in `Z` agrees with the strict transform of `F` relative to the blowup of `𝔅`
>    in `Z + D`, which by (1) is the same morphism `b`.
>
> Part (1) is
> `AlgebraicGeometry.Space.isBlowupAlong_sumClosedSubspaces_of_isEffectiveCartierDivisor` and
> part (2) is `AlgebraicGeometry.Space.strictTransformSheaf_preimage_sumClosedSubspaces`.  The
> source asks `F` to be quasi-coherent; the statement holds for every `𝒪_X`-module.

```lean
theorem isBlowupAlong_sumClosedSubspaces_and_strictTransformSheaf_eq
    {𝔅 B' : AlgebraicSpaces B S hS} (Z D : ClosedSubspaces B S hS 𝔅.obj)
    (hD : IsEffectiveCartierDivisor B S hS 𝔅 D)
    {b : B' ⟶ 𝔅} (hb : IsBlowupAlong B S hS Z b) :
    IsBlowupAlong B S hS (sumClosedSubspaces B S hS 𝔅 Z D) b ∧
      ∀ (X : AlgebraicSpaces B S hS) (f : X ⟶ 𝔅) (F : Modules.{u, u} B S hS X.1 X.2),
        HasNoSectionsSupportedIn B S hS X
            (pointsMap B S hS X.1 f.hom ⁻¹' subspacePointSet B S hS 𝔅.1 D.1) F →
          strictTransformSheaf B S hS f b
              (preimageClosedSubspace b (sumClosedSubspaces B S hS 𝔅 Z D)).1 F =
            strictTransformSheaf B S hS f b (preimageClosedSubspace b Z).1 F
```

## Tag 0868, a lemma

[Tag 0868](https://stacks.math.columbia.edu/tag/0868) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_strictTransformSheaf_comp_iso_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean#L211). The attribute's comment: “part (1): the strict transform of a module for the blowup of the base in the composite centre is the strict transform along the second blowup of the strict transform along the first, by the isomorphism carrying the pullback of the quotient map onto the former to the composite of the two quotient maps onto the latter, over the identification of the two ambient base changes and the identification of the two pullbacks of the module it induces; for an arbitrary module and with no assumed inputs”.

> **Stacks 0868, part (1).** Let `Z ⊆ A` be a closed subspace of an algebraic space over `S`,
> let `b : A' ⟶ A` be the blowup of `A` in `Z`, let `Z' ⊆ A'` be a closed subspace and let
> `c : A'' ⟶ A'` be the blowup of `A'` in `Z'`.  Let `Y ⊆ A` be a closed subspace with
> `|Y| = |Z| ∪ |b|(|Z'|)` and such that the composition `A'' ⟶ A` is the blowup of `A` in `Y`.
> Then for any algebraic space `f : X ⟶ A` over `A` and any `𝒪_X`-module `F`, the strict
> transform of `F` with respect to `c` of the strict transform of `F` with respect to `b` is the
> strict transform of `F` with respect to `A'' ⟶ A`, compatibly with the identification of the
> two ambient base changes and with the quotient maps onto the two strict transforms.
>
> The identification of the ambient base changes `(X ×_A A') ×_{A'} A'' ≅ X ×_A A''`, together
> with its compatibility with the projections to `X` and to `A''` — the two equations of the
> conclusion, the first of which the comparison of the modules is stated relative to — is
> `AlgebraicGeometry.Space.iteratedStrictTransformPullbackIso`, and is proved here
> unconditionally.
>
> The comparison of the modules themselves, the last conjunct, is produced with its compatibility
> with the two quotient maps onto the strict transforms: pulled back along the identification of
> the ambient base changes, the quotient map `pr_X^*F ⟶ F'` for the composite blowup becomes, over
> the induced identification of the two pullbacks of `F`
> (`AlgebraicGeometry.Space.strictTransformInnerModulePullbackIso`), the composite of the pullback
> of the first quotient map with the second.  Since the first of those is an epimorphism, there is
> exactly one isomorphism which does that; that is the sense in which the comparison is canonical.
>
> Its two halves are `AlgebraicGeometry.Space.exists_iteratedStrictTransformSheaf_iso` of
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformComposition.lean` — which carries the
> compatibility of the iterated quotient with the two projections — and the universal property of
> the quotient by the supported sections,
> `AlgebraicGeometry.Space.exists_strictTransformSheafIso`, applied to the pullback of the
> quotient map for the composite blowup along the ambient identification.  That pullback is an
> epimorphism because the pullback of modules is a left adjoint; it kills only the sections
> supported on the exceptional preimage of `(c ≫ b)⁻¹Y` because over the part of
> `(X ×_A A') ×_{A'} A''` lying off that set it is invertible
> (`AlgebraicGeometry.Space.isIso_modulePullback_map_cokernelπ_supportedSectionsSubmodule`, the
> points there missing the exceptional preimage downstairs), which is
> `AlgebraicGeometry.Space.kernelSectionsSupportedIn_of_mono_modulePullback_map`; and its target
> has no nonzero local section supported there because the restriction of the strict transform
> along that identification is the strict transform of the restriction, Stacks 0863 part (3) in
> its geometry-free form
> `AlgebraicGeometry.Space.strictTransformSheafEtaleRestrictionIso` — applicable because the
> identification is an isomorphism, hence étale.
>
> The hypothesis of the iterated comparison on the supported sets is
> `AlgebraicGeometry.Space.exceptionalPreimageSet_compositeCentre`, which is where `hY` and the
> blowup `b` are used: a blowup is injective on the points off its centre, so the exceptional
> preimage of `(c ≫ b)⁻¹Y` splits as the inverse image of the first exceptional preimage together
> with the exceptional preimage of `c⁻¹Z'`.
>
> The conditional form of this statement in
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformProperties.lean` keeps the name
> without the suffix `_unconditional`; the suffix marks the same conclusion with that form's
> assumed input discharged, and the tag is registered here.

```lean
theorem exists_strictTransformSheaf_comp_iso_unconditional (Z : ClosedSubspaces B S hS A.1)
    (Z' : ClosedSubspaces B S hS A'.1) (Y : ClosedSubspaces B S hS A.1)
    (F : Modules.{u, u} B S hS X.1 X.2)
    (hb : IsBlowupAlong B S hS Z b) (hc : IsBlowupAlong B S hS Z' c)
    (hY : IsCompositeCentre B S hS b Z Z' Y) (_hd : IsBlowupAlong B S hS Y (c ≫ b)) :
    ∃ e : strictTransformPullback B S hS (strictTransformPullbackToBlowUp B S hS f b) c ≅
        strictTransformPullback B S hS f (c ≫ b),
      ∃ hsrc : e.hom ≫ strictTransformPullbackToSource B S hS f (c ≫ b) =
          strictTransformPullbackToSource B S hS
              (strictTransformPullbackToBlowUp B S hS f b) c ≫
            strictTransformPullbackToSource B S hS f b,
      (e.hom ≫ strictTransformPullbackToBlowUp B S hS f (c ≫ b) =
        strictTransformPullbackToBlowUp B S hS
          (strictTransformPullbackToBlowUp B S hS f b) c) ∧
      ∃ cmp : (modulePullback B S hS e.hom).obj
            (strictTransformSheaf B S hS f (c ≫ b) (Y.1.preimage (c ≫ b).hom) F) ≅
          strictTransformSheaf B S hS (strictTransformPullbackToBlowUp B S hS f b) c
            (Z'.1.preimage c.hom) (strictTransformSheaf B S hS f b (Z.1.preimage b.hom) F),
        (modulePullback B S hS e.hom).map
              (strictTransformSheafQuotient B S hS f (c ≫ b)
                (Y.1.preimage (c ≫ b).hom) F) ≫ cmp.hom =
          (strictTransformInnerModulePullbackIso B S hS f (c ≫ b)
              (strictTransformPullbackToSource B S hS f b)
              (strictTransformPullbackToBlowUp B S hS f b) c e.hom hsrc F).hom ≫
            (modulePullback B S hS (strictTransformPullbackToSource B S hS
                  (strictTransformPullbackToBlowUp B S hS f b) c)).map
                (strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) F) ≫
              strictTransformSheafQuotient B S hS
                (strictTransformPullbackToBlowUp B S hS f b) c (Z'.1.preimage c.hom)
                (strictTransformSheaf B S hS f b (Z.1.preimage b.hom) F)
```

**`AlgebraicGeometry.Space.exists_strictTransformSpace_comp_iso_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFlatCompositionUnassumed.lean#L473). The attribute's comment: “part (2): strict transform of a space”.

> **Stacks 0868, part (2).** In the situation of part (1), the strict transform of `X` with
> respect to `c` of the strict transform of `X` with respect to `b` is the strict transform of `X`
> with respect to `A'' ⟶ A`: the two closed subspaces are isomorphic over the ambient base change
> `X ×_A A''`.
>
> The morphism `X' ×_{A'} A'' ⟶ X ×_A A''` of ambient base changes along which the comparison is
> made is `AlgebraicGeometry.Space.iteratedStrictTransformSpaceMap`; `X'` here is the first strict
> transform, the ambient base change of the second being taken over `A'` and not over `X ×_A A'`.
> Its two triangles over `X` and over `A''` are the first two conjuncts of the conclusion and hold
> with no hypothesis at all.
>
> The comparison of the two closed subspaces is
> `AlgebraicGeometry.Space.exists_iteratedStrictTransformSpace_iso` of
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformSpaceComposition.lean`.  Its route is the
> source's own, read on ideals: the image of the second strict transform in `(X ×_A A') ×_{A'} A''`
> is a closed subspace whose defining ideal is exactly the ideal of functions supported on the
> exceptional preimage of `(c ≫ b)^{-1}Y`, so it *is* the strict transform of `X` with respect to
> the composite by `AlgebraicGeometry.Space.strictTransformSubfunctor_eq_of_definingIdealSheaf_eq`,
> and the identification of the two ambient base changes transports that across Stacks 0863 part
> (2).  One inclusion of ideals is the geometry of the two blowups (Stacks 085T through
> `AlgebraicGeometry.Space.exceptionalPreimageSet_compositeCentre`, and Stacks 0862 off the
> exceptional divisor); the other is Stacks 082Z together with the fact that the second strict
> transform has no nonzero local function supported there, which is Stacks 083S for the two
> exceptional divisors it is built from.
>
> The conditional form of this statement in
> `StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformProperties.lean` keeps the name
> without the suffix `_unconditional`; the suffix marks the same conclusion with that form's
> assumed input discharged, and the tag is registered here.

```lean
theorem exists_strictTransformSpace_comp_iso_unconditional (Z : ClosedSubspaces B S hS A.1)
    (Z' : ClosedSubspaces B S hS A'.1) (Y : ClosedSubspaces B S hS A.1)
    (hb : IsBlowupAlong B S hS Z b) (hc : IsBlowupAlong B S hS Z' c)
    (hY : IsCompositeCentre B S hS b Z Z' Y) (hd : IsBlowupAlong B S hS Y (c ≫ b)) :
    ∃ (k : strictTransformPullback B S hS
          (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)) c ⟶
        strictTransformPullback B S hS f (c ≫ b))
      (j : strictTransformSpace B S hS
          (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)) c
          (Z'.1.preimage c.hom) ≅
        strictTransformSpace B S hS f (c ≫ b) (Y.1.preimage (c ≫ b).hom)),
      (k ≫ strictTransformPullbackToSource B S hS f (c ≫ b) =
        strictTransformPullbackToSource B S hS
            (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)) c ≫
          strictTransformSpaceι B S hS f b (Z.1.preimage b.hom) ≫
            strictTransformPullbackToSource B S hS f b) ∧
      (k ≫ strictTransformPullbackToBlowUp B S hS f (c ≫ b) =
        strictTransformPullbackToBlowUp B S hS
          (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)) c) ∧
      j.hom ≫ strictTransformSpaceι B S hS f (c ≫ b) (Y.1.preimage (c ≫ b).hom) =
        strictTransformSpaceι B S hS
            (strictTransformSpaceToBlowUp B S hS f b (Z.1.preimage b.hom)) c
            (Z'.1.preimage c.hom) ≫ k
```

## Tag 0869, a lemma

[Tag 0869](https://stacks.math.columbia.edu/tag/0869) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_strictTransformSheaf_shortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformShortExact.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformShortExact.lean#L500). The attribute's comment: “partial: the short complex of strict transforms with its two maps pinned down by the quotient maps, monomorphic on the left and epimorphic on the right, all unconditional; exactness in the middle is NOT proved and is instead reduced, as an equivalence, to epimorphy of the induced map on the subsheaves of sections supported on the exceptional preimage — the statement that Stacks 0863 parts (2) and (3) together with the scheme-level Stacks 080W would supply and that this library cannot reach”.

> **Stacks 0869, as far as this library reaches it.**  In the situation of Stacks 0862, let
> `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` be a sequence of `𝒪_X`-modules which is short exact after every base
> change `Y ⟶ A`.  Then the strict transforms of the `Fᵢ` relative to `(b, E)` form a short
> complex whose two maps are determined by the quotient maps onto the strict transforms; the
> left-hand map is a monomorphism and the right-hand map is an epimorphism, and exactness in the
> middle is equivalent to epimorphy of the morphism induced on the subsheaves of sections
> supported on the exceptional preimage.
>
> Everything asserted here is unconditional.  Exactness in the middle — the heart of the tag — is
> *not* proved; the last conjunct is the exact reduction of it, and the module documentation
> records what would discharge the reduced statement and why that input is absent.

```lean
theorem exists_strictTransformSheaf_shortComplex
    (hC : ∀ (Y P : AlgebraicSpaces B S hS) (t : Y ⟶ A) (pX : P ⟶ X) (pY : P ⟶ Y),
      IsPullback pX pY f t → (C.map (modulePullback B S hS pX)).ShortExact) :
    ∃ (f' : strictTransformSheaf B S hS f b E C.X₁ ⟶ strictTransformSheaf B S hS f b E C.X₂)
      (g' : strictTransformSheaf B S hS f b E C.X₂ ⟶ strictTransformSheaf B S hS f b E C.X₃)
      (w : f' ≫ g' = 0),
      Mono f' ∧ Epi g' ∧
      (strictTransformSheafQuotient B S hS f b E C.X₁ ≫ f' =
        (modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).map C.f ≫
          strictTransformSheafQuotient B S hS f b E C.X₂) ∧
      (strictTransformSheafQuotient B S hS f b E C.X₂ ≫ g' =
        (modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).map C.g ≫
          strictTransformSheafQuotient B S hS f b E C.X₃) ∧
      ((ShortComplex.mk f' g' w).Exact ↔
        Epi (supportedSectionsMap (exceptionalPreimageSet B S hS f b E)
          ((modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).map C.g)))
```

**`AlgebraicGeometry.Space.exists_strictTransformSheaf_shortComplex_of_isBlowupAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformShortExactBlowup.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformShortExactBlowup.lean#L89). The attribute's comment: “the strict transforms of a short exact sequence of quasi-coherent modules which stays short exact after every base change again form a short exact sequence, with its two maps pinned down by the quotient maps onto the strict transforms”.

> **Stacks 0869.**  In the situation of Stacks 0862 — a blowup `b : A' ⟶ A` of an algebraic
> space `A` in a closed subspace `Z`, with exceptional divisor `E = b^{-1}Z`, and an algebraic
> space `f : X ⟶ A` over `A` — let `0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` be a sequence of quasi-coherent
> `𝒪_X`-modules which is short exact after every base change `Y ⟶ A`.  Then the strict transforms
> of the `Fᵢ` form a short complex whose two maps are determined by the quotient maps onto the
> strict transforms, the left-hand map is a monomorphism, the right-hand map is an epimorphism,
> and the complex is exact in the middle: the strict transforms form a short exact sequence.
>
> The strict transform is the one of Stacks 0862,
> `AlgebraicGeometry.Space.strictTransformSheaf`, and "being the blowup of `A` in `Z`" is
> `AlgebraicGeometry.Space.IsBlowupAlong`, the universal property of Stacks 085U, since Stacks
> 085Q constructs no blowup of an algebraic space in this library.

```lean
theorem exists_strictTransformSheaf_shortComplex_of_isBlowupAlong {Z : ClosedSubspaces B S hS A.1}
    {b : A' ⟶ A}
    (hb : IsBlowupAlong B S hS Z b) (C : ShortComplex (Modules.{u, u} B S hS X.1 X.2))
    (hqc₁ : C.X₁.IsQuasicoherentOnSite) (hqc₂ : C.X₂.IsQuasicoherentOnSite)
    (hqc₃ : C.X₃.IsQuasicoherentOnSite)
    (hC : ∀ (Y P : AlgebraicSpaces B S hS) (t : Y ⟶ A) (pX : P ⟶ X) (pY : P ⟶ Y),
      IsPullback pX pY f t → (C.map (modulePullback B S hS pX)).ShortExact) :
    ∃ (f' : strictTransformSheaf B S hS f b (Z.1.preimage b.hom) C.X₁ ⟶
          strictTransformSheaf B S hS f b (Z.1.preimage b.hom) C.X₂)
      (g' : strictTransformSheaf B S hS f b (Z.1.preimage b.hom) C.X₂ ⟶
          strictTransformSheaf B S hS f b (Z.1.preimage b.hom) C.X₃)
      (w : f' ≫ g' = 0),
      Mono f' ∧ Epi g' ∧
      (strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) C.X₁ ≫ f' =
        (modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).map C.f ≫
          strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) C.X₂) ∧
      (strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) C.X₂ ≫ g' =
        (modulePullback B S hS (strictTransformPullbackToSource B S hS f b)).map C.g ≫
          strictTransformSheafQuotient B S hS f b (Z.1.preimage b.hom) C.X₃) ∧
      (ShortComplex.mk f' g' w).Exact
```

## Tag 0D0P, a lemma

[Tag 0D0P](https://stacks.math.columbia.edu/tag/0D0P) in the Stacks Project.

**`AlgebraicGeometry.Space.strictTransformSheaf_isLocallyGeneratedByOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformLocalGenerators.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformLocalGenerators.lean#L922).

> Let `F` be a finite type quasi-coherent module on an algebraic space `Bsp`, let `Z ⊆ Bsp` be
> the closed subspace cut out by the `k`-th Fitting ideal sheaf of `F`, and let `b : Bsp' ⟶ Bsp` be
> the blowup of `Bsp` in `Z`.  Then the strict transform of `F` can locally be generated by `k`
> sections.

```lean
theorem strictTransformSheaf_isLocallyGeneratedByOnSite
    {Bsp Bsp' : AlgebraicSpaces B S hS} (F : Modules.{u, u} B S hS Bsp.1 Bsp.2) (k : ℕ)
    (Z : ClosedSubspaces B S hS Bsp.1)
    (hZ : definingIdealSheaf B S hS Bsp Z = fittingIdeal B S hS Bsp.1 Bsp.2 F k)
    {b : Bsp' ⟶ Bsp} (hb : IsBlowupAlong B S hS Z b) (hFqc : F.IsQuasicoherentOnSite)
    (hFfin : ∀ W : SmallEtale B S hS Bsp.1,
      IsAffine ((SmallEtale.toOver B S hS Bsp.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS Bsp.1 Bsp.2 W) (F.val.obj (op W))) :
    SheafOfModules.IsLocallyGeneratedByOnSite
      (strictTransformSheaf B S hS (𝟙 Bsp) b (preimageClosedSubspace b Z).1 F) k
```

## Tag 0D0Q, a lemma

[Tag 0D0Q](https://stacks.math.columbia.edu/tag/0D0Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOfRank_strictTransformSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFittingRank.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StrictTransformFittingRank.lean#L518).

> Let `F` be a finite type quasi-coherent module on an algebraic space `Bsp`, let `Z ⊆ Bsp` be
> the closed subspace cut out by the `k`-th Fitting ideal sheaf of `F`, let `b : Bsp' ⟶ Bsp` be the
> blowup of `Bsp` in `Z`, and assume that `F` is locally free of rank `k` on the open complement
> `Bsp ∖ Z`.  Then the strict transform of `F` is locally free of rank `k`.

```lean
theorem isFiniteLocallyFreeOfRank_strictTransformSheaf
    {Bsp Bsp' : AlgebraicSpaces B S hS} (F : Modules.{u, u} B S hS Bsp.1 Bsp.2) (k : ℕ)
    (Z : ClosedSubspaces B S hS Bsp.1)
    (hZ : definingIdealSheaf B S hS Bsp Z = fittingIdeal B S hS Bsp.1 Bsp.2 F k)
    {b : Bsp' ⟶ Bsp} (hb : IsBlowupAlong B S hS Z b) (hFqc : F.IsQuasicoherentOnSite)
    (hFfin : ∀ W : SmallEtale B S hS Bsp.1,
      IsAffine ((SmallEtale.toOver B S hS Bsp.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS Bsp.1 Bsp.2 W) (F.val.obj (op W)))
    (h : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite B S hS (openComplementSpace B S hS Bsp Z).1
        (openComplementSpace B S hS Bsp Z).2)
      ((modulePullback B S hS (openComplementHom B S hS Bsp Z)).obj F) k) :
    RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite B S hS (strictTransformPullback B S hS (𝟙 Bsp) b).1
        (strictTransformPullback B S hS (𝟙 Bsp) b).2)
      (strictTransformSheaf B S hS (𝟙 Bsp) b (preimageClosedSubspace b Z).1 F) k
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.18, Tag 0861](https://stacks.math.columbia.edu/tag/0861)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
