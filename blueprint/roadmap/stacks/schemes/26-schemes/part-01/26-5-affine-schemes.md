---
declaration: section
origin: cited
lean: Stacks.Cohomology.Cech.exists_isStandardOpenCoverOfSpectrum_refinement, PrimeSpectrum.ringRestrictionMap, PrimeSpectrum.ringRestrictionMap_unique, PrimeSpectrum.moduleRestrictionMap, PrimeSpectrum.moduleRestrictionMap_mk, PrimeSpectrum.moduleRestrictionMap_unique, PrimeSpectrum.basicOpen_le_iSup_iff_span_algebraMap_eq_top, PrimeSpectrum.exists_finite_basicOpen_refinement
statement: formalized
proof: formalized
---

# 26.5 Affine schemes

Section 26.5 of the Stacks Project, [Tag 01HR](https://stacks.math.columbia.edu/tag/01HR). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 20 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01HS, a lemma

[Tag 01HS](https://stacks.math.columbia.edu/tag/01HS) in the Stacks Project.

**`Stacks.Cohomology.Cech.exists_isStandardOpenCoverOfSpectrum_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Cech/StandardCoverCofinality.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Cech/StandardCoverCofinality.lean#L105). The attribute's comment: “part (2), for an affine open of a scheme”.

> **Any open covering of an affine open of a scheme is refined by a finite standard open
> covering of it.** This is the scheme-level form of [Stacks, Tag 01HS] part (2), and it is
> condition (2) of [Stacks, Tag 01EW] for the system of finite standard open coverings of affine
> opens: the returned family `g` of sections over `U` satisfies the standard-covering condition of
> [Stacks, Tag 01HT], its ambient basic opens cover `U`, and each of them is contained in a member
> of the given family.

```lean
theorem exists_isStandardOpenCoverOfSpectrum_refinement {U : X.Opens} (hU : IsAffineOpen U)
    {ι : Type v} (W : ι → X.Opens) (hW : U ≤ ⨆ i, W i) :
    ∃ (n : ℕ) (g : Fin n → Γ(X, U)) (a : Fin n → ι),
      PrimeSpectrum.IsStandardOpenCoverOfSpectrum g ∧ (⨆ j, X.basicOpen (g j)) = U ∧
        ∀ j, X.basicOpen (g j) ≤ W (a j)
```

**`PrimeSpectrum.ringRestrictionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean#L55). The attribute's comment: “ring\_restriction\_map”.

> The canonical `R`-algebra map `R_f → R_g` attached to an inclusion `D(g) ⊆ D(f)`.

```lean
noncomputable def ringRestrictionMap {R : Type u} [CommRing R] (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) :
    Localization.Away f →ₐ[R] Localization.Away g
```

**`PrimeSpectrum.ringRestrictionMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean#L66). The attribute's comment: “ring\_restriction\_map”.

> The restriction map is canonical: it is the unique `R`-algebra
> homomorphism from `R_f` to `R_g`.

```lean
theorem ringRestrictionMap_unique {R : Type u} [CommRing R] (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f)
    (φ : Localization.Away f →ₐ[R] Localization.Away g) :
    φ = ringRestrictionMap f g hfg
```

**`PrimeSpectrum.moduleRestrictionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean#L76). The attribute's comment: “module\_restriction\_map”.

> The canonical `R_f`-linear restriction map `M_f → M_g` associated to an inclusion
> `D(g) ⊆ D(f)`.

```lean
noncomputable def moduleRestrictionMap {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) :
    let φ := ringRestrictionMap f g hfg
    letI := Module.compHom (R := Localization.Away g) (S := Localization.Away f)
      (LocalizedModule.Away (R := R) g M) φ.toRingHom
    LocalizedModule.Away (R := R) f M →ₗ[Localization.Away f]
      LocalizedModule.Away (R := R) g M
```

**`PrimeSpectrum.moduleRestrictionMap_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean#L118). The attribute's comment: “module\_restriction\_map”.

> The module restriction map agrees with the canonical localization maps on
> elements of `M`.

```lean
theorem moduleRestrictionMap_mk {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) (m : M) :
    moduleRestrictionMap f g hfg
        (LocalizedModule.mkLinearMap (Submonoid.powers f) M m) =
      LocalizedModule.mkLinearMap (Submonoid.powers g) M m
```

**`PrimeSpectrum.moduleRestrictionMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/RestrictionMaps.lean#L130). The attribute's comment: “module\_restriction\_map”.

> An `R_f`-linear map `M_f → M_g` which agrees with the localization maps
> from `M` is the canonical module restriction map.

```lean
theorem moduleRestrictionMap_unique {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f)
    (F :
      let φ := ringRestrictionMap f g hfg
      letI := Module.compHom (R := Localization.Away g) (S := Localization.Away f)
        (LocalizedModule.Away (R := R) g M) φ.toRingHom
      LocalizedModule.Away (R := R) f M →ₗ[Localization.Away f]
        LocalizedModule.Away (R := R) g M)
    (hF : ∀ m : M,
      F (LocalizedModule.mkLinearMap (Submonoid.powers f) M m) =
        LocalizedModule.mkLinearMap (Submonoid.powers g) M m) :
    F = moduleRestrictionMap f g hfg
```

**`PrimeSpectrum.basicOpen_le_iSup_iff_span_algebraMap_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L66). The attribute's comment: “cover\_iff\_unit\_ideal”.

> A standard open `D(f)` is contained in the union of the standard opens `D(g i)` if and only
> if the images of the `g i` generate the unit ideal after localizing away from `f`.

```lean
theorem basicOpen_le_iSup_iff_span_algebraMap_eq_top
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S]
    {ι : Type w} (f : R) [IsLocalization.Away f S] (g : ι → R) :
      PrimeSpectrum.basicOpen f ≤ ⨆ i, PrimeSpectrum.basicOpen (g i) ↔
      Ideal.span (Set.range fun i ↦ algebraMap R S (g i)) = ⊤
```

**`PrimeSpectrum.exists_finite_basicOpen_refinement`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L88). The attribute's comment: “finite\_standard\_refinement”.

> Every open cover of a standard open in the prime spectrum has a finite
> refinement by standard opens.

```lean
lemma exists_finite_basicOpen_refinement {R : Type u} [CommSemiring R]
    {ι : Type*} (f : R) (U : ι → Opens (PrimeSpectrum R))
    (hU : PrimeSpectrum.basicOpen f ≤ ⨆ i, U i) :
    ∃ (n : ℕ) (g : Fin n → R) (a : Fin n → ι),
      PrimeSpectrum.basicOpen f = ⨆ j, PrimeSpectrum.basicOpen (g j) ∧
        ∀ j, PrimeSpectrum.basicOpen (g j) ≤ U (a j)
```

**`PrimeSpectrum.exists_pow_eq_mul_of_basicOpen_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L128). The attribute's comment: “power\_divisible”. References: EGA I (1.1.9), “partial”.

> If `D(g) ⊆ D(f)`, a positive power of `g` is a multiple of `f`.

```lean
theorem exists_pow_eq_mul_of_basicOpen_le {R : Type*} [CommRing R] {f g : R}
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) :
    ∃ e : ℕ, 1 ≤ e ∧ ∃ a : R, g ^ e = a * f
```

Declarations registered for the tag:

- [`PrimeSpectrum.basicOpen_le_basicOpen_iff_algebraMap_isUnit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.basicOpen_le_basicOpen_iff_algebraMap_isUnit#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L44) (StacksFrontier): “invertible\_on\_smaller\_open”. References: EGA I (1.3.2), “(a) ⇔ (f)”.

## Tag 01HT, a definition

[Tag 01HT](https://stacks.math.columbia.edu/tag/01HT) in the Stacks Project.

**`PrimeSpectrum.IsStandardOpenCover`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L55). The attribute's comment: “part (2)”.

> A family `D(g i)`, indexed by `Fin n`, is a standard open covering of `D(f)` when its
> supremum is `D(f)`.

```lean
def IsStandardOpenCover {R : Type u} [CommRing R] (f : R) {n : ℕ} (g : Fin n → R) : Prop
```

**`PrimeSpectrum.IsStandardOpenCoverOfSpectrum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Zariski/StandardOpenCover.lean#L60). The attribute's comment: “part (1)”.

> A standard open covering of `Spec R`, expressed as the case `D(1) = Spec R`.

```lean
abbrev IsStandardOpenCoverOfSpectrum {R : Type u} [CommRing R] {n : ℕ} (g : Fin n → R) : Prop
```

## Tag 01HU, a definition

[Tag 01HU](https://stacks.math.columbia.edu/tag/01HU) in the Stacks Project.

Declarations registered for the tag:

- [`Spec.structureSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Spec.structureSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L82) (StacksFrontier): “(1) the structure sheaf”.
- [`StructureSheaf.IsLocalization.to_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=StructureSheaf.IsLocalization.to_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L83) (StacksFrontier): “(1) its sections over a standard open D(f) are the localization R\_f”.
- [`Spec.locallyRingedSpaceObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Spec.locallyRingedSpaceObj#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L85) (StacksFrontier): “(2) the spectrum as a locally ringed space”.
- [`tilde`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=tilde#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L86) (StacksFrontier): “(3) the sheaf of modules associated to a module”.

## Tag 01HV, a lemma

[Tag 01HV](https://stacks.math.columbia.edu/tag/01HV) in the Stacks Project.

**`AlgebraicGeometry.tilde.basicOpen_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L146). The attribute's comment: “functorial\_identifications”.

> Under the canonical localization identifications, the map on sections
> over a standard open induced by a module map is its localization.

```lean
theorem basicOpen_map {R : CommRingCat.{u}} {M N : ModuleCat.{u} R}
    (f : M ⟶ N) (a : R) (m : LocalizedModule.Away (R := R) a M) :
    ((modulesSpecToSheaf.map (tilde.map f)).1.app
        (.op (PrimeSpectrum.basicOpen a)))
      ((IsLocalizedModule.iso (Submonoid.powers a)
        (tilde.toOpen M (PrimeSpectrum.basicOpen a)).hom) m) =
      (IsLocalizedModule.iso (Submonoid.powers a)
        (tilde.toOpen N (PrimeSpectrum.basicOpen a)).hom)
        (IsLocalizedModule.map (Submonoid.powers a)
          (LocalizedModule.mkLinearMap (Submonoid.powers a) M)
          (LocalizedModule.mkLinearMap (Submonoid.powers a) N) f.hom m)
```

**`AlgebraicGeometry.tilde.toStalk_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L179). The attribute's comment: “functorial\_identifications”.

> The canonical identification of the stalk of an associated sheaf with
> localization at a prime is natural in the module.

```lean
theorem toStalk_map {R : CommRingCat.{u}} {M N : ModuleCat.{u} R}
    (f : M ⟶ N) (x : PrimeSpectrum.Top R)
    (m : (tilde M).presheaf.stalk x) :
    ((TopCat.Presheaf.stalkFunctor Ab x).map
      (Scheme.Modules.Hom.mapPresheaf (tilde.map f))) m =
      IsLocalizedModule.map x.asIdeal.primeCompl
        (tilde.toStalk M x).hom (tilde.toStalk N x).hom f.hom m
```

**`AlgebraicGeometry.StructureSheaf.map_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L79). The attribute's comment: “restriction\_maps”.

> Under the canonical identifications of sections on standard opens with localizations,
> restriction in the structure sheaf is the canonical map `R_f → R_g`.

```lean
theorem map_basicOpen {R : CommRingCat.{u}} (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) :
    ((AlgebraicGeometry.Spec.structureSheaf R).obj.map (homOfLE hfg).op).hom.comp
        (IsLocalization.algEquiv (Submonoid.powers f) (Localization.Away f)
          ((AlgebraicGeometry.Spec.structureSheaf R).obj.obj
            (.op (PrimeSpectrum.basicOpen f)))).toRingHom =
      (IsLocalization.algEquiv (Submonoid.powers g) (Localization.Away g)
        ((AlgebraicGeometry.Spec.structureSheaf R).obj.obj
          (.op (PrimeSpectrum.basicOpen g)))).toRingHom.comp
        (PrimeSpectrum.ringRestrictionMap f g hfg).toRingHom
```

**`AlgebraicGeometry.tilde.map_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L116). The attribute's comment: “restriction\_maps”.

> Sections of the associated sheaf on `D(f)` and `D(g)` are canonically isomorphic to `M_f`
> and `M_g`. The isomorphisms identify sheaf restriction with the canonical map `M_f → M_g`.

```lean
theorem map_basicOpen {R : CommRingCat.{u}} (M : ModuleCat.{u} R) (f g : R)
    (hfg : PrimeSpectrum.basicOpen g ≤ PrimeSpectrum.basicOpen f) :
    ∀ x : LocalizedModule.Away (R := R) f M,
      (modulesSpecToSheaf.obj (tilde M)).presheaf.map (homOfLE hfg).op
          ((IsLocalizedModule.iso (Submonoid.powers f)
            (tilde.toOpen M (PrimeSpectrum.basicOpen f)).hom) x) =
        (IsLocalizedModule.iso (Submonoid.powers g)
          (tilde.toOpen M (PrimeSpectrum.basicOpen g)).hom)
            (PrimeSpectrum.moduleRestrictionMap f g hfg x)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.tilde.functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.functor#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L32) (StacksFrontier): “functorial\_identifications”. References: EGA I (1.3.5); EGA II (1.4.4), “partial”.
- [`AlgebraicGeometry.tilde.toOpen_map_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.toOpen_map_app#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L35) (StacksFrontier): “functorial\_identifications”.
- [`AlgebraicGeometry.tilde.toTildeΓNatIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.toTildeΓNatIso#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L36) (StacksFrontier): “functorial\_identifications”. References: EGA I (1.3.7); EGA I (10.10.2), “(i), special case”.
- [`AlgebraicGeometry.instIsLeftAdjointModuleCatCarrierModulesSpecFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsLeftAdjointModuleCatCarrierModulesSpecFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Functoriality.lean#L39) (StacksFrontier): “tilde\_exact”.
- [`AlgebraicGeometry.StructureSheaf.globalSectionsIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.StructureSheaf.globalSectionsIso#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L48) (StacksFrontier): “global\_structure\_sections”. References: EGA I (1.3.7), “Case M = A”; EGA I (10.1.3), “special case”.
- [`AlgebraicGeometry.tilde.isoTop`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.isoTop#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L51) (StacksFrontier): “global\_module\_sections”. References: EGA I (1.3.7); EGA I (10.10.2), “(i), special case”.
- [`AlgebraicGeometry.StructureSheaf.IsLocalization.to_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.StructureSheaf.IsLocalization.to_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L54) (StacksFrontier): “basic\_open\_structure\_sections”. References: EGA I (9.3.2), “special case”; EGA I (9.3.3), “special case”; EGA III (1.2.2), “special case”.
- [`AlgebraicGeometry.tilde.instAwayCarrierCarrierObjOppositeOpensCarrierCarrierCommRingCatSpecModuleCatPresheafModulesSheafModulesSpecToSheafOpBasicOpenHomToOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.instAwayCarrierCarrierObjOppositeOpensCarrierCarrierCommRingCatSpecModuleCatPresheafModulesSheafModulesSpecToSheafOpBasicOpenHomToOpen#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L59) (StacksFrontier): “basic\_open\_module\_sections”.
- [`AlgebraicGeometry.StructureSheaf.IsLocalization.to_stalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.StructureSheaf.IsLocalization.to_stalk#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L68) (StacksFrontier): “structure\_stalk”.
- [`AlgebraicGeometry.tilde.instIsLocalizedModuleCarrierCarrierOfCarrierStalkAbPresheafPrimeComplAsIdealHomToStalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tilde.instIsLocalizedModuleCarrierCarrierOfCarrierStalkAbPresheafPrimeComplAsIdealHomToStalk#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/Sections.lean#L69) (StacksFrontier): “module\_stalk”.
- [`AlgebraicGeometry.tilde.preservesFiniteLimits`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Modules/TildeExactness.lean#L54), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean#L276) (StacksFrontier): “tilde\_exact: left exactness”.
- [`Stacks.AffineTilde.tildeFunctor_preservesHomology`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean#L265), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherentRelative/TildeExact.lean#L278) (StacksFrontier): “tilde\_exact: exactness as preservation of homology”.

## Tag 01HW, a definition

[Tag 01HW](https://stacks.math.columbia.edu/tag/01HW) in the Stacks Project.

Declarations registered for the tag:

- [`AffineScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AffineScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L88) (StacksFrontier): “the category of affine schemes, schemes isomorphic to some Spec R”.
- [`essImage_Spec`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=essImage_Spec#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L90) (StacksFrontier): “being isomorphic to some Spec R is being affine”.
- [`Scheme.fullyFaithfulForgetToLocallyRingedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.fullyFaithfulForgetToLocallyRingedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L91) (StacksFrontier): “morphisms of schemes are the morphisms of locally ringed spaces”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.5, Tag 01HR](https://stacks.math.columbia.edu/tag/01HR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
