---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.essImage_toQuotientStack, AlgebraicGeometry.Stack.fullyFaithful_fiberFunctor_toQuotientStack, AlgebraicGeometry.Stack.presentingDescentFunctor, AlgebraicGeometry.Stack.presentingDescentFunctor_obj, AlgebraicGeometry.Stack.presentingDescentFunctor_hom, AlgebraicGeometry.Stack.presentingDescentFunctor_map_hom, AlgebraicGeometry.Stack.exists_presentingDescentDatum, AlgebraicGeometry.Stack.effective_presentingDescentDatum
statement: formalized
proof: formalized
---

# 78.24 Explicit description of quotient stacks

Section 78.24 of the Stacks Project, [Tag 04MB](https://stacks.math.columbia.edu/tag/04MB). 1 tag here is carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 044X, a lemma

[Tag 044X](https://stacks.math.columbia.edu/tag/044X) in the Stacks Project.

**`AlgebraicGeometry.Stack.essImage_toQuotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStack.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStack.lean#L217). The attribute's comment: “part (1): local representatives”.

> Every object of the quotient locally comes from the pointwise groupoid presentation: clause
> (2) of Stacks 02ZN for this witness, and part (1) of Stacks 044X.

```lean
theorem essImage_toQuotientStack
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (U : BigFppfOver C S hS) (x : (quotientStack G).p.Fiber U) :
    ∃ R ∈ BigFppfOver.topology C S hS U,
      ∀ ⦃V : BigFppfOver C S hS⦄ ⦃f : V ⟶ U⦄, R.arrows f →
        (Functor.fiberFunctorOfCompEq (isFibredOneMorphism_toQuotientStack G).comp_eq V).essImage
          (Functor.pullbackFiber (quotientStack G).p x f)
```

**`AlgebraicGeometry.Stack.fullyFaithful_fiberFunctor_toQuotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/FibreFullFaithfulness.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/FibreFullFaithfulness.lean#L57). The attribute's comment: “part (2): transition arrows”.

> **Stacks 044X**, part (2). A transition isomorphism between two objects of a fibre of the
> quotient stack that come from points of the object space is the image under `π` of a unique
> arrow of the arrow space: the functor induced by `π` on the fibre over any test object is fully
> faithful. This is Stacks 044V read through the identity map of the test object.

```lean
theorem fullyFaithful_fiberFunctor_toQuotientStack
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS) :
    Nonempty (Functor.fiberFunctorOfCompEq
      (isFibredOneMorphism_toQuotientStack G).comp_eq T).FullyFaithful
```

**`AlgebraicGeometry.Stack.presentingDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L307). The attribute's comment: “parts (2) and (3): projection of presenting data”.

> **Stacks 044X**, parts (2) and (3). The functor on descent data relative to a fixed covering
> of a test object induced by the canonical 1-morphism `π : 𝒮_U ⟶ [U/R]`: a system `(u i, r i j)`
> of points of the object space and arrows of the arrow space is carried to the descent datum of
> `[U/R]` whose local objects are the `π (u i)` and whose transition isomorphisms are the images
> `π (r i j)`, conjugated by the canonical comparison between the chosen pullback of an image and
> the image of a chosen pullback. Part (3), that `(u i, r i j)` *is* a descent datum, is the
> hypothesis on the source; the content here is that its image is one for the quotient.

```lean
noncomputable def presentingDescentFunctor
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T) :
    Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰 ⥤
      Functor.FamilyDescentDatum (quotientStack G).p 𝒰
```

**`AlgebraicGeometry.Stack.presentingDescentFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L401). The attribute's comment: “part (2): local components”.

> **Stacks 044X**, part (2). The local objects of the projected descent datum are the images
> under `π` of the local points of the object space.

```lean
theorem presentingDescentFunctor_obj
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T)
    (D : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰)
    (i : 𝒰.I₀) :
    ((presentingDescentFunctor G 𝒰).obj D).obj i =
      (Functor.fiberFunctorOfCompEq
        (isFibredOneMorphism_toQuotientStack G).comp_eq
        (𝒰.X i)).obj (D.obj i)
```

**`AlgebraicGeometry.Stack.presentingDescentFunctor_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L416). The attribute's comment: “part (2): transition specification”.

> **Stacks 044X**, part (2). The transition isomorphism of the projected descent datum on an
> overlap is the image under `π` of the arrow of the arrow space, conjugated by the canonical
> comparisons between the chosen pullbacks of the images and the images of the chosen
> pullbacks.

```lean
theorem presentingDescentFunctor_hom
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T)
    (D : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰)
    {W : BigFppfOver C S hS} (q : W ⟶ T)
    {i j : 𝒰.I₀} (a : W ⟶ 𝒰.X i) (b : W ⟶ 𝒰.X j)
    (ha : a ≫ 𝒰.f i = q) (hb : b ≫ 𝒰.f j = q) :
    HEq (((presentingDescentFunctor G 𝒰).obj D).hom q a b ha hb)
      (((isFibredOneMorphism_toQuotientStack G).mapPullbackFiberIso
        (D.obj i) a).hom ≫
      (Functor.fiberFunctorOfCompEq
        (isFibredOneMorphism_toQuotientStack G).comp_eq W).map
          (D.hom q a b ha hb) ≫
      ((isFibredOneMorphism_toQuotientStack G).mapPullbackFiberIso
        (D.obj j) b).inv)
```

**`AlgebraicGeometry.Stack.presentingDescentFunctor_map_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L436). The attribute's comment: “part (5): local arrows of the projected morphism”.

> **Stacks 044X**, part (5). On morphisms the projection applies `π` to each local arrow of
> the arrow space.

```lean
theorem presentingDescentFunctor_map_hom
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T)
    {D E : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰}
    (f : D ⟶ E) (i : 𝒰.I₀) :
    HEq (((presentingDescentFunctor G 𝒰).map f).hom i)
      ((Functor.fiberFunctorOfCompEq
        (isFibredOneMorphism_toQuotientStack G).comp_eq
        (𝒰.X i)).map (f.hom i))
```

**`AlgebraicGeometry.Stack.exists_presentingDescentDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 712](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L712). The attribute's comment: “parts (1)–(3): local presenting descent datum”.

> **Stacks 044X**, parts (1)–(3). Every object `x` of a fibre of the quotient stack is, after
> an fppf covering of the test object, the projection of a descent datum for the pointwise
> groupoid presentation: there is a covering `𝒰` indexed in the universe of the site, a system
> `(u i, r i j)` of points of the object space and arrows of the arrow space forming a descent
> datum for the presentation relative to `𝒰`, and an isomorphism between the canonical descent
> datum of `x` and the projection of that system. The local isomorphisms `f i ^* x ≅ π (u i)` and
> their transition arrows are the components of that isomorphism.

```lean
theorem exists_presentingDescentDatum
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS)
    (x : (quotientStack G).p.Fiber T) :
    ∃ (𝒰 : PreZeroHypercover.{u} T)
      (_ : 𝒰.sieve₀ ∈ BigFppfOver.topology C S hS T)
      (D : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰),
      Nonempty (((Functor.toFamilyDescentDatum
        (quotientStack G).p 𝒰).obj x) ≅
          (presentingDescentFunctor G 𝒰).obj D)
```

**`AlgebraicGeometry.Stack.effective_presentingDescentDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 736](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L736). The attribute's comment: “part (4): effectivity”.

> **Stacks 044X**, part (4). Every descent datum for the pointwise groupoid presentation
> relative to an fppf covering arises as in parts (1)–(3): its projection is the canonical descent
> datum of an object of the fibre of the quotient stack over the test object. This is the
> effectivity of descent data in the stack `[U/R]`.

```lean
theorem effective_presentingDescentDatum
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T)
    (h𝒰 : 𝒰.sieve₀ ∈ BigFppfOver.topology C S hS T)
    (D : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰) :
    ∃ x : (quotientStack G).p.Fiber T,
      Nonempty (((Functor.toFamilyDescentDatum
        (quotientStack G).p 𝒰).obj x) ≅
          (presentingDescentFunctor G 𝒰).obj D)
```

**`AlgebraicGeometry.Stack.fullyFaithful_presentingDescentFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 754](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L754). The attribute's comment: “part (5): morphisms of presenting data”.

> **Stacks 044X**, part (5). For a fixed covering the projection is fully faithful on descent
> data for the presentation: a morphism of the projected data is the image of a unique compatible
> family of arrows of the arrow space.

```lean
theorem fullyFaithful_presentingDescentFunctor
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T) :
    Nonempty (presentingDescentFunctor G 𝒰).FullyFaithful
```

**`AlgebraicGeometry.Stack.homEquiv_presentingDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 796](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L796). The attribute's comment: “part (5): canonical bijection”.

> **Stacks 044X**, part (5). The canonical bijection between the morphisms `x ⟶ y` of a fibre
> of the quotient stack and the morphisms of the descent data for the presentation that represent
> `x` and `y`, together with the equation that characterises it: the projection of the morphism of
> descent data is the canonical descent datum morphism of `f`, conjugated by the two
> representing isomorphisms.

```lean
noncomputable def homEquiv_presentingDescentDatum
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS} (𝒰 : PreZeroHypercover.{w} T)
    (h𝒰 : 𝒰.sieve₀ ∈ BigFppfOver.topology C S hS T)
    (x y : (quotientStack G).p.Fiber T)
    (D E : Functor.FamilyDescentDatum (quotientPrestack G).p 𝒰)
    (δ : (Functor.toFamilyDescentDatum (quotientStack G).p 𝒰).obj x ≅
      (presentingDescentFunctor G 𝒰).obj D)
    (ε : (Functor.toFamilyDescentDatum (quotientStack G).p 𝒰).obj y ≅
      (presentingDescentFunctor G 𝒰).obj E) :
    {e : (x ⟶ y) ≃ (D ⟶ E) //
      ∀ f, (presentingDescentFunctor G 𝒰).map (e f) = δ.inv ≫
        (Functor.toFamilyDescentDatum (quotientStack G).p 𝒰).map f ≫ ε.hom}
```

**`AlgebraicGeometry.Stack.presentingDescentFunctor_refinementIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean, line 904](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/PresentingDescentData.lean#L904). The attribute's comment: “part (6): refinement compatibility”.

> **Stacks 044X**, part (6). The correspondence of parts (1)–(5) is compatible with refinement
> of the fppf covering: projecting a descent datum for the presentation and then pulling it back
> along a refinement is naturally isomorphic to pulling it back first and then projecting, and the
> isomorphism is natural in the descent datum, hence compatible with the bijection of part (5).

```lean
noncomputable def presentingDescentFunctor_refinementIso
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {T : BigFppfOver C S hS}
    {𝒰 : PreZeroHypercover.{w} T} {𝒱 : PreZeroHypercover.{w} T}
    (Φ : 𝒱.HomOver 𝒰 (𝟙 T)) :
    presentingDescentFunctor G 𝒰 ⋙
        Functor.FamilyDescentDatum.pullFunctor (quotientStack G).p Φ ≅
      Functor.FamilyDescentDatum.pullFunctor (quotientPrestack G).p Φ ⋙
        presentingDescentFunctor G 𝒱
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.24, Tag 04MB](https://stacks.math.columbia.edu/tag/04MB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
