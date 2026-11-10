---
declaration: section
origin: cited
lean: Stacks.Duality.ProjectiveBundleDualizing.nonempty_dualizingObject_iso_twistedInverseImage, Stacks.Duality.BlowupBaseChange.baseChange_example, Stacks.Duality.normalSheafToSheafExtOne, Stacks.Duality.isIso_normalSheafToSheafExtOne, Stacks.Duality.secondOrderThickening_shortExact, Stacks.AlgebraicGeometry.RegularIdealSheaf.isIso_desc_app_isKoszulRegularIdealSheaf, Stacks.RegularSequence.KoszulChainData.isZero_derivedSheafExt_unit_of_notMem_Icc, Stacks.AlgebraicGeometry.RegularIdealSheaf.nonempty_derivedSheafHom_iso_rankExterior
statement: formalized
proof: formalized
---

# 48.15 Right adjoint of pushforward in examples

Section 48.15 of the Stacks Project, [Tag 0BQV](https://stacks.math.columbia.edu/tag/0BQV). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A9W, a lemma

[Tag 0A9W](https://stacks.math.columbia.edu/tag/0A9W) in the Stacks Project.

**`Stacks.Duality.ProjectiveBundleDualizing.nonempty_dualizingObject_iso_twistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProjectiveBundle/TwistedInverseImage.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProjectiveBundle/TwistedInverseImage.lean#L471). The attribute's comment: “the projective bundle P(E) is the relative Proj of Sym(E) with twists O(d) of a twist datum D, and f^*L(-n-1) is written O(-n-1) ⊗ π^*(∧^(n+1) E); the special case E = O^(n+1) on projectiveSpaceOver is nonempty_twistedInverseImage_derivedStructureSheaf_iso_of_qcqs”.

> **[Stacks, Tag 0A9W].** Let `S` be a quasi-compact and quasi-separated scheme, `ℰ` a finite
> locally free `𝒪_S`-module of rank `n + 1` with determinant `𝓛 = ⋀ⁿ⁺¹ ℰ`, `π : 𝐏(ℰ) ⟶ S` the
> projection and `a` the right adjoint of `R π_* : D_QCoh(𝒪_{𝐏(ℰ)}) ⥤ D_QCoh(𝒪_S)` of
> [Stacks, Tag 0A9E]. Then `π^*𝓛(-n-1)[n] ≅ a(𝒪_S)`, for every `n ≥ 0`; the isomorphism is the
> transpose `dualizingComparison` of the trace `R π_*(π^*𝓛(-n-1)[n]) ≅ 𝒪_S`.
>
> For `ℰ = 𝒪_S^{⊕ n+1}` and projective space in the model `projectiveSpaceOver`, the statement
> `a(𝒪_S) ≅ 𝒪(-n-1)[n]` is
> `Stacks.Duality.ProjectiveSpace.nonempty_twistedInverseImage_derivedStructureSheaf_iso_of_qcqs`.

```lean
theorem nonempty_dualizingObject_iso_twistedInverseImage :
    haveI := quasiCompact_proj E hqc hfree
    haveI := AlgebraicGeometry.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward (proj E hqc)
    Nonempty (dualizingObject E hqc D hfree ≅ (twistedInverseImage (proj E hqc)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs (proj E hqc))).obj
        (DerivedPushforward.derivedStructureSheaf S))
```

## Tag 0AAC, an example

[Tag 0AAC](https://stacks.math.columbia.edu/tag/0AAC) in the Stacks Project.

**`Stacks.Duality.BlowupBaseChange.baseChange_example`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/BlowupBaseChange/Example.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/BlowupBaseChange/Example.lean#L238).

> **[Stacks, Example 0AAC]: the base change map (48.5.0.1) is not an isomorphism for a
> perfect proper `f` and a perfect `g`.** Let `k` be a field, `f : X ⟶ Y = 𝐀²_k` the blowup of
> the origin, `g : Y' = Spec k ⟶ Y` the origin and `X' = E = 𝐏¹_k` the exceptional divisor, with
> `g' : X' ⟶ X` its inclusion and `f' : X' ⟶ Y'` its structure morphism; let `a`, `a'` be the right
> adjoints of `Rf_*`, `Rf'_*` on `D_QCoh` ([Stacks, Tag 0A9E]). Then `f` is proper and perfect, `g`
> is perfect, the square is cartesian, `f` and `g` are not Tor independent, and no morphism
> `L(g')^* a(𝒪_Y) ⟶ a'(Lg^* 𝒪_Y)` — in particular no base change map — is an isomorphism.

```lean
theorem baseChange_example :
    IsProper (f k) ∧ Perfect (f k) ∧ Perfect (g k) ∧
      IsPullback (g' k) (projToSpecCoeff k 1) (f k) (g k) ∧ ¬ TorIndependent (f k) (g k) ∧
      ∀ φ : (twistedInverseImage (f k)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f k)) ⋙
            quasiCoherentDerivedPullback' (g' k)).obj (structureSheaf k) ⟶
        (quasiCoherentDerivedPullback' (g k) ⋙
          twistedInverseImage (projToSpecCoeff k 1)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs (projToSpecCoeff k 1))).obj
            (structureSheaf k), ¬ IsIso φ
```

## Tag 0BQW, a lemma

[Tag 0BQW](https://stacks.math.columbia.edu/tag/0BQW) in the Stacks Project.

**`Stacks.Duality.normalSheafToSheafExtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean#L415). The attribute's comment: “the canonical map `c` itself; `isIso_normalSheafToSheafExtOne` is the assertion that it is an isomorphism”.

> **The canonical map `c` of [Stacks, Tag 0BQW].** The normal sheaf
> `𝒩 = 𝓗om_{𝒪_Y}(ℐ/ℐ², 𝒪_X)` maps canonically to `𝓔xt¹_{𝒪_Y}(𝒪_X, 𝒪_X)`: precompose with
> `ℐ ↠ ℐ/ℐ²` to land in `𝓗om_{𝒪_Y}(ℐ, 𝒪_X)`, identify that with the degree-zero cohomology of
> `𝓗om_{𝒪_Y}(ℐ, J)` for the injective resolution `J` of `𝒪_X` that the derived functor uses, and
> take the degree-one connecting map of `sheafHomComplexSequence`. On a local section of `𝒩` this
> is the class of the pushout of the second-order thickening sequence of [Stacks, Tag 0BQX] along
> it, which is how the source constructs `c`.

```lean
public def normalSheafToSheafExtOne :
    normalSheafOfIdealSheaf Y I ⟶
      Stacks.RingedSpace.sheafExt Y (quotientByIdealSheaf Y I) (quotientByIdealSheaf Y I) 1
```

**`Stacks.Duality.isIso_normalSheafToSheafExtOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean, line 815](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean#L815).

> **Stacks Project, Tag 0BQW.** Let `Y` be a ringed space, let `ℐ ⊆ 𝒪_Y` be a sheaf of
> ideals, put `𝒪_X = 𝒪_Y/ℐ` and let `𝒩 = 𝓗om_{𝒪_Y}(ℐ/ℐ², 𝒪_X)` be the normal sheaf. The
> canonical map `c : 𝒩 ⟶ 𝓔xt¹_{𝒪_Y}(𝒪_X, 𝒪_X)` of `normalSheafToSheafExtOne` is an
> isomorphism.
>
> All four inputs of the source's proof are proved here:
> `isIso_internalHomMapLeft_cokernelπ_idealSquareInclusion` (every `𝒪_Y`-linear map
> `ℐ ⟶ 𝒪_X` factors uniquely through `ℐ/ℐ²`), `internalHomMapLeft_ι_app_quotient_eq_zero`
> (the degree-zero map vanishes, because `ℐ` annihilates `𝒪_X`),
> `sheafHomComplexSequence_shortExact` ([Stacks, Tag 01DR] for sheaves of modules) and
> `Stacks.RingedSpace.isZero_sheafExt_unit_succ` (`𝓔xt¹_{𝒪_Y}(𝒪_Y, 𝒪_X) = 0`).

```lean
public theorem isIso_normalSheafToSheafExtOne :
    IsIso (normalSheafToSheafExtOne Y I)
```

## Tag 0BQX, an equation

[Tag 0BQX](https://stacks.math.columbia.edu/tag/0BQX) in the Stacks Project.

**`Stacks.Duality.secondOrderThickening_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Sweep/SecondOrderThickening.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Sweep/SecondOrderThickening.lean#L89).

> **Stacks Project, Tag 0BQX.** For an ideal sheaf `I` on a ringed space, the canonical
> sequence
> `0 ⟶ I / I² ⟶ 𝒪_Y / I² ⟶ 𝒪_Y / I ⟶ 0`
> is short exact. The displayed equations say that its arrows are induced by the inclusion
> `I ⟶ 𝒪_Y` and the identity of `𝒪_Y`, respectively.

```lean
public theorem secondOrderThickening_shortExact (Y : RingedSpace.{u, u})
    (I : (SheafOfModules.unit (structureSheafRing Y)).Submodule) :
    let I2 := idealSquare Y I
    ∃ (j : I2.toSheafOfModules ⟶ I.toSheafOfModules)
      (_hj : j ≫ I.ι = I2.ι)
      (f : cokernel j ⟶ cokernel I2.ι)
      (g : cokernel I2.ι ⟶ cokernel I.ι)
      (hzero : f ≫ g = 0),
      (cokernel.π j ≫ f = I.ι ≫ cokernel.π I2.ι) ∧
        (cokernel.π I2.ι ≫ g = cokernel.π I.ι) ∧
          (ShortComplex.mk f g hzero).ShortExact
```

## Tag 0BQY, a lemma

[Tag 0BQY](https://stacks.math.columbia.edu/tag/0BQY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isIso_desc_app_isKoszulRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulSelfExtKoszulRegular.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulSelfExtKoszulRegular.lean#L148).

> Let `Y` be a ringed space, `𝓘 ⊆ O_Y` a Koszul-regular sheaf of ideals and `O_X = O_Y/𝓘`.
> Let `A` be, with its degree-one generator `ι`, the exterior algebra over `O_X` of
> `Ext¹_{O_Y}(O_X, O_X)`.  Then the homomorphism of sheaves of graded algebras that the identity of
> `Ext¹_{O_Y}(O_X, O_X)` induces out of `A` — the comparison
>
> `⋀ⁿ(Ext¹_{O_Y}(O_X, O_X)) ⟶ Extⁿ_{O_Y}(O_X, O_X)`
>
> that composition makes — is an isomorphism in every degree `n`.

```lean
theorem isIso_desc_app_isKoszulRegularIdealSheaf (hJ : IsKoszulRegularIdealSheaf Y J)
    (A : _root_.SheafOfModules.GradedAlgebra.{u, u}
      (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} (quotientRingSheaf.{u, u, u} J)))
    (ι : (koszulRegularSelfExtAlgebra J hJ).piece 1 ⟶ A.piece 1)
    (hA : _root_.SheafOfModules.GradedAlgebra.IsExteriorAlgebra A ι) (n : ℤ) :
    IsIso ((hA.desc (koszulRegularSelfExtAlgebra J hJ)
      (𝟙 ((koszulRegularSelfExtAlgebra J hJ).piece 1))
      (squareZero_id_koszulRegularSelfExtAlgebra J hJ)).app n)
```

## Tag 0BQZ, a lemma

[Tag 0BQZ](https://stacks.math.columbia.edu/tag/0BQZ) in the Stacks Project.

**`Stacks.RegularSequence.KoszulChainData.isZero_derivedSheafExt_unit_of_notMem_Icc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulExtStructureSheaf.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulExtStructureSheaf.lean#L190). The attribute's comment: “ONLY the degrees outside `0, …, r` of the vanishing half of the tag: the Ext sheaves `Ext^i_{O_Y}(O_Y/I, O_Y)` are zero for `i < 0` and for `i > r`. Carried: the ideal sheaf is presented GLOBALLY by a Koszul-regular sequence of `r` sections -- a Koszul chain datum for `φ : (O_Y)^r ⟶ O_Y` whose augmentation is a quasi-isomorphism -- where the tag assumes only the local condition that `I` be Koszul-regular, so the opening reduction of its proof is not performed and the tag's locally varying `r` is here constant. NOT covered: the degrees `0, …, r - 1`, the identification of `Ext^r` with the top exterior power of the normal sheaf, and the derived-category isomorphism `RHom(O_X, O_Y) = (top exterior power of N)[-r]`”.

> **The Ext sheaves of a Koszul-regular quotient into the structure sheaf vanish outside the
> degrees `0, …, r`.** For an ideal sheaf `ℐ ⊂ O_Y` generated by a Koszul-regular sequence of `r`
> global sections, with quotient `O_X = O_Y/ℐ`,
>
> `𝓔xt^n_{O_Y}(O_X, O_Y) = 0` for `n < 0` and for `n > r`.
>
> This is part of the vanishing half of [Stacks, Tag 0BQZ], whose conclusion
> `R𝓗om_{O_Y}(O_X, O_Y) = ⋀^r 𝒩 [-r]` says that these Ext sheaves vanish in every degree other
> than `r` and that the `r`-th one is the top exterior power of the normal sheaf. The degrees
> `0, …, r - 1` and the degree `r` itself are not treated: they are where the differential of the
> Hom complex, which is not zero, has to be computed.

```lean
theorem isZero_derivedSheafExt_unit_of_notMem_Icc (K : KoszulChainData.{u, u, u} A φ)
    [QuasiIso K.augmentation] {n : ℤ} (hn : n < 0 ∨ (r : ℤ) < n) :
    IsZero (derivedSheafExt Rc
      (DerivedCategory.Q.obj
        ((single (StructureSheafModules Rc) (ComplexShape.up ℤ) 0).obj
          (quotient Rc (φ := φ))))
      (DerivedCategory.Q.obj (unitSingleComplex Rc)) n)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.nonempty_derivedSheafHom_iso_rankExterior`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulRegularDerivedDual.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularSequence/KoszulRegularDerivedDual.lean#L806).

> **Stacks Project, Tag 0BQZ.** Let `Y` be a ringed space, `𝓘 ⊆ O_Y` a sheaf of ideals,
> `O_X = O_Y/𝓘` and `𝒩 = 𝓗om_{O_Y}(𝓘/𝓘², O_X)`. If `𝓘` is Koszul-regular, then
>
> `R𝓗om_{O_Y}(O_X, O_Y) ≅ ⋀^r 𝒩 [-r]`
>
> in `D(O_Y)`, where `r : Y → ℕ` sends `y` to the minimal number of generators of `𝓘` needed in a
> neighbourhood of `y` (`localGeneratorCount`). The right-hand side is the complex with zero
> differential whose degree-`n` term is the `n`-th exterior power of `𝒩` over `O_X` (the exterior
> algebra `SheafOfModules.algebras` of `normalSheafQuotient`) on the locus where `r = n`, extended
> by zero (`rankExteriorTerm`): `r` is locally constant on the support of `O_X`, and every term of
> the formula vanishes off it. See the module docstring for the codomain of `r`.

```lean
theorem nonempty_derivedSheafHom_iso_rankExterior (hJ : IsKoszulRegularIdealSheaf Y J) :
    Nonempty (((derivedSheafHom Y.sheaf).obj (op (DerivedCategory.Q.obj
        ((single (StructureSheafModules Y.sheaf) (ComplexShape.up ℤ) 0).obj (cokernel J.ι))))).obj
        (DerivedCategory.Q.obj ((single (StructureSheafModules Y.sheaf) (ComplexShape.up ℤ) 0).obj
          (_root_.SheafOfModules.unit (structureSheaf Y.sheaf)))) ≅
      DerivedCategory.Q.obj (CochainComplex.zeroDifferentialComplex (rankExteriorTerm (J := J)
        (_root_.SheafOfModules.algebras (Opens.grothendieckTopology Y.carrier)
          (normalSheafQuotient J)).exterior)))
```

## Tag 0BR0, a lemma

[Tag 0BR0](https://stacks.math.columbia.edu/tag/0BR0) in the Stacks Project.

**`Stacks.Duality.KoszulRegular.nonempty_normalExteriorComplex_iso_rightAdjoint_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulRegularRightAdjoint.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/KoszulRegularRightAdjoint.lean#L135).

> **Stacks Project, Tag 0BR0.** Let `Y` be a quasi-compact and quasi-separated scheme, let
> `i : X ⟶ Y` be a Koszul-regular closed immersion, and let `a` be the right adjoint of
> `Ri_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of [Stacks, Tag 0A9E]. Then there is an isomorphism
>
> `⋀^r 𝒩 [-r] ≅ a(𝒪_Y)`,
>
> where `𝒩 = 𝓗om_{𝒪_X}(𝒞_{X/Y}, 𝒪_X)` is the normal sheaf of `i` (`Stacks.Divisors.normalSheaf`)
> and `r` is its rank, a locally constant function on `X` (`normalRank`). Since `r` is only locally
> constant, `⋀^r 𝒩 [-r]` is the complex with zero differential whose degree-`n` term is `⋀ⁿ𝒩` on
> the open and closed locus where `r = n`, extended by zero (`normalExteriorComplex`): on that locus
> it is `⋀ⁿ𝒩[-n]`.
>
> The right adjoint `a` is quantified over together with its adjunction, which determines it up to
> unique isomorphism; the derived categories are the locally small models
> `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory`, at which [Stacks, Tag 0A9E] produces `a`.
> The isomorphism is one of objects of `D(𝒪_X)`; `D_QCoh(𝒪_X)` being a full subcategory, it is an
> isomorphism there.
>
> The proof is the source's. By [Stacks, Tags 0A9X and 0A77], `a(𝒪_Y)` is `R ℰom(𝒪_X, 𝒪_Y)` and its
> pushforward is `R𝓗om_{𝒪_Y}(i_*𝒪_X, 𝒪_Y)`, which [Stacks, Tag 0BQZ] computes: its cohomology
> sheaves are `⋀ⁿ𝒩` on the locus where `r = n`, extended by zero
> (`Stacks.AlgebraicGeometry.RegularIdealSheaf.extIsoRankExteriorTerm`). As `i_*` is exact and fully
> faithful on modules ([Stacks, Tag 08KS]), the cohomology sheaves of `a(𝒪_Y)` are the terms of
> `⋀^r 𝒩 [-r]`; they are concentrated in one degree on each member of the disjoint open cover of
> `X` by the rank loci, so `a(𝒪_Y)` is isomorphic to the complex of its cohomology sheaves with zero
> differential (`Stacks.SheafOfModules.nonempty_iso_zeroDifferentialComplex_homology_of_cover`).

```lean
theorem nonempty_normalExteriorComplex_iso_rightAdjoint_structureSheaf
    [CompactSpace Y] [QuasiSeparatedSpace Y] (hi : IsKoszulRegularImmersion i)
    (a : quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X)
    (adj : DerivedPushforward.qcqsRestrictedDerivedPushforward i ⊣ a) :
    Nonempty ((DerivedCategory.Q (C := X.Modules)).obj (normalExteriorComplex i hi) ≅
      (a.obj (DerivedPushforward.derivedStructureSheaf Y)).obj)
```

## Tag 0BRT, a lemma

[Tag 0BRT](https://stacks.math.columbia.edu/tag/0BRT) in the Stacks Project.

**`Stacks.Duality.singleFunctorExteriorPowerIsoRelativeDualizingComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SmoothProper/RelativeDualizingComplex.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SmoothProper/RelativeDualizingComplex.lean#L40).

> **[Stacks, Tag 0BRT].** Let `S` be a Noetherian scheme and `f : X ⟶ S` a smooth proper
> morphism of relative dimension `d`, and let `a` be the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_S)` ([Stacks, Tag 0A9E]). Then there is an isomorphism
> `∧^d Ω_{X/S}[d] ≅ a(𝒪_S)` in `D(𝒪_X)`.

```lean
def singleFunctorExteriorPowerIsoRelativeDualizingComplex {X S : Scheme.{u}} [IsNoetherian S]
    (f : X ⟶ S) (d : ℕ) [SmoothOfRelativeDimension d f] [IsProper f] :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    (DerivedCategory.singleFunctor X.Modules (-d)).obj
        (Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f) d) ≅
      (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf S)).obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.15, Tag 0BQV](https://stacks.math.columbia.edu/tag/0BQV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
