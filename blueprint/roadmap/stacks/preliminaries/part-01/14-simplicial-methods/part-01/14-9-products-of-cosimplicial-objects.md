---
declaration: section
origin: cited
lean: CategoryTheory.Limits.pointwiseProd, CategoryTheory.Limits.map_eq_prod_lift_comp_prod_map_comp_inv, CategoryTheory.Limits.pointwiseProdIsProd
statement: formalized
proof: formalized
---

# 14.9 Products of cosimplicial objects

Section 14.9 of the Stacks Project, [Tag 016Y](https://stacks.math.columbia.edu/tag/016Y). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 016Z, a definition

[Tag 016Z](https://stacks.math.columbia.edu/tag/016Z) in the Stacks Project.

**`CategoryTheory.Limits.pointwiseProd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean#L98). References: EGA 0 (8.2.1), “more general”; EGA I (3.3.2), “more general”.

> The **pointwise product** of two functors `F G : D ⥤ C`, defined when the products
> `F.obj d ⨯ G.obj d` exist in `C`: it sends `d` to `F.obj d ⨯ G.obj d` and a morphism
> `f : d ⟶ d'` to `prod.map (F.map f) (G.map f)`.
>
> For `D = SimplexCategory` this is the product `U × V` of two cosimplicial objects `U`, `V`
> of `C` of [Stacks, Tag 016Z]. It is the product formed pointwise in `C`, not by definition a
> product in the category `D ⥤ C`; that it is one is `pointwiseProdIsProd`, [Stacks, Tag 0170].

```lean
def pointwiseProd (F G : D ⥤ C) [∀ d, HasBinaryProduct (F.obj d) (G.obj d)] : D ⥤ C
```

**`CategoryTheory.Limits.map_eq_prod_lift_comp_prod_map_comp_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean#L233). The attribute's comment: “the definition's second clause, stated for an arbitrary functor satisfying the first: it is forced by the degrees and the two projections. Stated over an arbitrary index category `D`: the product of two cosimplicial objects is the case `D = SimplexCategory` and that of simplicial objects the case `D = SimplexCategoryᵒᵖ`”.

> **The product of two cosimplicial objects acts on morphisms by the product of the maps**,
> [Stacks, Tag 016Z]: let `F G P : D ⥤ C` be functors such that the products `F.obj d ⨯ G.obj d`
> exist in `C`, let `π₁ : P ⟶ F` and `π₂ : P ⟶ G` be natural transformations, and let `φ : d ⟶ d'`
> be a morphism such that the comparison map `prod.lift (π₁.app d') (π₂.app d')` is an isomorphism.
> Then `P.map φ` is `prod.map (F.map φ) (G.map φ)`, read through the comparison maps at `d` and
> `d'`.
>
> So the second clause of the definition of the product of `F` and `G` holds of every functor which
> is degreewise the product over its two projections. The functor of the definition itself is
> `pointwiseProd F G`, and that it is a product in `D ⥤ C` is `pointwiseProdIsProd`.

```lean
theorem map_eq_prod_lift_comp_prod_map_comp_inv {F G P : D ⥤ C}
    [∀ d, HasBinaryProduct (F.obj d) (G.obj d)] (π₁ : P ⟶ F) (π₂ : P ⟶ G) {d d' : D} (φ : d ⟶ d')
    [IsIso (prod.lift (π₁.app d') (π₂.app d'))] :
    P.map φ = prod.lift (π₁.app d) (π₂.app d) ≫ prod.map (F.map φ) (G.map φ) ≫
      inv (prod.lift (π₁.app d') (π₂.app d'))
```

## Tag 0170, a lemma

[Tag 0170](https://stacks.math.columbia.edu/tag/0170) in the Stacks Project.

**`CategoryTheory.Limits.pointwiseProdIsProd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean#L125). The attribute's comment: “stated for an arbitrary index category `D`: the product of cosimplicial objects is the case `D = SimplexCategory`, that of simplicial objects the case `D = SimplexCategoryᵒᵖ`”. References: EGA 0 (8.2.1), “more general”.

> **The pointwise product of two functors is their product**, [Stacks, Tag 0170]: for functors
> `F G : D ⥤ C` whose pointwise products exist, the binary fan on `F` and `G` with point the
> pointwise product `pointwiseProd F G` of [Stacks, Tag 016Z] and with projections `π₁`, `π₂`
> given degreewise by `prod.fst` and `prod.snd` is a limit. Thus `F` and `G` have a product in
> `D ⥤ C`, computed pointwise, and `Mor(W, F × G) = Mor(W, F) × Mor(W, G)` for every functor `W`.
>
> For `D = Δ` this is the statement that the product `U × V` of two cosimplicial objects of `C`
> is the product in the category of cosimplicial objects of `C`.

```lean
def pointwiseProdIsProd (F G : D ⥤ C)
    [∀ d, HasBinaryProduct (F.obj d) (G.obj d)]
    (π₁ : pointwiseProd F G ⟶ F) (π₂ : pointwiseProd F G ⟶ G)
    (h₁ : ∀ d, π₁.app d = prod.fst) (h₂ : ∀ d, π₂.app d = prod.snd) :
    IsLimit (BinaryFan.mk π₁ π₂)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.9, Tag 016Y](https://stacks.math.columbia.edu/tag/016Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
