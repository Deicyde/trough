---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_of_openCover, Stacks.Cohomology.DerivedProjectionFormula.isIso_derivedPullback_map_projectionFormulaMap_of_isOpenImmersion, AlgebraicGeometry.projectionFormulaIsIsoOnQuasicoherent, Stacks.Cohomology.ProjectionFormulaDevissage.isIso_projectionFormulaMap_twoOutOfThree, Stacks.Cohomology.ProjectionFormulaGeneralBase.isIso_projectionFormulaMap_of_isQuasicoherent, Stacks.Cohomology.ProjectionFormulaOverAffineBase.isIso_projectionFormulaMap_of_isQuasicoherent, Stacks.Cohomology.ProjectionFormulaPerfect.isIso_derivedPullback_map_projectionFormulaMap, Stacks.Cohomology.ProjectionFormulaQCoh.isIso_projectionFormulaMap_of_isDQCoh
statement: formalized
proof: formalized
---

# 36.22 Cohomology and base change, IV

Section 36.22 of the Stacks Project, [Tag 08ET](https://stacks.math.columbia.edu/tag/08ET). 9 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08EU, a lemma

[Tag 08EU](https://stacks.math.columbia.edu/tag/08EU) in the Stacks Project.

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ProjectionFormulaOpenCoverDescent.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ProjectionFormulaOpenCoverDescent.lean#L111). The attribute's comment: “the localization argument of the source's proof, closed over an open cover: for an arbitrary morphism of schemes and arbitrary complexes, invertibility of the projection-formula map for f|\_U at the restricted complexes, for U running through an open cover of the base, implies invertibility of the map for f; the affine case of the tag is NOT proved here, so the tag is not closed”.

> **The projection-formula morphism of [Stacks, Tag 0B53] is invertible as soon as it is after
> restriction to the members of an open cover of the base.**
>
> For an arbitrary morphism of schemes `f : X ⟶ Y`, arbitrary `E ∈ D(𝒪_X)` and `K ∈ D(𝒪_Y)`, and a
> family of opens `U i` covering `Y`: if the projection-formula map for the restricted morphism
> `f|_{U_i} : f^{-1}U_i ⟶ U_i` at the restricted complexes `Lg_i'^*E` and `Lg_i^*K` is invertible
> for every `i`, then the projection-formula map for `f` at `E` and `K` is invertible.
>
> This is the localization argument of the proof of [Stacks, Tag 08EU], over an open cover of the
> base.

```lean
theorem isIso_projectionFormulaMap_of_openCover {ι : Type*} (U : ι → Y.Opens)
    (hU : ∀ y : Y, ∃ i, y ∈ U i)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (h : ∀ i, IsIso (projectionFormulaMap (f ∣_ U i).toLRSHom.toShHom
      ((derivedPullback (f ⁻¹ᵁ U i).ι.toLRSHom.toShHom).obj E)
      ((derivedPullback (U i).ι.toLRSHom.toShHom).obj K))) :
    IsIso (projectionFormulaMap f.toLRSHom.toShHom E K)
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_derivedPullback_map_projectionFormulaMap_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ProjectionFormulaOpenImmersionBaseChange.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ProjectionFormulaOpenImmersionBaseChange.lean#L262). The attribute's comment: “the localization step of the source's proof, for schemes: for a Cartesian square of schemes whose bottom arrow is an open immersion, invertibility of the projection-formula map for f' at the restricted complexes implies invertibility of the derived pullback along g of the map for f; unconditional in both complexes, but only one implication of the source's reduction — the affine case and the descent from an open cover back to the base are not proved”.

> **Invertibility of the derived projection-formula map of [Stacks, Tag 0B53] descends along an
> open immersion of the base, for schemes.**
>
> For a Cartesian square of schemes whose bottom arrow `g` is an open immersion, the derived
> pullback along `g` of the projection-formula map for `f` is invertible as soon as the map for `f'`
> at the restricted complexes is.
>
> The other horizontal arrow `g'` is then an open immersion too, being a base change of `g`, and
> the square stays Cartesian in ringed spaces by
> `Stacks.Cohomology.DerivedBaseChange.isPullback_toShHom_of_isOpenImmersion`, so
> `Stacks.Cohomology.ProjectionFormulaPerfect.isIso_derivedPullback_map_projectionFormulaMap`
> applies.  This is the form the source's
> localization argument is run in: it replaces the base `Y` by an open `V ⊆ Y` and `X` by its
> preimage.

```lean
theorem isIso_derivedPullback_map_projectionFormulaMap_of_isOpenImmersion
    [AlgebraicGeometry.IsOpenImmersion g] (sq : IsPullback g' f' f g)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (h : IsIso (projectionFormulaMap f'.toLRSHom.toShHom
      ((derivedPullback g'.toLRSHom.toShHom).obj E)
      ((derivedPullback g.toLRSHom.toShHom).obj K))) :
    IsIso ((derivedPullback g.toLRSHom.toShHom).map
      (projectionFormulaMap f.toLRSHom.toShHom E K))
```

**`AlgebraicGeometry.projectionFormulaIsIsoOnQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/ProjectionFormulaDischarged.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/ProjectionFormulaDischarged.lean#L46). The attribute's comment: “the whole tag, in the shape of the proposition AlgebraicGeometry.ProjectionFormulaIsIsoOnQuasicoherent, which this proves”.

> **[Stacks, Tag 08EU].** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> schemes. For `E` in `D_QCoh(𝒪_X)` and `K` in `D_QCoh(𝒪_Y)` the projection-formula morphism of
> [Stacks, Tag 0B53]
>
> `R f_* E ⊗^𝐋_{𝒪_Y} K ⟶ R f_*(E ⊗^𝐋_{𝒪_X} L f^* K)`
>
> is an isomorphism; that is, `AlgebraicGeometry.ProjectionFormulaIsIsoOnQuasicoherent` holds.

```lean
theorem projectionFormulaIsIsoOnQuasicoherent :
    ProjectionFormulaIsIsoOnQuasicoherent.{u}
```

**`Stacks.Cohomology.ProjectionFormulaDevissage.isIso_projectionFormulaMap_twoOutOfThree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaDevissage.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaDevissage.lean#L138). The attribute's comment: “the triangle step of the source's dévissage, with no hypothesis: for a distinguished triangle of D(𝒪\_Y), invertibility of the Tag 0B53 map at all shifts of two of the three vertices gives it at all shifts of the third, in each of the three rotations. The source states this as `two out of three of the functors being exact`; the direct-sum step is isIso\_projectionFormulaMap\_coproduct and the affine reduction is isIso\_projectionFormulaMap\_of\_derivedModuleFunctor, both of which carry a geometric input and so are not registered”.

> Let `Δ` be a distinguished triangle of `D(𝒪_Y)`. If the projection-formula morphism of
> [Stacks, Tag 0B53] is invertible at every shift of two of the three vertices of `Δ`, it is
> invertible at every shift of the third, in each of the three rotations.

```lean
theorem isIso_projectionFormulaMap_twoOutOfThree
    (Δ : Triangle (DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))))
    (hΔ : Δ ∈ distTriang _) :
    ((∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₁⟦n⟧))) →
        (∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₂⟦n⟧))) →
        ∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₃⟦n⟧))) ∧
      ((∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₁⟦n⟧))) →
        (∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₃⟦n⟧))) →
        ∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₂⟦n⟧))) ∧
      ((∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₂⟦n⟧))) →
        (∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₃⟦n⟧))) →
        ∀ n : ℤ, IsIso (projectionFormulaMap f E (Δ.obj₁⟦n⟧)))
```

**`Stacks.Cohomology.ProjectionFormulaGeneralBase.isIso_projectionFormulaMap_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaGeneralBase.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaGeneralBase.lean#L177). The attribute's comment: “the tag in full: for a quasi-compact quasi-separated morphism of schemes f : X ⟶ Y, an E in D\_QCoh(𝒪\_X) and a K in D\_QCoh(𝒪\_Y), the Tag 0B53 map Rf\_*E ⊗ᴸ K ⟶ Rf\_*(E ⊗ᴸ Lf^*K) is invertible, with no hypothesis beyond those. The source's first step, that invertibility is a local question on Y, is carried out here: over an affine open V ⊆ Y the square of Tag 0B6B identifies L((V).ι)^* of the map with the map for the base change f ∣\_ V, every other arrow of that square being invertible because (V).ι is an open immersion; the map for f ∣\_ V is the affine case; and invertibility in D(𝒪\_Y) is local on the affine opens of Y”.

> **[Stacks, Tag 08EU].**  For a quasi-compact quasi-separated morphism of schemes
> `f : X ⟶ Y`, an `E` in `D_QCoh(𝒪_X)` and a `K` in `D_QCoh(𝒪_Y)`, the projection-formula
> morphism `Rf_*E ⊗^𝐋_{𝒪_Y} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*K)` of [Stacks, Tag 0B53] is invertible.

```lean
theorem isIso_projectionFormulaMap_of_isQuasicoherent {X Y : Scheme.{u}} (f : X ⟶ Y)
    [AlgebraicGeometry.QuasiCompact f] [AlgebraicGeometry.QuasiSeparated f]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hE : quasicoherentDerivedProperty X E)
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (hK : quasicoherentDerivedProperty Y K) :
    IsIso (projectionFormulaMap f.toLRSHom.toShHom E K)
```

**`Stacks.Cohomology.ProjectionFormulaOverAffineBase.isIso_projectionFormulaMap_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaOverAffineBase.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaOverAffineBase.lean#L253). The attribute's comment: “the affine case, with no hypothesis beyond the tag's own: for a quasi-compact quasi-separated morphism of schemes g : X ⟶ Spec A, an E in D\_QCoh(𝒪\_X) and a K in D\_QCoh(𝒪\_\{Spec A}), the Tag 0B53 map Rg\_*E ⊗ᴸ K ⟶ Rg\_*(E ⊗ᴸ Lg^*K) is invertible. This is the source's dévissage carried out — direct sums (Tag 08DZ), distinguished triangles, and the reduction to the shifts of the structure sheaf through the equivalence D(A) ≌ D\_QCoh(𝒪\_\{Spec A}) of Tag 06Z0 and the remark of Tag 09PB. This is the tag over a base of the form Spec A; the source's first step, the reduction of a general base Y to an affine one, is carried out in Stacks.Cohomology.ProjectionFormulaGeneralBase, where the tag is registered in full”.

> Let `g : X ⟶ Spec A` be a quasi-compact and quasi-separated morphism of schemes, let `E` be
> an object of `D_QCoh(𝒪_X)` and let `K` be an object of `D_QCoh(𝒪_{Spec A})`. Then the
> projection-formula morphism
>
> `Rg_*E ⊗^𝐋_{𝒪_{Spec A}} K ⟶ Rg_*(E ⊗^𝐋_{𝒪_X} Lg^*K)`
>
> is an isomorphism.

```lean
theorem isIso_projectionFormulaMap_of_isQuasicoherent
    [AlgebraicGeometry.QuasiCompact g] [AlgebraicGeometry.QuasiSeparated g]
    (E : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hE : quasicoherentDerivedProperty X E)
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      (structureSheafRing (Spec A).toRingedSpace)))
    (hK : quasicoherentDerivedProperty (Spec A) K) :
    IsIso (projectionFormulaMap g.toLRSHom.toShHom E K)
```

**`Stacks.Cohomology.ProjectionFormulaPerfect.isIso_derivedPullback_map_projectionFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaPerfect.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaPerfect.lean#L218). The attribute's comment: “the localization step of the source's proof: for a Cartesian square of ringed spaces whose horizontal arrows are open immersions, invertibility of the projection-formula map for f' at the restricted complexes implies invertibility of the derived pullback along g of the map for f; unconditional in both complexes, but only one implication of the source's reduction — the affine case and the passage from an open cover back to the base are not proved”.

> **The projection-formula morphism of [Stacks, Tag 0B53] is invertible after derived pullback
> along an open immersion of the base, as soon as it is invertible upstairs.**
>
> Let
>
> ```
>           g'
>    X' ----------→ X
>    |              |
> f' |              | f
>    v      g       v
>    Y' ----------→ Y
> ```
>
> be a Cartesian square of ringed spaces whose horizontal arrows `g` and `g'` are open immersions,
> and let `E ∈ D(𝒪_X)`, `K ∈ D(𝒪_Y)`.  If the projection-formula morphism for `f'` at
> `L(g')^*E` and `Lg^*K` is invertible, then `Lg^*` of the projection-formula morphism for `f` at
> `E` and `K` is invertible.
>
> This is [Stacks, Tag 0B6B] read for invertibility.  Of the six arrows of that square, five are
> invertible here — the two comparisons of [Stacks, Tag 079U] because they are components of
> `Stacks.Cohomology.DerivedPullbackTensor.derivedPullbackTensorIso`, the two derived base-change
> maps by
> `Stacks.Cohomology.DerivedBaseChange.isIso_derivedBaseChangeMap_of_isOpenImmersions`, and the
> projection-formula morphism for `f'` by hypothesis — so the sixth, `Lg^*` of the
> projection-formula morphism for `f`, is invertible too.
>
> There is no boundedness, flatness, quasi-coherence or perfectness hypothesis on `E` or `K`.

```lean
theorem isIso_derivedPullback_map_projectionFormulaMap
    [SheafedSpace.IsOpenImmersion g'] [SheafedSpace.IsOpenImmersion g]
    (sq : IsPullback g' f' f g)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (h : IsIso (projectionFormulaMap f' ((derivedPullback g').obj E)
      ((derivedPullback g).obj K))) :
    IsIso ((derivedPullback g).map (projectionFormulaMap f E K))
```

**`Stacks.Cohomology.ProjectionFormulaQCoh.isIso_projectionFormulaMap_of_isDQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaQCoh.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaQCoh.lean#L89). The attribute's comment: “the whole lemma: for a quasi-compact and quasi-separated morphism of schemes f : X ⟶ Y, E in D\_QCoh(𝒪\_X) and K in D\_QCoh(𝒪\_Y), the projection-formula morphism Rf\_*E ⊗ᴸ K ⟶ Rf\_*(E ⊗ᴸ Lf^*K) of Tag 0B53 is invertible. The proof is the source's dévissage: locality on Y, the affine equivalence D(A) ≌ D\_QCoh(𝒪\_Y) of Tag 06Z0 with the resolution of Tag 09PB, direct sums through Tag 08DZ, two-out-of-three on distinguished triangles, and the shifts of the structure sheaf as the base case”.

> **[Stacks, Tag 08EU].**  For a quasi-compact and quasi-separated morphism of schemes
> `f : X ⟶ Y`, an `E` in `D_QCoh(𝒪_X)` and a `K` in `D_QCoh(𝒪_Y)`, the projection-formula morphism
> of [Stacks, Tag 0B53]
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*K)`
>
> is an isomorphism.
>
> The hypotheses are the source's and no others: quasi-compactness and quasi-separatedness of `f`,
> and quasi-coherence of the cohomology sheaves of `E` and of `K`.  No boundedness, no flatness,
> no perfectness, no affineness, no Noetherian or separatedness assumption, and no choice of model
> for either derived category beyond the one the whole file works in.

```lean
theorem isIso_projectionFormulaMap_of_isDQCoh {X Y : Scheme.{u}} (f : X ⟶ Y)
    [QuasiCompact f] [QuasiSeparated f]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (hE : Stacks.DerivedQCoh.IsDQCoh (R := structureSheafRing X.toRingedSpace) E)
    (hK : Stacks.DerivedQCoh.IsDQCoh (R := structureSheafRing Y.toRingedSpace) K) :
    IsIso (projectionFormulaMap f.toLRSHom.toShHom E K)
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_quasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaQuasiCoherent.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaQuasiCoherent.lean#L183).

> **[Stacks, Tag 08EU].**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> schemes.  For `E` in `D_QCoh(𝒪_X)` and `K` in `D_QCoh(𝒪_Y)` the projection-formula morphism of
> [Stacks, Tag 0B53]
>
> `R f_* E ⊗^𝐋_{𝒪_Y} K ⟶ R f_*(E ⊗^𝐋_{𝒪_X} L f^* K)`
>
> is an isomorphism.
>
> Invertibility is local on `Y`, the affine opens cover `Y`, and over an affine open the statement
> is `isIso_projectionFormulaMap_of_isAffine`.

```lean
theorem isIso_projectionFormulaMap_quasiCoherent
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (hK : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)) j).obj K).IsQuasicoherent) :
    IsIso (projectionFormulaMap f.toLRSHom.toShHom E K)
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_unitObject_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaUnitKFlat.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaUnitKFlat.lean#L550). The attribute's comment: “the case K = 𝒪\_Y[0]: for an arbitrary morphism of ringed spaces f and an arbitrary E in D(𝒪\_X), the projection-formula morphism Rf\_*E ⊗ᴸ 𝒪\_Y ⟶ Rf\_*(E ⊗ᴸ Lf^*𝒪\_Y) is invertible; the right unitors are derivedTensorRightUnitorNatIso, the unit comparison is derivedPullbackUnitIso and the right-unitor coherence of Tag 079U is rightUnitorCoherence\_unitObject”.

> **[Stacks, Tag 08EU] at `K = 𝒪_Y[0]`.**  For an arbitrary
> morphism of ringed spaces `f : X ⟶ Y` and an arbitrary `E` in `D(𝒪_X)`, the derived
> projection-formula morphism
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} 𝒪_Y ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*𝒪_Y)`
>
> is an isomorphism.
>
> This is the base case of the source's dévissage for [Stacks, Tag 08EU].  The inputs of
> `isIso_projectionFormulaMap_unitObject` are: the two right unitors and the
> naturality of the one on `X` by `Stacks.RingedSpace.derivedTensorRightUnitorNatIso`, the unit
> comparison by `derivedPullbackUnitIso`, and the right-unitor coherence of [Stacks, Tag 079U] by
> `rightUnitorCoherence_unitObject`.

```lean
theorem isIso_projectionFormulaMap_unitObject_unconditional
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    IsIso (projectionFormulaMap f E (singleUnit Y))
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_unitShift_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaUnitShifts.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaUnitShifts.lean#L224). The attribute's comment: “the case K = 𝒪\_Y[0]⟦m⟧, every shift of the structure sheaf: for an arbitrary morphism of ringed spaces and an arbitrary E in D(𝒪\_X), Rf\_*E ⊗ᴸ 𝒪\_Y[0]⟦m⟧ ⟶ Rf\_*(E ⊗ᴸ Lf^*(𝒪\_Y[0]⟦m⟧)) is invertible for every integer m”.

> **[Stacks, Tag 08EU] at `K = 𝒪_Y[0]⟦m⟧`, for every integer `m`.**
> For an arbitrary morphism of ringed spaces `f : X ⟶ Y` and an arbitrary `E ∈ D(𝒪_X)`, the derived
> projection-formula morphism of [Stacks, Tag 0B53]
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} 𝒪_Y[0]⟦m⟧ ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*(𝒪_Y[0]⟦m⟧))`
>
> is an isomorphism.
>
> This is the case the source's proof calls clear — "the statement of the lemma is clear for shifts
> of the structure sheaf" — and it is the whole base case of the source's dévissage in `K`.  At
> `m = 0` it is the case `K = 𝒪_Y[0]` of [Stacks, Tag 08EU] up to the isomorphism `Z⟦0⟧ ≅ Z`.
>
> The morphism `f` is an arbitrary morphism of ringed spaces and `E` is arbitrary.

```lean
theorem isIso_projectionFormulaMap_unitShift_unconditional
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) (m : ℤ) :
    IsIso (projectionFormulaMap f E ((singleUnit Y)⟦m⟧))
```

## Tag 08IA, a definition

[Tag 08IA](https://stacks.math.columbia.edu/tag/08IA) in the Stacks Project.

**`AlgebraicGeometry.TorIndependent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorIndependence.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TorIndependence.lean#L101). References: SGA 6 III (1.5); SGA 5 III (6.2).

> Two schemes over a common base are Tor independent if their local rings at
> every pair of points with the same image are Tor independent over the local
> ring of the base.

```lean
def TorIndependent {S X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) : Prop
```

## Tag 0FXV, a lemma

[Tag 0FXV](https://stacks.math.columbia.edu/tag/0FXV) in the Stacks Project.

**`AlgebraicGeometry.torIndependent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TorIndependence.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TorIndependence.lean#L430). References: SGA 6 III (1.5), “affine/local criterion”.

> Tor independence of two schemes over a base can be checked on every
> compatible triple of affine opens, or on affine open coverings of the base and
> of the two inverse images.

```lean
theorem torIndependent_tfae {S X Y : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) :
    List.TFAE [
      TorIndependent f g,
      ∀ (U : X.Opens) (_ : IsAffineOpen U)
        (V : Y.Opens) (_ : IsAffineOpen V)
        (W : S.Opens) (_ : IsAffineOpen W)
        (hUW : U ≤ f ⁻¹ᵁ W) (hVW : V ≤ g ⁻¹ᵁ W),
        letI : Algebra Γ(S, W) Γ(X, U) := (f.appLE W U hUW).hom.toAlgebra
        letI : Algebra Γ(S, W) Γ(Y, V) := (g.appLE W V hVW).hom.toAlgebra
        Algebra.TorIndependent Γ(S, W) Γ(X, U) Γ(Y, V),
      ∃ (I : Type u) (W : I → S.Opens),
        ((⨆ i, W i) = ⊤) ∧
          ((∀ i, IsAffineOpen (W i)) ∧
            ∀ i, ∃ (J : Type u) (U : J → X.Opens)
              (hU : (⨆ j, U j) = f ⁻¹ᵁ W i),
              (∀ j, IsAffineOpen (U j)) ∧
                ∃ (K : Type u) (V : K → Y.Opens)
                  (hV : (⨆ k, V k) = g ⁻¹ᵁ W i),
                  (∀ k, IsAffineOpen (V k)) ∧
                    ∀ j k,
                      let hUW : U j ≤ f ⁻¹ᵁ W i := (le_iSup U j).trans hU.le
                      let hVW : V k ≤ g ⁻¹ᵁ W i := (le_iSup V k).trans hV.le
                      letI : Algebra Γ(S, W i) Γ(X, U j) :=
                        (f.appLE (W i) (U j) hUW).hom.toAlgebra
                      letI : Algebra Γ(S, W i) Γ(Y, V k) :=
                        (g.appLE (W i) (V k) hVW).hom.toAlgebra
                      Algebra.TorIndependent
                        Γ(S, W i) Γ(X, U j) Γ(Y, V k))]
```

## Tag 0FXW, a lemma

[Tag 0FXW](https://stacks.math.columbia.edu/tag/0FXW) in the Stacks Project.

**`AlgebraicGeometry.torIndependent_pullback_of_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BaseChangeFour/FlatBaseChange.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BaseChangeFour/FlatBaseChange.lean#L55).

> Tor independence of two schemes over a common base is preserved by a flat base change.

```lean
lemma torIndependent_pullback_of_flat
    {S X Y S' : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) (s : S' ⟶ S)
    [Flat s] (h : TorIndependent f g) :
    TorIndependent (pullback.snd f s) (pullback.snd g s)
```

## Tag 08IB, a lemma

[Tag 08IB](https://stacks.math.columbia.edu/tag/08IB) in the Stacks Project.

**`AlgebraicGeometry.BaseChangeChart.isIso_derivedBaseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparison.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/AffineChartComparison.lean#L194). The attribute's comment: “the Tor-independence input of the proof: on every Cartesian affine-open chart of the square the coordinate rings are Tor independent, so the ring-level derived base-change comparison of Stacks 065Z is invertible there. The global statement is isIso\_derivedBaseChangeMap\_of\_torIndependent”.

> **Stacks 0661 on a Cartesian affine-open chart.** If `X` and `S'` are Tor independent over
> `S`, then for every chart the canonical comparison
>
> `K ⊗ᴸ_R R' ⟶ K ⊗ᴸ_A A'`
>
> of Stacks 065Z is an isomorphism on the whole unbounded derived category of `A`-modules, for
> every choice of models of the two total derived extension-of-scalars functors.
>
> The pushout hypothesis of Stacks 0661 is the chart's own square `A' = A ⊗_R R'`, and the Tor
> independence hypothesis is `AlgebraicGeometry.BaseChangeChart.torIndependent`.
>
> This is the Tor-independence input of Stacks 08IB, not its conclusion: it does not say that the
> derived base-change map `Lg^*Rf_*K ⟶ Rf'_*L(g')^*K` of Stacks 08HY is an isomorphism. Passing
> from the chartwise comparison to that map is Stacks 0DJ9.

```lean
public theorem isIso_derivedBaseChangeComparison (hTor : TorIndependent f g)
    (ch : BaseChangeChart f g f' g')
    (L_g : DerivedCategory (ModuleCat.{u} ch.R) ⥤ DerivedCategory (ModuleCat.{u} ch.R'))
    (L_h : DerivedCategory (ModuleCat.{u} ch.A) ⥤ DerivedCategory (ModuleCat.{u} ch.A'))
    (alpha_g : DerivedCategory.Q ⋙ L_g ⟶
      (ModuleCat.extendScalars.{u, u, u} ch.b.hom).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q)
    (alpha_h : DerivedCategory.Q ⋙ L_h ⟶
      (ModuleCat.extendScalars.{u, u, u} ch.c.hom).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q)
    [L_g.IsLeftDerivedFunctor alpha_g
      (HomologicalComplex.quasiIso (ModuleCat.{u} ch.R) (ComplexShape.up ℤ))]
    [L_h.IsLeftDerivedFunctor alpha_h
      (HomologicalComplex.quasiIso (ModuleCat.{u} ch.A) (ComplexShape.up ℤ))] :
    IsIso (RingTheory.TorIndependence.derivedBaseChangeComparison.{u, u, u, u, u}
      ch.a.hom ch.b.hom ch.c.hom ch.d.hom ch.isPushout_hom L_g L_h alpha_g alpha_h).2.1
```

**`AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/BaseChangeUnitSingle.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/BaseChangeUnitSingle.lean#L285). References: SGA 6 IV (3.1.0), “more general”.

> **[Stacks, Tag 08IB].**  Let
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> be a Cartesian square of schemes with `f` quasi-compact and quasi-separated and `X` and `S'` Tor
> independent over `S`, and let `K` be an object of `D(𝒪_X)` with quasi-coherent cohomology
> sheaves.  Then the derived base-change map
>
> `Lg^*(Rf_*K) ⟶ Rf'_*(L(g')^*K)`
>
> of [Stacks, Tag 08HY] is an isomorphism.
>
> `AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent_of_overAffineBase` — the source's
> reduction to an affine base — at `derivedBaseChangeIsIsoOverAffineBase`.

```lean
theorem derivedBaseChangeIsIsoOnQuasicoherent : DerivedBaseChangeIsIsoOnQuasicoherent.{u}
```

**`AlgebraicGeometry.isIso_derivedBaseChangeMap_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TorIndependentBaseChange.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/TorIndependentBaseChange.lean#L55).

> Let `g : S' ⟶ S` be a morphism of schemes, `f : X ⟶ S` quasi-compact and quasi-separated,
> and `X' = X ×_S S'` with projections `g' : X' ⟶ X` and `f' : X' ⟶ S'`. If `X` and `S'` are Tor
> independent over `S`, then for every `E ∈ D_QCoh(𝒪_X)` the canonical arrow
> `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` is an isomorphism.

```lean
theorem isIso_derivedBaseChangeMap_of_torIndependent (sq : IsPullback g' f' f g) [QuasiCompact f]
    [QuasiSeparated f] (hTor : TorIndependent f g)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toSheafedSpace)))
    (hE : ∀ n : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) n).obj E).IsQuasicoherent) :
    IsIso (derivedBaseChangeMap g'.toLRSHom.toShHom f'.toLRSHom.toShHom f.toLRSHom.toShHom
      g.toLRSHom.toShHom (comp_toShHom_of_comm sq.w) E)
```

**`Stacks.Duality.OpenImmersion.isIso_quasiCoherentDerivedBaseChangeSquare_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean#L401). The attribute's comment: “for base change along an OPEN IMMERSION of the base, hence flat, hence Tor independent of f: invertibility of Stacks.Duality.quasiCoherentDerivedBaseChangeSquare, the derived base change map of Stacks 08HY on the quasi-coherent derived categories at the locally small model. The general Tor-independent case is not proved in this repository; see Stacks.Duality.OpenImmersion.isIso\_twistedInverseImagePushforwardBaseChange\_of\_isOpenImmersion”.

> **[Stacks, Tag 08IB] for base change along an open immersion of the base**, on the
> quasi-coherent derived categories at the locally small model: the derived base change map
> `β : Rf_* ⋙ Lj^* ⟶ L(j')^* ⋙ Rf'_*` of [Stacks, Tag 08HY] is invertible.
>
> This is the companion of
> `isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion` under
> `Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_iff`, and it is the localization
> step of [Stacks, Tag 0DJ9] at this model — `β` here is the mate of
> `Stacks.Duality.quasiCoherentDerivedPushforwardSquareIso`, not the comparison of
> `Stacks.Duality.OpenImmersion.quasiCoherentDerivedRestrictBaseChangeSquare`, so nothing identifies
> derived pullback with the exact restriction along the way.

```lean
theorem isIso_quasiCoherentDerivedBaseChangeSquare_of_isOpenImmersion
    [(Stacks.Duality.quasiCoherentDerivedPushforward f hpushf).IsLeftAdjoint]
    [(Stacks.Duality.quasiCoherentDerivedPushforward f' hpushf').IsLeftAdjoint]
    (sq : IsPullback j' f' f j) :
    IsIso (Stacks.Duality.quasiCoherentDerivedBaseChangeSquare j' f' f j hpushj' hpushf hpushf'
      hpushj (Stacks.Duality.isQuasicoherent_homology_derivedPullback' j)
      (Stacks.Duality.isQuasicoherent_homology_derivedPullback' j') sq.w)
```

## Tag 0AA7, a lemma

[Tag 0AA7](https://stacks.math.columbia.edu/tag/0AA7) in the Stacks Project.

**`AlgebraicGeometry.GlobalHomBaseChange.isIso_globalHomBaseChangeMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean#L505). The attribute's comment: “case (1): M perfect and K in D\_QCoh(O\_X)”.

> **Stacks 0AA7, case (1).**  Let `X' --g'--> X`, `f : X ⟶ Spec R`, `f' : X' ⟶ Spec R'` be a
> cartesian square over `Spec φ : Spec R' ⟶ Spec R`, with `f` quasi-compact and quasi-separated and
> `X`, `Spec R'` Tor independent over `Spec R`.  For `M` perfect and `K ∈ D_QCoh(𝒪_X)` the canonical
> map `R Hom_X(M, K) ⊗^𝐋_R R' ⟶ R Hom_{X'}(L(g')^*M, L(g')^*K)` of `D(R')` is an isomorphism.

```lean
theorem isIso_globalHomBaseChangeMap_of_isPerfect (hsq : IsPullback g' f' f (Spec.map φ))
    [QuasiCompact f] [QuasiSeparated f] (hTor : TorIndependent f (Spec.map φ))
    (M K : DerivedCategory X.Modules)
    (hM : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) M)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj K).IsQuasicoherent) :
    IsIso (globalHomBaseChangeMap φ f f' g' hsq.w M K)
```

**`AlgebraicGeometry.GlobalHomBaseChange.isIso_globalHomBaseChangeMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean#L521). The attribute's comment: “case (2): M pseudo-coherent, K in D^+\_QCoh(O\_X), R' of finite tor dimension over R”.

> **Stacks 0AA7, case (2).**  Let `X' --g'--> X`, `f : X ⟶ Spec R`, `f' : X' ⟶ Spec R'` be a
> cartesian square over `Spec φ : Spec R' ⟶ Spec R`, with `f` quasi-compact and quasi-separated and
> `X`, `Spec R'` Tor independent over `Spec R`.  If `M` is pseudo-coherent, `K ∈ D^+_QCoh(𝒪_X)` and
> `R'` has finite Tor dimension over `R`, the canonical map
> `R Hom_X(M, K) ⊗^𝐋_R R' ⟶ R Hom_{X'}(L(g')^*M, L(g')^*K)` of `D(R')` is an isomorphism.

```lean
theorem isIso_globalHomBaseChangeMap_of_isPseudoCoherent (hsq : IsPullback g' f' f (Spec.map φ))
    [QuasiCompact f] [QuasiSeparated f] (hTor : TorIndependent f (Spec.map φ))
    (M K : DerivedCategory X.Modules)
    (hM : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) M)
    (hK : DerivedCategoryB.derivedCategoryBPlus (SheafOfModules.isQuasicoherent X.ringCatSheaf) K)
    (hR' : StacksDraft.TorAmplitude.HasFiniteTorDimensionCanonical R (algebraComplex R R' φ)) :
    IsIso (globalHomBaseChangeMap φ f f' g' hsq.w M K)
```

## Tag 0BZA, a remark

[Tag 0BZA](https://stacks.math.columbia.edu/tag/0BZA) in the Stacks Project.

**`AlgebraicGeometry.GlobalHomBaseChange.isIso_globalHomAdjunctionMap_and_globalHomBaseChangeMap_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalHomBaseChangeIso.lean#L639).

> **Stacks 0BZA.**  With notation as in Stacks 0AA7, the square
>
> ```
> R Hom_X(M, Rg'_*L) ⊗^𝐋_R R' ----> R Hom_{X'}(L(g')^*M, L(g')^*Rg'_*L)
>         |  μ                                   |  a
>         v                                      v
> R Hom_X(M, Rg'_*L)  ===========  R Hom_{X'}(L(g')^*M, L)
> ```
>
> commutes, and its bottom map is the canonical identification.  The bottom map
> `R Hom_X(M, Rg'_*L) ⟶ R Hom_{X'}(L(g')^*M, L)` of `D(R)` (`globalHomAdjunctionMap`) is an
> isomorphism: it is `RΓ(X, -)` of the derived adjunction isomorphism
> `R𝓗om(M, Rg'_*L) ≅ Rg'_*R𝓗om(L(g')^*M, L)` followed by `RΓ(X, Rg'_* -) = RΓ(X', -)`.  The square
> says that the map of Stacks 0AA7 at `K = Rg'_*L` followed by the map `a` induced by the counit
> `L(g')^*Rg'_*L ⟶ L` is the multiplication map `μ`, the counit `K' ⊗^𝐋_R R' ⟶ K'` of the
> adjunction between `- ⊗^𝐋_R R'` and restriction of scalars at `K' = R Hom_{X'}(L(g')^*M, L)`, read
> through that identification.  Both hold for every commutative square over `Spec R' ⟶ Spec R`.

```lean
theorem isIso_globalHomAdjunctionMap_and_globalHomBaseChangeMap_comp_counit
    (M : DerivedCategory X.Modules) (L : DerivedCategory X'.Modules) :
    IsIso (globalHomAdjunctionMap φ f f' g' w M L) ∧
      globalHomBaseChangeMap φ f f' g' w M ((derivedPushforward g'.toLRSHom.toShHom).obj L) ≫
          (linearSections f').map
            (((Stacks.SheafOfModules.derivedSheafHom X'.toRingedSpace.sheaf).obj
              (op ((derivedPullback g'.toLRSHom.toShHom).obj M))).map
              ((derivedAdjunction g'.toLRSHom.toShHom).counit.app L)) =
        (derivedExtendScalars φ).map (globalHomAdjunctionMap φ f f' g' w M L) ≫
          (derivedExtendScalarsAdjunction φ).counit.app
            (globalHom f' ((derivedPullback g'.toLRSHom.toShHom).obj M) L)
```

## Tag 0C0V, a lemma

[Tag 0C0V](https://stacks.math.columbia.edu/tag/0C0V) in the Stacks Project.

**`AlgebraicGeometry.derivedPullback_hasTorAmplitudeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeTorAmplitudeBaseChange.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeTorAmplitudeBaseChange.lean#L223). The attribute's comment: “preservation of Tor amplitude over the base”. References: SGA 6 III (3.5.2); SGA 6 III (4.7.2), “amplitude inclusion”.

> **Stacks 0C0V (1).** For a cartesian square of schemes whose two morphisms to the base are
> Tor independent, derived pullback preserves Tor amplitude over the base.

```lean
public theorem derivedPullback_hasTorAmplitudeOver
    {X' X S' S : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ S')
    (f : X ⟶ S) (g : S' ⟶ S) (hpb : IsPullback g' f' f g)
    (htor : TorIndependent f g) (E : DerivedCategory X.Modules) (a b : ℤ)
    (hE : HasTorAmplitudeOver f E a b) :
    HasTorAmplitudeOver f'
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        g'.toLRSHom.toShHom).obj E) a b
```

**`AlgebraicGeometry.derivedPullbackComparison_isIso_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeTorAmplitudeBaseChange.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RelativeTorAmplitudeBaseChange.lean#L408). The attribute's comment: “derived pullback of a module flat over the base is the ordinary pullback”.

> **Stacks 0C0V (2).** For a Tor-independent cartesian square of schemes and an `𝒪_X`-module
> `G` flat over `S`, the canonical comparison from the derived pullback of `G` along `g'` to its
> ordinary pullback is an isomorphism.

```lean
public theorem derivedPullbackComparison_isIso_of_isFlatOver
    {X' X S' S : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ S')
    (f : X ⟶ S) (g : S' ⟶ S) (hpb : IsPullback g' f' f g)
    (htor : TorIndependent f g) (G : X.Modules) (hG : IsFlatOver f.toLRSHom.toShHom G) :
    IsIso ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullbackComparison
      g'.toLRSHom.toShHom).app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj
        ((CochainComplex.singleFunctor X.Modules 0).obj G)))
```

## Tag 0E23, a lemma

[Tag 0E23](https://stacks.math.columbia.edu/tag/0E23) in the Stacks Project.

**`Stacks.Cohomology.ClosedImmersionBaseChange.isIso_derivedBaseChangeSquare_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeMergeCoherence.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeMergeCoherence.lean#L275). The attribute's comment: “the canonical base change map Lf^* ∘ Ri\_* ⟶ Ri'\_* ∘ Lg^* is invertible”.

> In a cartesian square of schemes with `i` a closed immersion and `Z`, `X'` Tor independent
> over `X`, the canonical morphism of functors `Ri_* ⋙ Lf^* ⟶ Lg^* ⋙ Ri'_*` of Stacks 08HY is an
> isomorphism.

```lean
theorem isIso_derivedBaseChangeSquare_of_torIndependent (sq : IsPullback i' g f i)
    [AlgebraicGeometry.IsClosedImmersion i] (htor : AlgebraicGeometry.TorIndependent i f) :
    IsIso (derivedBaseChangeSquare g.toLRSHom.toShHom i'.toLRSHom.toShHom i.toLRSHom.toShHom
      f.toLRSHom.toShHom (comp_toShHom_of_isPullback sq))
```

**`Stacks.Cohomology.ClosedImmersionBaseChange.derivedBaseChangeSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeMergeCoherence.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeMergeCoherence.lean#L300).

> **Tor-independent base change along a closed immersion.**  For a cartesian square with `i` a
> closed immersion and `Z`, `X'` Tor independent over `X`, the functors `Lf^* ∘ Ri_*` and
> `Ri'_* ∘ Lg^*` from `D(𝒪_Z)` to `D(𝒪_{X'})` are isomorphic, by the canonical derived base change
> map of Stacks 08HY.

```lean
def derivedBaseChangeSquareIso (sq : IsPullback i' g f i)
    [AlgebraicGeometry.IsClosedImmersion i] (htor : AlgebraicGeometry.TorIndependent i f) :
    Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward i.toLRSHom.toShHom ⋙
        Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f.toLRSHom.toShHom ≅
      Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g.toLRSHom.toShHom ⋙
        Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
          i'.toLRSHom.toShHom
```

**`Stacks.Cohomology.ClosedImmersionBaseChange.derivedBaseChangeSquareAsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeTorIndependent.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/ClosedImmersionBaseChangeTorIndependent.lean#L406). The attribute's comment: “Lf^* ∘ Ri\_* ≅ Ri'\_* ∘ Lg^* on D(𝒪\_Z), by the canonical base change map”.

> **Tor-independent base change along a closed immersion.**  For a cartesian square of schemes
> with `i` a closed immersion and `Z`, `X'` Tor independent over `X`, the functors `Lf^* ∘ Ri_*` and
> `Ri'_* ∘ Lg^*` from `D(𝒪_Z)` to `D(𝒪_{X'})` are isomorphic, by the canonical derived base change
> map of Stacks 08HY.

```lean
def derivedBaseChangeSquareAsIso (sq : IsPullback i' g f i)
    [AlgebraicGeometry.IsClosedImmersion i] (htor : AlgebraicGeometry.TorIndependent i f) :
    derivedPushforward i.toLRSHom.toShHom ⋙ derivedPullback f.toLRSHom.toShHom ≅
      derivedPullback g.toLRSHom.toShHom ⋙ derivedPushforward i'.toLRSHom.toShHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.22, Tag 08ET](https://stacks.math.columbia.edu/tag/08ET)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
