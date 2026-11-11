---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackTensor, AlgebraicGeometry.Space.PullbackComparisonData.homEquiv_symm_compareWithPullbackTensor, AlgebraicGeometry.Space.PullbackComparisonData.projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit, AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackTensor_naturality, AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullback, AlgebraicGeometry.Space.PullbackComparisonData.projectionFormulaMap_comp_map_compareWithPullback_comp_counit, AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullback_naturality, AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackNatTrans
statement: formalized
proof: formalized
---

# 86.7 Right adjoint of pushforward and pullback

Section 86.7 of the Stacks Project, [Tag 0E5N](https://stacks.math.columbia.edu/tag/0E5N). 3 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E5P, an equation

[Tag 0E5P](https://stacks.math.columbia.edu/tag/0E5P) in the Stacks Project.

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L290). The attribute's comment: “two-variable construction”.

> **The two-variable comparison map of [Stacks, Tag 0E5P]**:
> `Lf^*K ⊗ᴸ_{𝒪_X} a(L) ⟶ a(K ⊗ᴸ_{𝒪_Y} L)`, for a right adjoint `a` of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. It is the map adjoint to the inverse of the projection
> formula `Rf_*(Lf^*K ⊗ᴸ_{𝒪_X} a(L)) ≅ K ⊗ᴸ_{𝒪_Y} Rf_*(a(L))` followed by the identity of `K`
> tensored with the trace map `adja.counit.app L : Rf_*(a(L)) ⟶ L`.

```lean
def compareWithPullbackTensor (K L : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    (D.tensorX.obj (D.pullback.obj K)).obj (a.obj L) ⟶ a.obj ((D.tensorY.obj K).obj L)
```

**`AlgebraicGeometry.Space.PullbackComparisonData.homEquiv_symm_compareWithPullbackTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L298). The attribute's comment: “two-variable adjunction characterization”.

> The adjoint transpose of the two-variable comparison map is the inverse projection formula
> followed by the identity of `K` tensored with the trace map.

```lean
theorem homEquiv_symm_compareWithPullbackTensor
    (K L : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    (adja.homEquiv _ _).symm (D.compareWithPullbackTensor adja K L) =
      inv (D.projectionFormulaMap (a.obj L) K) ≫
        (D.tensorY.obj K).map (adja.counit.app L)
```

**`AlgebraicGeometry.Space.PullbackComparisonData.projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L319). The attribute's comment: “two-variable characterization without the inverse”.

> **The two-variable comparison map as the source constructs it**: the projection formula,
> followed by `Rf_*` of the comparison map and the trace map, is the identity of `K` tensored with
> the trace map. This is the characterization with no inverse in it.

```lean
theorem projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit
    (K L : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    D.projectionFormulaMap (a.obj L) K ≫
        D.pushforward.map (D.compareWithPullbackTensor adja K L) ≫
          adja.counit.app ((D.tensorY.obj K).obj L) =
      (D.tensorY.obj K).map (adja.counit.app L)
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackTensor_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L383). The attribute's comment: “two-variable naturality”.

> The two-variable comparison map is natural in `K` and `L` jointly.

```lean
theorem compareWithPullbackTensor_naturality
    {K K' L L' : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2} (h : K ⟶ K') (g : L ⟶ L') :
    (D.tensorX.map (D.pullback.map h)).app (a.obj L) ≫
        (D.tensorX.obj (D.pullback.obj K')).map (a.map g) ≫
          D.compareWithPullbackTensor adja K' L' =
      D.compareWithPullbackTensor adja K L ≫
        a.map ((D.tensorY.map h).app L ≫ (D.tensorY.obj K').map g)
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L401).

> **Equation 86.7.0.1 of [Stacks, Tag 0E5P]**: the comparison map
> `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)`, the two-variable comparison map at `L = 𝒪_Y` followed by `a`
> applied to the right unitor `K ⊗ᴸ_{𝒪_Y} 𝒪_Y ≅ K`.

```lean
def compareWithPullback (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    (D.tensorX.obj (D.pullback.obj K)).obj
        (a.obj (derivedStructureSheaf B S hS Y.1 Y.2)) ⟶ a.obj K
```

**`AlgebraicGeometry.Space.PullbackComparisonData.projectionFormulaMap_comp_map_compareWithPullback_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L429). The attribute's comment: “characterization without the inverse”.

> **Equation 86.7.0.1 as the source constructs it**: the projection formula, followed by `Rf_*`
> of the displayed comparison map and the trace map, is the identity of `K` tensored with the trace
> map at `𝒪_Y`, followed by the right unitor.

```lean
theorem projectionFormulaMap_comp_map_compareWithPullback_comp_counit
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    D.projectionFormulaMap (a.obj (derivedStructureSheaf B S hS Y.1 Y.2)) K ≫
        D.pushforward.map (D.compareWithPullback adja ρ K) ≫ adja.counit.app K =
      (D.tensorY.obj K).map (adja.counit.app (derivedStructureSheaf B S hS Y.1 Y.2)) ≫
        ρ.hom.app K
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullback_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L455). The attribute's comment: “functoriality in K”.

> Equation 86.7.0.1 is functorial in `K`.

```lean
theorem compareWithPullback_naturality
    {K K' : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2} (h : K ⟶ K') :
    (D.tensorX.map (D.pullback.map h)).app
          (a.obj (derivedStructureSheaf B S hS Y.1 Y.2)) ≫
        D.compareWithPullback adja ρ K' =
      D.compareWithPullback adja ρ K ≫ a.map h
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L496). The attribute's comment: “functoriality in K, as a natural transformation”.

> Equation 86.7.0.1 as a natural transformation of functors of `K`, which is its
> functoriality in `K`.

```lean
def compareWithPullbackNatTrans :
    D.compareWithPullbackSource (a.obj (derivedStructureSheaf B S hS Y.1 Y.2)) ⟶ a
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullbackNatTrans_commShift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 623](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L623). The attribute's comment: “compatibility with distinguished triangles”.

> **Compatibility of Equation 86.7.0.1 with distinguished triangles**: the displayed comparison
> map commutes with translation, so it carries the third morphism of a distinguished triangle of
> `D_QCoh(𝒪_Y)` to the third morphism of its image.

```lean
theorem compareWithPullbackNatTrans_commShift :
    NatTrans.CommShift (D.compareWithPullbackNatTrans adja ρ) ℤ
```

**`AlgebraicGeometry.Space.PullbackComparisonData.compareWithPullback_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparison.lean#L630). The attribute's comment: “compatibility with distinguished triangles, componentwise”.

> Equation 86.7.0.1 at a translate of `K`, which is that compatibility componentwise.

```lean
theorem compareWithPullback_shift (n : ℤ)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    D.compareWithPullback adja ρ ((shiftFunctor _ n).obj K) =
      ((D.compareWithPullbackSource
          (a.obj (derivedStructureSheaf B S hS Y.1 Y.2))).commShiftIso n).hom.app K ≫
        (shiftFunctor _ n).map (D.compareWithPullback adja ρ K) ≫
          (a.commShiftIso n).inv.app K
```

**`AlgebraicGeometry.Space.quasicoherentDerivedCompareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonical.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonical.lean#L371).

> **Stacks 0E5P.** Let `f : X ⟶ Y` be a morphism of quasi-compact quasi-separated algebraic
> spaces over `S` and let `a` be the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`
> (Stacks 0E55). The map `Lf^*K ⊗^L_{𝒪_X} a(𝒪_Y) ⟶ a(K)`, the two-variable map at `L = 𝒪_Y`
> followed by `a` of the unitor, is functorial in `K`.

```lean
def quasicoherentDerivedCompareWithPullback :
    quasicoherentDerivedModulePullback f ⋙ (quasicoherentDerivedTensor B S hS X).flip.obj
        ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj
          (derivedStructureSheaf B S hS Y.1 Y.2)) ⟶
      quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs
```

**`AlgebraicGeometry.Space.quasicoherentDerivedCompareWithPullback_commShift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonical.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonical.lean#L395).

> **Stacks 0E5P, compatibility with distinguished triangles.** The map
> `Lf^*K ⊗^L_{𝒪_X} a(𝒪_Y) ⟶ a(K)` commutes with the shift, so it carries the third morphism of a
> distinguished triangle in `K` to the third morphism of its image.

```lean
theorem quasicoherentDerivedCompareWithPullback_commShift :
    NatTrans.CommShift (quasicoherentDerivedCompareWithPullback hZ f hXqc hXqs hYqs) ℤ
```

## Tag 0E5Q, a lemma

[Tag 0E5Q](https://stacks.math.columbia.edu/tag/0E5Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedCompareWithPullbackTensor_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonPerfectDual.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonPerfectDual.lean#L51). The attribute's comment: “the map Lf^*K ⊗ a(L) → a(K ⊗ L) is an isomorphism for K perfect”.

> **Stacks 0E5Q.** Let `f : X ⟶ Y` be a morphism of quasi-compact and quasi-separated algebraic
> spaces and `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. For `K, L ∈ D_QCoh(𝒪_Y)`
> with `K` perfect, the map `Lf^*K ⊗^L a(L) ⟶ a(K ⊗^L L)` is an isomorphism.

```lean
theorem isIso_quasicoherentDerivedCompareWithPullbackTensor_of_isPerfect
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hK : RingedSite.IsPerfect (smallEtaleRingedSite B S hS Y.1 Y.2) K.obj)
    (L : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    IsIso (quasicoherentDerivedCompareWithPullbackTensor hZ f hXqc hXqs hYqs K L)
```

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedCompareWithPullback_app_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonPerfectDual.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonPerfectDual.lean#L63). The attribute's comment: “in particular, the map (0E5P) Lf^*K ⊗ a(O\_Y) → a(K) is an isomorphism for K perfect”.

> **Stacks 0E5Q, in particular.** For `K ∈ D_QCoh(𝒪_Y)` perfect, the map
> `Lf^*K ⊗^L a(𝒪_Y) ⟶ a(K)` of Stacks 0E5P is an isomorphism.

```lean
theorem isIso_quasicoherentDerivedCompareWithPullback_app_of_isPerfect
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hK : RingedSite.IsPerfect (smallEtaleRingedSite B S hS Y.1 Y.2) K.obj) :
    IsIso ((quasicoherentDerivedCompareWithPullback hZ f hXqc hXqs hYqs).app K)
```

## Tag 0E5R, a lemma

[Tag 0E5R](https://stacks.math.columbia.edu/tag/0E5R) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedCompareWithPullback_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonicalBaseChange.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonCanonicalBaseChange.lean#L247).

> For a cartesian square of quasi-compact quasi-separated algebraic spaces
> with `X` and `Y'` Tor independent over `Y` and `K ∈ D_QCoh(𝒪_Y)`, the square
>
> `L(g')^*(Lf^*K ⊗^L a(𝒪_Y)) ⟶ L(g')^*a(K) ⟶ a'(Lg^*K)` (`L(g')^*` of Stacks 0E5P, then the base
> change map of Stacks 0E5D)
>
> equals `L(g')^*(Lf^*K ⊗^L a(𝒪\_Y)) ⟶ L(g')^*Lf^*K ⊗^L L(g')^*a(𝒪\_Y) ⟶ L(f')^*Lg^*K ⊗^L a'(𝒪\_\{Y'})
> ⟶ a'(Lg^*K)`: Stacks 07A4 for `g'`, the identification of the two iterated pullbacks around the
> square and Stacks 0E5D at `𝒪_Y` followed by `a'(Lg^*𝒪_Y ≅ 𝒪_{Y'})`, then Stacks 0E5P for `f'`.

```lean
theorem quasicoherentDerivedCompareWithPullback_baseChange
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    (quasicoherentDerivedModulePullback g').map
          ((quasicoherentDerivedCompareWithPullback hZ f hXqc hXqs hYqs).app K) ≫
        (quasicoherentDerivedRightAdjointBaseChangeMap hZ sq hXqc hXqs hYqs hY'qc hY'qs
          hTor).app K =
      (quasicoherentDerivedPullbackTensorComparison g').app
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj
            (derivedStructureSheaf B S hS Y.1 Y.2), (quasicoherentDerivedModulePullback f).obj K) ≫
        ((quasicoherentDerivedTensor B S hS X').map
            (ObjectProperty.homMk
              ((smallEtaleDerivedModulePullbackSquareIso B S hS f g f' g' sq.w).hom.app K.obj ≫
                (smallEtaleDerivedModulePullbackCompIso B S hS f' g).inv.app K.obj) :
              (quasicoherentDerivedModulePullback g').obj
                  ((quasicoherentDerivedModulePullback f).obj K) ⟶
                (quasicoherentDerivedModulePullback f').obj
                  ((quasicoherentDerivedModulePullback g).obj K))).app
            ((quasicoherentDerivedModulePullback g').obj
              ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj
                (derivedStructureSheaf B S hS Y.1 Y.2))) ≫
          ((quasicoherentDerivedTensor B S hS X').obj ((quasicoherentDerivedModulePullback f').obj
              ((quasicoherentDerivedModulePullback g).obj K))).map
            ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sq hXqc hXqs hYqs hY'qc hY'qs
                hTor).app (derivedStructureSheaf B S hS Y.1 Y.2) ≫
              (quasicoherentDerivedRightAdjoint hZ f'
                (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc)
                (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) hY'qs).map
                (ObjectProperty.homMk
                  (smallEtaleDerivedModulePullbackUnitIso (B := B) (S := S) (hS := hS) g).hom :
                  (quasicoherentDerivedModulePullback g).obj
                      (derivedStructureSheaf B S hS Y.1 Y.2) ⟶
                    derivedStructureSheaf B S hS Y'.1 Y'.2)) ≫
            (quasicoherentDerivedCompareWithPullback hZ f'
              (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc)
              (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) hY'qs).app
              ((quasicoherentDerivedModulePullback g).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.7, Tag 0E5N](https://stacks.math.columbia.edu/tag/0E5N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
