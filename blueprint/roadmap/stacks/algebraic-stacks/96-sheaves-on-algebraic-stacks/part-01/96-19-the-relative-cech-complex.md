---
declaration: section
origin: cited
lean: Stacks.RelativeCech.complex, Stacks.presheafPullbackMap, Stacks.presheafPullbackMap_natural, Stacks.presheafPullbackMap_whiskerLeft_ranCounit, Stacks.RelativeCech.reindexMap_eq_presheafPullbackMap, Stacks.sheafPullbackMap, Stacks.sheafPullbackMap_hom, Stacks.sheafPullbackMap_natural
statement: formalized
proof: formalized
---

# 96.19 The relative Čech complex

Section 96.19 of the Stacks Project, [Tag 06X7](https://stacks.math.columbia.edu/tag/06X7). 12 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06X8, a remark

[Tag 06X8](https://stacks.math.columbia.edu/tag/06X8) in the Stacks Project.

**`Stacks.RelativeCech.complex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RelativeCechComplex.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RelativeCechComplex.lean#L221). The attribute's comment: “presheaf_relative_cech_complex”.

> **Stacks 06X8.** The relative Čech complex of an abelian presheaf for a functor over a
> base category: the alternating-coface complex of the relative Čech cosimplicial presheaf.

```lean
public noncomputable def complex (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX w}) :
    CochainComplex (Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX w}) ℕ
```

**`Stacks.presheafPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L83). The attribute's comment: “the pullback map on presheaf direct images”.

> **Stacks 06X8.** The canonical map from the direct image of a presheaf along `f` to the
> direct image along `h ⋙ f` of its restriction along `h`: the direct image of the adjunction
> unit for `h`, followed by the comparison from iterated direct image to direct image along the
> composite.

```lean
public noncomputable def presheafPullbackMap (G : Uᵒᵖ ⥤ A) :
    f.op.ran.obj G ⟶ (h.op ⋙ f.op).ran.obj (h.op ⋙ G)
```

**`Stacks.presheafPullbackMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L90). The attribute's comment: “naturality of the pullback map on presheaf direct images”.

> **Stacks 06X8.** The presheaf pullback map is natural in the presheaf.

```lean
public theorem presheafPullbackMap_natural {G H : Uᵒᵖ ⥤ A} (α : G ⟶ H) :
    f.op.ran.map α ≫ presheafPullbackMap f h H =
      presheafPullbackMap f h G ≫
        (h.op ⋙ f.op).ran.map (Functor.whiskerLeft h.op α)
```

**`Stacks.presheafPullbackMap_whiskerLeft_ranCounit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L151). The attribute's comment: “the counit factorisation of the presheaf pullback map”.

> **Stacks 06X8.** The defining property of the presheaf pullback map against the
> Kan-extension counits: restricting the counit of `f` along `h` factors through it.

```lean
public theorem presheafPullbackMap_whiskerLeft_ranCounit (G : Xᵒᵖ ⥤ A) :
    Functor.whiskerLeft h.op (f.op.ranCounit.app (f.op ⋙ G)) =
      Functor.whiskerLeft (h.op ⋙ f.op) (presheafPullbackMap f h (f.op ⋙ G)) ≫
        (h.op ⋙ f.op).ranCounit.app (h.op ⋙ f.op ⋙ G)
```

**`Stacks.RelativeCech.reindexMap_eq_presheafPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L190). The attribute's comment: “the Čech reindexing maps are pullback maps”.

> **Stacks 06X8.** Each reindexing map of the relative Čech complex of an abelian presheaf is
> the canonical pullback map along the corresponding reindexing functor of relative Čech
> tuples.

```lean
public theorem reindexMap_eq_presheafPullbackMap {U : Type uU} {X : Type uX} {C : Type uC}
    [Category.{vU} U] [Category.{vX} X] [Category.{vC} C] (p : X ⥤ C) (f : U ⥤ X)
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX vU vC w}) {m n : ℕ} (φ : ⦋m⦌ ⟶ ⦋n⦌) :
    reindexMap.{vU, vX, vC, uU, uX, uC, max vU vC w} p f F φ =
      presheafPullbackMap (Tuple.projection p f m)
        (Tuple.reindex p f φ.toOrderHom) ((Tuple.projection p f m).op ⋙ F)
```

**`Stacks.sheafPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L226). The attribute's comment: “the pullback map on sheaf direct images”.

> **Stacks 06X8.** The canonical map from the direct image of a sheaf along `f` to the direct
> image along `h ⋙ f` of its restriction along `h`, formed from the unit of the
> restriction/direct-image adjunction for `h` and the direct-image compositor.

```lean
public noncomputable def sheafPullbackMap (G : Sheaf K A) :
    letI := isCocontinuous_comp h f J K (L := L)
    (f.sheafPushforwardCocontinuous A K L).obj G ⟶
      ((h ⋙ f).sheafPushforwardCocontinuous A J L).obj
        ((h.sheafPushforwardContinuous A J K).obj G)
```

**`Stacks.sheafPullbackMap_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L240). The attribute's comment: “agreement of the sheaf and presheaf pullback maps”.

> **Stacks 06X8.** The underlying presheaf morphism of the sheaf pullback map is the presheaf
> pullback map.

```lean
public theorem sheafPullbackMap_hom (G : Sheaf K A) :
    letI : ∀ P : Vᵒᵖ ⥤ A, (h.op ⋙ f.op).HasRightKanExtension P :=
      fun P => inferInstanceAs ((h ⋙ f).op.HasRightKanExtension P)
    (sheafPullbackMap J K L f h G).hom = presheafPullbackMap f h G.obj
```

**`Stacks.sheafPullbackMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PullbackMap.lean#L255). The attribute's comment: “naturality of the pullback map on sheaf direct images”.

> **Stacks 06X8.** The sheaf pullback map is natural in the sheaf.

```lean
public theorem sheafPullbackMap_natural {G H : Sheaf K A} (α : G ⟶ H) :
    letI := isCocontinuous_comp h f J K (L := L)
    (f.sheafPushforwardCocontinuous A K L).map α ≫ sheafPullbackMap J K L f h H =
      sheafPullbackMap J K L f h G ≫
        ((h ⋙ f).sheafPushforwardCocontinuous A J L).map
          ((h.sheafPushforwardContinuous A J K).map α)
```

## Tag 06X9, a lemma

[Tag 06X9](https://stacks.math.columbia.edu/tag/06X9) in the Stacks Project.

**`Stacks.RelativeCech.baseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean#L249). The attribute's comment: “part (1)”.

> **Stacks 06X9, part (1).** The canonical comparison is assembled from the
> right-Kan-extension adjunction in each Čech degree.

```lean
public noncomputable def baseChangeMap
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX uV uY vY w}) :
    (((Functor.whiskeringLeft Yᵒᵖ Xᵒᵖ
      AddCommGrpCat.{max uU uX vX uV uY vY w}).obj e.op).mapHomologicalComplex
        (ComplexShape.up ℕ)).obj
        (complex.{vU, vX, vC, uU, uX, uC, max uV uY vY w} pX f F) ⟶
      complex.{vV, vY, vC, uV, uY, uC, max uU uX vX w}
        (e ⋙ pX) g (e.op ⋙ F)
```

**`Stacks.RelativeCech.isIso_baseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean#L264). The attribute's comment: “part (2)”.

> **Stacks 06X9, part (2).** If the two horizontal 1-morphisms `h` and `e` of the
> square are equivalences, then the base-change morphism of part (1) is an
> isomorphism of complexes of abelian presheaves.

```lean
public theorem isIso_baseChangeMap
    [h.IsEquivalence] [e.IsEquivalence]
    (hpV : (g ⋙ e ⋙ pX).IsFiberedInGroupoids)
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX uV uY vY w}) :
    IsIso (baseChangeMap pX f e g h α hα F)
```

**`Stacks.RelativeCech.nonempty_complexIso_of_natIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeGeneralities.lean#L278). The attribute's comment: “part (3)”.

> **Stacks 06X9, part (3).** 2-isomorphic 1-morphisms `f, f' : 𝒰 ⟶ 𝒳` over the
> base have isomorphic relative Čech complexes.

```lean
public theorem nonempty_complexIso_of_natIso
    {C : Type uC} {X : Type uX} {U : Type uU} [Category.{vC} C] [Category.{vX} X]
    [Category.{vU} U] (pX : X ⥤ C) (f f' : U ⥤ X) (β : f ≅ f')
    (hβ : ∀ u : U, pX.IsHomLift (𝟙 (pX.obj (f.obj u))) (β.hom.app u))
    (hpU' : (f' ⋙ pX).IsFiberedInGroupoids)
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX w}) :
    Nonempty (complex pX f F ≅ complex pX f' F)
```

## Tag 06XA, a lemma

[Tag 06XA](https://stacks.math.columbia.edu/tag/06XA) in the Stacks Project.

**`Stacks.RelativeCech.nonempty_homotopy_extendedSheafComplex_id_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeHomotopy.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeHomotopy.lean#L639).

> **Stacks 06XA.** If there is a `1`-morphism `s : 𝒳 ⥤ 𝒰` such that `f ∘ s` is `2`-isomorphic
> to `id_𝒳` by a vertical `2`-isomorphism, then the extended relative Čech complex is homotopic to
> zero: its identity is homotopic to its zero endomorphism.

```lean
public theorem nonempty_homotopy_extendedSheafComplex_id_zero
    (s : 𝒳 ⥤ 𝒰) (α : s ⋙ f ≅ 𝟭 𝒳)
    (hα : ∀ x : 𝒳, q.IsHomLift (𝟙 (q.obj x)) (α.hom.app x)) :
    Nonempty (Homotopy
      (𝟙 (extendedSheafComplex.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕)) 0)
```

## Tag 06XB, a remark

[Tag 06XB](https://stacks.math.columbia.edu/tag/06XB) in the Stacks Project.

**`Stacks.RelativeCech.nerveBaseChangeEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L479). The attribute's comment: “equivalence of Čech nerves”.

> The Čech nerve of the base change of `f` to the slice over `p(x)` is, in each degree, the base
> change of the Čech nerve of `f`.

```lean
public def nerveBaseChangeEquivalence (p : X ⥤ C) (f : U ⥤ X) (c : p.ChoiceOfPullbacks)
    {V : C} (x : p.Fiber V) (n : ℕ) :
    Tuple (Over.forget V)
        (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f) n ≌
      TwoFibreProductOver (Over.forget V) (Tuple.projection p f n ⋙ p) p
        (c.sliceFunctor x) (Tuple.projection p f n)
```

**`Stacks.RelativeCech.nerveBaseChangeEquivalence_functor_comp_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L490). The attribute's comment: “equivalence of Čech nerves”.

> The first projection of the base change of the Čech nerve corresponds, under the equivalence,
> to the projection of the Čech nerve of the base change.

```lean
public theorem nerveBaseChangeEquivalence_functor_comp_fst (p : X ⥤ C) (f : U ⥤ X)
    (c : p.ChoiceOfPullbacks) {V : C} (x : p.Fiber V) (n : ℕ) :
    (nerveBaseChangeEquivalence p f c x n).functor ⋙
        TwoFibreProductOver.fst (Over.forget V) (Tuple.projection p f n ⋙ p) p
          (c.sliceFunctor x) (Tuple.projection p f n) =
      Tuple.projection (Over.forget V)
        (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f) n
```

**`Stacks.RelativeCech.nerveBaseChangeEquivalence_functor_comp_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L502). The attribute's comment: “equivalence of Čech nerves”.

> The second projection of the base change of the Čech nerve corresponds, under the equivalence,
> to the `1`-morphism of Čech nerves of `Stacks.Cech.nerveMap`.

```lean
public theorem nerveBaseChangeEquivalence_functor_comp_snd (p : X ⥤ C) (f : U ⥤ X)
    (c : p.ChoiceOfPullbacks) {V : C} (x : p.Fiber V) (n : ℕ) :
    (nerveBaseChangeEquivalence p f c x n).functor ⋙
        TwoFibreProductOver.snd (Over.forget V) (Tuple.projection p f n ⋙ p) p
          (c.sliceFunctor x) (Tuple.projection p f n) =
      Cech.nerveMap p (Over.forget V) f
        (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f)
        (TwoFibreProductOver.snd (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f)
        (c.sliceFunctor x)
        (TwoFibreProductOver.psiIso (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f).symm
        (c.sliceFunctor_comp x)
        (isHomLift_psi_inv (Over.forget V) p (c.sliceFunctor x) f) n
```

**`Stacks.RelativeCech.complexSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 663](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L663). The attribute's comment: “isomorphism of complexes”.

> The value at an object `x` of `𝒳` of the relative Čech complex of `f` is canonically the Čech
> complex of the base change of `f` to the slice `𝒞/p(x)`, which represents `x`. This is an
> isomorphism of complexes: it is compatible with the Čech differentials.

```lean
public def complexSectionsIso (p : X ⥤ C) (f : U ⥤ X) (hp : p.IsFiberedInGroupoids)
    (c : p.ChoiceOfPullbacks) {V : C} (x : p.Fiber V)
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX uC vU vX vC w}) :
    (((evaluation Xᵒᵖ AddCommGrpCat.{max uU uX uC vU vX vC w}).obj
          (op x.1)).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        (complex.{vU, vX, vC, uU, uX, uC, max uC vC vU w} p f F) ≅
      Cech.complex (Over.forget V)
        (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f)
        ((c.sliceFunctor x).op ⋙ F)
```

**`Stacks.RelativeCech.complexSectionsIso_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L695). The attribute's comment: “componentwise identification”.

> On a Čech tuple of the base-changed covering, the identification of complexes restricts a
> relative section along the chosen pullback comparison of the tuple's target and then applies the
> right-Kan-extension counit.

```lean
public theorem complexSectionsIso_π (p : X ⥤ C) (f : U ⥤ X) (hp : p.IsFiberedInGroupoids)
    (c : p.ChoiceOfPullbacks) {V : C} (x : p.Fiber V)
    (F : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX uC vU vX vC w}) (n : ℕ)
    (a : Tuple (Over.forget V)
      (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f) n)
    (s : (term.{vU, vX, vC, uU, uX, uC, max uC vC vU w} p f F n).obj (op x.1)) :
    ((complexSectionsIso p f hp c x F).hom.f n ≫
        limit.π ((Tuple.projection (Over.forget V)
          (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f) n).op ⋙
            (c.sliceFunctor x).op ⋙ F) (op a)) s =
      ((Tuple.projection p f n).op.ranCounit.app ((Tuple.projection p f n).op ⋙ F)).app
          (op ((Cech.nerveMap p (Over.forget V) f
            (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f)
            (TwoFibreProductOver.snd (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f)
            (c.sliceFunctor x)
            (TwoFibreProductOver.psiIso (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f).symm
            (c.sliceFunctor_comp x)
            (isHomLift_psi_inv (Over.forget V) p (c.sliceFunctor x) f) n).obj a))
        ((term.{vU, vX, vC, uU, uX, uC, max uC vC vU w} p f F n).map
          (c.map a.target.hom x).op s)
```

**`Stacks.RelativeCech.complexSectionsIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSections.lean#L720). The attribute's comment: “naturality in the coefficient presheaf”.

> The identification commutes in every degree with a morphism of coefficient presheaves; in
> particular it is natural in the abelian presheaf.

```lean
public theorem complexSectionsIso_naturality (p : X ⥤ C) (f : U ⥤ X)
    (hp : p.IsFiberedInGroupoids) (c : p.ChoiceOfPullbacks) {V : C} (x : p.Fiber V)
    (F G : Xᵒᵖ ⥤ AddCommGrpCat.{max uU uX uC vU vX vC w}) (η : F ⟶ G) (n : ℕ) :
    ((Tuple.projection p f n).op.ran.map
          (Functor.whiskerLeft (Tuple.projection p f n).op η)).app (op x.1) ≫
        (complexSectionsIso p f hp c x G).hom.f n =
      (complexSectionsIso p f hp c x F).hom.f n ≫
        limMap (Functor.whiskerLeft ((Tuple.projection (Over.forget V)
          (TwoFibreProductOver.fst (Over.forget V) (f ⋙ p) p (c.sliceFunctor x) f) n) ⋙
            c.sliceFunctor x).op η)
```

## Tag 06XC, a lemma

[Tag 06XC](https://stacks.math.columbia.edu/tag/06XC) in the Stacks Project.

**`Stacks.RelativeCech.isIso_baseChangeMap_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeBaseChange.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeBaseChange.lean#L371).

> **Stacks 06XC.** Base change along a 2-fibre-product square induces an
> isomorphism of relative Čech complexes of abelian presheaves. The comparison
> with the concrete 2-fibre product is required to be an equivalence, including
> when its category of objects lives in a larger universe.

```lean
public theorem isIso_baseChangeMap_of_isTwoFibreProduct
    {X₀ : Type uX} {U₀ : Type uU} {Y₀ : Type uY} {V₀ : Type uV}
    [Category.{vX} X₀] [Category.{vU} U₀]
    [Category.{vY} Y₀] [Category.{vV} V₀]
    (pX : X₀ ⥤ C) (pU : U₀ ⥤ C) (pY : Y₀ ⥤ C) (pV : V₀ ⥤ C)
    (f₀ : U₀ ⥤ X₀) (e₀ : Y₀ ⥤ X₀) (g₀ : V₀ ⥤ Y₀) (h₀ : V₀ ⥤ U₀)
    (hf : f₀ ⋙ pX = pU) (he : e₀ ⋙ pX = pY)
    (hg : g₀ ⋙ pY = pV) (hh : h₀ ⋙ pU = pV)
    (α : h₀ ⋙ f₀ ≅ g₀ ⋙ e₀)
    (hα : ∀ v : V₀, pX.IsHomLift
      (𝟙 (pX.obj (f₀.obj (h₀.obj v)))) (α.hom.app v))
    (hpX : pX.IsFiberedInGroupoids) (hpU : pU.IsFiberedInGroupoids)
    (hpY : pY.IsFiberedInGroupoids) (hpV : pV.IsFiberedInGroupoids)
    (hP : (TwoFibreProductOver.lift pU pY pX f₀ e₀ pV h₀ g₀
      hh hg α (by
        intro v
        have hv : pX.obj (f₀.obj (h₀.obj v)) = pV.obj v := by
          calc
            _ = pU.obj (h₀.obj v) := Functor.congr_obj hf _
            _ = pV.obj v := Functor.congr_obj hh _
        rw [← hv]
        exact hα v)).IsEquivalence)
    (F : X₀ᵒᵖ ⥤ AddCommGrpCat.{max uU uX vX uV uY vY w}) :
    IsIso (baseChangeMap pX f₀ e₀ g₀ h₀ α hα F)
```

## Tag 06XD, a lemma

[Tag 06XD](https://stacks.math.columbia.edu/tag/06XD) in the Stacks Project.

**`Stacks.exact_of_exact_inverseImage_of_covering_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ExactnessCriterion.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ExactnessCriterion.lean#L56).

> Exactness of a complex of abelian sheaves can be checked after pullback to
> a fibred category whose image covers the target locally.

```lean
public theorem exact_of_exact_inverseImage_of_covering_image
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒰 : Type vᵤ} [Category.{wᵤ} 𝒰]
    {𝒳 : Type vₓ} [Category.{wₓ} 𝒳]
    (p : 𝒰 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (q : 𝒳 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (F : 𝒰 ⥤ 𝒳)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hF : p.IsFibredOneMorphism q F)
    (τ : AlgebraicGeometry.SiteKind)
    (hcover : ∀ x : 𝒳, ∃ R : Sieve x,
      R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g →
          ∃ z : 𝒰, Nonempty (y ≅ F.obj z))
    (C : ShortComplex (CategoryTheory.Sheaf
      (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ) Ab.{a})) :
    (letI : p.IsFibered := hp.isFibered
     letI : q.IsFibered := hq.isFibered
     letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
       ((AlgebraicGeometry.BigFppfSite.baseTopology B τ).over (B.obj hS))).1
     letI : (F.sheafPushforwardContinuous Ab.{a}
       (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS p τ)
       (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)).PreservesZeroMorphisms :=
       ⟨by intros; rfl⟩
     (C.map (F.sheafPushforwardContinuous Ab.{a}
       (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS p τ)
       (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ))).Exact) → C.Exact
```

## Tag 06XE, a proposition

[Tag 06XE](https://stacks.math.columbia.edu/tag/06XE) in the Stacks Project.

**`Stacks.RelativeCech.mono_sheafAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean#L615). The attribute's comment: “exactness at the initial sheaf”.

> **Stacks 06XE.** Exactness of the extended relative Čech complex at its initial term: if the
> image of `f` covers every object of `𝒳` locally, the augmentation of an abelian sheaf into degree
> `0` of its sheafified relative Čech complex is a monomorphism.

```lean
public theorem mono_sheafAugmentation
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    [HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}]
    (𝓕 : Sheaf (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}) :
    Mono (sheafAugmentation.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕)
```

**`Stacks.RelativeCech.exact_sheafAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean#L682). The attribute's comment: “exactness at degree zero”.

> **Stacks 06XE.** Exactness of the extended relative Čech complex in degree zero: if `f` is a
> `1`-morphism of categories fibred in groupoids whose image covers every object of `𝒳` locally,
> the augmentation of an abelian sheaf is the kernel of the first differential of its sheafified
> relative Čech complex.

```lean
public theorem exact_sheafAugmentation
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hf : p.IsFibredOneMorphism q f)
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    [HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}]
    (𝓕 : Sheaf (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}) :
    (ShortComplex.mk (sheafAugmentation.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕)
      ((sheafComplex.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕).d 0 1)
      (sheafAugmentation_comp_d.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕)).Exact
```

**`Stacks.RelativeCech.exactAt_sheafComplex_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeExactness.lean#L707). The attribute's comment: “exactness in positive degrees”.

> **Stacks 06XE.** Exactness of the extended relative Čech complex in every positive degree: if
> `f` is a `1`-morphism of categories fibred in groupoids whose image covers every object of `𝒳`
> locally, the sheafified relative Čech complex of an abelian sheaf is exact in every positive
> degree.

```lean
public theorem exactAt_sheafComplex_succ
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hf : p.IsFibredOneMorphism q f)
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    [HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}]
    (𝓕 : Sheaf (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ t}) (n : ℕ) :
    (sheafComplex.{u, vᵤ, vₓ, wᵤ, wₓ, t} B S hS q f τ 𝓕).ExactAt (n + 1)
```

## Tag 06XF, a lemma

[Tag 06XF](https://stacks.math.columbia.edu/tag/06XF) in the Stacks Project.

**`Stacks.RelativeCech.exists_spectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Abelian.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Abelian.lean#L120).

> For a faithful `1`-morphism `f : 𝒰 ⥤ 𝒳` of categories fibred in groupoids over the big fppf
> site of `S`, with equalizers in `𝒰` and image covering `𝒳` locally, there is a first-quadrant
> spectral sequence `E₁^{i,j} = Hʲ((𝒰ᵢ)_τ, fᵢ⁻¹𝓕) ⇒ Hⁱ⁺ʲ(𝒳_τ, 𝓕)`.

```lean
public theorem exists_spectralSequenceData
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hf : p.IsFibredOneMorphism q f) [f.Faithful] [HasEqualizers 𝒰]
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    [HasSheafify (BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ a}]
    [HasExt.{b} (Sheaf (BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ a})]
    [∀ n : ℕ, HasSheafify
      (BigFppfOver.associatedTopology B S hS (Tuple.projection q f n ⋙ q) τ)
        AddCommGrpCat.{max vᵤ vₓ wₓ a}]
    [∀ n : ℕ, HasExt.{b} (Sheaf
      (BigFppfOver.associatedTopology B S hS (Tuple.projection q f n ⋙ q) τ)
        AddCommGrpCat.{max vᵤ vₓ wₓ a})]
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max vᵤ vₓ wₓ a}) :
    Nonempty (SpectralSequenceData (B := B) (S := S) (hS := hS)
      (q := q) (f := f) (τ := τ) 𝓕)
```

## Tag 06XG, a lemma

[Tag 06XG](https://stacks.math.columbia.edu/tag/06XG) in the Stacks Project.

**`Stacks.RelativeCech.exists_moduleSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequenceModules/Abutment.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequenceModules/Abutment.lean#L484).

> For a faithful 1-morphism `f : 𝒰 ⥤ 𝒳` of categories fibred in groupoids over `(Sch/S)_fppf`
> with equalizers in `𝒰`, whose image covers `𝒳` locally in the `τ`-topology, every sheaf of
> `𝒪_𝒳`-modules `𝓕` has a first-quadrant spectral sequence of `Γ(𝒪_𝒳)`-modules
> `E₁^{i,j} = Hʲ((𝒰ᵢ)_τ, fᵢ^*𝓕) ⇒ Hⁱ⁺ʲ(𝒳_τ, 𝓕)`.

```lean
public theorem exists_moduleSpectralSequenceData
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hf : p.IsFibredOneMorphism q f) [f.Faithful] [HasEqualizers 𝒰]
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (g : y ⟶ x), R g →
          ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    (𝓕 : SheafOfModules.{max u vᵤ vₓ wᵤ wₓ a}
      (AlgebraicGeometry.Stack.ringStructureSheafCore B S hS q hq (B.baseTopology τ)
        (B.baseTopology_le_topology τ))) :
    Nonempty (ModuleSpectralSequenceData.{u, vᵤ, vₓ, wᵤ, wₓ, a}
      B S hS q f τ hq 𝓕)
```

## Tag 06XH, a lemma

[Tag 06XH](https://stacks.math.columbia.edu/tag/06XH) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_singleton_fppf_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/LocalLifts.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/LocalLifts.lean#L55). The attribute's comment: “part (1): fppf-local lifts along a surjective flat morphism”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces, and assume that the structure morphism of the
> algebraic space representing the base change of `f` along any scheme-valued point of `𝒴` is
> surjective, flat and locally of finite presentation. Then every object `y` of `𝒴` admits a
> morphism `f(x) ⟶ y` from the image of an object `x` of `𝒳` whose generated sieve covers `y` in
> the associated fppf site of `𝒴`.

```lean
theorem exists_singleton_fppf_lift
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hsurj : ∀ (U : BigFppfOver B S hS) (q : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (hq : q ⋙ 𝒴.val.p = Over.map U.hom),
      Space.IsSurjective B S hS (baseChangeStructureMap B S hS f.hom hf U q hq).hom)
    (hflat : ∀ (U : BigFppfOver B S hS) (q : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (hq : q ⋙ 𝒴.val.p = Over.map U.hom),
      Space.IsFlat B S hS (baseChangeStructureMap B S hS f.hom hf U q hq).hom)
    (hlfp : ∀ (U : BigFppfOver B S hS) (q : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (hq : q ⋙ 𝒴.val.p = Over.map U.hom),
      Space.IsLocallyOfFinitePresentation B S hS
        (baseChangeStructureMap B S hS f.hom hf U q hq).hom)
    (y : 𝒴.val.obj) :
    ∃ (x : 𝒳.val.obj) (a : (CatFiberedInGroupoids.homFunctor f).obj x ⟶ y),
      Sieve.generate (Presieve.singleton a) ∈ fppfTopology B S hS 𝒴 y
```

**`AlgebraicGeometry.Stack.exists_etaleLocalLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean#L291). The attribute's comment: “part (2): étale-local lifts along a surjective smooth morphism”.

> Let `f : 𝒳 ⟶ 𝒴` be a surjective smooth 1-morphism of algebraic stacks. Then every object `y`
> of `𝒴` admits an object `x` of `𝒳` and a morphism `f(x) ⟶ y` whose singleton generates a covering
> sieve of the étale topology that `𝒴` inherits from the site.

```lean
theorem exists_etaleLocalLift {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hsurj : IsSurjective B S hS f)
    (hsmooth : AlgebraicStacks.IsSmooth B S hS f)
    (y : 𝒴.val.val.obj) :
    ∃ (x : 𝒳.val.val.obj) (a : (CatFiberedInGroupoids.homFunctor f.hom).obj x ⟶ y),
      Sieve.generate (Presieve.singleton a) ∈
        BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .etale y
```

**`AlgebraicGeometry.Stack.exists_etaleCovering_fibre_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean#L305). The attribute's comment: “part (2): étale covering of the base with a lift over every arrow”.

> Along a surjective smooth 1-morphism of algebraic stacks, every object of the base carries a
> covering sieve of the étale topology over each of whose arrows the given object of the fibre
> lifts.

```lean
theorem exists_etaleCovering_fibre_lift {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hsurj : IsSurjective B S hS f)
    (hsmooth : AlgebraicStacks.IsSmooth B S hS f)
    (U : BigFppfOver B S hS) (y : 𝒴.val.val.p.Fiber U) :
    ∃ R ∈ BigFppfOver.baseOverTopology B S hS .etale U,
      ∀ ⦃V : BigFppfOver B S hS⦄ ⦃k : V ⟶ U⦄, R.arrows k →
        ∃ (x : 𝒳.val.val.obj) (α : (CatFiberedInGroupoids.homFunctor f.hom).obj x ⟶ y.1),
          𝒴.val.val.p.IsHomLift k α
```

**`AlgebraicGeometry.Stack.exists_etaleLocalLift_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean#L390). The attribute's comment: “part (2) in full generality: étale-local lifts along a 1-morphism of CFGs”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces, and suppose that every algebraic space
> representing the base change of `f` along a scheme-valued point of `𝒴` has surjective and smooth
> structural morphism. Then every object `y` of `𝒴` admits an object `x` of `𝒳` and a morphism
> `a : f(x) ⟶ y` whose singleton generates a covering sieve of the étale topology `𝒴` inherits from
> the site.

```lean
theorem exists_etaleLocalLift_of_representable
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hprop : ∀ (V : BigFppfOver B S hS)
      (yv : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.obj)
      (_hyv : yv ⋙ 𝒴.val.p = Over.map V.hom)
      (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p 𝒴.val.p yv
          (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let h := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS h ∧ Space.IsSmooth B S hS h))
    (y : 𝒴.val.obj) :
    ∃ (x : 𝒳.val.obj) (a : (CatFiberedInGroupoids.homFunctor f).obj x ⟶ y),
      Sieve.generate (Presieve.singleton a) ∈
        BigFppfOver.associatedTopology B S hS 𝒴.val.p .etale y
```

**`AlgebraicGeometry.Stack.exists_etaleCovering_fibre_lift_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EtaleLocalLifts.lean#L418). The attribute's comment: “part (2) in full generality, family form: an étale covering of the base”.

> Along a 1-morphism of categories fibred in groupoids representable by algebraic spaces whose
> base change along every scheme-valued point is surjective and smooth, every object of the base
> carries a covering sieve of the étale topology over each of whose arrows the given object of the
> fibre lifts.

```lean
theorem exists_etaleCovering_fibre_lift_of_representable
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hprop : ∀ (V : BigFppfOver B S hS)
      (yv : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.obj)
      (_hyv : yv ⋙ 𝒴.val.p = Over.map V.hom)
      (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p 𝒴.val.p yv
          (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let h := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS h ∧ Space.IsSmooth B S hS h))
    (U : BigFppfOver B S hS) (y : 𝒴.val.p.Fiber U) :
    ∃ R ∈ BigFppfOver.baseOverTopology B S hS .etale U,
      ∀ ⦃V : BigFppfOver B S hS⦄ ⦃k : V ⟶ U⦄, R.arrows k →
        ∃ (x : 𝒳.val.obj) (α : (CatFiberedInGroupoids.homFunctor f).obj x ⟶ y.1),
          𝒴.val.p.IsHomLift k α
```

**`AlgebraicGeometry.Stack.exists_fppfLocalLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FppfLocalLifts.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FppfLocalLifts.lean#L130). The attribute's comment: “fppf_local_lifts”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces, and suppose that every algebraic space
> representing the base change of `f` along a scheme-valued point of `𝒴` has surjective, flat and
> locally finitely presented structural morphism. Then every object `y` of `𝒴` admits an object `x`
> of `𝒳` and a morphism `a : f(x) ⟶ y` whose singleton generates a covering sieve of the fppf
> topology `𝒴` inherits from the site.

```lean
theorem exists_fppfLocalLift
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hprops : ∀ (T : BigFppfOver B S hS)
      (y : BigFppfOver B T.left.1 T.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map T.hom)
      (F : (BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B T.left.1 T.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map T.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let g := (algebraicSpaceMap B S hS T
        ((spacesOverSmallerBaseFunctor B T.left.1 S T.left.2 hS T.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS g ∧ Space.IsFlat B S hS g ∧
         Space.IsLocallyOfFinitePresentation B S hS g))
    (y : 𝒴.val.obj) :
    ∃ (x : 𝒳.val.obj) (a : (CatFiberedInGroupoids.homFunctor f).obj x ⟶ y),
      Sieve.generate (Presieve.singleton a) ∈
        BigFppfOver.associatedTopology B S hS 𝒴.val.p .fppf y
```

## Tag 072D, a lemma

[Tag 072D](https://stacks.math.columbia.edu/tag/072D) in the Stacks Project.

**`Stacks.RelativeCech.exists_pushforwardSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Abelian.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Abelian.lean#L429).

> Let `f : 𝒰 ⥤ 𝒳` and `g : 𝒳 ⥤ 𝒴` be `1`-morphisms of categories fibred in groupoids over the
> big fppf site of `S`, with `f` faithful, with equalizers in `𝒰` and with the image of `f` covering
> `𝒳` locally for the topology `τ`. For an abelian sheaf `𝓕` on `𝒳_τ` there is a first-quadrant
> spectral sequence of abelian sheaves on `𝒴_τ` with first page `E₁^{i,j} = Rʲ(g ∘ fᵢ)_* fᵢ⁻¹𝓕`
> abutting to `Rⁱ⁺ʲ g_* 𝓕`.

```lean
public theorem exists_pushforwardSpectralSequenceData
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hr : r.IsFiberedInGroupoids)
    (hf : p.IsFibredOneMorphism q f) (hg : q.IsFibredOneMorphism r g)
    [f.Faithful] [HasEqualizers 𝒰]
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (k : y ⟶ x), R k → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    [HasSheafify (BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [HasSheafify (BigFppfOver.associatedTopology B S hS r τ)
      AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [∀ n : ℕ, HasSheafify
      (BigFppfOver.associatedTopology B S hS (Tuple.projection q f n ⋙ q) τ)
        AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [∀ P : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a},
      g.op.HasPointwiseRightKanExtension P]
    [∀ (n : ℕ) (P : (Tuple q f n)ᵒᵖ ⥤ AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a}),
      (Tuple.projection q f n ⋙ g).op.HasPointwiseRightKanExtension P]
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max v₁ w₁ v₂ w₂ v₃ w₃ a}) :
    Nonempty (PushforwardSpectralSequenceData (B := B) (S := S) (hS := hS)
      (q := q) (r := r) (f := f) (g := g) (τ := τ) 𝓕)
```

## Tag 072E, a lemma

[Tag 072E](https://stacks.math.columbia.edu/tag/072E) in the Stacks Project.

**`Stacks.RelativeCech.nonempty_modulePushforwardSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ModulePushforwardSpectralSequence.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/ModulePushforwardSpectralSequence.lean#L79).

> **Stacks 072E.** Let `f : 𝒰 ⥤ 𝒳` and `g : 𝒳 ⥤ 𝒴` be `1`-morphisms of categories fibred in
> groupoids over the big fppf site of `S`, with `f` faithful, with equalizers in `𝒰` and with the
> image of `f` covering `𝒳` locally for the topology `τ`. For a sheaf of `𝒪_𝒳`-modules `𝓕` on
> `𝒳_τ` there is a first-quadrant spectral sequence of sheaves of `𝒪_𝒴`-modules on `𝒴_τ` with
> first page `E₁^{i,j} = Rʲ(g ∘ fᵢ)_* fᵢ⁻¹𝓕` abutting to `Rⁱ⁺ʲ g_* 𝓕`, all higher direct images
> being computed in the `τ`-topology.

```lean
public theorem nonempty_modulePushforwardSpectralSequenceData
    [f.Faithful] [HasEqualizers 𝒰]
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (k : y ⟶ x), R k → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    (𝓕 : SheafOfModules.{max u v₁ w₁ v₂ w₂ v₃ w₃ a} (moduleRingSheaf B S hS q hq τ)) :
    Nonempty (ModulePushforwardSpectralSequenceData.{u, v₁, v₂, v₃, w₁, w₂, w₃, a}
      B S hS p q r f g τ hp hq hr hf hg 𝓕)
```

**`Stacks.RelativeCech.exists_modulePushforwardSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Modules.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/RelativeSpectralSequence/Modules.lean#L325).

> Let `f : 𝒰 ⥤ 𝒳` and `g : 𝒳 ⥤ 𝒴` be `1`-morphisms of categories fibred in groupoids over the
> big fppf site of `S`, with `f` faithful, with equalizers in `𝒰` and with the image of `f` covering
> `𝒳` locally for the topology `τ`. For a sheaf of `𝒪_𝒳`-modules `𝓕` on `𝒳_τ` there is a
> first-quadrant spectral sequence of sheaves of `𝒪_𝒴`-modules on `𝒴_τ` with first page
> `E₁^{i,j} = Rʲ(g ∘ fᵢ)_* fᵢ⁻¹𝓕` abutting to `Rⁱ⁺ʲ g_* 𝓕`, all higher direct images being computed
> in the `τ`-topology.

```lean
public theorem exists_modulePushforwardSpectralSequenceData
    [f.Faithful] [HasEqualizers 𝒰]
    (hcover : ∀ x : 𝒳, ∃ R : Presieve x,
      Sieve.generate R ∈ AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ x ∧
        ∀ ⦃y : 𝒳⦄ (k : y ⟶ x), R k → ∃ z : 𝒰, Nonempty (y ≅ f.obj z))
    (hRightAdjoint : ∀ n : ℕ, (PresheafOfModules.pushforward.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}
      (AlgebraicGeometry.Stack.ringStructureSheafCoreHom B S hS
        (Tuple.projection q f n ⋙ q) q (Tuple.projection q f n) (B.baseTopology τ)
        (tupleProjection_comp_isFiberedInGroupoids B S hS p q f hp hq hf n) hq rfl
        (B.baseTopology_le_topology τ)).hom).IsRightAdjoint)
    [∀ (n : ℕ) (G : (Tuple q f n)ᵒᵖ ⥤ AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}),
      (Tuple.projection q f n).op.HasPointwiseLeftKanExtension G]
    [HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ)
      AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [(AlgebraicGeometry.BigFppfOver.associatedTopology B S hS q τ).WEqualsLocallyBijective
      AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS r τ)
      AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [(AlgebraicGeometry.BigFppfOver.associatedTopology B S hS r τ).WEqualsLocallyBijective
      AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [∀ n : ℕ, HasSheafify (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS
      (Tuple.projection q f n ⋙ q) τ) AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [∀ n : ℕ, (AlgebraicGeometry.BigFppfOver.associatedTopology B S hS
      (Tuple.projection q f n ⋙ q) τ).WEqualsLocallyBijective
        AddCommGrpCat.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}]
    [∀ n : ℕ, EnoughInjectives (SheafOfModules.{max u v₁ w₁ v₂ w₂ v₃ w₃ a}
      (moduleRingSheaf B S hS (Tuple.projection q f n ⋙ q)
        (tupleProjection_comp_isFiberedInGroupoids B S hS p q f hp hq hf n) τ))]
    [EnoughInjectives (SheafOfModules.{max u v₁ w₁ v₂ w₂ v₃ w₃ a} (moduleRingSheaf B S hS q hq τ))]
    (𝓕 : SheafOfModules.{max u v₁ w₁ v₂ w₂ v₃ w₃ a} (moduleRingSheaf B S hS q hq τ)) :
    Nonempty (ModulePushforwardSpectralSequenceData.{u, v₁, v₂, v₃, w₁, w₂, w₃, a}
      B S hS p q r f g τ hp hq hr hf hg 𝓕)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.19, Tag 06X7](https://stacks.math.columbia.edu/tag/06X7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
