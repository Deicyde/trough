---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension, AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension_lt_top_of_finiteType, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_lt_top_of_finiteType, Stacks.EtaleCohomology.preservesColimitsOfShape_derivedDirectImage_zmod, Stacks.EtaleCohomology.preservesColimitsOfShape_derivedGlobalSections_zmod, Stacks.EtaleCohomology.preservesColimitsOfShape_derivedDirectImage_of_natCast_eq_zero, Stacks.EtaleCohomology.preservesColimitsOfShape_derivedGlobalSections_of_natCast_eq_zero, Stacks.EtaleCohomology.preservesColimitsOfShape_etaleModuleDerivedDirectImageUnbounded_of_isProper
statement: formalized
proof: formalized
---

# 59.96 Finite cohomological dimension

Section 59.96 of the Stacks Project, [Tag 0F0Y](https://stacks.math.columbia.edu/tag/0F0Y). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F0Z, a definition

[Tag 0F0Z](https://stacks.math.columbia.edu/tag/0F0Z) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension.lean#L163).

> **Stacks Project, Tag 0F0Z.** The cohomological dimension `cd(f)` of a quasi-compact,
> quasi-separated morphism of schemes `f : X ⟶ Y`: the smallest `d ∈ {0, 1, 2, …} ∪ {∞}` such
> that `R^i f_* F = 0` for every abelian torsion sheaf `F` on `X_ét` and every `i > d`.

```lean
public def etaleCohomologicalDimension [QuasiCompact f] [QuasiSeparated f] : ℕ∞
```

## Tag 0F10, a lemma

[Tag 0F10](https://stacks.math.columbia.edu/tag/0F10) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension_lt_top_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FiniteType.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FiniteType.lean#L93). The attribute's comment: “(1): cd(f) < ∞ for a morphism of schemes of finite type over a field”.

> **Stacks Project, Tag 0F10, part (1).** A morphism `f : X ⟶ Y` of schemes of finite type
> over a field `K` has finite cohomological dimension: `cd(f) < ∞`.

```lean
theorem Hom.etaleCohomologicalDimension_lt_top_of_finiteType (K : Type u) [Field K]
    {X Y : Scheme.{u}} (x : X ⟶ Spec (.of K)) [LocallyOfFiniteType x] [QuasiCompact x]
    (y : Y ⟶ Spec (.of K)) [LocallyOfFiniteType y] [QuasiCompact y] (f : X ⟶ Y)
    (hf : f ≫ y = x) :
    haveI := quasiCompact_of_finiteType K x y f
    haveI := quasiSeparated_of_finiteType K x f
    f.etaleCohomologicalDimension < ⊤
```

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_lt_top_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FiniteTypeAbsolute.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FiniteTypeAbsolute.lean#L48). The attribute's comment: “(2): cd(X) < ∞ for X of finite type over a field K with cd(K) < ∞”.

> **Stacks Project, Tag 0F10, part (2).** If the field `K` has finite cohomological dimension
> `cd(K) = cd(Spec K) < ∞`, then every scheme `X` of finite type over `K` has finite cohomological
> dimension: `cd(X) < ∞`.

```lean
theorem etaleCohomologicalDimension_lt_top_of_finiteType (K : Type u) [Field K]
    {X : Scheme.{u}} (x : X ⟶ Spec (.of K)) [LocallyOfFiniteType x] [QuasiCompact x]
    (hK : etaleCohomologicalDimension (Spec (.of K)) < ⊤) :
    haveI : CompactSpace X := compactSpace_of_finiteType K x
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_finiteType K x
    etaleCohomologicalDimension X < ⊤
```

## Tag 0F11, a lemma

[Tag 0F11](https://stacks.math.columbia.edu/tag/0F11) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesColimitsOfShape_derivedDirectImage_zmod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean#L422). The attribute's comment: “(1): Rf\_* : D(X\_étale, ℤ/nℤ) ⟶ D(Y\_étale, ℤ/nℤ) commutes with direct sums for f quasi-compact and quasi-separated with cd(f) < ∞, n ≥ 1”.

> **[Stacks, Tag 0F11] (1).** Let `n ≥ 1` and let `f : X ⟶ Y` be a quasi-compact and
> quasi-separated morphism of schemes with `cd(f) < ∞`. Then the unbounded derived direct image
> `Rf_* : D(X_étale, ℤ/nℤ) ⟶ D(Y_étale, ℤ/nℤ)` commutes with direct sums.
>
> Here `cd(f)` is `AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension`, Tag 0F0Z, and
> `Rf_*` is any unbounded right derived functor of the direct image of sheaves of `ℤ/nℤ`-modules.
> The two inputs of the argument of the source are proved: the uniform vanishing of the higher
> direct images on sheaves of `ℤ/nℤ`-modules is
> `Stacks.EtaleCohomology.exists_isZero_rightDerived_etaleModuleDirectImage_zmod`, and their
> commuting with direct sums (Tag 09Z1 for a constant system) is
> `Stacks.EtaleCohomology.preservesColimitsOfShape_discrete_rightDerived_etaleModuleDirectImage`.

```lean
theorem preservesColimitsOfShape_derivedDirectImage_zmod
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f] [QuasiSeparated f]
    (hcd : f.etaleCohomologicalDimension < ⊤) (n : ℕ) (hn : 0 < n)
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} (ZMod n) X)]
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} (ZMod n) Y)]
    (RF : DerivedCategory (EtaleModules.{u, 0} (ZMod n) X) ⥤
      DerivedCategory (EtaleModules.{u, 0} (ZMod n) Y))
    (α : (etaleModuleDirectImage.{u, 0} (ZMod n) f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (EtaleModules.{u, 0} (ZMod n) X) (ComplexShape.up ℤ))]
    (I : Type (u + 1)) :
    PreservesColimitsOfShape (Discrete I) RF
```

**`Stacks.EtaleCohomology.preservesColimitsOfShape_derivedGlobalSections_zmod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean#L498). The attribute's comment: “(2): RΓ(X, -) : D(X\_étale, ℤ/nℤ) ⟶ D(ℤ/nℤ) commutes with direct sums for X quasi-compact and quasi-separated with cd(X) < ∞, n ≥ 1”.

> **[Stacks, Tag 0F11] (2).** Let `n ≥ 1` and let `X` be a quasi-compact and quasi-separated
> scheme with `cd(X) < ∞`. Then the unbounded derived global sections
> `RΓ(X, -) : D(X_étale, ℤ/nℤ) ⟶ D(ℤ/nℤ)` commute with direct sums.
>
> Here `cd(X)` is `AlgebraicGeometry.Scheme.etaleCohomologicalDimension`, Tag 0F0Q, and
> `RΓ(X, -)` is any unbounded right derived functor of global sections of sheaves of
> `ℤ/nℤ`-modules. The two inputs of the argument of the source are proved: the uniform vanishing of
> the cohomology of sheaves of `ℤ/nℤ`-modules is
> `Stacks.EtaleCohomology.exists_isZero_rightDerived_etaleModuleGlobalSections_zmod`, and its
> commuting with direct sums is
> `preservesColimitsOfShape_discrete_rightDerived_etaleModuleGlobalSections`.

```lean
theorem preservesColimitsOfShape_derivedGlobalSections_zmod
    (hcd : Scheme.etaleCohomologicalDimension X < ⊤)
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} (ZMod n) X)]
    [HasDerivedCategory.{z} (ModuleCat.{u + 1} (ZMod n))]
    (RF : DerivedCategory (EtaleModules.{u, 0} (ZMod n) X) ⥤
      DerivedCategory (ModuleCat.{u + 1} (ZMod n)))
    (α : (etaleModuleGlobalSections.{u, 0} (ZMod n) X).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (EtaleModules.{u, 0} (ZMod n) X) (ComplexShape.up ℤ))]
    (I : Type (u + 1)) :
    PreservesColimitsOfShape (Discrete I) RF
```

**`Stacks.EtaleCohomology.preservesColimitsOfShape_derivedDirectImage_of_natCast_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean#L571). The attribute's comment: “(1): Rf\_* : D(X\_étale, Λ) ⟶ D(Y\_étale, Λ) commutes with direct sums for f quasi-compact and quasi-separated with cd(f) < ∞, for every commutative ring Λ with n = 0 in Λ for some n ≥ 1 (the source's case is Λ = ℤ/nℤ)”.

> **[Stacks, Tag 0F11] (1).** Let `n ≥ 1` and let `f : X ⟶ Y` be a quasi-compact and
> quasi-separated morphism of schemes with `cd(f) < ∞`. Then
> `Rf_* : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` commutes with direct sums, for every commutative ring `Λ`
> in which `n = 0`; the source's case is `Λ = ℤ/nℤ`.
>
> Here `cd(f)` is `AlgebraicGeometry.Scheme.Hom.etaleCohomologicalDimension`, [Stacks, Tag 0F0Z],
> and `Rf_*` is any unbounded right derived functor `RF` of the direct image of sheaves of
> `Λ`-modules on the small étale sites, with derivation unit `α`, in any model of the two derived
> categories.

```lean
theorem preservesColimitsOfShape_derivedDirectImage_of_natCast_eq_zero
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f] [QuasiSeparated f]
    (hcd : f.etaleCohomologicalDimension < ⊤)
    (Λ : Type) [CommRing Λ] (n : ℕ) (hn : 0 < n) (hΛ : (n : Λ) = 0)
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} Λ X)]
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} Λ Y)]
    (RF : DerivedCategory (EtaleModules.{u, 0} Λ X) ⥤ DerivedCategory (EtaleModules.{u, 0} Λ Y))
    (α : (etaleModuleDirectImage.{u, 0} Λ f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (EtaleModules.{u, 0} Λ X) (ComplexShape.up ℤ))]
    (I : Type (u + 1)) :
    PreservesColimitsOfShape (Discrete I) RF
```

**`Stacks.EtaleCohomology.preservesColimitsOfShape_derivedGlobalSections_of_natCast_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionCoefficientsDirectSums.lean#L600). The attribute's comment: “(2): RΓ(X, -) : D(X\_étale, Λ) ⟶ D(Λ) commutes with direct sums for X quasi-compact and quasi-separated with cd(X) < ∞, for every commutative ring Λ with n = 0 in Λ for some n ≥ 1 (the source's case is Λ = ℤ/nℤ)”.

> **[Stacks, Tag 0F11] (2).** Let `n ≥ 1` and let `X` be a quasi-compact and quasi-separated
> scheme with `cd(X) < ∞`. Then `RΓ(X, -) : D(X_étale, Λ) ⟶ D(Λ)` commutes with direct sums, for
> every commutative ring `Λ` in which `n = 0`; the source's case is `Λ = ℤ/nℤ`.
>
> Here `cd(X)` is `AlgebraicGeometry.Scheme.etaleCohomologicalDimension`, [Stacks, Tag 0F0Q], and
> `RΓ(X, -)` is any unbounded right derived functor `RF` of the global sections of sheaves of
> `Λ`-modules on the small étale site, with derivation unit `α`, in any model of the two derived
> categories.

```lean
theorem preservesColimitsOfShape_derivedGlobalSections_of_natCast_eq_zero
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (hcd : Scheme.etaleCohomologicalDimension X < ⊤)
    (Λ : Type) [CommRing Λ] (n : ℕ) (hn : 0 < n) (hΛ : (n : Λ) = 0)
    [HasDerivedCategory.{z} (EtaleModules.{u, 0} Λ X)]
    [HasDerivedCategory.{z} (ModuleCat.{u + 1} Λ)]
    (RF : DerivedCategory (EtaleModules.{u, 0} Λ X) ⥤ DerivedCategory (ModuleCat.{u + 1} Λ))
    (α : (etaleModuleGlobalSections.{u, 0} Λ X).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (EtaleModules.{u, 0} Λ X) (ComplexShape.up ℤ))]
    (I : Type (u + 1)) :
    PreservesColimitsOfShape (Discrete I) RF
```

## Tag 0F0D, a lemma

[Tag 0F0D](https://stacks.math.columbia.edu/tag/0F0D) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesColimitsOfShape_etaleModuleDerivedDirectImageUnbounded_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperDirectImageDirectSums.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperDirectImageDirectSums.lean#L293). The attribute's comment: “for a torsion ring Λ in any universe, which contains Λ = ℤ/nℤ, n ≥ 1”.

> Let `f : X ⟶ Y` be a proper morphism of schemes and let `Λ` be a torsion ring, in any
> universe; for instance `Λ = ℤ/nℤ` with `n ≥ 1`. Then the unbounded derived direct image
> `Rf_* : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` commutes with direct sums.

```lean
theorem preservesColimitsOfShape_etaleModuleDerivedDirectImageUnbounded_of_isProper
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) (I : Type (max (u + 1) r)) :
    PreservesColimitsOfShape (Discrete I) (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f)
```

## Tag 0F12, a lemma

[Tag 0F12](https://stacks.math.columbia.edu/tag/0F12) in the Stacks Project.

**`Stacks.EtaleCohomology.ProjectionFormulaConstant.isIso_projectionFormulaMap_toPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProjectionFormulaConstant/Main.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProjectionFormulaConstant/Main.lean#L204). The attribute's comment: “the canonical map of Section 0943 for the structure morphism of `(X_étale, Λ̲)` to the point ringed by `Λ`, on the shared ringed topos `EtaleCoefficients.ringedTopos`; `D(pt, Λ)` is `D(Λ)` through `EtaleCoefficients.pointDerivedEquivalence`”.

> Let `X` be a quasi-compact and quasi-separated scheme with `cd(X) < ∞` and let `Λ` be a
> torsion ring. For `E ∈ D(X_étale, Λ)` and `K ∈ D(pt, Λ) = D(Λ)`, the
> canonical map of Cohomology on Sites, Section 0943, for the structure morphism
> `π : (X_étale, Λ̲) ⟶ (pt, Λ)`,
>
> `RΓ(X, E) ⊗^L_Λ K = Rπ_*E ⊗^L_Λ K ⟶ Rπ_*(E ⊗^L_Λ Lπ^*K) = RΓ(X, E ⊗^L_Λ K̲)`,
>
> is an isomorphism.

```lean
theorem isIso_projectionFormulaMap_toPoint [CompactSpace X] [QuasiSeparatedSpace X]
    (hcd : Scheme.etaleCohomologicalDimension X < ⊤) (hΛ : IsAddTorsion Λ)
    (E : DerivedCategory (SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos Λ X).O)))
    (K : DerivedCategory (SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf (pointRingedTopos Λ).O))) :
    IsIso (projectionFormulaMap (toPoint Λ X) E K)
```

## Tag 0F0G, a lemma

[Tag 0F0G](https://stacks.math.columbia.edu/tag/0F0G) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etalePushforwardProjectionMap_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperProjectionFormula/TorsionProjectionFormula.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperProjectionFormula/TorsionProjectionFormula.lean#L149).

> **[Stacks, Tag 0F0G].** Let `f : X ⟶ Y` be a proper morphism of schemes and `Λ` a torsion ring.
> For `E ∈ D(X_étale, Λ)` and `K ∈ D(Y_étale, Λ)`, unbounded, the canonical map of
> [Stacks, Tag 0943]
> `Rf_*E ⊗^L_Λ K ⟶ Rf_*(E ⊗^L_Λ f^{-1}K)`
> is an isomorphism in `D(Y_étale, Λ)`.

```lean
theorem isIso_etalePushforwardProjectionMap_of_isProper (hΛ : IsAddTorsion Λ)
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    (E : DerivedCategory (EtaleModules.{u, 0} Λ X))
    (K : DerivedCategory (EtaleModules.{u, 0} Λ Y)) :
    IsIso (etalePushforwardProjectionMap.{u, 0} Λ f E K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.96, Tag 0F0Y](https://stacks.math.columbia.edu/tag/0F0Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
