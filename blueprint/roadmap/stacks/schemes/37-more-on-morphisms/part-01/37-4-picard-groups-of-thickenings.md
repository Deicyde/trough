---
declaration: section
origin: cited
lean: Stacks.Thickenings.thickeningShortComplex_shortExact, Stacks.Thickenings.injective_idealToUnitsCohomology_zero, Stacks.Thickenings.exact_idealToUnitsCohomology, Stacks.Thickenings.exact_unitsToSubCohomology, Stacks.Thickenings.exact_thickeningBoundary, Stacks.Thickenings.exact_picardOfIdeal, Stacks.Thickenings.exact_picardRestriction, Stacks.Thickenings.unitsKernelShortComplex_shortExact
statement: formalized
proof: formalized
---

# 37.4 Picard groups of thickenings

Section 37.4 of the Stacks Project, [Tag 0C6Q](https://stacks.math.columbia.edu/tag/0C6Q). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C6R, a lemma

[Tag 0C6R](https://stacks.math.columbia.edu/tag/0C6R) in the Stacks Project.

**`Stacks.Thickenings.thickeningShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 823](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L823). The attribute's comment: “the short exact sequence of sheaves”.

> The sequence of sheaves `0 ⟶ ℐ ⟶ 𝒪_{X'}^* ⟶ i_* 𝒪_X^* ⟶ 0` of a first-order thickening is
> short exact.

```lean
theorem thickeningShortComplex_shortExact (i : X ⟶ X') (hi : IsFirstOrderThickening i) :
    (thickeningShortComplex i hi).ShortExact
```

**`Stacks.Thickenings.injective_idealToUnitsCohomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L916). The attribute's comment: “injectivity at the global sections of the ideal”.

> The sequence starts with an injection: a global section of the ideal sheaf giving the unit
> `1` is zero.

```lean
theorem injective_idealToUnitsCohomology_zero (i : X ⟶ X')
    (hi : IsFirstOrderThickening i) :
    Function.Injective (idealToUnitsCohomology i hi 0)
```

**`Stacks.Thickenings.exact_idealToUnitsCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 923](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L923). The attribute's comment: “exactness at the cohomology of the units of the thickening”.

> Exactness at `H^n(X', 𝒪_{X'}^*)`.

```lean
theorem exact_idealToUnitsCohomology (i : X ⟶ X') (hi : IsFirstOrderThickening i)
    (n : ℕ) :
    Function.Exact (idealToUnitsCohomology i hi n) (unitsToSubCohomology i n)
```

**`Stacks.Thickenings.exact_unitsToSubCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 930](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L930). The attribute's comment: “exactness at the cohomology of the units of the closed subscheme”.

> Exactness at `H^n(X, 𝒪_X^*)`.

```lean
theorem exact_unitsToSubCohomology (i : X ⟶ X') (hi : IsFirstOrderThickening i)
    (n : ℕ) :
    Function.Exact (unitsToSubCohomology i n) (thickeningBoundary i hi n)
```

**`Stacks.Thickenings.exact_thickeningBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 937](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L937). The attribute's comment: “exactness at the cohomology of the ideal”.

> Exactness at `H^{n+1}(X, ℐ)`.

```lean
theorem exact_thickeningBoundary (i : X ⟶ X') (hi : IsFirstOrderThickening i) (n : ℕ) :
    Function.Exact (thickeningBoundary i hi n) (idealToUnitsCohomology i hi (n + 1))
```

**`Stacks.Thickenings.exact_picardOfIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 943](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L943). The attribute's comment: “exactness at the Picard group of the thickening”.

> Exactness at `Pic(X')`.

```lean
theorem exact_picardOfIdeal (i : X ⟶ X') (hi : IsFirstOrderThickening i) :
    Function.Exact (picardOfIdeal i hi) (picardRestriction i hi)
```

**`Stacks.Thickenings.exact_picardRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean, line 952](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardSequence.lean#L952). The attribute's comment: “exactness at the Picard group of the closed subscheme”.

> Exactness at `Pic(X)`.

```lean
theorem exact_picardRestriction (i : X ⟶ X') (hi : IsFirstOrderThickening i) :
    Function.Exact (picardRestriction i hi) (picardBoundary i hi)
```

**`Stacks.Thickenings.unitsKernelShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardTorsionGeneral.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardTorsionGeneral.lean#L435). The attribute's comment: “the short exact sequence of sheaves, for an arbitrary thickening, with the sheaf of units congruent to one presented as a kernel”.

> **Stacks Project, Tag 0C6R** for an arbitrary thickening: the sequence of sheaves
> `0 ⟶ 𝒦 ⟶ 𝒪_{X'}^* ⟶ i_* 𝒪_X^* ⟶ 0` is short exact, where `𝒦` is the kernel of restriction of
> units, i.e. the sheaf of units congruent to `1` modulo the ideal of `X`.

```lean
theorem unitsKernelShortComplex_shortExact (i : X ⟶ X') (hi : IsThickening i) :
    (unitsKernelShortComplex i).ShortExact
```

## Tag 0C6S, a lemma

[Tag 0C6S](https://stacks.math.columbia.edu/tag/0C6S) in the Stacks Project.

**`Stacks.Thickenings.bijOn_schemePullbackClass_zsmulTorsion_of_globalUnitsPowerLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/PicardTorsionGeneral.lean, line 845](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/PicardTorsionGeneral.lean#L845).

> **Stacks Project, Tag 0C6S** in its corrected form (an erratum to the printed statement).
> For a thickening `i : X ⟶ X'` and an integer `n` invertible in `𝒪_X`, assuming every invertible
> global function on `X` is an `n`-th power times the restriction of an invertible global function
> on `X'`, restriction of invertible modules is a bijection `Pic(X')[n] → Pic(X)[n]`.
>
> The original statement omitted that assumption and is refuted by
> `Stacks.Examples.TwistedDoubledLine.not_forall_bijOn_schemePullbackClass_zsmulTorsion`; the
> assumption is not merely sufficient but necessary, by
> `Stacks.Thickenings.bijOn_schemePullbackClass_zsmulTorsion_iff`.

```lean
theorem bijOn_schemePullbackClass_zsmulTorsion_of_globalUnitsPowerLift (i : X ⟶ X')
    (hi : IsThickening i) {n : ℤ} (hn : IsUnit ((n : ℤ) : Γ(X, ⊤)))
    (hpow : GlobalUnitsPowerLift i n) :
    Set.BijOn (schemePullbackClass i) (zsmulTorsion (ofScheme X') n)
      (zsmulTorsion (ofScheme X) n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.4, Tag 0C6Q](https://stacks.math.columbia.edu/tag/0C6Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
