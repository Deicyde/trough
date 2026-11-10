---
declaration: section
origin: cited
lean: Stacks.Chow.cyclesOfDimension, Stacks.Chow.CycleGroup, AlgebraicGeometry.locallyFiniteDirectSum, Stacks.Chow.pointwiseCycleEquiv, Stacks.Chow.pointwiseCycleEquiv_apply, Stacks.Chow.cycleSupport, tsupport, Stacks.Chow.IsEffectiveCycle
statement: formalized
proof: formalized
---

# 42.8 Cycles

Section 42.8 of the Stacks Project, [Tag 02QQ](https://stacks.math.columbia.edu/tag/02QQ). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02QR, a definition

[Tag 02QR](https://stacks.math.columbia.edu/tag/02QR) in the Stacks Project.

**`Stacks.Chow.cyclesOfDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L156). The attribute's comment: “k-cycles”.

> The subgroup `Z_k(X)` of cycles whose nonzero coefficients occur only at
> integral closed subschemes of delta-dimension `k`.

```lean
def cyclesOfDimension (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) : AddSubgroup (AlgebraicCycle X ℤ)
```

**`Stacks.Chow.CycleGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L180). The attribute's comment: “the abelian group of k-cycles”.

> The abelian group `Z_k(X)` of cycles of delta-dimension `k`.

```lean
abbrev CycleGroup (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) : Type u
```

## Tag 0GU2, a remark

[Tag 0GU2](https://stacks.math.columbia.edu/tag/0GU2) in the Stacks Project.

**`AlgebraicGeometry.locallyFiniteDirectSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Cycles/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Cycles/Basic.lean#L40). The attribute's comment: “locally_finite_direct_sum”.

> The subgroup of pointwise families whose support meets every quasi-compact open subset of
> the scheme in a finite set.

```lean
def locallyFiniteDirectSum (X : Scheme.{u}) (T : Set X) (G : T → Type v)
    [∀ x, AddCommGroup (G x)] : AddSubgroup (∀ x, G x)
```

**`Stacks.Chow.pointwiseCycleEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseCycles.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseCycles.lean#L183). The attribute's comment: “the pointwise description of cycles”.

> **Stacks 0GU2.** The group of `k`-cycles is the locally finite direct sum of the degree-zero
> Milnor K-groups of the residue fields at the points of relative dimension `k`.

```lean
def pointwiseCycleEquiv (k : ℤ) : CycleGroup C p k ≃+ PointwiseCycleGroup C p k
```

**`Stacks.Chow.pointwiseCycleEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseCycles.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseCycles.lean#L206). The attribute's comment: “the coordinate identification with integer coefficients”.

> **Stacks 0GU2.** Under the pointwise description of cycles, the degree-zero Milnor K-class at
> a point of relative dimension `k` is the coefficient of the cycle there.

```lean
theorem pointwiseCycleEquiv_apply (k : ℤ) (c : CycleGroup C p k)
    (x : pointsOfDimension C p k) :
    milnorKTheoryZeroAddEquiv (X.residueField x.1) ((pointwiseCycleEquiv C p k c).1 x) =
      c.1 x.1
```

## Tag 0H46, a definition

[Tag 0H46](https://stacks.math.columbia.edu/tag/0H46) in the Stacks Project.

**`Stacks.Chow.cycleSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/SupportOfCycle.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/SupportOfCycle.lean#L82). The attribute's comment: “support of a cycle”. References: EGA IV (21.6.1).

> **Stacks 0H46.** The support of a cycle `α = ∑ n_Z [Z]` on `X`, namely the union
> `Supp(α) = ⋃_{n_Z ≠ 0} Z` of the integral closed subschemes occurring in `α` with a nonzero
> coefficient.
>
> An integral closed subscheme of `X` is given by its underlying irreducible closed subset
> `Z : IrreducibleCloseds X`, and a cycle is a locally finitely supported function on the points
> of `X` which records the coefficient of `Z` at the generic point of `Z`, so that
> `n_Z = α Z.isIrreducible.genericPoint`.

```lean
def cycleSupport (α : AlgebraicCycle X ℤ) : Set X
```

Declarations registered for the tag:

- [`tsupport`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=tsupport#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/Setup/CycleSupport.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/CycleSupport.lean#L44) (StacksFrontier).

## Tag 0H47, a definition

[Tag 0H47](https://stacks.math.columbia.edu/tag/0H47) in the Stacks Project.

**`Stacks.Chow.IsEffectiveCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L87). References: EGA IV (21.6.1); EGA IV (21.6.2), “(X)”.

> **Stacks Project, Tag 0H47.** A cycle is *effective* when it can be written as a sum
> `∑ n_Z [Z]` of integral closed subschemes with all `n_Z ≥ 0`, that is, when every coefficient
> of the cycle is nonnegative.

```lean
def IsEffectiveCycle {X : Scheme.{u}} (c : AlgebraicCycle X ℤ) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.8, Tag 02QQ](https://stacks.math.columbia.edu/tag/02QQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
