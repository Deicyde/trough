---
declaration: section
origin: cited
lean: Deformation.IsCofiberedInGroupoids, Deformation.isCofiberedInGroupoids_twoFibreProductBasedCategory, Deformation.fiberHomEquiv, Deformation.isGroupoid_fiber, Deformation.fiberGroupoid, Deformation.existsUnique_iso_of_isHomLift, Deformation.ChoiceOfPushforwards, Deformation.nonempty_choiceOfPushforwards
statement: formalized
proof: formalized
---

# 90.5 Categories cofibered in groupoids

Section 90.5 of the Stacks Project, [Tag 06GA](https://stacks.math.columbia.edu/tag/06GA). 4 tags here are carried by 36 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06GJ, a definition

[Tag 06GJ](https://stacks.math.columbia.edu/tag/06GJ) in the Stacks Project.

**`Deformation.IsCofiberedInGroupoids`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered.lean#L60).

> A functor `p : F ⥤ C` is *cofibered in groupoids* when the opposite
> functor `p.op : Fᵒᵖ ⥤ Cᵒᵖ` is fibered in groupoids.

```lean
public abbrev IsCofiberedInGroupoids {F : Type u₁} [Category.{v₁} F]
    {C : Type u₂} [Category.{v₂} C] (p : F ⥤ C) : Prop
```

## Tag 06GK, remarks

[Tag 06GK](https://stacks.math.columbia.edu/tag/06GK) in the Stacks Project.

**`Deformation.isCofiberedInGroupoids_twoFibreProductBasedCategory`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean#L93). The attribute's comment: “(13) the 2-fibre product of categories cofibered in groupoids over 𝒞\_Λ is given by the construction of their 2-fibre product as categories over 𝒞\_Λ”.

> A `2`-fibre product of categories cofibered in groupoids over `𝒞_Λ` is cofibered in
> groupoids: the construction of the `2`-fibre product as categories over `𝒞_Λ` serves as the
> `2`-fibre product in the `(2, 1)`-category of categories cofibered in groupoids over `𝒞_Λ`.

```lean
public lemma isCofiberedInGroupoids_twoFibreProductBasedCategory
    (p₁ : BasedFunctor 𝓗₁ 𝓖) (p₂ : BasedFunctor 𝓗₂ 𝓖)
    (h𝓗₁ : IsCofiberedInGroupoids 𝓗₁.p) (h𝓗₂ : IsCofiberedInGroupoids 𝓗₂.p)
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (twoFibreProductBasedCategory p₁ p₂).p
```

**`Deformation.fiberHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L60). The attribute's comment: “(2) the fibre category F(U): objects of F over U, morphisms of F over id\_U”.

> **Stacks 06GK (2).** The morphisms `x ⟶ y` of the fibre category `p.Fiber U` are exactly the
> morphisms of `F` between the underlying objects lying over `𝟙 U`.

```lean
def fiberHomEquiv (p : F ⥤ C) (U : C) (x y : p.Fiber U) :
    (x ⟶ y) ≃ {φ : x.1 ⟶ y.1 // p.IsHomLift (𝟙 U) φ}
```

**`Deformation.isGroupoid_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L72). The attribute's comment: “(3) the fibre categories F(U) are groupoids”.

> **Stacks 06GK (3).** The fibre categories of a category cofibered in groupoids are groupoids:
> every morphism of `p.Fiber U` is an isomorphism (Categories, Lemma 003V).

```lean
theorem isGroupoid_fiber {p : F ⥤ C} (hp : IsCofiberedInGroupoids p) (U : C) :
    IsGroupoid (p.Fiber U)
```

**`Deformation.fiberGroupoid`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L86). The attribute's comment: “(3) the fibre category F(U) as a groupoid”.

> **Stacks 06GK (3).** The groupoid structure on a fibre category of a category cofibered in
> groupoids.

```lean
noncomputable abbrev fiberGroupoid {p : F ⥤ C} (hp : IsCofiberedInGroupoids p) (U : C) :
    Groupoid (p.Fiber U)
```

**`Deformation.existsUnique_iso_of_isHomLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L97). The attribute's comment: “(4) a pushforward is unique up to unique isomorphism”.

> **Stacks 06GK (4).** Two pushforwards `a : x ⟶ y` and `a' : x ⟶ y'` of `x` along `f : U ⟶ V`
> (morphisms lying over `f`) differ by a unique isomorphism `y ≅ y'` lying over `𝟙 V` and
> compatible with `a` and `a'`.

```lean
theorem existsUnique_iso_of_isHomLift {p : F ⥤ C} (hp : IsCofiberedInGroupoids p) {U V : C}
    (f : U ⟶ V) {x y y' : F} (a : x ⟶ y) (a' : x ⟶ y') [p.IsHomLift f a] [p.IsHomLift f a'] :
    ∃! e : y ≅ y', p.IsHomLift (𝟙 V) e.hom ∧ a ≫ e.hom = a'
```

**`Deformation.ChoiceOfPushforwards`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L117). The attribute's comment: “(5) a choice of pushforwards”.

> **Stacks 06GK (5).** A *choice of pushforwards* for `p`: for every morphism `f : U ⟶ V` of
> `C` and every object `x` of the fibre over `U`, an object `obj f x` of the fibre over `V` and a
> pushforward `hom f x : x ⟶ obj f x` of `x` along `f`.

```lean
structure ChoiceOfPushforwards (p : F ⥤ C)
```

**`Deformation.nonempty_choiceOfPushforwards`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L136). The attribute's comment: “(5) a choice of pushforwards exists by the axiom of choice”.

> **Stacks 06GK (5).** A category cofibered in groupoids admits a choice of pushforwards,
> by the axiom of choice.

```lean
theorem nonempty_choiceOfPushforwards {p : F ⥤ C} (hp : IsCofiberedInGroupoids p) :
    Nonempty (ChoiceOfPushforwards p)
```

**`Deformation.pushforwardPseudofunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L162). The attribute's comment: “(6) the pseudofunctor C → Groupoids attached to a choice of pushforwards”.

> **Stacks 06GK (6).** The pseudofunctor `C → Groupoids` associated to a category cofibered in
> groupoids together with the choice of pushforwards `ChoiceOfPushforwards.ofIsFibered p`. Its
> value at `U` is the fibre of `p.op` over `op U` (the objects of `F` over `U`, a groupoid by
> `isGroupoid_pushforwardPseudofunctor_obj`), and its value at `f : U ⟶ V` is pushforward along `f`.
> It is the pullback pseudofunctor of the fibred category `p.op` (Stacks 02XO), reindexed along
> `opOp C`.

```lean
noncomputable def pushforwardPseudofunctor {p : F ⥤ C} (hp : IsCofiberedInGroupoids p) :
    Pseudofunctor (LocallyDiscrete C) Cat
```

**`Deformation.isGroupoid_pushforwardPseudofunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/FibreCategory.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/FibreCategory.lean#L187). The attribute's comment: “(6) the values of the pseudofunctor are groupoids”.

> The values of the pseudofunctor of a category cofibered in groupoids are groupoids.

```lean
theorem isGroupoid_pushforwardPseudofunctor_obj {p : F ⥤ C} (hp : IsCofiberedInGroupoids p)
    (U : C) : IsGroupoid ((pushforwardPseudofunctor hp).obj ⟨U⟩)
```

**`Deformation.ofGroupoidFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L56). The attribute's comment: “(9) the category cofibered in groupoids associated to a functor C → Groupoids”.

> **Stacks 06GK (9).** The category over `C` attached to a functor `F : C ⥤ Groupoids`: objects
> the pairs `(U, x)` with `x` an object of `F(U)`, morphisms `(U, x) ⟶ (V, y)` the pairs `(f, a)`
> with `f : U ⟶ V` and `a : F(f)(x) ⟶ y` (`ofGroupoidFunctorHomEquiv`), and projection
> `(U, x) ↦ U`.

```lean
abbrev ofGroupoidFunctor (F : C ⥤ Grpd.{w, w}) : BasedCategory C
```

**`Deformation.ofGroupoidFunctorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L62). The attribute's comment: “(9) morphisms (U, x) → (V, y) are pairs (f, a) with a : F(f)(x) → y”.

> **Stacks 06GK (9).** A morphism `(U, x) ⟶ (V, y)` of the category attached to
> `F : C ⥤ Groupoids` is a pair `(f, a)` with `f : U ⟶ V` and `a : F(f)(x) ⟶ y` in `F(V)`.

```lean
def ofGroupoidFunctorHomEquiv (F : C ⥤ Grpd.{w, w}) (X Y : (ofGroupoidFunctor F).obj) :
    (X ⟶ Y) ≃ Σ f : X.base ⟶ Y.base, ((F.map f).obj X.fiber ⟶ Y.fiber)
```

**`Deformation.isCofiberedInGroupoids_ofGroupoidFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L72). The attribute's comment: “(9) the category associated to a functor C → Groupoids is cofibered in groupoids”.

> **Stacks 06GK (9).** The category attached to a functor `C ⥤ Groupoids` is cofibered in
> groupoids over `C`.

```lean
theorem isCofiberedInGroupoids_ofGroupoidFunctor (F : C ⥤ Grpd.{w, w}) :
    IsCofiberedInGroupoids (ofGroupoidFunctor F).p
```

**`Deformation.ofSetFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L81). The attribute's comment: “(11) the category cofibered in sets associated to a functor C → Sets”.

> **Stacks 06GK (11).** The category cofibered in sets attached to a functor `F : C ⥤ Type`:
> the construction (9) applied to `F`, each set being read as a discrete groupoid.

```lean
abbrev ofSetFunctor (F : C ⥤ Type w) : BasedCategory C
```

**`Deformation.isCofiberedInGroupoids_ofSetFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L138). The attribute's comment: “(11) the category associated to a functor C → Sets is cofibered in groupoids”.

> **Stacks 06GK (11).** The category attached to a functor to sets is cofibered in groupoids.

```lean
theorem isCofiberedInGroupoids_ofSetFunctor (F : C ⥤ Type w) :
    IsCofiberedInGroupoids (ofSetFunctor F).p
```

**`Deformation.isDiscrete_fiber_ofSetFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L146). The attribute's comment: “(11) the associated category is cofibered in sets: its fibre categories are discrete”.

> **Stacks 06GK (11).** The fibre categories of the category attached to a functor to sets are
> discrete, so it is a category cofibered in sets.

```lean
theorem isDiscrete_fiber_ofSetFunctor (F : C ⥤ Type w) (U : C) :
    IsDiscrete ((ofSetFunctor F).p.Fiber U)
```

**`Deformation.ofSetFunctorFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L181). The attribute's comment: “(11) the embedding of functors C → Sets into categories cofibered in groupoids”.

> **Stacks 06GK (11).** The functor from functors `C ⥤ Type` to the `(2, 1)`-category `Cof(C)`
> sending `F` to its category cofibered in sets.

```lean
def ofSetFunctorFunctor : (C ⥤ Type w) ⥤
    Bicategory.InducedBicategory (BasedCategory.{max v₁ w, max u₁ w} C)
      (Subtype.val (p := IsCofiberedBased (C := C)))
```

**`Deformation.ofSetFunctorFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L233). The attribute's comment: “(11) the embedding of functors C → Sets into Cof(C) is fully faithful”.

> **Stacks 06GK (11).** The embedding of the category of functors `C ⥤ Type` into the category
> of categories cofibered in groupoids over `C` is fully faithful.

```lean
def ofSetFunctorFullyFaithful : (ofSetFunctorFunctor (C := C)).FullyFaithful
```

**`Deformation.subsingleton_twoHom_ofSetFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L242). The attribute's comment: “(11) 2-morphisms into a category cofibered in sets are unique”.

> **Stacks 06GK (11).** Between two morphisms into a category cofibered in sets there is at
> most one 2-morphism.

```lean
instance subsingleton_twoHom_ofSetFunctor {𝒳 : Bicategory.InducedBicategory
    (BasedCategory.{max v₁ w, max u₁ w} C) (Subtype.val (p := IsCofiberedBased (C := C)))}
    {G : C ⥤ Type w} (φ ψ : 𝒳 ⟶ ofSetFunctorFunctor.obj G) : Subsingleton (φ ⟶ ψ)
```

**`Deformation.eq_of_twoHom_ofSetFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L260). The attribute's comment: “(11) 2-morphisms into a category cofibered in sets are identities”.

> **Stacks 06GK (11).** A 2-morphism between two morphisms into a category cofibered in sets
> exists only when they are equal; together with `subsingleton_twoHom_ofSetFunctor` the
> hom-categories into the image of the embedding are discrete.

```lean
theorem eq_of_twoHom_ofSetFunctor {𝒳 : Bicategory.InducedBicategory
    (BasedCategory.{max v₁ w, max u₁ w} C) (Subtype.val (p := IsCofiberedBased (C := C)))}
    {G : C ⥤ Type w} {φ ψ : 𝒳 ⟶ ofSetFunctorFunctor.obj G} (t : φ ⟶ ψ) : φ = ψ
```

**`Deformation.underlineFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/OfFunctor.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/OfFunctor.lean#L277). The attribute's comment: “(12) U ↦ Mor\_C(U, -) is a fully faithful embedding of C^opp into functors C → Sets (Mathlib's Coyoneda.fullyFaithful)”.

> **Stacks 06GK (12).** For `U : C` the functor `Mor_C(U, -) : C ⥤ Type` (written `U` underlined
> in Stacks) is `coyoneda.obj (op U)`, and `U ↦ Mor_C(U, -)` is a fully faithful embedding of `Cᵒᵖ`
> into the category of functors `C ⥤ Type`: a morphism `f : U ⟶ V` induces
> `coyoneda.map f.op : Mor_C(V, -) ⟶ Mor_C(U, -)`, and every morphism of functors arises so from a
> unique `f`. This is Mathlib's `Coyoneda.fullyFaithful`.

```lean
def underlineFullyFaithful : (coyoneda : Cᵒᵖ ⥤ C ⥤ Type v₁).FullyFaithful
```

**`Deformation.cofiberedProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Product.lean#L81). The attribute's comment: “(14) products of categories cofibered in groupoids”.

> The *product* of two categories cofibered in groupoids `𝓕` and `𝓖` over `𝒞_Λ` is their
> `2`-fibre product `𝓕 ×_{𝒞_Λ} 𝓖`, taken over `𝒞_Λ` itself: the `2`-fibre product of the two
> structure morphisms of `𝓕` and `𝓖` into the base category read through the identity functor as a
> category cofibered in groupoids over itself.

```lean
public def cofiberedProduct (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)) :
    BasedCategory (ArtinianLocalAlgCat.{u, w, w} Λ k)
```

**`Deformation.isCofiberedInGroupoids_cofiberedProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Product.lean#L217). The attribute's comment: “(14) the product is again a category cofibered in groupoids”.

> The product of two categories cofibered in groupoids over `𝒞_Λ` is again cofibered in
> groupoids.

```lean
public theorem isCofiberedInGroupoids_cofiberedProduct
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (cofiberedProduct 𝓕 𝓖).p
```

**`Deformation.restrictBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Restriction.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Restriction.lean#L80). The attribute's comment: “(15) the restriction F|\_\{C'} → C' to a full subcategory C' of the base”.

> **Stacks 06GK (15).** The restriction `p|_{C'} : F|_{C'} ⥤ C'` of `p : F ⥤ C` to the full
> subcategory `C'` of `C` cut out by `P`: here `F|_{C'}` is the full subcategory of `F` on the objects
> lying over objects of `C'`, and the functor is `p` on objects and morphisms.

```lean
def restrictBase : (P.inverseImage p).FullSubcategory ⥤ P.FullSubcategory
```

**`Deformation.isCofiberedInGroupoids_restrictBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Restriction.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Restriction.lean#L90). The attribute's comment: “(15) the restriction F|\_\{C'} → C' is cofibered in groupoids”.

> **Stacks 06GK (15).** The restriction of a category cofibered in groupoids to a full
> subcategory of its base is cofibered in groupoids.

```lean
theorem isCofiberedInGroupoids_restrictBase {P : ObjectProperty C} {p : F ⥤ C}
    (hp : IsCofiberedInGroupoids p) : IsCofiberedInGroupoids (restrictBase P p)
```

**`Deformation.IsCofiberedBased`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L59). The attribute's comment: “(8) the (2, 1)-category Cof(C): the full sub-2-category of categories over C cut out by this predicate”.

> **Stacks 06GK (8).** The 2-category `Cof(C)` of categories cofibered in groupoids over `C` is
> `Bicategory.InducedBicategory (BasedCategory C) (Subtype.val (p := IsCofiberedBased))`: the full
> sub-2-category of the 2-category `BasedCategory C` of categories over `C` spanned by the
> categories satisfying this predicate, i.e. whose structure functor is cofibered in groupoids.
> Its 1-morphisms are the functors commuting with the projections
> (`CatCofiberedInGroupoids.homEquiv`), its 2-morphisms the morphisms of functors lying over
> identities (`CatCofiberedInGroupoids.twoHomEquiv`), and every 2-morphism is
> invertible (`CatCofiberedInGroupoids.isIso_twoHom`).

```lean
abbrev IsCofiberedBased {C : Type u₁} [Category.{v₁} C] (𝒳 : BasedCategory.{v₂, u₂} C) : Prop
```

**`Deformation.CatCofiberedInGroupoids.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L81). The attribute's comment: “(7) a morphism of categories cofibered in groupoids is a functor commuting with the projections; Mor\_C(F, F')”.

> **Stacks 06GK (7).** A morphism `𝒳 ⟶ 𝒴` of categories cofibered in groupoids over `C`, i.e. an
> element of `Mor_C(𝒳, 𝒴)`, is precisely a functor between the underlying categories commuting with
> the projections to `C` (a `BasedFunctor`, see `homFunctor_comp_p`).

```lean
def homEquiv (𝒳 𝒴 : Bicategory.InducedBicategory (BasedCategory.{v₂, u₂} C)
      (Subtype.val (p := IsCofiberedBased (C := C)))) :
    (𝒳 ⟶ 𝒴) ≃ (𝒳.val ⥤ᵇ 𝒴.val)
```

**`Deformation.CatCofiberedInGroupoids.homFunctor_comp_p`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L89). The attribute's comment: “(7) 1-morphisms commute with the projections”.

> **Stacks 06GK (7).** The functor underlying a 1-morphism of `Cof(C)` commutes with the
> projections: `p' ∘ G = p`.

```lean
lemma homFunctor_comp_p (G : 𝒳 ⟶ 𝒴) : G.hom.toFunctor ⋙ 𝒴.val.p = 𝒳.val.p
```

**`Deformation.CatCofiberedInGroupoids.twoHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L96). The attribute's comment: “(8) 2-morphisms are morphisms of functors t with p'(t\_x) = id\_\{p(x)}”.

> **Stacks 06GK (8).** A 2-morphism `t : G ⟶ H` of `Cof(C)` is precisely a morphism of the
> underlying functors whose components satisfy `p'(t_x) = 𝟙 (p x)`, i.e. lie over identities
> (a `BasedNatTrans`).

```lean
def twoHomEquiv (G H : 𝒳 ⟶ 𝒴) : (G ⟶ H) ≃ BasedNatTrans G.hom H.hom
```

**`Deformation.CatCofiberedInGroupoids.isIso_twoHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L103). The attribute's comment: “(8) Cof(C) is a (2, 1)-category: every 2-morphism is invertible”.

> **Stacks 06GK (8).** Every 2-morphism of `Cof(C)` is invertible: its components lie over
> identities of `C`, hence are isomorphisms in the target, which is cofibered in groupoids. Thus
> `Cof(C)` is a `(2, 1)`-category.

```lean
theorem isIso_twoHom {G H : 𝒳 ⟶ 𝒴} (t : G ⟶ H) : IsIso t
```

**`Deformation.isomorphismClasses`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean#L475). The attribute's comment: “(10) the functor of isomorphism classes of the fibre categories”.

> The associated covariant functor of fibrewise isomorphism classes.

```lean
noncomputable abbrev isomorphismClasses : C ⥤ Type u₁
```

**`Deformation.isomorphismClassesMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean#L571). The attribute's comment: “(10) the morphism of functors of isomorphism classes induced by a morphism of cofibered categories”.

> The associated natural transformation, with universe lifts for independent total categories.

```lean
noncomputable def isomorphismClassesMap :
    (isomorphismClasses 𝓕 h𝓕 ⋙ uliftFunctor.{u₂}) ⟶
      (isomorphismClasses 𝓖 h𝓖 ⋙ uliftFunctor.{u₁})
```

Declarations registered for the tag:

- [`CategoryTheory.CatFiberedInGroupoids.map_app`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/TwoCategory.lean#L178), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Cofibered/TwoCategory.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/TwoCategory.lean#L114) (StacksFrontier): “(8) p'(t\_x) = id\_\{p(x)} for a 2-morphism t (stated for any full sub-2-category of categories over C, in particular Cof(C))”.

## Tag 07W5, an item

[Tag 07W5](https://stacks.math.columbia.edu/tag/07W5) in the Stacks Project.

**`Deformation.isomorphismClasses`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean#L475).

> The associated covariant functor of fibrewise isomorphism classes.

```lean
noncomputable abbrev isomorphismClasses : C ⥤ Type u₁
```

## Tag 0DZJ, an item

[Tag 0DZJ](https://stacks.math.columbia.edu/tag/0DZJ) in the Stacks Project.

**`Deformation.cofiberedProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Product.lean#L81). The attribute's comment: “the product of two categories cofibered in groupoids over 𝒞\_Λ is their 2-fibre product over 𝒞\_Λ”.

> The *product* of two categories cofibered in groupoids `𝓕` and `𝓖` over `𝒞_Λ` is their
> `2`-fibre product `𝓕 ×_{𝒞_Λ} 𝓖`, taken over `𝒞_Λ` itself: the `2`-fibre product of the two
> structure morphisms of `𝓕` and `𝓖` into the base category read through the identity functor as a
> category cofibered in groupoids over itself.

```lean
public def cofiberedProduct (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)) :
    BasedCategory (ArtinianLocalAlgCat.{u, w, w} Λ k)
```

**`Deformation.isCofiberedInGroupoids_cofiberedProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Product.lean#L217). The attribute's comment: “the product of two categories cofibered in groupoids is cofibered in groupoids”.

> The product of two categories cofibered in groupoids over `𝒞_Λ` is again cofibered in
> groupoids.

```lean
public theorem isCofiberedInGroupoids_cofiberedProduct
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (cofiberedProduct 𝓕 𝓖).p
```

**`Deformation.twoFibreProductBasedCategory_comp_baseProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Cofibered/Product.lean#L233). The attribute's comment: “the 2-fibre product over 𝒞\_Λ along the structure morphisms is the product”.

> Given morphisms `p₁ : 𝓗 → 𝓕` and `p₂ : 𝓖 → 𝓕` of categories cofibered in groupoids over `𝒞_Λ`,
> the `2`-fibre product of `𝓗` and `𝓖` formed over `𝒞_Λ` — that is, over the two composites of `p₁`
> and `p₂` with the structure morphism of `𝓕` — is the product `𝓗 ×_{𝒞_Λ} 𝓖`.

```lean
public theorem twoFibreProductBasedCategory_comp_baseProjection
    (p₁ : BasedFunctor 𝓗 𝓕) (p₂ : BasedFunctor 𝓖 𝓕) :
    twoFibreProductBasedCategory (BasedFunctor.comp p₁ (baseProjection 𝓕.p))
        (BasedFunctor.comp p₂ (baseProjection 𝓕.p)) = cofiberedProduct 𝓗 𝓖
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.5, Tag 06GA](https://stacks.math.columbia.edu/tag/06GA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
