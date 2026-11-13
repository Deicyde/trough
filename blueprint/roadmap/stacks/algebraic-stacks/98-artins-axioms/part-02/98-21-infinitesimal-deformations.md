---
declaration: section
origin: cited
lean: Deformation.Artin.liftOutFunctorOfPullback, Deformation.Artin.liftOutFunctor_unique, Deformation.Artin.liftFunctorOfHom_comp, Deformation.Artin.exists_infComparison, Deformation.Artin.exists_actionOnLifts, Deformation.Artin.exists_infinitesimalAutomorphismFunctor, Deformation.Artin.exists_tangentFunctor, Deformation.Artin.isLinearMap_tangentBaseChangeMap
statement: formalized
proof: formalized
---

# 98.21 Infinitesimal deformations

Section 98.21 of the Stacks Project, [Tag 07Y6](https://stacks.math.columbia.edu/tag/07Y6). 8 tags here are carried by 41 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07Y7, a lemma

[Tag 07Y7](https://stacks.math.columbia.edu/tag/07Y7) in the Stacks Project.

**`Deformation.Artin.liftOutFunctorOfPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L425). The attribute's comment: “the functor, on the source's Lift(x, A'), lifts out of the base”.

> **Stacks 07Y7.** Let `F : X ⥤ Y` be a `1`-morphism of categories fibred in groupoids over
> `C`, let `b ≫ a = d ≫ c` be a commutative square of the base with `a : U ⟶ U'`, `b : V ⟶ U`,
> `c : V' ⟶ U'` and `d : V ⟶ V'`, let `x` lie over `U`, let `y` lie over `V`, and let `φ` be a
> morphism `F(x)|_V ⟶ y` of the fibre over `V`. Then there is a canonical functor from the lifts
> of `x` along `a` to the lifts of `y` along `d`: a lift `x ⟶ x'` is carried to the chosen
> pullback of `F x'` along `c`, whose structure arrow out of `y` is the factorization of
> `y ⟶ F x ⟶ F x'` through that cartesian arrow.
>
> Over the big fppf site this is the source's `Lift(x, A') ⟶ Lift(y, B')` for the commutative
> diagram of `S`-algebras with rows `A' ⟶ A`, `B' ⟶ B` and columns `A' ⟶ B'`, `A ⟶ B`.

```lean
public noncomputable def liftOutFunctorOfPullback (p : X ⥤ C) (q : Y ⥤ C)
    (hq : q.IsFiberedInGroupoids) (F : X ⥤ Y) (hF : F ⋙ q = p)
    {U U' V V' : C} (a : U ⟶ U') (b : V ⟶ U) (c : V' ⟶ U') (d : V ⟶ V')
    (hsq : b ≫ a = d ≫ c) (x : X) (hx : p.obj x = U)
    (y : Y) (hy : q.obj y = V) (e : q.ChoiceOfPullbacks)
    (φ : (e.pullbackFunctor b).obj (imageFiber p q F hF x hx) ⟶ ⟨y, hy⟩) :
    LiftOutFunctor p q F a b c d x hx y hy
      (pullbackComparison p q hq F hF b x hx y hy e φ)
```

**`Deformation.Artin.liftOutFunctor_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L555). The attribute's comment: “uniqueness, on the source's Lift(x, A'), lifts out of the base”.

> Two constructions satisfying the cartesian-square specification are uniquely isomorphic by
> an isomorphism commuting with their comparison maps. In particular, the direct functor for a
> composite of morphisms of fibred groupoids agrees canonically with the composite of the induced
> lift functors.

```lean
public theorem liftOutFunctor_unique (p : X ⥤ C) (q : Y ⥤ C) (F : X ⥤ Y)
    {U U' V V' : C} (a : U ⟶ U') (b : V ⟶ U) (c : V' ⟶ U') (d : V ⟶ V')
    (x : X) (hx : p.obj x = U) (y : Y) (hy : q.obj y = V)
    (φ : y ⟶ F.obj x)
    (L M : LiftOutFunctor p q F a b c d x hx y hy φ) :
    ∃! η : L.toFunctor ≅ M.toFunctor,
      ∀ t : LiftOut p a x hx,
        (η.hom.app t).1.right ≫ M.comparison t = L.comparison t
```

**`Deformation.Artin.liftFunctorOfHom_comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L768). The attribute's comment: “compatibility with composition, on the source's Lift(x, A'), lifts out of the base”.

> **Stacks 07Y7, compatibility with composition.** The construction is compatible with
> composition of `1`-morphisms of categories fibred in groupoids: the functor on lifts induced
> by `F` and `φ`, followed by the functor on lifts induced by `G` and `ψ` over the identity
> square at `d`, is canonically isomorphic to the functor on lifts induced by `F ⋙ G` and the
> composite arrow `ψ ≫ G φ`, by the unique isomorphism commuting with the cartesian comparison
> arrows.
>
> All three functors here are built, not assumed to satisfy the specification: each is, by
> definition, a functor `Deformation.Artin.liftOutFunctorOfPullback` builds from the datum
> `Deformation.Artin.pullbackDatum` attaches to the given arrow. The source's data are covered
> because a morphism out of the chosen pullback gives such an arrow, by
> `Deformation.Artin.pullbackComparison` and
> `Deformation.Artin.pullbackComparison_isHomLift`.

```lean
public noncomputable def liftFunctorOfHom_comp {Z : Type*} [Category Z]
    (p : X ⥤ C) (q : Y ⥤ C) (r : Z ⥤ C)
    (hq : q.IsFiberedInGroupoids) (hr : r.IsFiberedInGroupoids)
    (F : X ⥤ Y) (G : Y ⥤ Z) (hF : F ⋙ q = p) (hG : G ⋙ r = q)
    {U U' V V' : C} (a : U ⟶ U') (b : V ⟶ U) (c : V' ⟶ U') (d : V ⟶ V')
    (hsq : b ≫ a = d ≫ c) (x : X) (hx : p.obj x = U)
    (y : Y) (hy : q.obj y = V) (z : Z) (hz : r.obj z = V)
    (eY : q.ChoiceOfPullbacks) (eZ : r.ChoiceOfPullbacks)
    (φ : y ⟶ F.obj x) (hφ : q.IsHomLift b φ)
    (ψ : z ⟶ G.obj y) (hψ : r.IsHomLift (𝟙 V) ψ) :
    {η : (liftFunctorOfHom p q hq F hF a b c d hsq x hx y hy eY φ hφ).toFunctor ⋙
          (liftFunctorOfHom q r hr G hG d (𝟙 V) (𝟙 V') d (id_comp_square d) y hy z hz
            eZ ψ hψ).toFunctor ≅
        (liftFunctorOfHom p r hr (F ⋙ G) (comp_over_base hF hG) a b c d hsq x hx z hz eZ
          (ψ ≫ G.map φ)
          (comp_comparison_isHomLift q r F G hG b x y z φ hφ ψ hψ)).toFunctor //
      ∀ t : LiftOut p a x hx,
        (η.hom.app t).1.right ≫
            (liftFunctorOfHom p r hr (F ⋙ G) (comp_over_base hF hG) a b c d hsq x hx z hz eZ
              (ψ ≫ G.map φ)
              (comp_comparison_isHomLift q r F G hG b x y z φ hφ ψ hψ)).comparison t =
          (liftFunctorOfHom q r hr G hG d (𝟙 V) (𝟙 V') d (id_comp_square d) y hy z hz
              eZ ψ hψ).comparison
            ((liftFunctorOfHom p q hq F hF a b c d hsq x hx y hy eY φ hφ).toFunctor.obj t) ≫
            G.map ((liftFunctorOfHom p q hq F hF a b c d hsq x hx y hy eY φ hφ).comparison t)}
```

## Tag 07Y9, a lemma

[Tag 07Y9](https://stacks.math.columbia.edu/tag/07Y9) in the Stacks Project.

**`Deformation.Artin.exists_infComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLifts/InfComparison.lean, line 760](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLifts/InfComparison.lean#L760). The attribute's comment: “part (1), the comparison of Inf\_x(I) with Inf(x'/x)”.

> **Stacks 07Y9 part (1).** For `𝒳` satisfying (RS*), a deformation situation `A' → A`
> with square-zero kernel `I` whose source lies in the chosen site, and a lift `x'` of `x`
> over `Spec A'`, the value of the `A`-linear functor `Inf_x` at `I` is isomorphic, as a
> group, to the infinitesimal automorphisms of `x'`.

```lean
public noncomputable def exists_infComparison (hRS : SatisfiesRSStar B S hS p hp)
    (Inf : InfinitesimalAutomorphismFunctorData A B S hS toS hA p x hx hp)
    (A' : Type u) [CommRing A'] (hA' : B.Contains (Spec (.of A')))
    (toS' : B.obj hA' ⟶ B.obj hS) (q : A' →+* A) (hq : Function.Surjective q)
    (hsq : RingHom.ker q ^ 2 = ⊥)
    (g : algebraOver A B S hS toS hA ⟶ (Over.mk toS' : BigFppfOver B S hS))
    (hg : B.inclusion.map g.left = Spec.map (CommRingCat.ofHom q))
    (x' : (Under.post p).Fiber (Under.mk (eqToHom hx ≫ g))) :
    InfComparisonData A B S hS toS hA p x hx hp Inf A' hA' toS' q hq hsq g x'
```

**`Deformation.Artin.exists_actionOnLifts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLifts/LiftAction.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLifts/LiftAction.lean#L547). The attribute's comment: “part (2)(b), the action of T\_x(I) on the lifts over A'”.

> **Stacks 07Y9 part (2)(b).** The difference-transport action of the tangent module
> `T_x(I)` on the isomorphism classes of lifts of `x` over a square-zero deformation `A' → A`
> with kernel `I`. Every orbit map is bijective, so the action is simply transitive whenever
> there is a lift.

```lean
public noncomputable def exists_actionOnLifts
    (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRSStar B S hS p hp)
    (A' : Type u) [CommRing A']
    (hA' : B.Contains (Spec (.of A')))
    (toS' : B.obj hA' ⟶ B.obj hS)
    (q : A' →+* A)
    (hq : Function.Surjective q)
    (hsq : (RingHom.ker q) ^ 2 = ⊥)
    (g : algebraOver A B S hS toS hA ⟶
      (Over.mk toS' : BigFppfOver B S hS))
    (hg : B.inclusion.map g.left = Spec.map (CommRingCat.ofHom q)) :
    ActionOnLiftsData A B S hS toS hA p x hx
      (tangentFunctor A B S hS toS hA p x hx hp hRS)
      A' hA' toS' q hq hsq g
```

**`Deformation.Artin.exists_infinitesimalAutomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/AutomorphismFunctor.lean, line 902](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/AutomorphismFunctor.lean#L902). The attribute's comment: “part (1), the A-linear functor Inf\_x on trivial square-zero extensions”.

> For `𝒳` satisfying (RS*), the infinitesimal automorphisms of the trivial deformations of
> `x` over the trivial square-zero extensions `A[M]` are the underlying sets of an `A`-linear
> functor of `M`.

```lean
public theorem exists_infinitesimalAutomorphismFunctor (hRS : SatisfiesRSStar B S hS p hp) :
    Nonempty (InfinitesimalAutomorphismFunctorData A B S hS toS hA p x hx hp)
```

**`Deformation.Artin.exists_tangentFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TangentFunctor.lean, line 1356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TangentFunctor.lean#L1356). The attribute's comment: “part (2)(a), the A-linear tangent functor T\_x”.

> **Stacks 07Y9 part (2)(a), the tangent functor.** For `𝒳` satisfying (RS*), the
> isomorphism classes of lifts of `x` over the trivial square-zero extensions `A[M]` are the
> underlying sets of an `A`-linear functor of `M`.

```lean
public theorem exists_tangentFunctor (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRSStar B S hS p hp) :
    Nonempty (TangentFunctorData A B S hS toS hA p x hx)
```

## Tag 07YA, a remark

[Tag 07YA](https://stacks.math.columbia.edu/tag/07YA) in the Stacks Project.

**`Deformation.Artin.isLinearMap_tangentBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/BaseChangeLinear.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/BaseChangeLinear.lean#L473). The attribute's comment: “the A-linear map T\_x(M) → T\_y(N)”.

> **Remark 07YA for the tangent functor.** For a ring map `f : A ⟶ C`, the restriction
> `y = x|_{Spec C}` and an `f`-semilinear map `M ⟶ N` of coefficients, the induced map
> `T_x(M) ⟶ T_y(N)` is `A`-linear, where `T_y(N)` is viewed as an `A`-module by restriction of
> scalars along `f`.

```lean
public theorem isLinearMap_tangentBaseChangeMap {M : SiteModule A B} {N : SiteModule C B}
    (ψ : M.obj ⟶ (ModuleCat.restrictScalars f).obj N.obj) :
    letI : Module A ((Ty.functor.obj N : Type (max (u + 1) v w))) := Module.compHom _ f
    IsLinearMap A
      (tangentBaseChangeMap f B S hS toS hA toSC hC hf p x y hx hy φ₀ hφ₀ hp Tx Ty ψ)
```

**`Deformation.Artin.isLinearMap_infBaseChangeMap_tangentBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSituationMorphism.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSituationMorphism.lean#L396). The attribute's comment: “the A-linear maps Inf\_x(M) → Inf\_y(N) and T\_x(M) → T\_y(N) induced by pullback”.

> **Stacks 07YA, the maps.** Let `𝒳` satisfy (RS*), let `f : A ⟶ C` be a map of
> `S`-algebras, `y = x|_{Spec C}` (the arrow `φ₀ : y ⟶ x` over `Spec C ⟶ Spec A`), `M` an
> `A`-module, `N` a `C`-module and `ψ : M ⟶ N` an `A`-linear map. The pullback functor on lifts
> along `Spec C[N] ⟶ Spec A[M]` induces maps `Inf_x(M) ⟶ Inf_y(N)` and `T_x(M) ⟶ T_y(N)` on the
> functors of Stacks 07Y9, and both are `A`-linear (with `A` acting on the targets through `f`).
> That the maps are induced by the pullback functor is the transition relation each of them
> realizes: `Deformation.Artin.IsSiteInfinitesimalAutomorphismBaseChange` and
> `Deformation.Artin.IsSiteSquareZeroLiftBaseChange`. The statement holds for every choice of
> the functors `Inf_x`, `Inf_y`, `T_x`, `T_y` of Stacks 07Y9.

```lean
public theorem isLinearMap_infBaseChangeMap_tangentBaseChangeMap
    (hRS : SatisfiesRSStar B S hS p hp)
    (Tx : TangentFunctorData A B S hS toS hA p x hx)
    (Ty : TangentFunctorData C B S hS toSC hC p y hy)
    {M : SiteModule A B} {N : SiteModule C B}
    (ψ : M.obj ⟶ (ModuleCat.restrictScalars f).obj N.obj) :
    letI : Module A (Inf'.functor.obj N : Type w) := Module.compHom _ f
    letI : Module A ((Ty.functor.obj N : Type (max (u + 1) v w))) := Module.compHom _ f
    IsLinearMap A (infBaseChangeMap f B S hS toS hA toSC hC hf p x y hx hy φ₀ hφ₀ hp Inf Inf'
        ψ) ∧
      (∀ a, IsSiteInfinitesimalAutomorphismBaseChange B S hS toS hA toSC hC p x y hx hy φ₀ f ψ hp
        (Inf.autEquiv M a)
        (Inf'.autEquiv N (infBaseChangeMap f B S hS toS hA toSC hC hf p x y hx hy φ₀ hφ₀ hp
          Inf Inf' ψ a))) ∧
      IsLinearMap A (tangentBaseChangeMap f B S hS toS hA toSC hC hf p x y hx hy φ₀ hφ₀ hp
        Tx Ty ψ) ∧
      (∀ a, IsSiteSquareZeroLiftBaseChange B S hS toS hA toSC hC p x y hx hy φ₀ f ψ
        (Tx.liftEquiv M a)
        (Ty.liftEquiv N (tangentBaseChangeMap f B S hS toS hA toSC hC hf p x y hx hy φ₀ hφ₀ hp
          Tx Ty ψ a)))
```

**`Deformation.Artin.infComparison_restrict_and_action_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSituationMorphism.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSituationMorphism.lean#L710). The attribute's comment: “the two commutative squares for a morphism of deformation situations”.

> **Stacks 07YA, the two squares.** Let `𝒳` satisfy (RS*) and let `(y, C' → C) ⟶ (x, A' → A)`
> be a morphism of deformation situations: `f' : A' → C'` over `f : A → C`, compatibly with the
> structure morphisms to `S`, and `φ₀ : y ⟶ x` over `Spec C ⟶ Spec A`. Let `I = Ker(A' → A)`,
> `J = Ker(C' → C)`, with the map `I ⟶ J` induced by `f'`.
>
> * For a lift `x'` of `x` to `A'` and its restriction `y'` to `C'` (any lift of `y` with an
>   arrow `y' ⟶ x'` over `Spec C' ⟶ Spec A'` compatible with `φ₀`), the square
>   `Inf_x(I) ⟶ Inf(x'/x) ⟶ Inf(y'/y)` = `Inf_x(I) ⟶ Inf_y(J) ⟶ Inf(y'/y)` commutes.
> * The square `T_x(I) × Lift(x, A') ⟶ Lift(x, A') ⟶ Lift(y, C')` =
>   `T_x(I) × Lift(x, A') ⟶ T_y(J) × Lift(y, C') ⟶ Lift(y, C')` commutes.
>
> The horizontal maps are the comparisons and the actions of Stacks 07Y9, the vertical ones the
> maps of Remark 07YA and the pullback of lifts along `Spec C' ⟶ Spec A'`. All the data of
> Stacks 07Y9 (the functors `Inf`, `T`, the comparisons and the actions) are arbitrary: each is
> pinned by its geometric difference, which is what the proof restricts.

```lean
public theorem infComparison_restrict_and_action_restrict (hRS : SatisfiesRSStar B S hS p hp)
    (Infx : InfinitesimalAutomorphismFunctorData A B S hS toS hA p x hx hp)
    (Infy : InfinitesimalAutomorphismFunctorData C B S hS toSC hC p y hy hp)
    (x' : (Under.post p).Fiber (Under.mk (eqToHom hx ≫ gA)))
    (y' : (Under.post p).Fiber (Under.mk (eqToHom hy ≫ gC)))
    (φ : y'.1.right ⟶ x'.1.right)
    (hφ : p.IsHomLift (deformationSituationMap B S hS hA' toS' hC' toSC' f' hf') φ)
    (hφc : y'.1.hom ≫ φ = φ₀ ≫ x'.1.hom)
    (Cx : InfComparisonData A B S hS toS hA p x hx hp Infx A' hA' toS' q hq hsq gA x')
    (Cy : InfComparisonData C B S hS toSC hC p y hy hp Infy C' hC' toSC' qC hqC hsqC gC y')
    (Tx : TangentFunctorData A B S hS toS hA p x hx)
    (Ty : TangentFunctorData C B S hS toSC hC p y hy)
    (Dx : ActionOnLiftsData A B S hS toS hA p x hx Tx A' hA' toS' q hq hsq gA)
    (Dy : ActionOnLiftsData C B S hS toSC hC p y hy Ty C' hC' toSC' qC hqC hsqC gC) :
    letI : Module A (RingHom.ker q) := Stacks.Smooth.kerModule hq hsq
    letI : Module C (RingHom.ker qC) := Stacks.Smooth.kerModule hqC hsqC
    (∀ a : (Infx.functor.obj ⟨ModuleCat.of A (RingHom.ker q), Cx.kernelIsSiteModule⟩ : Type w),
      Cy.equiv (infBaseChangeMap f B S hS toS hA toSC hC
          (specMap_comp_eq_of_deformationSituation f B S hS toS hA toSC hC hA' toS' q gA hgA hC'
          toSC' qC gC hgC f' hff hf') p x y hx hy φ₀ hφ₀ hp Infx Infy
          (M := ⟨ModuleCat.of A (RingHom.ker q), Cx.kernelIsSiteModule⟩)
          (N := ⟨ModuleCat.of C (RingHom.ker qC), Cy.kernelIsSiteModule⟩)
          (kernelBaseChange hq hsq hqC hsqC hff) a) =
        liftEndRestrict p hp φ₀ φ hφ hφc (Cx.equiv a)) ∧
    (∀ (a : (Tx.functor.obj ⟨ModuleCat.of A (RingHom.ker q), Dx.kernelIsSiteModule⟩ : Type _))
      (z : liftClassesOver A B S hS toS hA p x hx gA),
      liftClassesRestrict p hp φ₀ _ hφ₀
          (algebraOverMap_comp_deformationSituation f B S hS toS hA toSC hC hA' toS' q gA hgA
            hC' toSC' qC gC hgC f' hff hf') (Dx.action a z) =
        Dy.action (tangentBaseChangeMap f B S hS toS hA toSC hC
          (specMap_comp_eq_of_deformationSituation f B S hS toS hA toSC hC hA' toS' q gA hgA hC'
          toSC' qC gC hgC f' hff hf') p x y hx hy φ₀ hφ₀ hp Tx Ty
          (M := ⟨ModuleCat.of A (RingHom.ker q), Dx.kernelIsSiteModule⟩)
          (N := ⟨ModuleCat.of C (RingHom.ker qC), Dy.kernelIsSiteModule⟩)
          (kernelBaseChange hq hsq hqC hsqC hff) a)
          (liftClassesRestrict p hp φ₀ _ hφ₀
            (algebraOverMap_comp_deformationSituation f B S hS toS hA toSC hC hA' toS' q gA hgA
              hC' toSC' qC gC hgC f' hff hf') z))
```

**`Deformation.Artin.existsUnique_tangentBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/TangentPullback.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/TangentPullback.lean#L291). The attribute's comment: “tangent\_base\_change”.

> **Stacks 07YA on tangent modules.** Let `x` be an object over `Spec A` of a category fibred
> in groupoids over the big fppf site of `S`, let `f : A ⟶ C` be a homomorphism of `S`-algebras
> and let `y ⟶ x` be a morphism lying over `Spec C ⟶ Spec A`, so that `y = x|_{Spec C}`. For
> `M ∈ Mod_A`, `N ∈ Mod_C` and an `A`-linear map `M ⟶ N` there is exactly one `A`-linear map
> `T_x(M) ⟶ T_y(N)` — written as an `f`-semilinear map — carrying each class of lifts of `x`
> over `Spec A[M]` to the class of its pullback along `Spec C[N] ⟶ Spec A[M]`.
>
> The tangent functors `T_x`, `T_y` are arbitrary members of
> `Deformation.Artin.TangentFunctorData`, which (RS*) supplies by Stacks 07Y9 (2)(a).

```lean
public theorem existsUnique_tangentBaseChange {M : SiteModule A B} {N : SiteModule C B}
    (ψ : M.obj ⟶ (ModuleCat.restrictScalars f).obj N.obj) :
    ∃! τ : ↥(F.functor.obj M) →ₛₗ[f] ↥(G.functor.obj N),
      ∀ z, G.liftEquiv N (τ z) = liftClassPullback f hf hp φ hφ ψ (F.liftEquiv M z)
```

Declarations registered for the tag:

- [`Deformation.Artin.liftOutFunctorOfPullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L425), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean, line 803](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L803) (StacksFrontier): “pullback\_of\_lifts”.
- [`Deformation.Artin.liftOutFunctor_unique`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L555), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean, line 804](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/InfinitesimalLiftOut.lean#L804) (StacksFrontier): “pullback\_of\_lifts”.

## Tag 07YB, a remark

[Tag 07YB](https://stacks.math.columbia.edu/tag/07YB) in the Stacks Project.

**`Deformation.Artin.compositionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 816](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L816). The attribute's comment: “composition\_map”.

> Composition with relative infinitesimal automorphisms on both sides of a
> morphism of lifts.

```lean
public noncomputable def compositionMap
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x) :
    ((infinitesimalAutomorphisms hp t₁ × (t₁ ⟶ t₂)) ×
      infinitesimalAutomorphisms hp t₂) → (t₁ ⟶ t₂)
```

**`Deformation.Artin.leftCompositionAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 874](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L874). The attribute's comment: “groupoid\_actions”.

> The left action of relative infinitesimal automorphisms of the source lift
> on morphisms of lifts, by inverse precomposition.

```lean
public noncomputable def leftCompositionAction
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (a : infinitesimalAutomorphisms hp t₁) (f : t₁ ⟶ t₂) : t₁ ⟶ t₂
```

**`Deformation.Artin.rightCompositionAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 883](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L883). The attribute's comment: “groupoid\_actions”.

> The right action of relative infinitesimal automorphisms of the target lift
> on morphisms of lifts, by inverse postcomposition.

```lean
public noncomputable def rightCompositionAction
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (f : t₁ ⟶ t₂) (b : infinitesimalAutomorphisms hp t₂) : t₁ ⟶ t₂
```

**`Deformation.Artin.leftComposition_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1007](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1007). The attribute's comment: “groupoid\_actions”.

> The identity automorphism acts trivially on the left.

```lean
public theorem leftComposition_one (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x) (f : t₁ ⟶ t₂) :
    leftCompositionAction hp t₁ t₂ 1 f = f
```

**`Deformation.Artin.leftComposition_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1015). The attribute's comment: “groupoid\_actions”.

> The left action is compatible with multiplication of automorphisms.

```lean
public theorem leftComposition_mul (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (a b : infinitesimalAutomorphisms hp t₁) (f : t₁ ⟶ t₂) :
    leftCompositionAction hp t₁ t₂ (a * b) f =
      leftCompositionAction hp t₁ t₂ a (leftCompositionAction hp t₁ t₂ b f)
```

**`Deformation.Artin.rightComposition_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1027](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1027). The attribute's comment: “groupoid\_actions”.

> The identity automorphism acts trivially on the right.

```lean
public theorem rightComposition_one (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x) (f : t₁ ⟶ t₂) :
    rightCompositionAction hp t₁ t₂ f 1 = f
```

**`Deformation.Artin.rightComposition_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1035). The attribute's comment: “groupoid\_actions”.

> The right action is compatible with multiplication of automorphisms.

```lean
public theorem rightComposition_mul (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (a b : infinitesimalAutomorphisms hp t₂) (f : t₁ ⟶ t₂) :
    rightCompositionAction hp t₁ t₂ (rightCompositionAction hp t₁ t₂ f a) b =
      rightCompositionAction hp t₁ t₂ f (a * b)
```

**`Deformation.Artin.leftComposition_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1057). The attribute's comment: “groupoid\_actions”.

> At each morphism of lifts, the orbit map for the left action is a bijection.

```lean
public theorem leftComposition_bijective
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (f : t₁ ⟶ t₂) :
    Function.Bijective (fun a : infinitesimalAutomorphisms hp t₁ =>
      leftCompositionAction hp t₁ t₂ a f)
```

**`Deformation.Artin.rightComposition_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 1077](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L1077). The attribute's comment: “groupoid\_actions”.

> At each morphism of lifts, the orbit map for the right action is a bijection.

```lean
public theorem rightComposition_bijective
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (f : t₁ ⟶ t₂) :
    Function.Bijective (fun b : infinitesimalAutomorphisms hp t₂ =>
      rightCompositionAction hp t₁ t₂ f b)
```

**`Deformation.Artin.InfComparisonData.actions_agree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLiftsRestriction.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/ActionOnLiftsRestriction.lean#L440). The attribute's comment: “actions on Mor(x', x'') agree via Inf(x'/x) = Inf\_x(I) = Inf(x''/x)”.

> **Stacks 07YB.** Let `𝒳` satisfy (RS*), let `(x, A' → A)` be a deformation situation with
> kernel `I`, and let `x'`, `x''` be lifts of `x` to `Spec A'`. Composition gives a map
> `Inf(x'/x) × Mor(x', x'') × Inf(x''/x) → Mor(x', x'')`, and since the lifts form a groupoid it
> defines, at every morphism, simply transitive actions of `Inf(x'/x)` (by precomposition) and of
> `Inf(x''/x)` (by postcomposition). Let `C'` and `C''` be the comparisons of Stacks 07Y9,
> `Inf_x(I) ≅ Inf(x'/x)` and `Inf_x(I) ≅ Inf(x''/x)`. Then the two actions agree via these
> identifications: `C'(a) ≫ f = f ≫ C''(a)` for every `a ∈ Inf_x(I)` and every morphism
> `f : x' ⟶ x''`. In particular `Inf_x(I)` acts on `Mor(x', x'')`, and the action is simply
> transitive as soon as `Mor(x', x'')` is nonempty: every orbit map is a bijection.
>
> The agreement holds for *every* pair of comparisons in the sense of
> `Deformation.Artin.InfComparisonData`, which pins a comparison geometrically. The proof shows
> that this pin determines the comparison and is natural for isomorphisms of lifts
> (`Deformation.Artin.IsGeometricInfDifference.conj`), using (RS*) and the commutativity of
> `Inf(x'/x)` and of `Inf_x(I)`.

```lean
public theorem InfComparisonData.actions_agree (hRS : SatisfiesRSStar B S hS p hp)
    (Inf : InfinitesimalAutomorphismFunctorData A B S hS toS hA p x hx hp)
    (A' : Type u) [CommRing A'] (hA' : B.Contains (Spec (.of A')))
    (toS' : B.obj hA' ⟶ B.obj hS) (q : A' →+* A) (hq : Function.Surjective q)
    (hsq : RingHom.ker q ^ 2 = ⊥)
    (g : algebraOver A B S hS toS hA ⟶ (Over.mk toS' : BigFppfOver B S hS))
    (hg : B.inclusion.map g.left = Spec.map (CommRingCat.ofHom q))
    {x' x'' : (Under.post p).Fiber (Under.mk (eqToHom hx ≫ g))}
    (C' : InfComparisonData A B S hS toS hA p x hx hp Inf A' hA' toS' q hq hsq g x')
    (C'' : InfComparisonData A B S hS toS hA p x hx hp Inf A' hA' toS' q hq hsq g x'') :
    letI := Stacks.Smooth.kerModule hq hsq
    (∀ f : x' ⟶ x'', Function.Bijective (fun α : x' ⟶ x' => α ≫ f)) ∧
      (∀ f : x' ⟶ x'', Function.Bijective (fun β : x'' ⟶ x'' => f ≫ β)) ∧
      (∀ (a : Inf.functor.obj ⟨ModuleCat.of A (RingHom.ker q), C'.kernelIsSiteModule⟩)
        (f : x' ⟶ x''), C'.equiv a ≫ f = f ≫ C''.equiv a) ∧
      (∀ f : x' ⟶ x'', C'.equiv 0 ≫ f = f) ∧
      (∀ (a b : Inf.functor.obj ⟨ModuleCat.of A (RingHom.ker q), C'.kernelIsSiteModule⟩)
        (f : x' ⟶ x''), C'.equiv (a + b) ≫ f = C'.equiv a ≫ C'.equiv b ≫ f) ∧
      (∀ f : x' ⟶ x'', Function.Bijective
        (fun a : Inf.functor.obj ⟨ModuleCat.of A (RingHom.ker q), C'.kernelIsSiteModule⟩ =>
          C'.equiv a ≫ f))
```

**`Deformation.Artin.infinitesimalAutTransport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/LiftCompositionActions.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/LiftCompositionActions.lean#L143). The attribute's comment: “actions\_agree”.

> **The identification of the two groups of relative infinitesimal automorphisms.** A
> morphism of lifts identifies the relative infinitesimal automorphisms of its source with
> those of its target, by conjugation.

```lean
public noncomputable def infinitesimalAutTransport
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x) (f : t₁ ⟶ t₂) :
    infinitesimalAutomorphisms hp t₁ ≃* infinitesimalAutomorphisms hp t₂
```

**`Deformation.Artin.leftCompositionAction_eq_rightCompositionAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/LiftCompositionActions.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/LiftCompositionActions.lean#L199). The attribute's comment: “actions\_agree”.

> **The two actions agree.** The left action of a relative infinitesimal automorphism of the
> source lift on a morphism of lifts is the right action, on the same morphism, of the
> corresponding relative infinitesimal automorphism of the target lift.

```lean
public theorem leftCompositionAction_eq_rightCompositionAction
    (hp : Deformation.IsCofiberedInGroupoids p)
    (t₁ t₂ : Deformation.Lift p g x)
    (a : infinitesimalAutomorphisms hp t₁) (f : t₁ ⟶ t₂) :
    leftCompositionAction hp t₁ t₂ a f =
      rightCompositionAction hp t₁ t₂ f (infinitesimalAutTransport hp t₁ t₂ f a)
```

## Tag 07YE, a remark

[Tag 07YE](https://stacks.math.columbia.edu/tag/07YE) in the Stacks Project.

**`Deformation.Artin.IsShortExactSequence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L640). The attribute's comment: “short\_exact\_sequence\_of\_deformation\_situations”.

> A composable triple of deformation situations is short exact if its kernel sequence
> `0 → I₃ → I₂ → I₁ → 0` is exact. The maps of situations run in the opposite direction
> to the ring homomorphisms `f₂₁ : A₂' → A₁'` and `f₃₂ : A₃' → A₂'`.

```lean
public abbrev IsShortExactSequence {A₁ : Type u₁} {A₂ : Type u₂} {A₃ : Type u₃} {A : Type u}
    [CommRing A₁] [CommRing A₂] [CommRing A₃] [CommRing A]
    (q₁ : A₁ →+* A) (q₂ : A₂ →+* A) (q₃ : A₃ →+* A)
    (f₂₁ : A₂ →+* A₁) (f₃₂ : A₃ →+* A₂) : Prop
```

**`Deformation.Artin.exists_factorization_through_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L653). The attribute's comment: “factorization\_through\_a”.

> The composite `A₃' → A₂' → A₁'` in a short exact sequence of deformation
> situations factors through their common quotient `A`.

```lean
public theorem exists_factorization_through_base
    {A₁ : Type u₁} {A₂ : Type u₂} {A₃ : Type u₃} {A : Type u}
    [CommRing A₁] [CommRing A₂] [CommRing A₃] [CommRing A]
    (q₁ : A₁ →+* A) (q₂ : A₂ →+* A) (q₃ : A₃ →+* A)
    (f₂₁ : A₂ →+* A₁) (f₃₂ : A₃ →+* A₂)
    (h : IsShortExactSequence q₁ q₂ q₃ f₂₁ f₃₂) :
    ∃ g : A →+* A₁, g.comp q₃ = f₂₁.comp f₃₂
```

**`Deformation.Artin.splitExtensionRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal.lean, line 704](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal.lean#L704). The attribute's comment: “canonical\_isomorphism”.

> **The canonical isomorphism `A₁ = A[I₁]`.** In a short exact sequence of deformation
> situations, the splitting of `q₁` produced by `exists_factorization_through_base` exhibits
> `A₁` as the trivial square-zero extension of `A` by its kernel `I₁ = ker q₁`.

```lean
noncomputable def splitExtensionRingEquiv
    {A₁ : Type u₁} {A₂ : Type u₂} {A₃ : Type u₃} {A : Type u}
    [CommRing A₁] [CommRing A₂] [CommRing A₃] [CommRing A]
    {q₁ : A₁ →+* A} {q₂ : A₂ →+* A} {q₃ : A₃ →+* A}
    {f₂₁ : A₂ →+* A₁} {f₃₂ : A₃ →+* A₂}
    (h : IsShortExactSequence q₁ q₂ q₃ f₂₁ f₃₂) :
    letI := kerModule q₁ h.1
    letI : Module Aᵐᵒᵖ (RingHom.ker q₁) :=
      Module.compHom _ (RingHom.fromOpposite (RingHom.id A) fun _ _ => Commute.all _ _)
    letI : IsCentralScalar A (RingHom.ker q₁) := ⟨fun _ _ => rfl⟩
    A₁ ≃+* TrivSqZeroExt A (RingHom.ker q₁)
```

## Tag 0DNN, a lemma

[Tag 0DNN](https://stacks.math.columbia.edu/tag/0DNN) in the Stacks Project.

**`Deformation.Artin.injective_twoFibreInfProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/Functoriality/InfTransportSixTerm.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/Functoriality/InfTransportSixTerm.lean#L578). The attribute's comment: “exactness of the six-term sequence at Inf\_w(M), i.e. injectivity of Inf\_w(M) → Inf\_x(M) ⊕ Inf\_z(M), which is what exactness of 0 → Inf\_w(M) → ⋯ says (see exact\_zero\_iff\_injective). Also constructed in this module, and used to state that map, are the four functoriality maps of Remark 07YA out of the 2-fibre product and out of 𝒳 (infLinearMapOfOneMorphism, tangentLinearMapOfOneMorphism) and the zeros of Inf\_x(M) and T\_x(M) (autEquiv\_zero, liftEquiv\_zero). The sequence with all five of its maps and the exactness at all five of its places is Deformation.Artin.twoFibre\_sixTermExact in StacksFrontier.Deformation.Artin.Infinitesimal.TwoFibreInfExact.”.

> **Exactness of the six-term sequence of Stacks 0DNN at `Inf_w(M)`**: an infinitesimal
> automorphism of the trivial deformation of `w` is determined by its two components.  Each
> component is read off through the comparison of the trivial deformation of the component with
> the image of the trivial deformation of `w`, and that comparison is invertible because the
> lifts form a category fibred in groupoids; a morphism of the `2`-fibre product is determined
> by its two components.

```lean
public theorem injective_twoFibreInfProj (A : Type u) [CommRing A] (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (toS : Spec (.of A) ⟶ S)
    (hA : B.Contains (Spec (.of A)))
    {𝒳 : Type v₁} [Category.{w₁} 𝒳] {𝒵 : Type v₂} [Category.{w₂} 𝒵]
    {𝒴 : Type v₃} [Category.{w₃} 𝒴]
    (p𝒳 : 𝒳 ⥤ BigFppfOver B S hS) (p𝒵 : 𝒵 ⥤ BigFppfOver B S hS)
    (p𝒴 : 𝒴 ⥤ BigFppfOver B S hS) (P : 𝒳 ⥤ 𝒴) (Q : 𝒵 ⥤ 𝒴)
    (hP : P ⋙ p𝒴 = p𝒳) (hQ : Q ⋙ p𝒴 = p𝒵)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒵 : p𝒵.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (w : TwoFibreProductOver p𝒳 p𝒵 p𝒴 P Q)
    (hw : (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q).obj w = algebraOver A B S hS toS hA)
    (InfW : InfinitesimalAutomorphismFunctorData A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
        (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ))
    (InfX : InfinitesimalAutomorphismFunctorData A B S hS toS hA p𝒳 w.x (w.hx.trans hw) h𝒳)
    (InfZ : InfinitesimalAutomorphismFunctorData A B S hS toS hA p𝒵 w.y (w.hy.trans hw) h𝒵)
    (M : SiteModule A B) :
    Function.Injective (LinearMap.prod
        (infLinearMapOfOneMorphism A B S hS toS hA
            (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳 (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴
              P Q) TwoFibreProductOver.fst_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳
              p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ) h𝒳
            InfW InfX M)
        (infLinearMapOfOneMorphism A B S hS toS hA
            (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒵 (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴
              P Q) TwoFibreProductOver.snd_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳
              p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ) h𝒵
            InfW InfZ M))
```

**`Deformation.Artin.twoFibreInfSideMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean, line 581](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean#L581). The attribute's comment: “the map `Inf_z(M) → Inf_y(M)` of the six-term sequence -- the map of Remark 07YA induced by q, followed by the transport along the comparison isomorphism of w. The sequence and its exactness are Deformation.Artin.twoFibre\_sixTermExact.”.

> **The `𝒵`-side map `Inf_z(M) ⟶ Inf_y(M)` of the six-term sequence of Stacks 0DNN**: the
> map induced by `q` on infinitesimal automorphisms, followed by the identification of the
> invariants of `q z` with those of `y = p x` along the comparison isomorphism of `w`.

```lean
public def twoFibreInfSideMap
    (InfZ : InfinitesimalAutomorphismFunctorData A B S hS toS hA p𝒵 w.y
      (twoFibreSndOver A B S hS toS hA w hw) h𝒵)
    (InfY' : InfinitesimalAutomorphismFunctorData A B S hS toS hA p𝒴 (P.obj w.x)
      (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴)
    (M : SiteModule A B) : InfZ.functor.obj M →ₗ[A] InfY'.functor.obj M
```

**`Deformation.Artin.twoFibreTangentSideMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean#L612). The attribute's comment: “the map `T_z(M) → T_y(M)` of the six-term sequence -- the map of Remark 07YA induced by q, followed by the transport along the comparison isomorphism of w. The sequence and its exactness are Deformation.Artin.twoFibre\_sixTermExact.”.

> **The `𝒵`-side map `T_z(M) ⟶ T_y(M)` of the six-term sequence of Stacks 0DNN**: the map
> induced by `q` on tangent spaces, followed by the identification of the invariants of `q z`
> with those of `y = p x` along the comparison isomorphism of `w`.

```lean
public def twoFibreTangentSideMap
    (TZ : TangentFunctorData A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w hw))
    (TY : TangentFunctorData A B S hS toS hA p𝒴 (P.obj w.x)
      (twoFibreFstImageOver A B S hS toS hA hP w hw))
    (M : SiteModule A B) : TZ.functor.obj M →ₗ[A] TY.functor.obj M
```

**`Deformation.Artin.boundaryLinearMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean#L675). The attribute's comment: “the boundary map `δ : Inf_y(M) → T_w(M)` of the six-term sequence, as an A-linear map: an automorphism α of the trivial deformation y' of y = p x over A[M] is sent to the deformation (x', z', p x' → y' --α--> y' → q z') of w, exactly as in the source. The sequence and its exactness at all five places are Deformation.Artin.twoFibre\_sixTermExact.”.

> **The boundary map `δ : Inf_y(M) ⟶ T_w(M)` of Stacks 0DNN, as an `A`-linear map.**

```lean
public def boundaryLinearMap (M : SiteModule A B) :
    InfY.functor.obj M →ₗ[A] TW.functor.obj M
```

**`Deformation.Artin.tangentProj_twoFibreBoundaryMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean, line 733](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreBoundary.lean#L733). The attribute's comment: “one inclusion of exactness at T\_w(M): the composite Inf\_y(M) → T\_w(M) → T\_x(M) ⊕ T\_z(M) of the six-term sequence is zero, the two components of δ(α) being by construction the trivial deformations of x and of z. The exactness assertion itself is Deformation.Artin.exact\_boundary\_tangentProj, and the whole sequence is Deformation.Artin.twoFibre\_sixTermExact.”.

> **The six-term sequence of Stacks 0DNN is a complex at `T_w(M)`**: the boundary map
> followed by the pair of projections to the tangent spaces of `x` and of `z` is zero, because
> the two components of `δ(α)` are the trivial deformations.

```lean
public theorem tangentProj_twoFibreBoundaryMap_eq_zero
    (TX : TangentFunctorData A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w hw))
    (TZ : TangentFunctorData A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w hw))
    (M : SiteModule A B) (α : InfY.functor.obj M) :
    LinearMap.prod
        (tangentLinearMapOfOneMorphism A B S hS toS hA
          (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳
          (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 P Q) TwoFibreProductOver.fst_comp_eq w hw TW TX
          h𝒳 M)
        (tangentLinearMapOfOneMorphism A B S hS toS hA
          (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒵
          (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 P Q) TwoFibreProductOver.snd_comp_eq w hw TW TZ
          h𝒵 M)
        (boundaryLinearMap A B S hS toS hA hP hQ h𝒳 h𝒵 h𝒴 w hw InfY TW M α) = 0
```

**`Deformation.Artin.twoFibre_sixTermExact_of_satisfiesRSStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreSixTerm.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/TwoFibreSixTerm.lean#L61).

> **Stacks 0DNN.** Let `P : 𝒳 ⟶ 𝒴` and `Q : 𝒵 ⟶ 𝒴` be `1`-morphisms of categories fibred in
> groupoids over the big fppf site of `S`, and assume `𝒳`, `𝒴`, `𝒵` satisfy (RS\*). Let `w` be an
> object of `𝒲 = 𝒳 ×_𝒴 𝒵` over `Spec A`, with components `x`, `z` and `y = P x`. For every
> `A`-module `M` the six-term sequence
>
> `0 ⟶ Inf_w(M) ⟶ Inf_x(M) ⊕ Inf_z(M) ⟶ Inf_y(M) --δ--> T_w(M) ⟶ T_x(M) ⊕ T_z(M) ⟶ T_y(M)`
>
> of `A`-modules is exact. Here `Inf_?` and `T_?` are the `A`-linear functors that (RS\*)
> produces (Stacks 07Y9), for `w` through (RS\*) for `𝒲` (Stacks 0CXQ); the horizontal maps
> are those of Remark 07YA and `δ` is `Deformation.Artin.boundaryLinearMap`. Exactness is
> stated as injectivity of the first map together with four `Function.Exact`s.

```lean
public theorem twoFibre_sixTermExact_of_satisfiesRSStar
    (hRS𝒳 : SatisfiesRSStar B S hS p𝒳 h𝒳) (hRS𝒵 : SatisfiesRSStar B S hS p𝒵 h𝒵)
    (hRS𝒴 : SatisfiesRSStar B S hS p𝒴 h𝒴) (M : SiteModule A B) :
    Function.Injective (LinearMap.prod (infLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳 (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.fst_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳
      h𝒵 h𝒴 hP hQ) h𝒳 (infinitesimalAutomorphismFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w
      hw) h𝒳 hRS𝒳) M) (infLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒵 (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.snd_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳
      h𝒵 h𝒴 hP hQ) h𝒵 (infinitesimalAutomorphismFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w
      hw) h𝒵 hRS𝒵) M)) ∧ Function.Exact (LinearMap.prod (infLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳 (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.fst_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳
      h𝒵 h𝒴 hP hQ) h𝒳 (infinitesimalAutomorphismFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w
      hw) h𝒳 hRS𝒳) M) (infLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒵 (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.snd_comp_eq w hw (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳
      h𝒵 h𝒴 hP hQ) h𝒵 (infinitesimalAutomorphismFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w
      hw) h𝒵 hRS𝒵) M)) (LinearMap.coprod (infLinearMapOfOneMorphism A B S hS toS hA p𝒳 p𝒴 P hP w.x
      (twoFibreFstOver A B S hS toS hA w hw) h𝒳 h𝒴 (infinitesimalAutomorphismFunctor A B S hS toS hA
      p𝒳 w.x (twoFibreFstOver A B S hS toS hA w hw) h𝒳 hRS𝒳) (infinitesimalAutomorphismFunctor A B S
      hS toS hA p𝒴 (P.obj w.x) (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴 hRS𝒴) M)
      (-(twoFibreInfSideMap A B S hS toS hA hP hQ h𝒵 h𝒴 w hw (infinitesimalAutomorphismFunctor A B S
      hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w hw) h𝒵 hRS𝒵)
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒴 (P.obj w.x) (twoFibreFstImageOver A B S
      hS toS hA hP w hw) h𝒴 hRS𝒴) M))) ∧ Function.Exact (LinearMap.coprod (infLinearMapOfOneMorphism
      A B S hS toS hA p𝒳 p𝒴 P hP w.x (twoFibreFstOver A B S hS toS hA w hw) h𝒳 h𝒴
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w
      hw) h𝒳 hRS𝒳) (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒴 (P.obj w.x)
      (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴 hRS𝒴) M) (-(twoFibreInfSideMap A B S hS toS
      hA hP hQ h𝒵 h𝒴 w hw (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver
      A B S hS toS hA w hw) h𝒵 hRS𝒵) (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒴 (P.obj
      w.x) (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴 hRS𝒴) M))) (boundaryLinearMap A B S hS
      toS hA hP hQ h𝒳 h𝒵 h𝒴 w hw (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒴 (P.obj w.x)
      (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴 hRS𝒴) (tangentFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵)) M) ∧
      Function.Exact (boundaryLinearMap A B S hS toS hA hP hQ h𝒳 h𝒵 h𝒴 w hw
      (infinitesimalAutomorphismFunctor A B S hS toS hA p𝒴 (P.obj w.x) (twoFibreFstImageOver A B S
      hS toS hA hP w hw) h𝒴 hRS𝒴) (tangentFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵)) M)
      (LinearMap.prod (tangentLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳 (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.fst_comp_eq w hw (tangentFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (tangentFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w hw) h𝒳 hRS𝒳) h𝒳 M)
      (tangentLinearMapOfOneMorphism A B S hS toS hA (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴
      P Q) p𝒵 (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 P Q) TwoFibreProductOver.snd_comp_eq w hw
      (tangentFunctor A B S hS toS hA (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (tangentFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w hw) h𝒵 hRS𝒵) h𝒵 M))
      ∧ Function.Exact (LinearMap.prod (tangentLinearMapOfOneMorphism A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) p𝒳 (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 P Q)
      TwoFibreProductOver.fst_comp_eq w hw (tangentFunctor A B S hS toS hA
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (tangentFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver A B S hS toS hA w hw) h𝒳 hRS𝒳) h𝒳 M)
      (tangentLinearMapOfOneMorphism A B S hS toS hA (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴
      P Q) p𝒵 (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 P Q) TwoFibreProductOver.snd_comp_eq w hw
      (tangentFunctor A B S hS toS hA (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 P Q) w hw
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 P Q h𝒳 h𝒵 h𝒴 hP hQ)
      (twoFibreProductOver_satisfiesRSStar B S hS p𝒳 p𝒴 p𝒵 P Q h𝒳 h𝒴 h𝒵 hP hQ hRS𝒳 hRS𝒴 hRS𝒵))
      (tangentFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS hA w hw) h𝒵 hRS𝒵) h𝒵 M))
      (LinearMap.coprod (tangentLinearMapOfOneMorphism A B S hS toS hA p𝒳 p𝒴 P hP w.x
      (twoFibreFstOver A B S hS toS hA w hw) (tangentFunctor A B S hS toS hA p𝒳 w.x (twoFibreFstOver
      A B S hS toS hA w hw) h𝒳 hRS𝒳) (tangentFunctor A B S hS toS hA p𝒴 (P.obj w.x)
      (twoFibreFstImageOver A B S hS toS hA hP w hw) h𝒴 hRS𝒴) h𝒴 M) (-(twoFibreTangentSideMap A B S
      hS toS hA hP hQ h𝒴 w hw (tangentFunctor A B S hS toS hA p𝒵 w.y (twoFibreSndOver A B S hS toS
      hA w hw) h𝒵 hRS𝒵) (tangentFunctor A B S hS toS hA p𝒴 (P.obj w.x) (twoFibreFstImageOver A B S
      hS toS hA hP w hw) h𝒴 hRS𝒴) M)))
```

## Tag 0D18, a remark

[Tag 0D18](https://stacks.math.columbia.edu/tag/0D18) in the Stacks Project.

**`Deformation.Artin.tangentSpace_deformationCategory_linearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSpaceComparison.lean, line 995](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSpaceComparison.lean#L995). The attribute's comment: “tangent spaces”.

> **Stacks Project, Tag 0D18, tangent spaces.** For a category fibred in groupoids over the
> big fppf site of a locally Noetherian scheme satisfying (RS*), the tangent space of the
> deformation category of a finite-type field-valued point is the value of the tangent functor
> of Tag 07Y9 at the rank-one vector space. Both sides carry the unique linear structure
> compatible with finite products (Tag 06I6), and the identification carries the class of a
> deformation to the class of the corresponding lift.

```lean
public theorem tangentSpace_deformationCategory_linearEquiv
    (B : BigFppfSite.{u}) (S : Scheme.{u}) [IsLocallyNoetherian S] (hS : B.Contains S)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (toS : Spec (.of k) ⟶ S)
    (hk : B.Contains (Spec (.of k)))
    (hfin : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    {X : Type v} [Category.{w} X] (p : X ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hRS : SatisfiesRSStar B S hS p hp) (x₀ : X)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx : p.obj x₀ = algebraOver k B S hS toS hk) :
    let D := predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀
    let 𝓕 := BasedCategory.ofFunctor D.projection
    let hD : Deformation.IsDeformationCategory D.projection :=
      isDeformationCategory_predeformationCategory_of_satisfiesRSStar B S hS p hp hRS iΛ x₀
        hx₀ hfin hqc
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
      ⟨schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD⟩
    let M : SiteModule k B := (fgSiteModule B hk).obj (FGModuleCat.of k k)
    let L := tangentFunctor k B S hS toS hk p x₀ hx hp hRS
    ∃ e : artinianTangentSpace Λ k (isomorphismClasses 𝓕 hD.predeformation.cofibered) ≃ₗ[k]
        L.functor.obj M,
      ∀ z : D.projection.Fiber ((artinianSquareZeroExtensionFunctor Λ k).obj
          (FGModuleCat.of k k)),
        ∃ y : (Under.post p).Fiber
            (Under.mk (eqToHom hx ≫ squareZeroArrow k B S hS toS hk M)),
          L.liftEquiv M (e (classOf 𝓕 hD.predeformation.cofibered z)) = Quotient.mk _ y ∧
            ∃ (η : y.1.right ≅ (D.objects z.1).point)
              (hbase : p.obj y.1.right = p.obj (D.objects z.1).point),
              p.map η.hom = eqToHom hbase ∧
                y.1.hom ≫ η.hom = (D.objects z.1).arrow
```

**`Deformation.Artin.infinitesimalAutomorphisms_deformationCategory_linearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSpaceComparison.lean, line 1417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/DeformationSpaceComparison.lean#L1417). The attribute's comment: “infinitesimal automorphisms”.

> **Stacks Project, Tag 0D18, infinitesimal automorphisms.** For a category fibred in
> groupoids over the big fppf site of a locally Noetherian scheme satisfying (RS*), the
> infinitesimal automorphisms of the deformation category of a finite-type field-valued point
> are the value of the infinitesimal automorphism functor of Tag 07Y9 at the rank-one vector
> space, by a `k`-linear equivalence carrying an automorphism to the endomorphism of the
> trivial deformation given by the same arrow.

```lean
public theorem infinitesimalAutomorphisms_deformationCategory_linearEquiv
    (B : BigFppfSite.{u}) (S : Scheme.{u}) [IsLocallyNoetherian S] (hS : B.Contains S)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (toS : Spec (.of k) ⟶ S)
    (hk : B.Contains (Spec (.of k)))
    (hfin : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    {X : Type v} [Category.{w} X] (p : X ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hRS : SatisfiesRSStar B S hS p hp) (x₀ : X)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx : p.obj x₀ = algebraOver k B S hS toS hk) :
    let D := predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀
    let hD : Deformation.IsDeformationCategory D.projection :=
      isDeformationCategory_predeformationCategory_of_satisfiesRSStar B S hS p hp hRS iΛ x₀
        hx₀ hfin hqc
    let A₀ := (artinianSquareZeroExtensionFunctor Λ k).obj (FGModuleCat.of k PUnit.{u + 1})
    let Aε := (artinianSquareZeroExtensionFunctor Λ k).obj (FGModuleCat.of k k)
    let g : A₀ ⟶ Aε := (artinianSquareZeroExtensionFunctor Λ k).map 0
    let e : Aε ⟶ A₀ := (artinianSquareZeroExtensionFunctor Λ k).map 0
    let M : SiteModule k B := (fgSiteModule B hk).obj (FGModuleCat.of k k)
    let L := infinitesimalAutomorphismFunctor k B S hS toS hk p x₀ hx hp hRS
    let t := trivialDeformation k B S hS toS hk p x₀ hx hp M
    ∃ (hge : g ≫ e = 𝟙 A₀) (z₀ : D.projection.Fiber A₀) (zε : D.projection.Fiber Aε)
      (i : z₀.1 ⟶ zε.1) (hi : D.projection.IsHomLift g i)
      (η : (D.objects zε.1).point ≅ t.1.right),
      let G := ↥(infinitesimalAutomorphismsAlongSplitPair hD.predeformation.cofibered g e hge
        i hi)
      (D.objects zε.1).arrow ≫ η.hom = t.1.hom ∧
        ∃ hA : AddCommGroup G,
          letI : AddCommGroup G := hA
          ∃ hM : Module k G,
            letI : Module k G := hM
            ∃ E : G ≃ₗ[k] (L.functor.obj M : Type w),
              ∀ a : G, (L.autEquiv M (E a)).1.right =
                η.inv ≫ (D.morphisms zε.1 zε.1 a.val.asIso.hom.val).arrow ≫ η.hom
```

**`Deformation.Artin.localizedAutomorphismTangent_deformationCategory_linearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/InfinitesimalAutomorphismsComparison.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/InfinitesimalAutomorphismsComparison.lean#L120). The attribute's comment: “infinitesimal automorphisms”.

> **Stacks Project, Tag 0D18, infinitesimal automorphisms.** For a category fibred in groupoids
> over the big fppf site of a locally Noetherian scheme satisfying (RS*), the infinitesimal
> automorphisms of the deformation category of a finite-type field-valued point `x₀`, with their
> natural vector space structure of Tag 06JX, are the value at the rank-one vector space of the
> infinitesimal automorphism functor of Tag 07Y9: there is a `k`-linear equivalence `E`, which is
> conjugation by any isomorphism `η` of the object underlying the dual-number pushforward with the
> trivial deformation of `x₀` that is compatible with the arrows out of `x₀` and lies over the
> comparison of the two presentations of the dual numbers; such an `η` exists.

```lean
public theorem localizedAutomorphismTangent_deformationCategory_linearEquiv
    (B : BigFppfSite.{u}) (S : Scheme.{u}) [IsLocallyNoetherian S] (hS : B.Contains S)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (toS : Spec (.of k) ⟶ S)
    (hk : B.Contains (Spec (.of k)))
    (hfin : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    {X : Type v} [Category.{w} X] (p : X ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hRS : SatisfiesRSStar B S hS p hp) (x₀ : X)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx : p.obj x₀ = algebraOver k B S hS toS hk)
    (y : (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection.Fiber
      (residueFieldObject.{u, u, u} Λ k))
    (P : ChosenPushforwardsAt
      (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection y.1) :
    let D := predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀
    let hD : Deformation.IsDeformationCategory D.projection :=
      isDeformationCategory_predeformationCategory_of_satisfiesRSStar B S hS p hp hRS iΛ x₀
        hx₀ hfin hqc
    letI := naturalLocalizedTangentAddCommGroup P hD.satisfiesRS
    letI := naturalLocalizedTangentModule P hD.satisfiesRS
    let M : SiteModule k B := (fgSiteModule B hk).obj (FGModuleCat.of k k)
    let L := infinitesimalAutomorphismFunctor k B S hS toS hk p x₀ hx hp hRS
    let t := trivialDeformation k B S hS toS hk p x₀ hx hp M
    let yε := P.obj (dualNumbersUnder (p := D.projection) (x := y.1))
    let IsCompatible : ((D.objects yε.1).point ≅ t.1.right) → Prop := fun η =>
      (D.objects yε.1).arrow ≫ η.hom = t.1.hom ∧
        eqToHom (congrArg Over.left (D.objects yε.1).base).symm ≫
            ((p ⋙ Over.post B.inclusion).map η.hom).left ≫ eqToHom (congrArg Over.left
              (trivialDeformation_right_post B S hS iΛ toS hk p hp x₀ hx₀ hx
                (FGModuleCat.of k k))) =
            Spec.map (CommRingCat.ofHom (CategoryTheory.inv
              (dualNumbersUnderHom (p := D.projection) (x := y.1)) ≫
                eqToHom (yε.2.symm.trans (D.object_projection yε.1))).hom.toRingHom)
    ∃ E : localizedAutomorphismFunctorTangent P ≃ₗ[k] (L.functor.obj M : Type w),
      (∃ η, IsCompatible η) ∧
        ∀ η, IsCompatible η → ∀ a, (L.autEquiv M (E a)).1.right =
          η.inv ≫ (D.morphisms yε.1 yε.1 (localizedTangentEquivKernel P a).1.asIso.hom.1).arrow ≫
            η.hom
```

## Tag 07YC, a remark

[Tag 07YC](https://stacks.math.columbia.edu/tag/07YC) in the Stacks Project.

**`Deformation.Artin.canonicalDeformationElement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElement.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElement.lean#L151). The attribute's comment: “canonical\_deformation\_element”.

> **Stacks 07YC.** The canonical element of `T_x(Ω_{A/Λ})` attached to the universal
> derivation `d : A → Ω_{A/Λ}`.

```lean
public def canonicalDeformationElement (baseMap : Spec (.of Λ) ⟶ S)
    (baseFactorization :
      Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ baseMap = toS) :
    CanonicalDeformationData Λ A B S hS toS hA p x hx hp hRS hΩ
```

**`Deformation.Artin.canonicalTangentMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElement.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElement.lean#L259). The attribute's comment: “the tangent-space map”.

> **Stacks 07YC.** The map on tangent spaces induced by the family `x` over `Spec A`: a
> `Λ`-derivation of `A` with values in `k`, written as an `A`-linear map `Ω_{A/Λ} → k`, carries
> the canonical element to an element of `T_x(k)`.

```lean
public def canonicalTangentMap (θ : Ω[A⁄Λ] →ₗ[A] k) :
    (tangentFunctor A B S hS toS hA p x hx hp hRS).functor.obj
      (⟨ModuleCat.of A k, hk⟩ : SiteModule A B)
```

**`Deformation.Artin.canonicalTangentMap_eq_familyTangentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementInducedTangentMap.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementInducedTangentMap.lean#L743). The attribute's comment: “the canonical element gives the tangent map `T𝓕_{U,k,u₀} ⟶ T𝓕_{𝒳,k,x₀}` induced by `x`: `θ ↦ T_x(θ)(x_can)`”.

> **Stacks 07YC: the canonical element produces the map on tangent spaces induced by `x`.**
>
> Let `𝒳` be a category fibred in groupoids over the big fppf site of a locally Noetherian `S`,
> satisfying (RS*), let `Spec Λ ⊂ S` be an affine open through which `U = Spec A ⟶ S` factors,
> with `A` of finite type over `Λ`, let `x` be an object of `𝒳` over `U`, and let `k` be the
> residue field of a finite type point `u₀` of `U`, with `x₀ = x|_{u₀}`. Then:
>
> * `T_x(k)` is the tangent space of `𝓕_{𝒳,k,x₀}`: the `k`-linear identification `e` below is
>   the one of Stacks 0D18 composed with the (RS*) identification `T_x(k) = T_{x₀}(k)` across
>   `A[k] = A ×_k k[k]`, pinned down by sending the class of a deformation to the class of the
>   corresponding lift;
> * `T𝓕_{U,k,u₀} = Der_Λ(A, k) = Hom_A(Ω_{A/Λ}, k)` (Stacks 06IC), by
>   `Deformation.Artin.derivationTangentEquiv`;
> * through these identifications the map on tangent spaces `T𝓕_{U,k,u₀} ⟶ T𝓕_{𝒳,k,x₀}`
>   induced by the object `x` over `U` (`Deformation.Artin.familyTangentMap`) is
>   `θ ↦ T_x(θ)(x_can)`.
>
> The field `k` is only required to be an `A`-algebra with `Spec k ⟶ U` of finite type, which
> includes the residue field at a finite type point. The containments of the spectra of the
> square-zero extensions in the chosen big site are size conditions on the site.

```lean
public theorem canonicalTangentMap_eq_familyTangentMap [IsLocallyNoetherian S]
    [IsOpenImmersion baseMap] [Algebra.FiniteType Λ A]
    (hpt : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap A k)))) :
    letI : p.IsFibered := hp.isFibered
    let x₀ := (familyMorphism A B S hS toS hA p x hx hp).obj (residuePoint A k B S hS toS hA hAk)
    let D := predeformationCategory baseMap (p ⋙ Over.post B.inclusion) x₀
      (familyMorphism_residuePoint_base Λ A k B S hS toS hA hAk baseMap baseFactorization p x hx
        hp)
    let 𝓕 := BasedCategory.ofFunctor D.projection
    let hD : IsDeformationCategory D.projection :=
      isDeformationCategory_predeformationCategory_of_satisfiesRSStar B S hS p hp hRS baseMap x₀
        (familyMorphism_residuePoint_base Λ A k B S hS toS hA hAk baseMap baseFactorization p x
          hx hp)
        (residue_locallyOfFiniteType Λ A k S toS baseMap baseFactorization hpt)
        (residue_quasiCompact Λ k S baseMap)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
      ⟨schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD⟩
    let M : SiteModule k B := ⟨ModuleCat.of k k, hkk⟩
    let L := tangentFunctor k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk p
      x₀ (familyMorphism_residuePoint_obj A k B S hS toS hA hAk p x hx hp) hp hRS
    ∃ e : artinianTangentSpace Λ k (isomorphismClasses 𝓕 hD.predeformation.cofibered) ≃ₗ[k]
        ((tangentFunctor A B S hS toS hA p x hx hp hRS).functor.obj
          (⟨ModuleCat.of A k, hk⟩ : SiteModule A B) : Type max (u + 1) v w),
      (∀ z : D.projection.Fiber ((artinianSquareZeroExtensionFunctor Λ k).obj
          (FGModuleCat.of k k)),
        ∃ y : (Under.post p).Fiber (Under.mk (eqToHom
            (familyMorphism_residuePoint_obj A k B S hS toS hA hAk p x hx hp) ≫
              squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS)
                hAk M)),
          L.liftEquiv M (residueTangentEquiv A k B S hS toS hA p x hx hp hRS hk hAk hkk
              (e (classOf 𝓕 hD.predeformation.cofibered z))) = Quotient.mk _ y ∧
            ∃ (η : y.1.right ≅ (D.objects z.1).point)
              (hbase : p.obj y.1.right = p.obj (D.objects z.1).point),
              p.map η.hom = eqToHom hbase ∧ y.1.hom ≫ η.hom = (D.objects z.1).arrow) ∧
      ∀ θ : Ω[A⁄Λ] →ₗ[A] k,
        e (familyTangentMap Λ A k B S hS toS hA hAk baseMap baseFactorization p x hx hp
            (derivationTangentEquiv Λ A k B S hS toS hA hAk baseMap baseFactorization θ)) =
          (tangentFunctor A B S hS toS hA p x hx hp hRS).functor.map
            (⟨ModuleCat.ofHom θ⟩ : differentialsSiteModule Λ A B hΩ ⟶
              (⟨ModuleCat.of A k, hk⟩ : SiteModule A B))
            (canonicalDeformationElement Λ A B S hS toS hA p x hx hp hRS hΩ baseMap
              baseFactorization).element
```

**`Deformation.Artin.residueSquareZeroRing_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean#L251). The attribute's comment: “the fibre product `A[k] = A ×_k k[k]`”.

> **Stacks 07YC: the square `A[k] = A ×_k k[k]`.** For a ring map `A ⟶ k` to a field, the
> trivial square-zero extension `A[k]` is the fibre product of `A` and `k[k]` over `k`. The
> orientation is the one in which condition (RS*) reads a square: the pullback corner is `A[k]`,
> and the square-zero surjection is the projection `k[k] ⟶ k` appearing as the fourth map.
>
> This is `Deformation.Artin.squareZeroRingBaseMap_isPullback` at the residue map, with
> `Deformation.Artin.coeffCompare` — the identity of `k`, comparing the two module structures the
> `A`-algebra `k` puts on itself — as the semilinear bijection of coefficients.

```lean
public theorem residueSquareZeroRing_isPullback :
    IsPullback (CommRingCat.ofHom (TrivSqZeroExt.fstHom A A (ModuleCat.of A k)).toRingHom)
      (CommRingCat.ofHom (squareZeroRingBaseMap (algebraMap A k) (coeffCompare A k)
        (coeffCompare_smul A k)))
      (CommRingCat.ofHom (algebraMap A k))
      (CommRingCat.ofHom (TrivSqZeroExt.fstHom k k (ModuleCat.of k k)).toRingHom)
```

**`Deformation.Artin.residueTangentEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean#L430). The attribute's comment: “`T_x(k)` is the tangent space of the deformation functor at the residue field”.

> **Stacks 07YC: `T_x(k)` is the tangent space at the residue field.** By (RS\*) and the
> square `A[k] = A ×_k k[k]`, the tangent module `T_x(k)` of `x` at the coefficient module `k`
> is the tangent module `T_{x₀}(k)` of the restriction `x₀ = x|_{Spec k}` at the rank-one
> `k`-vector space, which by Stacks 0D18 is the tangent space of the deformation category
> `𝓕_{𝒳,k,x₀}`.
>
> This is an identification of `k`-vector spaces: on the left the structure
> `Deformation.Artin.residueTangentModule` that the `A`-linear tangent functor of Stacks 07Y9
> puts on its value at the algebra coefficient `k`, on the right the structure the rank-one
> `k`-vector space gives the value of the tangent functor over `k`, which is the one Stacks 0D18
> transports from the deformation category. Additivity is
> `Deformation.Artin.residueTangentBaseChange_map_add` and the scalar action is
> `Deformation.Artin.residueTangentBaseChange_map_smul`.
>
> The identification itself is the (RS\*) comparison of lift classes
> `Deformation.Artin.canonicalFieldBaseChangeEquiv` transported along the identifications
> `T_x(M) = Lift(x, A[M])` of the tangent functor data of Stacks 07Y9 on both sides, which is
> `Deformation.Artin.tangentBaseChangeEquiv` at the residue map.

```lean
public def residueTangentEquiv :
    letI : p.IsFibered := hp.isFibered
    ((tangentFunctor A B S hS toS hA p x hx hp hRS).functor.obj
        (⟨ModuleCat.of A k, hk⟩ : SiteModule A B) : Type max (u + 1) v w) ≃ₗ[k]
      ((tangentFunctor k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk p
          (((Functor.chosenPullbacks p).pullbackFunctor
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj
                ⟨x, hx⟩).1
          (((Functor.chosenPullbacks p).pullbackFunctor
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj
                ⟨x, hx⟩).2
          hp hRS).functor.obj
        (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B) : Type max (u + 1) v w)
```

**`Deformation.Artin.canonicalTangentMapRestrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Infinitesimal/CanonicalElementTangentSpace.lean#L509). The attribute's comment: “`θ ↦ T_x(θ)(x_can)` in `T_x(k) = T𝓕_{𝒳,k,x₀}`”.

> **Stacks 07YC: the canonical element produces the map on tangent spaces.** A tangent vector
> of `Spec A` at the point with residue field `k` — that is, an element of
> `Der_Λ(A, k) = Hom_A(Ω_{A/Λ}, k)`, the identification being Stacks 00RO
> (`KaehlerDifferential.linearMapEquivDerivation`) — is carried to `T_x(θ)(x_can)`, read in
> `T_{x₀}(k)`, which is the tangent space `T𝓕_{𝒳,k,x₀}` by Stacks 0D18.

```lean
public def canonicalTangentMapRestrict (θ : Ω[A⁄Λ] →ₗ[A] k) :
    letI : p.IsFibered := hp.isFibered
    ((tangentFunctor k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk p
        (((Functor.chosenPullbacks p).pullbackFunctor
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj ⟨x, hx⟩).1
        (((Functor.chosenPullbacks p).pullbackFunctor
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj ⟨x, hx⟩).2
        hp hRS).functor.obj
      (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B) : Type max (u + 1) v w)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.21, Tag 07Y6](https://stacks.math.columbia.edu/tag/07Y6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
