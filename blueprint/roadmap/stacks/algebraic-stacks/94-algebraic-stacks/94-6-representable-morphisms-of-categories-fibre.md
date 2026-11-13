---
declaration: section
origin: cited
lean: Stacks.RepresentableMorphism.isRepresentableMorphism_overMap, Stacks.RepresentableMorphism.isRepresentableMorphism_iff_of_equivalences, Stacks.RepresentableMorphism.isRepresentableMorphism_comp, Stacks.RepresentableMorphism.isRepresentableMorphism_fst_twoFibreProductOver, Stacks.RepresentableMorphism.isRepresentableMorphism_product
statement: formalized
proof: formalized
---

# 94.6 Representable morphisms of categories fibred in groupoids

Section 94.6 of the Stacks Project, [Tag 04ST](https://stacks.math.columbia.edu/tag/04ST). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02ZR, a lemma

[Tag 02ZR](https://stacks.math.columbia.edu/tag/02ZR) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_overMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Slices.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Slices.lean#L315).

> **Stacks 02ZR.** A morphism in a category with pullbacks induces a
> representable 1-morphism of the categories fibred in groupoids of objects over
> its source and target.

```lean
public theorem isRepresentableMorphism_overMap (f : X ⟶ Y) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism (Over.forget X) (Over.forget Y)
      (Over.map f)
```

## Tag 0456, a lemma

[Tag 0456](https://stacks.math.columbia.edu/tag/0456) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_iff_of_equivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Invariance.lean, line 660](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Invariance.lean#L660).

> **Stacks 0456.** Representability of a 1-morphism of categories fibred in
> groupoids is invariant under equivalences in a 2-commutative square.

```lean
public theorem isRepresentableMorphism_iff_of_equivalences
    (f' : 𝒳' ⟶ 𝒴') (f : 𝒳 ⟶ 𝒴)
    (a : 𝒳' ⟶ 𝒳) (b : 𝒴' ⟶ 𝒴)
    (α : a ≫ f ≅ f' ≫ b)
    [Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor a)]
    [Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor b)] :
    Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor f) ↔
    Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳'.val.p 𝒴'.val.p
      (CatFiberedInGroupoids.homFunctor f')
```

## Tag 02ZS, a lemma

[Tag 02ZS](https://stacks.math.columbia.edu/tag/02ZS) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Composition.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Composition.lean#L277).

> **Stacks 02ZS.** A composite of representable 1-morphisms of categories fibred in
> groupoids over a base category is representable.

```lean
public lemma isRepresentableMorphism_comp
    (p : 𝒳 ⥤ 𝒞) (q : 𝒴 ⥤ 𝒞) (r : 𝒵 ⥤ 𝒞)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hr : r.IsFiberedInGroupoids)
    (F : 𝒳 ⥤ 𝒴) (G : 𝒴 ⥤ 𝒵)
    (hF : F ⋙ q = p) (hG : G ⋙ r = q)
    (hrepF : Stacks.RepresentableMorphism.IsRepresentableMorphism p q F)
    (hrepG : Stacks.RepresentableMorphism.IsRepresentableMorphism q r G) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism p r (F ⋙ G)
```

## Tag 02ZT, a lemma

[Tag 02ZT](https://stacks.math.columbia.edu/tag/02ZT) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_fst_twoFibreProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/BaseChange.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/BaseChange.lean#L436).

> **Stacks Project, Tag 02ZT.** The projection to `𝒵` from the 2-fibre
> product `𝒵 ×_𝒴 𝒳` is representable when `𝒳 ⥤ 𝒴` is representable.

```lean
public theorem isRepresentableMorphism_fst_twoFibreProductOver
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒵 : 𝒵 ⥤ 𝒞)
    (F : 𝒳 ⥤ 𝒴) (G : 𝒵 ⥤ 𝒴)
    (hF : F ⋙ p𝒴 = p𝒳) (hG : G ⋙ p𝒴 = p𝒵)
    (hrep : Stacks.RepresentableMorphism.IsRepresentableMorphism p𝒳 p𝒴 F) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism
      (TwoFibreProductOver.structureFunctor p𝒵 p𝒳 p𝒴 G F) p𝒵
      (TwoFibreProductOver.fst p𝒵 p𝒳 p𝒴 G F)
```

## Tag 02ZU, a lemma

[Tag 02ZU](https://stacks.math.columbia.edu/tag/02ZU) in the Stacks Project.

**`Stacks.RepresentableMorphism.isRepresentableMorphism_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Product.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableMorphism/Product.lean#L362).

> The product of two representable 1-morphisms of categories fibred in groupoids over a base
> category is representable.

```lean
public theorem isRepresentableMorphism_product
    (p₁ : 𝒳₁ ⥤ 𝒞) (p₂ : 𝒳₂ ⥤ 𝒞)
    (q₁ : 𝒴₁ ⥤ 𝒞) (q₂ : 𝒴₂ ⥤ 𝒞)
    (hp₁ : p₁.IsFiberedInGroupoids) (hp₂ : p₂.IsFiberedInGroupoids)
    (hq₁ : q₁.IsFiberedInGroupoids) (hq₂ : q₂.IsFiberedInGroupoids)
    (F₁ : 𝒳₁ ⥤ 𝒴₁) (F₂ : 𝒳₂ ⥤ 𝒴₂)
    (hF₁ : F₁ ⋙ q₁ = p₁) (hF₂ : F₂ ⋙ q₂ = p₂)
    (hrep₁ : Stacks.RepresentableMorphism.IsRepresentableMorphism p₁ q₁ F₁)
    (hrep₂ : Stacks.RepresentableMorphism.IsRepresentableMorphism p₂ q₂ F₂) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism
      (TwoFibreProductOver.structureFunctor p₁ p₂ (𝟭 𝒞) p₁ p₂)
      (TwoFibreProductOver.structureFunctor q₁ q₂ (𝟭 𝒞) q₁ q₂)
      (productMorphism p₁ p₂ q₁ q₂ F₁ F₂ hF₁ hF₂)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.6, Tag 04ST](https://stacks.math.columbia.edu/tag/04ST)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
