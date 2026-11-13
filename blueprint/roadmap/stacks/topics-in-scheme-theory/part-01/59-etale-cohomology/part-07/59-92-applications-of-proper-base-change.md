---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.bijective_etaleCohomologyRestrictionMap_scalarExtensionFst_of_isProper, Stacks.EtaleCohomology.isZero_rightDerived_etaleModuleDirectImage_of_isIntegralHom, Stacks.EtaleCohomology.ProperFibreDimension.isZero_rightDerived_etaleAbelianDirectImage_of_isProper, Stacks.EtaleCohomology.isZero_rightDerived_etaleAbelianDirectImage_of_isProper, Stacks.EtaleCohomology.isIso_etaleModuleDerivedBaseChangeUnbounded_app_of_isProper, Stacks.EtaleCohomology.DerivedTensorConstant.nonempty_derivedSections_tensor_derivedConstantSheaf_iso, Stacks.EtaleCohomology.isIso_etalePushforwardProjectionMap_of_isProper_of_isGE
statement: formalized
proof: formalized
---

# 59.92 Applications of proper base change

Section 59.92 of the Stacks Project, [Tag 0A5I](https://stacks.math.columbia.edu/tag/0A5I). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DDG, a lemma

[Tag 0DDG](https://stacks.math.columbia.edu/tag/0DDG) in the Stacks Project.

**`Stacks.EtaleCohomology.bijective_etaleCohomologyRestrictionMap_scalarExtensionFst_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SeparablyClosedFieldExtension.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/SeparablyClosedFieldExtension.lean#L194).

> **Stacks Project, Tag 0DDG.** Let `K/k` be an extension of separably closed fields, `X` a
> proper scheme over `k` (`f : X ⟶ Spec k` proper) and `F` a torsion abelian sheaf on `X_étale`.
> Then the restriction map `H^q_étale(X, F) ⟶ H^q_étale(X_K, F|_{X_K})` along the projection
> `X_K = X ×_{Spec k} Spec K ⟶ X` is bijective for every `q ≥ 0`, with `Ext` computed in any
> universe `w`.

```lean
theorem bijective_etaleCohomologyRestrictionMap_scalarExtensionFst_of_isProper
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})]
    [HasExt.{w} (Sheaf (scalarExtension k K f).smallEtaleTopology AddCommGrpCat.{u + 1})]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) (q : ℕ) :
    Function.Bijective
      (etaleCohomologyRestrictionMap.{u, 0, w} (scalarExtensionFst k K f) F q)
```

## Tag 095U, a lemma

[Tag 095U](https://stacks.math.columbia.edu/tag/095U) in the Stacks Project.

**`Stacks.EtaleCohomology.isZero_rightDerived_etaleModuleDirectImage_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralCohomologicalDimension.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralCohomologicalDimension.lean#L132). The attribute's comment: “the case n = 0: for an integral morphism — a finite one, for instance, which is what a proper morphism with zero-dimensional fibres is — R^q f\_* F = 0 for every q > 0 and every sheaf of Λ-modules F, with no torsion hypothesis. The general bound 2n is NOT proved: its induction needs the curve case, Tag 03SC, which is not formalized here.”. References: SGA 4 VIII (5.6), “more general”; SGA 4 Vbis (4.3.4), “more general”; SGA 4 XII (5.3), “special case”; SGA 4 XIV (1.11), “partial”; SGA 4 XVII (4.3.1), “special case”; SGA 4 XVII (5.1.4), “special case”; SGA 4½ Arcata (2.3.6), “more general”; SGA 4½ Th finitude (1.3), “special case”.

> Let `Λ` be a ring and let `f : X ⟶ Y` be an integral morphism of schemes. Then the higher
> direct images of every sheaf of `Λ`-modules `F` on the small étale site of `X` vanish:
> `R^q f_* F = 0` for every `q > 2 · 0`.

```lean
theorem isZero_rightDerived_etaleModuleDirectImage_of_isIntegralHom (Λ : Type r) [Ring Λ]
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] (F : EtaleModules.{u, r} Λ X) (q : ℕ)
    (hq : 2 * 0 < q) :
    IsZero (((etaleModuleDirectImage.{u, r} Λ f).rightDerived q).obj F)
```

**`Stacks.EtaleCohomology.ProperFibreDimension.isZero_rightDerived_etaleAbelianDirectImage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperFibreDimensionBound.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperFibreDimensionBound.lean#L394). The attribute's comment: “the dévissage, with the curve input still open. PROVED: the tag's own conclusion, R^q f\_* F = 0 for every q > 2n and every abelian TORSION sheaf F, for f proper in the source's sense (IsProper together with QuasiCompact, since Mathlib's IsProper asks only for locally of finite type) with every fibre of dimension at most n. The content proved outright is the Leray/composition step that makes the bounds add, 2(n-1) + 2 = 2n: that is hasEtaleDirectImageBound\_comp, and under it isZero\_rightDerived\_comp, obtained from the Grothendieck spectral sequence of Tag 015N with no hypothesis beyond Tag 015M's acyclicity criterion. The base case n = 0 is proved outright as well: Tag 02LS, proved in this library by isFinite\_iff\_isProper\_and\_forall\_finite\_preimage\_singleton together with finite\_preimage\_singleton\_of\_topologicalKrullDim\_fiber\_le\_zero, makes f finite and therefore integral, and Tag 03QP (2) then gives the vanishing. ASSUMED, about the given f and nothing more: hdev, for n >= 1, a factorisation f = h ≫ g in which h already has the bound 2(n-1) and the curve leg g has the bound 2 — the latter is the conclusion of Tag 03SC (via Tag 0DDF), and TAG 03SC IS OWNED BY ANOTHER ITEM OF THIS PROJECT and is deliberately NOT formalized here, while the existence of the factorisation is the geometry of the source's steps 5-7 (reduction, normalization, graph of a rational function in X x P^1), also not available in this repository. The general bound is therefore NOT proved unconditionally.”. References: SGA 4 XVII (5.1.4), “special case”; SGA 4 XVII (5.2.8.1), “special case”; SGA 4½ Cycle (2.3.1), “special case”.

> **[Stacks, Tag 095U], its dévissage.** Let `f : X ⟶ Y` be a proper morphism of schemes — in
> the source's sense, so `[IsProper f]` together with `[QuasiCompact f]`, Mathlib's `IsProper`
> asking only for *locally* of finite type — all of whose fibres have dimension at most `n`. Then
> for **any** abelian torsion sheaf `F` on `X_étale` and every `q > 2n`,
>
> `R^q f_* F = 0`.
>
> The case `n = 0` is proved outright: [Stacks, Tag 02LS] makes `f` finite, by
> `AlgebraicGeometry.isFinite_iff_isProper_and_forall_finite_preimage_singleton` fed with
> `AlgebraicGeometry.finite_preimage_singleton_of_topologicalKrullDim_fiber_le_zero`, finiteness
> gives integrality, and the vanishing then comes from [Stacks, Tag 03QP] (2), already in this
> library, through `hasEtaleDirectImageBound_zero_of_isIntegralHom`.
>
> One input about `f` itself is assumed, and nothing else:
>
> * `hdev` is the outcome of the source's dévissage for `f` when `n ≥ 1`: a factorisation
>   `f = h ≫ g` in which `h` already satisfies the bound in dimension `n - 1` and `g`, the curve
>   leg, satisfies the bound `2`. The bound for the curve leg is the conclusion of
>   [Stacks, Tag 03SC] (through [Stacks, Tag 0DDF]); **Tag 03SC is deliberately not formalized
>   here.** The existence of the factorisation is the
>   geometry of the source's steps 5–7 (reduction, normalization, and the graph of a rational
>   function in `X × P^1`), which is likewise unavailable here, and which is why it is a
>   hypothesis about `f` rather than a statement proved for every proper `f`.
>
> What the file proves is the step that turns that input into the bound: the Leray/composition
> bound `hasEtaleDirectImageBound_comp`, and under it the purely homological
> `isZero_rightDerived_comp`.

```lean
theorem isZero_rightDerived_etaleAbelianDirectImage_of_isProper
    (f : X ⟶ Y) [IsProper f] [QuasiCompact f] (n : ℕ) (hdim : HasFibreDimLE f n)
    (hdev : 1 ≤ n → ∃ (C : Scheme.{u}) (h : X ⟶ C) (g : C ⟶ Y), f = h ≫ g ∧
      QuasiCompact h ∧ QuasiSeparated h ∧
      HasEtaleDirectImageBound h (2 * (n - 1)) ∧ HasEtaleDirectImageBound g 2)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : torsionSheafProperty X.smallEtaleTopology F) (q : ℕ) (hq : 2 * n < q) :
    IsZero (((etaleAbelianDirectImage.{u, u + 1} f).rightDerived q).obj F)
```

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.isZero_rightDerived_etaleAbelianDirectImage_of_isProper`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeTheoremUnconditional.lean#L175), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperDirectImageVanishingRegistration.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperDirectImageVanishingRegistration.lean#L23) (StacksFrontier): “f proper (Mathlib's IsProper, which implies quasi-compact) with every fibre of topological Krull dimension at most n, F any abelian torsion sheaf on the small étale site of X: R^q f\_* F = 0 for all q > 2n”.

## Tag 0F0C, a lemma

[Tag 0F0C](https://stacks.math.columbia.edu/tag/0F0C) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etaleModuleDerivedBaseChangeUnbounded_app_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ModuleProperBaseChangeUnbounded.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ModuleProperBaseChangeUnbounded.lean#L405). The attribute's comment: “for every commutative ring Λ with n = 0 in Λ for some n ≥ 1, which contains the source's Λ = ℤ/nℤ”. References: SGA 4 XVII (4.3.2), “special case”.

> **Stacks Project, Tag 0F0C.** Let `f : X ⟶ Y` be a proper morphism of schemes, `g : Y' ⟶ Y`
> a morphism of schemes, and `X' = Y' ×_Y X`, given as a cartesian square `sq` with projections
> `f' : X' ⟶ Y'` and `g' : X' ⟶ X`. Let `Λ` be a commutative ring in which some integer `n ≥ 1` is
> zero — for instance `ℤ/nℤ`. Then for every object `E` of the unbounded derived category
> `D(X_étale, Λ)` the base change map `g^{-1} Rf_* E ⟶ Rf'_* (g')^{-1} E` of [Stacks, Tag 0A2A]
> (`Stacks.EtaleCohomology.etaleModuleDerivedBaseChangeUnbounded`) is an isomorphism.

```lean
theorem isIso_etaleModuleDerivedBaseChangeUnbounded_app_of_isProper (Λ : Type) [CommRing Λ]
    (hΛ : ∃ n : ℕ, 0 < n ∧ (n : Λ) = 0) {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    {g : Y' ⟶ Y} {g' : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback g' f' f g)
    (E : DerivedCategory (EtaleModules Λ X)) :
    IsIso ((etaleModuleDerivedBaseChangeUnbounded Λ f g g' f' sq.w).app E)
```

## Tag 0F0E, a lemma

[Tag 0F0E](https://stacks.math.columbia.edu/tag/0F0E) in the Stacks Project.

**`Stacks.EtaleCohomology.DerivedTensorConstant.nonempty_derivedSections_tensor_derivedConstantSheaf_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedGlobalSectionsTensorConstant.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedGlobalSectionsTensorConstant.lean#L476). The attribute's comment: “abelian sheaves on `X_étale` are sheaves of `ULift ℤ`-modules, `RΓ(X, -)` is any right derived functor of global sections on the unbounded derived category, and the identification is stated as the existence of an isomorphism in `D(ℤ)`”.

> **[Stacks, Tag 0F0E].** Let `X` be a quasi-compact and quasi-separated scheme, let
> `E ∈ D⁺(X_étale)` and `K ∈ D⁺(ℤ)`. Then
>
> > `RΓ(X, E ⊗_ℤ^L K̲) ≅ RΓ(X, E) ⊗_ℤ^L K`.
>
> Here abelian sheaves are sheaves of modules over the integers lifted to the coefficient
> universe, `E ⊗_ℤ^L K̲` is the derived tensor product of `E` with the derived constant sheaf on
> `K`, `RΓ(X, -)` is any right derived functor of the global sections on the unbounded derived
> category, and the right-hand side is the derived tensor product of `D(ℤ)`.
>
> The isomorphism is the composite of the canonical identifications: `E` is represented by a
> bounded below complex `I` of injective sheaves and `K` by a bounded below complex `P` of flat
> modules (`ℤ` has global dimension one), so that `E ⊗_ℤ^L K̲ = I ⊗ P̲` and
> `RΓ(X, E) ⊗_ℤ^L K = Γ(X, I) ⊗ P`; the comparison `Γ(X, I) ⊗ P ⟶ Γ(X, I ⊗ P̲)` is an isomorphism
> of complexes (`totalTensorIso`), and `Γ(X, I ⊗ P̲) ⟶ RΓ(X, I ⊗ P̲)` is an isomorphism because
> `I ⊗ P̲` is a bounded below complex of acyclic sheaves (`rightAcyclic_tensorObj_X`). Both use that
> `X` is quasi-compact and quasi-separated, through the commutation of étale cohomology with
> filtered colimits (Stacks 03Q5): a flat module is the filtered colimit of free modules of finite
> rank (Stacks 058G), for which `Hᵖ(X, F ⊗ M̲) = Hᵖ(X, F) ⊗ M` is additivity.

```lean
theorem nonempty_derivedSections_tensor_derivedConstantSheaf_iso
    (RΓ : DerivedCategory (Sh X) ⥤ DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} ℤ)))
    (α : (Γm X).mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RΓ)
    [RΓ.IsRightDerivedFunctor α (HomotopyCategory.quasiIso (Sh X) (ComplexShape.up ℤ))]
    (E : DerivedCategory (Sh X)) (a : ℤ) [E.IsGE a]
    (K : DerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} ℤ))) (b : ℤ) [K.IsGE b] :
    letI := CochainComplex.KFlatMonoidal.derivedMonoidal (ModuleCat.{u + 1} (ULift.{u + 1} ℤ))
      (CochainComplex.DerivedTensor.OneSided.exists_kFlat_quasiIso (ULift.{u + 1} ℤ))
    Nonempty (RΓ.obj (E ⊗ (Stacks.ModuleSheaf.derivedConstantSheafComplexes.{t, t', u + 1, u, u + 1}
        X.smallEtaleTopology).obj K) ≅ RΓ.obj E ⊗ K)
```

## Tag 0F0F, a lemma

[Tag 0F0F](https://stacks.math.columbia.edu/tag/0F0F) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etalePushforwardProjectionMap_of_isProper_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperProjectionFormula/BoundedBelowTorsionProjectionFormula.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperProjectionFormula/BoundedBelowTorsionProjectionFormula.lean#L41).

> **Projection formula for a proper morphism and a bounded below object with torsion
> cohomology** [Stacks, Tag 0F0F]. Let `f : X ⟶ Y` be a proper morphism of schemes, let
> `E ∈ D^+(X_étale)` have torsion cohomology sheaves and let `K ∈ D^+(Y_étale)`. Then the projection
> map `Rf_*E ⊗^L_ℤ K ⟶ Rf_*(E ⊗^L_ℤ f^{-1}K)` is an isomorphism in `D(Y_étale, ℤ)`.

```lean
theorem isIso_etalePushforwardProjectionMap_of_isProper_of_isGE {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsProper f] (E : DerivedCategory (EtaleModules.{u, 0} ℤ X)) (a : ℤ) (hE : E.IsGE a)
    (hT : ∀ n, IsTorsionEtaleModule.{u, 0} ℤ X ((DerivedCategory.homologyFunctor _ n).obj E))
    (K : DerivedCategory (EtaleModules.{u, 0} ℤ Y)) (b : ℤ) (hK : K.IsGE b) :
    IsIso (etalePushforwardProjectionMap.{u, 0} ℤ f E K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.92, Tag 0A5I](https://stacks.math.columbia.edu/tag/0A5I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
