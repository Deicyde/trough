---
declaration: section
origin: cited
lean: Stacks.Adequate.BigSite.isLocalization_mapDerivedCategory_restrictModuleQCoh, Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryPlus_restrictModuleQCoh, Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryMinus_restrictModuleQCoh, Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryBounded_restrictModuleQCoh, Stacks.Adequate.BigSite.isLocalization_mapHomotopyCategoryPlus_associatedModuleAdeq_affine, Stacks.Adequate.exists_adequator, Stacks.Adequate.adequateComparisonSquare, Stacks.Adequate.adequateDiagramSquare
statement: formalized
proof: formalized
---

# 46.7 Derived categories of adequate modules, I

Section 46.7 of the Stacks Project, [Tag 06VS](https://stacks.math.columbia.edu/tag/06VS). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06ZQ, a lemma

[Tag 06ZQ](https://stacks.math.columbia.edu/tag/06ZQ) in the Stacks Project.

**`Stacks.Adequate.BigSite.isLocalization_mapDerivedCategory_restrictModuleQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean#L583). The attribute's comment: “the unbounded derived quotient `D(Adeq(𝒪))/D_𝒞(Adeq(𝒪)) = D(QCoh(𝒪_S))`”.

> **[Stacks, Tag 06ZQ].** `D(Adeq(𝒪))/D_𝒞(Adeq(𝒪)) = D(QCoh(𝒪_S))`: the functor
> `D(v) : D(Adeq(𝒪)) ⥤ D(QCoh(𝒪_S))` is a localization functor for the morphisms whose cone has
> all its cohomology objects in the Serre subcategory `𝒞` of parasitic adequate modules. This is
> [Stacks, Tag 06XM] applied to `v`, which realises the Serre quotient by `𝒞`
> (`Stacks.Adequate.BigSite.isLocalization_restrictModuleQCoh`, [Stacks, Tag 06ZN]) and has the
> fully faithful left adjoint `u` of [Stacks, Tag 06VN].

```lean
public theorem BigSite.isLocalization_mapDerivedCategory_restrictModuleQCoh
    [HasDerivedCategory.{w₁} (adequate.{u, u} B).FullSubcategory]
    [HasDerivedCategory.{w₂} (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory] :
    B.restrictModuleQCoh.mapDerivedCategory.IsLocalization
      (ObjectProperty.trW (fun X : DerivedCategory (adequate.{u, u} B).FullSubcategory =>
        ∀ n : ℤ, B.parasiticAdequate
          ((DerivedCategory.homologyFunctor (adequate.{u, u} B).FullSubcategory n).obj X)))
```

**`Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryPlus_restrictModuleQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean#L80). The attribute's comment: “bounded below version `D⁺(Adeq(𝒪))/D⁺_𝒞(Adeq(𝒪)) = D⁺(QCoh(𝒪_S))`”.

> **[Stacks, Tag 06ZQ], bounded below version.**
> `D⁺(Adeq(𝒪))/D⁺_𝒞(Adeq(𝒪)) = D⁺(QCoh(𝒪_S))`: the functor
> `D⁺(v) : D⁺(Adeq(𝒪)) ⥤ D⁺(QCoh(𝒪_S))` is a localization functor for the morphisms of
> `D⁺(Adeq(𝒪))` whose cone has all its cohomology objects in the Serre subcategory `𝒞` of
> parasitic adequate modules.

```lean
public theorem BigSite.isLocalization_mapDerivedCategoryPlus_restrictModuleQCoh :
    B.restrictModuleQCoh.mapDerivedCategoryPlus.IsLocalization
      ((derivedCategoryB B.parasiticAdequate).inverseImage DerivedCategory.Plus.ι).trW
```

**`Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryMinus_restrictModuleQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean#L92). The attribute's comment: “bounded above version `D⁻(Adeq(𝒪))/D⁻_𝒞(Adeq(𝒪)) = D⁻(QCoh(𝒪_S))`”.

> **[Stacks, Tag 06ZQ], bounded above version.**
> `D⁻(Adeq(𝒪))/D⁻_𝒞(Adeq(𝒪)) = D⁻(QCoh(𝒪_S))`: the functor
> `D⁻(v) : D⁻(Adeq(𝒪)) ⥤ D⁻(QCoh(𝒪_S))` is a localization functor for the morphisms of
> `D⁻(Adeq(𝒪))` whose cone has all its cohomology objects in the Serre subcategory `𝒞` of
> parasitic adequate modules.

```lean
public theorem BigSite.isLocalization_mapDerivedCategoryMinus_restrictModuleQCoh :
    B.restrictModuleQCoh.mapDerivedCategoryMinus.IsLocalization
      ((derivedCategoryB B.parasiticAdequate).inverseImage DerivedCategory.Minus.ι).trW
```

**`Stacks.Adequate.BigSite.isLocalization_mapDerivedCategoryBounded_restrictModuleQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDerivedQuotient.lean#L104). The attribute's comment: “bounded version `Dᵇ(Adeq(𝒪))/Dᵇ_𝒞(Adeq(𝒪)) = Dᵇ(QCoh(𝒪_S))`”.

> **[Stacks, Tag 06ZQ], bounded version.**
> `Dᵇ(Adeq(𝒪))/Dᵇ_𝒞(Adeq(𝒪)) = Dᵇ(QCoh(𝒪_S))`: the functor
> `Dᵇ(v) : Dᵇ(Adeq(𝒪)) ⥤ Dᵇ(QCoh(𝒪_S))` is a localization functor for the morphisms of
> `Dᵇ(Adeq(𝒪))` whose cone has all its cohomology objects in the Serre subcategory `𝒞` of
> parasitic adequate modules.

```lean
public theorem BigSite.isLocalization_mapDerivedCategoryBounded_restrictModuleQCoh :
    B.restrictModuleQCoh.mapDerivedCategoryBounded.IsLocalization
      ((derivedCategoryB B.parasiticAdequate).inverseImage DerivedCategory.Bounded.ι).trW
```

## Tag 06ZR, a lemma

[Tag 06ZR](https://stacks.math.columbia.edu/tag/06ZR) in the Stacks Project.

**`Stacks.Adequate.BigSite.isLocalization_mapHomotopyCategoryPlus_associatedModuleAdeq_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedLocalizationAffineSections.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedLocalizationAffineSections.lean#L565). The attribute's comment: “over an affine base `U = Spec A`, with no hypothesis: `D⁺(Adeq(𝒪))`, taken as the source does as the localization of `K⁺(Adeq(𝒪))` at the quasi-isomorphisms, is the localization of `K⁺(QCoh(𝒪_U))` at the universal quasi-isomorphisms along `u`. `(Sch/U)_fppf` is rendered as a chosen big fppf site containing `Spec A`”.

> **[Stacks, Tag 06ZR] over an affine base, unconditionally.** Over an affine scheme
> `U = Spec A` the bounded below derived category `D⁺(Adeq(𝒪))` is the localization of
> `K⁺(QCoh(𝒪_U))` at the universal quasi-isomorphisms.
>
> This is `BigSite.isLocalization_mapHomotopyCategoryPlus_associatedModuleAdeq_of_allAlgebras` with
> its single hypothesis discharged by
> `Stacks.Adequate.BigSite.universallyAcyclic_eq_inverseImage_qcohAllAlgebraSections`.

```lean
public theorem BigSite.isLocalization_mapHomotopyCategoryPlus_associatedModuleAdeq_affine :
    (((BigSite.ofBigFppfSite B (Spec A) hS).associatedModuleAdeq).mapHomotopyCategoryPlus ⋙
        MorphismProperty.Q (HomotopyCategory.Plus.quasiIso
          (adequate.{u, u}
            (BigSite.ofBigFppfSite B (Spec A) hS)).FullSubcategory)).IsLocalization
      (universalQuasiIso (Spec A))
```

## Tag 06ZS, a lemma

[Tag 06ZS](https://stacks.math.columbia.edu/tag/06ZS) in the Stacks Project.

**`Stacks.Adequate.exists_adequator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean#L220).

> **[Stacks, Tag 06ZS].** Let `U = Spec A` be an affine scheme. The inclusion functor
> `Adeq(𝒪) → Mod((Sch/U)_τ, 𝒪)` has a right adjoint, and the adjunction mapping `A(𝓕) → 𝓕` is
> an isomorphism for every adequate module `𝓕`.
>
> The right adjoint is `Stacks.Adequate.affineAdequator`, with adjunction
> `Stacks.Adequate.affineAdequatorAdjunction`.

```lean
public theorem exists_adequator :
    ∃ (R : SheafOfModules.{u} B.structureSheaf ⥤ (adequate.{u, u} B).FullSubcategory)
      (adjR : (adequate.{u, u} B).ι ⊣ R),
      ∀ F : SheafOfModules.{u} B.structureSheaf, IsAdequate B F → IsIso (adjR.counit.app F)
```

## Tag 06ZT, an equation

[Tag 06ZT](https://stacks.math.columbia.edu/tag/06ZT) in the Stacks Project.

**`Stacks.Adequate.adequateComparisonSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean#L150). The attribute's comment: “the commutativity of the square, with the comparison functor of Tag 06ZJ as its left vertical arrow; that it is an identification is `Stacks.Adequate.isEquivalence_adequateComparison`”.

> **[Stacks, Tag 06ZT]**, the commutative square in the proof of [Stacks, Tag 06ZS]: the
> inclusion of `Adeq(𝒪)` followed by the affine-section functor into the module-valued functors on
> the `A`-algebras of the site equals the comparison functor of [Stacks, Tag 06ZJ] followed by the
> inclusion of the adequate module-valued functors. It commutes by definitional unfolding, which
> is `Stacks.Adequate.adequateComparison_ι`.

```lean
public noncomputable def adequateComparisonSquare :
    adequateComparison.{u, m} B ⋙ (adequateOn.{u, max u m} A (schemeSizeBelow B.cutoff)).ι ≅
      (adequate.{u, max u m} B).ι ⋙ affineSectionsFunctor.{u, max u m} B A (𝟙 (Spec A))
```

**`Stacks.Adequate.adequateDiagramSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorDiagram.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorDiagram.lean#L96). The attribute's comment: “the commutativity of the diagram, with k, j and the right vertical arrow written out, at an arbitrary module universe”.

> **[Stacks, Tag 06ZT], the commutativity of the diagram**, at an arbitrary module universe:
> `k`, then the inclusion `j` of sheaves into presheaves, then the right vertical arrow, is the left
> vertical arrow (the comparison functor of [Stacks, Tag 06ZJ]) followed by the inclusion
> `i : 𝒜 → 𝒫`. Both sides restrict sections to spectra and scalars along `B ≅ 𝒪(Spec B)`.

```lean
public noncomputable def adequateDiagramSquare :
    adequateToAffineModules.{u, m} B ⋙ SheafOfModules.forget _ ⋙
        affinePresheafModulesToModuleValued.{u, m} B ≅
      adequateComparison.{u, m} B ⋙ (adequateOn.{u, max u m} A (schemeSizeBelow B.cutoff)).ι
```

**`Stacks.Adequate.adequateAffineDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorDiagram.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorDiagram.lean#L128). The attribute's comment: “the whole diagram: both vertical arrows are equivalences, it commutes, k and j are fully faithful, and its middle category is modules on the affine objects of the site”.

> **[Stacks, Tag 06ZT], the whole diagram.** For `U = Spec A` affine, in the diagram
> `Adeq(𝒪) --k--> Mod((Aff/U)_τ, 𝒪) --j--> PMod((Aff/U)_τ, 𝒪)` over `𝒜 --i--> 𝒫`:
>
> * the left vertical arrow `Adeq(𝒪) → 𝒜` is an equivalence ([Stacks, Tag 06ZJ]);
> * the right vertical arrow `PMod((Aff/U)_τ, 𝒪) → 𝒫` is an equivalence ([Stacks, Section 06US]);
> * the diagram commutes;
> * `k` and `j` are fully faithful;
> * the restriction `Mod((Sch/U)_τ, 𝒪) → Mod((Aff/U)_τ, 𝒪)` through which `k` factors is an
>   equivalence ([Stacks, Tag 021V]);
> * the affine-spectrum functor from the `A`-algebras of the site is fully faithful, with essential
>   image exactly the affine objects of the site, so that its source is `(Aff/U)_τ`.
>
> The commutativity and full-faithfulness conjuncts are wrapped in `Nonempty` because an
> isomorphism of functors and a full-faithfulness witness are data while a conjunction needs a
> proposition; asserting the diagram commutes is asserting such an isomorphism exists.

```lean
public theorem adequateAffineDiagram :
    (adequateComparison.{u, u} B).IsEquivalence ∧
      (affinePresheafModulesToModuleValued.{u, u} B).IsEquivalence ∧
      Nonempty (adequateToAffineModules.{u, u} B ⋙ SheafOfModules.forget _ ⋙
          affinePresheafModulesToModuleValued.{u, u} B ≅
        adequateComparison.{u, u} B ⋙ (adequateOn.{u, u} A (schemeSizeBelow B.cutoff)).ι) ∧
      Nonempty (adequateToAffineModules.{u, u} B).FullyFaithful ∧
      Nonempty (SheafOfModules.forget.{u} (DenseSubsiteModules.ringRestriction
        (affineSubsiteTopology B) B.topology (affineSpecOver B A (𝟙 (Spec A)))
        B.structureSheaf)).FullyFaithful ∧
      (SheafOfModules.pushforward.{u} (𝟙 (DenseSubsiteModules.ringRestriction
        (affineSubsiteTopology B) B.topology (affineSpecOver B A (𝟙 (Spec A)))
        B.structureSheaf))).IsEquivalence ∧
      (affineSpecOver B A (𝟙 (Spec A))).Full ∧ (affineSpecOver B A (𝟙 (Spec A))).Faithful ∧
      ∀ X : B.category, IsAffine X.left.obj ↔ (affineSpecOver B A (𝟙 (Spec A))).essImage X
```

Declarations registered for the tag:

- [`isEquivalence_adequateComparison`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isEquivalence_adequateComparison#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Adequator.lean#L155) (StacksFrontier): “the left vertical arrow of the square is an identification; the source reads it off Tag 06ZJ, and this is that tag”.

## Tag 06ZU, a lemma

[Tag 06ZU](https://stacks.math.columbia.edu/tag/06ZU) in the Stacks Project.

**`Stacks.Adequate.exactAt_mapHomologicalComplex_of_coreflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean#L177). The attribute's comment: “the homological step of the proof: exactness in positive degrees of a right adjoint applied to an injective resolution, from the Ext vanishing along a separating family; stated for an arbitrary adjunction”.

> **The homological core of [Stacks, Tag 06ZU].** Let `i ⊣ Q` be an adjunction with `i`
> additive, let `G` be a fully faithful additive functor preserving injective objects which
> carries an injective resolution `I` of `X` to a resolution of `G(X)`, and let `P` be a
> separating family in the domain of `i` whose objects have no degree-`n` extensions into `G(X)`.
> Then `Q(I^•)` is exact in degree `n > 0`.

```lean
public theorem exactAt_mapHomologicalComplex_of_coreflection [HasExt.{w} E]
    (i : D ⥤ C) (Q : C ⥤ D) [i.Additive] [Q.Additive] (adj : i ⊣ Q)
    (G : C ⥤ E) [G.Additive] [G.Full] [G.Faithful] [G.PreservesInjectiveObjects]
    (P : ObjectProperty D) (hP : P.IsSeparating)
    {X : C} (I : InjectiveResolution X)
    [QuasiIso ((G.mapHomologicalComplex (ComplexShape.up ℕ)).map I.ι)]
    (n : ℕ) (hn : 0 < n)
    (hExt : ∀ L : D, P L → Subsingleton (Abelian.Ext.{w} (G.obj (i.obj L)) (G.obj X) n)) :
    ((Q.mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex).ExactAt n
```

**`Stacks.Adequate.isZero_rightDerived_of_coreflection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean#L234). The attribute's comment: “the same step read as the vanishing of the right derived functors of the right adjoint; stated for an arbitrary adjunction”.

> **The homological core of [Stacks, Tag 06ZU]**, read as the vanishing of a right derived
> functor of the right adjoint: under the hypotheses of
> `Stacks.Adequate.exactAt_mapHomologicalComplex_of_coreflection`, `R^n Q(X) = 0`.

```lean
public theorem isZero_rightDerived_of_coreflection [EnoughInjectives C] [HasExt.{w} E]
    (i : D ⥤ C) (Q : C ⥤ D) [i.Additive] [Q.Additive] (adj : i ⊣ Q)
    (G : C ⥤ E) [G.Additive] [G.Full] [G.Faithful] [G.PreservesInjectiveObjects]
    [PreservesFiniteLimits G]
    (P : ObjectProperty D) (hP : P.IsSeparating) (X : C)
    (hacyclic : ∀ k : ℕ, 0 < k → IsZero ((G.rightDerived k).obj X))
    (n : ℕ) (hn : 0 < n)
    (hExt : ∀ L : D, P L → Subsingleton (Abelian.Ext.{w} (G.obj (i.obj L)) (G.obj X) n)) :
    IsZero ((Q.rightDerived n).obj X)
```

**`Stacks.Adequate.isZero_rightDerived_adequator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean#L367). The attribute's comment: “the full statement, `R^p A(F) = 0` for every `p > 0` and every object of `Adeq(O)`, for the named adequator of Tag 06ZS. Assumed: that adequator's own inputs (`Q`, `E`, `adj` from Tags 06Z6 and 06ZJ over the algebras of the site, `hj` and `comm` from Tag 06ZT), right acyclicity of the affine-section functor (`hacyclic`, Tags 06YK and 06VM), the positive-degree Ext vanishing along a separating family (`hP` and `hExt`, Tag 06ZI), the three closure properties of Tag 06VQ (1) and `EnoughInjectives` for the sheaves of modules on the site. Preservation of injective objects by the affine-section functor is proved, through Tag 03FB on the affine subsite”.

> **[Stacks, Tag 06ZU].** For `U = Spec A` affine, every object `𝓕` of `Adeq(𝒪)` and every
> `p > 0`, the `p`-th right derived functor of the adequator of [Stacks, Tag 06ZS] vanishes at
> `𝓕`: the adequator of an injective resolution of `𝓕` is exact in positive degrees.

```lean
public theorem isZero_rightDerived_adequator
    (adj : (adequateOn.{u, max u m} A (schemeSizeBelow B.cutoff)).ι ⊣ Q)
    (hj : (affineSectionsFunctor.{u, max u m} B A (𝟙 (Spec A))).FullyFaithful)
    (comm : E.functor ⋙ (adequateOn.{u, max u m} A (schemeSizeBelow B.cutoff)).ι ≅
      (adequate.{u, max u m} B).ι ⋙ affineSectionsFunctor.{u, max u m} B A (𝟙 (Spec A)))
    (F : (adequate.{u, max u m} B).FullSubcategory) (p : ℕ) (hp : 0 < p)
    (hacyclic : AffineSectionsAcyclic.{u, m} B A (𝟙 (Spec A)) F.obj)
    (P : ObjectProperty (adequate.{u, max u m} B).FullSubcategory) (hP : P.IsSeparating)
    (hExt : AffineSectionsExtVanishing.{u, m, w} B P F.obj p) :
    letI : (adequator.{u, max u m} B Q E).Additive := additive_adequator B Q E adj hj comm
    IsZero (((adequator.{u, max u m} B Q E).rightDerived p).obj F.obj)
```

**`Stacks.Adequate.isZero_rightDerived_affineAdequator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishingUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishingUnconditional.lean#L60).

> **[Stacks, Tag 06ZU].** Let `U = Spec A` be an affine scheme. For every object `𝓕` of
> `Adeq(𝒪)` and every `p > 0`, `R^p A(𝓕) = 0`, where `A` is the adequator
> `Stacks.Adequate.affineAdequator` of [Stacks, Tag 06ZS], the right adjoint of the inclusion
> `Adeq(𝒪) → Mod((Sch/U)_τ, 𝒪)`.
>
> The `letI` preamble is not a list of hypotheses: it is the abelian structure of `Adeq(𝒪)`
> (Tag 06VQ (1)) and the additivity of the adequator, which is a right adjoint of an additive
> functor.

```lean
public theorem isZero_rightDerived_affineAdequator
    (F : (adequate.{u, u} B).FullSubcategory) (p : ℕ) (hp : 0 < p) :
    letI := adequate_isClosedUnderKernels.{u, u} B
    letI := adequate_isClosedUnderCokernels.{u, u} B
    letI := adequate_isClosedUnderFiniteProducts.{u, u} B
    letI : Abelian (adequate.{u, u} B).FullSubcategory := abelian_adequate B
    letI : (affineAdequator B).Additive :=
      (affineAdequatorAdjunction B).right_adjoint_additive
    IsZero (((affineAdequator B).rightDerived p).obj F.obj)
```

## Tag 06ZV, a lemma

[Tag 06ZV](https://stacks.math.columbia.edu/tag/06ZV) in the Stacks Project.

**`Stacks.Adequate.isEquivalence_adequateBoundedBelowComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelow.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelow.lean#L94). The attribute's comment: “the full statement, that the canonical comparison functor `D⁺(Adeq(𝒪)) ⥤ D⁺_Adeq(𝒪)` of the equation (46.7.5.1) of Tag 06VV is an equivalence. Assumed: a right adjoint `Ψ` of the derived inclusion on bounded below objects together with its preservation of boundedness below (`adj`, `hΨ`), which is the source's `RA`, available because the adequator of Tag 06ZS is left exact and `Mod(𝒪)` has enough injectives; the source's key fact that the adjunction maps are quasi-isomorphisms on the SINGLE modules (`hunit`, `hcounit`), which is Tag 06ZU together with the moreover clause of Tag 06ZS; and the closure of adequacy under kernels, cokernels and finite products, Tag 06VQ (1), which makes `Adeq(𝒪)` abelian. The passage from the key fact on single modules to all of `D⁺`, which is the source's spectral sequence argument via Tag 015J, is proved”.

> **[Stacks, Tag 06ZV].** For `U = Spec A` affine, the canonical comparison functor
> `D⁺(Adeq(𝒪)) ⥤ D⁺_{Adeq}(𝒪)` — the inclusion `Adeq(𝒪) ⥤ Mod(𝒪)` applied degreewise to
> complexes — is an equivalence.

```lean
public theorem isEquivalence_adequateBoundedBelowComparison :
    (DerivedCategoryB.boundedBelowComparison (adequate.{u, m} B)).IsEquivalence
```

**`Stacks.Adequate.adequateBoundedBelowEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelow.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelow.lean#L104). The attribute's comment: “the equivalence as data, `D⁺(Adeq(𝒪)) ≌ D⁺_Adeq(𝒪)`, under the hypotheses of `Stacks.Adequate.isEquivalence_adequateBoundedBelowComparison`; its functor is the canonical comparison functor by `Stacks.Adequate.adequateBoundedBelowEquivalence_functor`”.

> **[Stacks, Tag 06ZV]** as an equivalence of categories:
> `D⁺(Adeq(𝒪)) ≌ D⁺_{Adeq}(𝒪)` for `U = Spec A` affine.

```lean
public def adequateBoundedBelowEquivalence :
    DerivedCategory.Plus (adequate.{u, m} B).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus (adequate.{u, m} B)).FullSubcategory
```

**`Stacks.Adequate.isEquivalence_boundedBelowComparison_adequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelowUnconditional.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/DerivedCategoryBoundedBelowUnconditional.lean#L95).

> **[Stacks, Tag 06ZV].** Let `U = Spec A` be an affine scheme. The canonical functor
> `D⁺(Adeq(𝒪)) ⥤ D⁺_{Adeq}(𝒪)`, the inclusion `Adeq(𝒪) ⥤ Mod((Sch/U)_τ, 𝒪)` applied
> degreewise to bounded below complexes, is an equivalence onto the bounded below objects of
> `D(𝒪)` whose cohomology sheaves are adequate.

```lean
public theorem isEquivalence_boundedBelowComparison_adequate
    [HasDerivedCategory.{w} (SheafOfModules.{u} B.structureSheaf)]
    [HasDerivedCategory.{w'} (adequate.{u, u} B).FullSubcategory] :
    (DerivedCategoryB.boundedBelowComparison (adequate.{u, u} B)).IsEquivalence
```

## Tag 06ZW, a lemma

[Tag 06ZW](https://stacks.math.columbia.edu/tag/06ZW) in the Stacks Project.

**`Stacks.Adequate.bijective_mapExtAddHom_ι_adequate_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateExtComparison.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateExtComparison.lean#L124). The attribute's comment: “degree 0, where the comparison is the map on Hom and the inclusion of the strictly full subcategory of adequate modules is fully faithful; every degree is bijective\_mapExtAddHom\_ι\_adequate in HigherExtsAdequate/AdequateExtComparisonAll”.

> For `U = Spec A` affine and adequate `𝒪`-modules `𝓕`, `𝓖`, the natural map
> `Ext^0_{Adeq(𝒪)}(𝓕, 𝓖) ⟶ Ext^0_{Mod((Sch/U)_τ, 𝒪)}(𝓕, 𝓖)` is bijective.

```lean
public theorem bijective_mapExtAddHom_ι_adequate_zero :
    letI := adequate_isClosedUnderKernels.{u, u} B
    letI := adequate_isClosedUnderCokernels.{u, u} B
    letI := adequate_isClosedUnderFiniteProducts.{u, u} B
    letI : Abelian (adequate.{u, u} B).FullSubcategory := abelian_adequate B
    letI : PreservesFiniteLimits (adequate.{u, u} B).ι := (exact_ι_adequate B).1
    letI : PreservesFiniteColimits (adequate.{u, u} B).ι := (exact_ι_adequate B).2
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    letI : HasExt.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      hasExt_of_hasDerivedCategory _
    ∀ (F G : (adequate.{u, u} B).FullSubcategory),
      Function.Bijective ((adequate.{u, u} B).ι.mapExtAddHom.{u + 1, u + 1} F G 0)
```

**`Stacks.Adequate.bijective_mapExtAddHom_ι_adequate_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateExtComparison.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequateExtComparison.lean#L157). The attribute's comment: “degree 1, where the comparison is bijective because the adequate modules are closed under extensions, Tag 06VQ (3), and Ext^1 is the group of Yoneda extensions; every degree is bijective\_mapExtAddHom\_ι\_adequate in HigherExtsAdequate/AdequateExtComparisonAll”.

> For `U = Spec A` affine and adequate `𝒪`-modules `𝓕`, `𝓖`, the natural map
> `Ext^1_{Adeq(𝒪)}(𝓕, 𝓖) ⟶ Ext^1_{Mod((Sch/U)_τ, 𝒪)}(𝓕, 𝓖)` is bijective.

```lean
public theorem bijective_mapExtAddHom_ι_adequate_one :
    letI := adequate_isClosedUnderKernels.{u, u} B
    letI := adequate_isClosedUnderCokernels.{u, u} B
    letI := adequate_isClosedUnderFiniteProducts.{u, u} B
    letI : Abelian (adequate.{u, u} B).FullSubcategory := abelian_adequate B
    letI : PreservesFiniteLimits (adequate.{u, u} B).ι := (exact_ι_adequate B).1
    letI : PreservesFiniteColimits (adequate.{u, u} B).ι := (exact_ι_adequate B).2
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    letI : HasExt.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      hasExt_of_hasDerivedCategory _
    ∀ (F G : (adequate.{u, u} B).FullSubcategory),
      Function.Bijective ((adequate.{u, u} B).ι.mapExtAddHom.{u + 1, u + 1} F G 1)
```

**`Stacks.Adequate.bijective_mapExtAddHom_ι_adequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/AdequateExtComparisonAll.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/AdequateExtComparisonAll.lean#L50). The attribute's comment: “every degree i ≥ 0”.

> Let `U = Spec A` be affine and `𝓕`, `𝓖` adequate `𝒪`-modules. For every `i ≥ 0` the natural map
> `Ext^i_{Adeq(𝒪)}(𝓕, 𝓖) ⟶ Ext^i_{Mod(𝒪)}(𝓕, 𝓖)`, induced by the exact inclusion of the adequate
> modules, is bijective.
>
> The `letI` preamble is not a list of hypotheses: it is the abelian structure of `Adeq(𝒪)`
> (Tag 06VQ (1)), the exactness of its inclusion (Tag 06VQ (2)) and the standard derived-category
> and `Ext` choices, spelled exactly as in `bijective_mapExtAddHom_ι_adequate_zero`.

```lean
public theorem bijective_mapExtAddHom_ι_adequate :
    letI := adequate_isClosedUnderKernels.{u, u} B
    letI := adequate_isClosedUnderCokernels.{u, u} B
    letI := adequate_isClosedUnderFiniteProducts.{u, u} B
    letI : Abelian (adequate.{u, u} B).FullSubcategory := abelian_adequate B
    letI : PreservesFiniteLimits (adequate.{u, u} B).ι := (exact_ι_adequate B).1
    letI : PreservesFiniteColimits (adequate.{u, u} B).ι := (exact_ι_adequate B).2
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    letI : HasExt.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      hasExt_of_hasDerivedCategory _
    ∀ (F G : (adequate.{u, u} B).FullSubcategory) (n : ℕ),
      Function.Bijective ((adequate.{u, u} B).ι.mapExtAddHom.{u + 1, u + 1} F G n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.7, Tag 06VS](https://stacks.math.columbia.edu/tag/06VS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
