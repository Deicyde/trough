---
declaration: section
origin: cited
lean: main_theorem008Q
statement: formalized
proof: formalized
---

# 6.23 Continuous maps and sheaves of algebraic structures

Section 6.23 of the Stacks Project, [Tag 008P](https://stacks.math.columbia.edu/tag/008P). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 008Q, a lemma

[Tag 008Q](https://stacks.math.columbia.edu/tag/008Q) in the Stacks Project.

**`main_theorem008Q`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/AlgebraicStructure.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Functors/FMap/AlgebraicStructure.lean#L105).

> **Stacks 008Q.** Given an f-map `φ` of underlying sheaves of sets whose components all lift
> along `U`, there exists a unique f-map of sheaves of algebraic structures with underlying
> f-map `φ`.

```lean
theorem main_theorem008Q
    {C : Type u} [Category.{w} C]
    (U : C ⥤ Type w) [U.Faithful] [U.ReflectsIsomorphisms]
    [HasLimits C] [PreservesLimits U]
    {X Y : TopCat} (f : X ⟶ Y)
    (F : TopCat.Sheaf C X) (G : TopCat.Sheaf C Y)
    (φ : underlyingSheaf U G ⟶
          (TopCat.Sheaf.pushforward (Type w) f).obj (underlyingSheaf U F))
    (hφ : ∀ (V : (Opens Y)ᵒᵖ),
            ∃ ψV : G.obj.obj V ⟶ F.obj.obj ((Opens.map f).op.obj V),
              U.map ψV = φ.hom.app V) :
    ∃! ψ : G ⟶ (TopCat.Sheaf.pushforward C f).obj F,
      underlyingSheafMap U ψ = φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.23, Tag 008P](https://stacks.math.columbia.edu/tag/008P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
