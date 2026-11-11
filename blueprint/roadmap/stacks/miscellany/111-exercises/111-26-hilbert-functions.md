---
declaration: section
origin: cited
lean: Polynomial.IsNumerical, GradedModule.IsLocallyFinite, GradedModule.EulerPoincareFunction, GradedModule.hilbertFunction, GradedModule.HasHilbertPolynomial, DirectSum.Decomposition
statement: formalized
proof: formalized
---

# 111.26 Hilbert functions

Section 111.26 of the Stacks Project, [Tag 027W](https://stacks.math.columbia.edu/tag/027W). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 027X, a definition

[Tag 027X](https://stacks.math.columbia.edu/tag/027X) in the Stacks Project.

**`Polynomial.IsNumerical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Polynomial/Numerical.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Polynomial/Numerical.lean#L58).

> A polynomial over `ℚ` is numerical if it takes an integer value at every integer.

```lean
public abbrev IsNumerical (f : Polynomial ℚ) : Prop
```

## Tag 027Y, a definition

[Tag 027Y](https://stacks.math.columbia.edu/tag/027Y) in the Stacks Project.

**`GradedModule.IsLocallyFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean#L60). The attribute's comment: “locally finite graded modules”.

> A graded module is locally finite when every homogeneous piece is finitely generated over
> the base ring.

```lean
abbrev IsLocallyFinite (piece : ℤ → Submodule A M) [DirectSum.Decomposition piece] : Prop
```

**`GradedModule.EulerPoincareFunction`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean#L72). The attribute's comment: “Euler-Poincare functions”.

> An Euler–Poincaré function assigns an integer to every finitely generated module and is
> additive in short exact sequences.

```lean
structure EulerPoincareFunction (A : Type u) [Ring A]
```

**`GradedModule.hilbertFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean#L88). The attribute's comment: “Hilbert functions”.

> The Hilbert function of a locally finite graded module with respect to an Euler–Poincaré
> function: its value at `n` is the value of the function on the degree-`n` piece.

```lean
def hilbertFunction (piece : ℤ → Submodule A M) [DirectSum.Decomposition piece]
    (hpiece : IsLocallyFinite piece) (φ : EulerPoincareFunction.{u, v} A) : ℤ → ℤ
```

**`GradedModule.HasHilbertPolynomial`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean#L101). The attribute's comment: “Hilbert polynomials”.

> A locally finite graded module has a Hilbert polynomial with respect to `φ` when its Hilbert
> function eventually agrees, on integer arguments, with a numerical polynomial.

```lean
abbrev HasHilbertPolynomial (piece : ℤ → Submodule A M) [DirectSum.Decomposition piece]
    (hpiece : IsLocallyFinite piece) (φ : EulerPoincareFunction.{u, v} A) : Prop
```

Declarations registered for the tag:

- [`DirectSum.Decomposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DirectSum.Decomposition#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedModule/HilbertFunction.lean#L53) (StacksFrontier): “graded modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.26, Tag 027W](https://stacks.math.columbia.edu/tag/027W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
