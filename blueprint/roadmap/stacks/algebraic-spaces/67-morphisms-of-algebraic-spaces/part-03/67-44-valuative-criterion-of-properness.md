---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isProper_tfae_of_isFiniteType_of_isQuasiSeparated, AlgebraicGeometry.Space.isProper_iff_valuativeCriterion_of_isFiniteType_of_isQuasiSeparated, AlgebraicGeometry.Space.isProper_iff_forall_unique_lift_of_isFiniteType_of_isQuasiSeparated
statement: formalized
proof: formalized
---

# 67.44 Valuative criterion of properness

Section 67.44 of the Stacks Project, [Tag 0CKZ](https://stacks.math.columbia.edu/tag/0CKZ). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A40, a lemma

[Tag 0A40](https://stacks.math.columbia.edu/tag/0A40) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_tfae_of_isFiniteType_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean#L54).

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` which is of finite type and
> quasi-separated, being proper, satisfying the valuative criterion of Stacks 03IX, and having
> exactly one dotted arrow in every valuative square over the given valuation ring are
> equivalent.

```lean
public theorem isProper_tfae_of_isFiniteType_of_isQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    List.TFAE
      [IsProper B S hS f,
        ValuativeCriterion f,
        ∀ q : ValuativeSquare f, Nonempty q.Lift ∧ Subsingleton q.Lift]
```

**`AlgebraicGeometry.Space.isProper_iff_valuativeCriterion_of_isFiniteType_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean#L72). The attribute's comment: “conditions (1) and (2)”.

> A morphism of algebraic spaces over `S` which is of finite type and quasi-separated is proper
> exactly when it satisfies the valuative criterion of Stacks 03IX.

```lean
public theorem isProper_iff_valuativeCriterion_of_isFiniteType_of_isQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔ ValuativeCriterion f
```

**`AlgebraicGeometry.Space.isProper_iff_forall_unique_lift_of_isFiniteType_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/Properness.lean#L82). The attribute's comment: “conditions (1) and (3)”.

> A morphism of algebraic spaces over `S` which is of finite type and quasi-separated is proper
> exactly when every valuative square for it has exactly one dotted arrow over the given valuation
> ring, which is the valuative criterion of Schemes, Stacks 01KD.

```lean
public theorem isProper_iff_forall_unique_lift_of_isFiniteType_of_isQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔ ∀ q : ValuativeSquare f, Nonempty q.Lift ∧ Subsingleton q.Lift
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.44, Tag 0CKZ](https://stacks.math.columbia.edu/tag/0CKZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
