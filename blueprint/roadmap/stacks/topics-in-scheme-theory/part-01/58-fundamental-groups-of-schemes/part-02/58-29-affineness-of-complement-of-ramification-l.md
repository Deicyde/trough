---
declaration: section
origin: cited
lean: Stacks.EtalePuncturedSpectrum.exists_directSum_injectiveHull_residueField, Stacks.SpectralSequence.isZero_derivedTensorHomology_zero_singleHomology_zero, Stacks.PuncturedSpectrum.isAffine_of_cohomologyOverBase_vanishing, Stacks.PuncturedSpectrum.isAffine_of_subsingleton_quotTensor_globalSections, Stacks.PuncturedSpectrum.isZero_derivedTensorHomology_cohomologyOverBase_residueField, Stacks.LocalCohomology.derivedSectionsMinus, AlgebraicGeometry.MaximalEtaleOpen.isAffineHom_maximalEtaleOpen
statement: formalized
proof: formalized
---

# 58.29 Affineness of complement of ramification locus

Section 58.29 of the Stacks Project, [Tag 0ECA](https://stacks.math.columbia.edu/tag/0ECA). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ECB, a lemma

[Tag 0ECB](https://stacks.math.columbia.edu/tag/0ECB) in the Stacks Project.

**`Stacks.EtalePuncturedSpectrum.exists_directSum_injectiveHull_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuncturedSpectrumCohomology.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuncturedSpectrumCohomology.lean#L641).

> **Stacks Project, Tag 0ECB.** Let `A` be a regular local ring containing a field `k`, let
> `f : V ⟶ Spec A` be étale and quasi-compact, and suppose `f` factors as `g ≫ U.ι` through the
> punctured spectrum `U = Spec A ∖ V(𝔪)` with `g` affine. Then for every `i > 0` the `A`-module
> `H ⁱ(V, 𝒪_V)` is a direct sum of copies of an injective hull `E` of the residue field of `A`.
>
> The index set and the isomorphism are not determined by the statement.

```lean
theorem exists_directSum_injectiveHull_residueField
    (A k E : Type u) [CommRing A] [IsRegularLocalRing A] [Field k] [Algebra k A]
    [AddCommGroup E] [Module A E]
    {V : Scheme.{u}} (f : V ⟶ Spec (.of A)) [Etale f] [QuasiCompact f]
    (g : V ⟶ (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)) [IsAffineHom g]
    (hg : g ≫ (complementZeroLocus A (IsLocalRing.maximalIdeal A)).ι = f)
    (i : ModuleCat.of A (IsLocalRing.ResidueField A) ⟶ ModuleCat.of A E) [Mono i]
    (hi : Module.IsInjectiveHull i) (n : ℕ) (hn : 0 < n) :
    ∃ J : Type u, Nonempty (structureSheafCohomology f n ≃ₗ[A] DirectSum J (fun _ => E))
```

## Tag 0ECC, a lemma

[Tag 0ECC](https://stacks.math.columbia.edu/tag/0ECC) in the Stacks Project.

**`Stacks.SpectralSequence.isZero_derivedTensorHomology_zero_singleHomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/OriginVanishing.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/OriginVanishing.lean#L188). The attribute's comment: “the cohomological step: the tensor spectral sequence at the origin”.

> Let `K` and `L` be bounded-above objects of the derived category of `A`-modules. Suppose
>
> * `H⁰(K ⊗^L L) = 0`;
> * `H^q(K) = 0` for `q < 0`;
> * `H^{-r}(H^{r-1}(K)[0] ⊗^L L) = 0` for every `r ≥ 2`.
>
> Then `H⁰(H⁰(K)[0] ⊗^L L) = 0`.

```lean
theorem isZero_derivedTensorHomology_zero_singleHomology_zero
    (K L : DerivedCategory.Minus (ModuleCat.{u} A))
    (habut : IsZero (derivedTensorHomology A K.1 L.1 0))
    (hneg : ∀ q : ℤ, q < 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj K.1))
    (hTor : ∀ r : ℤ, 2 ≤ r →
      IsZero (derivedTensorHomology A (singleHomology A K.1 (r - 1)) L.1 (-r))) :
    IsZero (derivedTensorHomology A (singleHomology A K.1 0) L.1 0)
```

**`Stacks.PuncturedSpectrum.isAffine_of_cohomologyOverBase_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/AffineOfCohomologyVanishing.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/AffineOfCohomologyVanishing.lean#L196). The attribute's comment: “the proof assembled under the source's own hypotheses: the cohomology vanishing above dim(A) - 1 is the hypothesis of the tag, and both cited inputs are proved — the abutment H⁰(RΓ(V,𝒪\_V) ⊗^L\_A A/𝔪) = 0 by computing the derived tensor product on an injective resolution against the Koszul complex of a generating family of the maximal ideal, which is acyclic because the standard opens of the generators cover V, and the Tor vanishing from Tags 0ECB and 0EBT”.

> **[Stacks, Tag 0ECC], the proof assembled, with the source's own degree bound.** In the
> situation of [Stacks, Tag 0ECB], write `d` for the Krull dimension of `A`. If
> `H ⁿ(V, 𝒪_V) = 0` for every `n ≥ d - 1`, then `V` is affine.
>
> Both inputs the source cites are discharged: the abutment `H⁰(RΓ(V, 𝒪_V) ⊗^L_A A/𝔪) = 0` by
> `Stacks.PuncturedSpectrum.isZero_derivedTensor_derivedSectionsOverBase_residueField`, and the
> vanishing of `Tor_r^A(H^{r-1}(V, 𝒪_V), A/𝔪)` for `2 ≤ r < d` by
> `Stacks.PuncturedSpectrum.isZero_derivedTensorHomology_cohomologyOverBase_residueField`. See the
> module documentation.

```lean
theorem isAffine_of_cohomologyOverBase_vanishing (A k : Type u) [CommRing A]
    [IsRegularLocalRing A] [Field k] [Algebra k A] {V : Scheme.{u}}
    (f : V ⟶ Spec (CommRingCat.of A)) [Etale f] [QuasiCompact f]
    (g : V ⟶ (Stacks.LocalCohomology.puncturedSpectrum (CommRingCat.of A) : Scheme))
    [IsAffineHom g]
    (hg : g ≫ (Stacks.LocalCohomology.puncturedSpectrum (CommRingCat.of A)).ι = f)
    (hvanish : ∀ n : ℕ, ((ringKrullDim A).unbotD 0).toNat - 1 ≤ n →
      IsZero (cohomologyOverBase A f (SheafOfModules.unit V.ringCatSheaf) n)) :
    IsAffine V
```

**`Stacks.PuncturedSpectrum.isAffine_of_subsingleton_quotTensor_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/AffineOverPuncturedSpectrum.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/AffineOverPuncturedSpectrum.lean#L272). The attribute's comment: “the final step: affineness once the residue field kills the global sections”.

> **[Stacks, Tag 0ECC], the final step of the proof.** In the situation of [Stacks, Tag 0ECB] —
> `A` a regular local ring containing a field `k`, `f : V ⟶ Spec A` étale and quasi-compact, and
> the structure morphism factored through the punctured spectrum `Spec A \ {𝔪}` by an affine
> morphism `g` — if `H⁰(V, 𝒪_V) ⊗_A A/𝔪 = 0`, then `V` is affine.
>
> This is the last paragraph of the source's proof: the vanishing of the residue tensor product
> says that a system of generators of `𝔪` maps to a system of generators of the unit ideal of
> `Γ(V, 𝒪_V)`, so the affine opens `V_{x_i}` cover `V`.
>
> What the source derives this vanishing from — the hypothesis `H^i(V, 𝒪_V) = 0` for
> `i ≥ dim(A) - 1`, Tag 0ECB, Tag 0EBT and cohomology and base change — is not formalized here;
> see the module documentation.
>
> The hypotheses of Tag 0ECB that this step does not use are nevertheless imposed, so that the
> statement is literally in the situation of that lemma. The ambient algebra structure on
> `Γ(V, 𝒪_V)` is required to be the one induced by `f`.

```lean
theorem isAffine_of_subsingleton_quotTensor_globalSections
    (A _k : Type u) [CommRing A] [IsRegularLocalRing A] [Field _k] [Algebra _k A]
    {V : Scheme.{u}} (f : V ⟶ Spec (CommRingCat.of A)) [Etale f] [QuasiCompact f]
    (g : V ⟶ (LocalCohomology.puncturedSpectrum (CommRingCat.of A) : Scheme)) [IsAffineHom g]
    (hg : g ≫ (LocalCohomology.puncturedSpectrum (CommRingCat.of A)).ι = f)
    [Algebra A Γ(V, ⊤)] (halg : algebraMap A Γ(V, ⊤) = baseHom f)
    (hzero : Subsingleton ((A ⧸ IsLocalRing.maximalIdeal A) ⊗[A] Γ(V, ⊤))) :
    IsAffine V
```

**`Stacks.PuncturedSpectrum.isZero_derivedTensorHomology_cohomologyOverBase_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/PuncturedSpectrumResidueFieldTor.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/PuncturedSpectrumResidueFieldTor.lean#L116). The attribute's comment: “the incoming terms of the tensor spectral sequence: Tor\_r(H ⁿ(V,𝒪\_V), A/𝔪) = 0 for n > 0 and r ≠ dim A, from Tags 0ECB and 0EBT”.

> **The incoming terms of the tensor spectral sequence of [Stacks, Tag 0ECC].** In the situation
> of [Stacks, Tag 0ECB] — `A` a regular local ring containing a field `k`, `f : V ⟶ Spec A` étale
> and quasi-compact, and the structure morphism factored through the punctured spectrum by an affine
> morphism `g` — write `d` for the Krull dimension of `A`. Then for every `n > 0` and every
> `r ≠ d`,
> `Tor_r^A(H ⁿ(V, 𝒪_V), A ⧸ 𝔪) = 0`,
> in the derived form `H ^{-r}(H ⁿ(V, 𝒪_V)[0] ⊗ᴸ_A (A ⧸ 𝔪)[0]) = 0`.
>
> By [Stacks, Tag 0ECB] the cohomology is a direct sum of copies of an injective hull of the residue
> field, by [Stacks, Tag 0EBT] each copy contributes nothing away from the dimension, and the
> derived tensor product commutes with the direct sum.

```lean
theorem isZero_derivedTensorHomology_cohomologyOverBase_residueField (A k : Type u) [CommRing A]
    [IsRegularLocalRing A] [Field k] [Algebra k A] {V : Scheme.{u}}
    (f : V ⟶ Spec (CommRingCat.of A)) [Etale f] [QuasiCompact f]
    (g : V ⟶ (LocalCohomology.puncturedSpectrum (CommRingCat.of A) : Scheme)) [IsAffineHom g]
    (hg : g ≫ (LocalCohomology.puncturedSpectrum (CommRingCat.of A)).ι = f)
    (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞)) (n : ℕ) (hn : 0 < n) (r : ℤ)
    (hr : r ≠ (d : ℤ)) :
    IsZero (derivedTensorHomology A
      ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (cohomologyOverBase A f (SheafOfModules.unit V.ringCatSheaf) n))
      ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ IsLocalRing.maximalIdeal A))) (-r))
```

**`Stacks.LocalCohomology.derivedSectionsMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/HigherDegree/DerivedSectionsOverBase.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/HigherDegree/DerivedSectionsOverBase.lean#L219). The attribute's comment: “the complex RΓ(V, 𝒪\_V) of A-modules, bounded above and concentrated in degrees ≥ 0”.

> **`RΓ(V, F)` as an object of the bounded above derived category `D⁻(A)`,** given a bound
> above which the cohomology of `F` on `V` vanishes.
>
> Together with `Stacks.LocalCohomology.nonempty_homology_derivedSectionsOverBase_iso` and
> `Stacks.LocalCohomology.isGE_derivedSectionsOverBase` this is the complex `RΓ(V, 𝒪_V)` the proof
> of [Stacks, Tag 0ECC] feeds to its spectral sequence: an object of `D⁻(A)` with no cohomology in
> negative degrees whose cohomology in degree `p` is `H^p(V, 𝒪_V)`.
>
> The attribute is qualified: this is the construction of that complex, not the whole tag. The
> remaining steps need Tags 08IB, 0ECB and 0EBT, none of which the library carries; see the module
> documentation.

```lean
def derivedSectionsMinus (f : V ⟶ Spec (.of A))
    (F : SheafOfModules.{u} V.ringCatSheaf) (a : ℤ)
    (hvanish : ∀ n : ℕ, a < (n : ℤ) → IsZero (cohomologyOverBase.{u, u} A f F n)) :
    DerivedCategory.Minus (ModuleCat.{u} A)
```

## Tag 0ECD, a theorem

[Tag 0ECD](https://stacks.math.columbia.edu/tag/0ECD) in the Stacks Project.

**`AlgebraicGeometry.MaximalEtaleOpen.isAffineHom_maximalEtaleOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/AffineMaximalEtaleOpen.lean, line 1451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/AffineMaximalEtaleOpen.lean#L1451). References: EGA IV (21.12.14), “special case”.

> **Stacks Project, Tag 0ECD.** Let `Y` be an excellent regular scheme over a field `k`, let
> `f : X ⟶ Y` be a morphism of finite type with `X` normal, and let `V ⊆ X` be the maximal open
> subscheme on which `f` is étale. Then the inclusion `V ⟶ X` is affine.
>
> `Y` regular is `AlgebraicGeometry.IsRegular` ([Stacks, Tag 02IS]); `Y` excellent is the existence
> around every point of an affine open neighbourhood whose ring of sections is excellent, which is
> the definition of an excellent scheme; `Y` over a field is a morphism `g : Y ⟶ Spec k`; finite
> type is `LocallyOfFiniteType` with `QuasiCompact`; `X` normal is `AlgebraicGeometry.IsNormal`
> ([Stacks, Tag 033I]); and "the maximal open subscheme where `f` is étale" is an open `V` that is
> the greatest element of the set of opens `U` with `U.ι ≫ f` étale. The proof uses purity of the
> ramification locus, `AlgebraicGeometry.etaleAt_of_etaleAt_codimensionOne` ([Stacks, Tag 0EA4]),
> and [Stacks, Tag 0ECC], `Stacks.PuncturedSpectrum.isAffine_of_cohomologyOverBase_vanishing`; see
> the module documentation. Quasi-compactness of `f` is not used by the argument.

```lean
theorem isAffineHom_maximalEtaleOpen
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsNormal X]
    (hYregular : IsRegular Y)
    (hYexcellent : ∀ y : Y, ∃ U : Y.affineOpens, y ∈ U.1 ∧ IsExcellent Γ(Y, U))
    (k : Type u) [Field k] (g : Y ⟶ Spec (.of k))
    (V : X.Opens) (hV : IsGreatest {U : X.Opens | Etale (U.ι ≫ f)} V) :
    IsAffineHom V.ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.29, Tag 0ECA](https://stacks.math.columbia.edu/tag/0ECA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
