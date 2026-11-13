---
declaration: section
origin: cited
lean: Stacks.Chow.specializationMap, Stacks.Chow.topologicalKrullDim_supp_fiberModule_closedPoint_le, Stacks.Chow.specializationCycle_familyAssociatedToModule, Stacks.Chow.topologicalKrullDim_supp_fiberClosedSubscheme_closedPoint_le, Stacks.Chow.specializationCycle_familyAssociatedToClosedSubscheme, Stacks.Chow.topologicalKrullDim_pullback_fiberClosedSubscheme_closedPoint_le, Stacks.Chow.specializationCycle_familyAssociatedToClosedSubscheme_of_genericFibre, Stacks.Chow.baseChangeFiberCycleOfEq_comp_specializationCycleHom
statement: formalized
proof: formalized
---

# 62.4 Specialization of cycles

Section 62.4 of the Stacks Project, [Tag 0H4H](https://stacks.math.columbia.edu/tag/0H4H). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H4H, the section

[Tag 0H4H](https://stacks.math.columbia.edu/tag/0H4H) in the Stacks Project.

**`Stacks.Chow.specializationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Specialization.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Specialization.lean#L327). The attribute's comment: “the specialization map sp\_\{X/R}”.

> **Stacks 0H4H.** The specialization map `sp_{X/R} : Z_r(X_K) ⟶ Z_r(X_κ)` of a scheme locally
> of finite type over a discrete valuation ring `R`, from the cycles on the generic fibre to the
> cycles on the closed fibre. The generic fibre is the scheme-theoretic fibre over the generic
> point of `Spec R`, whose residue field is the fraction field `K`, and the closed fibre is the
> one over the closed point, whose residue field is `κ`.

```lean
def specializationMap (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X : Scheme.{u}} (sX : X ⟶ Spec (.of R)) [LocallyOfFiniteType sX] (r : ℕ) :
    FiberCycleGroup sX (genericPoint (Spec (.of R))) r →+
      FiberCycleGroup sX (IsLocalRing.closedPoint R) r
```

## Tag 0H4I, a lemma

[Tag 0H4I](https://stacks.math.columbia.edu/tag/0H4I) in the Stacks Project.

**`Stacks.Chow.topologicalKrullDim_supp_fiberModule_closedPoint_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleSpecialization/SpecializationFormula.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleSpecialization/SpecializationFormula.lean#L595). The attribute's comment: “the dimension bound on the special fibre”.

> **Stacks Project, Tag 0H4I.** Let `R` be a discrete valuation ring with fraction field `K`
> and residue field `kappa`, let `X` be a scheme locally of finite type over `R`, let `r >= 0` and
> let `F` be a coherent `O_X`-module flat over `R`. If `dim(Supp(F_K)) <= r`, then
> `dim(Supp(F_kappa)) <= r`.

```lean
theorem topologicalKrullDim_supp_fiberModule_closedPoint_le
    (hflat : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F) (r : ℕ)
    (hK : topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (f.fiberι (genericPoint (Spec (.of R))))).obj F)) ≤
        (r : WithBot ℕ∞)) :
    topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (f.fiberι (IsLocalRing.closedPoint R))).obj F)) ≤
      (r : WithBot ℕ∞)
```

**`Stacks.Chow.specializationCycle_familyAssociatedToModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleSpecialization/SpecializationFormula.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleSpecialization/SpecializationFormula.lean#L613). The attribute's comment: “the specialization formula”.

> **Stacks Project, Tag 0H4I.** Let `R` be a discrete valuation ring with fraction field `K`
> and residue field `kappa`, let `X` be a scheme locally of finite type over `R`, let `r >= 0` and
> let `F` be a coherent `O_X`-module flat over `R` with `dim(Supp(F_K)) <= r`. Then the
> specialization map `sp_{X/R} : Z_r(X_K) -> Z_r(X_kappa)` carries `[F_K]_r` to `[F_kappa]_r`:
> the member over the generic point of the family of cycles `[F/X/Spec R]_r` specializes to its
> member over the closed point.

```lean
theorem specializationCycle_familyAssociatedToModule
    (hflat : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F) (r : ℕ)
    (hK : topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (f.fiberι (genericPoint (Spec (.of R))))).obj F)) ≤
        (r : WithBot ℕ∞)) :
    specializationCycle f r
        (familyAssociatedToModule f F r
          (topologicalKrullDim_supp_fiberModule_le_of_genericFibre f F hflat r hK)
          (genericPoint (Spec (.of R)))) =
      familyAssociatedToModule f F r
        (topologicalKrullDim_supp_fiberModule_le_of_genericFibre f F hflat r hK)
        (IsLocalRing.closedPoint R)
```

## Tag 0H4J, a lemma

[Tag 0H4J](https://stacks.math.columbia.edu/tag/0H4J) in the Stacks Project.

**`Stacks.Chow.topologicalKrullDim_supp_fiberClosedSubscheme_closedPoint_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L185). The attribute's comment: “the dimension bound on the special fibre, for the support of i\_* 𝒪\_Z”.

> **Stacks Project, Lemma 0H4J**, the dimension clause for the support of `i_* 𝒪_Z`. Let `R`
> be a discrete valuation ring with fraction field `K` and residue field `κ`, let `Y` be locally
> of finite type over `R`, let `r ≥ 0` and let `Z ⊆ Y` be a closed subscheme flat over `R`. If
> `dim(Supp((i_* 𝒪_Z)_K)) ≤ r`, then `dim(Supp((i_* 𝒪_Z)_κ)) ≤ r`.
>
> With `𝒪_Z` for the module this is the dimension clause of Tag 0H4I; it is the tag's own
> statement `dim(Z_K) ≤ r ⟹ dim(Z_κ) ≤ r` read through
> `Stacks.Chow.topologicalKrullDim_pullback_fiberι_eq_supp`, which is what
> `Stacks.Chow.topologicalKrullDim_pullback_fiberClosedSubscheme_closedPoint_le` below does.

```lean
theorem topologicalKrullDim_supp_fiberClosedSubscheme_closedPoint_le {r : ℕ} {R : Type u}
    [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] {Y Z : Scheme.{u}}
    (p : Y ⟶ Spec (.of R)) [LocallyOfFiniteType p] (i : Z ⟶ Y) [IsClosedImmersion i]
    [Flat (i ≫ p)]
    (hK : topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (p.fiberι (genericPoint (Spec (.of R))))).obj
        (structureSheafPushforward i))) ≤ (r : WithBot ℕ∞)) :
    topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (p.fiberι (IsLocalRing.closedPoint R))).obj
        (structureSheafPushforward i))) ≤ (r : WithBot ℕ∞)
```

**`Stacks.Chow.specializationCycle_familyAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L210). The attribute's comment: “the specialization formula for the family of i\_* 𝒪\_Z”.

> **Stacks Project, Lemma 0H4J**, the specialization formula for the family of `i_* 𝒪_Z`. Let
> `R` be a discrete valuation ring with fraction field `K` and residue field `κ`, let `Y` be
> locally of finite type over `R`, let `r ≥ 0` and let `Z ⊆ Y` be a closed subscheme flat over `R`
> with `dim(Supp((i_* 𝒪_Z)_K)) ≤ r`. Then the specialization map `sp_{Y/R}` carries the member of
> `[i_* 𝒪_Z/Y/Spec R]_r` over the generic point to its member over the closed point.
>
> With `𝒪_Z` for the module this is the specialization clause of Tag 0H4I; the bound on every
> fibre that the family `[Z/Y/Spec R]_r` consumes comes from the bound on the generic fibre by
> `Stacks.Chow.topologicalKrullDim_supp_fiberModule_le_of_genericFibre`. The tag's own formula
> `sp_{Y/R}([Z_K]_r) = [Z_κ]_r`, for the family `[Z/Y/Spec R]_r` of the closed subscheme itself,
> is `Stacks.Chow.specializationCycle_familyAssociatedToClosedSubscheme_of_genericFibre` below.

```lean
theorem specializationCycle_familyAssociatedToClosedSubscheme {r : ℕ} {R : Type u} [CommRing R]
    [IsDomain R] [IsDiscreteValuationRing R] {Y Z : Scheme.{u}} (p : Y ⟶ Spec (.of R))
    [LocallyOfFiniteType p] (i : Z ⟶ Y) [IsClosedImmersion i] [Flat (i ≫ p)]
    (hK : topologicalKrullDim (SheafOfModules.supp
      ((Scheme.Modules.pullback (p.fiberι (genericPoint (Spec (.of R))))).obj
        (structureSheafPushforward i))) ≤ (r : WithBot ℕ∞)) :
    specializationCycle p r
        (familyAssociatedToModule p (structureSheafPushforward i) r
          (topologicalKrullDim_supp_fiberModule_le_of_genericFibre p
            (structureSheafPushforward i) (isFlatOver_pushforwardStructureSheaf i p) r hK)
          (genericPoint (Spec (.of R)))) =
      familyAssociatedToModule p (structureSheafPushforward i) r
        (topologicalKrullDim_supp_fiberModule_le_of_genericFibre p
          (structureSheafPushforward i) (isFlatOver_pushforwardStructureSheaf i p) r hK)
        (IsLocalRing.closedPoint R)
```

**`Stacks.Chow.topologicalKrullDim_pullback_fiberClosedSubscheme_closedPoint_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L269). The attribute's comment: “the dimension bound on the special fibre”.

> **Stacks Project, Lemma 0H4J.** Let `R` be a discrete valuation ring with fraction field `K`
> and residue field `κ`, let `Y` be locally of finite type over `R`, let `r ≥ 0` and let `Z ⊆ Y` be
> a closed subscheme flat over `R`. If `dim(Z_K) ≤ r`, then `dim(Z_κ) ≤ r`.
>
> This is the previous bound at the closed point of `Spec R`.

```lean
theorem topologicalKrullDim_pullback_fiberClosedSubscheme_closedPoint_le {r : ℕ} {R : Type u}
    [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] {Y Z : Scheme.{u}}
    (p : Y ⟶ Spec (.of R)) [LocallyOfFiniteType p] (i : Z ⟶ Y) [IsClosedImmersion i]
    [Flat (i ≫ p)]
    (hK : topologicalKrullDim (pullback i (p.fiberι (genericPoint (Spec (.of R)))) :
      Scheme.{u}) ≤ (r : WithBot ℕ∞)) :
    topologicalKrullDim (pullback i (p.fiberι (IsLocalRing.closedPoint R)) :
      Scheme.{u}) ≤ (r : WithBot ℕ∞)
```

**`Stacks.Chow.specializationCycle_familyAssociatedToClosedSubscheme_of_genericFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L291). The attribute's comment: “the specialization formula”.

> **Stacks Project, Lemma 0H4J.** Let `R` be a discrete valuation ring with fraction field `K`
> and residue field `κ`, let `Y` be locally of finite type over `R`, let `r ≥ 0` and let `Z ⊆ Y` be
> a closed subscheme flat over `R` with `dim(Z_K) ≤ r`. Then the specialization homomorphism
> `sp_{Y/R}` of Section 0H4H carries `[Z_K]_r` to `[Z_κ]_r`.
>
> This is the proof of the source: the family `[Z/Y/Spec R]_r` of the closed subscheme is the
> family `[i_* 𝒪_Z/Y/Spec R]_r` of its structure sheaf by Chow Homology, Lemma 42.10.3, which is
> `Stacks.Chow.familyAssociatedToClosedSubscheme_eq_familyAssociatedToModule`, and for that family
> the formula is the specialization clause of Tag 0H4I. The bound on every fibre that the
> identification consumes comes from the bound on the generic fibre by
> `Stacks.Chow.topologicalKrullDim_pullback_fiberι_le_of_genericFibre`.

```lean
theorem specializationCycle_familyAssociatedToClosedSubscheme_of_genericFibre {r : ℕ}
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] {Y Z : Scheme.{u}}
    (p : Y ⟶ Spec (.of R)) [LocallyOfFiniteType p] (i : Z ⟶ Y) [IsClosedImmersion i]
    [Flat (i ≫ p)]
    (hK : topologicalKrullDim (pullback i (p.fiberι (genericPoint (Spec (.of R)))) :
      Scheme.{u}) ≤ (r : WithBot ℕ∞)) :
    specializationCycle p r
        (familyAssociatedToClosedSubscheme p i r (genericPoint (Spec (.of R)))) =
      familyAssociatedToClosedSubscheme p i r (IsLocalRing.closedPoint R)
```

## Tag 0H4K, a lemma

[Tag 0H4K](https://stacks.math.columbia.edu/tag/0H4K) in the Stacks Project.

**`Stacks.Chow.baseChangeFiberCycleOfEq_comp_specializationCycleHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationBaseChange.lean, line 645](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationBaseChange.lean#L645).

> **Stacks Project, Tag 0H4K.** Let `R'/R` be an extension of discrete valuation rings,
> inducing a fraction field extension `K'/K` and a residue field extension `κ'/κ`, let `X` be
> locally of finite type over `R` and let `X' = X_{R'}`. For `r ≥ 0` the square formed by the
> specialization homomorphisms `sp_{X/R} : Z_r(X_K) ⟶ Z_r(X_κ)` and
> `sp_{X'/R'} : Z_r(X'_{K'}) ⟶ Z_r(X'_{κ'})` of Section 0H4H and the base change maps of
> Section 0H4E commutes.
>
> The integral-subscheme case is
> `Stacks.Chow.specializationCompatibleWithBaseChange` and the passage from it to an arbitrary
> cycle is `Stacks.Chow.baseChangeFiberCycleOfEq_comp_specializationCycleHom_of_generator`.

```lean
theorem baseChangeFiberCycleOfEq_comp_specializationCycleHom :
    (baseChangeSpecialFibreCycle R' f r).comp (specializationCycleHom f r) =
      (specializationCycleHom (pullback.snd f (specMapAlgebraMap R R')) r).comp
        (baseChangeGenericFibreCycle R' f r)
```

## Tag 0H4L, a lemma

[Tag 0H4L](https://stacks.math.columbia.edu/tag/0H4L) in the Stacks Project.

**`Stacks.Chow.fiberCycleFlatPullback_comp_specializationCycleHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationFlatPullback.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationFlatPullback.lean#L188).

> **Stacks Project, Lemma 0H4L.** Let `R` be a discrete valuation ring with fraction field `K`
> and residue field `κ`, let `X` be a scheme locally of finite type over `R`, and let `p : X' ⟶ X`
> be a morphism which is locally of finite type, flat and of relative dimension `e`. Then for
> `r ≥ 0` the square formed by the specialization homomorphisms
> `sp_{X/R} : Z_r(X_K) ⟶ Z_r(X_κ)` and `sp_{X'/R} : Z_{r+e}(X'_K) ⟶ Z_{r+e}(X'_κ)` of
> Section 0H4H and the flat pullbacks `Z_r(X_K) ⟶ Z_{r+e}(X'_K)`, `Z_r(X_κ) ⟶ Z_{r+e}(X'_κ)` of
> Section 0H4N commutes.
>
> The integral-subscheme case is
> `Stacks.Chow.specializationCycle_fiberCycleFlatPullback_integralGenericCycle`. The passage from
> it to an arbitrary cycle is the regrouping below: the coefficient of `sp_{X'/R}` of a flat
> pullback is a locally finite sum over the points of `X'_K`, which is summed along the fibres of
> `X'_K ⟶ X_K` and each fibre identified with the corresponding term of the flat pullback of
> `sp_{X/R}`.

```lean
theorem fiberCycleFlatPullback_comp_specializationCycleHom :
    (fiberCycleFlatPullback f fX' p hp e he (IsLocalRing.closedPoint R) r).comp
        (specializationCycleHom f r) =
      (specializationCycleHom fX' (r + e)).comp
        (fiberCycleFlatPullback f fX' p hp e he (genericPoint (Spec (.of R))) r)
```

**`Stacks.Chow.specializationCycle_baseChangedFiberCycleFlatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationFlatPullback.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationFlatPullback.lean#L289). The attribute's comment: “for the base change of the flat morphism to the spectrum of a discrete valuation ring over the base”.

> **Stacks Project, Lemma 0H4L** for the base change of a flat morphism of the source to the
> spectrum of a discrete valuation ring over the base. This is the shape in which the valuative
> condition of Definition 0H50 compares the two members of a flat pullback of a family of cycles on
> fibres: `Stacks.Chow.baseChangedFiberCycleFlatPullback` is flat pullback along the base change of
> `j`, which is again flat, locally of finite type and of relative dimension `e`.

```lean
theorem specializationCycle_baseChangedFiberCycleFlatPullback {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ S) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU) (e : ℕ)
    (he : AlgebraicGeometry.RelativeDimension j e) {R : Type u} [CommRing R] [IsDomain R]
    [IsDiscreteValuationRing R] (g : Spec (.of R) ⟶ S) (r : ℕ)
    (c : FiberCycleGroup (pullback.snd f g) (genericPoint (Spec (.of R))) r) :
    baseChangedFiberCycleFlatPullback f fU j h e he g (IsLocalRing.closedPoint R) r
        (specializationCycle (pullback.snd f g) r c) =
      specializationCycle (pullback.snd fU g) (r + e)
        (baseChangedFiberCycleFlatPullback f fU j h e he g
          (genericPoint (Spec (.of R))) r c)
```

**`Stacks.Chow.specializationCycle_fiberCycleRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationRestriction.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationRestriction.lean#L271). The attribute's comment: “open immersions”.

> The specialization map commutes with restriction to an open subscheme of the source: for
> `j : U ⟶ X` an open immersion of schemes locally of finite type over a discrete valuation ring
> `R`, restricting an `r`-cycle on the generic fibre of `X` to the generic fibre of `U` and then
> specializing is the same as specializing and then restricting to the special fibre of `U`.

```lean
theorem specializationCycle_fiberCycleRestrict {R : Type u} [CommRing R] [IsDomain R]
    [IsDiscreteValuationRing R] {X U : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFiniteType f] (fU : U ⟶ Spec (.of R)) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [IsOpenImmersion j] (h : j ≫ f = fU) (r : ℕ)
    (c : FiberCycleGroup f (genericPoint (Spec (.of R))) r) :
    specializationCycle fU r
        (fiberCycleRestrict f fU j h (genericPoint (Spec (.of R))) r c) =
      fiberCycleRestrict f fU j h (IsLocalRing.closedPoint R) r (specializationCycle f r c)
```

## Tag 0H4M, a lemma

[Tag 0H4M](https://stacks.math.columbia.edu/tag/0H4M) in the Stacks Project.

**`Stacks.Chow.specializationCycle_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean#L268). The attribute's comment: “specialization commutes with pushforward along a closed immersion”.

> Specialization of cycles over a discrete valuation ring commutes with pushforward along a
> closed immersion over that ring: pushing the specialization of a cycle on the generic fibre forward
> along the morphism of closed fibres gives the specialization of its pushforward along the morphism
> of generic fibres.

```lean
theorem specializationCycle_properPushforwardFamily
    (c : FiberCycleGroup sX (genericPoint (Spec (.of R))) r) :
    fiberProperPushforward sX sY i hi (IsLocalRing.closedPoint R) r (specializationCycle sX r c) =
      specializationCycle sY r
        (fiberProperPushforward sX sY i hi (genericPoint (Spec (.of R))) r c)
```

**`Stacks.Chow.specializationCycle_fiberProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationProperPushforward.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationProperPushforward.lean#L362). The attribute's comment: “the square of the specialization maps and the proper pushforwards commutes”.

> **Stacks 0H4M.** Let `R` be a discrete valuation ring with fraction field `K` and residue
> field `κ`, let `f : X ⟶ Y` be a proper morphism of schemes locally of finite type over `R` and
> let `r ≥ 0`. The square formed by the specialization maps `sp_{X/R} : Z_r(X_K) ⟶ Z_r(X_κ)` and
> `sp_{Y/R} : Z_r(Y_K) ⟶ Z_r(Y_κ)` and the proper pushforwards along the morphisms `f_K` and
> `f_κ` induced by `f` on the generic and the closed fibres commutes.

```lean
theorem specializationCycle_fiberProperPushforward (sX : X ⟶ Spec (.of R))
    [LocallyOfFiniteType sX] (sY : Y ⟶ Spec (.of R)) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [IsProper f] (hf : f ≫ sY = sX) (r : ℕ)
    (c : FiberCycleGroup sX (genericPoint (Spec (.of R))) r) :
    fiberProperPushforward sX sY f hf (IsLocalRing.closedPoint R) r
        (specializationCycle sX r c) =
      specializationCycle sY r
        (fiberProperPushforward sX sY f hf (genericPoint (Spec (.of R))) r c)
```

**`Stacks.Chow.properPushforward_specializationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationProperPushforward.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationProperPushforward.lean#L412). The attribute's comment: “the square, read on the specialization map sp\_\{X/R} of Stacks 0H4H”.

> **Stacks 0H4M**, read on the specialization map `sp_{X/R}` of Stacks 0H4H: the square
> formed by `sp_{X/R}`, `sp_{Y/R}` and the proper pushforwards along the morphisms induced by `f`
> on the generic and the closed fibres commutes.

```lean
theorem properPushforward_specializationMap (R : Type u) [CommRing R] [IsDomain R]
    [IsDiscreteValuationRing R] {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of R))
    [LocallyOfFiniteType sX] (sY : Y ⟶ Spec (.of R)) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [IsProper f] (hf : f ≫ sY = sX) (r : ℕ)
    (α : FiberCycleGroup sX (genericPoint (Spec (.of R))) r) :
    fiberProperPushforward sX sY f hf (IsLocalRing.closedPoint R) r
        (specializationMap R sX r α) =
      specializationMap R sY r
        (fiberProperPushforward sX sY f hf (genericPoint (Spec (.of R))) r α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.4, Tag 0H4H](https://stacks.math.columbia.edu/tag/0H4H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
