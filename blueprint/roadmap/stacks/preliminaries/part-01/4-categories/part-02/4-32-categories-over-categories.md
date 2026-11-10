---
declaration: section
origin: cited
lean: CategoryTheory.BasedCategory, CategoryTheory.BasedFunctor, CategoryTheory.BasedNatTrans, CategoryTheory.BasedNatTrans.homCategory, CategoryTheory.BasedCategory.bicategory, CategoryTheory.Functor.Fiber, CategoryTheory.Functor.Fiber.fiberCategory, CategoryTheory.Functor.IsHomLift
statement: formalized
proof: formalized
---

# 4.32 Categories over categories

Section 4.32 of the Stacks Project, [Tag 02XG](https://stacks.math.columbia.edu/tag/02XG). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 003Y, a definition

[Tag 003Y](https://stacks.math.columbia.edu/tag/003Y) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.BasedCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BasedCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L70) (StacksFrontier): “objects: functors p : S → C”.
- [`CategoryTheory.BasedFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BasedFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L71) (StacksFrontier): “1-morphisms: functors G with p' ∘ G = p”.
- [`CategoryTheory.BasedNatTrans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BasedNatTrans#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L72) (StacksFrontier): “2-morphisms”.
- [`CategoryTheory.BasedNatTrans.homCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BasedNatTrans.homCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L73) (StacksFrontier): “the category Mor\_\{Cat/C}(S, S')”. References: SGA 4 VI (6.0).
- [`CategoryTheory.BasedCategory.bicategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BasedCategory.bicategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L74) (StacksFrontier): “the 2-category structure”.

## Tag 02XH, a definition

[Tag 02XH](https://stacks.math.columbia.edu/tag/02XH) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.Fiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Fiber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L34) (StacksFrontier): “(1) objects of the fibre category, (2) lifts of an object”. References: SGA 4 V (8.1.0), “partial”; SGA 4 VI (6.1.1).
- [`CategoryTheory.Functor.Fiber.fiberCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Fiber.fiberCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L38) (StacksFrontier): “(1) morphisms of the fibre category”. References: SGA 4 V (8.1.0); SGA 4 VI (6.1.1).
- [`CategoryTheory.Functor.IsHomLift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsHomLift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L41) (StacksFrontier): “(3) lift of a morphism”.

## Tag 0040, a lemma

[Tag 0040](https://stacks.math.columbia.edu/tag/0040) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.fibreIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L77).

> Clause (1) of Stacks 0040: the comparison isomorphism `φ` of an object `(U, x, y, φ)` is an
> isomorphism `F x ≅ G y` *in the fibre category* `𝒮_U`. Both `F x` and `G y` lie over `U` because
> `F` and `G` are 1-morphisms over `𝒞`, and `φ` is vertical by construction.

```lean
def fibreIso (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (P : TwoFibreProductOver p𝒳 p𝒴 p𝒮 F G) :
    Functor.Fiber.mk (obj_over_base_x p𝒳 p𝒴 p𝒮 F G hF P) ≅
      Functor.Fiber.mk (obj_over_base_y p𝒳 p𝒴 p𝒮 F G hG P)
```

**`CategoryTheory.TwoFibreProductOver.lift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L96).

> The mediating 1-morphism `γ : W ⥤ 𝒳 ×_𝒮 𝒴` of Stacks 0040, sending `w` to the quadruple
> `(pW w, H w, K w, t w)`. That `H` and `K` are 1-morphisms over `𝒞` is what makes the two components
> of `γ h` lie over the common base morphism `pW h`, and the comparison square is the naturality
> of `t`.

```lean
def lift : W ⥤ TwoFibreProductOver p𝒳 p𝒴 p𝒮 F G
```

**`CategoryTheory.TwoFibreProductOver.lift_comp_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L151).

> The mediating 1-morphism is a 1-morphism of categories over `𝒞`: it sends `w` to an object
> lying over `pW w`, and a morphism to one lying over `pW h`.

```lean
theorem lift_comp_structureFunctor :
    lift p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht ⋙ structureFunctor p𝒳 p𝒴 p𝒮 F G = pW
```

**`CategoryTheory.TwoFibreProductOver.liftCompFst_hom_app_isHomLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L168).

> The first comparison isomorphism is a 2-morphism over `𝒞`: its components are vertical.

```lean
theorem liftCompFst_hom_app_isHomLift (w : W) :
    p𝒳.IsHomLift (𝟙 (pW.obj w)) ((liftCompFst p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht).hom.app w)
```

**`CategoryTheory.TwoFibreProductOver.liftCompSnd_hom_app_isHomLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L174).

> The second comparison isomorphism is a 2-morphism over `𝒞`: its components are vertical.

```lean
theorem liftCompSnd_hom_app_isHomLift (w : W) :
    p𝒴.IsHomLift (𝟙 (pW.obj w)) ((liftCompSnd p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht).hom.app w)
```

**`CategoryTheory.TwoFibreProductOver.lift_whiskerRight_psi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L183).

> The factorisation is compatible with the given isomorphism `t`: whiskering the 2-cell `ψ` into
> `γ` and correcting by the two comparison isomorphisms recovers `t`. This is the commuting square of
> 2-morphisms which makes `γ` a factorisation of the test cone `(H, K, t)`, rather than merely a
> 1-morphism with the right two projections.

```lean
theorem lift_whiskerRight_psi :
    Functor.whiskerRight (liftCompFst p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht).hom F ≫ t.hom =
      Functor.whiskerLeft (lift p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht) (psiIso p𝒳 p𝒴 p𝒮 F G).hom ≫
        Functor.whiskerRight (liftCompSnd p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht).hom G
```

**`CategoryTheory.TwoFibreProductOver.natTrans_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L213).

> Two 2-morphisms into the 2-fibre product that agree after projecting to `𝒳` and to `𝒴` are
> equal, so the mediating 2-morphism supplied by `liftIso` is the only one.

```lean
theorem natTrans_ext {γ δ : W ⥤ TwoFibreProductOver p𝒳 p𝒴 p𝒮 F G} {α β : γ ⟶ δ}
    (h₁ : Functor.whiskerRight α (fst p𝒳 p𝒴 p𝒮 F G) =
      Functor.whiskerRight β (fst p𝒳 p𝒴 p𝒮 F G))
    (h₂ : Functor.whiskerRight α (snd p𝒳 p𝒴 p𝒮 F G) =
      Functor.whiskerRight β (snd p𝒳 p𝒴 p𝒮 F G)) : α = β
```

**`CategoryTheory.TwoFibreProductOver.liftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverBase.lean#L230).

> Any other factorisation of the test cone `(H, K, t)` through the 2-fibre product is
> 2-isomorphic over `𝒞` to the mediating 1-morphism `lift`. Together with `natTrans_ext` this is the
> uniqueness half of the 2-universal property: the factorisation is unique up to a unique
> 2-isomorphism over `𝒞`.

```lean
noncomputable def liftIso (γ : W ⥤ TwoFibreProductOver p𝒳 p𝒴 p𝒮 F G)
    (a : γ ⋙ fst p𝒳 p𝒴 p𝒮 F G ≅ H) (b : γ ⋙ snd p𝒳 p𝒴 p𝒮 F G ≅ K)
    (ha : ∀ w, p𝒳.IsHomLift (𝟙 (pW.obj w)) (a.hom.app w))
    (hb : ∀ w, p𝒴.IsHomLift (𝟙 (pW.obj w)) (b.hom.app w))
    (hab : Functor.whiskerRight a.hom F ≫ t.hom =
      Functor.whiskerLeft γ (psiIso p𝒳 p𝒴 p𝒮 F G).hom ≫ Functor.whiskerRight b.hom G)
    (hH : H ⋙ p𝒳 = pW) (hK : K ⋙ p𝒴 = pW)
    (ht : ∀ w, p𝒮.IsHomLift (𝟙 (pW.obj w)) (t.hom.app w)) :
    γ ≅ lift p𝒳 p𝒴 p𝒮 F G pW H K hH hK t ht
```

**`CategoryTheory.TwoFibreProductOver.fst_comp_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProductOver.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProductOver.lean#L207).

> The first projection is strictly over `𝒞`.

```lean
lemma fst_comp_eq : fst p𝒳 p𝒴 p𝒮 F G ⋙ p𝒳 = structureFunctor p𝒳 p𝒴 p𝒮 F G
```

**`CategoryTheory.TwoFibreProductOver.snd_comp_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProductOver.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProductOver.lean#L214).

> The second projection is strictly over `𝒞`.

```lean
lemma snd_comp_eq : snd p𝒳 p𝒴 p𝒮 F G ⋙ p𝒴 = structureFunctor p𝒳 p𝒴 p𝒮 F G
```

**`CategoryTheory.TwoFibreProductOver.psiIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProductOver.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProductOver.lean#L222).

> The 2-cell `ψ : π₁ ⋙ F ≅ π₂ ⋙ G` filling the square, with component at
> `(U, x, y, φ)` the comparison isomorphism `φ` itself.

```lean
def psiIso (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮) :
    (fst p𝒳 p𝒴 p𝒮 F G ⋙ F) ≅ (snd p𝒳 p𝒴 p𝒮 F G ⋙ G)
```

**`CategoryTheory.TwoFibreProductOver.psiIso_hom_vertical`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProductOver.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProductOver.lean#L237).

> Every component of the 2-cell `ψ` is vertical over `𝒞`: it lies over an identity.

```lean
lemma psiIso_hom_vertical (P : TwoFibreProductOver p𝒳 p𝒴 p𝒮 F G) :
    p𝒮.IsHomLift (𝟙 P.base) ((psiIso p𝒳 p𝒴 p𝒮 F G).hom.app P)
```

## Tag 02XI, a lemma

[Tag 02XI](https://stacks.math.columbia.edu/tag/02XI) in the Stacks Project.

**`CategoryTheory.Limits.CategoricalPullbackOver.toFiberPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean#L295).

> **Stacks 02XI.** The canonical functor `(X ×_S Y)_U ⥤ X_U ×_{S_U} Y_U`, sending
> `(U, x, y, f)` to `(x, y, f)` and `(a, b)` to `(a, b)`.

```lean
def toFiberPullback (hf : F ⋙ pS = pX) (hg : G ⋙ pS = pY) (U : C) :
    (CategoricalPullbackOver.structureFunctor (pX := pX) (pY := pY) (pS := pS) (F := F)
      (G := G)).Fiber U ⥤
    CategoricalPullback (Functor.fiberMap pX pS F hf U) (Functor.fiberMap pY pS G hg U)
```

**`CategoryTheory.Limits.CategoricalPullbackOver.ofFiberPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean#L317).

> **Stacks 02XI.** The canonical functor `X_U ×_{S_U} Y_U ⥤ (X ×_S Y)_U` inverse to
> `toFiberPullback`, sending `(x, y, f)` to `(U, x, y, f)` and `(a, b)` to `(a, b)`.

```lean
def ofFiberPullback (hf : F ⋙ pS = pX) (hg : G ⋙ pS = pY) (U : C) :
    CategoricalPullback (Functor.fiberMap pX pS F hf U) (Functor.fiberMap pY pS G hg U) ⥤
    (CategoricalPullbackOver.structureFunctor (pX := pX) (pY := pY) (pS := pS) (F := F)
      (G := G)).Fiber U
```

**`CategoryTheory.Limits.CategoricalPullbackOver.toFiberPullback_comp_ofFiberPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean#L425).

> **Stacks 02XI.** Composing the comparison functor with its inverse gives the identity on the
> fibre `(X ×_S Y)_U`.

```lean
theorem toFiberPullback_comp_ofFiberPullback (hf : F ⋙ pS = pX) (hg : G ⋙ pS = pY) (U : C) :
    toFiberPullback pX pY pS F G hf hg U ⋙ ofFiberPullback pX pY pS F G hf hg U = 𝟭 _
```

**`CategoryTheory.Limits.CategoricalPullbackOver.ofFiberPullback_comp_toFiberPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/Fibres.lean#L439).

> **Stacks 02XI.** Composing the inverse comparison functor with the comparison functor gives
> the identity on `X_U ×_{S_U} Y_U`. Together with
> `toFiberPullback_comp_ofFiberPullback` this says the fibre of the 2-fibre product over `C` at `U`
> is *isomorphic*, not merely equivalent, to the 2-fibre product of the fibres.

```lean
theorem ofFiberPullback_comp_toFiberPullback (hf : F ⋙ pS = pX) (hg : G ⋙ pS = pY) (U : C) :
    ofFiberPullback pX pY pS F G hf hg U ⋙ toFiberPullback pX pY pS F G hf hg U = 𝟭 _
```

**`CategoryTheory.TwoFibreProductOver.toFiberPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean#L48).

> **Stacks 02XI.** The canonical functor `(𝒳 ×_𝒮 𝒴)_U ⥤ 𝒳_U ×_{𝒮_U} 𝒴_U`, sending
> `(U, x, y, φ)` to `(x, y, φ)` and `(a, b)` to `(a, b)`.

```lean
def toFiberPullback (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (U : 𝒞) :
    (structureFunctor p𝒳 p𝒴 p𝒮 F G).Fiber U ⥤
      CategoricalPullback (Functor.fiberMap p𝒳 p𝒮 F hF U) (Functor.fiberMap p𝒴 p𝒮 G hG U)
```

**`CategoryTheory.TwoFibreProductOver.ofFiberPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean#L67).

> **Stacks 02XI.** The canonical functor `𝒳_U ×_{𝒮_U} 𝒴_U ⥤ (𝒳 ×_𝒮 𝒴)_U` inverse to
> `toFiberPullback`, sending `(x, y, φ)` to `(U, x, y, φ)` and `(a, b)` to `(a, b)` over `𝟙 U`.

```lean
def ofFiberPullback (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (U : 𝒞) :
    CategoricalPullback (Functor.fiberMap p𝒳 p𝒮 F hF U) (Functor.fiberMap p𝒴 p𝒮 G hG U) ⥤
      (structureFunctor p𝒳 p𝒴 p𝒮 F G).Fiber U
```

**`CategoryTheory.TwoFibreProductOver.toFiberPullback_comp_ofFiberPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean#L166).

> **Stacks 02XI.** Composing the comparison functor with its inverse gives the identity on the
> fibre `(𝒳 ×_𝒮 𝒴)_U`: the round trip forgets the base object and reinstates it as the literal
> `U`, which is the same object because it lies over `U`, and both functors are the identity on the
> underlying pair of components.

```lean
theorem toFiberPullback_comp_ofFiberPullback (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (U : 𝒞) :
    toFiberPullback p𝒳 p𝒴 p𝒮 F G hF hG U ⋙ ofFiberPullback p𝒳 p𝒴 p𝒮 F G hF hG U = 𝟭 _
```

**`CategoryTheory.TwoFibreProductOver.ofFiberPullback_comp_toFiberPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean#L181).

> **Stacks 02XI.** Composing the inverse comparison functor with the comparison functor gives
> the identity on `𝒳_U ×_{𝒮_U} 𝒴_U`: the base coordinate `U` is added and then forgotten, so the
> triple `(x, y, φ)` is rebuilt unchanged. Together with `toFiberPullback_comp_ofFiberPullback`
> this says the fibre of the 2-fibre product over `𝒞` at `U` is *isomorphic*, not merely
> equivalent, to the 2-fibre product of the fibres.

```lean
theorem ofFiberPullback_comp_toFiberPullback (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (U : 𝒞) :
    ofFiberPullback p𝒳 p𝒴 p𝒮 F G hF hG U ⋙ toFiberPullback p𝒳 p𝒴 p𝒮 F G hF hG U = 𝟭 _
```

**`CategoryTheory.TwoFibreProductOver.fiberEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/OverFibres.lean#L193).

> **Stacks 02XI**, as an equivalence of categories: the fibre of the 2-fibre product over `𝒞`
> at `U` is the 2-fibre product of the fibre categories. Both unit and counit are identities, the
> two functors being strictly mutually inverse.

```lean
def fiberEquiv (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) (U : 𝒞) :
    (structureFunctor p𝒳 p𝒴 p𝒮 F G).Fiber U ≌
      CategoricalPullback (Functor.fiberMap p𝒳 p𝒮 F hF U) (Functor.fiberMap p𝒴 p𝒮 G hG U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.32, Tag 02XG](https://stacks.math.columbia.edu/tag/02XG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
