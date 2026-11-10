---
declaration: section
origin: cited
lean: AlgebraicGeometry.polarizedCurvesSquareUnconditional, AlgebraicGeometry.polarizedCurves, AlgebraicGeometry.polarizedCurvesToPolarizedStack, AlgebraicGeometry.polarizedCurvesToCurves, AlgebraicGeometry.isTwoFibreProduct_polarizedCurvesSquareUnconditional, AlgebraicGeometry.isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarized, AlgebraicGeometry.isOpenImmersion_polarizedCurvesToPolarized, AlgebraicGeometry.isClosedImmersion_polarizedCurvesToPolarized
statement: formalized
proof: formalized
---

# 109.4 The stack of polarized curves

Section 109.4 of the Stacks Project, [Tag 0DPY](https://stacks.math.columbia.edu/tag/0DPY). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DPY, the section

[Tag 0DPY](https://stacks.math.columbia.edu/tag/0DPY) in the Stacks Project.

**`AlgebraicGeometry.polarizedCurvesSquareUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean#L47). The attribute's comment: “the 2-fibre product square defining PolarizedCurves”.

> The 2-fibre product square defining the stack of polarized curves: the cospan is the
> forgetful 1-morphism `𝒫olarized ⟶ 𝒮paces'_{fp, flat, proper}` of Stacks 0D3Y and the inclusion
> `𝒞urves ⟶ 𝒮paces'_{fp, flat, proper}` of Stacks 0D50, and the apex is the canonical 2-fibre
> product of Stacks 0040.

```lean
def polarizedCurvesSquareUnconditional :
    Bicategory.TwoCommSq
      (polarizedToCartesianProperFlatHom B hZ
        (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B))
      (curvesToCartesianProperFlatHom B hZ)
```

**`AlgebraicGeometry.polarizedCurves`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean#L58). The attribute's comment: “PolarizedCurves, the apex of the 2-fibre product”.

> *PolarizedCurves* `= 𝒞urves ×_{𝒮paces'_{fp, flat, proper}} 𝒫olarized`, the stack of
> families of curves endowed with a relatively ample invertible module, as a category fibred in
> groupoids over the big fppf site of `Spec(ℤ)`.

```lean
def polarizedCurves :
    CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver B integerBase hZ)
```

**`AlgebraicGeometry.polarizedCurvesToPolarizedStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean#L64). The attribute's comment: “the projection to Polarized”.

> The projection `PolarizedCurves ⟶ 𝒫olarized`.

```lean
def polarizedCurvesToPolarizedStack :
    polarizedCurves B hZ ⟶
      polarizedFiberedCategory B hZ
        (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B)
```

**`AlgebraicGeometry.polarizedCurvesToCurves`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean#L72). The attribute's comment: “the projection to Curves”.

> The projection `PolarizedCurves ⟶ 𝒞urves`, forgetting the polarization.

```lean
def polarizedCurvesToCurves : polarizedCurves B hZ ⟶ curvesFiberedCategory B hZ
```

**`AlgebraicGeometry.isTwoFibreProduct_polarizedCurvesSquareUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesStack.lean#L78). The attribute's comment: “the square is a 2-fibre product”.

> The square of `AlgebraicGeometry.polarizedCurvesSquareUnconditional` is a 2-fibre product,
> being the canonical one.

```lean
def isTwoFibreProduct_polarizedCurvesSquareUnconditional :
    Bicategory.IsTwoFibreProduct (polarizedCurvesSquareUnconditional B hZ)
```

## Tag 0DPZ, a lemma

[Tag 0DPZ](https://stacks.math.columbia.edu/tag/0DPZ) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean#L195). The attribute's comment: “representability by algebraic spaces, given Stacks 0D3Z”.

> **Stacks 0DPZ.** The projection `PolarizedCurves ⟶ 𝒫olarized` is representable by algebraic
> spaces, being the base change of the inclusion of Stacks 0D50, which is representable by
> algebraic spaces by Stacks 0D5B.

```lean
theorem isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarized
    (h3Z : (polarizedProjection B ⋙ schemeOverIntegers B).IsFiberedInGroupoids) :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
      (polarizedCurvesToPolarized B hZ h3Z).hom
```

**`AlgebraicGeometry.isOpenImmersion_polarizedCurvesToPolarized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean#L209). The attribute's comment: “open immersion, given Stacks 0D3Z”.

> **Stacks 0DPZ.** The projection `PolarizedCurves ⟶ 𝒫olarized` is an open immersion, being
> the base change of the inclusion of Stacks 0D50, which is an open immersion by Stacks 0D5B.

```lean
theorem isOpenImmersion_polarizedCurvesToPolarized
    (h3Z : (polarizedProjection B ⋙ schemeOverIntegers B).IsFiberedInGroupoids) :
    Stack.IsOpenImmersion B integerBase hZ (polarizedCurvesToPolarized B hZ h3Z)
```

**`AlgebraicGeometry.isClosedImmersion_polarizedCurvesToPolarized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurves.lean#L222). The attribute's comment: “closed immersion, given Stacks 0D3Z”.

> **Stacks 0DPZ.** The projection `PolarizedCurves ⟶ 𝒫olarized` is a closed immersion, being
> the base change of the inclusion of Stacks 0D50, which is a closed immersion by Stacks 0D5B.

```lean
theorem isClosedImmersion_polarizedCurvesToPolarized
    (h3Z : (polarizedProjection B ⋙ schemeOverIntegers B).IsFiberedInGroupoids) :
    Stack.IsClosedImmersion B integerBase hZ (polarizedCurvesToPolarized B hZ h3Z)
```

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarizedUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean#L264). The attribute's comment: “representability by algebraic spaces”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarizedUnconditional :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
      (polarizedCurvesToPolarizedUnconditional B hZ).hom
```

**`AlgebraicGeometry.isOpenImmersion_polarizedCurvesToPolarizedUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean#L272). The attribute's comment: “open immersion”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is an open immersion.

```lean
theorem isOpenImmersion_polarizedCurvesToPolarizedUnconditional :
    Stack.IsOpenImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditional B hZ)
```

**`AlgebraicGeometry.isClosedImmersion_polarizedCurvesToPolarizedUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditional.lean#L279). The attribute's comment: “closed immersion”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is a closed immersion.

```lean
theorem isClosedImmersion_polarizedCurvesToPolarizedUnconditional :
    Stack.IsClosedImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditional B hZ)
```

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarized_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean#L127). The attribute's comment: “representability by algebraic spaces”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_polarizedCurvesToPolarized_unconditional :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
      (polarizedCurvesToPolarizedUnconditionalUp B hZ).hom
```

**`AlgebraicGeometry.isOpenImmersion_polarizedCurvesToPolarized_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean#L140). The attribute's comment: “open immersion”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is an open immersion.

```lean
theorem isOpenImmersion_polarizedCurvesToPolarized_unconditional :
    Stack.IsOpenImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditionalUp B hZ)
```

**`AlgebraicGeometry.isClosedImmersion_polarizedCurvesToPolarized_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesUnconditionalImmersion.lean#L152). The attribute's comment: “closed immersion”.

> The projection `PolarizedCurves ⟶ 𝒫olarized` is a closed immersion.

```lean
theorem isClosedImmersion_polarizedCurvesToPolarized_unconditional :
    Stack.IsClosedImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditionalUp B hZ)
```

## Tag 0DQ0, a lemma

[Tag 0DQ0](https://stacks.math.columbia.edu/tag/0DQ0) in the Stacks Project.

**`AlgebraicGeometry.isSmooth_and_isSurjective_polarizedCurvesToCurves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesToCurvesSmoothSurjective.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PolarizedCurvesToCurvesSmoothSurjective.lean#L80).

> The projection `PolarizedCurves ⟶ 𝒞urves` is smooth and surjective.
>
> The 1-morphism is `AlgebraicGeometry.polarizedCurvesToCurvesAlgebraicOfPolarized`, the projection
> of the 2-fibre product `PolarizedCurves = 𝒞urves ×_{𝒮paces'_{fp, flat, proper}} 𝒫olarized` of
> Stacks 0DPY, read in the 2-category of algebraic stacks of Stacks 03YP; smoothness is Stacks 075U
> and surjectivity is Stacks 04ZS.

```lean
theorem isSmooth_and_isSurjective_polarizedCurvesToCurves :
    Stack.AlgebraicStacks.IsSmooth B integerBase hZ
        (polarizedCurvesToCurvesAlgebraicOfPolarized B hZ
          (polarizedCurvesToCurves_isAlgebraic_smooth_surjective.{w, u} B hZ).2.1.1
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)) ∧
      Stack.IsSurjective B integerBase hZ
        (polarizedCurvesToCurvesAlgebraicOfPolarized B hZ
          (polarizedCurvesToCurves_isAlgebraic_smooth_surjective.{w, u} B hZ).2.1.1
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ))
```

## Tag 0E6F, a lemma

[Tag 0E6F](https://stacks.math.columbia.edu/tag/0E6F) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.exists_etaleCovering_isPullback_isProjectiveMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesEtaleLocallyHProjective.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesEtaleLocallyHProjective.lean#L351).

> **Families of curves are étale locally H-projective schemes.** Let `X ⟶ S` be a family of
> curves. Then there is an étale covering `{S_j ⟶ S}` (a family of étale morphisms of the site whose
> images cover `S`) such that each `X_j = X ×_S S_j` is a scheme `Z` — a cartesian square of
> algebraic spaces with `schemeSpace Z` at its corner — and `Z ⟶ S_j` is H-projective.

```lean
theorem exists_etaleCovering_isPullback_isProjectiveMorphism (X : CurveFamily B hZ) :
    ∃ (J : Type u) (U : J → BigFppfOver B integerBase hZ) (φ : ∀ j, U j ⟶ X.base),
      (∀ j, Etale ((𝒯).map (φ j))) ∧
      (∀ s : (𝒯).obj X.base, ∃ j, s ∈ Set.range ((𝒯).map (φ j))) ∧
      ∀ j, ∃ (Z : BigFppfOver B integerBase hZ) (p : schemeSpace Z ⟶ X.total) (q : Z ⟶ U j),
        IsPullback p (schemeSpaceMap q) X.toBase (schemeSpaceMap (φ j)) ∧
        IsProjectiveMorphism ((𝒯).map q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.4, Tag 0DPY](https://stacks.math.columbia.edu/tag/0DPY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
