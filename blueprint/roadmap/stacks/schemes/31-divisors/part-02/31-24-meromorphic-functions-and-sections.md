---
declaration: section
origin: cited
lean: AlgebraicGeometry.MeromorphicFunction, totalQuotientSheaf, AlgebraicGeometry.NoChange.noChangeRing, AlgebraicGeometry.NoChange.normalForm_bijective, AlgebraicGeometry.NoChange.isUnit_of_isRegular_localizationAway, AlgebraicGeometry.NoChange.isIso_toTotalQuotientSheaf, AlgebraicGeometry.meromorphicSectionSheaf, AlgebraicGeometry.MeromorphicSection
statement: formalized
proof: formalized
---

# 31.24 Meromorphic functions and sections

Section 31.24 of the Stacks Project, [Tag 01X1](https://stacks.math.columbia.edu/tag/01X1). 10 tags here are carried by 47 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01X2, a definition

[Tag 01X2](https://stacks.math.columbia.edu/tag/01X2) in the Stacks Project.

**`AlgebraicGeometry.MeromorphicFunction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean#L70). The attribute's comment: “a meromorphic function”. References: EGA IV (20.1.3), “M(X)”.

> A meromorphic function on a locally ringed space is a global section of its sheaf of
> meromorphic functions, the sheaf of total quotient rings of its structure sheaf.

```lean
abbrev MeromorphicFunction (O : TopCat.Sheaf CommRingCat.{u} X) : Type u
```

Declarations registered for the tag:

- [`totalQuotientSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=totalQuotientSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TotalQuotient.lean#L138) (StacksFrontier): “the sheaf of meromorphic functions”.

## Tag 01X3, an example

[Tag 01X3](https://stacks.math.columbia.edu/tag/01X3) in the Stacks Project.

**`AlgebraicGeometry.NoChange.noChangeRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean#L71). The attribute's comment: “the ring”.

> The ring `ℂ[x, {y_α}]/((x-α)y_α, y_α y_β)`.

```lean
abbrev noChangeRing
```

**`AlgebraicGeometry.NoChange.normalForm_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean#L479). The attribute's comment: “unique normal form”.

> Every element of the example ring has a unique displayed normal form.

```lean
theorem normalForm_bijective : Function.Bijective normalForm
```

**`AlgebraicGeometry.NoChange.isUnit_of_isRegular_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean#L487). The attribute's comment: “nonzerodivisors on principal opens”.

> On every principal open of `Spec A`, a nonzerodivisor is a unit.

```lean
theorem isUnit_of_isRegular_localizationAway (f : noChangeRing)
    (a : Localization.Away f) (ha : IsRegular a) : IsUnit a
```

**`AlgebraicGeometry.NoChange.isIso_toTotalQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/NoChange.lean#L676). The attribute's comment: “equality of sheaves”.

> The canonical map from the structure sheaf of `Spec A` to its sheaf of
> meromorphic functions is an isomorphism.

```lean
theorem isIso_toTotalQuotientSheaf :
    IsIso (Scheme.toTotalQuotientSheaf
      (Spec (.of noChangeRing)))
```

## Tag 01X4, a definition

[Tag 01X4](https://stacks.math.columbia.edu/tag/01X4) in the Stacks Project.

**`AlgebraicGeometry.meromorphicSectionSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean#L61). The attribute's comment: “part (1)”. References: EGA IV (20.1.3), “M\_X(F)”.

> The sheaf `K_X(F)` of meromorphic sections of `F`, obtained by extension of scalars from
> `O` to its sheaf of total quotient rings.

```lean
noncomputable abbrev meromorphicSectionSheaf (O : TopCat.Sheaf CommRingCat.{u} X)
    (F : SheafOfModules.{max u z} (Stacks.Sheaves.Differentials.ringSheaf (C := Opens X)
      (J := Opens.grothendieckTopology X) O)) :
    SheafOfModules.{max u z} (Stacks.Sheaves.Differentials.ringSheaf (C := Opens X)
      (J := Opens.grothendieckTopology X) (totalQuotientSheaf (X := X) O))
```

**`AlgebraicGeometry.MeromorphicSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean#L75). The attribute's comment: “part (2)”. References: EGA IV (20.1.3), “M(X,F)”.

> A meromorphic section of `F` is a global section of `K_X(F)`.

```lean
abbrev MeromorphicSection (O : TopCat.Sheaf CommRingCat.{u} X)
    (F : SheafOfModules.{max u z} (Stacks.Sheaves.Differentials.ringSheaf (C := Opens X)
      (J := Opens.grothendieckTopology X) O))
```

## Tag 02OT, a definition

[Tag 02OT](https://stacks.math.columbia.edu/tag/02OT) in the Stacks Project.

**`AlgebraicGeometry.PullbacksMeromorphicSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Pullback.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Pullback.lean#L105). References: EGA IV (20.1.11), “M\_f = M\_X condition”.

> Pullbacks of meromorphic functions are defined for `f` when the pullback to every compatible
> pair of opens sends regular sections of the target structure sheaf to regular sections of the
> source structure sheaf.

```lean
noncomputable abbrev PullbacksMeromorphicSections
    {X Y : LocallyRingedSpace.{u}} (f : X ⟶ Y) : Prop
```

## Tag 02OU, a lemma

[Tag 02OU](https://stacks.math.columbia.edu/tag/02OU) in the Stacks Project.

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_mapsTo_genericPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L86). The attribute's comment: “weakly\_associated”.

> If a morphism of schemes maps every weakly associated point of its source to the generic
> point of an irreducible component of its target, then pullbacks of meromorphic functions are
> defined for the morphism.

```lean
lemma pullbacksMeromorphicSections_of_mapsTo_genericPoints
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : Set.MapsTo f (Stacks.Divisors.schemeWeaklyAssociatedPoints X) (genericPoints Y)) :
    PullbacksMeromorphicSections f.1
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_reduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L127). The attribute's comment: “reduced\_source”.

> **Stacks Project, Tag 02OU (reduced source).** If a morphism from a reduced scheme sends
> every generic point of an irreducible component to a generic point of an irreducible component,
> then pullbacks of meromorphic functions along it are defined.

```lean
theorem pullbacksMeromorphicSections_of_reduced {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsReduced X] (hf : Set.MapsTo f (genericPoints X) (genericPoints Y)) :
    PullbacksMeromorphicSections f.toLRSHom
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_isIntegral`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L137). The attribute's comment: “integral\_source”.

> **Stacks Project, Tag 02OU (integral source).** If the source of a morphism of schemes is
> integral and its generic point maps to a generic point of an irreducible component of the target,
> then pullbacks of meromorphic functions are defined.

```lean
lemma pullbacksMeromorphicSections_of_isIntegral
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral X]
    (h : f (genericPoint X) ∈ genericPoints Y) :
    PullbacksMeromorphicSections f.toLRSHom
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_isDominant`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L146). The attribute's comment: “dominant\_integral”. References: EGA IV (21.4.5), “(iii), X,X' integral”.

> **Stacks Project, Tag 02OU.** Pullbacks of meromorphic functions are defined along a
> dominant morphism between integral schemes.

```lean
lemma pullbacksMeromorphicSections_of_isDominant
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral X] [IsIntegral Y] [IsDominant f] :
    PullbacksMeromorphicSections f.toLRSHom
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_associatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L158). The attribute's comment: “associated\_points”. References: EGA IV (21.4.5), “(ii), to generic points”.

> **Stacks Project, Tag 02OU (associated points).** If every associated point of a locally
> Noetherian source scheme maps to the generic point of an irreducible component of the target,
> then pullbacks of meromorphic functions are defined.

```lean
theorem pullbacksMeromorphicSections_of_associatedPoints
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X]
    (h : ∀ x ∈ Stacks.Divisors.schemeAssociatedPoints X,
      ∃ Z ∈ irreducibleComponents Y, IsGenericPoint (f x) Z) :
    PullbacksMeromorphicSections f.toLRSHom
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_noEmbeddedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L175). The attribute's comment: “no\_embedded\_points”.

> **Stacks Project, Tag 02OU (no embedded points).** If a morphism from a locally Noetherian
> scheme without embedded points sends every generic point of an irreducible component to a
> generic point of an irreducible component, then pullbacks of meromorphic functions along it are
> defined.

```lean
theorem pullbacksMeromorphicSections_of_noEmbeddedPoints
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian X]
    (hX : AlgebraicGeometry.HasNoEmbeddedPoints X)
    (hf : Set.MapsTo f (genericPoints X) (genericPoints Y)) :
    PullbacksMeromorphicSections f.toLRSHom
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PullbackCriteria.lean#L197). The attribute's comment: “flat”. References: EGA IV (21.4.5), “(i)”.

> Pullbacks of meromorphic functions are defined along a flat morphism of schemes.

```lean
theorem pullbacksMeromorphicSections_of_flat
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f] :
    PullbacksMeromorphicSections f.toLRSHom
```

## Tag 0EMF, a lemma

[Tag 0EMF](https://stacks.math.columbia.edu/tag/0EMF) in the Stacks Project.

**`AlgebraicGeometry.regularSectionGerms_eq_nonZeroDivisors_of_weaklyAssociatedPoints_subset_genericPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksWeaklyAssociated.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksWeaklyAssociated.lean#L139). The attribute's comment: “regular\_elements\_in\_stalks”.

> If weakly associated points are generic points of irreducible components and
> quasi-compact opens have finitely many irreducible components, then the germs of regular
> sections at every point are exactly the nonzerodivisors in its local ring.

```lean
lemma regularSectionGerms_eq_nonZeroDivisors_of_weaklyAssociatedPoints_subset_genericPoints
    (X : Scheme.{u})
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ (U : X.Opens), IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    (⨆ (U : Opens X) (hx : x ∈ U),
      ((X.presheaf.submonoidPresheafOfStalk
        (fun y ↦ nonZeroDivisors (X.presheaf.stalk y))).obj (Opposite.op U)).map
          (X.presheaf.germ U x hx).hom) =
      nonZeroDivisors (X.presheaf.stalk x)
```

**`AlgebraicGeometry.stalk_totalQuotientPresheaf_isFractionRing_of_weaklyAssociatedPoints_subset_genericPoints`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksWeaklyAssociated.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/StalksWeaklyAssociated.lean#L183). The attribute's comment: “stalk\_total\_quotient\_ring”.

> If every weakly associated point of a scheme is a generic point of an irreducible component
> and every quasi-compact open has finitely many irreducible components, then the stalk of the
> presheaf of meromorphic functions at any point is the total quotient ring of the local ring.

```lean
lemma stalk_totalQuotientPresheaf_isFractionRing_of_weaklyAssociatedPoints_subset_genericPoints
    (X : Scheme.{u})
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ (U : X.Opens), IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.presheaf.toTotalQuotientPresheaf).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x) (X.presheaf.totalQuotientPresheaf.stalk x)
```

**`AlgebraicGeometry.stalk_totalQuotientSheaf_isFractionRing_of_weaklyAssociated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/TotalQuotientSheafStalks.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/TotalQuotientSheafStalks.lean#L85). The attribute's comment: “stalk\_total\_quotient\_ring”.

> If every weakly associated point of a scheme is a generic point of an irreducible component
> and every quasi-compact open has finitely many irreducible components, then the stalk `K_{X, x}`
> of the sheaf of meromorphic functions at any point is the total quotient ring of the local ring
> `𝒪_{X, x}`.

```lean
lemma stalk_totalQuotientSheaf_isFractionRing_of_weaklyAssociated
    (X : Scheme.{u})
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ (U : X.Opens), IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    letI : Algebra (X.presheaf.stalk x) (X.totalQuotientSheaf.presheaf.stalk x) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        X.toTotalQuotientSheaf.hom).hom.toAlgebra
    IsFractionRing (X.presheaf.stalk x) (X.totalQuotientSheaf.presheaf.stalk x)
```

**`AlgebraicGeometry.isIso_toGenericPointStalkProduct`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Basic.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Basic.lean#L268). The attribute's comment: “generic\_point\_decomposition”.

> The comparison map of sheaves of rings is an isomorphism: it is so on stalks, because the
> presheaf-level comparison is bijective on the affine opens and the sheafification unit is an
> isomorphism on stalks.

```lean
lemma isIso_toGenericPointStalkProduct
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) :
    IsIso (toGenericPointStalkProduct X)
```

**`AlgebraicGeometry.meromorphicFunctions_iso_product_genericPointStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Basic.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Basic.lean#L363). The attribute's comment: “generic\_point\_decomposition”.

> **Stacks 0EMF.** The `𝒪_X`-module of meromorphic functions is the product of the
> pushed-forward structure sheaves of the local schemes at the generic points of the irreducible
> components, for a scheme whose weakly associated points are generic points of irreducible
> components and whose quasi-compact opens have finitely many irreducible components.

```lean
theorem meromorphicFunctions_iso_product_genericPointStalks
    (X : Scheme.{u})
    (hassoc : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) →
      (irreducibleComponents U).Finite) :
    Nonempty (meromorphicFunctions X ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`AlgebraicGeometry.meromorphicFunctions_iso_coproduct_genericPointStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Coproduct.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Coproduct.lean#L247). The attribute's comment: “generic\_point\_decomposition”.

> **Stacks 0EMF, displayed direct-sum decomposition.** For a scheme whose weakly associated
> points are generic points of irreducible components and whose quasi-compact opens have finitely
> many irreducible components, the `𝒪_X`-module of meromorphic functions is the direct sum over
> the generic points of the irreducible components of the pushed-forward structure sheaves of the
> spectra of the local rings there.

```lean
theorem meromorphicFunctions_iso_coproduct_genericPointStalks (X : Scheme.{u})
    (hassoc : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    Nonempty (meromorphicFunctions X ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModule X η)
```

**`AlgebraicGeometry.isLocalization_totalQuotientSheaf_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L187). The attribute's comment: “part (5)”.

> **Part (5) of [Stacks, Tag 0EMF].** On an affine open `U` of a scheme whose weakly associated
> points are generic points of irreducible components and whose quasi-compact opens have finitely
> many irreducible components, the sections `K_X(U)` of the *sheaf* of meromorphic functions — not
> only those of the presheaf — are the total quotient ring of `Γ(X, U)`, that is, its localization
> at its nonzerodivisors.

```lean
theorem isLocalization_totalQuotientSheaf_obj
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    {U : X.Opens} (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U) (X.totalQuotientSheaf.obj.obj (op U)) :=
      (X.toTotalQuotientSheaf.hom.app (op U)).hom.toAlgebra
    IsLocalization (nonZeroDivisors Γ(X, U)) (X.totalQuotientSheaf.obj.obj (op U))
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_pi_genericPointStalkModuleOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L626). The attribute's comment: “part (2), product”.

> **Part (2) of [Stacks, Tag 0EMF], the product decomposition.** For a quasi-coherent module `F`
> on a scheme whose weakly associated points are generic points of irreducible components and whose
> quasi-compact opens have finitely many irreducible components, the sheaf `K_X(F)` of meromorphic
> sections of `F` is the product over the generic points of the irreducible components of the
> generic-point contributions.

```lean
theorem nonempty_meromorphicSections_iso_pi_genericPointStalkModuleOf
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∏ᶜ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.nonempty_meromorphicSections_iso_sigma_genericPointStalkModuleOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L638). The attribute's comment: “part (2), direct sum”.

> **Part (2) of [Stacks, Tag 0EMF], the direct-sum decomposition.** The family of generic-point
> contributions is locally finite, so the product of the previous theorem is also their direct
> sum.

```lean
theorem nonempty_meromorphicSections_iso_sigma_genericPointStalkModuleOf
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    Nonempty (meromorphicSections X F ≅
      ∐ fun η : genericPoints X ↦ genericPointStalkModuleOf X F η)
```

**`AlgebraicGeometry.meromorphicSections_isQuasicoherent_of_genericHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicGenericPointDecomposition/Globalization.lean#L651). The attribute's comment: “part (2), quasi-coherence”.

> **Part (2) of [Stacks, Tag 0EMF], quasi-coherence.** The sheaf `K_X(F)` of meromorphic
> sections of a quasi-coherent module `F` is quasi-coherent, being the product of the generic-point
> contributions.

```lean
theorem meromorphicSections_isQuasicoherent_of_genericHypotheses
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (F : X.Modules) [F.IsQuasicoherent] :
    (meromorphicSections X F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.MeromorphicQuasicoherent.meromorphicFunctions_isQuasicoherent_of_genericHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MeromorphicQuasicoherent/Criteria.lean#L60). The attribute's comment: “part (1)”.

> **Part (1) of [Stacks, Tag 0EMF].** On a scheme whose weakly associated points are generic
> points of irreducible components and whose quasi-compact opens have finitely many irreducible
> components, the sheaf of meromorphic functions is quasi-coherent: it is then the product of the
> generic-point contributions, and that product is quasi-coherent.

```lean
theorem meromorphicFunctions_isQuasicoherent_of_genericHypotheses {X : Scheme.{u}}
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfin : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents (U : Set X)).Finite) :
    (meromorphicFunctions X).IsQuasicoherent
```

**`AlgebraicGeometry.exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean, line 608](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RationalFunctions/Meromorphic.lean#L608). The attribute's comment: “part (6)”. References: EGA I (7.1.3), “special case”.

> **Part (6) of [Stacks, Tag 0EMF]**, with the commutative ring structure on the rational
> functions constructed rather than assumed: it is transported from the global sections of the sheaf
> of total quotient rings along the bijection, and every section on a dense open set is a ring
> homomorphism to it, which is the characterization of [Stacks, Tag 01RU].

```lean
theorem exists_commRing_rationalFunctions_ringEquiv_totalQuotientSheaf_top (X : Scheme.{u})
    (hass : Stacks.Divisors.schemeWeaklyAssociatedPoints X ⊆ genericPoints X)
    (hfinite : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) :
    ∃ _ : CommRing X.rationalFunctions,
      (∀ (U : X.Opens) (hU : Dense (U : Set X)),
          ∃ ψ : Γ(X, U) →+* X.rationalFunctions,
            ∀ s, ψ s = X.rationalFunctionOfSection U hU s) ∧
        Nonempty (X.rationalFunctions ≃+* X.totalQuotientSheaf.presheaf.obj (op ⊤))
```

## Tag 02OX, a definition

[Tag 02OX](https://stacks.math.columbia.edu/tag/02OX) in the Stacks Project.

**`AlgebraicGeometry.IsRegularMeromorphicSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/MeromorphicSections.lean#L83). References: EGA IV (20.1.8), “regular section defn”.

> A meromorphic section is regular if its induced map from the total quotient sheaf
> to the meromorphic section sheaf is injective.

```lean
noncomputable abbrev IsRegularMeromorphicSection (O : TopCat.Sheaf CommRingCat.{u} X)
    (L : SheafOfModules.{u} (Stacks.Sheaves.Differentials.ringSheaf (C := Opens X)
      (J := Opens.grothendieckTopology X) O))
    (s : MeromorphicSection O L) : Prop
```

## Tag 02OY, a lemma

[Tag 02OY](https://stacks.math.columbia.edu/tag/02OY) in the Stacks Project.

**`AlgebraicGeometry.pullbackMeromorphicSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionPullback.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionPullback.lean#L216). The attribute's comment: “part (1)”. References: EGA IV (20.1.11), “mero section pullback”.

> **The canonical pullback map on meromorphic sections.** When pullbacks of meromorphic
> functions are defined for `f`, a meromorphic section of a sheaf of `𝒪_Y`-modules `F` pulls
> back to a meromorphic section of `f^* F`: apply the morphism `𝒦_Y(F) ⟶ f_* 𝒦_X(f^* F)` and
> read the resulting global section over the whole of `X`.

```lean
noncomputable def pullbackMeromorphicSection (s : MeromorphicSection Y.sheaf F) :
    MeromorphicSection X.sheaf
      ((RingedSpaceModuleAdjunction.modulePullback f.toShHom).obj F)
```

**`AlgebraicGeometry.isRegularMeromorphicSection_pullbackMeromorphicSection_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionPullbackRegularGeneral.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionPullbackRegularGeneral.lean#L49). The attribute's comment: “part (2)”.

> **Stacks 02OY part (2).** Let `f : X ⟶ Y` be a morphism of locally ringed spaces for which
> pullbacks of meromorphic functions are defined and let `L` be an invertible `𝒪_Y`-module. The
> pullback of a regular meromorphic section of `L` is a regular meromorphic section of `f^* L`.

```lean
theorem isRegularMeromorphicSection_pullbackMeromorphicSection_of_isInvertible
    {X Y : LocallyRingedSpace.{u}} (f : X ⟶ Y) (hf : PullbacksMeromorphicSections f)
    (L : SheafOfModules.{u} Y.ringCatSheaf)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.property L)
    (s : MeromorphicSection Y.sheaf L) (hs : IsRegularMeromorphicSection Y.sheaf L s) :
    IsRegularMeromorphicSection X.sheaf
      ((RingedSpaceModuleAdjunction.modulePullback f.toShHom).obj L)
      (pullbackMeromorphicSection f hf L s)
```

## Tag 02P0, a lemma

[Tag 02P0](https://stacks.math.columbia.edu/tag/02P0) in the Stacks Project.

**`Stacks.DenominatorIdeal.denominatorIdeal_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdeal/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdeal/Basic.lean#L117). The attribute's comment: “the denominator rule”.

> A section of the structure sheaf is a denominator of the meromorphic section `s` exactly when
> its product with `s` is a section of `L`.

```lean
theorem denominatorIdeal_sections (U : Opens X)
    (f : (SheafOfModules.unit (O X)).val.obj (op U)) :
    (∃ d : (denominatorIdeal X L s).val.obj (op U),
      (denominatorIdealι X L s).val.app (op U) d = f) ↔
    (∃ t : L.val.obj (op U),
      (sectionMap X L s).val.app (op U) f =
        (toK X L).val.app (op U) t)
```

**`Stacks.DenominatorIdeal.denominatorIdeal_section_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdeal/Basic.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdeal/Basic.lean#L167). The attribute's comment: “multiplication is injective”.

> Multiplication by a regular meromorphic section embeds its denominator ideal in `L`.

```lean
theorem denominatorIdeal_section_mono (hs : IsRegularMeromorphicSection X.sheaf L s) :
    Mono (denominatorIdealMul X L s)
```

**`Stacks.DenominatorIdealInvertible.denominatorIdeal_inclusion_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdealInvertible/Basic.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdealInvertible/Basic.lean#L140). The attribute's comment: “inclusion is injective”.

> **The denominator ideal of a meromorphic section of an invertible sheaf embeds in the
> structure sheaf.** Stacks Tag 02P0, "inclusion is injective".

```lean
theorem denominatorIdeal_inclusion_mono (s : MeromorphicSection.{u, u} X.sheaf L)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L) :
    Mono (denominatorIdealι X L s)
```

**`Stacks.DenominatorIdealQcoh.denominatorIdeal_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/Basic.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/Basic.lean#L276). The attribute's comment: “quasi-coherence”. References: EGA IV (20.2.14), “special case”.

> **The denominator ideal of a meromorphic section of an invertible sheaf is quasi-coherent.**
>
> Around every point there is an affine open `V` on which the denominator ideal is the colon ideal
> `(b Γ(X, V) : a)` for a nonzerodivisor `b` and a numerator `a`, and the colon ideal commutes with
> localization, so the sections over each basic open of `V` are the localization of the sections
> over `V`.  Those affine opens cover `X`, and quasi-coherence is detected by that condition on the
> members of a cover.

```lean
theorem denominatorIdeal_isQuasicoherent
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L) :
    (denominatorIdeal X L s).IsQuasicoherent
```

**`Stacks.DenominatorIdealQcoh.denominatorIdealData_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/IdealData.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/IdealData.lean#L189). The attribute's comment: “affine denominator ideal”.

> **On each affine open the ideal-sheaf data are exactly the denominators.**
>
> `Scheme.IdealSheafData.ofIdeals` is a supremum and in general shrinks the family of ideals it is
> applied to; it does not here, because quasi-coherence of the denominator ideal makes that family
> compatible with passage to a basic open, so it is already an ideal sheaf.

```lean
theorem denominatorIdealData_ideal
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L)
    (U : X.affineOpens) :
    (denominatorIdealData X L s).ideal U =
      ((denominatorIdealι X L s).val.app (op U.1)).hom.range
```

**`Stacks.DenominatorIdealQcoh.denominatorIdealData_support_isNowhereDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/IdealData.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorIdealQcoh/IdealData.lean#L204). The attribute's comment: “support of the denominator ideal”.

> **The closed support of the denominator ideal is nowhere dense.**
>
> Around every point of every open set there is an affine open carrying a nonzerodivisor `b` which
> is a denominator of `s`, so `(b) ⊆ I` there and the support is contained in `V(b)`, which has
> empty interior.  Shrinking freely is legitimate because the nowhere-density argument runs on an
> affine open of its own choosing inside the interior of the support.

```lean
theorem denominatorIdealData_support_isNowhereDense
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L) :
    IsNowhereDense ((denominatorIdealData X L s).support : Set X)
```

**`Stacks.DenominatorCokernel.denominatorIdeal_inclusion_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorLocalRatio/Cokernels.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorLocalRatio/Cokernels.lean#L189). The attribute's comment: “support of the first cokernel”.

> **The cokernel of the inclusion of the denominator ideal in the structure sheaf is supported
> on a closed nowhere dense subset.**

```lean
theorem denominatorIdeal_inclusion_support
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L) :
    ∃ T : Set X, IsClosed T ∧ IsNowhereDense T ∧
      (asModuleSheaf X (cokernel (denominatorIdealι X L s))).supp ⊆ T
```

**`Stacks.DenominatorCokernel.denominatorIdeal_section_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DenominatorLocalRatio/MulCokernel.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DenominatorLocalRatio/MulCokernel.lean#L112). The attribute's comment: “support of the second cokernel”.

> **The cokernel of multiplication by a regular meromorphic section of an invertible sheaf is
> supported on a closed nowhere dense subset.**  Stacks Tag 02P0, "support of the second
> cokernel".

```lean
theorem denominatorIdeal_section_support
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf (O X).property L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    ∃ T : Set X, IsClosed T ∧ IsNowhereDense T ∧
      (asModuleSheaf X (cokernel (denominatorIdealMul X L s))).supp ⊆ T
```

**`AlgebraicGeometry.exists_denominatorIdeal_inclusion_app_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorRule.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorRule.lean#L93). The attribute's comment: “the denominator rule”.

> **Stacks Project, Tag 02P0**, the denominator rule. A section `f` of `𝒪_X` over `V` lies in
> the ideal of denominators of a meromorphic section `s` of `L` exactly when `f s` is a section
> of `L` over `V`; here "lies in the ideal" means that `f` is the image of a section of the fibre
> product under the ideal inclusion, and "`f s` is a section of `L`" means that `f s` is the
> image of a section of `L` under the canonical map `L ⟶ K_X(L)`.

```lean
theorem exists_denominatorIdeal_inclusion_app_eq_iff
    (L : SheafOfModules.{u}
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf))
    (s : MeromorphicSection X.sheaf L) (V : Opens X)
    (f : (SheafOfModules.unit
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf)).val.obj
        (op V)) :
    (∃ d : (denominatorIdeal X L s).val.obj (op V),
      (denominatorIdealι X L s).val.app (op V) d = f) ↔
    (∃ t : L.val.obj (op V),
      (meromorphicSectionMul X L s).val.app (op V) f =
        (toMeromorphicSectionSheafAsModule X L).val.app (op V) t)
```

**`AlgebraicGeometry.denominatorIdeal_section_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Denominators.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Denominators.lean#L241). The attribute's comment: “multiplication is injective”.

> **Stacks Project, Tag 02P0**, injectivity of multiplication by the section. For a regular
> meromorphic section `s` of `L`, multiplication by `s` embeds the ideal of denominators of `s`
> in `L`.

```lean
theorem denominatorIdeal_section_mono
    (L : SheafOfModules.{u}
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf))
    (s : MeromorphicSection X.sheaf L)
    (_hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    Mono (denominatorIdealMul X L s)
```

**`AlgebraicGeometry.denominatorIdeal_inclusion_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorsInclusion.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DenominatorsInclusion.lean#L473). The attribute's comment: “inclusion is injective”.

> **Stacks Project, Tag 02P0**, injectivity of the ideal inclusion. For an invertible sheaf of
> modules `L` and a meromorphic section `s` of `L`, the ideal of denominators of `s` embeds in the
> structure sheaf.

```lean
theorem denominatorIdeal_inclusion_mono
    (L : SheafOfModules.{u}
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf))
    (s : MeromorphicSection X.sheaf L)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L) :
    Mono (denominatorIdealι X L s)
```

**`AlgebraicGeometry.denominatorIdealData_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorIdealData.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorIdealData.lean#L228). The attribute's comment: “affine denominator ideal”.

> **Stacks Project, Tag 02P0**, the affine denominator ideal. For an invertible sheaf of
> modules `L` and a meromorphic section `s` of `L`, the component of
> `AlgebraicGeometry.denominatorIdealData` at an affine open `U` is exactly the range of the
> inclusion of the ideal of denominators on sections over `U`: assembling the ideal sheaf from
> those ranges by `AlgebraicGeometry.Scheme.IdealSheafData.ofIdeals` does not shrink any of
> them.

```lean
theorem denominatorIdealData_ideal
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L)
    (U : X.affineOpens) :
    (denominatorIdealData X L s).ideal U =
      ((denominatorIdealι X L s).val.app (op U.1)).hom.range
```

**`AlgebraicGeometry.denominatorIdealData_support_isNowhereDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorIdealData.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorIdealData.lean#L256). The attribute's comment: “support of the denominator ideal”.

> **Stacks Project, Tag 02P0**, the support of the ideal of denominators. For an invertible
> sheaf of modules `L` and a meromorphic section `s` of `L`, the support of
> `AlgebraicGeometry.denominatorIdealData` is a nowhere dense subset of `X`.
>
> It is contained in the complement of the union, over the points of `X`, of the part of the
> affine neighbourhood produced by
> `AlgebraicGeometry.exists_isAffineOpen_nhds_isNowhereDense_denominator` on which the denominator
> `b` found there is invertible: on an affine open inside such a set the ideal inclusion is
> surjective on sections, so by `AlgebraicGeometry.denominatorIdealData_ideal` the component of
> the ideal sheaf there is the unit ideal and its zero locus contains no point of that open. The
> union is dense because the vanishing locus of a nonzerodivisor on an affine open is nowhere
> dense, so its complement is nowhere dense.

```lean
theorem denominatorIdealData_support_isNowhereDense
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L) :
    IsNowhereDense ((denominatorIdealData X L s).support : Set X)
```

**`AlgebraicGeometry.denominatorIdeal_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorQuasicoherent.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorQuasicoherent.lean#L411). The attribute's comment: “quasi-coherence”. References: EGA IV (20.2.14), “special case”.

> **Stacks Project, Tag 02P0**, quasi-coherence of the ideal of denominators. For an
> invertible sheaf of modules `L` and a meromorphic section `s` of `L`, the ideal of denominators
> of `s` is a quasi-coherent sheaf of ideals.
>
> Quasi-coherence is checked by the localization criterion on the affine opens contained in the
> neighbourhoods of `AlgebraicGeometry.exists_isAffineOpen_nhds_denominator_numerator_isUnit`,
> which cover `X`. There the sections of the ideal are cut out by the colon condition
> `f · a ∈ (b)` of
> `AlgebraicGeometry.exists_denominatorIdeal_inclusion_app_eq_iff_mul_eq_of_le`, and a colon
> condition localizes by `AlgebraicGeometry.isLocalizedModule_restrictₗ_of_colon`. Regularity of
> `s` is not used: the source assumes it throughout Tag 02P0, but of its conclusions only
> injectivity of multiplication by `s` and the support of that map's cokernel need it.

```lean
theorem denominatorIdeal_isQuasicoherent
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L) :
    (denominatorIdeal X L s).IsQuasicoherent
```

**`AlgebraicGeometry.denominatorIdeal_inclusion_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorSupport.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorSupport.lean#L350). The attribute's comment: “support of the first cokernel”.

> **Stacks Project, Tag 02P0**, the support of the first cokernel. For an invertible sheaf of
> modules `L` and a meromorphic section `s` of `L`, the cokernel of the inclusion of the ideal of
> denominators of `s` in the structure sheaf is supported on a closed nowhere dense subset.
>
> The set is the complement of the union, over the points of `X`, of the part of the affine
> neighbourhood produced by
> `AlgebraicGeometry.exists_isAffineOpen_nhds_isNowhereDense_denominator` on which the
> denominator `b` found there is invertible. On each such open set the whole structure sheaf
> consists of denominators, because `b` lies in the ideal and is a unit, so the cokernel has no
> sections there; and the union is dense because the vanishing locus of a nonzerodivisor on an
> affine open is nowhere dense.

```lean
theorem denominatorIdeal_inclusion_support
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L) :
    ∃ T : Set X, IsClosed T ∧ IsNowhereDense T ∧
      (⟨(cokernel (denominatorIdealι X L s)).val,
        (cokernel (denominatorIdealι X L s)).isSheaf⟩ :
          RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp ⊆ T
```

**`AlgebraicGeometry.denominatorIdeal_section_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorSupport.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Meromorphic/DenominatorSupport.lean#L580). The attribute's comment: “support of the second cokernel”.

> **Stacks Project, Tag 02P0**, the support of the second cokernel. For an invertible sheaf of
> modules `L` and a *regular* meromorphic section `s` of `L`, the cokernel of multiplication by
> `s` on the ideal of denominators of `s` is supported on a closed nowhere dense subset.
>
> The set is the complement of the union, over the points of `X`, of the part of the affine
> neighbourhood produced by
> `AlgebraicGeometry.exists_isAffineOpen_nhds_denominator_numerator` on which the numerator `a`
> found there is invertible. On each such open set every section of `L` is `d · s` for a
> denominator `d`, because `L` is generated by `g` and `b · s = a · g` with `a` a unit; and the
> union is dense because `a` is a nonzerodivisor
> (`AlgebraicGeometry.numerator_mem_nonZeroDivisors`, which is where regularity of `s` enters)
> and the vanishing locus of a nonzerodivisor on an affine open is nowhere dense.

```lean
theorem denominatorIdeal_section_support
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    ∃ T : Set X, IsClosed T ∧ IsNowhereDense T ∧
      (⟨(cokernel (denominatorIdealMul X L s)).val,
        (cokernel (denominatorIdealMul X L s)).isSheaf⟩ :
          RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp ⊆ T
```

## Tag 02P1, a definition

[Tag 02P1](https://stacks.math.columbia.edu/tag/02P1) in the Stacks Project.

**`AlgebraicGeometry.denominatorIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Denominators.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Denominators.lean#L190). The attribute's comment: “the ideal sheaf of denominators of `s`”. References: EGA IV (20.2.14), “definition”.

> The sheaf of denominators of a meromorphic section, as the fibre product of the structure
> sheaf and `L` over `K_X(L)`. Its sections over `V` are the pairs `(f, t)` with `f s = t` in
> `K_X(L)(V)`, so the image of its first projection is `{f ∈ 𝒪_X(V) | f s ∈ L(V)}`.

```lean
def denominatorIdeal
    (L : SheafOfModules.{u}
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf))
    (s : MeromorphicSection X.sheaf L) :
    SheafOfModules.{u} (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X)
      X.sheaf)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.24, Tag 01X1](https://stacks.math.columbia.edu/tag/01X1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
