---
declaration: section
origin: cited
lean: Stacks.StronglyCartesian.isStronglyCartesian_conditions_hold, CategoryTheory.Functor.IsStronglyCartesian.comp_functor, CategoryTheory.hasPullback_of_isStronglyCartesian, CategoryTheory.pullbackIsoOfIsStronglyCartesian, CategoryTheory.Functor.IsFibredCategory, CategoryTheory.Functor.isFibredCategory_iff_isFibered, CategoryTheory.Functor.IsFibered, CategoryTheory.Functor.ChoiceOfPullbacks
statement: formalized
proof: formalized
---

# 4.33 Fibred categories

Section 4.33 of the Stacks Project, [Tag 02XJ](https://stacks.math.columbia.edu/tag/02XJ). 13 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02XL, a lemma

[Tag 02XL](https://stacks.math.columbia.edu/tag/02XL) in the Stacks Project.

**`Stacks.StronglyCartesian.isStronglyCartesian_conditions_hold`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/StronglyCartesian.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/StronglyCartesian.lean#L37). References: SGA 1 VI (6.12), “iso ⇒ Cartesian”.

> **Stacks 02XL.** All three claims of `StronglyCartesianStability` hold for every `p : 𝒮 ⥤ 𝒞`,
> each supplied by Mathlib: `Functor.IsStronglyCartesian.comp`, `.of_isIso` and
> `.isIso_of_base_isIso`.

```lean
theorem isStronglyCartesian_conditions_hold {𝒞 : Type*} [Category 𝒞] {𝒮 : Type*} [Category 𝒮]
    (p : 𝒮 ⥤ 𝒞) : StronglyCartesianStability p
```

## Tag 09WU, a lemma

[Tag 09WU](https://stacks.math.columbia.edu/tag/09WU) in the Stacks Project.

**`CategoryTheory.Functor.IsStronglyCartesian.comp_functor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/StronglyCartesianComp.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/StronglyCartesianComp.lean#L64).

> If `θ : a' ⟶ a` is a strongly cartesian lift of `φ : b ⟶ F.obj a` along `F : A ⥤ B`, and `φ`
> is in turn a strongly cartesian lift of `f : R ⟶ G.obj (F.obj a)` along `G : B ⥤ C`, then `θ` is a
> strongly cartesian lift of `f` along `F ⋙ G`.
>
> Taking `φ := F.map θ` and `f := G.map (F.map θ)`: strong cartesianness of `θ` for `F` together with
> strong cartesianness of `F.map θ` for `G` implies strong cartesianness of `θ` for `F ⋙ G`.

```lean
lemma IsStronglyCartesian.comp_functor (F : A ⥤ B) (G : B ⥤ C)
    {a' a : A} {b : B} {R : C}
    (f : R ⟶ G.obj (F.obj a)) (φ : b ⟶ F.obj a) (θ : a' ⟶ a)
    [F.IsStronglyCartesian φ θ] [G.IsStronglyCartesian f φ] :
    (F ⋙ G).IsStronglyCartesian f θ
```

## Tag 06N4, a lemma

[Tag 06N4](https://stacks.math.columbia.edu/tag/06N4) in the Stacks Project.

**`CategoryTheory.hasPullback_of_isStronglyCartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FibreProductsCartesian.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/FibreProductsCartesian.lean#L172).

> **Stacks 06N4.**
> Given `φ : x ⟶ y` strongly cartesian over `p`, an existing fibre product
> `p x ×_{p y} p z` in `𝒞`, and a strongly cartesian morphism `a : w ⟶ z` in `𝒮`
> lying over the second projection of that fibre product (as recorded by `hw` and `ha`),
> the fibre product `x ×_y z` exists in `𝒮`.

```lean
theorem hasPullback_of_isStronglyCartesian
    (p : 𝒮 ⥤ 𝒞) {x y z : 𝒮} (φ : x ⟶ y) (g : z ⟶ y)
    [Functor.IsStronglyCartesian p (p.map φ) φ]
    [Limits.HasPullback (p.map φ) (p.map g)]
    (w : 𝒮) (a : w ⟶ z)
    (hw : p.obj w = Limits.pullback (p.map φ) (p.map g))
    (ha : p.map a = eqToHom hw ≫ Limits.pullback.snd (p.map φ) (p.map g))
    [Functor.IsStronglyCartesian p (p.map a) a] :
    Limits.HasPullback φ g
```

**`CategoryTheory.pullbackIsoOfIsStronglyCartesian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FibreProductsCartesian.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/FibreProductsCartesian.lean#L190).

> **Stacks 06N4.**
> In the situation of `hasPullback_of_isStronglyCartesian` the fibre product `x ×_y z`
> is canonically isomorphic to `w`: both are limits of the same cospan, `w` by the limit
> square built from the strongly cartesian morphisms `φ` and `a`.

```lean
noncomputable def pullbackIsoOfIsStronglyCartesian
    (p : 𝒮 ⥤ 𝒞) {x y z : 𝒮} (φ : x ⟶ y) (g : z ⟶ y)
    [Functor.IsStronglyCartesian p (p.map φ) φ]
    [Limits.HasPullback (p.map φ) (p.map g)]
    (w : 𝒮) (a : w ⟶ z)
    (hw : p.obj w = Limits.pullback (p.map φ) (p.map g))
    (ha : p.map a = eqToHom hw ≫ Limits.pullback.snd (p.map φ) (p.map g))
    [Functor.IsStronglyCartesian p (p.map a) a] [Limits.HasPullback φ g] :
    Limits.pullback φ g ≅ w
```

## Tag 02XM, a definition

[Tag 02XM](https://stacks.math.columbia.edu/tag/02XM) in the Stacks Project.

**`CategoryTheory.Functor.IsFibredCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean#L303).

> **Stacks 02XM.** A functor `p : 𝒳 ⥤ 𝒮` is a *fibred category over `𝒮`* when for every object
> `x` of `𝒳` lying over an object `U` of `𝒮` and every morphism `f : V ⟶ U` of `𝒮` there exists a
> strongly cartesian morphism `f^* x ⟶ x` lying over `f`.
>
> That `φ` lies over `f` is part of `CategoryTheory.Functor.IsStronglyCartesian`, which extends
> `CategoryTheory.Functor.IsHomLift`. See the implementation notes for why this is Mathlib's
> `CategoryTheory.Functor.IsFibered` and not its `CategoryTheory.Functor.IsPreFibered`.

```lean
def IsFibredCategory (p : 𝒳 ⥤ 𝒮) : Prop
```

**`CategoryTheory.Functor.isFibredCategory_iff_isFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean#L315). The attribute's comment: “the identification with Mathlib's `Functor.IsFibered`”. References: SGA 1 VI (6.11), “Sufficiency”.

> **Stacks 02XM is Mathlib's `CategoryTheory.Functor.IsFibered`.** Forward, a strongly
> cartesian lift of every base morphism makes `p` fibred by
> `CategoryTheory.Functor.IsFibered.of_exists_isStronglyCartesian`. Backward, a fibred category has
> a cartesian lift of every base morphism by `CategoryTheory.Functor.IsPreFibered.exists_isCartesian`
> and every cartesian morphism of a fibred category is strongly cartesian by
> `CategoryTheory.Functor.IsFibered.isStronglyCartesian_of_isCartesian`.

```lean
theorem isFibredCategory_iff_isFibered (p : 𝒳 ⥤ 𝒮) : p.IsFibredCategory ↔ p.IsFibered
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsFibered`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsFibered#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean#L325) (StacksFrontier): “Mathlib's SGA 1 VI.6.1 form of the definition, identified with the Stacks form by `CategoryTheory.Functor.isFibredCategory_iff_isFibered`”. References: SGA 1 VI (6.1); SGA 4 I (9.21), “The hypothesis that p”; SGA 4 VI (6.1).

## Tag 02XN, a definition

[Tag 02XN](https://stacks.math.columbia.edu/tag/02XN) in the Stacks Project.

**`CategoryTheory.Functor.ChoiceOfPullbacks`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean#L91). The attribute's comment: “(1)”.

> **Stacks 02XN (1).**
> A *choice of pullbacks* for `p : 𝒳 ⥤ 𝒮` is a choice, for every morphism `f : V ⟶ U` of `𝒮` and
> every object `x` of the fibre of `p` over `U`, of an object `f^* x` of the fibre over `V` together
> with a strongly cartesian morphism `f^* x ⟶ x` lying over `f`.

```lean
structure ChoiceOfPullbacks (p : 𝒳 ⥤ 𝒮)
```

**`CategoryTheory.Functor.ChoiceOfPullbacks.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/ChoiceOfPullbacks.lean#L171). The attribute's comment: “(2)”.

> **Stacks 02XN (2).**
> The *pullback functor* `f^* : 𝒳_U ⥤ 𝒳_V` between the fibres of `p` attached to a morphism
> `f : V ⟶ U` of `𝒮` by a choice of pullbacks.

```lean
noncomputable def pullbackFunctor {V U : 𝒮} (f : V ⟶ U) : p.Fiber U ⥤ p.Fiber V
```

## Tag 02XO, a lemma

[Tag 02XO](https://stacks.math.columbia.edu/tag/02XO) in the Stacks Project.

**`CategoryTheory.Functor.IsFibered.pbMapId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean#L352).

> **Stacks 02XO**, clause (2). The unitor `(𝟙 U)* ≅ 𝟭 (p.Fiber U)`, the canonical
> isomorphism coming from the uniqueness of strongly cartesian factorisations.

```lean
noncomputable def pbMapId (p : 𝒳 ⥤ 𝒮) [p.IsFibered] (U : LocallyDiscrete 𝒮ᵒᵖ) :
    pbMap p (𝟙 U) ≅ 𝟙 (pbObj p U)
```

**`CategoryTheory.Functor.IsFibered.pbMapComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean#L360). References: SGA 4 VI (6.1.2), “(6.1.2.1)”.

> **Stacks 02XO**, clause (1). The compositor `(g ≫ f)* ≅ f* ⋙ g*`, the canonical
> isomorphism compatible with the chosen cartesian lifts; `pbMapComp_uniq` shows it is the only
> such isomorphism.

```lean
noncomputable def pbMapComp (p : 𝒳 ⥤ 𝒮) [p.IsFibered]
    {U V W : LocallyDiscrete 𝒮ᵒᵖ} (φ : U ⟶ V) (γ : V ⟶ W) :
    pbMap p (φ ≫ γ) ≅ pbMap p φ ≫ pbMap p γ
```

**`CategoryTheory.Functor.IsFibered.pullbackPseudofunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean#L525). References: SGA 4 VI (7.1.4), “partial”; SGA 4 XVII (3.3.3), “Forward direction”.

> Statement 1 (Stacks 02XO).  The pullback pseudofunctor associated to a fibred category
> `p`.  Its object part is `U ↦ Cat.of (p.Fiber U)`, its 1-cell part is `f ↦ f*`, its unitor
> is `(𝟙 U)* ≅ 𝟭 (p.Fiber U)` and its compositor is `(g ≫ f)* ≅ f* ⋙ g*`.

```lean
noncomputable def pullbackPseudofunctor (p : 𝒳 ⥤ 𝒮) [p.IsFibered] :
    Pseudofunctor (LocallyDiscrete 𝒮ᵒᵖ) Cat
```

**`CategoryTheory.Functor.IsFibered.pullbackPseudofunctor_mapComp_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean#L563). References: SGA 1 VI (7.2), “partial”.

> **Stacks 02XO**, clause (1). The compositor of the pullback pseudofunctor is compatible
> with the chosen strongly cartesian lifts: on each object `X`, its underlying comparison
> morphism, followed by the composite of the chosen cartesian projections over `γ` and over `φ`,
> is the chosen cartesian projection over `φ ≫ γ`.

```lean
theorem pullbackPseudofunctor_mapComp_compatible (p : 𝒳 ⥤ 𝒮) [p.IsFibered]
    {U V W : LocallyDiscrete 𝒮ᵒᵖ} (φ : U ⟶ V) (γ : V ⟶ W) (X : ↑(pbObj p U)) :
    Fiber.fiberInclusion.map (((pullbackPseudofunctor p).mapComp φ γ).hom.toNatTrans.app X)
        ≫ (cartComp φ.as.unop γ.as.unop).proj X =
      IsPreFibered.pullbackMap X.2 (φ ≫ γ).as.unop
```

**`CategoryTheory.Functor.IsFibered.pbMapComp_uniq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/PullbackPseudofunctor.lean#L576). References: SGA 4 VI (6.1.2), “(6.1.2.1)”.

> **Stacks 02XO**, clause (1), uniqueness. The compositor is the *unique* isomorphism
> `(g ≫ f)* ≅ f* ⋙ g*` compatible with the chosen cartesian lifts: any isomorphism whose
> components satisfy the compatibility triangle of
> `pullbackPseudofunctor_mapComp_compatible` equals `pbMapComp`.

```lean
theorem pbMapComp_uniq (p : 𝒳 ⥤ 𝒮) [p.IsFibered]
    {U V W : LocallyDiscrete 𝒮ᵒᵖ} (φ : U ⟶ V) (γ : V ⟶ W)
    (θ : pbMap p (φ ≫ γ) ≅ pbMap p φ ≫ pbMap p γ)
    (hθ : ∀ X : ↑(pbObj p U),
      Fiber.fiberInclusion.map (θ.hom.toNatTrans.app X) ≫
          (cartComp φ.as.unop γ.as.unop).proj X =
        IsPreFibered.pullbackMap X.2 (φ ≫ γ).as.unop) :
    θ = pbMapComp p φ γ
```

## Tag 042G, a lemma

[Tag 042G](https://stacks.math.columbia.edu/tag/042G) in the Stacks Project.

**`CategoryTheory.BasedCategory.isFibered_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/EquivalenceInvariance.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/EquivalenceInvariance.lean#L170).

> **Stacks 042G (Lemma 4.33.8).** Let `𝒮` be a category and let `𝒳` and `𝒴` be categories
> over `𝒮`.  If `𝒳` and `𝒴` are equivalent as categories over `𝒮`, then `𝒳` is a fibred
> category over `𝒮` if and only if `𝒴` is.

```lean
theorem BasedCategory.isFibered_iff_of_equivalence
    {𝒳 : BasedCategory.{v₂, u₂} 𝒮} {𝒴 : BasedCategory.{v₃, u₃} 𝒮}
    (e : BasedCategory.Equivalence 𝒳 𝒴) :
    𝒳.p.IsFibered ↔ 𝒴.p.IsFibered
```

## Tag 02XP, a definition

[Tag 02XP](https://stacks.math.columbia.edu/tag/02XP) in the Stacks Project.

**`CategoryTheory.CatFibered`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/TwoCategory.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/TwoCategory.lean#L85).

> The 2-category of fibred categories over `𝒮`: the sub-2-category of the 2-category
> `BasedCategory 𝒮` of categories over `𝒮` (Stacks 003Y) whose
>
> 1. objects are the categories `p : 𝒳 ⥤ 𝒮` over `𝒮` that are fibred categories;
> 2. 1-morphisms `(𝒳, p) ⟶ (𝒴, p')` are the functors `G : 𝒳 ⥤ 𝒴` with `p' ∘ G = p` carrying
>    strongly cartesian morphisms to strongly cartesian morphisms;
> 3. 2-morphisms `t : G ⟶ H` are the morphisms of functors with `p'(t_x) = 𝟙 (p x)` for every
>    object `x` of `𝒳`.
>
> The hom-category `𝒳 ⟶ 𝒴` is the source's `Mor_{Fib/𝒮}(𝒳, 𝒴)`.

```lean
def CatFibered (𝒮 : Type u₁) [Category.{v₁} 𝒮]
```

## Tag 02XQ, a lemma

[Tag 02XQ](https://stacks.math.columbia.edu/tag/02XQ) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isFibered_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean#L223).

> **Stacks 02XQ, fibredness.** If `p𝒳`, `p𝒴`, `p𝒮` are fibred categories over `𝒞` and
> `F`, `G` are 1-morphisms of fibred categories over `𝒞`, then the structure functor of the
> 2-fibre product `𝒳 ×_𝒮 𝒴` exhibits it as a fibred category over `𝒞`.

```lean
theorem TwoFibreProductOver.isFibered_structureFunctor
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮)
    [p𝒳.IsFibered] [p𝒴.IsFibered] [p𝒮.IsFibered]
    (hF : Functor.IsFibredOneMorphism p𝒳 p𝒮 F)
    (hG : Functor.IsFibredOneMorphism p𝒴 p𝒮 G) :
    (TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒮 F G).IsFibered
```

**`CategoryTheory.TwoFibreProductOver.fst_isFibredOneMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean#L238).

> **Stacks 02XQ, first projection.** Under the hypotheses of
> `TwoFibreProductOver.isFibered_structureFunctor`, the first projection `π₁` is a 1-morphism
> of fibred categories over `𝒞`: it is strictly over `𝒞` and preserves strongly cartesian
> morphisms.

```lean
theorem TwoFibreProductOver.fst_isFibredOneMorphism
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮)
    [p𝒳.IsFibered] [p𝒴.IsFibered] [p𝒮.IsFibered]
    (hF : Functor.IsFibredOneMorphism p𝒳 p𝒮 F)
    (hG : Functor.IsFibredOneMorphism p𝒴 p𝒮 G) :
    Functor.IsFibredOneMorphism (TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒮 F G) p𝒳
      (TwoFibreProductOver.fst p𝒳 p𝒴 p𝒮 F G)
```

**`CategoryTheory.TwoFibreProductOver.snd_isFibredOneMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/TwoFibreProduct.lean#L254).

> **Stacks 02XQ, second projection.** Under the hypotheses of
> `TwoFibreProductOver.isFibered_structureFunctor`, the second projection `π₂` is a 1-morphism
> of fibred categories over `𝒞`.

```lean
theorem TwoFibreProductOver.snd_isFibredOneMorphism
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮)
    [p𝒳.IsFibered] [p𝒴.IsFibered] [p𝒮.IsFibered]
    (hF : Functor.IsFibredOneMorphism p𝒳 p𝒮 F)
    (hG : Functor.IsFibredOneMorphism p𝒴 p𝒮 G) :
    Functor.IsFibredOneMorphism (TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒮 F G) p𝒴
      (TwoFibreProductOver.snd p𝒳 p𝒴 p𝒮 F G)
```

## Tag 02XR, a lemma

[Tag 02XR](https://stacks.math.columbia.edu/tag/02XR) in the Stacks Project.

**`CategoryTheory.Functor.IsFibered.of_comp_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Slice.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Slice.lean#L94).

> If a fibred category `p : S ⥤ C` factors as `p' ⋙ Over.forget U` through the slice
> category `Over U`, then `p' : S ⥤ Over U` is a fibred category.

```lean
theorem IsFibered.of_comp_over (p : S ⥤ C)
    [p.IsFibered] (h : p' ⋙ Over.forget U = p) :
    p'.IsFibered
```

## Tag 09WV, a lemma

[Tag 09WV](https://stacks.math.columbia.edu/tag/09WV) in the Stacks Project.

**`CategoryTheory.Functor.IsFibered.comp_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/CompFibered.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/CompFibered.lean#L34).

> A composite of fibred functors is fibred: if `F : A ⥤ B` and `G : B ⥤ C` are fibred, then so
> is `F ⋙ G`.

```lean
theorem IsFibered.comp_functor (F : A ⥤ B) (G : B ⥤ C)
    [F.IsFibered] [G.IsFibered] : (F ⋙ G).IsFibered
```

## Tag 06N5, a lemma

[Tag 06N5](https://stacks.math.columbia.edu/tag/06N5) in the Stacks Project.

**`CategoryTheory.Functor.IsFibered.hasPullback_of_isStronglyCartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean#L96).

> **Stacks 06N5, existence half.**
> In a fibred category `p : 𝒮 ⥤ 𝒞`, if `φ : x ⟶ y` is strongly cartesian over `p` and
> the fibre product of `p φ` and `p g` exists in `𝒞`, then the fibre product of `φ` and
> `g` exists in `𝒮`.

```lean
theorem Functor.IsFibered.hasPullback_of_isStronglyCartesian
    (p : 𝒮 ⥤ 𝒞) [p.IsFibered]
    {x y z : 𝒮} (φ : x ⟶ y) (g : z ⟶ y)
    [Functor.IsStronglyCartesian p (p.map φ) φ]
    [Limits.HasPullback (p.map φ) (p.map g)] :
    Limits.HasPullback φ g
```

**`CategoryTheory.Functor.IsFibered.snd_isStronglyCartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean#L111).

> **Stacks 06N5, second projection strongly cartesian.**
> Under the same hypotheses the second projection `Limits.pullback.snd φ g : x ×_y z ⟶ z`
> is strongly cartesian over `p`, since it is the canonical isomorphism `x ×_y z ≅ w`
> followed by the strongly cartesian morphism `a`.

```lean
theorem Functor.IsFibered.snd_isStronglyCartesian
    (p : 𝒮 ⥤ 𝒞) [p.IsFibered]
    {x y z : 𝒮} (φ : x ⟶ y) (g : z ⟶ y)
    [Functor.IsStronglyCartesian p (p.map φ) φ]
    [Limits.HasPullback (p.map φ) (p.map g)]
    [Limits.HasPullback φ g] :
    Functor.IsStronglyCartesian p
      (p.map (Limits.pullback.snd φ g)) (Limits.pullback.snd φ g)
```

**`CategoryTheory.Functor.IsFibered.map_isPullback_of_isStronglyCartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/FibreProducts.lean#L131).

> **Stacks 06N5, image square is a fibre product square.**
> Under the same hypotheses `p` sends the fibre product square of `φ, g` in `𝒮` to a
> fibre product square in `𝒞`: the image `p (x ×_y z)`, with the images of the two
> projections, is the fibre product of `p φ` and `p g`.

```lean
theorem Functor.IsFibered.map_isPullback_of_isStronglyCartesian
    (p : 𝒮 ⥤ 𝒞) [p.IsFibered]
    {x y z : 𝒮} (φ : x ⟶ y) (g : z ⟶ y)
    [Functor.IsStronglyCartesian p (p.map φ) φ]
    [Limits.HasPullback (p.map φ) (p.map g)]
    [Limits.HasPullback φ g] :
    IsPullback (p.map (Limits.pullback.fst φ g)) (p.map (Limits.pullback.snd φ g))
      (p.map φ) (p.map g)
```

## Tag 08NF, a lemma

[Tag 08NF](https://stacks.math.columbia.edu/tag/08NF) in the Stacks Project.

**`CategoryTheory.Functor.IsFibered.exists_amelioration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Amelioration.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Amelioration.lean#L770).

> **Stacks 4.33.14 / 08NF.** Let `F : X ⥤ Y` be a 1-morphism of fibred categories over
> `C`, with structure functors `p : X ⥤ C` and `q : Y ⥤ C`. Then there exist a fibred
> category `(X', p'')` over `C` and three 1-morphisms of fibred categories over `C`
>
>   `u : X ⥤ X'`, `v : X' ⥤ Y`, `w : X' ⥤ X`,
>
> with `F = u ⋙ v` such that
> 1. `u` is fully faithful;
> 2. `w` is left adjoint to `u`; and
> 3. `v` exhibits `X'` as a fibred category over `Y` (`v.IsFibered`), the structure functor of
>    `X'` over `C` factoring as `p'' = v ⋙ q`.
>
> The witness category `X'` is stated in the universe `max u₁ u₂ u₃ v₁ v₂ v₃` so as to
> accommodate the explicit construction, in which an object carries a morphism of `Y` (living
> in the hom universe `v₃`). It is the amelioration `Amelioration p q F hFq` of `F`, moved
> into that universe by `exists_amelioration_uliftHom`.

```lean
theorem Functor.IsFibered.exists_amelioration
    {C : Type u₁} [Category.{v₁} C]
    {X : Type u₂} [Category.{v₂} X]
    {Y : Type u₃} [Category.{v₃} Y]
    (p : X ⥤ C) (q : Y ⥤ C) [p.IsFibered] [q.IsFibered]
    (F : X ⥤ Y) (hF : Functor.IsFibredOneMorphism p q F) :
    ∃ (X' : Type (max u₁ u₂ u₃ v₁ v₂ v₃)) (_ : Category.{max v₁ v₂ v₃} X')
      (p'' : X' ⥤ C) (_ : p''.IsFibered)
      (u : X ⥤ X') (v : X' ⥤ Y) (w : X' ⥤ X),
        -- the three functors are 1-morphisms of fibred categories over C
        Functor.IsFibredOneMorphism p p'' u ∧
        Functor.IsFibredOneMorphism p'' q v ∧
        Functor.IsFibredOneMorphism p'' p w ∧
        -- F factors as u ⋙ v
        F = u ⋙ v ∧
        -- the structure functor of X' over C factors through Y as p'' = v ⋙ q
        p'' = v ⋙ q ∧
        -- (1) u is fully faithful
        Nonempty u.FullyFaithful ∧
        -- (2) w is left adjoint to u
        Nonempty (w ⊣ u) ∧
        -- (3) v exhibits X' as a fibred category over Y
        v.IsFibered
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.33, Tag 02XJ](https://stacks.math.columbia.edu/tag/02XJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
