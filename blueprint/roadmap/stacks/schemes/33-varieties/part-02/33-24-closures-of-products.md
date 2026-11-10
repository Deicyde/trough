---
declaration: section
origin: cited
lean: AlgebraicGeometry.closure_product, AlgebraicGeometry.closure_range_pullback_map, AlgebraicGeometry.existsUnique_imageProductMapIso
statement: formalized
proof: formalized
---

# 33.24 Closures of products

Section 33.24 of the Stacks Project, [Tag 047A](https://stacks.math.columbia.edu/tag/047A). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 047B, a lemma

[Tag 047B](https://stacks.math.columbia.edu/tag/047B) in the Stacks Project.

**`AlgebraicGeometry.closure_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ClosureProduct.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ClosureProduct.lean#L111). References: EGA IV (2.4.11), “more general”.

> **Stacks Project, Tag 047B.** The set-theoretic fibre product of the closures of two
> subsets of schemes over a field is the closure of their set-theoretic fibre product.

```lean
theorem closure_product {k : Type u} [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k)) (A : Set X) (B : Set Y) :
    (pullback.fst f g).base ⁻¹' closure A ∩ (pullback.snd f g).base ⁻¹' closure B =
      closure ((pullback.fst f g).base ⁻¹' A ∩ (pullback.snd f g).base ⁻¹' B)
```

## Tag 04Q0, a lemma

[Tag 04Q0](https://stacks.math.columbia.edu/tag/04Q0) in the Stacks Project.

**`AlgebraicGeometry.closure_range_pullback_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ClosureProduct.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/ClosureProduct.lean#L169).

> **Stacks Project, Tag 04Q0.** For morphisms `f : A ⟶ X` and `g : B ⟶ Y` of schemes over a
> field, the closure of the image of the induced morphism `A ×ₖ B ⟶ X ×ₖ Y` is the
> set-theoretic fibre product of the closures of the two images.

```lean
theorem closure_range_pullback_map {k : Type u} [Field k] {A B X Y : Scheme.{u}}
    (pA : A ⟶ Spec (.of k)) (pB : B ⟶ Spec (.of k))
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    (f : A ⟶ X) (g : B ⟶ Y) (hf : f ≫ pX = pA) (hg : g ≫ pY = pB) :
    (pullback.fst pX pY).base ⁻¹' closure (Set.range f.base) ∩
        (pullback.snd pX pY).base ⁻¹' closure (Set.range g.base) =
      closure (Set.range
        (pullback.map pA pB pX pY f g (𝟙 _)
          (by simpa using hf.symm) (by simpa using hg.symm)).base)
```

## Tag 04Q1, a lemma

[Tag 04Q1](https://stacks.math.columbia.edu/tag/04Q1) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_imageProductMapIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/SchemeTheoreticImage.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/SchemeTheoreticImage.lean#L100).

> The image of the product of two quasi-compact maps over a field is canonically isomorphic,
> over the product of their targets, to the product of their scheme-theoretic images.

```lean
public theorem existsUnique_imageProductMapIso
    {k : Type u} [Field k] {A B X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    (f : A ⟶ X) (g : B ⟶ Y) [QuasiCompact f] [QuasiCompact g] :
    ∃! e : (productMap pX pY f g).image ≅
        pullback (f.imageι ≫ pX) (g.imageι ≫ pY),
      e.hom ≫ productMap pX pY f.imageι g.imageι =
        (productMap pX pY f g).imageι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.24, Tag 047A](https://stacks.math.columbia.edu/tag/047A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
