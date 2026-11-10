---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.logarithmicDifferentialComplexMap, AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian, AlgebraicGeometry.SheafOfModules.hodgeFirstChernClassAbelian, AlgebraicGeometry.Scheme.Hom.logarithmicDifferentialSheafHom, AlgebraicGeometry.Scheme.Hom.hodgeFirstChernClass, AlgebraicGeometry.Scheme.Hom.deRhamFirstChernClassAbelian_schemePullbackClassHom, AlgebraicGeometry.Scheme.Hom.hodgeFirstChernClass_schemePullbackClassHom, AlgebraicGeometry.SheafOfModules.filteredChernProduct
statement: formalized
proof: formalized
---

# 50.9 First Chern class in de Rham cohomology

Section 50.9 of the Stacks Project, [Tag 0FLE](https://stacks.math.columbia.edu/tag/0FLE). 3 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FLE, the section

[Tag 0FLE](https://stacks.math.columbia.edu/tag/0FLE) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.logarithmicDifferentialComplexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L313). The attribute's comment: “d log as a map of complexes”.

> **Stacks Project, Tag 0FLE.** **Logarithmic differentiation as a morphism of complexes of
> abelian sheaves** `𝒪_X^*[-1] ⟶ Ω^•_{𝒪_X/A}`. There is a single condition to check, that
> `d log u` is closed, and it is
> `AlgebraicGeometry.SheafOfModules.d_logarithmicDifferentialAbelian`.

```lean
def logarithmicDifferentialComplexMap : unitsComplex X ⟶ deRhamAbelianComplexInt B D
```

**`AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L552). The attribute's comment: “the de Rham first Chern class”.

> **Stacks Project, Tag 0FLE.** **The first Chern class in relative de Rham cohomology**, in
> the abelian-sheaf realization: the image of a Picard class under the map on degree-two
> hypercohomology induced by logarithmic differentiation `𝒪_X^*[-1] ⟶ Ω^•_{𝒪_X/A}`.

```lean
def deRhamFirstChernClassAbelian :
    Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj (structureSheaf X.sheaf).property →+
      deRhamCohomologyAbelian B D 2
```

**`AlgebraicGeometry.SheafOfModules.hodgeFirstChernClassAbelian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L614). The attribute's comment: “the Hodge first Chern class, for a ringed space over a base ring sheaf”.

> **Stacks Project, Tag 0FLE.** **The first Chern class in Hodge cohomology**
> `c₁^{Hodge} : Pic(X) ⟶ H¹(X, Ω¹_{𝒪_X/A})`, in the abelian-sheaf realization: the identification
> `Pic(X) = H¹(X, 𝒪_X^*)` of Stacks Tag 09NU followed by the map on first cohomology induced by
> logarithmic differentiation `𝒪_X^* ⟶ Ω¹_{𝒪_X/A}`.
>
> The construction is the one of `AlgebraicGeometry.Scheme.Hom.hodgeFirstChernClass`, carried out
> for a ringed space over a base ring sheaf rather than for a morphism of schemes — the two use
> the same functor `(Γ(X, -)).rightDerived 1` and the same `d log`, but different spellings of the
> identification of Tag 09NU, and no comparison between them is proved here. This realization is
> the one the first step of the Hodge filtration projects onto, in
> `AlgebraicGeometry.SheafOfModules.hodgeFirstChernClassAbelian_eq`.

```lean
def hodgeFirstChernClassAbelian :
    Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj (structureSheaf X.sheaf).property →+
      hodgeCohomologyOneAbelian B D
```

**`AlgebraicGeometry.Scheme.Hom.logarithmicDifferentialSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean#L133). The attribute's comment: “d log into the sheaf of relative differentials”.

> **Logarithmic differentiation as a morphism of sheaves of abelian groups**
> `𝒪_X^* ⟶ Ω_{X/S}`, the sheaf of units being written additively.

```lean
def logarithmicDifferentialSheafHom :
    unitsSheaf X.toRingedSpace ⟶ relativeDifferentialsAbelian p
```

**`AlgebraicGeometry.Scheme.Hom.hodgeFirstChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean#L220). The attribute's comment: “the Hodge first Chern class”.

> **The first Chern class in Hodge cohomology** `c₁^{Hodge} : Pic(X) ⟶ H¹(X, Ω_{X/S})`: the
> identification `Pic(X) = H¹(X, 𝒪_X^*)` of Stacks Tag 09NU followed by the map on first cohomology
> induced by logarithmic differentiation.

```lean
def hodgeFirstChernClass {X S : Scheme.{u}} (p : X ⟶ S) :
    Stacks.Picard.ofScheme X →+ hodgeCohomologyOne p
```

## Tag 0FMD, a lemma

[Tag 0FMD](https://stacks.math.columbia.edu/tag/0FMD) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamFirstChernClassAbelian_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/DeRhamFirstChernClassSquare.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/DeRhamFirstChernClassSquare.lean#L229). The attribute's comment: “the de Rham square”.

> **Stacks Project, Tag 0FMD.** **The de Rham first Chern class commutes with pullback**: for
> a commutative square of schemes with horizontal arrows `f : X' ⟶ X` and `g : S' ⟶ S`, the square
> formed by `c₁^{dR}`, by pullback of Picard classes and by the de Rham pullback
> `H²_{dR}(X/S) ⟶ H²_{dR}(X'/S')` of [Stacks, Tag 0FL6] commutes.

```lean
theorem deRhamFirstChernClassAbelian_schemePullbackClassHom (c : Stacks.Picard.ofScheme X) :
    SheafOfModules.deRhamFirstChernClassAbelian (deRhamAlgebras p')
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p'))
        (Stacks.GluePicard.picardModelAddEquiv X'.toRingedSpace
          (Stacks.Picard.schemePullbackClassHom f c)) =
      (deRhamCohomologyPullback f p p' g hcomm 2).hom
        (SheafOfModules.deRhamFirstChernClassAbelian (deRhamAlgebras p)
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p))
          (Stacks.GluePicard.picardModelAddEquiv X.toRingedSpace c))
```

**`AlgebraicGeometry.Scheme.Hom.hodgeFirstChernClass_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/HodgeFirstChernClass.lean#L266). The attribute's comment: “the Hodge square”.

> **The Hodge first Chern class commutes with pullback**: for a commutative square of schemes
> with horizontal arrows `f : X' ⟶ X` and `g : S' ⟶ S`, the square formed by `c₁^{Hodge}`, by
> pullback of Picard classes and by pullback on `H¹(-, Ω)` commutes.

```lean
theorem hodgeFirstChernClass_schemePullbackClassHom (c : Stacks.Picard.ofScheme X) :
    hodgeFirstChernClass p' (Stacks.Picard.schemePullbackClassHom f c) =
      (hodgeCohomologyOnePullback f p p' g hcomm).hom (hodgeFirstChernClass p c)
```

## Tag 0FME, a remark

[Tag 0FME](https://stacks.math.columbia.edu/tag/0FME) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.filteredChernProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean#L195). The attribute's comment: “Remark 50.9.2, clause F of A-I: the a-fold cup product ξ = γ₁(L₁) ∪ … ∪ γ₁(L_a) ∈ H^{2a}(X, σ^{≥a}Ω^•), for every a, formed with the cup product of Section 50.7 on the hypercohomology of the brutal truncations (`hodgeFiltrationCup`, the cup product of Cohomology Section 0FKU along the multiplication of the Hodge filtration) from the class γ₁ of clause B”.

> **Stacks Project, Tag 0FME.** **The `a`-fold cup product
> `ξ = γ₁(L₁) ∪ … ∪ γ₁(L_a) ∈ H^{2a}(X, σ^{≥a}Ω^•_{𝒪_X/A})`** of Hodge-filtered first Chern
> classes, for `a = k + 1` invertible modules with Picard classes `L 0, …, L k`, the cup product
> being the one of Section 50.7, `AlgebraicGeometry.SheafOfModules.hodgeFiltrationCup`.
>
> The filtration index and the cohomological degree are `AlgebraicGeometry.SheafOfModules.cupLength`
> and `AlgebraicGeometry.SheafOfModules.cupDegree`, which `cupLength_eq` and `cupDegree_eq` identify
> with `a` and `2a`.

```lean
def filteredChernProduct : (k : ℕ) →
    (ℕ → Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) →
      truncatedDeRhamCohomologyAbelian B D (cupLength k) (cupDegree k)
```

**`AlgebraicGeometry.SheafOfModules.truncatedDeRhamCohomologyAbelianMap_filteredChernProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean#L356). The attribute's comment: “Remark 50.9.2, clause G of A-I: the map σ^{≥a}Ω^• ⟶ Ω^• sends ξ to the a-fold product c₁^dR(L₁) ∪ … ∪ c₁^dR(L_a) in H^{2a}_dR(X/S), for every a, both cup products being those of Cohomology Section 0FKU (`hodgeFiltrationCup` and `deRhamCup`)”.

> **Stacks Project, Tag 0FME.** **The image of `ξ = γ₁(L₁) ∪ … ∪ γ₁(L_a)` under
> `σ^{≥a}Ω^• ⟶ Ω^•` is `c₁^{dR}(L₁) ∪ … ∪ c₁^{dR}(L_a)` in `H^{2a}_{dR}(X/S)`.**
>
> The induction is on the number of factors: for one factor this is clause `C`,
> `AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian_eq`, and the inductive step is the
> commutative diagram of Section 50.7,
> `AlgebraicGeometry.SheafOfModules.truncatedDeRhamCohomologyAbelianMap_hodgeFiltrationCup`.

```lean
theorem truncatedDeRhamCohomologyAbelianMap_filteredChernProduct (k : ℕ)
    (L : ℕ → Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    (truncatedDeRhamCohomologyAbelianMap B D (cupLength k) (cupDegree k)).hom
        (filteredChernProduct B D k L) = deRhamChernProduct B D k L
```

**`AlgebraicGeometry.SheafOfModules.deRhamChernProduct_mem_hodgeFiltrationAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean#L377). The attribute's comment: “Remark 50.9.2, clause H of A-I: the a-fold product c₁^dR(L₁) ∪ … ∪ c₁^dR(L_a), for the cup product of Cohomology Section 0FKU on de Rham cohomology (`deRhamCup`), is contained in the a-th step F^a H^{2a}_dR(X/S) of the Hodge filtration, for every a”.

> **Stacks Project, Tag 0FME.** **`c₁^{dR}(L₁) ∪ … ∪ c₁^{dR}(L_a)` lies in
> `F^a H^{2a}_{dR}(X/S)`**, the `a`-th step of the Hodge filtration of Tag 0FM8.
>
> The step `F^a H^{2a}_{dR}` is the image of `H^{2a}(X, σ^{≥a}Ω^•) ⟶ H^{2a}_{dR}`, and
> `AlgebraicGeometry.SheafOfModules.truncatedDeRhamCohomologyAbelianMap_filteredChernProduct`
> exhibits the `a`-fold product as the image of `ξ` under exactly that map. Membership in the step is
> written as in
> `AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian_mem_hodgeFiltrationAbelian`: the
> class is the image of an element of the subobject.

```lean
theorem deRhamChernProduct_mem_hodgeFiltrationAbelian (k : ℕ)
    (L : ℕ → Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    ∃ y : (hodgeFiltrationAbelian B D (cupLength k) (cupDegree k) : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D (cupLength k) (cupDegree k)).arrow).hom y =
        deRhamChernProduct B D k L
```

**`AlgebraicGeometry.SheafOfModules.hodgeGradedIso_inv_gradedPieceProjection_filteredChernProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean#L433). The attribute's comment: “Remark 50.9.2, clause I of A-I, with the sign the identifications force: the map σ^{≥a}Ω^• ⟶ Ω^a[-a] sends ξ to (-1)^{a(a-1)/2} · c₁^Hodge(L₁) ∪ … ∪ c₁^Hodge(L_a) in H^{2a}(X, Ω^a[-a]) = H^a(X, Ω^a), for every a, the cup product being the Hodge cup product of Tag 0FM4 (`hodgeCup`: the cup product of Cohomology Section 0FKU along the wedge product Ω^p ⊗ Ω^q ⟶ Ω^{p+q} on the sheaves of forms in degree 0). The source states it without the sign; the sign is -1 for a ≡ 2, 3 mod 4”.

> **Stacks Project, Tag 0FME.** **The image of `ξ = γ₁(L₁) ∪ … ∪ γ₁(L_a)` under
> `σ^{≥a}Ω^• ⟶ Ω^a_{𝒪_X/A}[-a]`, read in `H^a(X, Ω^a_{𝒪_X/A})`, is
> `(-1)^{a(a - 1)/2} · c₁^{Hodge}(L₁) ∪ … ∪ c₁^{Hodge}(L_a)`**, the cup product being the one on
> Hodge cohomology of Tag 0FM4, `AlgebraicGeometry.SheafOfModules.hodgeCup`: the cup product of
> Cohomology, Section 0FKU along the wedge product `Ω^p ⊗_A Ω^q ⟶ Ω^{p + q}` on the sheaves of forms
> placed in degree `0`. The identification `H^{2a}(X, Ω^a[-a]) = H^a(X, Ω^a)` is
> `AlgebraicGeometry.SheafOfModules.hodgeGradedIso`, the comparison of the two indexings of the
> right derived functors followed by the degree shift of
> `DerivedCategory.Plus.singleFunctorCompHomologyFunctorShiftIso`, which for `a = 1` is the
> identification of clause `E`.
>
> **The sign.** The source states clause `I` without a sign. Through these identifications the cup
> product on the graded pieces is the Hodge cup product up to `(-1)^{ib}` on
> `H^{i + a}(Ω^a[-a]) × H^{j + b}(Ω^b[-b])`
> (`AlgebraicGeometry.SheafOfModules.hodgeCohomologyIsoGradedPiece_gradedPieceCup`): moving the
> shift `[-b]` of the second factor past a class of degree `i` costs `(-1)^{ib}`
> (`Stacks.Cohomology.DerivedGlobalCupProduct.totalCupPairing_shift₂`), and moving the shift `[-a]`
> of the first factor costs nothing (`totalCupPairing_shift₁`). Each new factor `c₁(L)` has `i = 1`,
> so the `(k + 1)`-st factor contributes `(-1)^k`, and the product of `a` factors carries
> `(-1)^{0 + 1 + ⋯ + (a - 1)} = (-1)^{a(a - 1)/2}`, which is `-1` for `a ≡ 2, 3 mod 4`. This is the
> corrected form of clause `I`.

```lean
theorem hodgeGradedIso_inv_gradedPieceProjection_filteredChernProduct (k : ℕ)
    (L : ℕ → Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    (hodgeGradedIso B D (k + 1) (k + 1) (cupLength k) (cupDegree k) (cast_eq_cupLength k)
        (cast_add_cupLength k)).inv.hom
      ((gradedPieceProjectionCohomologyMap B D (cupLength k) (cupDegree k)).hom
        (filteredChernProduct B D k L)) =
      hodgeChernSign k • hodgeCupChernProduct B D k L
```

**`AlgebraicGeometry.SheafOfModules.remark_filteredFirstChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/CanonicalChernCupProduct.lean#L478). The attribute's comment: “Remark 50.9.2 IN FULL: ALL NINE CLAUSES A-I, FOR EVERY a. The conjuncts in order are A (d log as a map into σ^{≥1}Ω^•, pinned down to d log), B (the class γ₁(L), the morphism `filteredFirstChernClass` the conjuncts speak of), C (its image in H²_dR is c₁^dR), D (so c₁^dR ∈ F¹H²_dR), E (its image in H²(Ω¹[-1]) = H¹(Ω¹) is c₁^Hodge), F (the a-fold product ξ, the class `filteredChernProduct` the conjuncts speak of), G (its image in H^{2a}_dR is the a-fold product of the c₁^dR), H (so that product lies in F^a H^{2a}_dR) and I (its image in H^{2a}(Ω^a[-a]) = H^a(Ω^a) is (-1)^{a(a-1)/2} times the a-fold Hodge cup product of Tag 0FM4 of the c₁^Hodge, the sign being the one the identifications force, absent from the source). Every cup product is the one of Cohomology Section 0FKU along the multiplication the source names”.

> **Stacks Project, Tag 0FME.** **Remark 50.9.2 in full**: all nine clauses of the remark, for
> every number `a = k + 1` of invertible modules, in one statement. In order:
>
> * **(A)** `d log`, viewed as a map `𝒪_X^*[-1] ⟶ σ^{≥1}Ω^•_{𝒪_X/A}` — the morphism is
>   `AlgebraicGeometry.SheafOfModules.filteredLogarithmicDifferentialComplexMap`, and the first
>   conjunct says that it is `d log`;
> * **(B)** the class `γ₁(L) ∈ H²(X, σ^{≥1}Ω^•)` — the morphism
>   `AlgebraicGeometry.SheafOfModules.filteredFirstChernClass` occurring in the conjuncts below;
> * **(C)** the image of `γ₁(L)` under `σ^{≥1}Ω^• ⟶ Ω^•` is `c₁^{dR}(L)`;
> * **(D)** hence `c₁^{dR}(L) ∈ F¹H²_{dR}(X/S)`;
> * **(E)** the image of `γ₁(L)` under `σ^{≥1}Ω^• ⟶ Ω¹[-1]` is `c₁^{Hodge}(L)`;
> * **(F)** the `a`-fold cup product `ξ = γ₁(L₁) ∪ … ∪ γ₁(L_a) ∈ H^{2a}(X, σ^{≥a}Ω^•)` — the class
>   `AlgebraicGeometry.SheafOfModules.filteredChernProduct` occurring in the conjuncts below;
> * **(G)** the image of `ξ` under `σ^{≥a}Ω^• ⟶ Ω^•` is `c₁^{dR}(L₁) ∪ … ∪ c₁^{dR}(L_a)` in
>   `H^{2a}_{dR}(X/S)`;
> * **(H)** hence that product lies in `F^a H^{2a}_{dR}(X/S)`;
> * **(I)** the image of `ξ` under `σ^{≥a}Ω^• ⟶ Ω^a[-a]`, read in `H^a(X, Ω^a_{𝒪_X/A})`, is
>   `(-1)^{a(a - 1)/2} · c₁^{Hodge}(L₁) ∪ … ∪ c₁^{Hodge}(L_a)` for the Hodge cup product of
>   Tag 0FM4; the sign, absent from the source, is the one the identifications force (see
>   `hodgeGradedIso_inv_gradedPieceProjection_filteredChernProduct`).
>
> Each conjunct is one of the theorems above or of
> `StacksFrontier.AlgebraicGeometry.DeRham.FirstChernClass.FilteredFirstChernClass`.

```lean
theorem remark_filteredFirstChernClass (k : ℕ)
    (L : ℕ → Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    (filteredLogarithmicDifferentialComplexMap B D ≫
        HomologicalComplex.ιStupidTrunc (deRhamAbelianComplexInt B D) (embeddingUpIntGE 1) =
      logarithmicDifferentialComplexMap B D) ∧
    (∀ c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
        (structureSheaf X.sheaf).property,
      deRhamFirstChernClassAbelian B D c =
        (truncatedDeRhamCohomologyAbelianMap B D 1 2).hom (filteredFirstChernClass B D c)) ∧
    (∀ c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
        (structureSheaf X.sheaf).property,
      ∃ y : (hodgeFiltrationAbelian B D 1 2 : AddCommGrpCat.{u}),
        ((hodgeFiltrationAbelian B D 1 2).arrow).hom y = deRhamFirstChernClassAbelian B D c) ∧
    (∀ c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
        (structureSheaf X.sheaf).property,
      (degreeOneProjectionCohomologyMap B D).hom (filteredFirstChernClass B D c) =
        (sheafCohomologyOneIsoShiftedCohomologyTwo X.carrier
          ((deRhamAbelianComplex B D).X 1)).hom.hom (hodgeFirstChernClassAbelian B D c)) ∧
    ((truncatedDeRhamCohomologyAbelianMap B D (cupLength k) (cupDegree k)).hom
      (filteredChernProduct B D k L) = deRhamChernProduct B D k L) ∧
    (∃ y : (hodgeFiltrationAbelian B D (cupLength k) (cupDegree k) : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D (cupLength k) (cupDegree k)).arrow).hom y =
        deRhamChernProduct B D k L) ∧
    ((hodgeGradedIso B D (k + 1) (k + 1) (cupLength k) (cupDegree k) (cast_eq_cupLength k)
        (cast_add_cupLength k)).inv.hom
      ((gradedPieceProjectionCohomologyMap B D (cupLength k) (cupDegree k)).hom
        (filteredChernProduct B D k L)) =
      hodgeChernSign k • hodgeCupChernProduct B D k L)
```

**`AlgebraicGeometry.SheafOfModules.filteredLogarithmicDifferentialComplexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L326). The attribute's comment: “d log as a map to the first step of the Hodge filtration”.

> **Stacks Project, Tag 0FME.** **Logarithmic differentiation as a morphism of complexes into
> the first step of the Hodge filtration**, `d log : 𝒪_X^*[-1] ⟶ σ^{≥1}Ω^•_{𝒪_X/A}`.
>
> The source is concentrated in degree one, hence strictly supported in degrees `≥ 1`, so the
> morphism `AlgebraicGeometry.SheafOfModules.logarithmicDifferentialComplexMap` into the de Rham
> complex factors uniquely through the brutal truncation.

```lean
def filteredLogarithmicDifferentialComplexMap :
    unitsComplex X ⟶ (deRhamAbelianComplexInt B D).stupidTrunc (embeddingUpIntGE 1)
```

**`AlgebraicGeometry.SheafOfModules.filteredLogarithmicDifferentialComplexMap_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L339). The attribute's comment: “Remark 50.9.2, clause A of A-I, the theorem half: the factorization of d log through σ^{≥1}Ω^• IS d log, composing with σ^{≥1}Ω^• ⟶ Ω^• back to the unfiltered one. This is what pins `filteredLogarithmicDifferentialComplexMap` down to the source's map rather than to some morphism into the truncation. The covering set here is the a = 1 case, clauses A-E; the a ≥ 2 clauses F-I are proved for every a in `StacksFrontier.AlgebraicGeometry.DeRham.FirstChernClass.CanonicalChernCupProduct`”.

> The factorization of `d log` through the brutal truncation is one: composing it with the
> inclusion of the truncation returns the unfiltered logarithmic differential.

```lean
theorem filteredLogarithmicDifferentialComplexMap_ι :
    filteredLogarithmicDifferentialComplexMap B D ≫
        HomologicalComplex.ιStupidTrunc (deRhamAbelianComplexInt B D)
          (embeddingUpIntGE 1) =
      logarithmicDifferentialComplexMap B D
```

**`AlgebraicGeometry.SheafOfModules.filteredFirstChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L542). The attribute's comment: “the filtered first Chern class”.

> **Stacks Project, Tag 0FME.** **The first Chern class in Hodge-filtered de Rham
> cohomology.** Logarithmic differentiation is a morphism of complexes of abelian sheaves
> `𝒪_X^*[-1] ⟶ σ^{≥1}Ω^•_{𝒪_X/A}`, and `Pic(X) = H¹(X, 𝒪_X^*) = H²(X, 𝒪_X^*[-1])`; the class
> `γ₁(L) ∈ H²(X, σ^{≥1}Ω^•_{𝒪_X/A})` of an invertible module is the image of its Picard class
> under the composite.

```lean
def filteredFirstChernClass :
    Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj (structureSheaf X.sheaf).property →+
      truncatedDeRhamCohomologyAbelian B D 1 2
```

**`AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L568). The attribute's comment: “Remark 50.9.2, clause C of A-I: the image of γ₁(L) under σ^{≥1}Ω^• ⟶ Ω^• is the de Rham first Chern class c₁^dR(L). The a = 1 case; the a ≥ 2 analogue, clause G, is `truncatedDeRhamCohomologyAbelianMap_filteredChernProduct` in `StacksFrontier.AlgebraicGeometry.DeRham.FirstChernClass.CanonicalChernCupProduct`, which this is the base case of”.

> **The de Rham first Chern class is the image of the Hodge-filtered one** under the map
> `H²(X, σ^{≥1}Ω^•) ⟶ H²_{dR}` induced by the inclusion of the first filtered step. In
> particular `c₁^{dR}(L)` lies in the first step of the Hodge filtration,
> `AlgebraicGeometry.SheafOfModules.hodgeFiltrationAbelian`, that step being by definition the
> image of that map.

```lean
theorem deRhamFirstChernClassAbelian_eq
    (c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    deRhamFirstChernClassAbelian B D c =
      (truncatedDeRhamCohomologyAbelianMap B D 1 2).hom (filteredFirstChernClass B D c)
```

**`AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian_mem_hodgeFiltrationAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L589). The attribute's comment: “Remark 50.9.2, clause D of A-I: c₁^dR(L) lies in the first step F¹H²_dR of the Hodge filtration. The a = 1 case; the a ≥ 2 analogue, clause H, that the a-fold product c₁^dR(L₁) ∪ … ∪ c₁^dR(L_a) lies in F^a H^{2a}_dR, is `deRhamChernProduct_mem_hodgeFiltrationAbelian` in `StacksFrontier.AlgebraicGeometry.DeRham.FirstChernClass.CanonicalChernCupProduct`”.

> **Stacks Project, Tag 0FME.** **`c₁^{dR}(L)` lies in `F¹H²_{dR}(X/S)`**, the first step of
> the Hodge filtration of Tag 0FM8.
>
> The step `F¹H²_{dR}` is the image of `H²(X, σ^{≥1}Ω^•) ⟶ H²_{dR}`, and
> `AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelian_eq` exhibits `c₁^{dR}(L)` as the
> image of `γ₁(L)` under exactly that map; the witness is therefore `γ₁(L)` pushed into the
> image.

```lean
theorem deRhamFirstChernClassAbelian_mem_hodgeFiltrationAbelian
    (c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    ∃ y : (hodgeFiltrationAbelian B D 1 2 : AddCommGrpCat.{u}),
      ((hodgeFiltrationAbelian B D 1 2).arrow).hom y =
        deRhamFirstChernClassAbelian B D c
```

**`AlgebraicGeometry.SheafOfModules.hodgeFirstChernClassAbelian_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L635). The attribute's comment: “Remark 50.9.2, clause E of A-I: the image of γ₁(L) under σ^{≥1}Ω^• ⟶ Ω¹[-1] is the Hodge first Chern class c₁^Hodge(L) ∈ H¹(X, Ω¹). The a = 1 case; the a ≥ 2 analogue, clause I, is `hodgeGradedIso_inv_gradedPieceProjection_filteredChernProduct` in `StacksFrontier.AlgebraicGeometry.DeRham.FirstChernClass.CanonicalChernCupProduct`, which this is the base case of”.

> **Stacks Project, Tag 0FME.** **The image of `γ₁(L)` under `σ^{≥1}Ω^• ⟶ Ω¹_{𝒪_X/A}[-1]`
> recovers `c₁^{Hodge}(L)`**, read through the identification `H¹(X, Ω¹) ≅ H²(X, Ω¹[-1])` of
> `sheafCohomologyOneIsoShiftedCohomologyTwo`.
>
> Both sides are the image of the Picard class under a map on degree-two hypercohomology induced
> by `d log : 𝒪_X^*[-1] ⟶ Ω¹[-1]`: on the left because the projection composed with the filtered
> `d log` is that map (`filteredLogarithmicDifferentialComplexMapPlus_degreeOneProjectionPlus`), on
> the right because the identification is natural in the sheaf
> (`sheafCohomologyOneIsoShiftedCohomologyTwo_hom_naturality`).

```lean
theorem hodgeFirstChernClassAbelian_eq
    (c : Stacks.SheafOfModules.Picard.PicardGroup X.sheaf.obj
      (structureSheaf X.sheaf).property) :
    (degreeOneProjectionCohomologyMap B D).hom (filteredFirstChernClass B D c) =
      (sheafCohomologyOneIsoShiftedCohomologyTwo X.carrier
          ((deRhamAbelianComplex B D).X 1)).hom.hom
        (hodgeFirstChernClassAbelian B D c)
```

**`AlgebraicGeometry.SheafOfModules.filteredFirstChernClassOf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/FilteredFirstChernClass.lean#L674). The attribute's comment: “the filtered first Chern class of an invertible module”.

> **Stacks Project, Tag 0FME.** The Hodge-filtered first Chern class of an invertible
> module.

```lean
abbrev filteredFirstChernClassOf (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L) :
    truncatedDeRhamCohomologyAbelian B D 1 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.9, Tag 0FLE](https://stacks.math.columbia.edu/tag/0FLE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
