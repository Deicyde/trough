---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.pulledBackCover_isFinite, Stacks.FundamentalGroup.pulledBackCover_etale, Stacks.FundamentalGroup.pulledBackCover_isUnramifiedInCodimensionOne, Stacks.FundamentalGroup.pulledBackCover_isTamelyRamifiedInCodimensionOne, AlgebraicGeometry.exists_finiteEtale_of_isUnramifiedInCodimensionOne, AlgebraicGeometry.exists_finiteEtale_extension_of_isUnramifiedInCodimensionOne, AlgebraicGeometry.exists_finiteEtale_extension_of_isEffectiveCartierDivisor, AlgebraicGeometry.standardTamelyRamifiedAlgebra
statement: formalized
proof: formalized
---

# 58.31 Tame ramification

Section 58.31 of the Stacks Project, [Tag 0BSE](https://stacks.math.columbia.edu/tag/0BSE). 9 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EYD, a lemma

[Tag 0EYD](https://stacks.math.columbia.edu/tag/0EYD) in the Stacks Project.

**`Stacks.FundamentalGroup.pulledBackCover_isFinite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullback.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullback.lean#L207). The attribute's comment: “finite\_etale\_pullback”.

> The canonical pullback of the cover is finite.

```lean
public instance pulledBackCover_isFinite
    (D : CodimensionOnePullbackSetup.{u}) :
    IsFinite D.pulledBackCover
```

**`Stacks.FundamentalGroup.pulledBackCover_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullback.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullback.lean#L216). The attribute's comment: “finite\_etale\_pullback”.

> The canonical pullback of the cover is étale.

```lean
public instance pulledBackCover_etale
    (D : CodimensionOnePullbackSetup.{u}) :
    Etale D.pulledBackCover
```

**`Stacks.FundamentalGroup.pulledBackCover_isUnramifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullbackRamification.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullbackRamification.lean#L511). The attribute's comment: “unramified\_in\_codimension\_one”.

> **Stacks 0EYD**, unramified half. If the cover `Y → U` is unramified over `X` in
> codimension one, then the pulled-back cover is unramified over `X'` in codimension one.

```lean
public theorem pulledBackCover_isUnramifiedInCodimensionOne
    (D : CodimensionOnePullbackSetup.{u})
    (h : IsUnramifiedInCodimensionOne D.U.ι D.f) :
    IsUnramifiedInCodimensionOne (pullback.fst D.g D.U.ι) D.pulledBackCover
```

**`Stacks.FundamentalGroup.pulledBackCover_isTamelyRamifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullbackRamification.lean, line 533](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/CodimensionOnePullbackRamification.lean#L533). The attribute's comment: “tamely\_ramified\_in\_codimension\_one”. References: SGA 1 XIII (2.0.2), “partial”; SGA 1 XIII (2.0.3), “more general”.

> **Stacks 0EYD**, tamely ramified half. If the cover `Y → U` is tamely ramified over `X` in
> codimension one, then the pulled-back cover is tamely ramified over `X'` in codimension one.

```lean
public theorem pulledBackCover_isTamelyRamifiedInCodimensionOne
    (D : CodimensionOnePullbackSetup.{u})
    (h : IsTamelyRamifiedInCodimensionOne D.U.ι D.f) :
    IsTamelyRamifiedInCodimensionOne (pullback.fst D.g D.U.ι) D.pulledBackCover
```

## Tag 0H2W, a lemma

[Tag 0H2W](https://stacks.math.columbia.edu/tag/0H2W) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_of_isUnramifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendUnramifiedCodimensionOne.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendUnramifiedCodimensionOne.lean#L140). The attribute's comment: “extension across a regular complement, with the two inputs carried”.

> **Stacks Project, Tag 0H2W.** Let `X` be a locally Noetherian scheme, `U ⊆ X` a dense open
> and `f : Y ⟶ U` finite étale. If `Y` is unramified over `X` in codimension one and `𝒪_{X, x}` is
> regular for every `x` outside `U`, then `f` is the restriction of a finite étale cover of `X`.

```lean
public theorem exists_finiteEtale_of_isUnramifiedInCodimensionOne
    (hExtend : ExtendsAcrossCodimensionOneBoundary.{u})
    (hPurity : PurityAtRegularLocalRings.{u})
    {X : Scheme.{u}} [IsLocallyNoetherian X] (U : X.Opens) (hdense : DenseRange U.ι.base)
    (hEssSurj : ∀ V : X.Opens, (∀ x : X, x ∉ V → HasPurity (X.presheaf.stalk x)) →
      (finiteEtaleBaseChange V.ι).EssSurj)
    {Y : Scheme.{u}} (f : Y ⟶ U) [IsFinite f] [Etale f]
    (hunr : Stacks.FundamentalGroup.IsUnramifiedInCodimensionOne U.ι f)
    (hreg : ∀ x : X, x ∉ U → IsRegularLocalRing (X.presheaf.stalk x)) :
    ∃ (Y' : Scheme.{u}) (p : Y' ⟶ X), IsFinite p ∧ Etale p ∧
      ∃ e : pullback p U.ι ≅ Y, e.hom ≫ f = pullback.snd p U.ι
```

**`AlgebraicGeometry.exists_finiteEtale_extension_of_isUnramifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendUnramifiedRegularBoundary.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendUnramifiedRegularBoundary.lean#L183). The attribute's comment: “a finite étale cover unramified in codimension one extends across a regular complement”. References: SGA 1 X (3.3), “partial”; SGA 2 XIV (1.11), “Regular case”.

> **Stacks Project, Tag 0H2W.** Let `X` be a locally Noetherian scheme, `U ⊆ X` a dense open
> and `f : Y ⟶ U` finite étale. If `Y` is unramified over `X` in codimension one and `𝒪_{X, x}` is
> regular for every `x` outside `U`, then `f` is the restriction of a finite étale cover of `X`:
> there is a finite étale `p : Y' ⟶ X` and an isomorphism `Y' ×_X U ≅ Y` over `U`.

```lean
public theorem exists_finiteEtale_extension_of_isUnramifiedInCodimensionOne
    {X : Scheme.{u}} [IsLocallyNoetherian X] (U : X.Opens) (hdense : DenseRange U.ι.base)
    {Y : Scheme.{u}} (f : Y ⟶ U) [IsFinite f] [Etale f]
    (hunr : Stacks.FundamentalGroup.IsUnramifiedInCodimensionOne U.ι f)
    (hreg : ∀ x : X, x ∉ U → IsRegularLocalRing (X.presheaf.stalk x)) :
    ∃ (Y' : Scheme.{u}) (p : Y' ⟶ X), IsFinite p ∧ Etale p ∧
      ∃ e : pullback p U.ι ≅ Y, e.hom ≫ f = pullback.snd p U.ι
```

## Tag 0EYE, a lemma

[Tag 0EYE](https://stacks.math.columbia.edu/tag/0EYE) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_extension_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendAcrossRegularDivisor.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityBranchLocus/ExtendAcrossRegularDivisor.lean#L67). The attribute's comment: “a finite étale cover of `X ∖ D` unramified in codimension one extends across a regular effective Cartier divisor `D`; the special case `U = X ∖ D` of Tag 0H2W”. References: SGA 7 II (2.3.1), “Extension clause”.

> **Stacks Project, Tag 0EYE.** Let `X` be a locally Noetherian scheme and let `D ⊆ X` be an
> effective Cartier divisor such that `D` is a regular scheme. Let `f : Y ⟶ X ∖ D` be a finite
> étale morphism. If `Y` is unramified over `X` in codimension one, then there exists a finite étale
> morphism `p : Y' ⟶ X` whose restriction to `X ∖ D` is `Y`: an isomorphism
> `Y' ×_X (X ∖ D) ≅ Y` over `X ∖ D`.
>
> Here `D` is the closed subscheme `D.subscheme` cut out by the ideal sheaf `D`, and `X ∖ D` is the
> open subscheme `D.support.compl`.

```lean
public theorem exists_finiteEtale_extension_of_isEffectiveCartierDivisor
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (hDreg : IsRegular D.subscheme)
    {Y : Scheme.{u}} (f : Y ⟶ D.support.compl) [IsFinite f] [Etale f]
    (hunr : Stacks.FundamentalGroup.IsUnramifiedInCodimensionOne
      (Scheme.Opens.ι D.support.compl) f) :
    ∃ (Y' : Scheme.{u}) (p : Y' ⟶ X), IsFinite p ∧ Etale p ∧
      ∃ e : pullback p (Scheme.Opens.ι D.support.compl) ≅ Y,
        e.hom ≫ f = pullback.snd p (Scheme.Opens.ι D.support.compl)
```

## Tag 0EYF, an example

[Tag 0EYF](https://stacks.math.columbia.edu/tag/0EYF) in the Stacks Project.

**`AlgebraicGeometry.standardTamelyRamifiedAlgebra`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L64). The attribute's comment: “standard\_tamely\_ramified\_morphism”.

> The standard tamely ramified algebra `A[X] / (X ^ e - f)`.

```lean
public abbrev standardTamelyRamifiedAlgebra (A : Type u) [CommRing A] (f : A) (e : ℕ)
```

**`AlgebraicGeometry.standardTamelyRamifiedMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L69). The attribute's comment: “standard\_tamely\_ramified\_morphism”.

> The canonical morphism `Spec(A[X] / (X ^ e - f)) ⟶ Spec(A)`.

```lean
public noncomputable abbrev standardTamelyRamifiedMorphism
    (A : Type u) [CommRing A] (f : A) (e : ℕ) :
    Scheme.Spec.obj (Opposite.op (CommRingCat.of (standardTamelyRamifiedAlgebra A f e))) ⟶
      Scheme.Spec.obj (Opposite.op (CommRingCat.of A))
```

**`AlgebraicGeometry.standardTamelyRamifiedCover`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L79). The attribute's comment: “standard\_tamely\_ramified\_morphism”.

> The associated cover, obtained by restricting the standard morphism over
> `Spec(A_f)`.

```lean
public noncomputable abbrev standardTamelyRamifiedCover
    (A : Type u) [CommRing A] (f : A) (e : ℕ) :
    Scheme.Spec.obj (Opposite.op (CommRingCat.of
        (Localization.Away (algebraMap A (standardTamelyRamifiedAlgebra A f e) f)))) ⟶
      Scheme.Spec.obj (Opposite.op (CommRingCat.of (Localization.Away f)))
```

**`AlgebraicGeometry.standardTamelyRamifiedCover_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L91). The attribute's comment: “standard\_cover\_etale\_away”. References: SGA 1 XIII (5.1), “r = 1, étale part”.

> Away from `f`, the standard cover defined by `X ^ e = f` is étale when
> `e` is a unit in the base ring.

```lean
public theorem standardTamelyRamifiedCover_etale
    (A : Type u) [CommRing A] (f : A) (e : ℕ) [NeZero e]
    (he : IsUnit (e : A)) :
    Etale (standardTamelyRamifiedCover A f e)
```

**`AlgebraicGeometry.standardTamelyRamifiedMorphism_finiteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L181). The attribute's comment: “standard\_morphism\_finite\_locally\_free”. References: SGA 1 XIII (5.1), “r = 1, finite part”.

> The standard morphism `Spec(A[X] / (X ^ e - f)) ⟶ Spec(A)` is finite locally free: it is
> finite, flat and locally of finite presentation. In fact `A[X] / (X ^ e - f)` is free of rank
> `e` over `A` (`standardTamelyRamifiedAlgebra_free`,
> `standardTamelyRamifiedAlgebra_finrank`), so the morphism is even finite free.

```lean
public theorem standardTamelyRamifiedMorphism_finiteLocallyFree
    (A : Type u) [CommRing A] (f : A) (e : ℕ) [NeZero e] :
    IsFinite (standardTamelyRamifiedMorphism A f e) ∧
      Flat (standardTamelyRamifiedMorphism A f e) ∧
      LocallyOfFinitePresentation (standardTamelyRamifiedMorphism A f e)
```

**`AlgebraicGeometry.standardTamelyRamifiedCover_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/Basic.lean#L210). The attribute's comment: “the restriction of the standard morphism over Spec(A\_f), that is the standard cover, is finite”.

> **Stacks 0EYF, finiteness of the standard cover.** The restriction
> `Spec(C_f) ⟶ Spec(A_f)` of the standard morphism over `Spec(A_f)` is finite. The ring `C_f` is
> the localization of `C = A[X] / (X ^ e - f)` at the image of `f`, so it is a finite module over
> `A_f` because `C` is a finite `A`-module (`standardTamelyRamifiedAlgebra_finite`); finiteness of
> a ring map is preserved by localizing source and target at the same element. Together with
> `standardTamelyRamifiedCover_etale` this is the assertion of the tag that
> `Spec(C_f) ⟶ Spec(A_f)` is a *finite* étale morphism. As for étaleness, the Noetherian,
> nonzerodivisor, reducedness and invertibility hypotheses of the tag are not needed away from
> `f` and are omitted; only positivity of `e`, expressed by `NeZero e`, is used.

```lean
public theorem standardTamelyRamifiedCover_isFinite
    (A : Type u) [CommRing A] (f : A) (e : ℕ) [NeZero e] :
    IsFinite (standardTamelyRamifiedCover A f e)
```

**`AlgebraicGeometry.isDiscreteValuationRing_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L177). The attribute's comment: “the hypotheses on the base imply that A\_p is a DVR with uniformizer f, for every minimal prime p over f”.

> **Tag 0EYF, the base of the standard tamely ramified morphism.** Let `A` be a Noetherian
> ring, let `f : A` be a nonzerodivisor such that `A / fA` is reduced, and let `p` be a minimal
> prime over `f`. Then the localization `A_p` is a discrete valuation ring and `f` is a
> uniformizer of it. This is the implication asserted in the first sentences of the tag; it is
> what licenses the discrete valuation ring hypotheses in the tameness statements below.

```lean
public theorem isDiscreteValuationRing_of_mem_minimalPrimes [IsNoetherianRing A] {f : A}
    (hf : f ∈ nonZeroDivisors A) (hred : _root_.IsReduced (A ⧸ Ideal.span ({f} : Set A)))
    {p : Ideal A} [p.IsPrime] (hp : p ∈ (Ideal.span ({f} : Set A)).minimalPrimes)
    (S : Type v) [CommRing S] [Algebra A S] [IsLocalization.AtPrime S p] :
    ∃ _ : IsDomain S, IsDiscreteValuationRing S ∧ Irreducible (algebraMap A S f)
```

**`AlgebraicGeometry.standardTamelyRamifiedGenericFibreEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L255). The attribute's comment: “standard\_cover\_generic\_fibre”.

> **The generic fibre of the standard morphism is the Kummer extension.** Base changing
> `C = A[X] / (X ^ e - f)` along `A → K` gives `K[X] / (X ^ e - f)`, i.e. the Kummer algebra
> `K[f ^ (1 / e)]` of Tag 09EV.

```lean
public def standardTamelyRamifiedGenericFibreEquiv :
    K ⊗[A] standardTamelyRamifiedAlgebra A f e ≃ₐ[K] K1 K f e
```

**`AlgebraicGeometry.standardTamelyRamifiedGenericFibre_isTamelyRamified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L272). The attribute's comment: “the generic fibre of the standard cover at a codimension-one point is tamely ramified with respect to the local ring, for an exponent e ≥ 2”. References: SGA 1 XIII (5.1), “r = 1, tame part”.

> **Tag 0EYF, tameness in codimension one.** Let `A` be a discrete valuation ring with
> uniformizer `f`; this is the local ring of `Spec(A)` at the generic point of a prime divisor
> contained in the complement of `Spec(A_f)`. Let `K` be its fraction field and let `e ≥ 2` be
> invertible in `A`. The generic fibre of the standard morphism over that point is the field
> `K[f ^ (1 / e)] = K[X] / (X ^ e - f)` (`standardTamelyRamifiedGenericFibreEquiv`), and that
> field extension of `K` is tamely ramified with respect to `A`.

```lean
public theorem standardTamelyRamifiedGenericFibre_isTamelyRamified
    (hf : Irreducible f) (he : 2 ≤ e) (hinv : IsUnit (e : A)) :
    letI : Fact (Irreducible (kummerPoly K f e)) :=
      ⟨kummerPoly_irreducible K f e (by omega) hf⟩
    letI : Algebra.IsSeparable K (K1 K f e) :=
      isSeparable_K1 K f e he hf (ringChar_residue_coprime_of_isUnit (R := A) e hinv)
    IsDiscreteValuationRing.IsTamelyRamifiedWithRespectTo A K (K1 K f e)
```

**`AlgebraicGeometry.isTamelyRamified_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L307). The attribute's comment: “trivial\_extension\_tame”.

> **The trivial extension is tamely ramified.** `K / K` is tamely ramified with respect to
> the discrete valuation ring `A`.

```lean
public theorem isTamelyRamified_self :
    IsDiscreteValuationRing.IsTamelyRamifiedWithRespectTo A K K
```

**`AlgebraicGeometry.standardTamelyRamifiedGenericFibreEquivOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L322). The attribute's comment: “standard\_cover\_generic\_fibre\_one”.

> **Tag 0EYF, the exponent `e = 1`.** The generic fibre of the standard morphism for `e = 1`
> is `K` itself; combined with `isTamelyRamified_self` this is tameness in codimension one for
> the degenerate exponent.

```lean
public def standardTamelyRamifiedGenericFibreEquivOne :
    K ⊗[A] standardTamelyRamifiedAlgebra A f 1 ≃ₐ[K] K
```

**`AlgebraicGeometry.standardTamelyRamifiedGenericFibreFactor_isTamelyRamified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExample.lean#L390). The attribute's comment: “every field factor of the generic fibre of the standard cover at a codimension-one point is tamely ramified with respect to the local ring”.

> **Tag 0EYF, tameness in codimension one for every field factor.** Let `A` be a discrete
> valuation ring with uniformizer `f` — by `isDiscreteValuationRing_of_mem_minimalPrimes` this is
> the local ring of `Spec(A)` at the generic point of a prime divisor outside `Spec(A_f)` — let
> `K` be its fraction field, and let `e ≥ 1` be invertible in `A`. Then every field factor of the
> generic fibre `K ⊗[A] C` of the standard cover, that is, every field `L` receiving a surjection
> of `K`-algebras from it, is a finite separable extension of `K` which is tamely ramified with
> respect to `A`.

```lean
public theorem standardTamelyRamifiedGenericFibreFactor_isTamelyRamified
    (hf : Irreducible f) (he : 1 ≤ e) (hinv : IsUnit (e : A))
    (L : Type*) [Field L] [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    (φ : K ⊗[A] standardTamelyRamifiedAlgebra A f e →ₐ[K] L)
    (hφ : Function.Surjective φ) :
    ∃ (_ : Module.Finite K L) (_ : Algebra.IsSeparable K L),
      IsDiscreteValuationRing.IsTamelyRamifiedWithRespectTo A K L
```

**`AlgebraicGeometry.standardTamelyRamifiedCover_isTamelyRamifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExampleCodimensionOne.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameRamification/StandardExampleCodimensionOne.lean#L387). The attribute's comment: “standard\_cover\_tame\_codimension\_one”. References: SGA 1 XIII (5.1), “r = 1, codim 1 tame”.

> **Stacks 0EYF, tameness in codimension one.** Let `A` be a Noetherian ring, let `f : A` be a
> nonzerodivisor such that `A / fA` is reduced, and let `e ≥ 1` be invertible in `A`.  The finite
> étale cover `Spec(C_f) ⟶ Spec(A_f)` attached to `C = A[x] / (x ^ e - f)` is tamely ramified over
> `Spec(A)` in codimension one.

```lean
public theorem standardTamelyRamifiedCover_isTamelyRamifiedInCodimensionOne
    (A : Type u) [CommRing A] [IsNoetherianRing A] (f : A) (e : ℕ) [NeZero e]
    (hf : f ∈ nonZeroDivisors A)
    (hred : _root_.IsReduced (A ⧸ Ideal.span ({f} : Set A)))
    (hinv : IsUnit (e : A)) :
    Stacks.FundamentalGroup.IsTamelyRamifiedInCodimensionOne
      (standardTamelyRamifiedOpen A f) (standardTamelyRamifiedCover A f e)
```

## Tag 0EYG, a lemma

[Tag 0EYG](https://stacks.math.columbia.edu/tag/0EYG) in the Stacks Project.

**`AlgebraicGeometry.isEtaleLocallyStandardTamelyRamified_of_isTamelyRamifiedInCodimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/Abhyankar/RegularDivisorUnconditional.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/Abhyankar/RegularDivisorUnconditional.lean#L97). The attribute's comment: “Abhyankar's lemma for a regular divisor: a finite étale cover of `X ∖ D` tamely ramified in codimension one is étale locally on `X` a finite disjoint union of the standard tamely ramified covers of Example 0EYF”.

> **Abhyankar's lemma for a regular divisor, [Stacks, Tag 0EYG].** Let `X` be a locally
> Noetherian scheme and let `D ⊆ X` be an effective Cartier divisor such that `D` is a regular
> scheme. Let `f : Y ⟶ X ∖ D` be a finite étale morphism. If `Y` is tamely ramified over `X` in
> codimension one, then étale locally on `X` the morphism `Y ⟶ X` is a finite disjoint union of
> standard tamely ramified morphisms as described in [Stacks, Example 0EYF]: every `x ∈ X` lies in
> the image of an étale `Spec A ⟶ X` with `A` Noetherian, on which `X ∖ D` is `Spec A_φ` for a
> nonzerodivisor `φ` with `A / φA` reduced, and over which `Y` is
> `∐ᵢ Spec (A[x]/(x^{eᵢ} - φ))_φ` with each `eᵢ ≥ 1` invertible in `A`.
>
> Here `D` is the closed subscheme `D.subscheme` cut out by the ideal sheaf `D`, and `X ∖ D` is the
> open subscheme `D.support.compl`.

```lean
theorem isEtaleLocallyStandardTamelyRamified_of_isTamelyRamifiedInCodimensionOne
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (hDreg : IsRegular D.subscheme)
    {Y : Scheme.{u}} (f : Y ⟶ (D.support.compl : X.Opens)) [IsFinite f] [Etale f]
    (htame : IsTamelyRamifiedInCodimensionOne (Scheme.Opens.ι (D.support.compl : X.Opens)) f) :
    IsEtaleLocallyStandardTamelyRamified (D.support.compl : X.Opens) f
```

## Tag 0EYH, a lemma

[Tag 0EYH](https://stacks.math.columbia.edu/tag/0EYH) in the Stacks Project.

**`AlgebraicGeometry.TameCovers.normalization_of_isTamelyRamifiedInCodimensionOne_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/NormalizationAlongRegularDivisor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/NormalizationAlongRegularDivisor.lean#L68). The attribute's comment: “the normalization of `X` in a tame cover `Y` of `X ∖ D` is finite locally free, restricts to `Y`, has `π⁻¹(D)_red` a regular effective Cartier divisor, and is étale locally a finite disjoint union of standard `Spec(A[x]/(x^e - f)) ⟶ Spec(A)`”.

> **Stacks Project, Tag 0EYH.** Let `X` be a locally Noetherian scheme, let `D ⊆ X` be an
> effective Cartier divisor such that `D` is a regular scheme, and let `f : Y ⟶ X ∖ D` be finite
> étale and tamely ramified over `X` in codimension one (the situation of [Stacks, Tag 0EYG]).
> Then the normalization `π : Y' ⟶ X` of `X` in `Y` is a finite locally free morphism such that
> 1. the restriction of `Y'` to `X ∖ D` is isomorphic to `Y` (over `X ∖ D`),
> 2. `D' = π⁻¹(D)_red` is an effective Cartier divisor on `Y'`, and
> 3. `D'` is a regular scheme.
> Moreover, étale locally on `X` the morphism `Y' ⟶ X` is a finite disjoint union of morphisms
> `Spec(A[x]/(x^e - φ)) ⟶ Spec(A)` where `A` is a Noetherian ring, `φ ∈ A` is a nonzerodivisor
> with `A/φA` regular, and `e ≥ 1` is invertible in `A`: every `x ∈ X` is in the image of an
> étale `g : Spec A ⟶ X` over which `Y' ×_X Spec A ≅ ∐ᵢ Spec(A[x]/(x^{eᵢ} - φ))` over `Spec A`.
>
> Here `π` is `(f ≫ ι).fromNormalization` for the inclusion `ι` of `X ∖ D = D.support.compl`,
> and `D'` is the closed subscheme of the radical of the ideal sheaf `D.comap π`.

```lean
public theorem normalization_of_isTamelyRamifiedInCodimensionOne_of_isRegular {X : Scheme.{u}}
    [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (hDreg : IsRegular D.subscheme)
    {Y : Scheme.{u}} (f : Y ⟶ (D.support.compl : X.Opens)) [IsFinite f] [Etale f]
    (hf : Stacks.FundamentalGroup.IsTamelyRamifiedInCodimensionOne
      (Scheme.Opens.ι (D.support.compl : X.Opens)) f) :
    Stacks.Morphisms.IsFiniteLocallyFree
        (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization ∧
      (∃ e : pullback (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization
          (Scheme.Opens.ι (D.support.compl : X.Opens)) ≅ Y,
        e.hom ≫ f = pullback.snd _ _) ∧
      Stacks.Divisors.IsEffectiveCartierDivisor
        (D.comap (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization).radical ∧
      IsRegular (D.comap (f ≫ Scheme.Opens.ι
          (D.support.compl : X.Opens)).fromNormalization).radical.subscheme ∧
      ∀ x : X, ∃ (A : CommRingCat.{u}) (g : Spec A ⟶ X) (_ : Etale g) (a : Spec A)
        (_ : g a = x) (φ : A) (_ : IsNoetherianRing A) (_ : φ ∈ nonZeroDivisors A)
        (_ : IsRegularRing (A ⧸ Ideal.span {φ})) (n : ℕ) (e : Fin n → ℕ)
        (_ : ∀ i, 0 < e i ∧ IsUnit (e i : A)),
        ∃ ι : pullback (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization g ≅
            ∐ fun i ↦ Spec (.of (standardTamelyRamifiedAlgebra A φ (e i))),
          ι.hom ≫ Sigma.desc (fun i ↦ standardTamelyRamifiedMorphism A φ (e i)) =
            pullback.snd _ g
```

## Tag 0EYI, a lemma

[Tag 0EYI](https://stacks.math.columbia.edu/tag/0EYI) in the Stacks Project.

**`AlgebraicGeometry.TameCovers.exists_lift_etaleAt_fromNormalization_of_isTamelyRamified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/LiftDiscreteValuationRingPoints.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/LiftDiscreteValuationRingPoints.lean#L60). The attribute's comment: “(1): a lift of `t|_{Spec K}` to `Y` gives a lift `t'` of `t` to the normalization `Y'`, and `Y' ⟶ X` is étale along `t'(Spec R)`”.

> **Stacks Project, Tag 0EYI (1).** Let `X` be a locally Noetherian scheme, `D ⊆ X` an
> effective Cartier divisor such that `D` is a regular scheme, and `f : Y ⟶ X ∖ D` a finite étale
> morphism tamely ramified over `X` in codimension one (the situation of [Stacks, Tag 0EYG]). Let
> `π : Y' ⟶ X` be the normalization of `X` in `Y` ([Stacks, Tag 0EYH]). Let `R` be a discrete
> valuation ring with fraction field `K` and `t : Spec R ⟶ X` a morphism such that the scheme
> theoretic inverse image `t⁻¹D` is the reduced closed point of `Spec R`. If `t|_{Spec K}` lifts to
> a point `y : Spec K ⟶ Y`, then there is a lift `t' : Spec R ⟶ Y'` of `t` (extending `y`) such
> that `π` is étale along `t'(Spec R)`.
>
> Here `D` is the closed subscheme `D.subscheme` cut out by the ideal sheaf `D`, `X ∖ D` is the
> open subscheme `D.support.compl`, and `Y'` is the relative normalization of `Y ⟶ X`.

```lean
theorem exists_lift_etaleAt_fromNormalization_of_isTamelyRamified
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (hDreg : IsRegular D.subscheme)
    {Y : Scheme.{u}} (f : Y ⟶ (D.support.compl : X.Opens)) [IsFinite f] [Etale f]
    (hf : Stacks.FundamentalGroup.IsTamelyRamifiedInCodimensionOne
      (Scheme.Opens.ι (D.support.compl : X.Opens)) f)
    (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    (K : Type u) [Field K] [Algebra R K] [IsFractionRing R K]
    (t : Spec (.of R) ⟶ X)
    (ht : D.comap t = Scheme.IdealSheafData.vanishingIdeal
      ⟨({IsLocalRing.closedPoint R} : Set (Spec (.of R))),
        (PrimeSpectrum.isClosed_singleton_iff_isMaximal _).mpr
          (IsLocalRing.maximalIdeal.isMaximal R)⟩)
    (y : Spec (.of K) ⟶ Y)
    (hy : y ≫ f ≫ Scheme.Opens.ι (D.support.compl : X.Opens) =
      Spec.map (CommRingCat.ofHom (algebraMap R K)) ≫ t) :
    ∃ t' : Spec (.of R) ⟶ (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).normalization,
      t' ≫ (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization = t ∧
      Spec.map (CommRingCat.ofHom (algebraMap R K)) ≫ t' =
        y ≫ (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).toNormalization ∧
      ∀ r, EtaleAt (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization (t' r)
```

**`AlgebraicGeometry.TameCovers.exists_opens_etale_fromNormalization_of_isTamelyRamified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/LiftDiscreteValuationRingPoints.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TameCovers/LiftDiscreteValuationRingPoints.lean#L94). The attribute's comment: “(2): if `Spec K ×_X Y` is a disjoint union of copies of `Spec K`, the normalization `Y' ⟶ X` is finite étale over an open neighbourhood of `t(Spec R)`”.

> **Stacks Project, Tag 0EYI (2).** In the situation of Tag 0EYI (1) (`X` locally Noetherian,
> `D ⊆ X` an effective Cartier divisor which is a regular scheme, `f : Y ⟶ X ∖ D` finite étale and
> tamely ramified over `X` in codimension one, `π : Y' ⟶ X` the normalization of `X` in `Y`, `R` a
> discrete valuation ring with fraction field `K`, `t : Spec R ⟶ X` with `t⁻¹D` the reduced closed
> point of `Spec R`): if `Spec K ×_X Y` is isomorphic, over `Spec K`, to a disjoint union of copies
> of `Spec K`, then `π` is finite étale over an open neighbourhood `V` of `t(Spec R)`.

```lean
theorem exists_opens_etale_fromNormalization_of_isTamelyRamified
    {X : Scheme.{u}} [IsLocallyNoetherian X] (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (hDreg : IsRegular D.subscheme)
    {Y : Scheme.{u}} (f : Y ⟶ (D.support.compl : X.Opens)) [IsFinite f] [Etale f]
    (hf : Stacks.FundamentalGroup.IsTamelyRamifiedInCodimensionOne
      (Scheme.Opens.ι (D.support.compl : X.Opens)) f)
    (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    (K : Type u) [Field K] [Algebra R K] [IsFractionRing R K]
    (t : Spec (.of R) ⟶ X)
    (ht : D.comap t = Scheme.IdealSheafData.vanishingIdeal
      ⟨({IsLocalRing.closedPoint R} : Set (Spec (.of R))),
        (PrimeSpectrum.isClosed_singleton_iff_isMaximal _).mpr
          (IsLocalRing.maximalIdeal.isMaximal R)⟩)
    (J : Type u)
    (eJ : pullback (Spec.map (CommRingCat.ofHom (algebraMap R K)) ≫ t)
        (f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)) ≅ ∐ fun _ : J ↦ Spec (.of K))
    (heJ : eJ.hom ≫ Sigma.desc (fun _ ↦ 𝟙 _) = pullback.fst _ _) :
    ∃ V : X.Opens, (∀ r, t r ∈ V) ∧
      IsFinite ((f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization ∣_ V) ∧
      Etale ((f ≫ Scheme.Opens.ι (D.support.compl : X.Opens)).fromNormalization ∣_ V)
```

## Tag 0EYJ, a lemma

[Tag 0EYJ](https://stacks.math.columbia.edu/tag/0EYJ) in the Stacks Project.

**`AlgebraicGeometry.FiniteEtaleGaloisCover.exists_extension_of_genericFiber_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/Abhyankar/GaloisCoverNoetherianExtension.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/Abhyankar/GaloisCoverNoetherianExtension.lean#L51). The attribute's comment: “the full statement under the tag's hypotheses and nothing else: `S` integral (`IsIntegral S`), normal (`IsNormal S`) and Noetherian (`IsNoetherian S`); `f` smooth with geometrically connected fibres (`Smooth f`, `GeometricallyConnected f`); a section `σ` of `f` (`hσ`); a finite étale Galois cover `Z` of the generic fibre `X_η` with group `G`, `G` finite of order invertible on `S` (`hG`: a unit in every residue field); a `κ(η)`-rational point `z` of `Z` over `σ(η)` (`hz`). The conclusion is a finite étale Galois cover `Y` of `X` with group `G` and a `G`-equivariant isomorphism `Y ×_X X_η ≅ Z` over `X_η`.”.

> **Extending a Galois cover of the generic fibre.** Let `S` be an integral normal Noetherian
> scheme with generic point `η`, let `f : X ⟶ S` be a smooth morphism with geometrically connected
> fibres and let `σ : S ⟶ X` be a section of `f`. Let `Z ⟶ X_η` be a finite étale Galois cover
> with group `G` whose order is invertible on `S` (a unit in every residue field `κ(s)`), such that
> `Z` has a `κ(η)`-rational point `z` mapping to `σ(η)`. Then there is a finite étale Galois cover
> `Y ⟶ X` with group `G` whose restriction to `X_η` is `Z`: an isomorphism `Y ×_X X_η ≅ Z` over
> `X_η` compatible with the actions of `G`.

```lean
theorem exists_extension_of_genericFiber_of_isNoetherian
    {S X : Scheme.{u}} (f : X ⟶ S) [IsNoetherian S] [IsIntegral S] [IsNormal S]
    [Smooth f] [GeometricallyConnected f]
    (σ : S ⟶ X) (hσ : σ ≫ f = 𝟙 S)
    (G : Type v) [Group G] [Finite G]
    (hG : ∀ s : S, IsUnit (Nat.card G : S.residueField s))
    (Z : FiniteEtaleGaloisCover (f.fiber (genericPoint S)) G)
    (z : Spec (S.residueField (genericPoint S)) ⟶ Z.obj.left)
    (hz : z ≫ Z.obj.hom = genericFiberSection f σ hσ) :
    ∃ (Y : FiniteEtaleGaloisCover X G)
      (e : (finiteEtaleBaseChange (f.fiberι (genericPoint S))).obj Y.obj ≅ Z.obj),
      ∀ g : Gᵐᵒᵖ, (finiteEtaleBaseChange (f.fiberι (genericPoint S))).map (Y.action g).asIso.hom ≫
        e.hom = e.hom ≫ (Z.action g).asIso.hom
```

## Tag 0EZJ, a lemma

[Tag 0EZJ](https://stacks.math.columbia.edu/tag/0EZJ) in the Stacks Project.

**`AlgebraicGeometry.FiniteEtaleGaloisCover.exists_extending_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCoverLimits/ExtensionTheorem.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCoverLimits/ExtensionTheorem.lean#L55). The attribute's comment: “the full statement under the tag's hypotheses: S qcqs integral normal; f qcqs smooth with geometrically connected fibres and a section σ; Z a finite étale Galois cover of X\_η with group G of order invertible on S and a κ(η)-point over σ(η); the extension Y is G-equivariantly a Galois cover restricting to Z”.

> **Stacks Project, Tag 0EZJ.** Let `S` be a quasi-compact and quasi-separated integral normal
> scheme with generic point `η`, let `f : X ⟶ S` be a quasi-compact and quasi-separated smooth
> morphism with geometrically connected fibres and `σ` a section of `f`. Let `Z ⟶ X_η` be a finite
> étale Galois cover (Section 03SF) with group `G` of order invertible on `S` such that `Z` has a
> `κ(η)`-rational point `z` mapping to `σ(η)`. Then there is a finite étale Galois cover `Y ⟶ X`
> with group `G` whose restriction to `X_η` is `Z`: the restriction is isomorphic to `Z` by an
> isomorphism compatible with the two actions of `G`.
>
> The order of `G` is invertible on `S` when it is a unit in every residue field of `S`.

```lean
theorem exists_extending_genericFiber
    {S X : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsIntegral S] [IsNormal S]
    [QuasiCompact f] [QuasiSeparated f] [Smooth f] [GeometricallyConnected f]
    (σ : S ⟶ X) (hσ : σ ≫ f = 𝟙 S)
    (G : Type v) [Group G] [Finite G]
    (hG : ∀ s : S, IsUnit (Nat.card G : S.residueField s))
    (Z : FiniteEtaleGaloisCover (f.fiber (genericPoint S)) G)
    (z : Spec (S.residueField (genericPoint S)) ⟶ Z.obj.left)
    (hz : z ≫ Z.obj.hom = genericFiberSection f σ hσ) :
    ∃ (Y : FiniteEtaleGaloisCover X G)
      (e : (finiteEtaleBaseChange (f.fiberι (genericPoint S))).obj Y.obj ≅ Z.obj),
      ∀ g : Gᵐᵒᵖ, (finiteEtaleBaseChange (f.fiberι (genericPoint S))).map (Y.action g).asIso.hom ≫
        e.hom = e.hom ≫ (Z.action g).asIso.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.31, Tag 0BSE](https://stacks.math.columbia.edu/tag/0BSE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
