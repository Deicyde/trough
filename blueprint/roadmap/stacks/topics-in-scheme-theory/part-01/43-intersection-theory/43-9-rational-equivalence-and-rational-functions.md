---
declaration: section
origin: cited
lean: Stacks.Chow.rationalEquivalences_eq_rationalEquivalencesByFibres, Stacks.Chow.principalDivisorPushforward_mem_rationalEquivalencesByFibres
statement: formalized
proof: formalized
---

# 43.9 Rational equivalence and rational functions

Section 43.9 of the Stacks Project, [Tag 0AZH](https://stacks.math.columbia.edu/tag/0AZH). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AZI, a lemma

[Tag 0AZI](https://stacks.math.columbia.edu/tag/0AZI) in the Stacks Project.

**`Stacks.Chow.rationalEquivalences_eq_rationalEquivalencesByFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/GeometricRationalEquivalence.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/GeometricRationalEquivalence.lean#L160). The attribute's comment: “principal divisors generate the cycles rationally equivalent to zero”.

> **Stacks Project, Tag 0AZI.** On a variety over an algebraically closed field the
> principal divisors of nonzero rational functions on the `(k + 1)`-dimensional integral closed
> subschemes generate exactly the group of `k`-cycles rationally equivalent to zero in the
> geometric sense: the rational equivalence of Chow homology agrees with the geometric one.

```lean
theorem rationalEquivalences_eq_rationalEquivalencesByFibres (K : Type u) [Field K]
    [IsAlgClosed K] (C : ChowSituation.{u})
    (hC : C.S = AlgebraicGeometry.Spec (CommRingCat.of K)) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p]
    [AlgebraicGeometry.IsVariety K (p ≫ eqToHom hC)] (k : ℤ) :
    rationalEquivalences C p k = rationalEquivalencesByFibres C p k
```

**`Stacks.Chow.principalDivisorPushforward_mem_rationalEquivalencesByFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/GeometricRationalEquivalence.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/GeometricRationalEquivalence.lean#L203). The attribute's comment: “principal divisors are rationally equivalent to zero”.

> **Stacks Project, Tag 0AZI.** On a variety over an algebraically closed field the
> principal divisor of a nonzero rational function on an integral closed subscheme of
> delta-dimension `k + 1`, pushed forward to a `k`-cycle on the variety, is rationally
> equivalent to zero in the geometric sense.

```lean
theorem principalDivisorPushforward_mem_rationalEquivalencesByFibres (K : Type u) [Field K]
    [IsAlgClosed K] (C : ChowSituation.{u})
    (hC : C.S = AlgebraicGeometry.Spec (CommRingCat.of K)) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p]
    [AlgebraicGeometry.IsVariety K (p ≫ eqToHom hC)] (k : ℤ) (V : X.IdealSheafData)
    (hV : IsIntegral V.subscheme)
    (hDim : schemeDeltaDimension C (V.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (f : (rationalFunctions V.subscheme)ˣ) :
    (⟨principalDivisorPushforward C p V hV f,
        principalDivisorPushforward_mem_cyclesOfDimension C p k V hV hDim f⟩ :
      CycleGroup C p k) ∈ rationalEquivalencesByFibres C p k
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.9, Tag 0AZH](https://stacks.math.columbia.edu/tag/0AZH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
