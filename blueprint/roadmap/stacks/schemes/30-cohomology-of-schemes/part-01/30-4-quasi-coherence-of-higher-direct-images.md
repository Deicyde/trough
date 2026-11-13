---
declaration: section
origin: cited
lean: AlgebraicGeometry.baseChangeOverAffineBase_of_affineOpens, Stacks.AlgebraicGeometry.CompactOpenInduction.of_isCompact, Stacks.AlgebraicGeometry.CompactOpenInduction.top, Stacks.AlgebraicGeometry.InductionPrinciple.induction_isCompact_open, Stacks.AlgebraicGeometry.InductionPrinciple.induction_top, Stacks.Cohomology.AffineCover.isZero_cohomology_of_finite_affine_cover, Stacks.Cohomology.AffineCover.isZero_cohomologyPresheaf_of_affineCoveringNumber_le, AlgebraicGeometry.isZero_cohomology_of_affineCoverNum_le
statement: formalized
proof: formalized
---

# 30.4 Quasi-coherence of higher direct images

Section 30.4 of the Stacks Project, [Tag 01XH](https://stacks.math.columbia.edu/tag/01XH). 6 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08DR, a lemma

[Tag 08DR](https://stacks.math.columbia.edu/tag/08DR) in the Stacks Project.

**`AlgebraicGeometry.baseChangeOverAffineBase_of_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalBaseChange.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/GlobalBaseChange.lean#L345). The attribute's comment: “the induction of Stacks 0DJ9 from the affine opens of X to X itself”.

> **The induction of Stacks 0DJ9 over the quasi-compact opens of `X`.**  Granted the affine
> case and the Mayer--Vietoris step, the conclusion holds for every cartesian square over an affine
> base: an affine base makes `X` quasi-compact and quasi-separated, so the induction principle of
> Stacks 08DR carries the property from the affine opens to all of `X`.

```lean
public theorem baseChangeOverAffineBase_of_affineOpens
    (haffine : BaseChangeAffineOpenCase.{u}) (hstep : BaseChangeMayerVietorisStep.{u}) :
    BaseChangeOverAffineBase.{u}
```

**`Stacks.AlgebraicGeometry.CompactOpenInduction.of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CompactOpenInduction/Basic.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CompactOpenInduction/Basic.lean#L140). The attribute's comment: “induction on quasi-compact opens”.

> **[Stacks, Tag 08DR], the induction principle.** Let `X` be a quasi-separated scheme and let
> `P` be a property of its open subsets such that `P` holds for every affine open, and such that
> `P (U ⊔ V)` holds whenever `U` is quasi-compact open, `V` is affine open and `P U`, `P V`,
> `P (U ⊓ V)` hold. Then `P` holds for every quasi-compact open of `X`.
>
> Only the hypothesis `P (U ⊓ V)` has to be produced beyond what
> `AlgebraicGeometry.compact_open_induction_on` already supplies, and `U ⊓ V` is a quasi-compact
> open of the affine open `V`, so `of_le_isAffineOpen` produces it.

```lean
theorem of_isCompact [QuasiSeparatedSpace X] (S : X.Opens) (hS : IsCompact (S : Set X)) : P S
```

**`Stacks.AlgebraicGeometry.CompactOpenInduction.top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CompactOpenInduction/Basic.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CompactOpenInduction/Basic.lean#L153). The attribute's comment: “induction on quasi-compact opens”.

> **[Stacks, Tag 08DR], the conclusion at `X` itself.** For a quasi-compact quasi-separated
> scheme, `P ⊤` holds.

```lean
theorem top [QuasiSeparatedSpace X] [CompactSpace X] : P ⊤
```

**`Stacks.AlgebraicGeometry.InductionPrinciple.induction_isCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InductionPrinciple/Basic.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InductionPrinciple/Basic.lean#L169).

> **[Stacks, Tag 08DR], the Induction Principle.** Let `X` be a quasi-separated scheme and
> let `P` be a property of the opens of `X` which holds for every affine open and which, given a
> quasi-compact open `U` and an affine open `V`, passes from `U`, `V` and `U ⊓ V` to `U ⊔ V`.
> Then `P` holds for every quasi-compact open of `X`.
>
> The source assumes in addition that `X` is quasi-compact; that hypothesis is not used for the
> conclusion about an arbitrary quasi-compact open, and `induction_top` records the clause of the
> source that does use it.

```lean
theorem induction_isCompact_open [QuasiSeparatedSpace X] (W : X.Opens)
    (hW : IsCompact (W : Set X)) : P W
```

**`Stacks.AlgebraicGeometry.InductionPrinciple.induction_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InductionPrinciple/Basic.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InductionPrinciple/Basic.lean#L202). The attribute's comment: “in particular for X”.

> **[Stacks, Tag 08DR], the clause "and in particular for `X`".** On a quasi-compact
> quasi-separated scheme the induction principle applies to the whole space.

```lean
theorem induction_top [CompactSpace X] [QuasiSeparatedSpace X] : P ⊤
```

## Tag 01XI, a lemma

[Tag 01XI](https://stacks.math.columbia.edu/tag/01XI) in the Stacks Project.

**`Stacks.Cohomology.AffineCover.isZero_cohomology_of_finite_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/Basic.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/Basic.lean#L184). The attribute's comment: “finite-cover form”.

> If `X` has affine diagonal and is covered by `t` affine opens, then the
> cohomology of a quasi-coherent `𝒪_X`-module vanishes in every degree at least `t`.

```lean
theorem isZero_cohomology_of_finite_affine_cover (X : Scheme.{u})
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    {t : ℕ} (U : Fin t → X.Opens) (hU : ∀ i, IsAffineOpen (U i))
    (hUcover : ⨆ i, U i = ⊤) (F : X.Modules) [F.IsQuasicoherent] (n : ℕ) (hn : t ≤ n) :
    IsZero (Hgroup X.ringCatSheaf (⊤ : X.Opens) n F)
```

**`Stacks.Cohomology.AffineCover.isZero_cohomologyPresheaf_of_affineCoveringNumber_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/Basic.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/Basic.lean#L197). The attribute's comment: “minimal-cover form”.

> If `X` is quasi-compact with affine diagonal — for example if `X` is
> separated — then the cohomology of a quasi-coherent `𝒪_X`-module vanishes in every degree at
> least the least number of affine opens needed to cover `X`.

```lean
theorem isZero_cohomologyPresheaf_of_affineCoveringNumber_le (X : Scheme.{u}) [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [HasExt.{w} (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u})]
    (F : X.Modules) [F.IsQuasicoherent] (n : ℕ)
    (hn : minimalAffineCoverCardinality (⊤ : X.Opens) ≤ n) :
    IsZero ((((SheafOfModules.toSheaf X.ringCatSheaf).obj F).cohomologyPresheaf n).obj
      (op (⊤ : X.Opens)))
```

**`AlgebraicGeometry.isZero_cohomology_of_affineCoverNum_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean#L220).

> **Stacks Project, Tag 01XI.** Let `X` be a quasi-compact scheme with affine diagonal — for
> instance a separated scheme — and let `t = t(X)` be the minimal number of affine opens needed to
> cover `X`. Then `H^p(X, F) = 0` for every `p ≥ t` and every quasi-coherent `𝒪_X`-module `F`.

```lean
theorem isZero_cohomology_of_affineCoverNum_le (X : Scheme.{u}) [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))] (F : X.Modules) [F.IsQuasicoherent]
    (p : ℕ) (hp : X.affineCoverNum ⊤ ≤ p) :
    IsZero (Hgroup X.ringCatSheaf ⊤ p F)
```

**`Stacks.Cohomology.FiniteCover.isZero_Hgroup_of_finite_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EulerCharVanishing/Basic.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EulerCharVanishing/Basic.lean#L197). The attribute's comment: “finite-cover form”.

> **[Stacks, Tag 01XI], finite-cover form.** On a scheme with affine diagonal covered by `t`
> affine opens, the cohomology of a quasi-coherent module vanishes in every degree at least `t`.
>
> This is the library-spelling counterpart of `isZero_H'_of_finite_affine_cover`. The tag's own
> phrasing bounds the degree by the
> *minimal* number of affine opens needed to cover the scheme; that follows from this by applying
> it to a cover realizing the minimum, and is not stated here because the affine covering number
> has no name in the library yet.

```lean
theorem isZero_Hgroup_of_finite_affine_cover
    [IsAffineHom (pullback.diagonal (terminal.from X))] (F : X.Modules) [F.IsQuasicoherent]
    {t : ℕ} (U : Fin t → X.Opens) (hU : ∀ i, IsAffineOpen (U i)) (W : X.Opens)
    (hcover : ⨆ i, U i = W) (n : ℕ) (hn : t ≤ n) :
    IsZero (Hgroup X.ringCatSheaf W n F)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.minimalAffineCoverCardinality`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/CoveringNumber.lean#L49), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/CoveringNumber.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/CoveringNumber.lean#L52) (StacksFrontier): “affine covering number”.

## Tag 0BDY, a lemma

[Tag 0BDY](https://stacks.math.columbia.edu/tag/0BDY) in the Stacks Project.

**`Stacks.Cohomology.QcohDelta.exists_mono_isZero_hfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/QcohUniversalDeltaFunctor.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/QcohUniversalDeltaFunctor.lean#L165). The attribute's comment: “part (1): the embedding with vanishing higher cohomology”.

> **Stacks 0BDY, part (1).** On a quasi-compact scheme with affine diagonal every
> quasi-coherent `𝒪_X`-module `ℱ` admits an embedding `ℱ → ℱ'` into a quasi-coherent module with
> `Hᵖ(X, ℱ') = 0` for all `p ≥ 1`.
>
> Take `ℱ' = ∏ᵢ (ιᵢ)_*(ℱ|_{Uᵢ})` for a finite affine open cover `X = ⋃ Uᵢ`: each `ιᵢ` is affine
> because the diagonal of `X` is, so `ℱ'` is quasi-coherent and its cohomology is the product of
> the cohomologies of the `ℱ|_{Uᵢ}` on the affine schemes `Uᵢ`, which vanish in positive
> degrees.

```lean
theorem exists_mono_isZero_hfunctor (X : Scheme.{u}) [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    ∃ (G : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) (φ : F ⟶ G),
      Mono ((ObjectProperty.ι (SheafOfModules.isQuasicoherent X.ringCatSheaf)).map φ) ∧
        ∀ p : ℕ, 0 < p → IsZero ((Hfunctor X.ringCatSheaf ⊤ p).obj G.obj)
```

**`Stacks.Cohomology.QcohDelta.cohomologyDeltaFunctor_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/QcohUniversalDeltaFunctor.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/QcohUniversalDeltaFunctor.lean#L235). The attribute's comment: “part (2): universality of the delta-functor”.

> **Stacks 0BDY, part (2).** On a quasi-compact scheme with affine diagonal the cohomology
> functors `{Hⁿ(X, -)}_{n ≥ 0}` form a *universal* δ-functor from `QCoh(𝒪_X)` to `Ab`.
>
> Part (1) effaces every positive-degree component, and an effaceable δ-functor is universal.

```lean
theorem cohomologyDeltaFunctor_isUniversal [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))] :
    (cohomologyDeltaFunctor X).IsUniversal
```

## Tag 071L, a lemma

[Tag 071L](https://stacks.math.columbia.edu/tag/071L) in the Stacks Project.

**`Stacks.Cohomology.AffineCover.isZero_cohomology_of_degree_ge_separatedCoverBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/SeparatedCover.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineCoverVanishing/SeparatedCover.lean#L271).

> Let `X` be a quasi-compact quasi-separated scheme and let
> `X = U₁ ∪ … ∪ Uₙ` be an open covering by quasi-compact separated opens — for example affine ones.
> If `d = max_{I} (|I| + t(⋂_{i ∈ I} Uᵢ) - 1)`, where `t` is the affine covering number, then the
> cohomology of every quasi-coherent `𝒪_X`-module vanishes in every degree at least `d`.

```lean
theorem isZero_cohomology_of_degree_ge_separatedCoverBound {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X]
    [HasExt.{w} (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u})]
    {n d : ℕ} (U : Fin n → X.Opens) (hU : ⨆ i, U i = ⊤)
    (hU_compact : ∀ i, IsCompact (U i : Set X))
    (hU_separated : ∀ i, Scheme.IsSeparated (U i : Scheme))
    (hd : d = Finset.univ.sup fun I : Finset (Fin n) ↦
      I.card + minimalAffineCoverCardinality (⨅ i ∈ I, U i) - 1)
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) (hp : d ≤ p) :
    IsZero ((((SheafOfModules.toSheaf X.ringCatSheaf).obj F).cohomologyPresheaf p).obj
      (op (⊤ : X.Opens)))
```

**`AlgebraicGeometry.isZero_cohomology_of_coverDegreeBound_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean#L290).

> **Stacks Project, Tag 071L.** Let `X` be a quasi-compact quasi-separated scheme and let
> `X = U 1 ∪ … ∪ U n` be an open covering with each `U i` quasi-compact and with affine
> diagonal — for instance separated, or affine. Set
>
> `d = max { |I| + t(⋂_{i ∈ I} U i) - 1 : ∅ ≠ I ⊆ {1, …, n} }`,
>
> the `AlgebraicGeometry.Scheme.coverDegreeBound` of the covering, where `t(U)` is the minimal
> number of affine opens needed to cover `U`. Then `H^p(X, F) = 0` for all `p ≥ d` and every
> quasi-coherent `𝒪_X`-module `F`.

```lean
theorem isZero_cohomology_of_coverDegreeBound_le [CompactSpace X] [QuasiSeparatedSpace X]
    (F : X.Modules) [F.IsQuasicoherent] {n : ℕ} (U : Fin n → X.Opens) (hcov : ⨆ i, U i = ⊤)
    (hUc : ∀ i, IsCompact (U i : Set X))
    (hUinf : ∀ (i : Fin n) (A B : X.Opens), A ≤ U i → B ≤ U i → IsAffineOpen A →
      IsAffineOpen B → IsAffineOpen (A ⊓ B))
    (p : ℕ) (hp : X.coverDegreeBound U ≤ p) :
    IsZero (Hgroup X.ringCatSheaf ⊤ p F)
```

**`AlgebraicGeometry.isZero_cohomology_of_coverDegreeBound_le_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/UniformVanishing/Basic.lean#L303).

> **Stacks Project, Tag 071L**, with the covering hypothesis in the source's form: each `U i`
> is quasi-compact and separated.

```lean
theorem isZero_cohomology_of_coverDegreeBound_le_of_isSeparated [CompactSpace X]
    [QuasiSeparatedSpace X] (F : X.Modules) [F.IsQuasicoherent] {n : ℕ} (U : Fin n → X.Opens)
    (hcov : ⨆ i, U i = ⊤) (hUc : ∀ i, IsCompact (U i : Set X))
    (hUsep : ∀ i, (U i).toScheme.IsSeparated)
    (p : ℕ) (hp : X.coverDegreeBound U ≤ p) :
    IsZero (Hgroup X.ringCatSheaf ⊤ p F)
```

## Tag 01XJ, a lemma

[Tag 01XJ](https://stacks.math.columbia.edu/tag/01XJ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.isQuasicoherent_higherDirectImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/Qcqs.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/Qcqs.lean#L485). The attribute's comment: “quasicoherence”. References: EGA III (1.4.10), “more general”.

> **Stacks Project, Tag 01XJ (quasicoherence).** The higher direct images of a
> quasi-coherent module under a quasi-compact and quasi-separated morphism of schemes are
> quasi-coherent.

```lean
instance isQuasicoherent_higherDirectImage {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] (F : X.Modules) [F.IsQuasicoherent] (p : ℤ) :
    (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.exists_isZero_rightDerived_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean#L439). The attribute's comment: “uniform\_vanishing”.

> For a quasi-compact and quasi-separated morphism of schemes whose target is quasi-compact
> there is an integer, depending on the morphism alone, above which every higher direct image of
> every quasi-coherent module vanishes.

```lean
theorem exists_isZero_rightDerived_pushforward {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] :
    ∃ n : ℤ, ∀ p : ℤ, n ≤ p → ∀ (F : X.Modules) [F.IsQuasicoherent],
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F)
```

**`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.exists_isZero_rightDerivedNat_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean#L562). The attribute's comment: “uniform\_vanishing”. References: EGA IV (1.7.21), “vanishing bound”; EGA III (1.4.12), “existence of r”.

> For a quasi-compact and quasi-separated morphism of schemes whose target is quasi-compact
> there is a natural number, depending on the morphism alone, above which `(Rⁿ f_*) F` vanishes for
> every quasi-coherent module `F`, where `Rⁿ f_*` is Mathlib's `ℕ`-indexed
> `CategoryTheory.Functor.rightDerived (Scheme.Modules.pushforward f) n`.

```lean
theorem exists_isZero_rightDerivedNat_pushforward {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] :
    ∃ N : ℕ, ∀ F : X.Modules, F.IsQuasicoherent → ∀ n : ℕ, N ≤ n →
      IsZero (((Scheme.Modules.pushforward f).rightDerived n).obj F)
```

**`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.exists_isZero_rightDerivedPlus_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HigherDirectImageQcqs/UniformVanishing.lean#L586). The attribute's comment: “uniform\_vanishing”.

> For a quasi-compact and quasi-separated morphism of schemes whose target is quasi-compact
> there is an integer, depending on the morphism alone, above which every higher direct image of
> every quasi-coherent module vanishes, for the `ℤ`-indexed right derived functors at an arbitrary
> model of the bounded below derived category.

```lean
theorem exists_isZero_rightDerivedPlus_pushforward {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S]
    [HasDerivedCategory.{w} X.Modules] [HasDerivedCategory.{w'} S.Modules] :
    ∃ N : ℤ, ∀ p : ℤ, N ≤ p → ∀ F : X.Modules, F.IsQuasicoherent →
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F)
```

**`Stacks.AlgebraicGeometry.Tag01XJQcohInduction.higherDirectImage_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohInduction/Basic.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QcohInduction/Basic.lean#L332). The attribute's comment: “quasicoherence”. References: EGA III (6.2.3), “special case”.

> **Stacks Project, Tag 01XJ (quasicoherence).** The higher direct images of a quasi-coherent
> module under a quasi-compact and quasi-separated morphism of schemes are quasi-coherent.
>
> Quasi-coherence is local on the base
> (`Stacks.AlgebraicGeometry.HigherDirectImageQcoh.isQuasicoherent_rightDerivedPlus_of_affineOpens`,
> which is [Stacks, Tag 01E5] for schemes), and `f ∣_ V` is again quasi-compact and quasi-separated
> with affine target, so the statement reduces to
> `isQuasicoherent_rightDerivedPlus_of_isAffine`.

```lean
instance higherDirectImage_isQuasicoherent (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] (p : ℤ) :
    (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F).IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.Tag01XJUniformVanishing.exists_isZero_rightDerived_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/UniformVanishing/Basic.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/UniformVanishing/Basic.lean#L383). The attribute's comment: “uniform\_vanishing”. References: EGA IV (1.7.21), “vanishing bound”; EGA III (1.4.12), “existence of r”.

> **Stacks Project, Tag 01XJ (uniform\_vanishing).** Let `f : X ⟶ S` be a quasi-compact and
> quasi-separated morphism of schemes with `S` quasi-compact.  Then there is an integer `n`,
> depending only on `f`, such that `R ᵖ f_* F = 0` for every `p ≥ n` and every quasi-coherent
> `𝒪_X`-module `F`.
>
> `S` is covered by finitely many affine opens `B j` (`exists_fin_affineOpen_cover`), each
> `f ∣_ B j` is again quasi-compact and quasi-separated with affine target, so
> `exists_isZero_rightDerived_pushforward_of_isAffine` supplies a bound `n j`; the bound is
> `⨆ j, (n j).toNat`.  Above it every restriction of `R ᵖ f_* F` to a `B j` vanishes — by
> [Stacks, Tag 01E5] for schemes, `higherDirectImageRestrictObjIso` — and vanishing is local,
> `isZero_of_isZero_restrict`.

```lean
theorem exists_isZero_rightDerived_pushforward (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    [CompactSpace S] :
    ∃ n : ℤ, ∀ (p : ℤ), n ≤ p → ∀ (F : X.Modules) [F.IsQuasicoherent],
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F)
```

**`AlgebraicGeometry.exists_uniform_isZero_rightDerived_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/UniformVanishingDirectImage/Basic.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/UniformVanishingDirectImage/Basic.lean#L243). The attribute's comment: “base\_change\_uniform\_vanishing”. References: EGA IV (1.7.21), “base change vanishing”; EGA III (1.4.12), “existence of r”.

> **Stacks Project, Tag 01XJ (3).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes with `S` quasi-compact. There is an integer `n = n(X, S, f)` such that for
> every morphism `g : S' ⟶ S` the base change `f' : X' = X ×_S S' ⟶ S'` satisfies
> `R ᵖ f'_* F' = 0` for every `p ≥ n` and every quasi-coherent module `F'` on `X'`.

```lean
theorem exists_uniform_isZero_rightDerived_pushforward {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] :
    ∃ n : ℤ, ∀ (S' : Scheme.{u}) (g : S' ⟶ S) (F : (pullback f g).Modules) [F.IsQuasicoherent],
      ∀ p : ℤ, n ≤ p →
        IsZero (((Scheme.Modules.pushforward (pullback.snd f g)).rightDerivedPlus p).obj F)
```

## Tag 01XK, a lemma

[Tag 01XK](https://stacks.math.columbia.edu/tag/01XK) in the Stacks Project.

**`Stacks.Cohomology.AffineBase.cohomologyIsoGlobalSectionsRightDerivedPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/AffineBase.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/AffineBase.lean#L262). References: EGA III (1.4.14), “affine base, Z=point”.

> **[Stacks, Tag 01XK].** For a quasi-compact and quasi-separated morphism `f : X ⟶ S` with
> affine target, the cohomology of a quasi-coherent module on `X` is naturally isomorphic, as a
> module over `Γ(S, ⊤)`, to the global sections of its higher direct image.

```lean
public noncomputable def cohomologyIsoGlobalSectionsRightDerivedPushforward (q : ℤ) :
    (SheafOfModules.isQuasicoherent X.ringCatSheaf).ι ⋙
        (moduleGlobalSections X).rightDerivedPlus q ⋙
        ModuleCat.restrictScalars f.appTop.hom ≅
      (SheafOfModules.isQuasicoherent X.ringCatSheaf).ι ⋙
        (AlgebraicGeometry.Scheme.Modules.pushforward f).rightDerivedPlus q ⋙
        moduleGlobalSections S
```

**`Stacks.Cohomology.AffineBase.cohomologyIsoSectionsRightDerivedPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineBase.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/AffineBase.lean#L149). References: EGA III (1.4.14), “affine base, Z=point”.

> Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of
> schemes with `S` affine. For every `q : ℤ` the cohomology `H^q(X, F)` of a quasi-coherent
> `𝒪_X`-module `F`, regarded as a `Γ(S, 𝒪_S)`-module by restriction of scalars along
> `f^\# : Γ(S, 𝒪_S) ⟶ Γ(X, 𝒪_X)`, is the module of global sections of the higher direct image
> `R^qf_*F`, naturally in `F`.

```lean
def cohomologyIsoSectionsRightDerivedPushforward (q : ℤ) :
    quasicoherentInclusion X ⋙
        (sectionsFunctor X ⊤).rightDerivedPlus q ⋙ ModuleCat.restrictScalars f.appTop.hom ≅
      quasicoherentInclusion X ⋙
        (Scheme.Modules.pushforward f).rightDerivedPlus q ⋙ sectionsFunctor S ⊤
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.4, Tag 01XH](https://stacks.math.columbia.edu/tag/01XH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
