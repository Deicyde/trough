---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.EquivariantQuasicoherentModule, AlgebraicGeometry.Space.equivariantQuasicoherentPullback
statement: formalized
proof: formalized
---

# 78.10 Equivariant quasi-coherent sheaves

Section 78.10 of the Stacks Project, [Tag 043S](https://stacks.math.columbia.edu/tag/043S). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 043T, a definition

[Tag 043T](https://stacks.math.columbia.edu/tag/043T) in the Stacks Project.

**`AlgebraicGeometry.Space.EquivariantQuasicoherentModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivariantQuasicoherentModules.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivariantQuasicoherentModules.lean#L133).

> A `G`-equivariant quasi-coherent `𝒪_X`-module for an action `A` of a group algebraic space
> `G` over `B` on an algebraic space `X` over `B`: a quasi-coherent `𝒪_X`-module `ℱ` together with
> a morphism `α : a^*ℱ ⟶ pr₁^*ℱ` of `𝒪_{G ×_B X}`-modules which satisfies the action cocycle
> condition and is normalized along the unit section.

```lean
structure EquivariantQuasicoherentModule (G : GroupAlgebraicSpace 𝒞 S hS B hB) (X : Over B)
    (hX : IsAlgebraicSpace 𝒞 S hS X.left) (A : ModObj G.obj.X X)
```

## Tag 043U, a lemma

[Tag 043U](https://stacks.math.columbia.edu/tag/043U) in the Stacks Project.

**`AlgebraicGeometry.Space.equivariantQuasicoherentPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivariantQuasicoherentPullback/Functor.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivariantQuasicoherentPullback/Functor.lean#L600). References: SGA 3 I (6.3.1), “special case”.

> **Stacks 043U.**  The inverse image along a `G`-equivariant morphism `f : X ⟶ Y` of
> algebraic spaces over `B` is a functor from the `G`-equivariant quasi-coherent `𝒪_Y`-modules to
> the `G`-equivariant quasi-coherent `𝒪_X`-modules: it sends `(ℱ, α)` to `f^*ℱ` with the
> reindexing of `α` along `1_G × f`.

```lean
def equivariantQuasicoherentPullback :
    EquivariantQuasicoherentModule (hB := hB) G Y hY AY ⥤
      EquivariantQuasicoherentModule (hB := hB) G X hX AX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.10, Tag 043S](https://stacks.math.columbia.edu/tag/043S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
