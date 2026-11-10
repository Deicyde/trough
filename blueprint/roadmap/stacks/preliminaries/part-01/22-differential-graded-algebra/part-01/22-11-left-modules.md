---
declaration: section
origin: cited
lean: DifferentialGradedAlgebra.opposite, DifferentialGraded.leftRightEquivalence, ExternallyGradedRightModule.shift, ExternallyGradedLeftModule.shift
statement: formalized
proof: formalized
---

# 22.11 Left modules

Section 22.11 of the Stacks Project, [Tag 0FPZ](https://stacks.math.columbia.edu/tag/0FPZ). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09JG, a definition

[Tag 09JG](https://stacks.math.columbia.edu/tag/09JG) in the Stacks Project.

**`DifferentialGradedAlgebra.opposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Opposite.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Opposite.lean#L231).

> The opposite differential graded algebra. Its underlying graded module and differential are
> canonically identified with those of `A`, and its multiplication on homogeneous elements is
> `a ⋅ᵒᵖᵖ b = (-1)^(deg a * deg b) • (b * a)`.

```lean
public noncomputable def opposite : Opposite R A
```

## Tag 0FQ0, a lemma

[Tag 0FQ0](https://stacks.math.columbia.edu/tag/0FQ0) in the Stacks Project.

**`DifferentialGraded.leftRightEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/LeftModule.lean, line 855](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/LeftModule.lean#L855).

> Graded opposition is an equivalence from left differential graded `A`-modules to
> right differential graded modules over the graded opposite algebra.

```lean
public noncomputable def leftRightEquivalence (R : Type u) [CommRing R]
    (A : DifferentialGradedAlgebra.{u, v} R) : OppositeEquivalence R A
```

## Tag 0FQ1, a definition

[Tag 0FQ1](https://stacks.math.columbia.edu/tag/0FQ1) in the Stacks Project.

**`ExternallyGradedRightModule.shift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/GradedModule/ExternalShift.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/GradedModule/ExternalShift.lean#L161). The attribute's comment: “right graded modules”.

> The shift `M[k]` of a graded right module, with `M[k]ⁿ = Mⁿ⁺ᵏ`.

```lean
def shift {A : ExternallyGradedAlgebra R} (M : ExternallyGradedRightModule A) (k : ℤ) :
    ExternallyGradedRightModule A
```

**`ExternallyGradedLeftModule.shift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/GradedModule/ExternalShift.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/GradedModule/ExternalShift.lean#L190). The attribute's comment: “left graded modules”.

> The shift `M[k]` of a graded left module.  A homogeneous element of degree `i`
> acts with the Koszul factor `(-1)^(i*k)`.

```lean
def shift {A : ExternallyGradedAlgebra R} (M : ExternallyGradedLeftModule A) (k : ℤ) :
    ExternallyGradedLeftModule A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.11, Tag 0FPZ](https://stacks.math.columbia.edu/tag/0FPZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
