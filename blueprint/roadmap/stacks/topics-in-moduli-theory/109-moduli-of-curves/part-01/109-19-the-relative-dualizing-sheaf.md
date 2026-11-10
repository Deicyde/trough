---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.exists_iso_shift_relativeDualizingComplex, AlgebraicGeometry.CurveFamily.relativeDualizingSheaf, AlgebraicGeometry.CurveFamily.isInvertibleModule_relativeDualizingSheaf
statement: formalized
proof: formalized
---

# 109.19 The relative dualizing sheaf

Section 109.19 of the Stacks Project, [Tag 0E6N](https://stacks.math.columbia.edu/tag/0E6N). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E6P, a lemma

[Tag 0E6P](https://stacks.math.columbia.edu/tag/0E6P) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.exists_iso_shift_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean#L153).

> Let `f : X ⟶ S` be a family of curves with Cohen–Macaulay fibres equidimensional of
> dimension one (Stacks 0E1F: `f` is Cohen–Macaulay in the sense of Stacks 0E0V and has relative
> dimension one in the sense of part (2) of Stacks 06LR), and let `(ω^•_{X/S}, τ)` be a relative
> dualizing complex of `f` (Stacks 0E5X). Then `ω^•_{X/S} = ω_{X/S}[1]` for a pseudo-coherent
> `𝒪_X`-module `ω_{X/S}` flat over `S` whose formation commutes with arbitrary base change: for
> every morphism of families of curves `X' ⟶ X` over `S' ⟶ S` (a cartesian square), every relative
> dualizing complex of `X'/S'` is `(g'^*ω_{X/S})[1]`, `g' : X' ⟶ X` the projection.

```lean
theorem CurveFamily.exists_iso_shift_relativeDualizingComplex (X : CurveFamily B hZ)
    (hcm : Space.IsCohenMacaulay B integerBase hZ X.toBase.hom)
    (hdim : Space.HasRelativeDimension 1 B integerBase hZ X.toBase.hom)
    (D : RelativeDualizingComplex B.contains_terminal X.toBase X.proper X.flat
      X.finitePresentation) :
    ∃ F : Space.Modules.{u, u} B integerBase hZ X.total.1 X.total.2,
      Nonempty (D.ω ≅ ((DerivedCategory.singleFunctor _ 0).obj F)⟦(1 : ℤ)⟧) ∧
      (Space.smallEtaleRingedSite B integerBase hZ X.total.1 X.total.2).IsPseudoCoherent
        ((DerivedCategory.singleFunctor _ 0).obj F) ∧
      Space.IsFlatOver B integerBase hZ X.total.2 X.toBase.hom F ∧
      ∀ {X' : CurveFamily B hZ} (φ : X' ⟶ X)
        (D' : RelativeDualizingComplex B.contains_terminal X'.toBase X'.proper X'.flat
          X'.finitePresentation),
        Nonempty (D'.ω ≅ (smallEtaleDerivedModulePullback B integerBase hZ φ.totalMap).obj
          (((DerivedCategory.singleFunctor _ 0).obj F)⟦(1 : ℤ)⟧)) ∧
        Nonempty ((smallEtaleDerivedModulePullback B integerBase hZ φ.totalMap).obj
            ((DerivedCategory.singleFunctor
              (SheafOfModules.{u} (ringedToposStructureRingSheaf B integerBase hZ X.total))
                0).obj F) ≅
          (DerivedCategory.singleFunctor
            (SheafOfModules.{u} (ringedToposStructureRingSheaf B integerBase hZ X'.total)) 0).obj
            ((modulePullback B integerBase hZ φ.totalMap).obj F))
```

## Tag 0E6Q, a definition

[Tag 0E6Q](https://stacks.math.columbia.edu/tag/0E6Q) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.relativeDualizingSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean#L131).

> Let `f : X ⟶ S` be a family of curves and `(ω^•_{X/S}, τ)` its relative dualizing complex
> (Stacks 0E5X). The *relative dualizing sheaf* of `f` is the `𝒪_X`-module
> `ω_{X/S} = H^{-1}(ω^•_{X/S})`. For a Cohen–Macaulay family of relative dimension one it is the
> pseudo-coherent module flat over `S` of Stacks 0E6P, with `ω^•_{X/S} = ω_{X/S}[1]`
> (`AlgebraicGeometry.CurveFamily.exists_iso_shift_relativeDualizingComplex`).

```lean
def CurveFamily.relativeDualizingSheaf (X : CurveFamily B hZ)
    (D : RelativeDualizingComplex B.contains_terminal X.toBase X.proper X.flat
      X.finitePresentation) :
    Space.Modules.{u, u} B integerBase hZ X.total.1 X.total.2
```

## Tag 0E6R, a lemma

[Tag 0E6R](https://stacks.math.columbia.edu/tag/0E6R) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.isInvertibleModule_relativeDualizingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeDualizingSheaf.lean#L582).

> Let `f : X ⟶ S` be a family of curves with Gorenstein fibres equidimensional of dimension
> one (`Curves^{Gorenstein, 1}` of Stacks 0E6M: `f` is Gorenstein in the sense of Stacks 0E14 and
> has relative dimension one in the sense of part (2) of Stacks 06LR), and let `(ω^•_{X/S}, τ)` be
> a relative dualizing complex (Stacks 0E5X). Then the relative dualizing sheaf
> `ω_{X/S} = H^{-1}(ω^•_{X/S})` (Stacks 0E6Q) is an invertible `𝒪_X`-module, and its formation
> commutes with arbitrary base change: for every morphism of families of curves `X' ⟶ X` over
> `S' ⟶ S` (a cartesian square) and every relative dualizing complex of `X'/S'`, the relative
> dualizing sheaf of `X'/S'` is the pullback of `ω_{X/S}` along the projection `g' : X' ⟶ X`.

```lean
theorem CurveFamily.isInvertibleModule_relativeDualizingSheaf (X : CurveFamily B hZ)
    (hX : IsGorensteinDimOneFamily B hZ X)
    (D : RelativeDualizingComplex B.contains_terminal X.toBase X.proper X.flat
      X.finitePresentation) :
    Space.IsInvertibleModule X.total (X.relativeDualizingSheaf D) ∧
      ∀ {X' : CurveFamily B hZ} (φ : X' ⟶ X)
        (D' : RelativeDualizingComplex B.contains_terminal X'.toBase X'.proper X'.flat
          X'.finitePresentation),
        Nonempty (X'.relativeDualizingSheaf D' ≅
          (modulePullback B integerBase hZ φ.totalMap).obj (X.relativeDualizingSheaf D))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.19, Tag 0E6N](https://stacks.math.columbia.edu/tag/0E6N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
