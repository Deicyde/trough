---
declaration: section
origin: cited
lean: TwoMorphismOfTopoi.hcomp, TwoMorphismOfTopoi
statement: formalized
proof: formalized
---

# 7.36 2-morphisms of topoi

Section 7.36 of the Stacks Project, [Tag 04I9](https://stacks.math.columbia.edu/tag/04I9). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04I9, the section

[Tag 04I9](https://stacks.math.columbia.edu/tag/04I9) in the Stacks Project.

**`TwoMorphismOfTopoi.hcomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/TwoMorphismOfTopoi.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/TwoMorphismOfTopoi.lean#L183). The attribute's comment: “horizontal composition s ⋆ t of 2-morphisms of topoi, and its two descriptions”.

> Horizontal composition `s ⋆ t` of 2-morphisms of topoi: a 2-morphism from `f' ∘ f` to
> `g' ∘ g`, given on `ℱ` by either of the two composites `f'_*f_*ℱ ⟶ g'_*g_*ℱ`.

```lean
def hcomp (s : TwoMorphismOfTopoi f' g') (t : TwoMorphismOfTopoi f g) :
    TwoMorphismOfTopoi (f'.comp f) (g'.comp g)
```

## Tag 04IA, a definition

[Tag 04IA](https://stacks.math.columbia.edu/tag/04IA) in the Stacks Project.

**`TwoMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/TwoMorphismOfTopoi.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/TwoMorphismOfTopoi.lean#L57). The attribute's comment: “a 2-morphism f ⇒ g of morphisms of topoi is a transformation f\_* ⟶ g\_*”. References: SGA 4 IV (3.2); SGA 4 IV (3.3.2), “2-arrows”.

> A *2-morphism* from a morphism of topoi `f : E → F` to a morphism of topoi `g : E → F` is a
> transformation of functors `t : f_* ⟶ g_*`.

```lean
def TwoMorphismOfTopoi {E : Type u} [Category.{v} E] {F : Type u'} [Category.{v'} F]
    (f g : MorphismOfTopoi E F) : Type _
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.36, Tag 04I9](https://stacks.math.columbia.edu/tag/04I9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
