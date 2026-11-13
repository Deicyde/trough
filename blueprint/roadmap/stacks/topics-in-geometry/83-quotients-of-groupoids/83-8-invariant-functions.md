---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.invariantFunctionSheaf, AlgebraicGeometry.Space.HasInvariantFunctions
statement: formalized
proof: formalized
---

# 83.8 Invariant functions

Section 83.8 of the Stacks Project, [Tag 04A9](https://stacks.math.columbia.edu/tag/04A9). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04AA, a definition

[Tag 04AA](https://stacks.math.columbia.edu/tag/04AA) in the Stacks Project.

**`AlgebraicGeometry.Space.invariantFunctionSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantFunctions.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantFunctions.lean#L196). The attribute's comment: “part (1): the sheaf of invariant functions”.

> **Stacks 04AA**, part (1).  The *sheaf of `R`-invariant functions* `(φ_*O_U)^R` of an
> `R`-invariant morphism `φ : U ⟶ X`: the equalizer, on the small étale site of `X`, of the two
> maps `φ_*t^♯, φ_*s^♯ : φ_*O_U ⟶ φ'_*O_R` given by pulling functions back along the target and
> the source of the pre-relation.
>
> Its inclusion into `φ_*O_U` as an `O_X`-subalgebra is `CategoryTheory.Limits.equalizer.ι`,
> which is a monomorphism.

```lean
noncomputable def invariantFunctionSheaf {R U : Over B} {X : AlgebraicSpaces site S hS}
    (j : PreRelation R U) (φ : U.left ⟶ X) (hφ : IsInvariant j φ) :
    Sheaf (SmallEtale.topology site S hS X.1) CommRingCat.{u}
```

**`AlgebraicGeometry.Space.HasInvariantFunctions`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantFunctions.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/InvariantFunctions.lean#L213). The attribute's comment: “part (2): the functions on X are the invariant functions”.

> **Stacks 04AA**, part (2).  *The functions on `X` are the `R`-invariant functions on `U`*
> when the natural map `O_X ⟶ (φ_*O_U)^R` is an isomorphism.

```lean
noncomputable abbrev HasInvariantFunctions {R U : Over B} {X : AlgebraicSpaces site S hS}
    (j : PreRelation R U) (φ : U.left ⟶ X) (hφ : IsInvariant j φ) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.8, Tag 04A9](https://stacks.math.columbia.edu/tag/04A9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
