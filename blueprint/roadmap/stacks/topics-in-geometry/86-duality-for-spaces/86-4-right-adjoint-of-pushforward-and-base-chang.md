---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.TorIndependentBaseChangeSquare, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChange, AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChange, AlgebraicGeometry.Space.TorIndependentBaseChangeSquare.DualityData.twistedInverseImageBaseChange, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_vertical, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_horizontal, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_grid
statement: formalized
proof: formalized
---

# 86.4 Right adjoint of pushforward and base change, I

Section 86.4 of the Stacks Project, [Tag 0E5A](https://stacks.math.columbia.edu/tag/0E5A). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E5B, an equation

[Tag 0E5B](https://stacks.math.columbia.edu/tag/0E5B) in the Stacks Project.

**`AlgebraicGeometry.Space.TorIndependentBaseChangeSquare`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChange.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChange.lean#L71). The attribute's comment: “the Tor-independent cartesian square”.

> A cartesian square of algebraic spaces over `S` whose upper right and
> lower left corners are Tor independent over the lower right corner.

```lean
structure TorIndependentBaseChangeSquare (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointBaseChange.lean#L178).

> For a cartesian square of algebraic spaces with `X` and `Y'` quasi-compact and
> quasi-separated and `Y` quasi-separated, the transformation `Rg'_* ∘ a' ⟶ a ∘ Rg_*` between the
> right adjoints `a`, `a'` of `Rf_*`, `Rf'_*` on `D_QCoh` (Stacks 0E55): the mate of the base change
> map `Lg^* ∘ Rf_* ⟶ Rf'_* ∘ L(g')^*` of Stacks 07A7.

```lean
def quasicoherentDerivedRightAdjointBaseChange :
    quasicoherentDerivedRightAdjoint hZ f'
          (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc)
          (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) hY'qs ⋙
        quasicoherentDerivedPushforward B S hS g'
          (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ X.2 hXqs
            (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc) g'.hom)
          (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X'.2
            (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) g'.hom) ⟶
      quasicoherentDerivedPushforward B S hS g
          (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y.2 hYqs hY'qc g.hom)
          (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ Y'.2 hY'qs g.hom) ⋙
        quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs
```

## Tag 0E5C, a lemma

[Tag 0E5C](https://stacks.math.columbia.edu/tag/0E5C) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedRightAdjointBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L105).

> **Stacks 0E5C.**  For a cartesian square of quasi-compact quasi-separated algebraic spaces
> with `X` and `Y'` Tor independent over `Y`, the base change transformation
> `Rg'_* ∘ a' ⟶ a ∘ Rg_*` of Stacks 0E5B is an isomorphism.

```lean
theorem isIso_quasicoherentDerivedRightAdjointBaseChange :
    IsIso (quasicoherentDerivedRightAdjointBaseChange hZ sq hXqc hXqs hYqs hY'qc hY'qs)
```

## Tag 0E5D, an equation

[Tag 0E5D](https://stacks.math.columbia.edu/tag/0E5D) in the Stacks Project.

**`AlgebraicGeometry.Space.TorIndependentBaseChangeSquare.DualityData.twistedInverseImageBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChange.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChange.lean#L165).

> The base change map `L(g')^* ∘ a ⟶ a' ∘ Lg^*` between twisted inverse
> images, the composition of the unit of `Lg^* ⊣ Rg_*`, the inverse of the base change map
> `Rg'_* ∘ a' ⟶ a ∘ Rg_*` between right adjoints, and the counit of `L(g')^* ⊣ Rg'_*`.

```lean
noncomputable def twistedInverseImageBaseChange (hbc : IsIso D.baseChange) :
    D.twistedInverseImage ⋙ D.pullbackG' ⟶ D.pullbackG ⋙ D.twistedInverseImage'
```

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L117).

> **The base change map `L(g')^* ∘ a ⟶ a' ∘ Lg^*`** (Stacks 0E5D) of a cartesian square of
> quasi-compact quasi-separated algebraic spaces with `X` and `Y'` Tor independent over `Y`:
> the unit of `Lg^* ⊣ Rg_*`, the inverse of the isomorphism of Stacks 0E5C, and the counit of
> `L(g')^* ⊣ Rg'_*`.

```lean
def quasicoherentDerivedRightAdjointBaseChangeMap :
    quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs ⋙ quasicoherentDerivedModulePullback g' ⟶
      quasicoherentDerivedModulePullback g ⋙
        quasicoherentDerivedRightAdjoint hZ f'
          (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc)
          (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) hY'qs
```

## Tag 0E5E, a lemma

[Tag 0E5E](https://stacks.math.columbia.edu/tag/0E5E) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_vertical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L214).

> **Stacks 0E5E.**  For two vertically stacked cartesian squares of quasi-compact
> quasi-separated algebraic spaces, with `f` and `l` as well as `g` and `m` Tor independent, the
> base change map of Stacks 0E5D for the outer rectangle is the composite of those of the two
> squares, read through the identifications `a ∘ b = c` and `a' ∘ b' = c'` of the right adjoints
> of `R(g ∘ f)_* = Rg_* ∘ Rf_*` and `R(g' ∘ f')_* = Rg'_* ∘ Rf'_*`.

```lean
theorem quasicoherentDerivedRightAdjointBaseChangeMap_vertical (K) :
    (quasicoherentDerivedRightAdjointBaseChangeMap hZ (sqt.paste_vert sqb) hXqc hXqs hZqs
        hZ'qc hZ'qs (torIndependent_rectangle_vertical sqb hTt hTb)).app K =
      (quasicoherentDerivedModulePullback k).map
          ((RightAdjointBaseChange.rightAdjointCompIso (squareAdjF hZ hXqc hXqs hYqs)
            (squareAdjF hZ hYqc hYqs hZqs) (squareAdjF hZ hXqc hXqs hZqs)
            (quasicoherentDerivedPushforwardCompIso f g
              (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y.2 hYqs hXqc f.hom)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X.2 hXqs f.hom)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Z.2 hZqs hYqc g.hom)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ Y.2 hYqs g.hom)
              (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Z.2 hZqs hXqc (f ≫ g).hom)
              (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X.2 hXqs
                (f ≫ g).hom))).inv.app K) ≫
        (quasicoherentDerivedRightAdjointBaseChangeMap hZ sqt hXqc hXqs hYqs hY'qc hY'qs
          hTt).app ((quasicoherentDerivedRightAdjoint hZ g hYqc hYqs hZqs).obj K) ≫
        (quasicoherentDerivedRightAdjoint hZ f'
            (isQuasiCompactSpace_of_isPullback hZ sqt hXqc hYqs hY'qc)
            (isAbsolutelyQuasiSeparated_of_isPullback hZ sqt hXqs hY'qs) hY'qs).map
          ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sqb hYqc hYqs hZqs hZ'qc hZ'qs
            hTb).app K) ≫
        (RightAdjointBaseChange.rightAdjointCompIso (squareAdjF' hZ sqt hXqc hXqs hYqs hY'qc hY'qs)
          (squareAdjF' hZ sqb hYqc hYqs hZqs hZ'qc hZ'qs)
          (squareAdjF' hZ (sqt.paste_vert sqb) hXqc hXqs hZqs hZ'qc hZ'qs)
          (quasicoherentDerivedPushforwardCompIso f' g'
            (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y'.2 hY'qs
              (isQuasiCompactSpace_of_isPullback hZ sqt hXqc hYqs hY'qc) f'.hom)
            (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X'.2
              (isAbsolutelyQuasiSeparated_of_isPullback hZ sqt hXqs hY'qs) f'.hom)
            (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Z'.2 hZ'qs hY'qc g'.hom)
            (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ Y'.2 hY'qs g'.hom)
            (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Z'.2 hZ'qs
              (isQuasiCompactSpace_of_isPullback hZ sqt hXqc hYqs hY'qc) (f' ≫ g').hom)
            (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X'.2
              (isAbsolutelyQuasiSeparated_of_isPullback hZ sqt hXqs hY'qs)
              (f' ≫ g').hom))).hom.app ((quasicoherentDerivedModulePullback m).obj K)
```

## Tag 0E5F, a lemma

[Tag 0E5F](https://stacks.math.columbia.edu/tag/0E5F) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_horizontal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L288).

> **Stacks 0E5F.**  For two horizontally composed cartesian squares of quasi-compact
> quasi-separated algebraic spaces, with `f` and `h` as well as `f'` and `h'` Tor independent, the
> base change map of Stacks 0E5D for the outer rectangle is the composite of those of the two
> squares, read through `L(g ∘ g')^* = L(g')^* ∘ Lg^*` and `L(h ∘ h')^* = L(h')^* ∘ Lh^*`.

```lean
theorem quasicoherentDerivedRightAdjointBaseChangeMap_horizontal (K) :
    (quasicoherentDerivedRightAdjointBaseChangeMap hZ (sql.paste_horiz sqr) hXqc hXqs hYqs
        hY''qc hY''qs (torIndependent_rectangle_horizontal sqr hTr hTl)).app K =
      (quasicoherentDerivedModulePullbackCompIso g' g).inv.app
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K) ≫
        (quasicoherentDerivedModulePullback g').map
          ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sqr hXqc hXqs hYqs hY'qc hY'qs
            hTr).app K) ≫
        (quasicoherentDerivedRightAdjointBaseChangeMap hZ sql hX'qc hX'qs hY'qs hY''qc
          hY''qs hTl).app ((quasicoherentDerivedModulePullback h).obj K) ≫
        (quasicoherentDerivedRightAdjoint hZ f''
          (isQuasiCompactSpace_of_isPullback hZ (sql.paste_horiz sqr) hXqc hYqs hY''qc)
          (isAbsolutelyQuasiSeparated_of_isPullback hZ (sql.paste_horiz sqr) hXqs hY''qs)
          hY''qs).map ((quasicoherentDerivedModulePullbackCompIso h' h).hom.app K)
```

## Tag 0E5G, a remark

[Tag 0E5G](https://stacks.math.columbia.edu/tag/0E5G) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_grid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMapGrid.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMapGrid.lean#L276).

> **Stacks 0E5G.**  Let `S` be a scheme and consider a commutative diagram
>
> ```
> X'' --k'--> X' --k--> X
>  |f''        |f'       |f
>  v           v         v
> Y'' --l'--> Y' --l--> Y
>  |g''        |g'       |g
>  v           v         v
> Z'' --m'--> Z' --m--> Z
> ```
>
> of quasi-compact and quasi-separated algebraic spaces over `S` whose squares `A B / C D` are
> cartesian, with `(f, l)`, `(g, m)`, `(f', l')`, `(g', m')` Tor independent pairs. Let `a`, `a'`,
> `a''`, `b`, `b'`, `b''` be the right adjoints of Stacks 0E55 for `f`, `f'`, `f''`, `g`, `g'`, `g''`
> (`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjoint`). Then the two transformations
> `(k')^* ∘ k^* ∘ a ∘ b ⟶ a'' ∘ b'' ∘ (m')^* ∘ m^*` built from the base change maps (Stacks 0E5D)
> of the rectangles, `γ_{A+C} ∘ γ_{B+D}` (columns) and `γ_{C+D} ∘ γ_{A+B}` (rows), are equal. Here
> the maps of the rectangles are read through the identifications of Stacks 0E5E and 0E5F
> (`quasicoherentDerivedRightAdjointBaseChangeMapPasteVert`,
> `quasicoherentDerivedRightAdjointBaseChangeMapPasteHoriz`), and the equality is stated at every
> object `K` of `D_QCoh(𝒪_Z)`.
>
> Of the source's standing hypothesis that all nine spaces are quasi-compact and quasi-separated,
> two parts are not assumed: `X''` inherits both properties from the cartesian squares, and
> quasi-compactness of `Z` is not used.

```lean
theorem quasicoherentDerivedRightAdjointBaseChangeMap_grid (K) :
    (quasicoherentDerivedModulePullback k').map
        ((quasicoherentDerivedRightAdjointBaseChangeMapPasteVert hZ sqB sqD hXqc hXqs hYqc hYqs
          hZqs hY'qc hY'qs hZ'qc hZ'qs hTB hTD).app K) ≫
      (quasicoherentDerivedRightAdjointBaseChangeMapPasteVert hZ sqA sqC hX'qc hX'qs hY'qc hY'qs
        hZ'qs hY''qc hY''qs hZ''qc hZ''qs hTA hTC).app
          ((quasicoherentDerivedModulePullback m).obj K) =
    (quasicoherentDerivedRightAdjointBaseChangeMapPasteHoriz hZ sqB sqA hXqc hXqs hYqs hY''qc
        hY''qs hTB hTA).app
          ((quasicoherentDerivedRightAdjoint hZ g hYqc hYqs hZqs).obj K) ≫
      (quasicoherentDerivedRightAdjoint hZ f''
          (isQuasiCompactSpace_of_isPullback hZ (sqA.paste_horiz sqB) hXqc hYqs hY''qc)
          (isAbsolutelyQuasiSeparated_of_isPullback hZ (sqA.paste_horiz sqB) hXqs hY''qs)
          hY''qs).map
        ((quasicoherentDerivedRightAdjointBaseChangeMapPasteHoriz hZ sqD sqC hYqc hYqs hZqs
          hZ''qc hZ''qs hTD hTC).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.4, Tag 0E5A](https://stacks.math.columbia.edu/tag/0E5A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
