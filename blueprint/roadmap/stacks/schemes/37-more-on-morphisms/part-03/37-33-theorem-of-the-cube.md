---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasDescentLocus_of_flat_of_isProper, AlgebraicGeometry.exists_finiteLocallyFree_iso_of_fiberwiseFree_of_isReduced, AlgebraicGeometry.ValuativeTriviality.isTrivial_of_isTrivial_genericFiber, AlgebraicGeometry.IsDescentLocus.isClosedImmersion_hom_of_geometricallyIntegral, AlgebraicGeometry.exists_open_descendsFromBase_iff, AlgebraicGeometry.IsDescentLocus.exists_factorsThrough_iff_forall_of_injective_H1, AlgebraicGeometry.SheafOfModules.exists_isTrivial_on_open_of_isTrivial_faces, AlgebraicGeometry.SheafOfModules.isTrivial_of_isTrivial_faces_and_fiber
statement: formalized
proof: formalized
---

# 37.33 Theorem of the cube

Section 37.33 of the Stacks Project, [Tag 0BEZ](https://stacks.math.columbia.edu/tag/0BEZ). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BDP, a lemma

[Tag 0BDP](https://stacks.math.columbia.edu/tag/0BDP) in the Stacks Project.

**`AlgebraicGeometry.hasDescentLocus_of_flat_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusRepresentable.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusRepresentable.lean#L47).

> **Stacks Tag 0BDP.** Let `f : X ⟶ S` be a flat, proper morphism of finite presentation and
> `E` a finite locally free `𝒪_X`-module. Assume that `𝒪_T ⟶ p_*𝒪_{X_T}` is an isomorphism for
> every `g : T ⟶ S`, where `p : X_T = X ×_S T ⟶ T`. Then there is an immersion of finite
> presentation `j : Z ⟶ S` such that `g : T ⟶ S` factors through `Z` if and only if there is a
> finite locally free `𝒪_T`-module `N` with `p^*N ≅ q^*E`, `q : X_T ⟶ X` the projection.

```lean
theorem hasDescentLocus_of_flat_of_isProper {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [IsProper f]
    (hfp : FinitePresentation f)
    (hO : ∀ {T : Scheme.{u}} (g : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f g).toLRSHom.toShHom))
    (E : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [hE : SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] :
    HasDescentLocus f E
```

## Tag 0EX7, a lemma

[Tag 0EX7](https://stacks.math.columbia.edu/tag/0EX7) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteLocallyFree_iso_of_fiberwiseFree_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FiberwiseFreeReducedBaseUnconditional.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FiberwiseFreeReducedBaseUnconditional.lean#L42).

> **Stacks Tag 0EX7.** Let `f : X ⟶ S` be a flat, proper morphism of finite presentation such
> that `𝒪_S ⟶ f_*𝒪_X` is an isomorphism and remains so after arbitrary base change. Let `E` be a
> finite locally free `𝒪_X`-module such that (1) `E|_{X_s} ≅ 𝒪_{X_s}^{⊕ r_s}` for every `s ∈ S`,
> and (2) `S` is reduced. Then `E ≅ f^*N` for a finite locally free `𝒪_S`-module `N`.
>
> The descent locus of `E` exists by Stacks Tag 0BDP, `hasDescentLocus_of_flat_of_isProper`, which
> consumes the hypotheses on `f` and the finite local freeness of `E`.

```lean
theorem exists_finiteLocallyFree_iso_of_fiberwiseFree_of_isReduced {X S : Scheme.{u}}
    (f : X ⟶ S) [Flat f] [IsProper f] (hfp : FinitePresentation f)
    (hO : ∀ {T : Scheme.{u}} (g : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f g).toLRSHom.toShHom))
    (E : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    (hfiber : ∀ s : S, ∃ r : ℕ,
      Nonempty ((modulePullback
          (pullback.fst f (S.fromSpecResidueField s)).toLRSHom.toShHom).obj E ≅
        SheafOfModules.free (ULift.{u} (Fin r))))
    [IsReduced S] :
    ∃ N : SheafOfModules.{u} (structureSheafRing S.toRingedSpace),
      SheafOfModules.IsFiniteLocallyFree.{u, u, u} N ∧
        Nonempty ((modulePullback f.toLRSHom.toShHom).obj N ≅ E)
```

## Tag 0EX8, a lemma

[Tag 0EX8](https://stacks.math.columbia.edu/tag/0EX8) in the Stacks Project.

**`AlgebraicGeometry.ValuativeTriviality.isTrivial_of_isTrivial_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusValuationRing.lean, line 825](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusValuationRing.lean#L825).

> **[Stacks, Tag 0EX8].** Let `f : X ⟶ Spec A` be a proper flat
> morphism of finite presentation over a valuation ring `A` with fraction field `K`, and let `L` be
> an invertible `𝒪_X`-module. Assume that `L` is trivial on the generic fibre `X_K`, that the closed
> fibre is integral, and that `K = H⁰(X_K, 𝒪_{X_K})`. Then `L` is trivial.

```lean
theorem isTrivial_of_isTrivial_genericFiber
    [ValuationRing A] (K : Type u) [Field K] [Algebra A K] [IsFractionRing A K]
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (L : X.Modules) [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hgen : SheafOfModules.IsTrivial
      (pullback f (Spec.map (CommRingCat.ofHom (algebraMap A K)))).presheaf
      (pullback f (Spec.map (CommRingCat.ofHom (algebraMap A K)))).ringCatSheaf.2
      ((modulePullback (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap A K)))).toLRSHom.toShHom).obj L))
    [IsIntegral (f.fiber (IsLocalRing.closedPoint A))]
    (hΓ : Function.Bijective
      (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap A K)))).appTop.hom) :
    SheafOfModules.IsTrivial X.presheaf X.ringCatSheaf.2 L
```

## Tag 0BF0, a lemma

[Tag 0BF0](https://stacks.math.columbia.edu/tag/0BF0) in the Stacks Project.

**`AlgebraicGeometry.IsDescentLocus.isClosedImmersion_hom_of_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusClosedness.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusClosedness.lean#L167).

> **[Stacks, Tag 0BF0].** Let `f : X ⟶ S` be flat, proper and of finite
> presentation, with `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` an isomorphism for every base change `T ⟶ S`, let `E`
> be an invertible `𝒪_X`-module, and let the geometric fibres of `f` be integral (`hgeom`:
> `X ×_S Spec k` is integral for every algebraically closed field `k` and `Spec k ⟶ S`). Then every
> descent locus `Z` of `E` over `f` (Tag 0BDP) is closed in `S`: its structure morphism is a closed
> immersion.

```lean
theorem IsDescentLocus.isClosedImmersion_hom_of_geometricallyIntegral
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (hO : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f a).toLRSHom.toShHom))
    (E : X.Modules) [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 E]
    (hgeom : ∀ (k : Type u) [Field k] [IsAlgClosed k] (s : Spec (.of k) ⟶ S),
      IsIntegral (pullback f s))
    {Z : Over S} (hZ : IsDescentLocus f E Z) :
    IsClosedImmersion Z.hom
```

## Tag 0BF1, a lemma

[Tag 0BF1](https://stacks.math.columbia.edu/tag/0BF1) in the Stacks Project.

**`AlgebraicGeometry.exists_open_descendsFromBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentLocusComparison0BF1.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentLocusComparison0BF1.lean#L253).

> **Stacks Tag 0BF1.** Let `f : X ⟶ S` and `f' : X' ⟶ S` satisfy the hypotheses of
> [Stacks, Tag 0BDP] — flat, proper, of finite presentation, with `𝒪_T ⟶ p_* 𝒪_{X_T}` an
> isomorphism after every base change `T ⟶ S` — and let `i : X' ⟶ X` be a morphism over `S`, `L` an
> invertible `𝒪_X`-module and `L' = i^* L`. Let `s ∈ S` be a point of the descent locus `Z` of
> `(f, L)` at which `H¹(X_s, 𝒪) → H¹(X'_s, 𝒪)` is injective. Then `Z ∩ U = Z' ∩ U` for an open
> neighbourhood `U` of `s`, where `Z'` is the descent locus of `(f', L')`.
>
> **Rendering.** The locus `Z` of Tag 0BDP is the subscheme representing the descent condition
> `AlgebraicGeometry.DescendsFromBase f L` (a morphism `g : T ⟶ S` factors through `Z` exactly when
> `L` pulled back to `X ×_S T` comes from a finite locally free module on `T`), and likewise `Z'`
> for `(f', L')`. The statement is written through the functors these subschemes represent, which
> determine them: `s ∈ Z` is `DescendsFromBase f L (S.fromSpecResidueField s)`, and
> `Z ∩ U = Z' ∩ U` is the equivalence of the two descent conditions for every `g : T ⟶ S` with
> image in `U`. The fibre map `X'_s ⟶ X_s` is `pullback.map` of `i`, and the map on `H¹` is the
> pullback map of [Stacks, Tag 01FA] on the structure sheaf, read in `H¹(X'_s, 𝒪_{X'_s})` through
> the canonical `(X'_s ⟶ X_s)^* 𝒪_{X_s} ≅ 𝒪_{X'_s}`. The containment `Z ⊆ Z'` is
> `descendsFromBase_modulePullback_of_comp`; the same statement for given representing objects
> `Z`, `Z'` is `AlgebraicGeometry.IsDescentLocus.exists_open_factorsThrough_iff`.

```lean
theorem exists_open_descendsFromBase_iff {X X' S : Scheme.{u}} (f : X ⟶ S) (f' : X' ⟶ S)
    (i : X' ⟶ X) (hi : i ≫ f = f')
    [Flat f] [IsProper f] (hfp : FinitePresentation f)
    (hfO : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f a).toLRSHom.toShHom))
    [Flat f'] [IsProper f'] (hfp' : FinitePresentation f')
    (hfO' : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f' a).toLRSHom.toShHom))
    (L : X.Modules) [Stacks.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (s : S) (hs : DescendsFromBase f L (S.fromSpecResidueField s))
    (hH1 : Function.Injective (Stacks.Cohomology.moduleCohomologyPullbackMap
      (pullback.map f' (S.fromSpecResidueField s) f (S.fromSpecResidueField s) i (𝟙 _) (𝟙 _)
        (by rw [Category.comp_id, hi])
        (by rw [Category.comp_id, Category.id_comp])).toLRSHom.toShHom
      1 (SheafOfModules.unit (pullback f (S.fromSpecResidueField s)).ringCatSheaf) ≫
        (Stacks.Cohomology.moduleCohomologyAlong
          (pullback.map f' (S.fromSpecResidueField s) f (S.fromSpecResidueField s) i (𝟙 _) (𝟙 _)
            (by rw [Category.comp_id, hi])
            (by rw [Category.comp_id, Category.id_comp])).toLRSHom.toShHom 1).map
          (Scheme.Modules.pullbackUnitIso
            (pullback.map f' (S.fromSpecResidueField s) f (S.fromSpecResidueField s) i (𝟙 _)
              (𝟙 _) (by rw [Category.comp_id, hi])
              (by rw [Category.comp_id, Category.id_comp]))).hom)) :
    ∃ U : S.Opens, s ∈ U ∧ ∀ {T : Scheme.{u}} (g : T ⟶ S), Set.range g.base ⊆ U →
      (DescendsFromBase f L g ↔ DescendsFromBase f' ((Scheme.Modules.pullback i).obj L) g)
```

## Tag 0BF2, a lemma

[Tag 0BF2](https://stacks.math.columbia.edu/tag/0BF2) in the Stacks Project.

**`AlgebraicGeometry.IsDescentLocus.exists_factorsThrough_iff_forall_of_injective_H1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusIntersection.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DescentLocusIntersection.lean#L407).

> **[Stacks, Tag 0BF2].** Let `f : X ⟶ S` and the `i k ≫ f : Y k ⟶ S` (`k` in a finite type)
> be flat, proper and of finite presentation with `𝒪_T ⟶ p_{T,*}𝒪` an isomorphism after every base
> change `T ⟶ S`, the hypotheses of Tag 0BDP. Let `ℒ` be an invertible `𝒪_X`-module, `ℒ_k` its
> pullback to `Y k`, and `Z`, `Z_k` descent loci (Tag 0BDP) of `ℒ` over `f` and of `ℒ_k` over
> `i k ≫ f`. If `s ∈ Z` and `H¹(X_s, 𝒪) ⟶ ⊕_k H¹(Y_{k,s}, 𝒪)` is injective, then
> `Z ∩ U = (⋂_k Z_k) ∩ U` (scheme theoretic intersection) for an open neighbourhood `U` of `s`: a
> morphism `g : T ⟶ S` with image in `U` factors through `Z` if and only if it factors through every
> `Z_k`.
>
> `H¹(X_s, 𝒪)` is the degree-`1` cohomology of the `κ(s)`-linear derived global sections of
> `𝒪_{X_s}`, and the `k`-th component of the map is
> `Stacks.Cohomology.GlobalKunneth.sectionsPullbackMap` along the base change `Y_{k,s} ⟶ X_s` of
> `i k`.

```lean
theorem IsDescentLocus.exists_factorsThrough_iff_forall_of_injective_H1
    [Flat f] [IsProper f] (hfp : FinitePresentation f)
    (hO : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f a).toLRSHom.toShHom))
    {ι : Type u} [Finite ι] (Y : ι → Scheme.{u}) (i : ∀ k, Y k ⟶ X)
    (hflat : ∀ k, Flat (i k ≫ f)) (hprop : ∀ k, IsProper (i k ≫ f))
    (hfpk : ∀ k, FinitePresentation (i k ≫ f))
    (hOk : ∀ k {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd (i k ≫ f) a).toLRSHom.toShHom))
    (L : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [hL : IsInvertible X.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) X.IsSheaf) L]
    {Z : Over S} (hZ : IsDescentLocus f L Z) {Zk : ι → Over S}
    (hZk : ∀ k, IsDescentLocus (i k ≫ f) ((modulePullback (i k).toLRSHom.toShHom).obj L) (Zk k))
    (s : S) (hs : s ∈ Set.range Z.hom)
    (hinj : ∀ c : (DerivedCategory.homologyFunctor
          (ModuleCat.{u} (baseRing (Spec (S.residueField s)).toRingedSpace)) 1).obj
        ((sectionsOverBase (pullback.snd f (S.fromSpecResidueField s)).toLRSHom.toShHom).obj
          (DerivedCategory.Q.obj ((HomologicalComplex.single _ (ComplexShape.up ℤ) 0).obj
            (SheafOfModules.unit (structureSheafRing
              (pullback f (S.fromSpecResidueField s)).toRingedSpace))))),
      (∀ k, ((DerivedCategory.homologyFunctor _ 1).map
          (sectionsPullbackMap (pullback.snd f (S.fromSpecResidueField s)).toLRSHom.toShHom
            (pullback.map (i k ≫ f) (S.fromSpecResidueField s) f (S.fromSpecResidueField s)
              (i k) (𝟙 _) (𝟙 _) (by simp) (by simp)).toLRSHom.toShHom
            (DerivedCategory.Q.obj ((HomologicalComplex.single _ (ComplexShape.up ℤ) 0).obj
              (SheafOfModules.unit (structureSheafRing
                (pullback f (S.fromSpecResidueField s)).toRingedSpace)))))).hom c = 0) →
        c = 0) :
    ∃ U : S.Opens, s ∈ U ∧ ∀ {T : Scheme.{u}} (g : T ⟶ S), Set.range g ⊆ (U : Set S) →
      ((∃ h : T ⟶ Z.left, h ≫ Z.hom = g) ↔
        ∀ k, ∃ h : T ⟶ (Zk k).left, h ≫ (Zk k).hom = g)
```

## Tag 0BF3, a lemma

[Tag 0BF3](https://stacks.math.columbia.edu/tag/0BF3) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.exists_isTrivial_on_open_of_isTrivial_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentLocusTrivialityKunneth.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentLocusTrivialityKunneth.lean#L59).

> Let `f : X ⟶ S` and `g : Y ⟶ S` be flat, proper and of finite presentation with
> `𝒪_T ≅ f_{T,*}𝒪` and `𝒪_T ≅ g_{T,*}𝒪` after every base change, with sections `σ` of `f` and `τ`
> of `g`, and let `L` be invertible on `X ×_S Y`. If `L` is trivial on the two faces
> `(1, τ ∘ f) : X ⟶ X ×_S Y` and `(σ ∘ g, 1) : Y ⟶ X ×_S Y` and on the fibre over `s`, then `L` is
> trivial over `U ×_S (X ×_S Y)` for an open neighbourhood `U` of `s`.

```lean
theorem exists_isTrivial_on_open_of_isTrivial_faces
    {S X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    [Flat f] [IsProper f] (hfp : FinitePresentation f)
    (hfO : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd f a).toLRSHom.toShHom))
    [Flat g] [IsProper g] (hgp : FinitePresentation g)
    (hgO : ∀ {T : Scheme.{u}} (a : T ⟶ S),
      IsIso (structureSheafHom (pullback.snd g a).toLRSHom.toShHom))
    (σ : S ⟶ X) (hσ : σ ≫ f = 𝟙 S)
    (τ : S ⟶ Y) (hτ : τ ≫ g = 𝟙 S)
    (s : S)
    (L : _root_.SheafOfModules.{u} (structureSheafRing (pullback f g).toRingedSpace))
    [IsInvertible (pullback f g).presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
        (pullback f g).IsSheaf) L]
    (hfaceX :
      let i : X ⟶ pullback f g :=
        pullback.lift (𝟙 X) (f ≫ τ) (by simp [Category.assoc, hτ])
      IsTrivial X.presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) X.IsSheaf)
        ((modulePullback i.toLRSHom.toShHom).obj L))
    (hfaceY :
      let i : Y ⟶ pullback f g :=
        pullback.lift (g ≫ σ) (𝟙 Y) (by simp [Category.assoc, hσ])
      IsTrivial Y.presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) Y.IsSheaf)
        ((modulePullback i.toLRSHom.toShHom).obj L))
    (hfiber :
      let P := pullback f g
      let p : P ⟶ S := pullback.fst f g ≫ f
      let W := pullback p (S.fromSpecResidueField s)
      IsTrivial W.presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) W.IsSheaf)
        ((modulePullback (pullback.fst p (S.fromSpecResidueField s)).toLRSHom.toShHom).obj L)) :
    ∃ U : S.Opens, s ∈ U ∧
      (let P := pullback f g
       let p : P ⟶ S := pullback.fst f g ≫ f
       let W := pullback p U.ι
       IsTrivial W.presheaf
         (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) W.IsSheaf)
         ((modulePullback (pullback.fst p U.ι).toLRSHom.toShHom).obj L))
```

## Tag 0BF4, a theorem

[Tag 0BF4](https://stacks.math.columbia.edu/tag/0BF4) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.isTrivial_of_isTrivial_faces_and_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/TheoremOfTheCube0BF4.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/TheoremOfTheCube0BF4.lean#L46).

> **The theorem of the cube.** Let `f : X ⟶ S`, `g : Y ⟶ S` and `h : Z ⟶ S` be morphisms of
> schemes, with `f` and `g` flat, proper, of finite presentation and with geometrically integral
> fibres, let `x` and `y` be sections of `f` and `g`, and let `L` be an invertible module on
> `X ×_S Y ×_S Z` whose pullbacks along the faces `x × 1 × 1` and `1 × y × 1` are trivial and whose
> restriction to one fibre `X ×_S Y ×_S z` is trivial. If `Z` is connected, then `L` is trivial.
>
> The fibre over `z` is the base change of the projection `X ×_S Y ×_S Z ⟶ Z` along
> `Z.fromSpecResidueField z`.

```lean
theorem isTrivial_of_isTrivial_faces_and_fiber {S X Y Z : Scheme.{u}}
    (f : X ⟶ S) (g : Y ⟶ S) (h : Z ⟶ S)
    (x : S ⟶ X) (hx : x ≫ f = 𝟙 S) (y : S ⟶ Y) (hy : y ≫ g = 𝟙 S)
    [Flat f] [IsProper f] (hfp : FinitePresentation f) [GeometricallyIntegral f]
    [Flat g] [IsProper g] (hgp : FinitePresentation g) [GeometricallyIntegral g]
    [ConnectedSpace Z]
    (L : _root_.SheafOfModules.{u}
      (structureSheafRing (pullback (pullback.fst f g ≫ f) h).toRingedSpace))
    [IsInvertible (pullback (pullback.fst f g ≫ f) h).presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
        (pullback (pullback.fst f g ≫ f) h).IsSheaf) L]
    (hfaceX :
      let i : pullback g h ⟶ pullback (pullback.fst f g ≫ f) h :=
        pullback.lift
          (pullback.lift (pullback.fst g h ≫ g ≫ x) (pullback.fst g h)
            (by simp only [Category.assoc, hx, Category.comp_id]))
          (pullback.snd g h)
          (by rw [pullback.lift_fst_assoc]
              simp only [Category.assoc, hx, Category.comp_id, pullback.condition])
      IsTrivial (pullback g h).presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
          (pullback g h).IsSheaf)
        ((modulePullback i.toLRSHom.toShHom).obj L))
    (hfaceY :
      let i : pullback f h ⟶ pullback (pullback.fst f g ≫ f) h :=
        pullback.lift
          (pullback.lift (pullback.fst f h) (pullback.fst f h ≫ f ≫ y)
            (by simp only [Category.assoc, hy, Category.comp_id]))
          (pullback.snd f h)
          (by rw [pullback.lift_fst_assoc, pullback.condition])
      IsTrivial (pullback f h).presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
          (pullback f h).IsSheaf)
        ((modulePullback i.toLRSHom.toShHom).obj L))
    (hfiber : ∃ z : Z,
      IsTrivial (pullback (pullback.snd (pullback.fst f g ≫ f) h)
          (Z.fromSpecResidueField z)).presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
          (pullback (pullback.snd (pullback.fst f g ≫ f) h)
            (Z.fromSpecResidueField z)).IsSheaf)
        ((modulePullback (pullback.fst (pullback.snd (pullback.fst f g ≫ f) h)
          (Z.fromSpecResidueField z)).toLRSHom.toShHom).obj L)) :
    IsTrivial (pullback (pullback.fst f g ≫ f) h).presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
        (pullback (pullback.fst f g ≫ f) h).IsSheaf) L
```

**`AlgebraicGeometry.SheafOfModules.isTrivial_of_isTrivial_face_and_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/TheoremOfTheCube.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/TheoremOfTheCube.lean#L223). The attribute's comment: “assuming the conclusions of Tags 0BDP, 0BF0 and 0BF3 for the descent locus”.

> **The theorem of the cube.** Let `f : X ⟶ S`, `g : Y ⟶ S` and `h : Z ⟶ S` be morphisms of
> schemes, let `x` and `y` be sections of `f` and `g`, and let `L` be a sheaf of modules on
> `X ×_S Y ×_S Z` whose pullback along the face `x × 1 × 1` is trivial and whose restriction to one
> fibre `X ×_S Y ×_S z` is trivial. If `Z` is connected and `D` is a descent locus for `L` along the
> projection to `Z` which is a closed immersion and contains a neighbourhood of each of its points,
> then `L` is trivial.

```lean
theorem isTrivial_of_isTrivial_face_and_fiber {S X Y Z : Scheme.{u}} {D : Over Z}
    (f : X ⟶ S) (g : Y ⟶ S) (h : Z ⟶ S)
    (x : S ⟶ X) (hx : x ≫ f = 𝟙 S) (y : S ⟶ Y) (hy : y ≫ g = 𝟙 S) [ConnectedSpace Z]
    (L : _root_.SheafOfModules.{u}
      (structureSheafRing (pullback (pullback.fst f g ≫ f) h).toRingedSpace))
    (hD : IsDescentLocus (pullback.snd (pullback.fst f g ≫ f) h) L D)
    (hclosed : _root_.AlgebraicGeometry.IsClosedImmersion D.hom)
    (hnbhd : ∀ z ∈ Set.range D.hom, ∃ U : Z.Opens, z ∈ U ∧
      DescendsFromBase (pullback.snd (pullback.fst f g ≫ f) h) L U.ι)
    (hfaceX :
      let i : pullback g h ⟶ pullback (pullback.fst f g ≫ f) h :=
        pullback.lift
          (pullback.lift (pullback.fst g h ≫ g ≫ x) (pullback.fst g h)
            (by simp only [Category.assoc, hx, Category.comp_id]))
          (pullback.snd g h)
          (by rw [pullback.lift_fst_assoc]
              simp only [Category.assoc, hx, Category.comp_id, pullback.condition])
      IsTrivial (pullback g h).presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
          (pullback g h).IsSheaf)
        ((modulePullback i.toLRSHom.toShHom).obj L))
    (hfiber : ∃ z : Z,
      IsTrivial (pullback (pullback.snd (pullback.fst f g ≫ f) h)
          (Z.fromSpecResidueField z)).presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
          (pullback (pullback.snd (pullback.fst f g ≫ f) h)
            (Z.fromSpecResidueField z)).IsSheaf)
        ((modulePullback (pullback.fst (pullback.snd (pullback.fst f g ≫ f) h)
          (Z.fromSpecResidueField z)).toLRSHom.toShHom).obj L)) :
    IsTrivial (pullback (pullback.fst f g ≫ f) h).presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
        (pullback (pullback.fst f g ≫ f) h).IsSheaf) L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.33, Tag 0BEZ](https://stacks.math.columbia.edu/tag/0BEZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
