---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.EtaleSmoothLift, AlgebraicGeometry.Stack.EtaleSmoothLift.Hom, AlgebraicGeometry.Stack.EtaleSmoothLift.instCategory, AlgebraicGeometry.Stack.EtaleSmoothLift.proj, AlgebraicGeometry.Stack.EtaleSmoothLift.isThickening_inclusion, AlgebraicGeometry.Stack.EtaleSmoothLift.Hom.isEtale_ambient, AlgebraicGeometry.Stack.EtaleSmoothLift.isEtale_ambient, AlgebraicGeometry.Stack.EtaleSmoothLift.isFiberedInGroupoids_proj
statement: formalized
proof: formalized
---

# 106.6 Lifting affines

Section 106.6 of the Stacks Project, [Tag 0CJN](https://stacks.math.columbia.edu/tag/0CJN). 9 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CJP, a remark

[Tag 0CJP](https://stacks.math.columbia.edu/tag/0CJP) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean#L191). The attribute's comment: “objects”.

> **Stacks 0CJP, the objects.** For a thickening `ι : 𝒳 ⟶ 𝒳'` of algebraic stacks over `S` and
> a smooth 1-morphism `x` from an algebraic space `W` to `𝒳`, a *smooth lift of an étale open of
> `W`* consists of an algebraic space `U` étale over `W` through `a : U ⟶ W`, an algebraic space
> `U'` containing it through `i : U ⟶ U'`, a smooth 1-morphism `x' : U' ⟶ 𝒳'`, and a 2-morphism
> filling the square with sides `a`, `x`, `ι`, `i`, `x'` which exhibits it as the 2-fibre product
> `U = 𝒳 ×_{𝒳'} U'`.
>
> The last condition forces `i` to be a thickening, so no thickening hypothesis is imposed on
> it.

```lean
structure EtaleSmoothLift (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (ι : 𝒳 ⟶ 𝒳') (_hι : IsThickening ι)
    (W : AlgebraicSpaces B S hS)
    (x : (algebraicSpaceStackFunctor B S hS).obj W ⟶ 𝒳)
    (_hx : AlgebraicStacks.IsSmooth B S hS x)
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean#L336). The attribute's comment: “morphisms”.

> **Stacks 0CJP, the morphisms.** A morphism of smooth lifts of étale opens of `W` from
> `(U, U', a, i, x', α)` to `(V, V', b, j, y', β)` is a morphism `f : U ⟶ V` over `W`, a morphism
> `f' : U' ⟶ V'` restricting to `f` on `U`, and a 2-morphism `γ : x' ⟶ y' ∘ f'` filling the
> right-hand triangle, compatible with the two fillers in the sense that `i^*γ ∘ α = f^*β`.

```lean
structure Hom (ξ η : EtaleSmoothLift B S hS ι hι W x hx)
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean#L450). The attribute's comment: “category”.

> **Stacks 0CJP, the category.** The smooth lifts of the étale opens of `W` along the
> thickening `ι`, with the morphisms above, their identities and their composition.

```lean
instance instCategory : Category (EtaleSmoothLift B S hS ι hι W x hx)
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.proj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCategory.lean#L461). The attribute's comment: “projection”.

> **Stacks 0CJP, the projection.** The functor sending a smooth lift to the étale open
> `a : U ⟶ W` it lies over and a morphism of smooth lifts to its component `f : U ⟶ V`.

```lean
def proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ Space.SpacesEtale B S hS W
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isThickening_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean#L228). The attribute's comment: “the inclusion of an object is a thickening”.

> **Stacks 0CJP, the inclusion of an object is a thickening.** For a smooth lift
> `(U, U', a, i, x', α)` the 2-fibre product condition `U = 𝒳 ×_{𝒳'} U'` exhibits `i : U ⟶ U'` as
> the base change of the thickening `ι : 𝒳 ⟶ 𝒳'` along `x' : U' ⟶ 𝒳'`, so `i` is a thickening by
> **Stacks 0BPR**, `AlgebraicGeometry.Stack.isThickening_baseChange`.
>
> This is the source's "In particular `U ⊂ U'` is a thickening", which Remark 0CJP asserts and
> `StacksFrontier.AlgebraicGeometry.Stacks.LiftingAffinesCategory` records only in prose; Stacks 0CJU
> re-uses it as "above we have already shown that there is a thickening `i : U ⟶ U'`". The
> conclusion is read in the 2-category of algebraic stacks, that is for the 1-morphism which
> `AlgebraicGeometry.Stack.algebraicSpaceStackFunctor` attaches to `i`; see the implementation
> notes for why it cannot yet be read as `AlgebraicGeometry.Space.IsThickeningHom` on `i`
> itself.

```lean
theorem isThickening_inclusion (ξ : EtaleSmoothLift B S hS ι hι W x hx) :
    IsThickening ((algebraicSpaceStackFunctor B S hS).map ξ.inclusion)
```

## Tag 0CJS, a lemma

[Tag 0CJS](https://stacks.math.columbia.edu/tag/0CJS) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift.Hom.isEtale_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleAmbient.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleAmbient.lean#L226).

> **Stacks 0CJS.** For a morphism `(f, f', γ)` of smooth lifts of étale opens of `W` along the
> thickening `ι : 𝒳 ⟶ 𝒳'` (**Stacks 0CJP**), from `(U, U', a, i, x', α)` to
> `(V, V', b, j, y', β)`, the component `f' : U' ⟶ V'` between the ambient algebraic spaces is
> étale.
>
> As in the source: `f` is étale as a morphism of the spaces-étale site of `W`
> (`AlgebraicGeometry.Stack.EtaleSmoothLift.isEtale_base`, **Stacks 03FV**), and the étale clause
> of **Stacks 0CJC** applies
> (`AlgebraicGeometry.Stack.isEtale_of_isTwoFibreProduct_of_isThickening`), because `x'` and `y'`
> are smooth — hence flat and locally of finite presentation, resp. locally of finite type — and
> `U = 𝒳 ×_{𝒳'} U'`, `V = 𝒳 ×_{𝒳'} V'` are the `isTwoFibreProduct` fields of the two smooth
> lifts.

```lean
theorem isEtale_ambient (ξ η : EtaleSmoothLift B S hS ι hι W x hx) (m : ξ ⟶ η) :
    Space.IsEtale B S hS (Hom.ambient m).hom
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isEtale_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleMorphism.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleMorphism.lean#L126).

> **Stacks 0CJS.** For a morphism `(f, f', γ)` of smooth lifts of étale opens of `W` along the
> thickening `ι`, the component `f' : U' ⟶ V'` between the ambient algebraic spaces is étale.
>
> The hypothesis `hCJC` is the étale clause, item (9), of **Stacks 0CJC** for the thickening `ι`,
> written out for a morphism of two cartesian squares over `ι` whose right-hand legs come from
> algebraic spaces: given that the target's leg `y'` is locally of finite type, that the source's
> leg `x'` is flat and locally of finite presentation, that the two squares are 2-fibre products,
> and that `(f, f', γ)` is a morphism of them over `𝒳'`, étaleness of `f` gives étaleness of `f'`.
> See the implementation notes for why that clause is not available from the three formalized clauses
> of 0CJC.
>
> Everything 0CJC asks for is supplied here from the two smooth lifts and the morphism between
> them: the squares are their `isTwoFibreProduct` fields, the restriction equation, the comparison
> 2-morphism and its coherence are the fields of the morphism, and the three conditions on `x'`
> and `y'` follow from smoothness of the ambient maps — local finite presentation by
> **Stacks 0DNP**, local finite type by **Stacks 06Q5** on top of it, and flatness by
> monotonicity of the smooth-diagram criterion. Étaleness of `f` is `isEtale_base`.

```lean
theorem isEtale_ambient
    (hCJC : ∀ (U U' V V' : AlgebraicSpaces B S hS) (i : U ⟶ U') (j : V ⟶ V')
      (u : (algebraicSpaceStackFunctor B S hS).obj U ⟶ 𝒳)
      (v : (algebraicSpaceStackFunctor B S hS).obj V ⟶ 𝒳)
      (x' : (algebraicSpaceStackFunctor B S hS).obj U' ⟶ 𝒳')
      (y' : (algebraicSpaceStackFunctor B S hS).obj V' ⟶ 𝒳')
      (α : u ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map i ≫ x')
      (β : v ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map j ≫ y'),
      IsTwoFibreProduct
          (⟨(algebraicSpaceStackFunctor B S hS).obj U, u,
            (algebraicSpaceStackFunctor B S hS).map i, α⟩ : TwoCommSq ι x') →
        IsTwoFibreProduct
            (⟨(algebraicSpaceStackFunctor B S hS).obj V, v,
              (algebraicSpaceStackFunctor B S hS).map j, β⟩ : TwoCommSq ι y') →
          AlgebraicStacks.IsFlat B S hS x' →
            AlgebraicStacks.IsLocallyOfFinitePresentation B S hS x' →
              AlgebraicStacks.IsLocallyOfFiniteType B S hS y' →
                ∀ (f : U ⟶ V) (f' : U' ⟶ V')
                  (hL : u ≫ ι = (algebraicSpaceStackFunctor B S hS).map f ≫ (v ≫ ι)),
                  i ≫ f' = f ≫ j →
                    ∀ (γ : x' ⟶ (algebraicSpaceStackFunctor B S hS).map f' ≫ y')
                      (hR : (algebraicSpaceStackFunctor B S hS).map f ≫
                          ((algebraicSpaceStackFunctor B S hS).map j ≫ y') =
                        (algebraicSpaceStackFunctor B S hS).map i ≫
                          ((algebraicSpaceStackFunctor B S hS).map f' ≫ y')),
                      α.hom ≫ ((algebraicSpaceStackFunctor B S hS).map i ◁ γ) =
                          eqToHom hL ≫
                            ((algebraicSpaceStackFunctor B S hS).map f ◁ β.hom) ≫ eqToHom hR →
                        Space.IsEtale B S hS f.hom → Space.IsEtale B S hS f'.hom)
    (ξ η : EtaleSmoothLift B S hS ι hι W x hx) (m : ξ ⟶ η) :
    Space.IsEtale B S hS (Hom.ambient m).hom
```

## Tag 0CJT, a lemma

[Tag 0CJT](https://stacks.math.columbia.edu/tag/0CJT) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isFiberedInGroupoids_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCartesianLifts.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesCartesianLifts.lean#L582).

> **Stacks 0CJT.** The category of smooth lifts of étale opens of `W` along the thickening
> `ι : 𝒳 ⟶ 𝒳'` (**Stacks 0CJP**), projected to the spaces-étale site of `W`, is fibred in
> groupoids (**Stacks 003S**).
>
> Both conditions of Stacks 003S are proved outright, with no hypothesis beyond those of
> Stacks 0CJP. Existence of lifts is
> `AlgebraicGeometry.Stack.EtaleSmoothLift.exists_hom_isHomLift`, the source's construction of
> `f^*ξ` from the topological invariance of the étale site along the thickening `U ⊂ U'`. Unique
> fill-ins hold for *every* pair of morphisms with a common target, which is what Stacks 003S asks
> and is stronger than the source's strongly cartesian verification for its chosen pullbacks
> together with its groupoid-fibre argument: for `φ : η ⟶ ξ`, `ψ : ζ ⟶ ξ` and `h` with
> `φ ∘ h = ψ` on the base, the fill-in is
> `AlgebraicGeometry.Stack.EtaleSmoothLift.fillIn` — its ambient component comes from fullness of
> the étale base change along `U ⊂ U'` (**Stacks 05ZH**, the source's **Stacks 07VW**), applied to
> the cartesian squares of `φ` and `ψ` and to their ambient components, étale by **Stacks 0CJS** —
> and it is unique by faithfulness of that base change and invertibility of the comparison
> 2-morphism of `φ`.

```lean
theorem isFiberedInGroupoids_proj :
    (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).IsFiberedInGroupoids
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.fiber_isGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesFibredInGroupoids.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesFibredInGroupoids.lean#L419). The attribute's comment: “the fibre categories are groupoids”.

> **Stacks 0CJT, the fibre categories are groupoids.** A morphism of the fibre over an étale
> open `U` of `W` lies over the identity of `U`, so its base component is invertible; its ambient
> component is then invertible by `hiso`, and
> `AlgebraicGeometry.Stack.EtaleSmoothLift.isIso_of_isIso_components` makes the morphism itself
> invertible.
>
> The hypothesis `hiso` is the isomorphism clause of **Stacks 0CJC** for the thickening `ι`,
> written out for this category: if the base component of a morphism of smooth lifts is an
> isomorphism then so is its ambient component. It is carried because that clause of 0CJC is not
> available here — see the implementation notes — and **Stacks 0CJC** is the tag that would
> discharge it.

```lean
theorem fiber_isGroupoid
    (hiso : ∀ (ζ ζ' : EtaleSmoothLift B S hS ι hι W x hx) (n : ζ ⟶ ζ'),
      IsIso (Hom.base n) → IsIso (Hom.ambient n))
    (U : Space.SpacesEtale B S hS W) :
    IsGroupoid ((proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U)
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesFibredInGroupoids.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesFibredInGroupoids.lean#L458). The attribute's comment: “fibred in groupoids, granted the fibred-category half”.

> **Stacks 0CJT.** The category of smooth lifts of the étale opens of `W` along the thickening
> `ι`, projected to the spaces-étale site of `W`, is fibred in groupoids. The fibre categories are
> groupoids by `AlgebraicGeometry.Stack.EtaleSmoothLift.fiber_isGroupoid`, and that together with
> the fibred-category half gives the conclusion by **Stacks 003V**.
>
> Two hypotheses are carried. The first, `hiso`, is the isomorphism clause of **Stacks 0CJC** for
> `ι`; see `AlgebraicGeometry.Stack.EtaleSmoothLift.fiber_isGroupoid`. The second, `hfib`, is that
> the projection is a fibred category, which is **Stacks 02XM** in the source's own words, stated
> here as `CategoryTheory.Functor.IsFibredCategory` and converted to Mathlib's class by
> `CategoryTheory.Functor.isFibredCategory_iff_isFibered`: every morphism of the spaces-étale site
> of `W` has a strongly cartesian lift. It is carried because its substantive input is the
> topological invariance of the small étale site along an arbitrary thickening, **Stacks 07VW**,
> which is not available here — every available form of it asks the thickening to be first order — and
> because the source omits the strongly cartesian verification itself. **Stacks 07VW** is the tag
> that would discharge it; see the implementation notes for the full evidence. What `hfib` supplies
> is existence of strongly cartesian lifts; the uniqueness of fill-ins demanded by **Stacks 003S**
> is supplied by the groupoid-fibre half proved here.

```lean
theorem isFiberedInGroupoids
    (hiso : ∀ (ζ ζ' : EtaleSmoothLift B S hS ι hι W x hx) (n : ζ ⟶ ζ'),
      IsIso (Hom.base n) → IsIso (Hom.ambient n))
    (hfib : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).IsFibredCategory) :
    (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).IsFiberedInGroupoids
```

## Tag 0CJU, a lemma

[Tag 0CJU](https://stacks.math.columbia.edu/tag/0CJU) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isStackInGroupoids_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesIsStack.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesIsStack.lean#L148).

> **Stacks 0CJU.** The category `p : 𝒞 ⟶ W_{spaces, étale}` of smooth lifts constructed in
> Stacks 0CJP is a stack in groupoids: the three conditions of Stacks 02ZI, for covering families
> indexed by an arbitrary universe `t`.
>
> There is no hypothesis beyond those of Stacks 0CJP. Condition (1) is
> `AlgebraicGeometry.Stack.EtaleSmoothLift.isFiberedInGroupoids_proj` (Stacks 0CJT); conditions
> (2) and (3) come from `AlgebraicGeometry.Stack.EtaleSmoothLift.isStack_proj` through
> `CategoryTheory.Functor.IsStack.isStackInGroupoids`. See the module docstring for the proof of
> effectivity.

```lean
theorem isStackInGroupoids_proj :
    Functor.IsStackInGroupoids.{t} (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _)
      (Space.SpacesEtale.topology B S hS W)
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isEtale_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean#L272). The attribute's comment: “the two legs of the relation are étale”.

> **Stacks 0CJU, the two legs of the relation are étale.** Both `s_{kk'}` and `t_{kk'}` are
> ambient components of morphisms of the category of smooth lifts, so **Stacks 0CJS** applies to
> each of them.
>
> The hypothesis `hCJC` is the one carried by
> `AlgebraicGeometry.Stack.EtaleSmoothLift.isEtale_ambient`: the étale clause, item (9), of
> **Stacks 0CJC** for the thickening `ι`, which is not available in this library.

```lean
theorem isEtale_relation
    (hCJC : ∀ (U U' V' V'' : AlgebraicSpaces B S hS) (i : U ⟶ U') (j : V' ⟶ V'')
      (u : (algebraicSpaceStackFunctor B S hS).obj U ⟶ 𝒳)
      (v : (algebraicSpaceStackFunctor B S hS).obj V' ⟶ 𝒳)
      (y : (algebraicSpaceStackFunctor B S hS).obj U' ⟶ 𝒳')
      (y' : (algebraicSpaceStackFunctor B S hS).obj V'' ⟶ 𝒳')
      (α : u ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map i ≫ y)
      (β : v ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map j ≫ y'),
      IsTwoFibreProduct
          (⟨(algebraicSpaceStackFunctor B S hS).obj U, u,
            (algebraicSpaceStackFunctor B S hS).map i, α⟩ : TwoCommSq ι y) →
        IsTwoFibreProduct
            (⟨(algebraicSpaceStackFunctor B S hS).obj V', v,
              (algebraicSpaceStackFunctor B S hS).map j, β⟩ : TwoCommSq ι y') →
          AlgebraicStacks.IsFlat B S hS y →
            AlgebraicStacks.IsLocallyOfFinitePresentation B S hS y →
              AlgebraicStacks.IsLocallyOfFiniteType B S hS y' →
                ∀ (g : U ⟶ V') (g' : U' ⟶ V'')
                  (hL : u ≫ ι = (algebraicSpaceStackFunctor B S hS).map g ≫ (v ≫ ι)),
                  i ≫ g' = g ≫ j →
                    ∀ (γ : y ⟶ (algebraicSpaceStackFunctor B S hS).map g' ≫ y')
                      (hR : (algebraicSpaceStackFunctor B S hS).map g ≫
                          ((algebraicSpaceStackFunctor B S hS).map j ≫ y') =
                        (algebraicSpaceStackFunctor B S hS).map i ≫
                          ((algebraicSpaceStackFunctor B S hS).map g' ≫ y')),
                      α.hom ≫ ((algebraicSpaceStackFunctor B S hS).map i ◁ γ) =
                          eqToHom hL ≫
                            ((algebraicSpaceStackFunctor B S hS).map g ◁ β.hom) ≫ eqToHom hR →
                        Space.IsEtale B S hS g.hom → Space.IsEtale B S hS g'.hom)
    (k k' : K) :
    Space.IsEtale B S hS (relationFst D k k').hom ∧
      Space.IsEtale B S hS (relationSnd D k k').hom
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.relation_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean#L316). The attribute's comment: “reflexivity of the relation”.

> **Stacks 0CJU, reflexivity of the relation.** A fibre automorphism `e` of `ξ_k` which is the
> pullback along the diagonal `Δ : U_k ⟶ U_k ×_U U_k ×_U U_k` of each of the three gluing
> isomorphisms of the triple `(k, k, k)` has identity ambient component. This is the first
> identity of **Stacks 026C** read on the ambient spaces.
>
> The hypotheses `hiso` and `hfib` are the two carried by
> `AlgebraicGeometry.Stack.EtaleSmoothLift.isFiberedInGroupoids` (**Stacks 0CJT**), which is where
> the fibred-in-groupoids hypothesis of Stacks 026C comes from.

```lean
theorem relation_refl
    (hiso : ∀ (ζ ζ' : EtaleSmoothLift B S hS ι hι W x hx) (n : ζ ⟶ ζ'),
      IsIso (Hom.base n) → IsIso (Hom.ambient n))
    (hfib : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).IsFibredCategory)
    (k : K) {d : V k ⟶ Vijk k k k}
    {hd₁ : 𝟙 (V k) = d ≫ q₁ k k k} {hd₂ : 𝟙 (V k) = d ≫ q₂ k k k}
    {hd₃ : 𝟙 (V k) = d ≫ q₃ k k k}
    {e : D.x k ⟶ D.x k}
    (he : Functor.FibreHom (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _)
      (D.x k) (D.x k) (D.hx k) (D.hx k) e)
    (heij : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d hd₁ hd₂
      (D.wi k k k) (D.wj k k k)
      (Functor.Restriction.id _ (D.x k) (D.hx k)) (Functor.Restriction.id _ (D.x k) (D.hx k))
      (D.αij k k k) e)
    (hejk : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d hd₂ hd₃
      (D.wj k k k) (D.wk k k k)
      (Functor.Restriction.id _ (D.x k) (D.hx k)) (Functor.Restriction.id _ (D.x k) (D.hx k))
      (D.αjk k k k) e)
    (heik : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d hd₁ hd₃
      (D.wi k k k) (D.wk k k k)
      (Functor.Restriction.id _ (D.x k) (D.hx k)) (Functor.Restriction.id _ (D.x k) (D.hx k))
      (D.αik k k k) e) :
    ambientSpaceFunctor.map e = 𝟙 (D.x k).ambient
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.relation_symm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean#L348). The attribute's comment: “symmetry of the relation”.

> **Stacks 0CJU, symmetry of the relation.** Over the overlap `U_k ×_U U_{k'}` the gluing
> isomorphism `φ_{kk'}` and the pullback `σ^*φ_{k'k}` of `φ_{k'k}` along the switching morphism
> have mutually inverse ambient components: this is the second identity of **Stacks 026C** read on
> the ambient spaces, and it is the source's observation that `φ_{kk'}⁻¹` is the flip of
> `φ_{k'k}`.

```lean
theorem relation_symm (k k' : K) {d₁₃ : Vij k k' ⟶ Vijk k k' k}
    {hd₁ : pr₁ k k' = d₁₃ ≫ q₁ k k' k} {hd₂ : pr₂ k k' = d₁₃ ≫ q₂ k k' k}
    {hd₃ : pr₁ k k' = d₁₃ ≫ q₃ k k' k}
    {σφ : (D.xrji k k').pt ⟶ (D.xrij k k').pt}
    (hσφ : Functor.FibreHom (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _)
      (D.xrji k k').pt (D.xrij k k').pt (D.xrji k k').hpt (D.xrij k k').hpt σφ)
    (hij : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d₁₃ hd₁ hd₂
      (D.wi k k' k) (D.wj k k' k) (D.xrij k k') (D.xrji k k') (D.αij k k' k) (D.φ k k'))
    (hji : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d₁₃ hd₂ hd₃
      (D.wj k k' k) (D.wk k k' k) (D.xrji k k') (D.xrij k k') (D.αjk k k' k) σφ)
    (hik : Functor.IsRestrictionOf (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _) d₁₃ hd₁ hd₃
      (D.wi k k' k) (D.wk k k' k) (D.xrij k k') (D.xrij k k') (D.αik k k' k)
      (𝟙 (D.xrij k k').pt)) :
    ambientSpaceFunctor.map (D.φ k k') ≫ ambientSpaceFunctor.map σφ =
      𝟙 (D.xrij k k').pt.ambient
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.relation_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesStack.lean#L372). The attribute's comment: “transitivity of the relation”.

> **Stacks 0CJU, transitivity of the relation.** Over the triple overlap the cocycle condition
> of the descent datum says that the gluing isomorphism from `ξ_k` to `ξ_{k''}` is the composite
> of the ones from `ξ_k` to `ξ_{k'}` and from `ξ_{k'}` to `ξ_{k''}`; the same therefore holds of
> their ambient components. This is the source's transitivity of the relation.

```lean
theorem relation_trans (k k' k'' : K) :
    ambientSpaceFunctor.map (D.αik k k' k'') =
      ambientSpaceFunctor.map (D.αij k k' k'') ≫ ambientSpaceFunctor.map (D.αjk k k' k'')
```

## Tag 0CJV, a lemma

[Tag 0CJV](https://stacks.math.columbia.edu/tag/0CJV) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_etaleCovering_etaleSmoothLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleCovering.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleCovering.lean#L125). The attribute's comment: “the covering, from the lifts over the affine members”.

> **Stacks 0CJV, the covering.** Let `ι : 𝒳 ⟶ 𝒳'` be a thickening of algebraic stacks over
> `S`, let `W` be an algebraic space over `S` and let `x : W ⟶ 𝒳` be a smooth 1-morphism. Let
> `p : V₀ ⟶ W` be a smooth morphism of algebraic spaces which is surjective on points, and suppose
> that every affine scheme of the site which is étale over `W` through a morphism factoring through
> `p` carries a smooth lift of that étale open along `ι`. Then there is a family of smooth lifts of
> étale opens of `W` along `ι` whose bases form an étale covering of `W`.
>
> The hypothesis `hlift` stands in for Steps 2–4 of the source's proof, which construct the lift
> over one affine member of the covering: the immersion of the affine member into an affine space
> over the chart is a Koszul-regular immersion, its equations lift to the ambient chart of `𝒳'`,
> and the closed subspace they cut out there is smooth over `𝒳'` by **Stacks 0CER**. The covering
> itself is not assumed: it is produced from `p` by **Stacks 0CFV**, and the members are shrunk to
> affine opens.

```lean
theorem exists_etaleCovering_etaleSmoothLift
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (ι : 𝒳 ⟶ 𝒳') (hι : IsThickening ι)
    (W : AlgebraicSpaces B S hS)
    (x : (algebraicSpaceStackFunctor B S hS).obj W ⟶ 𝒳)
    (hx : AlgebraicStacks.IsSmooth B S hS x)
    (V₀ : AlgebraicSpaces B S hS) (p : V₀ ⟶ W)
    (hp : Space.IsSmooth B S hS p.hom)
    (hpsurj : Function.Surjective (Space.pointsMap B S hS V₀.obj p.hom))
    (hlift : ∀ (T : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
      ∀ (t : yoneda.obj T ⟶ W.obj) (ht : Space.IsEtale B S hS t),
        (∃ s : yoneda.obj T ⟶ V₀.obj, s ≫ p.hom = t) →
          ∃ ξ : EtaleSmoothLift B S hS ι hι W x hx,
            ξ.base = Space.SpacesEtale.ofRepresentable B S hS W T t ht) :
    ∃ (J : Type (u + 1)) (ξ : J → EtaleSmoothLift B S hS ι hι W x hx),
      Space.IsEtaleCovering B S hS (fun j => ((ξ j).base.obj.left).obj)
        (fun j => ((ξ j).base.obj.hom).hom)
```

**`AlgebraicGeometry.Stack.exists_isEtaleCovering_etaleSmoothLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleSmoothLift.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEtaleSmoothLift.lean#L128).

> **Stacks 0CJV.** Let `ι : 𝒳 ⟶ 𝒳'` be a thickening of algebraic stacks over `S`, let `W` be an
> algebraic space over `S` and let `x : W ⟶ 𝒳` be a smooth 1-morphism. Then there is a family of
> smooth lifts of étale opens of `W` along `ι` whose bases form an étale covering of `W`: an étale
> covering `{W_j ⟶ W}` with cartesian squares `W_j = 𝒳 ×_{𝒳'} W'_j` and `W'_j ⟶ 𝒳'` smooth.

```lean
theorem exists_isEtaleCovering_etaleSmoothLift
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (ι : 𝒳 ⟶ 𝒳') (hι : IsThickening ι)
    (W : AlgebraicSpaces B S hS)
    (x : (algebraicSpaceStackFunctor.{u, w} B S hS).obj W ⟶ 𝒳)
    (hx : AlgebraicStacks.IsSmooth B S hS x) :
    ∃ (J : Type (u + 1)) (ξ : J → EtaleSmoothLift B S hS ι hι W x hx),
      Space.IsEtaleCovering B S hS (fun j => ((ξ j).base.obj.left).obj)
        (fun j => ((ξ j).base.obj.hom).hom)
```

## Tag 0CJW, a lemma

[Tag 0CJW](https://stacks.math.columbia.edu/tag/0CJW) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isEtaleCovering_ambientComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesAmbientComparison.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesAmbientComparison.lean#L503).

> **Stacks 0CJW.** Let `ι : 𝒳 ⟶ 𝒳'` be a thickening of algebraic stacks over `S` and let
> `W = 𝒳 ×_{𝒳'} W'` and `W = 𝒳 ×_{𝒳'} W''` be two 2-fibre products, along `x' : W' ⟶ 𝒳'` and
> `x'' : W'' ⟶ 𝒳'`, with `W`, `W'`, `W''` algebraic spaces, inclusions `i : W ⟶ W'`,
> `i'' : W ⟶ W''`, fillers `α'`, `α''` and the vertical 1-morphisms `x`, `x'`, `x''` smooth. Then
> there are an étale covering `{f'_k : W'_k ⟶ W'}`, étale morphisms `f''_k : W'_k ⟶ W''` and
> 2-isomorphisms `γ_k : x'' ∘ f''_k ≅ x' ∘ f'_k` such that, for each `k`, a single algebraic space
> `U` with `e : U ⟶ W'_k` and `g : U ⟶ W` is a pullback both of `i` along `f'_k` and of `i''` along
> `f''_k` — that is, `(f'_k)⁻¹(W) = (f''_k)⁻¹(W)` and the two restrictions to it agree — and `γ_k`
> restricted to `U` is the filler `α''⁻¹ ≫ α'` of the given diagram over `W`, restricted along `g`.
>
> This is `exists_isEtaleCovering_ambientComparison_of_lifting` at Stacks 0CHJ,
> `AlgebraicGeometry.Space.exists_isEtaleCovering_lift_of_isSmooth_of_isThickeningHom`. The
> smoothness of `x` is part of the source's hypotheses and is not used.

```lean
theorem exists_isEtaleCovering_ambientComparison
    (hι : IsThickening ι) {W W' W'' : AlgebraicSpaces B S hS}
    {x : (algebraicSpaceStackFunctor B S hS).obj W ⟶ 𝒳}
    {x' : (algebraicSpaceStackFunctor B S hS).obj W' ⟶ 𝒳'}
    {x'' : (algebraicSpaceStackFunctor B S hS).obj W'' ⟶ 𝒳'}
    (hx : AlgebraicStacks.IsSmooth B S hS x) (hx' : AlgebraicStacks.IsSmooth B S hS x')
    (hx'' : AlgebraicStacks.IsSmooth B S hS x'')
    {i : W ⟶ W'} {i'' : W ⟶ W''}
    {α' : x ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map i ≫ x'}
    {α'' : x ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map i'' ≫ x''}
    (h' : IsTwoFibreProduct (⟨(algebraicSpaceStackFunctor B S hS).obj W, x,
        (algebraicSpaceStackFunctor B S hS).map i, α'⟩ : TwoCommSq ι x'))
    (h'' : IsTwoFibreProduct (⟨(algebraicSpaceStackFunctor B S hS).obj W, x,
        (algebraicSpaceStackFunctor B S hS).map i'', α''⟩ : TwoCommSq ι x'')) :
    ∃ (K : Type (u + 1)) (V : K → AlgebraicSpaces B S hS) (f' : ∀ k, V k ⟶ W')
      (f'' : ∀ k, V k ⟶ W'')
      (γ : ∀ k, (algebraicSpaceStackFunctor B S hS).map (f'' k) ≫ x'' ≅
        (algebraicSpaceStackFunctor B S hS).map (f' k) ≫ x'),
      Space.IsEtaleCovering B S hS (fun k => (V k).obj) (fun k => (f' k).hom) ∧
      (∀ k, Space.IsEtale B S hS (f'' k).hom) ∧
      ∀ k, ∃ (U : AlgebraicSpaces B S hS) (e : U ⟶ V k) (g : U ⟶ W)
        (h₁ : IsPullback g e i (f' k)) (h₂ : IsPullback g e i'' (f'' k)),
        (algebraicSpaceStackFunctor B S hS).map e ◁ (γ k).hom =
          eqToHom (algebraicSpaceStackFunctor_map_comp_whisker_eq h₂.w.symm x'') ≫
            ((algebraicSpaceStackFunctor B S hS).map g ◁ (α''.inv ≫ α'.hom)) ≫
            eqToHom (algebraicSpaceStackFunctor_map_comp_whisker_eq h₁.w x')
```

## Tag 0CJX, a lemma

[Tag 0CJX](https://stacks.math.columbia.edu/tag/0CJX) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift.isGerbe_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesGerbe.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesGerbe.lean#L370).

> The category `p : 𝒞 ⟶ W_{spaces, étale}` of smooth lifts of étale opens of `W` along the
> thickening `ι : 𝒳 ⟶ 𝒳'` constructed in Stacks 0CJP is a gerbe (Stacks 06NZ), for covering
> families indexed by an arbitrary universe `t` in the stack condition.

```lean
theorem isGerbe_proj :
    Functor.IsGerbe.{t} (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _)
      (Space.SpacesEtale.topology B S hS W)
```

## Tag 0CKG, a lemma

[Tag 0CKG](https://stacks.math.columbia.edu/tag/0CKG) in the Stacks Project.

**`AlgebraicGeometry.Stack.EtaleSmoothLift.fiber_endomorphisms_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesAutomorphismAbelian.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesAutomorphismAbelian.lean#L482). The attribute's comment: “part (1): the automorphism sheaves of objects of the category of smooth lifts are abelian”.

> **Stacks 0CKG, part (1).** Let `𝒳 ⊂ 𝒳'` be a first-order thickening of algebraic stacks, `W` an
> algebraic space and `x : W ⟶ 𝒳` smooth, and consider the category `𝒞` of smooth lifts of the étale
> opens of `W` along the thickening with its projection `p : 𝒞 ⟶ W_{spaces, étale}`
> (Stacks 0CJP). Then the automorphism sheaves of the objects of `𝒞` are abelian: for every étale
> open `U` of `W` and every object `ζ` of the fibre over `U`, the endomorphisms of `ζ` in that fibre
> commute.

```lean
theorem fiber_endomorphisms_comm (hι₁ : AlgebraicStacks.IsFirstOrderThickening B S hS ι)
    (U : Space.SpacesEtale B S hS W)
    (ζ : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U) (α β : ζ ⟶ ζ) :
    α ≫ β = β ≫ α
```

**`AlgebraicGeometry.Stack.EtaleSmoothLift.exists_band_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesBandQuasicoherent.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesBandQuasicoherent.lean#L265). The attribute's comment: “part (2): the sheaf of groups `𝒢` of Stacks 0CJY is a quasi-coherent `𝒪_W`-module”.

> **Stacks 0CKG (2).** In Situation 0CJP, let `𝒳 ⊂ 𝒳'` be a first order thickening. Then the
> sheaf of groups `𝒢` of Stacks 0CJY — the band of the gerbe `p : 𝒞 ⟶ W_{spaces,étale}` of smooth
> lifts, with its banding `θ` and the three clauses of 0CJY — is a quasi-coherent `𝒪_W`-module: its
> restriction to `W_étale` (Stacks 03G1) underlies a quasi-coherent `𝒪_W`-module `M`.
>
> The gerbe inputs are proved (Stacks 0CJU, 0CJX) and so is the commutativity of the automorphism
> groups (part (1)); nothing is assumed beyond Situation 0CJP and the first order thickening.

```lean
theorem exists_band_isQuasicoherent (hι₁ : AlgebraicStacks.IsFirstOrderThickening B S hS ι) :
               haveI : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).IsFibered :=
        isFiberedInGroupoids_proj.isFibered
      haveI : ∀ U, IsGroupoid ((proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U) :=
        isFiberedInGroupoids_proj.fiber_isGroupoid
      ∃ (𝒢 : Sheaf (Space.SpacesEtale.topology B S hS W) CommGrpCat.{u + 1})
        (θ : ∀ (U : Space.SpacesEtale B S hS W)
          (y : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U),
          (Over.forget U).op ⋙ 𝒢.obj ⋙ forget CommGrpCat.{u + 1} ≅
            (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).morPresheaf y y ⋙
              uliftFunctor.{u + 1, u + 1}),
        (∀ (U : Space.SpacesEtale B S hS W)
            (y : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U) (g : Over U)
            (a b : 𝒢.obj.obj (op g.left)),
            ((θ U y).hom.app (op g) (a * b)).down =
              ((θ U y).hom.app (op g) a).down ≫ ((θ U y).hom.app (op g) b).down) ∧
          (∀ (U : Space.SpacesEtale B S hS W)
              (y z : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U) (φ : y ⟶ z)
              (g : Over U) (a : 𝒢.obj.obj (op g.left)),
            ((θ U z).hom.app (op g) a).down =
              Functor.pullbackFiberHom (CategoryTheory.inv φ) g.hom ≫
                ((θ U y).hom.app (op g) a).down ≫ Functor.pullbackFiberHom φ g.hom) ∧
          (∀ (U : Space.SpacesEtale B S hS W)
            (y : (proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).Fiber U) (g : Over U)
            (a : 𝒢.obj.obj (op g.left)),
            ((θ U y).hom.app (op g) a).down =
              (Functor.pullbackFiberIdIso
                  ((proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).pullbackFiber y g.hom)).inv ≫
                ((θ g.left ((proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).pullbackFiber y
                    g.hom)).hom.app (op (Over.mk (𝟙 g.left))) a).down ≫
                  (Functor.pullbackFiberIdIso
                    ((proj : EtaleSmoothLift B S hS ι hι W x hx ⥤ _).pullbackFiber y
                      g.hom)).hom) ∧
          ∃ M : SheafOfModules.{u + 1} (Space.structureRingSheaf B S hS W),
            M.IsQuasicoherentOnSite ∧
              Nonempty ((Space.spacesEtaleAbelianRestriction B S hS W).obj
                ((sheafCompose _ commGroupAddCommGroupEquivalence.{u + 1}.functor).obj 𝒢) ≅
                (SheafOfModules.toSheaf _).obj M)
```

## Tag 0CKI, a proposition

[Tag 0CKI](https://stacks.math.columbia.edu/tag/0CKI) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_smooth_affine_lift_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEmertonLift.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LiftingAffinesEmertonLift.lean#L56).

> **Stacks 0CKI (Emerton).** Let `ι : 𝒳 ⟶ 𝒳'` be a first order thickening of algebraic stacks,
> let `W` be affine and let `x : W ⟶ 𝒳` be smooth. Then there are an affine `W'`, a morphism
> `i : W ⟶ W'` and a smooth `x' : W' ⟶ 𝒳'` such that the square `x ≫ ι ≅ i ≫ x'` is
> 2-cartesian, i.e. `W = 𝒳 ×_{𝒳'} W'`.
>
> Here `W` and `W'` are algebraic spaces that are affine, that is, representable by affine schemes,
> viewed as algebraic stacks through `algebraicSpaceStackFunctor`.

```lean
theorem exists_smooth_affine_lift_of_isFirstOrderThickening {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS}
    {ι : 𝒳 ⟶ 𝒳'} (hι₁ : IsFirstOrderThickening B S hS ι) (W : AlgebraicSpaces B S hS)
    (hW : Space.IsAffineSpace B S hS W.obj) (x : (algebraicSpaceStackFunctor B S hS).obj W ⟶ 𝒳)
    (hx : IsSmooth B S hS x) :
    ∃ (W' : AlgebraicSpaces B S hS) (i : W ⟶ W')
      (x' : (algebraicSpaceStackFunctor B S hS).obj W' ⟶ 𝒳')
      (α : x ≫ ι ≅ (algebraicSpaceStackFunctor B S hS).map i ≫ x'),
      IsSmooth B S hS x' ∧
        Nonempty (IsTwoFibreProduct
          (⟨(algebraicSpaceStackFunctor B S hS).obj W, x,
            (algebraicSpaceStackFunctor B S hS).map i, α⟩ : TwoCommSq ι x')) ∧
        Space.IsAffineSpace B S hS W'.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.6, Tag 0CJN](https://stacks.math.columbia.edu/tag/0CJN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
