---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_affine_algebraization_of_isRigEtale, AlgebraicGeometry.FormalSpace.isEtale_of_isEtale_completionSheafMap, AlgebraicGeometry.FormalSpace.exists_etale_completion_factorization, AlgebraicGeometry.FormalSpace.exists_factorization_of_openComplement_and_completion, AlgebraicGeometry.FormalSpace.eq_of_eq_on_openComplement_of_eq_on_completion, AlgebraicGeometry.Space.eq_of_eq_on_compl_of_completionSubfunctorMap_eq, AlgebraicGeometry.FormalSpace.isEtaleEquivalenceRelation_of_openComplement_and_completion, AlgebraicGeometry.FormalSpace.exists_factorization_isIso_completionSheafMap
statement: formalized
proof: formalized
---

# 88.25 Completions and morphisms, I

Section 88.25 of the Stacks Project, [Tag 0GDP](https://stacks.math.columbia.edu/tag/0GDP). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AR4, a lemma

[Tag 0AR4](https://stacks.math.columbia.edu/tag/0AR4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_affine_algebraization_of_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineRigEtaleAlgebraization.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineRigEtaleAlgebraization.lean#L320).

> Let `X = Spec R` be a Noetherian affine scheme over `S` in the big fppf
> site, let `T ⊆ |X|` be closed, let `W` be a Noetherian affine formal algebraic space and let
> `g : W ⟶ X_{/T}` be rig-étale. Then there are an affine scheme `X'` and a morphism
> `f : X' ⟶ X` of finite type (locally of finite type and quasi-compact), étale at every point
> lying over `X ∖ T`, and an isomorphism `X'_{/f⁻¹T} ≅ W` compatible with `f_{/T}` and `g`.
> Moreover, if `g` is étale, that is representable by algebraic spaces and étale, then `f` is
> étale.

```lean
theorem exists_affine_algebraization_of_isRigEtale
    {R : Type u} [CommRing R] [IsNoetherianRing R] (hR : B.Contains (Spec (.of R)))
    (s : Spec (.of R) ⟶ S)
    (T : Set (Space.points B S hS (yoneda.obj (affineOver B S hS hR s)))) (hT : IsClosed T)
    {W : FppfSheaf B S hS} (hWaff : IsAffineFormalAlgebraicSpace B S hS W)
    (hWnoeth : IsNoetherian B S hS W)
    (g : W ⟶ Space.completionSheaf B S hS (yoneda.obj (affineOver B S hS hR s)) T)
    (hg : IsRigEtale B S hS g) :
    ∃ (X' : BigFppfOver B S hS) (_ : IsAffine ((BigFppfOver.toScheme B S hS).obj X'))
      (f : X' ⟶ affineOver B S hS hR s)
      (e : Space.completionSheaf B S hS (yoneda.obj X')
          (Space.pointsMap B S hS (yoneda.obj X') (yoneda.map f) ⁻¹' T) ≅ W),
      LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map f) ∧
      QuasiCompact ((BigFppfOver.toScheme B S hS).map f) ∧
      (∀ p : Space.points B S hS (yoneda.obj X'),
        Space.pointsMap B S hS (yoneda.obj X') (yoneda.map f) p ∉ T →
          EtaleAt ((BigFppfOver.toScheme B S hS).map f) (Space.pointsToScheme B S hS X' p)) ∧
      e.hom ≫ g = Space.completionSheafMap B S hS (yoneda.map f) T ∧
      (IsRepresentableEtale B S hS g → Etale ((BigFppfOver.toScheme B S hS).map f))
```

**`AlgebraicGeometry.FormalSpace.isEtale_of_isEtale_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtale.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtale.lean#L546). The attribute's comment: “the étale clause: a morphism locally of finite type which is étale away from `T` and whose completion `f_{/T}` is étale is étale everywhere, by Tag 0A43 (`AlgebraicGeometry.etaleAt_of_etale_infinitesimalNeighbourhoods`) above the closed subscheme cut out by `T`. Stated for `f` locally of finite type over a locally Noetherian `X`, where the source has `f` of finite type over an affine Noetherian `X`. The existence clause of the tag is not stated”.

> Let `f : X' ⟶ X` be a morphism of the big fppf site over `S` which is locally of finite
> type, let `X` be locally Noetherian, let `T` be a set of points of `X` and let `i : Z ⟶ X` be a
> closed subscheme whose set of points is `T`. If `f` is étale at every point of `X'` outside
> `|f|⁻¹ T` and the morphism of completions `f_{/T}` is étale, then `f` is étale.

```lean
theorem isEtale_of_isEtale_completionSheafMap
    {X' X : BigFppfOver B S hS} (f : X' ⟶ X)
    (T : Set (Space.points B S hS (yoneda.obj X)))
    {Z : Scheme.{u}} (i : Z ⟶ (BigFppfOver.toScheme B S hS).obj X)
    [IsClosedImmersion i]
    [_root_.AlgebraicGeometry.IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj X)]
    (hiT : Set.range i = Space.pointsToScheme B S hS X '' T)
    (hf : Space.IsLocallyOfFiniteType B S hS (yoneda.map f))
    (haway : ∀ p : Space.points B S hS (yoneda.obj X'),
      Space.pointsMap B S hS (yoneda.obj X') (yoneda.map f) p ∉ T →
        AlgebraicGeometry.EtaleAt ((BigFppfOver.toScheme B S hS).map f)
          (Space.pointsToScheme B S hS X' p))
    (hetale : ∃ hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.completionSheafMap B S hS (yoneda.map f) T).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun ⦃A C : Space.AlgebraicSpacesULift.{u + 1} B S hS⦄ (g : A ⟶ C) ↦
          Space.IsEtaleULift.{u + 1} B S hS g.hom)
        (Space.completionSheafMap B S hS (yoneda.map f) T).hom hrep) :
    Space.IsEtale B S hS (yoneda.map f)
```

## Tag 0AR3, a lemma

[Tag 0AR3](https://stacks.math.columbia.edu/tag/0AR3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_etale_completion_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionMorphismsAffine.lean, line 1355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionMorphismsAffine.lean#L1355).

> Let `X`, `X'`, `Y` be Noetherian affine schemes of the big fppf site over `S`, let `T ⊆ |X|`
> be closed, let `f : X' ⟶ X` be locally of finite type and étale over `X ∖ T`, let `h : Y ⟶ X` be
> a morphism and let `α : Y_{/T} ⟶ X'_{/T}` be a morphism over `X_{/T}`. Then there are an étale
> morphism `b : Y' ⟶ Y` of affine schemes inducing an isomorphism `b_{/T} : Y'_{/T} ⟶ Y_{/T}` and
> a morphism `a : Y' ⟶ X'` over `X` such that `α = a_{/T} ∘ b_{/T}⁻¹`.
>
> Here `g_{/T}` is the completion along `T`, `Space.completionOverFunctor`, which sends `g : V ⟶ X`
> to `V_{/g⁻¹T} ⟶ X_{/T}`.

```lean
theorem exists_etale_completion_factorization {X X' Y : BigFppfOver B S hS}
    [IsAffine ((BigFppfOver.toScheme B S hS).obj X)]
    [IsNoetherian ((BigFppfOver.toScheme B S hS).obj X)]
    [IsAffine ((BigFppfOver.toScheme B S hS).obj X')]
    [IsNoetherian ((BigFppfOver.toScheme B S hS).obj X')]
    [IsAffine ((BigFppfOver.toScheme B S hS).obj Y)]
    [IsNoetherian ((BigFppfOver.toScheme B S hS).obj Y)]
    (T : Set (Space.points B S hS (yoneda.obj X))) (T_closed : IsClosed T)
    (f : X' ⟶ X) [LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map f)]
    (hf : ∀ p : Space.points B S hS (yoneda.obj X'),
      Space.pointsMap B S hS (yoneda.obj X') (yoneda.map f) p ∉ T →
        EtaleAt ((BigFppfOver.toScheme B S hS).map f) (Space.pointsToScheme B S hS X' p))
    (h : Y ⟶ X)
    (α : (Space.completionOverFunctor B S hS T).obj (Over.mk (yoneda.map h)) ⟶
      (Space.completionOverFunctor B S hS T).obj (Over.mk (yoneda.map f))) :
    ∃ (Y' : BigFppfOver B S hS) (_ : IsAffine ((BigFppfOver.toScheme B S hS).obj Y'))
      (b : Y' ⟶ Y) (_ : Etale ((BigFppfOver.toScheme B S hS).map b))
      (a : Y' ⟶ X') (comm_ab : a ≫ f = b ≫ h)
      (_ : IsIso ((Space.completionOverFunctor B S hS T).map
        (Over.homMk (yoneda.map b) : Over.mk (yoneda.map b ≫ yoneda.map h) ⟶
          Over.mk (yoneda.map h)))),
      α = inv ((Space.completionOverFunctor B S hS T).map
          (Over.homMk (yoneda.map b) : Over.mk (yoneda.map b ≫ yoneda.map h) ⟶
            Over.mk (yoneda.map h))) ≫
        (Space.completionOverFunctor B S hS T).map
          (Over.homMk (yoneda.map a) (by simp only [Over.mk_hom, ← Functor.map_comp, comm_ab]) :
            Over.mk (yoneda.map b ≫ yoneda.map h) ⟶ Over.mk (yoneda.map f))
```

## Tag 0AR6, a lemma

[Tag 0AR6](https://stacks.math.columbia.edu/tag/0AR6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_factorization_of_openComplement_and_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFactorization.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFactorization.lean#L184). The attribute's comment: “the completion hypothesis is stated on the unsheafified subfunctor of sections with point-set image in `T` (`AlgebraicGeometry.Space.completionSubfunctor`), whose sheafification is the completion `X_{/T}` of Tag 0AMC by Tag 0AIZ, because the completion lands one universe above `Y` and so admits no morphism to `Y` in this library; no other hypothesis is carried”.

> **Stacks 0AR6.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of algebraic spaces over `S`
> and let `T ⊆ |X|` be closed. Assume that `X` is locally Noetherian, that `g` is a monomorphism
> and locally of finite type, that `f` restricted to the open complement of `T` factors through
> `g`, and that `f` factors through `g` on the subfunctor of sections with point-set image in
> `T`. Then `f` factors through `g`.
>
> The last hypothesis is the factorization on the completion `X_{/T}` of Stacks 0AMC, stated on
> the subfunctor whose sheafification that completion is by Stacks 0AIZ; see the module
> documentation.

```lean
theorem exists_factorization_of_openComplement_and_completion
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hXnoeth : Space.HasEtaleLocalProperty B S hS X
      (fun V : Scheme.{u} => IsLocallyNoetherian V))
    (hgmono : Mono g) (hgft : Space.IsLocallyOfFiniteType B S hS g)
    (hopen : ∃ v : ((Space.openSubspacesOrderIso B S hS X hX).symm
        ⟨Tᶜ, hT.isOpen_compl⟩).1.toFunctor ⟶ Z,
      v ≫ g = ((Space.openSubspacesOrderIso B S hS X hX).symm
        ⟨Tᶜ, hT.isOpen_compl⟩).1.ι ≫ f)
    (hcompletion : ∃ v : (Space.completionSubfunctor B S hS X T).toFunctor ⟶
        Z ⋙ uliftFunctor.{u + 1},
      v ≫ Functor.whiskerRight g uliftFunctor.{u + 1} =
        (Space.completionSubfunctor B S hS X T).ι ≫
          Functor.whiskerRight f uliftFunctor.{u + 1}) :
    ∃ v : X ⟶ Z, v ≫ g = f
```

## Tag 0GI1, a lemma

[Tag 0GI1](https://stacks.math.columbia.edu/tag/0GI1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.eq_of_eq_on_openComplement_of_eq_on_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismEqualityFromCompletion.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismEqualityFromCompletion.lean#L504).

> **Stacks 0GI1.** Let `X` and `W` be algebraic spaces over `S` with `X` locally Noetherian,
> let `T ⊆ |X|` be a closed subset and let `a, b : X ⟶ W` be morphisms over `S` which agree on
> the open subspace `X ∖ T` and whose completions along `T` agree. Then `a = b`.
>
> The equalizer `E` of `a` and `b` is an algebraic space whose projection `g : E ⟶ X` is a
> monomorphism locally of finite type — Stacks 03HK — and the two hypotheses factor
> `X ∖ T ⟶ X` and `X_{/T} ⟶ X` through `g`, so Stacks 0AR6 applied to `𝟙 X` and `g` gives a
> section `v` of `g`. Since `g ≫ a = g ≫ b` by construction, `a = v ≫ g ≫ a = v ≫ g ≫ b = b`.

```lean
theorem eq_of_eq_on_openComplement_of_eq_on_completion
    (hX : IsAlgebraicSpace B S hS X) (hW : IsAlgebraicSpace B S hS W)
    (hXnoeth : Space.HasEtaleLocalProperty B S hS X
      (fun V : Scheme.{u} => IsLocallyNoetherian V))
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) (a b : X ⟶ W)
    (hopen : (Space.openSubspaceOfPoints B S hS X Tᶜ).ι ≫ a =
      (Space.openSubspaceOfPoints B S hS X Tᶜ).ι ≫ b)
    (hcompletion :
      completionOfAlgebraicSpaceInclusion B S hS hX T ≫ upliftedMap B S hS hX hW a =
        completionOfAlgebraicSpaceInclusion B S hS hX T ≫ upliftedMap B S hS hX hW b) :
    a = b
```

## Tag 0AR7, a lemma

[Tag 0AR7](https://stacks.math.columbia.edu/tag/0AR7) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_eq_on_compl_of_completionSubfunctorMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismUniquenessAlongClosedSubset.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismUniquenessAlongClosedSubset.lean#L367).

> **Stacks 0AR7.** Let `X` and `Y` be locally Noetherian algebraic spaces over `S`, let
> `T ⊆ |X|` and `T' ⊆ |Y|` be closed subsets and let `a, b : X ⟶ Y` be morphisms with
> `|a| (T) ⊆ T'` and `|b| (T) ⊆ T'`. If `a` and `b` agree on the open subspace `X ∖ T` and the
> induced morphisms of completions `a_{/T}, b_{/T} : X_{/T} ⟶ Y_{/T'}` agree, then `a = b`.

```lean
theorem eq_of_eq_on_compl_of_completionSubfunctorMap_eq
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXnoeth : HasEtaleLocalProperty B S hS X (fun V : Scheme.{u} => IsLocallyNoetherian V))
    (_hYnoeth : HasEtaleLocalProperty B S hS Y (fun V : Scheme.{u} => IsLocallyNoetherian V))
    {T : Set (points B S hS X)} (hT : IsClosed T)
    {T' : Set (points B S hS Y)} (_hT' : IsClosed T')
    (a b : X ⟶ Y)
    (ha : pointsMap B S hS X a '' T ⊆ T') (hb : pointsMap B S hS X b '' T ⊆ T')
    (hcompl :
      (openSubspaceOfPoints B S hS X Tᶜ).ι ≫ a = (openSubspaceOfPoints B S hS X Tᶜ).ι ≫ b)
    (hcompletion : completionSubfunctorMap B S hS a T T' ha =
      completionSubfunctorMap B S hS b T T' hb) :
    a = b
```

## Tag 0AR8, a lemma

[Tag 0AR8](https://stacks.math.columbia.edu/tag/0AR8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEtaleEquivalenceRelation_of_openComplement_and_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EquivalenceRelationFromCompletion.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EquivalenceRelationFromCompletion.lean#L1158). The attribute's comment: “WHAT IS FORMALIZED: hypothesis (3) is read as saying that the formal completion `(t_{/T}, s_{/T})` is an *étale* equivalence relation — an equivalence relation whose two maps `s_{/T}` and `t_{/T}` are étale — and not merely an equivalence relation. THE LITERAL READING OF (3) IS FALSE: take `X = Spec k` and `T = |X|`, so that `X ∖ T` is empty and (2) is vacuous, and `U = 𝔸¹`, `R = U ×_X U`, `t = pr₀`, `s = pr₁`; then `X_{/T} = X`, `U_{/T} = U`, `R_{/T} = R`, so (3) says that the identity is an equivalence relation, (1) and (2) hold, and yet `s = pr₁ : 𝔸¹ × 𝔸¹ ⟶ 𝔸¹` is not étale, so the conclusion fails. THE ÉTALE READING IS THE ONE THE SOURCE'S OWN PROOF USES: "Since the formal completions of the maps `s`, `t` are étale, we see that `s` and `t` are étale for example by More on Morphisms, Lemma 37.12.3". Otherwise the statement is the tag's: hypothesis (2) is read as the restrictions of `s` and `t` to the subspaces cut out by the complements of the inverse images of `T`, which is the base change to `X ∖ T` by `AlgebraicGeometry.FormalSpace.isPullback_ι_openSubspaceOfPoints_compl`, and (3) as the restriction morphisms of the completions of Tag 0AMC along those inverse images. No further hypothesis is added and no part of the conclusion is dropped: the conclusion carries monomorphy of `(t, s)`, the equivalence-relation structure, and étaleness of both `s` and `t`”.

> Let `S` be a scheme, let `X` be a locally Noetherian algebraic space over
> `S`, let `T ⊆ |X|` be a closed subset and let `s, t : R ⟶ U` be two morphisms of algebraic
> spaces over `X`. Assume
>
> 1. `R` and `U` are locally of finite type over `X`,
> 2. the base change of `s` and `t` to `X ∖ T` is an étale equivalence relation, and
> 3. the formal completion `(t_{/T}, s_{/T}) : R_{/T} ⟶ U_{/T} ×_{X_{/T}} U_{/T}` is an étale
>    equivalence relation.
>
> Then `(t, s) : R ⟶ U ×_X U` is an étale equivalence relation: it is a monomorphism, `t` and `s`
> form an equivalence relation, and both are étale.

```lean
theorem isEtaleEquivalenceRelation_of_openComplement_and_completion
    (hX : IsAlgebraicSpace B S hS X) (hR : IsAlgebraicSpace B S hS R)
    (hU : IsAlgebraicSpace B S hS U)
    (qR : R ⟶ X) (qU : U ⟶ X) (s t : R ⟶ U)
    (hs : s ≫ qU = qR) (ht : t ≫ qU = qR)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hXnoeth : Space.HasEtaleLocalProperty B S hS X
      (fun V : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian V))
    (hqR : Space.IsLocallyOfFiniteType B S hS qR)
    (hqU : Space.IsLocallyOfFiniteType B S hS qU)
    (hopen : IsEquivalenceRelation
      (Space.openSubspaceOfPointsRestrict B S hS t _ _
        (compl_subset_preimage_compl B S hS t qU qR ht T))
      (Space.openSubspaceOfPointsRestrict B S hS s _ _
        (compl_subset_preimage_compl B S hS s qU qR hs T)))
    (hopent : Space.IsEtale B S hS (Space.openSubspaceOfPointsRestrict B S hS t _ _
      (compl_subset_preimage_compl B S hS t qU qR ht T)))
    (hopens : Space.IsEtale B S hS (Space.openSubspaceOfPointsRestrict B S hS s _ _
      (compl_subset_preimage_compl B S hS s qU qR hs T)))
    (hcompletion : IsEquivalenceRelation
      (Space.completionSheafRestrict B S hS t _ _
        (preimage_subset_preimage_of_comp B S hS t qU qR ht T))
      (Space.completionSheafRestrict B S hS s _ _
        (preimage_subset_preimage_of_comp B S hS s qU qR hs T)))
    (hcomplt : ∃ hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.completionSheafMap B S hS t (Space.pointsMap B S hS U qU ⁻¹' T)).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun ⦃A C : Space.AlgebraicSpacesULift.{u + 1} B S hS⦄ (g : A ⟶ C) ↦
          Space.IsEtaleULift.{u + 1} B S hS g.hom)
        (Space.completionSheafMap B S hS t (Space.pointsMap B S hS U qU ⁻¹' T)).hom hrep)
    (hcompls : ∃ hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.completionSheafMap B S hS s (Space.pointsMap B S hS U qU ⁻¹' T)).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun ⦃A C : Space.AlgebraicSpacesULift.{u + 1} B S hS⦄ (g : A ⟶ C) ↦
          Space.IsEtaleULift.{u + 1} B S hS g.hom)
        (Space.completionSheafMap B S hS s (Space.pointsMap B S hS U qU ⁻¹' T)).hom hrep) :
    Mono (relationMap B S hS qU s t (ht.trans hs.symm)) ∧ IsEquivalenceRelation t s ∧
      Space.IsEtale B S hS s ∧ Space.IsEtale B S hS t
```

## Tag 0AR9, a lemma

[Tag 0AR9](https://stacks.math.columbia.edu/tag/0AR9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_factorization_isIso_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleAwayFromClosedFactorization.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleAwayFromClosedFactorization.lean#L183).

> Let `X` be an algebraic space over `S`, let `T ⊆ |X|` be closed with open
> complement `U = X ∖ T`, and let `f : X' ⟶ X` be a morphism of algebraic spaces which is locally
> of finite type and étale over `U`. Then `f` factors as `X' ⟶ X'' ⟶ X` where `X'' ⟶ X` is locally
> of finite type and an isomorphism over `U`, and `X' ⟶ X''` induces an isomorphism
> `X'_{/T} ⟶ X''_{/T}` of completions.
>
> Here `U` is the open subspace with point set `Tᶜ`, and "over `U`" is the base change along its
> inclusion.

```lean
theorem exists_factorization_isIso_completionSheafMap
    {X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hX' : IsAlgebraicSpace B S hS X')
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (f : X' ⟶ X) (hf : Space.IsLocallyOfFiniteType B S hS f)
    (hfU : Space.IsEtale B S hS (pullback.snd f
      ((Space.openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)) :
    ∃ (X'' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS X'')
      (g : X' ⟶ X'') (p : X'' ⟶ X),
      g ≫ p = f ∧ Space.IsLocallyOfFiniteType B S hS p ∧
        IsIso (pullback.snd p
          ((Space.openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι) ∧
        IsIso (Space.completionSheafMap B S hS g (Space.pointsMap B S hS X'' p ⁻¹' T))
```

**`AlgebraicGeometry.FormalSpace.exists_factorization_of_isEtale_openComplementRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleOutsideFactorization.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleOutsideFactorization.lean#L448). The attribute's comment: “stated without the hypothesis that X be locally Noetherian, which the source's proof does not use; X'' ⟶ X is an isomorphism over U in the form that its base change to the open subspace with point set |X| ∖ T is an isomorphism, and the completions are the completionSheafMap of Section 0GDB”.

> **Stacks 0AR9.** Let `S` be a scheme contained in a big fppf site `B`, let `X` be an algebraic
> space over `S` and let `T ⊆ |X|` be closed. Let `f : X' ⟶ X` be a morphism of algebraic spaces
> which is locally of finite type and étale outside of `T`, i.e. whose restriction
> `U' = f⁻¹U ⟶ U` to the open subspace `U` with `|U| = |X| ∖ T` is étale. Then `f` factors as
> `X' ⟶ X'' ⟶ X` where
>
> * `X''` is an algebraic space and `X'' ⟶ X` is locally of finite type,
> * `X'' ⟶ X` is an isomorphism over `U`: its base change to `U` is an isomorphism, and
> * `X'_{/T} ⟶ X''_{/T}` is an isomorphism, the completion of `X' ⟶ X''` along the inverse image
>   of `T` in the sense of Section 0GDB, `AlgebraicGeometry.Space.completionSheafMap`.
>
> The source assumes moreover that `X` is locally Noetherian; its proof does not use that
> hypothesis, so it is dropped here.

```lean
theorem exists_factorization_of_isEtale_openComplementRestriction
    {X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hX' : IsAlgebraicSpace B S hS X') (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (f : X' ⟶ X) (hft : Space.IsLocallyOfFiniteType B S hS f)
    (het : Space.IsEtale B S hS (Space.openComplementRestriction B S hS f T)) :
    ∃ (X'' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS X'')
      (g : X' ⟶ X'') (h : X'' ⟶ X), g ≫ h = f ∧ Space.IsLocallyOfFiniteType B S hS h ∧
        IsIso (pullback.snd h (Space.openSubspaceOfPoints B S hS X Tᶜ).ι) ∧
        IsIso (Space.completionSheafMap B S hS g (Space.pointsMap B S hS X'' h ⁻¹' T))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.25, Tag 0GDP](https://stacks.math.columbia.edu/tag/0GDP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
