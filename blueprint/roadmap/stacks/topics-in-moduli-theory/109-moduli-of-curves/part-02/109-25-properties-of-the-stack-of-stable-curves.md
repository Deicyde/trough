---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSeparated_moduliStableCurvesOfGenus_unconditional, AlgebraicGeometry.compactSpace_points_moduliStableCurvesOfGenusSmall, AlgebraicGeometry.moduliStableCurves_isDeligneMumford_proper_smooth
statement: formalized
proof: formalized
---

# 109.25 Properties of the stack of stable curves

Section 109.25 of the Stacks Project, [Tag 0E99](https://stacks.math.columbia.edu/tag/0E99). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E9A, a lemma

[Tag 0E9A](https://stacks.math.columbia.edu/tag/0E9A) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_moduliStableCurvesOfGenus_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesUnconditional.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesUnconditional.lean#L73). The attribute's comment: “g ≥ 2 (hg); 𝓜̄_g → Spec(ℤ) is separated, which is what the source says the statement means; nothing is assumed”.

> Let `g ≥ 2`. The stack `𝓜̄_g` is separated: the morphism `𝓜̄_g → Spec(ℤ)` (the inclusion of
> the open substack of stable families of genus `g` into the small model of the algebraic stack
> `Curves`, followed by its structure morphism) is separated.

```lean
theorem isSeparated_moduliStableCurvesOfGenus_unconditional (g : ℕ) (hg : 2 ≤ g) :
    Stack.AlgebraicStacks.IsSeparated B integerBase hZ
      ((curvesSmallOpenSubstack B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, u + 1} B hZ)
          (isOpenCurvesLocus_isStableCurveFamilyOfGenus_unconditional B hZ g)).inclusion ≫
        Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, u + 1} B hZ)))
```

## Tag 0E9B, a lemma

[Tag 0E9B](https://stacks.math.columbia.edu/tag/0E9B) in the Stacks Project.

**`AlgebraicGeometry.compactSpace_points_moduliStableCurvesOfGenusSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOfGenusQuasiCompact.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesOfGenusQuasiCompact.lean#L126).

> Let `g ≥ 2`. The moduli stack `𝓜̄_g` of stable curves of genus `g` is
> quasi-compact: the space of points of its small model
> `AlgebraicGeometry.moduliStableCurvesOfGenusSmall` (Stacks 04XG), with the topology of
> Stacks 04XL, is compact. This is quasi-compactness of an algebraic stack in the sense of
> Stacks 04YB (`AlgebraicGeometry.Stack.IsQuasiCompactStack`, which is this `CompactSpace`).

```lean
theorem compactSpace_points_moduliStableCurvesOfGenusSmall (g : ℕ) (hg : 2 ≤ g) :
    @CompactSpace (Stack.points B integerBase hZ (moduliStableCurvesOfGenusSmall B hZ g).val
      (moduliStableCurvesOfGenusSmall B hZ g).property)
      (Stack.pointTopology B integerBase hZ (moduliStableCurvesOfGenusSmall B hZ g))
```

## Tag 0E9C, a theorem

[Tag 0E9C](https://stacks.math.columbia.edu/tag/0E9C) in the Stacks Project.

**`AlgebraicGeometry.moduliStableCurves_isDeligneMumford_proper_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesProperSmoothReduced.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliStableCurvesProperSmoothReduced.lean#L335). The attribute's comment: “g ≥ 2 (hg); 𝓜̄_g is Deligne–Mumford, proper and smooth over Spec(ℤ), and 𝓜_g is an open substack of 𝓜̄_g whose points are dense in |𝓜̄_g|; nothing is assumed”.

> Let `g ≥ 2`. The algebraic stack `𝓜̄_g` is a Deligne–Mumford stack, proper and smooth over
> `Spec(ℤ)`. Moreover, the locus `𝓜_g` parametrizing smooth curves is a dense open substack.
>
> Here `𝓜̄_g` is the open substack of the algebraic stack of curves (Stacks 0D5A) cut out by the
> stable families of genus `g` (Stacks 0E78), and `𝓜_g` the one cut out by the families smooth of
> relative dimension one with `f_*𝒪_X = 𝒪_S` universally and of genus `g` (Stacks 0E83); the
> conjuncts are: `𝓜̄_g` is Deligne–Mumford, `𝓜̄_g → Spec(ℤ)` is proper, it is smooth, and `𝓜_g`
> is contained in `𝓜̄_g` (so it is an open substack of `𝓜̄_g`) with points dense in `|𝓜̄_g|`.

```lean
theorem moduliStableCurves_isDeligneMumford_proper_smooth (g : ℕ) (hg : 2 ≤ g) :
    Stack.IsDeligneMumfordStack.{u, u + 1} B integerBase hZ
        (curvesSmallOpenSubstack B hZ
          (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
          (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
            (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ)
            g)).toAlgebraicStack.val.val ∧
      Stack.AlgebraicStacks.IsProper B integerBase hZ
        ((curvesSmallOpenSubstack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
            (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
              (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) g)).inclusion ≫
          Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ))) ∧
      IsSmoothOverIntegers B hZ
        (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
        (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
          (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) g) ∧
      ∃ hle : (curvesSmallOpenSubstack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
            (isOpenCurvesLocus_isSmoothH0FamilyOfGenus_of_isStable B hZ
              (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) hg)).property ≤
          (curvesSmallOpenSubstack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
            (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
              (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) g)).property,
        @Dense _ (Stack.pointTopology B integerBase hZ
            (curvesSmallOpenSubstack B hZ
              (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
              (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
                (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ)
                g)).toAlgebraicStack.val)
          (Set.range (Stack.AlgebraicStacks.pointsMap B integerBase hZ
            (Stack.OpenSubstack.homOfLE B integerBase hZ
              (curvesSmallOpenSubstack B hZ
                (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
                (isOpenCurvesLocus_isSmoothH0FamilyOfGenus_of_isStable B hZ
                  (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) hg))
              (curvesSmallOpenSubstack B hZ
                (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, u + 1} B hZ)
                (isOpenCurvesLocus_isStableCurveFamilyOfGenus_of_isStable B hZ
                  (C1590Private.isOpenCurvesLocus_isStableCurveFamily B hZ) g))
                hle)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.25, Tag 0E99](https://stacks.math.columbia.edu/tag/0E99)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
