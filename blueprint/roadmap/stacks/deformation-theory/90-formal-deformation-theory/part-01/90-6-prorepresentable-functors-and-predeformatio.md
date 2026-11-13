---
declaration: section
origin: cited
lean: Deformation.IsProrepresentable, Deformation.IsPredeformationCategory, BasedFunctor, Deformation.isPredeformationFunctor_isomorphismClasses, Deformation.IsPredeformationFunctor, Deformation.isPredeformationCategory_iff, Deformation.objectsOverFunctor, Deformation.isPredeformationCategory_objectsOverFunctor
statement: formalized
proof: formalized
---

# 90.6 Prorepresentable functors and predeformation categories

Section 90.6 of the Stacks Project, [Tag 06GI](https://stacks.math.columbia.edu/tag/06GI). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06GX, a definition

[Tag 06GX](https://stacks.math.columbia.edu/tag/06GX) in the Stacks Project.

**`Deformation.IsProrepresentable`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 717](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L717).

> A functor on Artinian local `Λ`-algebras is prorepresentable if it is
> naturally isomorphic to the restriction of the covariant representable functor
> of some Noetherian complete local `Λ`-algebra.

```lean
abbrev IsProrepresentable {Λ : Type u} {k : Type w} [CommRing Λ] [Field k]
    [Algebra Λ k] (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type v) : Prop
```

## Tag 06GS, a definition

[Tag 06GS](https://stacks.math.columbia.edu/tag/06GS) in the Stacks Project.

**`Deformation.IsPredeformationCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L139). The attribute's comment: “objects”.

> A functor to `𝒞_Λ` presents a predeformation category when it is cofibered in
> groupoids and its fibre over the residue field `k` is equivalent to the category with one
> object and one morphism.

```lean
structure IsPredeformationCategory {Λ : Type u} {k : Type w} [CommRing Λ]
  [Field k] [Algebra Λ k] {F : Type u₁} [Category.{v₁} F] (p : F ⥤ ArtinianLocalAlgCat.{u, max v w,
    w} Λ k) : Prop
```

Declarations registered for the tag:

- [`BasedFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BasedFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L147) (StacksFrontier): “morphisms”.

## Tag 06GT, a remark

[Tag 06GT](https://stacks.math.columbia.edu/tag/06GT) in the Stacks Project.

**`Deformation.isPredeformationFunctor_isomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Associated.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Associated.lean#L37).

> The associated functor of isomorphism classes of a predeformation category is a
> predeformation functor.

```lean
public theorem isPredeformationFunctor_isomorphismClasses
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{v₁, u₁}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (h𝓕 : IsPredeformationCategory 𝓕.p) :
    IsPredeformationFunctor
      (isomorphismClasses 𝓕 h𝓕.cofibered)
```

**`Deformation.IsPredeformationFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L611). The attribute's comment: “predeformation\_functor”.

> A set-valued functor on `𝒞_Λ` is a predeformation functor when its value at
> the residue field `k` is a one-element set.

```lean
public abbrev IsPredeformationFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t) : Prop
```

**`Deformation.isPredeformationCategory_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L619). The attribute's comment: “predeformation\_functor”.

> A functor is a predeformation functor exactly when its associated cofibered
> set, the category of elements, is a predeformation category.

```lean
public theorem isPredeformationCategory_iff
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t) :
    IsPredeformationCategory (Functor.Elements.π F) ↔
      IsPredeformationFunctor F
```

## Tag 06GU, a remark

[Tag 06GU](https://stacks.math.columbia.edu/tag/06GU) in the Stacks Project.

**`Deformation.objectsOverFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L251). The attribute's comment: “category\_of\_objects\_over\_x”.

> The structure functor on the category of arrows in `F` with target `x`, obtained by
> forgetting the arrow to `x` and then applying `p`.

```lean
def objectsOverFunctor (p : F ⥤ C)
  (x : F) : Over x ⥤ C
```

**`Deformation.isPredeformationCategory_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L403).

> Localizing a category cofibered in groupoids at an object of its special
> fibre gives a predeformation category.

```lean
public theorem isPredeformationCategory_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    IsPredeformationCategory
      (objectsOverFunctor p x.1)
```

Declarations registered for the tag:

- [`CategoryTheory.Over`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Predeformation/Basic.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/Basic.lean#L229) (StacksFrontier): “category\_of\_objects\_over\_x”. References: EGA I (10.4.7); EGA I (2.5.1); EGA I (3.3.1); EGA IV (14.5.8); SGA 1 V (6.13); SGA 1 VIII (5.2), “fiber over S”; SGA 3 I (1.3); SGA 3 VIIA (4.0), “more general”; SGA 3 VIII (1.0.3); SGA 4 III (5.1), “special case”; SGA 4 IV (5.1); SGA 4 IV (7.1.8), “more general”; SGA 4 VI (4.1), “partial”; SGA 4½ Arcata (1.6.4), “partial”; SGA 7 VI (3.1(a)), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.6, Tag 06GI](https://stacks.math.columbia.edu/tag/06GI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
