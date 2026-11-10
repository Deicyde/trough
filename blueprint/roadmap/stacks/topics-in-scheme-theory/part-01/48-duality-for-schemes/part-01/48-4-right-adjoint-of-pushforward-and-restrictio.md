---
declaration: section
origin: cited
lean: CategoryTheory.IsPullback, Stacks.Duality.isIso_refinementXi, Stacks.Duality.OpenImmersion.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion, Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent, Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap, Stacks.Duality.OpenImmersion.isIso_qcqsTwistedInverseImageRestrictionMap_app_iff, Stacks.Duality.OpenImmersion.exists_not_isIso_qcqsTwistedInverseImageRestrictionMap_app, Stacks.Duality.OpenImmersion.qcqs_cohomologySupportedOn_iff_isIso_restrictionMap
statement: formalized
proof: formalized
---

# 48.4 Right adjoint of pushforward and restriction to opens

Section 48.4 of the Stacks Project, [Tag 0E4G](https://stacks.math.columbia.edu/tag/0E4G). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A9J, an equation

[Tag 0A9J](https://stacks.math.columbia.edu/tag/0A9J) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch48.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch48.lean#L16) (StacksFrontier): “the cartesian square of a base change”. References: SGA 4 I (10.1).

## Tag 0A9K, a lemma

[Tag 0A9K](https://stacks.math.columbia.edu/tag/0A9K) in the Stacks Project.

**`Stacks.Duality.isIso_refinementXi`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekRefinementXi.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekRefinementXi.lean#L73). The attribute's comment: “for the cartesian square of an interior-preserving morphism of compactifications of a morphism of AlgebraicGeometry.FTS S over a Noetherian base, whose base change morphism is the open immersion of the target compactification. See Stacks.Duality.OpenImmersion.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion for the scope of the registration and for why the general Tor-independent case is not proved. What this discharges is the instance argument IsIso (Stacks.Duality.refinementXi ..) of Stacks.Duality.refinementBaseChange and of Stacks.Duality.refinementIso; the other instance argument, Stacks 0A9P, is Stacks.Duality.isIso_refinementBaseChangePlus”.

> **[Stacks, Tag 0A9K] for the cartesian square of an interior-preserving morphism of
> compactifications.**  The base change morphism of that square is the open immersion `j₂` of the
> target compactification, so this is
> `Stacks.Duality.OpenImmersion.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion`;
> no hypothesis is carried.

```lean
instance isIso_refinementXi (hg : CompactificationOf.PreservesInterior g) :
    IsIso (refinementXi f g hg)
```

**`Stacks.Duality.OpenImmersion.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean#L372). The attribute's comment: “for a cartesian square of schemes whose base change morphism g is an OPEN IMMERSION, hence flat, hence Tor independent of f: the transformation xi = Stacks.Duality.twistedInverseImagePushforwardBaseChange of the Situation of Stacks 0A9J is invertible, with nothing assumed beyond the quasi-coherence of the cohomology of the four derived direct images (Stacks 08D5) and the existence of the two twisted inverse images (Stacks 0A9E), which is what makes xi exist. The general Tor-independent case is NOT proved: by Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_iff it is equivalent to Stacks 08IB, whose route Stacks 0DJ9 is carried in this repository over three unproved hypotheses (AlgebraicGeometry.BaseChangeAffineOpenCase, AlgebraicGeometry.BaseChangeMayerVietorisStep, and the localization step) at AlgebraicGeometry.isIso_derivedBaseChangeComp_of_affineCase. Along an open immersion none of that is needed, Stacks 08IB being replaced by Stacks 08FE”.

> **[Stacks, Tag 0A9K] for a cartesian square whose base change morphism is an open
> immersion.**  In the Situation of [Stacks, Tag 0A9J], if `j : V ⟶ Y` is an open immersion — so
> flat, and the square is Tor independent — then the transformation
> `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` is an isomorphism.
>
> The arguments are the four quasi-coherence conditions of [Stacks, Tag 08D5] and the two
> adjointness instances of [Stacks, Tag 0A9E], without which `ξ` does not exist; no further
> hypothesis is carried.

```lean
theorem isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion
    [(Stacks.Duality.quasiCoherentDerivedPushforward f hpushf).IsLeftAdjoint]
    [(Stacks.Duality.quasiCoherentDerivedPushforward f' hpushf').IsLeftAdjoint]
    (sq : IsPullback j' f' f j) :
    IsIso (Stacks.Duality.twistedInverseImagePushforwardBaseChange j' f' f j hpushj' hpushf
      hpushf' hpushj sq)
```

**`Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeIsIso.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeIsIso.lean#L344).

> **[Stacks, Tag 0A9K].** Let
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> Y' --g---> Y
> ```
> be a cartesian square of quasi-compact and quasi-separated schemes (Situation [Stacks, Tag 0A9J]:
> all four schemes), and let `a`, `a'` be the right adjoints of `Rf_*`, `Rf'_*` on `D_QCoh`
> ([Stacks, Tag 0A9E]). If `f` and `g` are Tor independent (for instance if `g` is flat,
> `AlgebraicGeometry.torIndependent_of_flat_right`), the transformation
> `ξ : Rg'_* ∘ a' ⟶ a ∘ Rg_*` is invertible.

```lean
theorem isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent
    {X' X Y' Y : Scheme.{u}} [CompactSpace X'] [QuasiSeparatedSpace X'] [CompactSpace X]
    [QuasiSeparatedSpace X] [CompactSpace Y'] [QuasiSeparatedSpace Y'] [CompactSpace Y]
    [QuasiSeparatedSpace Y] {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (sq : IsPullback g' f' f g) (hTor : TorIndependent f g) :
    IsIso (twistedInverseImagePushforwardBaseChange g' f' f g
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq)
```

## Tag 0A9L, an equation

[Tag 0A9L](https://stacks.math.columbia.edu/tag/0A9L) in the Stacks Project.

**`Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionQcqs.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionQcqs.lean#L106).

> **Stacks Project, Tag 0A9L.** For a morphism `f : X ⟶ Y` of quasi-compact and
> quasi-separated schemes and a quasi-compact open `V ⊆ Y`, with `U = f⁻¹(V)`, `j : V ⟶ Y` and
> `j' : U ⟶ X` the inclusions, the transformation `(j')^* ∘ a ⟶ a' ∘ j^*` of functors
> `D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_U)`, where `a` and `a'` are the right adjoints of `Rf_*` and
> `R(f|_U)_*`: the unit of `j^* ⊣ Rj_*`, then the inverse of the isomorphism
> `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` of [Stacks, Tag 0A9K], then the counit of `(j')^* ⊣ Rj'_*`.
>
> It is `Stacks.Duality.OpenImmersion.twistedInverseImageRestrictionMap` for the square
> `AlgebraicGeometry.isPullback_morphismRestrict`, every argument of which is proved here.

```lean
def qcqsTwistedInverseImageRestrictionMap :
    twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⋙
        quasiCoherentDerivedRestrict (f ⁻¹ᵁ V).ι
          (isQuasicoherent_homology_derivedRestrict (f ⁻¹ᵁ V).ι) ⟶
      quasiCoherentDerivedRestrict V.ι (isQuasicoherent_homology_derivedRestrict V.ι) ⋙
        twistedInverseImage (f ∣_ V) (isQuasicoherent_homology_derivedPushforward_of_qcqs _)
```

**`Stacks.Duality.OpenImmersion.isIso_qcqsTwistedInverseImageRestrictionMap_app_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionQcqs.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionQcqs.lean#L127). The attribute's comment: “the isomorphism criterion: invertible at `K` iff `a(K)|_U ⟶ a(Rj_*(K|_V))|_U` is”.

> **Stacks Project, Tag 0A9L, the criterion.** The transformation
> `Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap` is an isomorphism when
> evaluated on `K` if and only if `a(K)|_U ⟶ a(Rj_*(K|_V))|_U`, the restriction to `U` of `a`
> applied to the unit of `j^* ⊣ Rj_*` at `K`, is an isomorphism: the other two arrows of the
> composite are invertible.

```lean
theorem isIso_qcqsTwistedInverseImageRestrictionMap_app_iff
    (K : quasiCoherentDerivedCategory Y) :
    IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K) ↔
      IsIso ((quasiCoherentDerivedRestrict (f ⁻¹ᵁ V).ι
          (isQuasicoherent_homology_derivedRestrict (f ⁻¹ᵁ V).ι)).map
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map
          ((quasiCoherentDerivedRestrictAdjunction V.ι
            (isQuasicoherent_homology_derivedRestrict V.ι)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs _)).unit.app K)))
```

## Tag 0A9M, an example

[Tag 0A9M](https://stacks.math.columbia.edu/tag/0A9M) in the Stacks Project.

**`Stacks.Duality.OpenImmersion.exists_not_isIso_qcqsTwistedInverseImageRestrictionMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionExample.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionExample.lean#L276).

> **Stacks Project, Tag 0A9M.** There is a finite morphism `f : X ⟶ Y` of Noetherian schemes, a
> quasi-compact open `V ⊆ Y` and an object `K` of `D_QCoh(𝒪_Y)` with coherent cohomology sheaves,
> such that the map `(j')^*(a(K)) ⟶ a'(K|_V)` of [Stacks, Tag 0A9L]
> (`Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap`) is not an isomorphism.
>
> The witnesses are those of the source, over the field `k = ℚ`: `f : Spec k[x] ⟶ Spec k[x][ε]`
> (`Stacks.SquareZeroExt.specProj`), `V = D(x)` (`Stacks.SquareZeroExt.basicOpenX`) and
> `K = ⨁ₙ Mₙ[n]` with `Mₙ = k[x][ε]/(ε, xⁿ)` (`Stacks.SquareZeroExt.coefficientSumTilde`). The
> same holds over every field, which is
> `Stacks.SquareZeroExt.not_isIso_qcqsTwistedInverseImageRestrictionMap_app`.

```lean
theorem exists_not_isIso_qcqsTwistedInverseImageRestrictionMap_app :
    ∃ (X Y : Scheme.{u}) (f : X ⟶ Y) (_ : IsFinite f) (_ : IsNoetherian X) (_ : IsNoetherian Y)
      (V : Y.Opens) (_ : CompactSpace V) (K : quasiCoherentDerivedCategory Y),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor Y.Modules i).obj K.obj).IsCoherent) ∧
        ¬ IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K)
```

## Tag 0A9N, a lemma

[Tag 0A9N](https://stacks.math.columbia.edu/tag/0A9N) in the Stacks Project.

**`Stacks.Duality.OpenImmersion.qcqs_cohomologySupportedOn_iff_isIso_restrictionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionSupportQcqs.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionSupportQcqs.lean#L54). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0A9N], part (2), at the source's hypotheses, with nothing carried.** Let
> `f : X ⟶ Y` be a morphism of quasi-compact and quasi-separated schemes, let `a` be the right
> adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, let `V ⊆ Y` be a quasi-compact open with inverse
> image `U = f⁻¹(V)`. Then for every `Q ∈ D_QCoh(𝒪_Y)` supported on `Y ∖ V` the image `a(Q)` is
> supported on `X ∖ U` if and only if the comparison of [Stacks, Tag 0A9L] is an isomorphism on all
> `K` in `D_QCoh(𝒪_Y)`.

```lean
theorem qcqs_cohomologySupportedOn_iff_isIso_restrictionMap :
    (∀ Q : quasiCoherentDerivedCategory Y,
        Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn Y.ringCatSheaf
            (Set.range V.ι.base)ᶜ Q.obj →
          Stacks.Cohomology.PushforwardRestriction.CohomologySupportedOn X.ringCatSheaf
            (Set.range (f ⁻¹ᵁ V).ι.base)ᶜ
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              Q).obj) ↔
      (∀ K : quasiCoherentDerivedCategory Y,
        IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K))
```

**`Stacks.Duality.twistedInverseImageRestrictionMap_isIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/RestrictionSupport.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/RestrictionSupport.lean#L336).

> **[Stacks, Tag 0A9N].** Let `f : X ⟶ Y` be a morphism of quasi-compact quasi-separated schemes,
> `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, `j : V ⟶ Y` the inclusion of a
> quasi-compact open and `j' : U ⟶ X` its base change, with `f' : U ⟶ V` and `a'` the right adjoint
> of `Rf'_*`. Then, writing `φ : (j')^* ∘ a ⟶ a' ∘ j^*` for the map of [Stacks, Tag 0A9L]:
> 1. `a` carries every `Q ∈ D^+_QCoh(𝒪_Y)` supported on `Y ∖ V` to an object supported on `X ∖ U` if
>    and only if `φ` is invertible on `D^+_QCoh(𝒪_Y)`;
> 2. the same holds with `D_QCoh(𝒪_Y)` in place of `D^+_QCoh(𝒪_Y)`;
> 3. if `a` commutes with direct sums, the conditions of (1) imply those of (2).
> "Supported on `Y ∖ V`" is "restricts to zero on `V`". The square is an arbitrary cartesian square
> along `j`.

```lean
theorem twistedInverseImageRestrictionMap_isIso_iff (sq : IsPullback j' f' f j) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : QuasiSeparatedSpace V := j.isOpenEmbedding.quasiSeparatedSpace
    haveI : QuasiSeparatedSpace U := j'.isOpenEmbedding.quasiSeparatedSpace
    haveI : CompactSpace U := compactSpace_of_isPullback sq
    let a := twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    let φ := twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j') sq
    ((∀ Q : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow Q.obj →
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ↔
      ∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)) ∧
    ((∀ Q : quasiCoherentDerivedCategory Y,
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ↔
      ∀ K : quasiCoherentDerivedCategory Y, IsIso (φ.app K)) ∧
    ((∀ α : Type u, PreservesColimitsOfShape (Discrete α) a) →
      (∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)) → ∀ K : quasiCoherentDerivedCategory Y, IsIso (φ.app K))
```

**`Stacks.Duality.qcqs_twistedInverseImageRestrictionMap_isIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/RestrictionSupportUnconditional.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/RestrictionSupportUnconditional.lean#L57).

> Let `f : X ⟶ Y` be a morphism of quasi-compact quasi-separated schemes, `a` the right adjoint
> of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, `j : V ⟶ Y` the inclusion of a quasi-compact open and
> `j' : U ⟶ X` its base change, with `f' : U ⟶ V` and `a'` the right adjoint of `Rf'_*`. The
> transformation `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` is invertible by [Stacks, Tag 0A9K] (`j` is flat, so Tor
> independent from `f`). Writing `φ : (j')^* ∘ a ⟶ a' ∘ j^*` for the map of [Stacks, Tag 0A9L]:
> 1. `a` carries every `Q ∈ D^+_QCoh(𝒪_Y)` supported on `Y ∖ V` to an object supported on `X ∖ U` if
>    and only if `φ` is invertible on `D^+_QCoh(𝒪_Y)`;
> 2. the same holds with `D_QCoh(𝒪_Y)` in place of `D^+_QCoh(𝒪_Y)`;
> 3. if `a` commutes with direct sums, the conditions of (1) imply those of (2).
> "Supported on `Y ∖ V`" is "restricts to zero on `V`".

```lean
theorem qcqs_twistedInverseImageRestrictionMap_isIso_iff (sq : IsPullback j' f' f j) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : QuasiSeparatedSpace V := j.isOpenEmbedding.quasiSeparatedSpace
    haveI : QuasiSeparatedSpace U := j'.isOpenEmbedding.quasiSeparatedSpace
    haveI : CompactSpace U := compactSpace_of_isPullback sq
    haveI : IsIso (twistedInverseImagePushforwardBaseChange j' f' f j
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j) sq) :=
      isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq
        (torIndependent_of_flat_right f j)
    let a := twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    let φ := twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j') sq
    ((∀ Q : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow Q.obj →
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ↔
      ∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)) ∧
    ((∀ Q : quasiCoherentDerivedCategory Y,
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ↔
      ∀ K : quasiCoherentDerivedCategory Y, IsIso (φ.app K)) ∧
    ((∀ α : Type u, PreservesColimitsOfShape (Discrete α) a) →
      (∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)) → ∀ K : quasiCoherentDerivedCategory Y, IsIso (φ.app K))
```

## Tag 0A9P, a lemma

[Tag 0A9P](https://stacks.math.columbia.edu/tag/0A9P) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatRestriction.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatRestriction.lean#L73). The attribute's comment: “(1): f flat and of finite presentation”.

> Let `Y` be a quasi-compact and quasi-separated scheme, `f : X ⟶ Y` a proper, flat morphism of
> finite presentation, and `j : V ⟶ Y` a quasi-compact open immersion with base change
> `j' : U ⟶ X`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of [Stacks, Tag 0A9L] is invertible on
> `D^+_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageRestrictionMap_app_of_flat (sq : IsPullback j' f' f j)
    (K : quasiCoherentDerivedCategory Y) (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : CompactSpace V := QuasiCompact.compactSpace_of_compactSpace j
    haveI : CompactSpace U := compactSpace_of_isPullback sq
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : QuasiSeparatedSpace V := j.isOpenEmbedding.quasiSeparatedSpace
    haveI : QuasiSeparatedSpace U := j'.isOpenEmbedding.quasiSeparatedSpace
    IsIso ((twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j')
      sq).app K)
```

**`Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestriction.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestriction.lean#L276). The attribute's comment: “(2): Y Noetherian”.

> **[Stacks, Tag 0A9P] (2).** Let `Y` be Noetherian, `f : X ⟶ Y` proper and `j : V ⟶ Y` an open
> immersion with base change `j' : U ⟶ X`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of [Stacks, Tag 0A9L]
> is invertible on `D^+_QCoh(𝒪_Y)`. Part (1) is
> `Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_flat`.

```lean
theorem isIso_twistedInverseImageRestrictionMap_app_of_isProper (sq : IsPullback j' f' f j)
    (K : quasiCoherentDerivedCategory Y) (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI := isNoetherian_of_isProper f
    haveI : IsProper f' := MorphismProperty.of_isPullback sq inferInstance
    haveI := isNoetherian_of_isOpenImmersion j
    haveI := isNoetherian_of_isProper f'
    IsIso ((twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j')
      sq).app K)
```

**`Stacks.Duality.restrictionSupport_and_isIso_twistedInverseImageRestrictionMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestrictionUnconditional.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestrictionUnconditional.lean#L64). The attribute's comment: “(1)”.

> **[Stacks, Tag 0A9P] (1).** Let `Y` be a quasi-compact quasi-separated scheme, `f : X ⟶ Y` a
> proper, flat morphism of finite presentation, `j : V ⟶ Y` the inclusion of a quasi-compact open and
> `j' : U ⟶ X` its base change, with `f' : U ⟶ V`; let `a`, `a'` be the right adjoints of `Rf_*`,
> `Rf'_*` on `D_QCoh`. With `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` invertible by [Stacks, Tag 0A9K], the
> equivalent conditions of [Stacks, Tag 0A9N] (1) hold: `a` carries every `Q ∈ D^+_QCoh(𝒪_Y)`
> supported on `Y ∖ V` to an object supported on `X ∖ U`, and the map `φ : (j')^* ∘ a ⟶ a' ∘ j^*`
> of [Stacks, Tag 0A9L] is invertible on `D^+_QCoh(𝒪_Y)`.

```lean
theorem restrictionSupport_and_isIso_twistedInverseImageRestrictionMap_of_flat
    (sq : IsPullback j' f' f j) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : CompactSpace U := compactSpace_of_isPullback sq
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : QuasiSeparatedSpace V := j.isOpenEmbedding.quasiSeparatedSpace
    haveI : QuasiSeparatedSpace U := j'.isOpenEmbedding.quasiSeparatedSpace
    haveI : IsIso (twistedInverseImagePushforwardBaseChange j' f' f j
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j) sq) :=
      isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq
        (torIndependent_of_flat_right f j)
    let a := twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    let φ := twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j') sq
    (∀ Q : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow Q.obj →
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ∧
      ∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)
```

**`Stacks.Duality.restrictionSupport_and_isIso_twistedInverseImageRestrictionMap_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestrictionUnconditional.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperRestrictionUnconditional.lean#L110). The attribute's comment: “(2)”.

> **[Stacks, Tag 0A9P] (2).** Let `Y` be a Noetherian scheme, `f : X ⟶ Y` a proper morphism,
> `j : V ⟶ Y` the inclusion of an open (quasi-compact, as `Y` is Noetherian) and `j' : U ⟶ X` its
> base change, with `f' : U ⟶ V`; let `a`, `a'` be the right adjoints of `Rf_*`, `Rf'_*` on
> `D_QCoh`. With `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` invertible by [Stacks, Tag 0A9K], the equivalent
> conditions of [Stacks, Tag 0A9N] (1) hold: `a` carries every `Q ∈ D^+_QCoh(𝒪_Y)` supported on
> `Y ∖ V` to an object supported on `X ∖ U`, and the map `φ : (j')^* ∘ a ⟶ a' ∘ j^*` of
> [Stacks, Tag 0A9L] is invertible on `D^+_QCoh(𝒪_Y)`.

```lean
theorem restrictionSupport_and_isIso_twistedInverseImageRestrictionMap_of_isNoetherian
    (sq : IsPullback j' f' f j) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI := isNoetherian_of_isProper f
    haveI : IsProper f' := MorphismProperty.of_isPullback sq inferInstance
    haveI := isNoetherian_of_isOpenImmersion j
    haveI := isNoetherian_of_isProper f'
    haveI : IsIso (twistedInverseImagePushforwardBaseChange j' f' f j
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs j) sq) :=
      isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq
        (torIndependent_of_flat_right f j)
    let a := twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    let φ := twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j') sq
    (∀ Q : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow Q.obj →
        IsZero ((derivedRestrict j).obj Q.obj) → IsZero ((derivedRestrict j').obj (a.obj Q).obj)) ∧
      ∀ K : quasiCoherentDerivedCategory Y, DerivedCategoryB.IsBoundedBelow K.obj →
        IsIso (φ.app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.4, Tag 0E4G](https://stacks.math.columbia.edu/tag/0E4G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
