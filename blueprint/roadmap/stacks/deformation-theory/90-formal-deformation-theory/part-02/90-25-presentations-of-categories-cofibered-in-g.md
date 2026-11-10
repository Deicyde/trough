---
declaration: section
origin: cited
lean: Deformation.Presentation, Deformation.presentationGroupoid, Deformation.presentationMorphism, Deformation.presentationMorphism_full, Deformation.presentationMorphism_faithful, Deformation.presentationMorphism_isEquivalence_iff
statement: formalized
proof: formalized
---

# 90.25 Presentations of categories cofibered in groupoids

Section 90.25 of the Stacks Project, [Tag 06KW](https://stacks.math.columbia.edu/tag/06KW). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06KX, a definition

[Tag 06KX](https://stacks.math.columbia.edu/tag/06KX) in the Stacks Project.

**`Deformation.Presentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Presentation.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Presentation.lean#L44).

> An equivalence over `C` from the quotient of `G` to a category over `C`.
> When the latter is cofibered in groupoids, this is a presentation in the
> sense of Stacks Project, Tag 06KX.

```lean
public abbrev Presentation {C : Type u} [Category.{v} C] (G : GroupoidInFunctors.{u, v, w} C)
    {F : Type u₁} [Category.{v₁} F] (p : F ⥤ C)
```

## Tag 06KY, a lemma

[Tag 06KY](https://stacks.math.columbia.edu/tag/06KY) in the Stacks Project.

**`Deformation.presentationGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Groupoid.lean, line 1108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Groupoid.lean#L1108).

> A morphism from a set-valued functor to a category cofibered in groupoids canonically
> produces a groupoid in functors, whose arrows are the two-fibre product with source, target, and
> composition given by the second, first, and first-and-last projections respectively.

```lean
noncomputable def presentationGroupoid
    (hp : IsCofiberedInGroupoids p) : PresentationGroupoid p U f over
```

## Tag 06KZ, a lemma

[Tag 06KZ](https://stacks.math.columbia.edu/tag/06KZ) in the Stacks Project.

**`Deformation.presentationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean#L593). The attribute's comment: “natural morphism”.

> The canonical morphism from the quotient of a presentation to the category
> being presented, together with its compatibility with the projection and the
> original presentation functor.

```lean
noncomputable def presentationMorphism :
    {g : Grothendieck (evaluationFunctor P.toGroupoidInFunctors) ⥤ F //
      (g ⋙ p = Grothendieck.forget
        (evaluationFunctor P.toGroupoidInFunctors)) ∧
      ((uliftElementsEquivalence U).functor ⋙
        quotientMorphism P.toGroupoidInFunctors ⋙ g = f)}
```

**`Deformation.presentationMorphism_full`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean, line 609](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean#L609). The attribute's comment: “full”.

> The morphism from a presentation quotient is full.

```lean
theorem presentationMorphism_full
    (hp : IsCofiberedInGroupoids p) :
    (presentationMorphism p U f over P).1.Full
```

**`Deformation.presentationMorphism_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean#L616). The attribute's comment: “faithful”.

> The morphism from a presentation quotient is faithful.

```lean
theorem presentationMorphism_faithful :
    (presentationMorphism p U f over P).1.Faithful
```

**`Deformation.presentationMorphism_isEquivalence_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean, line 623](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/CofiberedPresentation/Morphism.lean#L623). The attribute's comment: “equivalence criterion”.

> The quotient morphism is an equivalence exactly when the original
> presentation functor is essentially surjective.

```lean
theorem presentationMorphism_isEquivalence_iff
    (hp : IsCofiberedInGroupoids p) :
    (presentationMorphism p U f over P).1.IsEquivalence ↔ f.EssSurj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.25, Tag 06KW](https://stacks.math.columbia.edu/tag/06KW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
