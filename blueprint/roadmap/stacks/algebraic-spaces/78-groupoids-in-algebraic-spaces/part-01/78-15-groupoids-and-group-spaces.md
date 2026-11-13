---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.actionGroupoid, AlgebraicGeometry.Space.groupoidOfAction, AlgebraicGeometry.Space.actionGroupoidModulesComparison, AlgebraicGeometry.Space.actionGroupoidModulesEquivalence
statement: formalized
proof: formalized
---

# 78.15 Groupoids and group spaces

Section 78.15 of the Stacks Project, [Tag 0443](https://stacks.math.columbia.edu/tag/0443). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0444, a lemma

[Tag 0444](https://stacks.math.columbia.edu/tag/0444) in the Stacks Project.

**`AlgebraicGeometry.Space.actionGroupoid`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean#L87). The attribute's comment: “the action groupoid itself”.

> The action groupoid `(X, G ×_B X, pr₁, a, m)` of an action `A` of a group algebraic space `G`
> over `B` on an algebraic space `X` over `B`, with the projection as its source and the action
> morphism as its target.
>
> At the trivial action of `G` on the base this groupoid has arrow space `G ×_B B`, not `G`; the
> groupoid `(Spec k, G, p, p, m)` of Stacks 06DZ, with arrow space `G` itself, is
> `AlgebraicGeometry.Space.groupoidOfGroupOverField`.

```lean
noncomputable abbrev actionGroupoid (G : GroupAlgebraicSpace 𝒞 S hS B hB) (X : Over B)
    (hX : IsAlgebraicSpace 𝒞 S hS X.left) (A : ModObj G.obj.X X) :
    GroupoidInAlgebraicSpaces 𝒞 S hS ⟨B, hB⟩
```

**`AlgebraicGeometry.Space.groupoidOfAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ActionGroupoid.lean, line 1351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ActionGroupoid.lean#L1351).

> A group action gives the action groupoid,
> with the stated object and arrow spaces and all five structure maps.

```lean
noncomputable def groupoidOfAction :
    ActionGroupoidConstruction B G X hG hX
```

## Tag 0445, a lemma

[Tag 0445](https://stacks.math.columbia.edu/tag/0445) in the Stacks Project.

**`AlgebraicGeometry.Space.actionGroupoidModulesComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean#L354).

> The rule `(ℱ, α) ↦ (ℱ, α)` is a fully faithful and essentially surjective functor from the
> `G`-equivariant quasi-coherent `𝒪_X`-modules of Stacks 043T to the quasi-coherent modules of
> Stacks 0441 on the action groupoid of Stacks 0444, leaving the underlying quasi-coherent module,
> the transition morphism and the morphisms unchanged.

```lean
noncomputable def actionGroupoidModulesComparison (G : GroupAlgebraicSpace 𝒞 S hS B hB)
    (X : Over B) (hX : IsAlgebraicSpace 𝒞 S hS X.left) (A : ModObj G.obj.X X) :
    ActionGroupoidModulesComparison (hB := hB) G X hX A (actionGroupoid G X hX A)
```

**`AlgebraicGeometry.Space.actionGroupoidModulesEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionGroupoidModules.lean#L365). The attribute's comment: “the equivalence of categories”.

> The rule `(ℱ, α) ↦ (ℱ, α)` is an equivalence between the category of `G`-equivariant
> quasi-coherent `𝒪_X`-modules of Stacks 043T and the category of quasi-coherent modules of
> Stacks 0441 on the action groupoid of Stacks 0444.

```lean
noncomputable def actionGroupoidModulesEquivalence (G : GroupAlgebraicSpace 𝒞 S hS B hB)
    (X : Over B) (hX : IsAlgebraicSpace 𝒞 S hS X.left) (A : ModObj G.obj.X X) :
    EquivariantQuasicoherentModule (hB := hB) G X hX A ≌
      QuasicoherentModule 𝒞 S hS (actionGroupoid G X hX A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.15, Tag 0443](https://stacks.math.columbia.edu/tag/0443)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
