---
declaration: section
origin: cited
lean: Stacks.Algebraization.AlgebraizationSituation, Stacks.Algebraization.AlgebraizationSituation.X, Stacks.Algebraization.AlgebraizationSituation.Y, Stacks.Algebraization.AlgebraizationSituation.Z, Stacks.Algebraization.AlgebraizationSituation.U, Stacks.Algebraization.restrictedTildeSystem_isCoherentAdicSystem, Stacks.Algebraization.exists_finiteModuleModel, Stacks.Algebraization.completionFunctor
statement: formalized
proof: formalized
---

# 52.16 Algebraization of coherent formal modules, I

Section 52.16 of the Stacks Project, [Tag 0DXS](https://stacks.math.columbia.edu/tag/0DXS). 14 tags here are carried by 102 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EHC, a situation

[Tag 0EHC](https://stacks.math.columbia.edu/tag/0EHC) in the Stacks Project.

**`Stacks.Algebraization.AlgebraizationSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean#L59). The attribute's comment: “the ring and ideals”.

> **Stacks Project, Tag 0EHC (standing data).** A Noetherian ring with nested ideals
> `I ⊆ 𝔞`.

```lean
public structure AlgebraizationSituation
```

**`Stacks.Algebraization.AlgebraizationSituation.X`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean#L79). The attribute's comment: “the scheme X”.

> **Stacks Project, Tag 0EHC (`X`).** The affine scheme `X = Spec(A)`.

```lean
public abbrev X (S : AlgebraizationSituation) : Scheme
```

**`Stacks.Algebraization.AlgebraizationSituation.Y`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean#L83). The attribute's comment: “the closed subscheme Y”.

> **Stacks Project, Tag 0EHC (`Y`).** The closed subscheme `Y = V(I) = Spec(A/I)`.

```lean
public abbrev Y (S : AlgebraizationSituation) : Scheme
```

**`Stacks.Algebraization.AlgebraizationSituation.Z`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean#L87). The attribute's comment: “the closed subscheme Z”.

> **Stacks Project, Tag 0EHC (`Z`).** The closed subscheme `Z = V(𝔞) = Spec(A/𝔞)`.

```lean
public abbrev Z (S : AlgebraizationSituation) : Scheme
```

**`Stacks.Algebraization.AlgebraizationSituation.U`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationSituation.lean#L112). The attribute's comment: “the open complement U”.

> **Stacks Project, Tag 0EHC (`U`).** The open subset `U = X \ Z`, namely the complement of
> `V(𝔞)` in `Spec(A)`.

```lean
public def U (S : AlgebraizationSituation) : S.X.Opens
```

## Tag 0DXT, a lemma

[Tag 0DXT](https://stacks.math.columbia.edu/tag/0DXT) in the Stacks Project.

**`Stacks.Algebraization.restrictedTildeSystem_isCoherentAdicSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FiniteModuleModel.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/FiniteModuleModel.lean#L1012). The attribute's comment: “forward implication”.

> A finite module model gives a coherent adic system on the punctured
> spectrum.

```lean
public theorem restrictedTildeSystem_isCoherentAdicSystem
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} S.A) (hM : IsFiniteModuleModel S M) :
    Stacks.Coherent.IsCoherentAdicSystem (Stacks.Algebraization.idealOnOpen S)
      (restrictedTildeSystem S M)
```

**`Stacks.Algebraization.exists_finiteModuleModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FiniteModuleModel.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/FiniteModuleModel.lean#L1029). The attribute's comment: “converse”.

> Every coherent adic system on `U` has a finite module model, compatible
> with the whole inverse-system structure.

```lean
public theorem exists_finiteModuleModel
    (F : Stacks.Coherent.CoherentAdicSystems (Stacks.Algebraization.idealOnOpen S)) :
    ∃ M : ℕᵒᵖ ⥤ ModuleCat.{u} S.A,
      ∃ hM : IsFiniteModuleModel S M,
        Nonempty (coherentAdicSystemOfFiniteModuleModel S M hM ≅ F)
```

## Tag 0EIK, an equation

[Tag 0EIK](https://stacks.math.columbia.edu/tag/0EIK) in the Stacks Project.

**`Stacks.Algebraization.completionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean#L475). The attribute's comment: “the same completion functor on an open subscheme, at the restricted ideal”.

> Completion of a coherent sheaf along a quasi-coherent ideal, as a coherent adic inverse
> system.

```lean
public noncomputable def completionFunctor (X : Scheme.{u})
    [AlgebraicGeometry.IsLocallyNoetherian X] (I : X.IdealSheafData) :
    AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf ⥤
      Stacks.Coherent.CoherentAdicSystems I
```

## Tag 0EIL, a lemma

[Tag 0EIL](https://stacks.math.columbia.edu/tag/0EIL) in the Stacks Project.

**`Stacks.Algebraization.isRestrictionOfCompletion_of_extendsToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AffineExistence.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AffineExistence.lean#L250). The attribute's comment: “extendable implies restriction of a completion”.

> **Stacks 0EIL, condition (6) implies condition (5) when `A` is `I`-adically complete.**

```lean
public theorem isRestrictionOfCompletion_of_extendsToX (S : AlgebraizationSituation.{u})
    [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι))
    (h : ExtendsToX S F) : IsRestrictionOfCompletion S F
```

**`Stacks.Algebraization.isCompletion_iff_nearClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean#L225). The attribute's comment: “completion iff near the closed subscheme”.

> **Stacks 0EIL, conditions (2) and (3) are equivalent.** A coherent adic system on `U` is the
> completion of a coherent module on `U` exactly when it is the completion of a coherent module on
> some open neighbourhood of `U ∩ Y` in `U`.
>
> One direction takes the neighbourhood to be `U` itself. For the other, a coherent module on the
> neighbourhood `V` extends to `U`, and the two systems — the completion of the extension and the
> given one — are then isomorphic over `V`; every term of either is annihilated by a power of the
> ideal and so is supported inside `V`, and restriction to `V` is fully faithful on modules
> supported there, so the isomorphism over `V` comes from an isomorphism over `U`.

```lean
public theorem isCompletion_iff_nearClosed (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage F ↔
      IsCompletionNearClosed S F
```

**`Stacks.Algebraization.isCompletion_iff_ofRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean#L262). The attribute's comment: “completion iff completion of a restriction”.

> **Stacks 0EIL, conditions (2) and (4) are equivalent.** A coherent adic system on `U` is the
> completion of a coherent module on `U` exactly when it is the completion of one that extends to a
> coherent module on `X`.
>
> `X` is affine and Noetherian, so every coherent module on the open `U` is the restriction of a
> coherent module on `X`; the converse direction forgets the extension.

```lean
public theorem isCompletion_iff_ofRestriction (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage F ↔
      IsCompletionOfRestriction S F
```

**`Stacks.Algebraization.isCompletionOfRestriction_iff_isRestrictionOfCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean#L276). The attribute's comment: “the two restriction conditions agree”.

> **Stacks 0EIL, conditions (4) and (5) are equivalent.** Being the completion of a module
> restricted from `X` is the same as being the restriction of a completion on `X`, because
> completion commutes with restriction to an open.

```lean
public theorem isCompletionOfRestriction_iff_isRestrictionOfCompletion
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)) :
    IsCompletionOfRestriction S F ↔ IsRestrictionOfCompletion S F
```

**`Stacks.Algebraization.extendsToX_of_isRestrictionOfCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/Algebraization.lean#L291). The attribute's comment: “restriction of a completion extends to X”.

> **Stacks 0EIL, condition (5) implies condition (6).** A system that is the restriction of a
> completion on `X` extends to `X`: the completion itself is the extension.

```lean
public theorem extendsToX_of_isRestrictionOfCompletion (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι))
    (h : IsRestrictionOfCompletion S F) : ExtendsToX S F
```

## Tag 0EHE, an example

[Tag 0EHE](https://stacks.math.columbia.edu/tag/0EHE) in the Stacks Project.

**`Stacks.Algebraization.NonAlgebraizableExample.idealPowerQuotientIsoPushforwardPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean#L316). The attribute's comment: “L/I^n L is the direct image along Spec(A/t^n A) ∩ U → U of the pullback of L”.

> **Stacks Project, Tag 0EHE (the level comparison).** For a quasi-coherent `𝒪_U`-module `𝓛`
> the term `𝓛 / Iⁿ𝓛` is the direct image along `levelStructureMap k n` of the pullback of `𝓛`: the
> closed immersion `Spec(A/tⁿA) ∩ U ⟶ U` has kernel ideal sheaf `(I𝒪_U)ⁿ`
> (`ker_levelStructureMap`), which is exactly the hypothesis of [Stacks, Tag 0EL1].

```lean
public def idealPowerQuotientIsoPushforwardPullback (n : ℕ)
    (M : (situation k).U.toScheme.Modules) [M.IsQuasicoherent] :
    idealPowerQuotient (idealOnOpen (situation k)) n M ≅
      (Scheme.Modules.pushforward (levelStructureMap k n)).obj
        ((Scheme.Modules.pullback (levelStructureMap k n)).obj M)
```

**`Stacks.Algebraization.NonAlgebraizableExample.idealPowerQuotientIsoPushforwardPullbackOnOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean#L329). The attribute's comment: “L/I^n L is the direct image of the pullback of L restricted to a smaller open”.

> **Stacks Project, Tag 0EHE (the level comparison through an intermediate open).** The same
> identification, with the pullback taken in two steps through an open `V ⊆ U` that
> `levelStructureMap k n` factors through: `𝓛 / Iⁿ𝓛` is the direct image of the pullback of
> `𝓛|_V`.

```lean
public def idealPowerQuotientIsoPushforwardPullbackOnOpen (n : ℕ)
    (M : (situation k).U.toScheme.Modules) [M.IsQuasicoherent]
    (V : (situation k).U.toScheme.Opens) (f : (levelOpen k n).toScheme ⟶ V.toScheme)
    (hf : f ≫ V.ι = levelStructureMap k n) :
    idealPowerQuotient (idealOnOpen (situation k)) n M ≅
      (Scheme.Modules.pushforward (levelStructureMap k n)).obj
        ((Scheme.Modules.pullback f).obj ((Scheme.Modules.pullback V.ι).obj M))
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_isCompletionOfCoherent_levelCoherentAdicSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableAlgebraizing.lean#L376). The attribute's comment: “the family (L\_n) is not the completion of a coherent O\_U-module”.

> **Stacks Project, Tag 0EHE (the family is not algebraizable).** The object `(𝓛ₙ)` of
> `Coh(U, I𝒪_U)` is not the completion of any coherent `𝒪_U`-module, for every choice of the
> coefficients `aₘ` and the exponents `φ(m)`.
>
> This is the source's first proof. An algebraizing coherent module `𝓛` has invertible stalks along
> `U ∩ Y`, so it is invertible on an open `V` with `U ∩ Y ⊆ V ⊆ U`
> (`exists_isInvertibleModule_restrict_of_isInvertibleAdic_completionIso`); there it is trivial,
> `A = k[x,y][[t]]` being a unique factorization domain
> (`isTrivial_of_isInvertible_ambientOpen`); the level-two term of its completion is the direct
> image along the closed immersion of the punctured spectrum of `A/t²A` of the pullback of `𝓛|_V`
> (`idealPowerQuotientIsoPushforwardPullbackOnOpen`), hence of the structure sheaf, and direct
> image along a closed immersion is fully faithful, so `𝓛₂ ≅ 𝒪`; and
> `not_isTrivial_levelModule_two` forbids that.

```lean
public theorem not_isCompletionOfCoherent_levelCoherentAdicSystem (a : ℕ → PlaneRing k)
    (φ : ℕ → ℕ) :
    ¬ IsCompletionOfCoherent (idealOnOpen (situation k)) (levelCoherentAdicSystem k a φ)
```

**`Stacks.Algebraization.NonAlgebraizableExample.isLocalization_away_levelToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartLocalization.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartLocalization.lean#L74). The attribute's comment: “A\_r/t^n A\_r is the localization of A/t^n A away from the image of r”.

> **Stacks Project, Tag 0EHE (the chart rings).** The chart ring `A_r/t^nA_r` is the
> localization of the level ring `A/t^nA` away from the image of `r`, so it is the ring of sections
> of `O` on the basic open `D(r)` of `Spec(A/t^nA)`.

```lean
public theorem isLocalization_away_levelToChart (r : AmbientRing k) (n : ℕ) :
    letI : Algebra (levelRing k n) (chartRing k r n) := (levelToChart k r n).toAlgebra
    IsLocalization.Away (Ideal.Quotient.mk ((idealT k) ^ n) r) (chartRing k r n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.map_chartOpenEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean#L75). The attribute's comment: “restriction from D(r) to D(q) is A\_r/t^n A\_r -> A\_q/t^n A\_q”.

> **Restriction of chart functions along a divisibility.** On the sections of `𝒪` over the
> basic opens of `Spec(A/tⁿA)`, restriction from `D(r̄)` to the smaller `D(q̄)` is the map
> `A_r/tⁿA_r → A_q/tⁿA_q`.

```lean
public theorem map_chartOpenEquiv (r q : AmbientRing k) (hdvd : r ∣ q) (n : ℕ)
    (hle : chartOpen k q n ≤ chartOpen k r n) (v : chartRing k r n) :
    ((levelScheme k n).presheaf.map (homOfLE hle).op).hom (chartOpenEquiv k r n v) =
      chartOpenEquiv k q n (chartRestrict k r q hdvd n v)
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelChartRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean#L110). The attribute's comment: “A\_r/t^n A\_r is the ring of sections of O on the chart D(r)”.

> **Stacks Project, Tag 0EHE (a chart ring is the ring of sections on the chart).** The chart
> ring `A_r/tⁿA_r` is the ring of sections of `𝒪` on the chart `D(r̄)` of the punctured spectrum of
> `A/tⁿA`; compare `levelOverlapRingEquiv` for the overlap of the two charts.

```lean
public def levelChartRingEquiv (r : AmbientRing k) (n : ℕ)
    (hle : chartOpen k r n ≤ levelOpen k n) :
    chartRing k r n ≃+* Γ((levelOpen k n).toScheme, levelChart k r n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.map_levelChartRingEquiv_overlap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableChartSections.lean#L131). The attribute's comment: “restriction from a chart to the overlap is A\_r/t^n A\_r -> A\_xy/t^n A\_xy”.

> **Stacks Project, Tag 0EHE (restriction from a chart to the overlap).** Restriction of
> sections of `𝒪` from a chart of the punctured spectrum of `A/tⁿA` to the overlap of the two
> charts is the map `chartRestrict` of chart rings. This is the dictionary between the sheaf-level
> and the ring-level description of the glued module: a global section of `𝓛ₙ` is a pair of chart
> functions matched on the overlap, and this is what matching means.

```lean
public theorem map_levelChartRingEquiv_overlap (r : AmbientRing k) (n : ℕ)
    (hdvd : r ∣ xVar k * yVar k) (hle : chartOpen k r n ≤ levelOpen k n)
    (hq : chartOpen k (xVar k * yVar k) n ≤ chartOpen k r n)
    (h : levelOverlap k n ≤ levelChart k r n) (v : chartRing k r n) :
    ((levelOpen k n).toScheme.presheaf.map (homOfLE h).op).hom
        (levelChartRingEquiv k r n hle v) =
      levelOverlapRingEquiv k n (chartRestrict k r (xVar k * yVar k) hdvd n v)
```

**`Stacks.Algebraization.NonAlgebraizableExample.situation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L128). The attribute's comment: “the situation A = k[x,y][[t]], I = (t), 𝔞 = (x,y,t)”.

> **Stacks Project, Tag 0EHE (the situation).** The algebraization situation with
> `A = k[x,y][[t]]`, `I = (t)` and `𝔞 = (x,y,t)`.

```lean
public def situation : AlgebraizationSituation.{u}
```

**`Stacks.Algebraization.NonAlgebraizableExample.coe_U_inter_zeroLocus_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L151). The attribute's comment: “the open covering of U ∩ Y by D(x) and D(y)”.

> **Stacks Project, Tag 0EHE (the two-chart covering).** The punctured closed fibre
> `U ∩ Y` of the situation is covered by the two basic opens `D(x)` and `D(y)`. Each of
> `D(x) ∩ Y` and `D(y) ∩ Y` is affine, being a basic open of an affine scheme; see
> `AlgebraicGeometry.IsAffineOpen.basicOpen`.

```lean
public theorem coe_U_inter_zeroLocus_eq :
    (situation k).U.carrier ∩
        PrimeSpectrum.zeroLocus ((idealT k : Ideal (AmbientRing k)) : Set (AmbientRing k)) =
      ((PrimeSpectrum.basicOpen (xVar k)).carrier ∪
          (PrimeSpectrum.basicOpen (yVar k)).carrier) ∩
        PrimeSpectrum.zeroLocus ((idealT k : Ideal (AmbientRing k)) : Set (AmbientRing k))
```

**`Stacks.Algebraization.NonAlgebraizableExample.compl_zeroLocus_map_idealXYT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L211). The attribute's comment: “the two charts D(x), D(y) cover the punctured spectrum of A/t^n”.

> **Stacks Project, Tag 0EHE (the two charts cover the punctured spectrum of `A/t^n`).**
> The element `t` is nilpotent in `A/t^nA`, hence lies in every prime, so the vanishing locus of
> `𝔞 = (x,y,t)` in `Spec(A/t^nA)` is the vanishing locus of `(x,y)`. Its complement — the part of
> `Spec(A/t^nA)` lying over `U` — is therefore the union of the two basic opens `D(x)` and `D(y)`,
> and no third chart is needed to cover it.

```lean
public theorem compl_zeroLocus_map_idealXYT (n : ℕ) :
    (PrimeSpectrum.zeroLocus
        (((idealXYT k).map (Ideal.Quotient.mk ((idealT k) ^ n)) : Ideal (levelRing k n)) :
          Set (levelRing k n)))ᶜ =
      (PrimeSpectrum.basicOpen (Ideal.Quotient.mk ((idealT k) ^ n) (xVar k))).carrier ∪
        (PrimeSpectrum.basicOpen (Ideal.Quotient.mk ((idealT k) ^ n) (yVar k))).carrier
```

**`Stacks.Algebraization.NonAlgebraizableExample.isUnit_transitionElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L273). The attribute's comment: “the transition element is a unit of A\_xy/t^n A\_xy”.

> **Stacks Project, Tag 0EHE (invertibility of the transition element).** The transition
> element is a unit of `A_{xy}/t^nA_{xy}`: it is `1` plus a nilpotent element, every term beyond
> the leading `1` being divisible by `t`.

```lean
public theorem isUnit_transitionElement (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    IsUnit (transitionElement k a φ n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.chartReduction_transitionElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L303). The attribute's comment: “the transition elements are compatible with reduction mod t^n”.

> **Stacks Project, Tag 0EHE (the transition tower).** The transition elements are
> compatible with reduction modulo `t^n`, so the glued modules form an inverse system.

```lean
public theorem chartReduction_transitionElement (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    chartReduction k (xVar k * yVar k) n (transitionElement k a φ (n + 1)) =
      transitionElement k a φ n
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_ne_zero_compatible_mem_gluedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L556). The attribute's comment: “for a\_m = 0 the functions x and x + t/y glue to a nonzero compatible system”.

> **Stacks Project, Tag 0EHE (nonzero limit of global sections for `a_m = 0`).** When the
> higher coefficients `a_m` vanish, the function `x` on `D(x)` and the function `x + t/y` on
> `D(y)` glue at every order to a system of glued sections which is compatible with the reductions
> modulo `t^n` and is nonzero at every positive order. This is the source's reason that
> `lim H⁰(U, L_n)` is nonzero for this choice of coefficients.

```lean
public theorem exists_ne_zero_compatible_mem_gluedSections (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (ha : ∀ m : ℕ, 2 ≤ m → a m = 0) :
    ∃ s : (n : ℕ) → chartRing k (xVar k) n × chartRing k (yVar k) n,
      (∀ n : ℕ, s n ∈ gluedSections k n (transitionElement k a φ n)) ∧
      (∀ n : ℕ, (chartReduction k (xVar k) n (s (n + 1)).1,
        chartReduction k (yVar k) n (s (n + 1)).2) = s n) ∧
      ∀ n : ℕ, 0 < n → s n ≠ 0
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_isUnit_of_mem_gluedSections_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 919](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L919). The attribute's comment: “modulo t^2 no pair of invertible chart functions is matched”.

> **Stacks Project, Tag 0EHE (nontriviality of the glued module at order two).** The glued
> module at order two is not free: no pair consisting of an invertible function on `D(x)` and an
> invertible function on `D(y)`, both taken modulo `t²`, is matched by the transition element. The
> obstruction is that `1/(xy)` is not a sum of a function on `D(x)` and a function on `D(y)`.

```lean
public theorem not_isUnit_of_mem_gluedSections_two (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (s : chartRing k (xVar k) 2 × chartRing k (yVar k) 2)
    (hs : s ∈ gluedSections k 2 (transitionElement k a φ 2)) :
    ¬ (IsUnit s.1 ∧ IsUnit s.2)
```

**`Stacks.Algebraization.NonAlgebraizableExample.hasSeparatedExponents_of_eq_two_pow_or_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 1014](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L1014). The attribute's comment: “phi(m) = 2^m and phi(m) = m^2 separate degrees”.

> **Stacks Project, Tag 0EHE (both prescribed growth rates separate degrees).** The exponents
> `φ(m) = 2ᵐ` and the exponents `φ(m) = m²` both satisfy `HasSeparatedExponents`: the index
> `n = p + 3` works for either, since `p < 2^{p+2}` and `p < 2p + 5`.

```lean
public theorem hasSeparatedExponents_of_eq_two_pow_or_sq {φ : ℕ → ℕ}
    (hφ : (∀ m : ℕ, 2 ≤ m → φ m = 2 ^ m) ∨ (∀ m : ℕ, 2 ≤ m → φ m = m ^ 2)) :
    HasSeparatedExponents φ
```

**`Stacks.Algebraization.NonAlgebraizableExample.sectionsLimit_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean, line 1295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableExample.lean#L1295). The attribute's comment: “lim H^0(U, L\_n) = 0 for a\_m = 1 and φ(m) = 2^m or m^2”.

> **Stacks Project, Tag 0EHE (vanishing limit of global sections).** When every higher
> coefficient `a_m` is `1` and the exponents are `φ(m) = 2^m` or `φ(m) = m²`, the limit
> `lim H⁰(U, L_n)` of the global sections of the glued modules is zero.

```lean
public theorem sectionsLimit_eq_bot (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (ha : ∀ m : ℕ, 2 ≤ m → a m = 1)
    (hφ : (∀ m : ℕ, 2 ≤ m → φ m = 2 ^ m) ∨ (∀ m : ℕ, 2 ≤ m → φ m = m ^ 2)) :
    sectionsLimit k a φ = ⊥
```

**`Stacks.Algebraization.NonAlgebraizableExample.hasNonAlgebraizableInvertibleObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableInvertibleObject.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableInvertibleObject.lean#L181). The attribute's comment: “Coh(U, I O\_U) contains an invertible object which is not the completion of a coherent O\_U-module”.

> **Stacks Project, Tag 0EHE.** The category `Coh(U, I𝒪_U)` of the situation
> `A = k[x,y][[t]]`, `I = (t)`, `𝔞 = (x,y,t)` contains an invertible object which is not the
> completion of any coherent `𝒪_U`-module.
>
> The witness is the family `(𝓛ₙ)` of the example,
> `Stacks.Algebraization.NonAlgebraizableExample.levelCoherentAdicSystem`, with the source's own
> choice `aₘ = 1`, `φ(m) = 2ᵐ` of parameters — though neither clause depends on that choice.
> Invertibility is
> `Stacks.Algebraization.NonAlgebraizableExample.isInvertibleAdic_levelCoherentAdicSystem` and
> non-algebraizability is `not_isCompletionOfCoherent_levelCoherentAdicSystem`.

```lean
public theorem hasNonAlgebraizableInvertibleObject : HasNonAlgebraizableInvertibleObject k
```

**`Stacks.Algebraization.NonAlgebraizableExample.chartOpenEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L94). The attribute's comment: “A\_r/t^n A\_r is the ring of sections of O on D(r) in Spec(A/t^n A)”.

> The chart ring `A_r/tⁿA_r` is the ring of sections of `𝒪` on the basic open `D(r̄)` of
> `Spec(A/tⁿA)`, as `A/tⁿA`-algebras.

```lean
public def chartOpenEquiv (r : AmbientRing k) (n : ℕ) :
    chartRing k r n ≃ₐ[levelRing k n] Γ(levelScheme k n, chartOpen k r n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.coe_levelOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L107). The attribute's comment: “D(x) union D(y) is the part of Spec(A/t^n A) lying over U”.

> The union of the two charts is the part of `Spec(A/tⁿA)` lying over `U`, namely the complement
> of the vanishing locus of the image of `𝔞 = (x,y,t)`.

```lean
public theorem coe_levelOpen (n : ℕ) :
    (levelOpen k n : Set (levelScheme k n)) =
      (PrimeSpectrum.zeroLocus
        (((idealXYT k).map (Ideal.Quotient.mk ((idealT k) ^ n)) : Ideal (levelRing k n)) :
          Set (levelRing k n)))ᶜ
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L173). The attribute's comment: “the module L\_n, glued from A\_x/t^n A\_x and A\_y/t^n A\_y along u”.

> The module `L_n`: the sheaf of modules on the punctured spectrum of `A/tⁿA` glued from the two
> charts `D(x̄)` and `D(ȳ)` along the transition element
> `u = 1 + t/(xy) + ∑_{m ≥ 2} aₘtᵐ/(xy)^{φ(m)}`.

```lean
public def levelModule (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    (levelOpen k n).toScheme.Modules
```

**`Stacks.Algebraization.NonAlgebraizableExample.isInvertibleModule_levelModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L181). The attribute's comment: “L\_n is an invertible module on the punctured spectrum of A/t^n A”.

> The module `L_n` is an invertible module on the punctured spectrum of `A/tⁿA`.

```lean
public theorem isInvertibleModule_levelModule (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    Stacks.Ample.IsInvertibleModule (levelOpen k n).toScheme (levelModule k a φ n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_chartReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L187). The attribute's comment: “ker(A\_r/t^(n+1) A\_r -> A\_r/t^n A\_r) = t^n A\_r/t^(n+1) A\_r”.

> The kernel of the reduction `A_r/t^{n+1}A_r → A_r/tⁿA_r` is `tⁿ·A_r/t^{n+1}A_r`.

```lean
public theorem ker_chartReduction (r : AmbientRing k) (n : ℕ) :
    LinearMap.ker (chartReduction k r n).toLinearMap =
      Ideal.span {algebraMap (AmbientRing k) (Localization.Away r) (tVar k)} ^ n •
        (⊤ : Submodule (Localization.Away r) (chartRing k r (n + 1)))
```

**`Stacks.Algebraization.NonAlgebraizableExample.preimage_U_levelToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L224). The attribute's comment: “the preimage of U in Spec(A/t^n A) is its punctured spectrum”.

> The punctured spectrum of `A/tⁿA` is the preimage of the punctured spectrum `U` of `A` under
> the structure map `Spec(A/tⁿA) ⟶ Spec(A)`.

```lean
public theorem preimage_U_levelToAmbient (n : ℕ) :
    levelToAmbient k n ⁻¹ᵁ (situation k).U = levelOpen k n
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelModuleOnOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelChart.lean#L247). The attribute's comment: “L\_n pushed forward to U along Spec(A/t^n A) ∩ U → U”.

> The module `L_n` as a module on the punctured spectrum `U` of `A`: its direct image along the
> structure map `levelStructureMap`.

```lean
public def levelModuleOnOpen (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    (situation k).U.toScheme.Modules
```

**`Stacks.Algebraization.NonAlgebraizableExample.surjective_app_levelTransition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L121). The attribute's comment: “L\_(n+1) -> L\_n is surjective on sections over an affine open of a chart”.

> The transition map `𝓛ₙ₊₁ ⟶ (𝓛ₙ)` is surjective on the sections over every affine open
> contained in one of the two charts.

```lean
public theorem surjective_app_levelTransition (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ)
    (i : ULift.{u} Bool) {V : (levelOpen k (n + 1)).toScheme.Opens}
    (hV : V ≤ Stacks.SheafOfModules.twoChartFamily
      (levelChart k (xVar k) (n + 1)) (levelChart k (yVar k) (n + 1)) i)
    (hVa : IsAffineOpen V) :
    Function.Surjective ((levelTransition k a φ n).val.app (op V))
```

**`Stacks.Algebraization.NonAlgebraizableExample.epi_levelTransition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L146). The attribute's comment: “the transition map L\_(n+1) -> L\_n is an epimorphism”.

> The transition map `𝓛ₙ₊₁ ⟶ (𝓛ₙ)` of the system is an epimorphism of modules on the
> punctured spectrum of `A/t^{n+1}A`.

```lean
public theorem epi_levelTransition (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    Epi (levelTransition k a φ n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelOpenMap_comp_levelStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L175). The attribute's comment: “the closed immersions of punctured spectra are compatible with the maps to U”.

> The closed immersion of the punctured spectrum of `A/tⁿA` in that of `A/t^{n+1}A`, followed by
> the structure map of level `n + 1` to `U`, is the structure map of level `n`.

```lean
public theorem levelOpenMap_comp_levelStructureMap (n : ℕ) :
    levelOpenMap k n ≫ levelStructureMap k (n + 1) = levelStructureMap k n
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelTransitionOnOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L195). The attribute's comment: “the transition map L\_(n+1) -> L\_n of the system, as modules on U”.

> The transition map `𝓛ₙ₊₁ ⟶ 𝓛ₙ` of the system as a morphism of modules on the punctured
> spectrum `U` of `A`: the direct image along the structure map of level `n + 1` of
> `Stacks.Algebraization.NonAlgebraizableExample.levelTransition`, read through
> `Stacks.Algebraization.NonAlgebraizableExample.levelPushforwardIso`.

```lean
public def levelTransitionOnOpen (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    levelModuleOnOpen k a φ (n + 1) ⟶ levelModuleOnOpen k a φ n
```

**`Stacks.Algebraization.NonAlgebraizableExample.preimage_levelStructureMap_ambientBasicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L248). The attribute's comment: “the preimage of D(h) in the punctured spectrum of A/t^n A is D(h)”.

> The preimage of `D(h)` under the structure map `Spec(A/tⁿA) ∩ U ⟶ U` is the chart `D(h̄)` of
> the punctured spectrum of `A/tⁿA`.

```lean
public theorem preimage_levelStructureMap_ambientBasicOpen (h : AmbientRing k) (m : ℕ) :
    levelStructureMap k m ⁻¹ᵁ ambientBasicOpen k h = levelChart k h m
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_mem_basicOpen_of_mem_U`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L280). The attribute's comment: “U is covered by D(x), D(y) and D(t)”.

> The punctured spectrum `U` of `A` is covered by `D(x)`, `D(y)` and `D(t)`.

```lean
public theorem exists_mem_basicOpen_of_mem_U (p : (situation k).X)
    (hp : p ∈ (situation k).U) :
    p ∈ PrimeSpectrum.basicOpen (xVar k) ∨ p ∈ PrimeSpectrum.basicOpen (yVar k) ∨
      p ∈ PrimeSpectrum.basicOpen (tVar k)
```

**`Stacks.Algebraization.NonAlgebraizableExample.epi_levelTransitionOnOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L334). The attribute's comment: “the transition map of the system on U is an epimorphism”.

> The transition map `𝓛ₙ₊₁ ⟶ 𝓛ₙ` of the system, read as a morphism of modules on the punctured
> spectrum `U` of `A`, is an epimorphism.

```lean
public theorem epi_levelTransitionOnOpen (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    Epi (levelTransitionOnOpen k a φ n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L370). The attribute's comment: “the system (L\_n) as a diagram over the opposite of the naturals”.

> The family `(𝓛ₙ)` as an inverse system of modules on the punctured spectrum `U` of `A`,
> assembled from the transition maps
> `Stacks.Algebraization.NonAlgebraizableExample.levelTransitionOnOpen`. Its `n`-th term is
> `𝓛ₙ₊₁`, the module on the punctured spectrum of `A/t^{n+1}A`, matching the indexing of
> `Stacks.Coherent.IsCoherentAdicSystem`.

```lean
public def levelSystem (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) :
    ℕᵒᵖ ⥤ (situation k).U.toScheme.Modules
```

**`Stacks.Algebraization.NonAlgebraizableExample.epi_levelSystem_map_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelEpi.lean#L387). The attribute's comment: “the maps of the system (L\_n) from level n+1 to level n are epimorphisms”.

> The maps of the system from its `(n + 1)`-st term to its `n`-th one are epimorphisms.

```lean
public theorem epi_levelSystem_map_succ (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    Epi ((levelSystem k a φ).map (homOfLE (Nat.le_succ n)).op)
```

**`Stacks.Algebraization.NonAlgebraizableExample.appLE_levelStructureMap_chartOpenEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L218). The attribute's comment: “the two routes from A into the sections of O over a chart agree”.

> **The two routes from `A` into a chart's sections agree.** An element `z` of `A`, restricted
> to an open `V` of `U` and pulled back along the structure map `Spec(A/tᵐA) ∩ U ⟶ U` to an open `P`
> inside the chart `D(r̄)`, is the image of `z` in the chart ring `A_r/tᵐA_r` read as a section of
> `𝒪` and restricted to `P`.
>
> This is what joins the description of the ideal `(I𝒪_U)(V)` — the image of `I` under
> `A → Γ(X, X) → Γ(U, V)` — to the description of the chart rings, and so the identity the kernel
> computation of the transition maps rests on.

```lean
public theorem appLE_levelStructureMap_chartOpenEquiv (q : AmbientRing k) (m : ℕ)
    {V : (situation k).U.toScheme.Opens} {P : (levelOpen k m).toScheme.Opens}
    (e : P ≤ levelStructureMap k m ⁻¹ᵁ V)
    (e' : P ≤ (levelOpen k m).ι ⁻¹ᵁ chartOpen k q m) (z : AmbientRing k) :
    ((levelStructureMap k m).appLE V P e).hom
        (((situation k).U.ι.appLE ⊤ V le_top).hom
          ((Scheme.ΓSpecIso (CommRingCat.of (AmbientRing k))).inv.hom z)) =
      ((levelOpen k m).ι.appLE (chartOpen k q m) P e').hom
        (chartOpenEquiv k q m (levelToChart k q m (levelElt k z m)))
```

**`Stacks.Algebraization.NonAlgebraizableExample.app_levelOpenMap_appLE_ι_chartOpenEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L308). The attribute's comment: “on an open over D(r) the closed immersion induces A\_r/t^(m+1) -> A\_r/t^m”.

> **The closed immersion of punctured spectra on a chart's sections.** Over an open `P` of the
> punctured spectrum of `A/t^{m+1}A` whose image is the basic open `D(r̄)`, the closed immersion of
> punctured spectra induces the reduction of chart rings `A_r/t^{m+1}A_r → A_r/tᵐA_r`.
>
> This is the general-open analogue of
> `Stacks.Algebraization.NonAlgebraizableExample.app_levelOverlapRingEquiv`, which is the case of
> the overlap of the two charts.

```lean
public theorem app_levelOpenMap_appLE_ι_chartOpenEquiv (q : AmbientRing k) (m : ℕ)
    {P : (levelOpen k (m + 1)).toScheme.Opens}
    (e' : P ≤ (levelOpen k (m + 1)).ι ⁻¹ᵁ chartOpen k q (m + 1))
    (f' : levelOpenMap k m ⁻¹ᵁ P ≤ (levelOpen k m).ι ⁻¹ᵁ chartOpen k q m)
    (v : chartRing k q (m + 1)) :
    ((levelOpenMap k m).app P).hom
        (((levelOpen k (m + 1)).ι.appLE (chartOpen k q (m + 1)) P e').hom
          (chartOpenEquiv k q (m + 1) v)) =
      ((levelOpen k m).ι.appLE (chartOpen k q m) (levelOpenMap k m ⁻¹ᵁ P) f').hom
        (chartOpenEquiv k q m (chartReduction k q m v))
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_smul_of_app_levelTransitionOnOpen_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L378). The attribute's comment: “a section of L\_(m+1) killed by the transition map is t^m times a section”.

> **The hard half of the kernel computation.** A section of `𝓛ₘ₊₁`
> over an open `V` of `U` whose preimage is a chart `D(r̄)` of the punctured spectrum of
> `A/t^{m+1}A`, killed by the transition map `𝓛ₘ₊₁ ⟶ 𝓛ₘ`, is `tᵐ` times a section.
>
> Both modules are trivialized over the chart by
> `Stacks.Algebraization.NonAlgebraizableExample.chartLinearEquiv_levelTransition`, the sections
> over the chart are the chart ring by
> `Stacks.Algebraization.NonAlgebraizableExample.chartOpenEquiv`, and there the statement is
> `Stacks.Algebraization.NonAlgebraizableExample.ker_chartReduction`. The factor `tᵐ` produced
> upstairs is the pullback of the restriction of `t` to `V` by
> `Stacks.Algebraization.NonAlgebraizableExample.appLE_levelStructureMap_chartOpenEquiv`.

```lean
public theorem exists_smul_of_app_levelTransitionOnOpen_eq_zero (a : ℕ → PlaneRing k)
    (φ : ℕ → ℕ) (m : ℕ) (q : AmbientRing k) (i : ULift.{u} Bool)
    (hq : PrimeSpectrum.basicOpen q ≤ (situation k).U)
    {V : (situation k).U.toScheme.Opens}
    (hPeq : levelStructureMap k (m + 1) ⁻¹ᵁ V = levelChart k q (m + 1))
    (hchart : levelChart k q (m + 1) ≤ Stacks.SheafOfModules.twoChartFamily
      (levelChart k (xVar k) (m + 1)) (levelChart k (yVar k) (m + 1)) i)
    (s : Γ(levelModuleOnOpen k a φ (m + 1), V))
    (hs : ((levelTransitionOnOpen k a φ m).val.app (op V)).hom s = 0) :
    ∃ y : Γ(levelModuleOnOpen k a φ (m + 1), V),
      s = ((situation k).U.ι.appLE ⊤ V le_top).hom
        ((Scheme.ΓSpecIso (CommRingCat.of (AmbientRing k))).inv.hom (tVar k)) ^ m • y
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_app_levelTransitionOnOpen_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L488). The attribute's comment: “over a basic open inside a chart ker(L\_(m+1) -> L\_m) = I(V)^m L\_(m+1)(V)”.

> **The kernel over a basic open inside a chart.** Over an affine
> open `V` of `U` whose preimage upstairs is a chart of the punctured spectrum of `A/t^{m+1}A`, the
> kernel of the transition map `𝓛ₘ₊₁ ⟶ 𝓛ₘ` is `I(V)ᵐ 𝓛ₘ₊₁(V)`.

```lean
public theorem ker_app_levelTransitionOnOpen_chart (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (m : ℕ)
    (q : AmbientRing k) (i : ULift.{u} Bool)
    (hq : PrimeSpectrum.basicOpen q ≤ (situation k).U)
    (V : (situation k).U.toScheme.affineOpens)
    (hPeq : levelStructureMap k (m + 1) ⁻¹ᵁ (V : (situation k).U.toScheme.Opens) =
      levelChart k q (m + 1))
    (hchart : levelChart k q (m + 1) ≤ Stacks.SheafOfModules.twoChartFamily
      (levelChart k (xVar k) (m + 1)) (levelChart k (yVar k) (m + 1)) i) :
    LinearMap.ker ((levelTransitionOnOpen k a φ m).val.app
        (op (V : (situation k).U.toScheme.Opens))).hom =
      (idealOnOpen (situation k)).ideal V ^ m •
        (⊤ : Submodule Γ((situation k).U.toScheme, (V : (situation k).U.toScheme.Opens))
          Γ(levelModuleOnOpen k a φ (m + 1), (V : (situation k).U.toScheme.Opens)))
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_app_levelTransitionOnOpen_of_preimage_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L513). The attribute's comment: “over a basic open with empty preimage both sides of the kernel identity vanish”.

> **The kernel over a basic open meeting no chart.** Over an affine
> open `V` of `U` whose preimage upstairs is empty — a `D(ht)`, the image of `t` being nilpotent in
> `A/t^{m+1}A` — the kernel of the transition map `𝓛ₘ₊₁ ⟶ 𝓛ₘ` is `I(V)ᵐ 𝓛ₘ₊₁(V)`, both sides
> being submodules of a module with one element.

```lean
public theorem ker_app_levelTransitionOnOpen_of_preimage_eq_bot (a : ℕ → PlaneRing k)
    (φ : ℕ → ℕ) (m : ℕ) (V : (situation k).U.toScheme.affineOpens)
    (hbot : levelStructureMap k (m + 1) ⁻¹ᵁ (V : (situation k).U.toScheme.Opens) = ⊥) :
    LinearMap.ker ((levelTransitionOnOpen k a φ m).val.app
        (op (V : (situation k).U.toScheme.Opens))).hom =
      (idealOnOpen (situation k)).ideal V ^ m •
        (⊤ : Submodule Γ((situation k).U.toScheme, (V : (situation k).U.toScheme.Opens))
          Γ(levelModuleOnOpen k a φ (m + 1), (V : (situation k).U.toScheme.Opens)))
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_app_levelSystem_map_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L536). The attribute's comment: “the kernel of the maps of the system over the basis of affine opens D(hg)”.

> **The kernel computation of the system.** The kernel of the map of
> the system `(𝓛ₙ)` from its `(n + 1)`-st term to its `n`-th one, over a member `D(hg)` of the basis
> of affine opens, is `I(V)^{n+1}` times the sections of the `(n + 1)`-st term. This is the
> hypothesis `hker` of `Stacks.Algebraization.isCoherentAdicSystem_of_basis_ker`.
>
> For `g` one of the two variables the preimage of `D(hg)` upstairs is a chart, where the chartwise
> computation applies; for `g = t` it is empty and both sides vanish.

```lean
public theorem ker_app_levelSystem_map_succ (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ)
    (V : (situation k).U.toScheme.affineOpens) (hV : V ∈ ambientBasicAffineOpens k) :
    LinearMap.ker (((levelSystem k a φ).map (homOfLE (Nat.le_succ n)).op).val.app
        (op (V : (situation k).U.toScheme.Opens))).hom =
      (idealOnOpen (situation k)).ideal V ^ (n + 1) •
        (⊤ : Submodule Γ((situation k).U.toScheme, (V : (situation k).U.toScheme.Opens))
          Γ((levelSystem k a φ).obj (op (n + 1)),
            (V : (situation k).U.toScheme.Opens)))
```

**`Stacks.Algebraization.NonAlgebraizableExample.isCoherentAdicSystem_levelSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L567). The attribute's comment: “the system (L\_n) is a coherent I O\_U-adic system”.

> **The system lies in `Coh(U, I𝒪_U)`.** The family `(𝓛ₙ)`, as a diagram over `ℕᵒᵖ` of modules
> on the punctured spectrum `U` of `A`, is a coherent `I𝒪_U`-adic system: its terms are coherent and
> annihilated by the successive powers of `I𝒪_U`, its transition maps are epimorphisms, and their
> kernels over the basis of affine opens `D(hg)` are the expected ideal multiples.

```lean
public theorem isCoherentAdicSystem_levelSystem (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) :
    Stacks.Coherent.IsCoherentAdicSystem (idealOnOpen (situation k)) (levelSystem k a φ)
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelCoherentAdicSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L578). The attribute's comment: “the family (L\_n) as an object of Coh(U, I O\_U)”.

> **The object of `Coh(U, I𝒪_U)`.** The family `(𝓛ₙ)` as an object
> of the category `Coh(U, I𝒪_U)` of coherent `I𝒪_U`-adic systems on the punctured spectrum `U` of
> `A`.

```lean
public def levelCoherentAdicSystem (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) :
    Stacks.Coherent.CoherentAdicSystems (idealOnOpen (situation k))
```

**`Stacks.Algebraization.NonAlgebraizableExample.isInvertibleAdic_levelCoherentAdicSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L591). The attribute's comment: “the object (L\_n) of Coh(U, I O\_U) is invertible”.

> **The object is invertible.** The object `(𝓛ₙ)` of
> `Coh(U, I𝒪_U)` is invertible: its `n`-th term is the direct image of an invertible module on the
> closed subscheme `V((I𝒪_U)^{n+1})` of `U`.
>
> That subscheme is the punctured spectrum of `A/t^{n+1}A` by
> `Stacks.Algebraization.NonAlgebraizableExample.exists_subschemeIso_levelOpen`, compatibly with
> the two morphisms to `U`, and `𝓛ₙ₊₁` is invertible there by
> `Stacks.Algebraization.NonAlgebraizableExample.isInvertibleModule_levelModule`.

```lean
public theorem isInvertibleAdic_levelCoherentAdicSystem (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) :
    Stacks.Coherent.IsInvertibleAdic (idealOnOpen (situation k))
      (levelCoherentAdicSystem k a φ)
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_isUnit_mem_gluedSections_of_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean#L89). The attribute's comment: “a trivialization of L\_n is a matched pair of invertible chart functions”.

> **Stacks Project, Tag 0EHE (a trivialization of `𝓛ₙ` is a pair of invertible chart
> functions).** If the glued module `𝓛ₙ` is isomorphic to the structure sheaf of the punctured
> spectrum of `A/tⁿA`, then the transition element matches a pair consisting of an invertible
> function on `D(x̄)` and an invertible function on `D(ȳ)`.

```lean
public theorem exists_isUnit_mem_gluedSections_of_iso_unit (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (n : ℕ) (e : levelModule k a φ n ≅ Stacks.Ample.unitModule (levelOpen k n).toScheme) :
    ∃ s : chartRing k (xVar k) n × chartRing k (yVar k) n,
      s ∈ gluedSections k n (transitionElement k a φ n) ∧ IsUnit s.1 ∧ IsUnit s.2
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_isTrivial_levelModule_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean#L139). The attribute's comment: “L\_2 is not isomorphic to the structure sheaf”.

> **Stacks Project, Tag 0EHE (`𝓛₂ ≇ 𝒪`).** The glued module at order two is not trivial, for
> every choice of the coefficients `aₘ` and the exponents `φ(m)`: a trivialization would match a
> pair of invertible chart functions by the transition element `1 + t/(xy)`, and
> `not_isUnit_of_mem_gluedSections_two` rules that out. This is the source's "`𝓛₂ ≇ 𝒪_U/I²𝒪_U` by
> construction".

```lean
public theorem not_isTrivial_levelModule_two (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) :
    ¬ Nonempty (levelModule k a φ 2 ≅ Stacks.Ample.unitModule (levelOpen k 2).toScheme)
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_nonempty_pullback_iso_levelModule_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean#L151). The attribute's comment: “no invertible module on an open of Spec(A) pulls back to L\_2”.

> **Stacks Project, Tag 0EHE (no line bundle on an open of `Spec(A)` pulls back to `𝓛₂`).**
> Let `V` be an open subscheme of `Spec(A)`, `A = k[x,y][[t]]`, let `L` be an invertible
> `𝒪_V`-module, and let `f` be any morphism from the punctured spectrum of `A/t²A` to `V`. Then
> the pullback of `L` along `f` is not isomorphic to `𝓛₂`: the pullback is trivial, because `L`
> itself is trivial — `A` being a UFD — and `𝓛₂` is not.

```lean
public theorem not_nonempty_pullback_iso_levelModule_two (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    {V : (Spec (CommRingCat.of (AmbientRing k))).Opens}
    (f : (levelOpen k 2).toScheme ⟶ V.toScheme) (L : V.toScheme.Modules)
    (hL : Stacks.Ample.IsInvertibleModule V.toScheme L) :
    ¬ Nonempty ((Scheme.Modules.pullback f).obj L ≅ levelModule k a φ 2)
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_nonempty_pullback_levelStructureMap_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelNontrivial.lean#L167). The attribute's comment: “no invertible module on U restricts to L\_2”.

> **Stacks Project, Tag 0EHE (the class of `𝓛₂` is not in the image of `Pic(U)`).** The
> specialization of `not_nonempty_pullback_iso_levelModule_two` to the structure map of the
> punctured spectrum of `A/t²A` over the punctured spectrum `U` of `A`: no invertible
> `𝒪_U`-module restricts to `𝓛₂`.

```lean
public theorem not_nonempty_pullback_levelStructureMap_iso (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (L : (situation k).U.toScheme.Modules)
    (hL : Stacks.Ample.IsInvertibleModule (situation k).U.toScheme L) :
    ¬ Nonempty ((Scheme.Modules.pullback (levelStructureMap k 2)).obj L ≅ levelModule k a φ 2)
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_levelToAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean#L68). The attribute's comment: “Spec(A/t^n A) is the closed subscheme of Spec(A) cut out by I^n”.

> The kernel ideal sheaf of the closed immersion `Spec(A/tⁿA) ⟶ Spec(A)` is the `n`-th power of
> the ideal sheaf attached to `I = (t)`.

```lean
public theorem ker_levelToAmbient (n : ℕ) :
    (levelToAmbient k n).ker =
      Scheme.IdealSheafData.ofIdealTop ((idealT k).map
        (CommRingCat.Hom.hom (Scheme.ΓSpecIso (CommRingCat.of (AmbientRing k))).inv)) ^ n
```

**`Stacks.Algebraization.NonAlgebraizableExample.idealOnOpen_pow_eq_comap_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean#L79). The attribute's comment: “(I O\_U)^n is the restriction to U of the ideal sheaf of Spec(A/t^n A)”.

> The `n`-th power of the ideal sheaf `I𝒪_U` on the punctured spectrum of `A` is the
> restriction to `U` of the ideal sheaf cutting out `Spec(A/tⁿA)` in `Spec(A)`.

```lean
public theorem idealOnOpen_pow_eq_comap_ker (n : ℕ) :
    idealOnOpen (situation k) ^ n = (levelToAmbient k n).ker.comap (situation k).U.ι
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_subschemeIso_levelOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSubscheme.lean#L90). The attribute's comment: “V((I O\_U)^n) is the punctured spectrum of A/t^n A”.

> The closed subscheme of the punctured spectrum `U` of `A` cut out by the `n`-th power of
> `I𝒪_U` is the punctured spectrum of `A/tⁿA`, compatibly with the two morphisms to `U`: the closed
> immersion of the subscheme and the structure map
> `Stacks.Algebraization.NonAlgebraizableExample.levelStructureMap`.

```lean
public theorem exists_subschemeIso_levelOpen (n : ℕ) :
    ∃ e : (idealOnOpen (situation k) ^ n).subscheme ≅ (levelOpen k n).toScheme,
      e.hom ≫ levelStructureMap k n = (idealOnOpen (situation k) ^ n).subschemeι
```

**`Stacks.Algebraization.NonAlgebraizableExample.ker_levelStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L135). The attribute's comment: “the kernel ideal sheaf of Spec(A/t^n A) ∩ U → U is (I O\_U)^n”.

> **Stacks Project, Tag 0EHE (the level scheme over `U` is cut out by `(I𝒪_U)ⁿ`).** The kernel
> ideal sheaf of the structure map `Spec(A/tⁿA) ∩ U ⟶ U` is the `n`-th power of `I𝒪_U`.
>
> This is `Stacks.Algebraization.NonAlgebraizableExample.exists_subschemeIso_levelOpen` read as an
> equality of ideal sheaves: that identification is compatible with the two morphisms to `U`, and a
> kernel ideal sheaf does not change when the morphism is precomposed with an isomorphism.

```lean
public theorem ker_levelStructureMap (m : ℕ) :
    (levelStructureMap k m).ker = idealOnOpen (situation k) ^ m
```

**`Stacks.Algebraization.NonAlgebraizableExample.isCoherent_levelModuleOnOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L148). The attribute's comment: “L\_n, pushed forward to U, is a coherent module”.

> **Stacks Project, Tag 0EHE (`𝓛ₙ` is coherent on `U`).** The module `𝓛ₙ`, read on the
> punctured spectrum `U` of `A`, is coherent: it is invertible upstairs, hence coherent there by
> [Stacks, Tag 01XZ], and its direct image along the closed immersion
> `Spec(A/tⁿA) ∩ U ⟶ U` — a finite morphism — is coherent by [Stacks, Tag 01Y6].

```lean
public theorem isCoherent_levelModuleOnOpen (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (m : ℕ) :
    _root_.SheafOfModules.IsCoherent.{u} (levelModuleOnOpen k a φ m)
```

**`Stacks.Algebraization.NonAlgebraizableExample.isCoherent_levelSystem_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L160). The attribute's comment: “the terms of the system (L\_n) are coherent”.

> **Stacks Project, Tag 0EHE (the system has coherent terms).** Every term of the system
> `(𝓛ₙ)` is a coherent module on `U`. This is the hypothesis `hcoh` of
> `Stacks.Algebraization.isCoherentAdicSystem_of_basis_ker`.

```lean
public theorem isCoherent_levelSystem_obj (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    _root_.SheafOfModules.IsCoherent.{u} ((levelSystem k a φ).obj (op n))
```

**`Stacks.Algebraization.NonAlgebraizableExample.idealPowerMultiple_levelModuleOnOpen_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L183). The attribute's comment: “L\_n, pushed forward to U, is annihilated by (I O\_U)^n”.

> **Stacks Project, Tag 0EHE (`𝓛ₙ` is annihilated by `(I𝒪_U)ⁿ`).** The module `𝓛ₙ`, read on
> `U`, is annihilated by the `n`-th power of `I𝒪_U`: that power is the kernel ideal sheaf of the
> closed immersion `Spec(A/tⁿA) ∩ U ⟶ U` by
> `Stacks.Algebraization.NonAlgebraizableExample.ker_levelStructureMap`, and the kernel of a closed
> immersion kills every direct image along it.

```lean
public theorem idealPowerMultiple_levelModuleOnOpen_eq_bot (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (m : ℕ) :
    idealPowerMultiple (idealOnOpen (situation k)) m (levelModuleOnOpen k a φ m) = ⊥
```

**`Stacks.Algebraization.NonAlgebraizableExample.idealPowerMultiple_levelSystem_obj_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L198). The attribute's comment: “the n-th term of the system (L\_n) is annihilated by (I O\_U)^(n+1)”.

> **Stacks Project, Tag 0EHE (the system is annihilated by the successive ideal powers).** The
> `n`-th term of the system `(𝓛ₙ)` is annihilated by the `(n + 1)`-st power of `I𝒪_U`. This is the
> hypothesis `hann` of `Stacks.Algebraization.isCoherentAdicSystem_of_basis_ker`; the exponent
> matches because the `n`-th term of the system is `𝓛ₙ₊₁`.

```lean
public theorem idealPowerMultiple_levelSystem_obj_eq_bot (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (n : ℕ) :
    idealPowerMultiple (idealOnOpen (situation k)) (n + 1) ((levelSystem k a φ).obj (op n)) = ⊥
```

**`Stacks.Algebraization.NonAlgebraizableExample.ambientBasicAffineOpens`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L220). The attribute's comment: “the family of affine opens D(hg) of U, for g one of x, y, t”.

> **Stacks Project, Tag 0EHE (the family of affine opens the kernel computation runs on).** The
> affine opens `D(hg)` of `U`, for `h` an element of `A` and `g` one of the three variables `x`,
> `y`, `t`. Over each of them the module `𝓛ₙ` is trivialized — for `g = x` or `g = y` because
> `D(hg)` lies in a chart, for `g = t` because its preimage upstairs is empty — and they form a
> basis of the topology of `U`.

```lean
public def ambientBasicAffineOpens : Set (situation k).U.toScheme.affineOpens
```

**`Stacks.Algebraization.NonAlgebraizableExample.exists_mem_ambientBasicAffineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelSystem.lean#L230). The attribute's comment: “the affine opens D(hg) are a basis of the topology of U”.

> **Stacks Project, Tag 0EHE (those affine opens are a basis).** Every point of every open `W`
> of the punctured spectrum `U` of `A` has one of the affine opens `D(hg)` around it inside `W`:
> the basic opens `D(h)` of `Spec(A)` are a basis of `U`, and `D(h)` is cut down into `U` by
> whichever of `D(x)`, `D(y)`, `D(t)` contains the point. This is the hypothesis `hS` of
> `Stacks.Algebraization.isCoherentAdicSystem_of_basis_ker`.

```lean
public theorem exists_mem_ambientBasicAffineOpens
    (W : (situation k).U.toScheme.Opens) (x : (situation k).U.toScheme) (hx : x ∈ W) :
    ∃ V ∈ ambientBasicAffineOpens k, x ∈ (V : (situation k).U.toScheme.Opens) ∧
      (V : (situation k).U.toScheme.Opens) ≤ W
```

**`Stacks.Algebraization.NonAlgebraizableExample.preimage_levelChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean#L117). The attribute's comment: “the preimage of the chart D(r) of level n+1 is the chart D(r) of level n”.

> **Stacks Project, Tag 0EHE (the charts are compatible down the tower).** The preimage of the
> chart `D(r̄)` of the punctured spectrum of `A/t^{n+1}A` is the chart `D(r̄)` of the punctured
> spectrum of `A/tⁿA`, for a chart whose basic open lies in the punctured spectrum.

```lean
public theorem preimage_levelChart (r : AmbientRing k) (n : ℕ)
    (h : chartOpen k r (n + 1) ≤ levelOpen k (n + 1)) :
    levelOpenMap k n ⁻¹ᵁ levelChart k r (n + 1) = levelChart k r n
```

**`Stacks.Algebraization.NonAlgebraizableExample.app_levelSchemeMap_chartOpenEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean#L151). The attribute's comment: “on D(r) the closed immersion of level schemes induces A\_r/t^(n+1) -> A\_r/t^n”.

> **Stacks Project, Tag 0EHE (the closed immersion induces the reduction on chart rings).** On
> the ring of sections over the basic open `D(r̄)`, the closed immersion
> `Spec(A/tⁿA) ⟶ Spec(A/t^{n+1}A)` induces the reduction `A_r/t^{n+1}A_r → A_r/tⁿA_r`.

```lean
public theorem app_levelSchemeMap_chartOpenEquiv (r : AmbientRing k) (n : ℕ)
    (w : chartRing k r (n + 1)) :
    ((levelSchemeMap k n).app (chartOpen k r (n + 1))).hom (chartOpenEquiv k r (n + 1) w) =
      chartOpenEquiv k r n (chartReduction k r n w)
```

**`Stacks.Algebraization.NonAlgebraizableExample.app_levelOverlapUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean#L257). The attribute's comment: “the closed immersion of punctured spectra carries u at level n+1 to u at level n”.

> **Stacks Project, Tag 0EHE (the transition units form a tower on the schemes).** The closed
> immersion of the punctured spectrum of `A/tⁿA` in that of `A/t^{n+1}A` carries the transition unit
> of level `n + 1` to the transition unit of level `n`. This is the scheme-level form of
> `Stacks.Algebraization.NonAlgebraizableExample.chartReduction_transitionElement`, and the
> intertwining hypothesis the transition map `𝓛ₙ₊₁ ⟶ 𝓛ₙ` is built from.

```lean
public theorem app_levelOverlapUnit (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    Units.map ((levelOpenMap k n).app (levelOverlap k (n + 1))).hom
        (levelOverlapUnit k a φ (n + 1)) =
      Stacks.SheafOfModules.overlapUnit (levelOverlapUnit k a φ n)
        (levelOpenMap k n ⁻¹ᵁ levelOverlap k (n + 1)) (preimage_levelOverlap k n).le
```

**`Stacks.Algebraization.NonAlgebraizableExample.levelTransition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean#L278). The attribute's comment: “the transition map L\_(n+1) -> L\_n of the system”.

> **Stacks Project, Tag 0EHE (the transition maps of the system).** The transition map
> `𝓛ₙ₊₁ ⟶ 𝓛ₙ` of the system of [Stacks, Tag 0EHE], as a morphism from the module of level `n + 1`
> on the punctured spectrum of `A/t^{n+1}A` to the direct image of the module of level `n` along the
> closed immersion of punctured spectra.

```lean
public def levelTransition (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ) :
    levelModule k a φ (n + 1) ⟶
      (Scheme.Modules.pushforward (levelOpenMap k n)).obj (levelModule k a φ n)
```

**`Stacks.Algebraization.NonAlgebraizableExample.chartLinearEquiv_levelTransition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelTransition.lean#L291). The attribute's comment: “in the chart trivializations L\_(n+1) -> L\_n is the reduction of functions”.

> **Stacks Project, Tag 0EHE (the transition map in the chart trivializations).** Over an open
> inside one of the two charts, where both modules are trivialized by reading the coordinate of that
> chart, the transition map is the reduction of functions. This pins `levelTransition` down.

```lean
public theorem chartLinearEquiv_levelTransition (a : ℕ → PlaneRing k) (φ : ℕ → ℕ) (n : ℕ)
    (i : ULift.{u} Bool) {V : (levelOpen k (n + 1)).toScheme.Opens}
    (hV : V ≤ Stacks.SheafOfModules.twoChartFamily
      (levelChart k (xVar k) (n + 1)) (levelChart k (yVar k) (n + 1)) i)
    (hV' : levelOpenMap k n ⁻¹ᵁ V ≤ Stacks.SheafOfModules.twoChartFamily
      (levelChart k (xVar k) n) (levelChart k (yVar k) n) i)
    (s : (Stacks.SheafOfModules.twoChartCocycle
      (levelOverlapUnit k a φ (n + 1))).sectionsSubmodule V) :
    (Stacks.SheafOfModules.twoChartCocycle (levelOverlapUnit k a φ n)).chartLinearEquiv i hV'
        ((levelTransition k a φ n).val.app (op V) s) =
      ((levelOpenMap k n).app V).hom
        ((Stacks.SheafOfModules.twoChartCocycle
          (levelOverlapUnit k a φ (n + 1))).chartLinearEquiv i hV s)
```

**`Stacks.Algebraization.NonAlgebraizableExample.isVanishingSectionsParameter_two_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean#L84). The attribute's comment: “a\_m = 1 and φ(m) = 2^m satisfy the parameter condition”.

> **Stacks Project, Tag 0EHE (the first prescribed choice).** The coefficients `aₘ = 1` and
> the exponents `φ(m) = 2ᵐ` satisfy the parameter condition.

```lean
public theorem isVanishingSectionsParameter_two_pow {a : ℕ → PlaneRing k} {φ : ℕ → ℕ}
    (ha : ∀ m : ℕ, 2 ≤ m → a m = 1) (hφ : ∀ m : ℕ, 2 ≤ m → φ m = 2 ^ m) :
    IsVanishingSectionsParameter k a φ
```

**`Stacks.Algebraization.NonAlgebraizableExample.isVanishingSectionsParameter_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean#L92). The attribute's comment: “a\_m = 1 and φ(m) = m^2 satisfy the parameter condition”.

> **Stacks Project, Tag 0EHE (the second prescribed choice).** The coefficients `aₘ = 1` and
> the exponents `φ(m) = m²` satisfy the parameter condition.

```lean
public theorem isVanishingSectionsParameter_sq {a : ℕ → PlaneRing k} {φ : ℕ → ℕ}
    (ha : ∀ m : ℕ, 2 ≤ m → a m = 1) (hφ : ∀ m : ℕ, 2 ≤ m → φ m = m ^ 2) :
    IsVanishingSectionsParameter k a φ
```

**`Stacks.Algebraization.NonAlgebraizableExample.sectionsLimit_eq_bot_of_isVanishingSectionsParameter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean#L108). The attribute's comment: “lim H^0(U, L\_n) = 0 under the parameter condition”.

> **Stacks Project, Tag 0EHE (the vanishing of the limit of global sections).** Under the
> parameter condition the limit `lim H⁰(U, 𝓛ₙ)` is zero.

```lean
public theorem sectionsLimit_eq_bot_of_isVanishingSectionsParameter (a : ℕ → PlaneRing k)
    (φ : ℕ → ℕ) (h : IsVanishingSectionsParameter k a φ) : sectionsLimit k a φ = ⊥
```

**`Stacks.Algebraization.NonAlgebraizableExample.not_exists_compatible_isUnit_mem_gluedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableParameter.lean#L120). The attribute's comment: “under the parameter condition (L\_n) has no compatible trivializing sections”.

> **Stacks Project, Tag 0EHE (no compatible trivializing sections under the parameter
> condition).** A trivialization of the glued module `𝓛ₙ` is a pair of invertible chart functions
> matched by the transition element, so a *compatible system* of trivializations of the whole
> family would be a system of glued pairs, compatible with reduction modulo `tⁿ`, whose
> `D(x̄)`-components are invertible. Under the parameter condition no such system exists: it would
> be a nonzero element of `lim H⁰(U, 𝓛ₙ)`, which vanishes. This is the content of the source's
> second proof of non-algebraizability.

```lean
public theorem not_exists_compatible_isUnit_mem_gluedSections (a : ℕ → PlaneRing k) (φ : ℕ → ℕ)
    (h : IsVanishingSectionsParameter k a φ) :
    ¬ ∃ s : (n : ℕ) → chartRing k (xVar k) n × chartRing k (yVar k) n,
      (∀ n : ℕ, s n ∈ gluedSections k n (transitionElement k a φ n)) ∧
      (∀ n : ℕ, (chartReduction k (xVar k) n (s (n + 1)).1,
        chartReduction k (yVar k) n (s (n + 1)).2) = s n) ∧
      ∀ n : ℕ, 0 < n → IsUnit (s n).1
```

**`Stacks.Algebraization.NonAlgebraizableExample.uniqueFactorizationMonoid_ambientRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean#L64). The attribute's comment: “the ring A = k[x,y][[t]] is a UFD”.

> **The ambient ring `A = k[x,y][[t]]` of the example is a unique factorization domain.** The
> polynomial ring `k[x,y]` is regular and factorial, so its Picard group is trivial, and the power
> series ring over a regular factorial ring is factorial.

```lean
public theorem uniqueFactorizationMonoid_ambientRing :
    UniqueFactorizationMonoid (AmbientRing k)
```

**`Stacks.Algebraization.NonAlgebraizableExample.subsingleton_picardGroup_ambientOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean#L72). The attribute's comment: “Pic of every open of Spec(k[x,y][[t]]) is trivial”.

> **`Pic` of an open of the ambient affine scheme vanishes.** The Picard group of every open
> subscheme of `Spec(A)`, `A = k[x,y][[t]]`, is trivial: `A` is a unique factorization domain, and
> [Stacks, Tag 0BDA] trivializes the Picard group of every open of the spectrum of one.

```lean
public theorem subsingleton_picardGroup_ambientOpen
    (V : (Spec (CommRingCat.of (AmbientRing k))).Opens) :
    Subsingleton V.toScheme.picardGroup
```

**`Stacks.Algebraization.NonAlgebraizableExample.isTrivial_of_isInvertible_ambientOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizablePicard.lean#L82). The attribute's comment: “an invertible module on an open of Spec(k[x,y][[t]]) is trivial”.

> **An invertible module on an open of `Spec(A)` is trivial.** An invertible module on an open
> `V ⊆ Spec(k[x,y][[t]])` — for instance on an open `V` with `U ∩ Y ⊆ V ⊆ U` on which an
> algebraizing coherent module becomes invertible — is isomorphic to the structure sheaf of `V`.

```lean
public theorem isTrivial_of_isInvertible_ambientOpen
    {V : (Spec (CommRingCat.of (AmbientRing k))).Opens} (L : V.toScheme.Modules)
    (hL : Stacks.SheafOfModules.IsInvertible V.toScheme.presheaf V.toScheme.ringCatIsSheaf L) :
    Stacks.SheafOfModules.IsTrivial V.toScheme.presheaf V.toScheme.ringCatIsSheaf L
```

**`Stacks.Algebraization.NonAlgebraizableExample.sectionsLimitLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean#L637). The attribute's comment: “lim H^0(U, L\_n) is the module of compatible systems of glued chart pairs”.

> **Stacks Project, Tag 0EHE (`lim H⁰(U, 𝓛ₙ)` is the module of compatible glued pairs).** The
> `A`-module `lim H⁰(U, 𝓛ₙ)` of the object `(𝓛ₙ)` of `Coh(U, I𝒪_U)` is the module `sectionsLimit` of
> compatible systems of pairs of chart functions matched by the transition elements: a global
> section of `𝓛ₙ` is read through its functions on the charts `D(x̄)` and `D(ȳ)`, and the maps of the
> system become the reductions modulo `tⁿ`.

```lean
public def sectionsLimitLinearEquiv :
    sectionsLimit k a φ ≃ₗ[(situation k).A]
      limitGlobalSections (situation k) (levelCoherentAdicSystem k a φ)
```

**`Stacks.Algebraization.NonAlgebraizableExample.nontrivial_limitGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean#L645). The attribute's comment: “lim H^0(U, L\_n) is nonzero when a\_m = 0 for m ≥ 2”.

> **Stacks Project, Tag 0EHE (`lim H⁰(U, 𝓛ₙ) ≠ 0` for the degenerate choice).** When the higher
> coefficients `aₘ` vanish, the module `lim H⁰(U, 𝓛ₙ)` of the system `(𝓛ₙ)` is nonzero.

```lean
public theorem nontrivial_limitGlobalSections (ha : ∀ m : ℕ, 2 ≤ m → a m = 0) :
    Nontrivial (limitGlobalSections (situation k) (levelCoherentAdicSystem k a φ))
```

**`Stacks.Algebraization.NonAlgebraizableExample.subsingleton_limitGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableSectionsLimit.lean#L655). The attribute's comment: “lim H^0(U, L\_n) = 0 for a\_m = 1 and φ(m) = 2^m or m^2”.

> **Stacks Project, Tag 0EHE (`lim H⁰(U, 𝓛ₙ) = 0`).** When every higher coefficient `aₘ` is
> `1` and the exponents are `φ(m) = 2ᵐ` or `φ(m) = m²`, the module `lim H⁰(U, 𝓛ₙ)` of the system
> `(𝓛ₙ)` is zero.

```lean
public theorem subsingleton_limitGlobalSections (ha : ∀ m : ℕ, 2 ≤ m → a m = 1)
    (hφ : (∀ m : ℕ, 2 ≤ m → φ m = 2 ^ m) ∨ (∀ m : ℕ, 2 ≤ m → φ m = m ^ 2)) :
    Subsingleton (limitGlobalSections (situation k) (levelCoherentAdicSystem k a φ))
```

## Tag 0EIM, a definition

[Tag 0EIM](https://stacks.math.columbia.edu/tag/0EIM) in the Stacks Project.

**`Stacks.Algebraization.ExtendsToX`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicSystemsOnComplement.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicSystemsOnComplement.lean#L97).

> **Stacks Project, Tag 0EIM.** A coherent `I`-adic system on `U` extends to `X` when it is
> isomorphic, as an inverse system, to the restriction of a coherent `I`-adic system on `X`.

```lean
public abbrev ExtendsToX (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)) : Prop
```

## Tag 0EIN, a lemma

[Tag 0EIN](https://stacks.math.columbia.edu/tag/0EIN) in the Stacks Project.

**`Stacks.Algebraization.extendsToX_iff_pullback_isCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/BaseAdicCompletion.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/BaseAdicCompletion.lean#L413).

> **Stacks Project, Tag 0EIN.** A coherent `I`-adic system on `U = Spec(A) ∖ V(𝔞)` extends to
> `Spec(A)` if and only if its pullback to `U' = Spec(A') ∖ V(𝔞')`, for `A'` the `I`-adic
> completion of `A`, is the completion of a coherent `𝒪_{U'}`-module.

```lean
public theorem extendsToX_iff_pullback_isCompletion (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)) :
    ExtendsToX S F ↔
      (completionFunctor (completionMap S ⁻¹ᵁ S.U).toScheme
          ((S.Yι.ker.comap S.U.ι).comap (completionMap S ∣_ S.U))).essImage
        ((Stacks.Coherent.coherentAdicPullback (completionMap S ∣_ S.U)
          (S.Yι.ker.comap S.U.ι)).obj F)
```

## Tag 0EHD, an equation

[Tag 0EHD](https://stacks.math.columbia.edu/tag/0EHD) in the Stacks Project.

**`Stacks.Algebraization.limitGlobalSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicSystemsOnComplement.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicSystemsOnComplement.lean#L90).

> **Stacks Project, Tag 0EHD.** The `A`-module `M = limₙ H⁰(U, Fₙ)` associated to a coherent
> adic system on `U`.

```lean
public abbrev limitGlobalSections (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) : ModuleCat.{u} S.A
```

## Tag 0EIP, a definition

[Tag 0EIP](https://stacks.math.columbia.edu/tag/0EIP) in the Stacks Project.

**`Stacks.Algebraization.CanonicallyExtends`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtension.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtension.lean#L77).

> A coherent `I`-adic system on `U` *canonically extends* to `X` when the quasi-coherent
> sheaves associated to its global sections are pro-isomorphic to a coherent `I`-adic system on
> `X`.

```lean
public abbrev CanonicallyExtends (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) : Prop
```

## Tag 0EIR, a lemma

[Tag 0EIR](https://stacks.math.columbia.edu/tag/0EIR) in the Stacks Project.

**`Stacks.Algebraization.isMittagLefflerCategorical_of_canonicallyExtends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean#L178). The attribute's comment: “part (3): the inverse system of global sections of a canonically extending coherent adic system on the open complement satisfies Mittag-Leffler”.

> **Part (3) of Stacks Project, Tag 0EIR.** If a coherent `I`-adic system on the open
> complement `U` canonically extends to `X`, then the inverse system `{H⁰(U, ℱₙ)}` of its modules
> of sections satisfies the Mittag-Leffler condition.

```lean
public theorem isMittagLefflerCategorical_of_canonicallyExtends (h : CanonicallyExtends S F) :
    IsMittagLefflerCategorical (globalSectionsSystem S F)
```

**`Stacks.Algebraization.limitTopologyAgrees_of_canonicallyExtends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean#L436). The attribute's comment: “part (4), the equality of topologies: the limit topology on M is the I-adic topology, for a canonically extending coherent adic system on the open complement”.

> **Part (4) of Stacks Project, Tag 0EIR, second half.** The limit topology on
> `M = limₙ H⁰(U, ℱₙ)` is the `I`-adic topology.

```lean
public theorem limitTopologyAgrees_of_canonicallyExtends (h : CanonicallyExtends S F) :
    LimitTopologyAgrees S F
```

**`Stacks.Algebraization.isAdicComplete_and_finite_adicCompletion_of_canonicallyExtends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionMittagLeffler.lean#L458). The attribute's comment: “part (4), finiteness: M is finite over the I-adic completion of A, for a canonically extending coherent adic system on the open complement”.

> **Part (4) of Stacks Project, Tag 0EIR, first half.** The module `M = limₙ H⁰(U, ℱₙ)` is
> finite over the `I`-adic completion `Â` of `A`: it is `I`-adically complete, so the canonical map
> `M ⟶ M^ = limₙ M/IⁿM` (`AdicCompletion.of`) is an isomorphism of `A`-modules, and its completion
> `M^`, with its canonical structure of `Â`-module, is a finite `Â`-module.

```lean
public theorem isAdicComplete_and_finite_adicCompletion_of_canonicallyExtends
    (h : CanonicallyExtends S F) :
    IsAdicComplete S.I (limitGlobalSections S F) ∧
      Module.Finite (AdicCompletion S.I S.A)
        (AdicCompletion S.I (limitGlobalSections S F : Type u))
```

**`Stacks.Algebraization.canonicalExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean#L77). The attribute's comment: “unique\_extension”.

> **Stacks Project, Tag 0EIR.** A coherent adic system on `X` extending `F`, together with
> a chosen pro-isomorphism from the sheaves associated to the global sections of `F`.

```lean
public noncomputable def canonicalExtension
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (h : CanonicallyExtends S F) :
    Σ G : Stacks.Coherent.CoherentAdicSystems (idealOnX S),
      Stacks.Coherent.diagramToPro (tildeGlobalSectionsSystem S F) ≅
        (Stacks.Coherent.coherentAdicToPro S.X (idealOnX S)).obj G
```

**`Stacks.Algebraization.existsUnique_compatibleIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean#L89). The attribute's comment: “unique\_extension”.

> **Stacks Project, Tag 0EIR.** Two coherent adic extensions of the same pro-object are
> isomorphic by exactly one isomorphism compatible with their chosen pro-isomorphisms.

```lean
public theorem existsUnique_compatibleIso
    (S : AlgebraizationSituation.{u})
    (P : (Ind (Scheme.QuasicoherentModules S.X)ᵒᵖ)ᵒᵖ)
    (G H : Stacks.Coherent.CoherentAdicSystems (idealOnX S))
    (φ : P ≅ (Stacks.Coherent.coherentAdicToPro S.X (idealOnX S)).obj G)
    (ψ : P ≅ (Stacks.Coherent.coherentAdicToPro S.X (idealOnX S)).obj H) :
    ∃! e : G ≅ H,
      φ ≪≫ (Stacks.Coherent.coherentAdicToPro S.X (idealOnX S)).mapIso e = ψ
```

**`Stacks.Algebraization.extendsToX_kerComapSystem_of_canonicallyExtends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CanonicalExtensionUniqueness.lean#L133). The attribute's comment: “part (2): the implication CanonicallyExtends → ExtendsToX, for a coherent adic system on the open complement of an algebraization situation”.

> **Part (2) of Stacks Project, Tag 0EIR.** A coherent `I`-adic system on the open complement
> `U` which canonically extends to `X` is the restriction to `U` of a coherent `I`-adic system
> on `X`.

```lean
public theorem extendsToX_kerComapSystem_of_canonicallyExtends (h : CanonicallyExtends S F) :
    ExtendsToX S (kerComapSystem S F)
```

## Tag 0EIS, a lemma

[Tag 0EIS](https://stacks.math.columbia.edu/tag/0EIS) in the Stacks Project.

**`Stacks.Algebraization.nonempty_pullback_extension_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtensionBaseChange.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtensionBaseChange.lean#L343). The attribute's comment: “the extension pulls back”.

> For `A → A'` flat, if `(G_n)` in `Coh(X, I 𝒪_X)` is pro-isomorphic to `(H⁰(U, F_n)^~)`, then
> `(f^*G_n)` is pro-isomorphic to `(H⁰(U', F'_n)^~)`.

```lean
public theorem nonempty_pullback_extension_iso
    (G : Stacks.Coherent.CoherentAdicSystems (idealOnX S))
    (e : Stacks.Coherent.diagramToPro (tildeGlobalSectionsSystem S F) ≅
      (Stacks.Coherent.coherentAdicToPro S.X (idealOnX S)).obj G) :
    Nonempty (Stacks.Coherent.diagramToPro
        (tildeGlobalSectionsSystem (S.baseChange A') (baseChangeAdicSystem S A' F)) ≅
      (Stacks.Coherent.coherentAdicToPro (S.baseChange A').X (idealOnX (S.baseChange A'))).obj
        (baseChangeCanonicalExtension S A' G))
```

**`Stacks.Algebraization.canonicallyExtends_base_change`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtensionBaseChange.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CanonicalExtensionBaseChange.lean#L364). The attribute's comment: “flat base change of the canonical extension”.

> Let `S` be an algebraization situation: a Noetherian ring `A`
> with ideals `I ⊆ 𝔞`, the affine scheme `X = Spec(A)` and the open complement `U = X ∖ V(𝔞)`. Let
> `(F_n)` be a coherent `I`-adic system on `U` and let `A → A'` be a flat ring map with `A'`
> Noetherian. Put `X' = Spec(A')`, let `U' ⊆ X'` be the inverse image of `U`, let `g : U' ⟶ U` be
> the induced morphism and set `(F'_n) = (g^*F_n)`. If `(F_n)` canonically extends to `X`, then
> `(F'_n)` canonically extends to `X'`.

```lean
public theorem canonicallyExtends_base_change (h : CanonicallyExtends S F) :
    CanonicallyExtends (S.baseChange A') (baseChangeAdicSystem S A' F)
```

## Tag 0EHH, a lemma

[Tag 0EHH](https://stacks.math.columbia.edu/tag/0EHH) in the Stacks Project.

**`Stacks.Algebraization.essImage_completionFunctor_of_finite_limit_images`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerAlgebraization.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerAlgebraization.lean#L84). The attribute's comment: “the in-particular clause, that over an I-adically complete A the system is the completion of a coherent 𝒪\_U-module, i.e. lies in the essential image of the completion functor of U, which is condition (2) of 0EIL; deduced from the canonical extension of the main clause by part (2) of 0EIR and the chain of 0EIL”.

> **The in-particular clause of Stacks Project, Tag 0EHH.** In an algebraization situation with
> `A` moreover `I`-adically complete, a coherent `I`-adic system `(ℱₙ)` on the open complement `U`
> whose global sections have Mittag-Leffler, whose limit topology on `M = limₙ H⁰(U, ℱₙ)` is the
> `I`-adic topology, and whose projections `M → H⁰(U, ℱₙ)` have finite image, is the completion of a
> coherent `𝒪_U`-module.
>
> The system extends canonically to `X` by
> `Stacks.Algebraization.canonicallyExtends_of_finite_limit_images`, part (2) of Stacks 0EIR turns
> that into extendability to `X`, and adic completeness then runs the chain of Stacks 0EIL: an
> extendable system is the restriction of a completion on `X`, hence the completion of a module
> restricted from `X`, hence a completion on `U`.

```lean
public theorem essImage_completionFunctor_of_finite_limit_images
    (S : AlgebraizationSituation.{u}) [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hML : IsMittagLefflerCategorical (globalSectionsSystem S F))
    (htop : (⨅ n : ℕ, TopologicalSpace.induced
      (fun x : limitGlobalSections S F =>
        (limit.π (globalSectionsSystem S F) (op n)).hom x) ⊥) =
        S.I.adicModuleTopology (limitGlobalSections S F))
    (hfinite : ∀ n : ℕ, Module.Finite S.A
      (LinearMap.range (limit.π (globalSectionsSystem S F) (op n)).hom)) :
    (completionFunctor S.U.toScheme (idealOnOpen S)).essImage F
```

**`Stacks.Algebraization.canonicallyExtends_of_finite_limit_images`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerCriterion.lean, line 1098](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerCriterion.lean#L1098). The attribute's comment: “canonical extension”.

> The Mittag-Leffler, topology, and finite-image hypotheses imply canonical
> extension of a coherent adic system to `X`.

```lean
public theorem canonicallyExtends_of_finite_limit_images
    (S : Stacks.Algebraization.AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (Stacks.Algebraization.idealOnOpen S))
    (hML : IsMittagLefflerCategorical (Stacks.Algebraization.globalSectionsSystem S F))
    (htop : (⨅ n : ℕ, TopologicalSpace.induced
      (fun x : Stacks.Algebraization.limitGlobalSections S F =>
        (limit.π (Stacks.Algebraization.globalSectionsSystem S F) (op n)).hom x) ⊥) =
        S.I.adicModuleTopology (Stacks.Algebraization.limitGlobalSections S F))
    (hfinite : ∀ n : ℕ, Module.Finite S.A
      (LinearMap.range (limit.π (Stacks.Algebraization.globalSectionsSystem S F) (op n)).hom)) :
    Stacks.Algebraization.CanonicallyExtends S F
```

## Tag 0DXW, a lemma

[Tag 0DXW](https://stacks.math.columbia.edu/tag/0DXW) in the Stacks Project.

**`Stacks.Algebraization.canonicallyExtends_and_isCompletion_of_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalEquivalence.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalEquivalence.lean#L389).

> **[Stacks, Tag 0DXW].** Let `S` be the standing situation of [Stacks, Tag 0EHC] and let
> `(F_n)` be an object of `Coh(U, I𝒪_U)`. Assume
>
> 1. `I = (f)` is principal with `f` a nonzerodivisor of `A`,
> 2. every `F_n` is a finite locally free `𝒪_U/Iⁿ𝒪_U`-module, and
> 3. `H¹_𝔞(A/fA)` and `H²_𝔞(A/fA)` are finite `A`-modules.
>
> Then `(F_n)` extends canonically to `X = Spec(A)`; and if moreover `A` is `f`-adically complete,
> `(F_n)` is the completion of a coherent `𝒪_U`-module.
>
> Hypothesis (2) is used at the stalks, where a finite locally free `𝒪_U/Iⁿ𝒪_U`-module is a finite
> free module over the local ring modulo the `n`-th power of the stalk of `I𝒪_U`; that is
> `Stacks.Algebraization.HasFiniteFreeStalks`.
>
> The three conditions (a), (b), (c) of the Mittag-Leffler criterion [Stacks, Tag 0EHH] come from
> `Stacks.Algebraization.canonicallyExtends_of_principal_shortExactSequences`, whose two
> hypotheses are discharged here: the short exact sequences
> `0 → F_n → F_{n+1} → F_1 → 0` by
> `Stacks.Algebraization.hasPrincipalShortExactSequences_of_nonzerodivisor`, and the finiteness of
> `H⁰(U, F₁)` and `H¹(U, F₁)` by
> `Stacks.Algebraization.finite_openCohomology_of_hasFiniteFreeStalks`. The second clause follows
> from the first along the chain of [Stacks, Tag 0EIL].

```lean
theorem canonicallyExtends_and_isCompletion_of_principal
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) {f : S.A}
    (hI : S.I = Ideal.span {f}) (hnzd : f ∈ nonZeroDivisors S.A)
    (hH1 : Module.Finite S.A (specialFibreLocalCohomology S f 1))
    (hH2 : Module.Finite S.A (specialFibreLocalCohomology S f 2))
    (hfree : HasFiniteFreeStalks S F) :
    CanonicallyExtends S F ∧
      (IsAdicComplete (Ideal.span {f}) S.A →
        (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage
          (kerComapSystem S F))
```

**`Stacks.Algebraization.canonicallyExtends_of_principal_shortExactSequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalNonzerodivisor.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalNonzerodivisor.lean#L511). The attribute's comment: “first clause (canonical extension) only; conditions (a), (b), (c) of 0EHH are proved, but hypotheses (2) and (3) of the source are replaced by the consequences its proof draws from them, namely the short exact sequences 0 → Fₙ → F₍ₙ₊₁₎ → F₁ → 0 and the finiteness of H⁰(U, F₁) and H¹(U, F₁)”.

> **Stacks Project, Tag 0DXW, first clause.** Let `S` be an algebraization situation whose ideal
> `I` is the principal ideal generated by `f ∈ A`, and let `(F_n)` be a coherent `I`-adic system on
> the open complement `U`. If the system has the short exact sequences
> `0 → F_n → F_{n+1} → F_1 → 0` of the source's proof, and if `H⁰(U, F_1)` and `H¹(U, F_1)` are
> finite `A`-modules, then `(F_n)` extends canonically to `X = Spec(A)`.
>
> The three hypotheses (a), (b), (c) of the Mittag-Leffler criterion Stacks 0EHH are proved here:
> (b) from the degree-zero half of Stacks 0EHA, (a) from Stacks 0BLC, and (c) by the source's
> induction on the short exact sequences.
>
> The source's hypotheses (2) and (3) are replaced by the two consequences its proof uses. Finite
> local freeness of `F_n` over `𝒪_U/f^n𝒪_U` and the nonzerodivisor property of `f` are used only
> to produce the short exact sequences `0 → F_n → F_{n+1} → F_1 → 0`, which is the hypothesis `h`;
> and the finiteness of `H¹_𝔞(A/fA)` and `H²_𝔞(A/fA)` is used only to produce the finiteness of
> `H⁰(U, F_1)` and `H¹(U, F_1)`, by Local Cohomology 0BK0 and 0BLT, which are the hypotheses `h0`
> and `h1`. Neither derivation is carried out here.
>
> The source's second clause, algebraizability over an `I`-adically complete `A`, is
> `Stacks.Algebraization.isCompletionNearClosed_of_principal_shortExactSequences`.
>
> Stacks 0DXW itself, with the source's own hypotheses and both of its clauses, is
> `Stacks.Algebraization.canonicallyExtends_and_isCompletion_of_principal`, which derives the two
> hypotheses below from them.

```lean
theorem canonicallyExtends_of_principal_shortExactSequences (f : S.A)
    (hI : S.I = Ideal.span {f}) (h : HasPrincipalShortExactSequences S F f)
    (h0 : Module.Finite S.A ((globalSectionsSystem S F).obj (op 0)))
    (h1 : Module.Finite S.A ((openCohomologyFunctor S 1).obj (systemObj S F 0))) :
    CanonicallyExtends S F
```

**`Stacks.Algebraization.canonicallyExtends_and_isCompletion_of_principal_nonzerodivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalNonzerodivisorWhole.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalNonzerodivisorWhole.lean#L200). The attribute's comment: “both clauses under the source's own conditions (1), (2) and (3): for I = (f) generated by a nonzerodivisor, with every term finite locally free over the infinitesimal neighbourhood it is annihilated by, and with H¹\_𝔞(A/fA) and H²\_𝔞(A/fA) finite, the system extends canonically to X, and over an I-adically complete A it is the completion of a coherent O\_U-module”.

> **Stacks Project, Tag 0DXW.** Let `S` be an algebraization situation and let `(F_n)` be a
> coherent `I`-adic system on the open complement `U`. Assume
>
> 1. `I = (f)` is generated by a nonzerodivisor `f ∈ 𝔞`,
> 2. every term of the system is finite locally free over the infinitesimal neighbourhood it is
>    annihilated by,
> 3. `H¹_𝔞(A/fA)` and `H²_𝔞(A/fA)` are finite `A`-modules.
>
> Then `(F_n)` extends canonically to `X = Spec(A)`, and if `A` is `I`-adically complete then
> `(F_n)` is the completion of a coherent `𝒪_U`-module.
>
> Conditions (1) and (2) give the short exact sequences `0 → F_n → F_{n+1} → F_1 → 0` of the
> source's proof (`Stacks.Algebraization.hasPrincipalShortExactSequences_of_locallyFree`), and
> all three give the finiteness of `H⁰(U, F_1)` and `H¹(U, F_1)`
> (`Stacks.Algebraization.finite_complementCohomologyBase_firstTerm`). The Mittag-Leffler criterion
> Stacks 0EHH turns those into the first clause
> (`Stacks.Algebraization.canonicallyExtends_of_principal_shortExactSequences`) and the chain of
> Stacks 0EIL into the second
> (`Stacks.Algebraization.isCompletionNearClosed_of_principal_shortExactSequences`).

```lean
theorem canonicallyExtends_and_isCompletion_of_principal_nonzerodivisor
    (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) (f : S.A)
    (hI : S.I = Ideal.span {f}) (hf : f ∈ nonZeroDivisors S.A)
    (hfree : IsFiniteLocallyFreeAdic (idealOnOpen S) F)
    (h₁ : Module.Finite S.A (localCohomologyBaseQuotient S f 1))
    (h₂ : Module.Finite S.A (localCohomologyBaseQuotient S f 2)) :
    CanonicallyExtends S F ∧
      (IsAdicComplete (Ideal.span {f}) S.A →
        (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (kerComapSystem S F))
```

## Tag 0EHI, a remark

[Tag 0EHI](https://stacks.math.columbia.edu/tag/0EHI) in the Stacks Project.

**`Stacks.LocalCohomology.finite_localCohomology_quotient_span_iff_two_lt_depth_add_height`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/PrincipalQuotientFiniteness.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/PrincipalQuotientFiniteness.lean#L415).

> **Stacks Project, Tag 0EHI.** In Situation 0EHC, let `I = (f)` be principal for a
> nonzerodivisor `f ∈ 𝔞`, as in Tag 0DXW. The remark has three assertions, conjoined here into one
> statement because they are one remark; the first is quantified over the dualizing complexes of
> `A`, and the other two carry the remark's own hypotheses as antecedents, exactly as the source
> states them.
>
> * The parenthetical: if `A` has a dualizing complex, then `A` is universally catenary and the
>   formal fibres of its local rings are Cohen--Macaulay. (Tags 0A80, 0A7G, 0AWY.)
>
> * The equivalence: if `A` is universally catenary with Cohen--Macaulay formal fibres, then
>   `H¹_𝔞(A/fA)` and `H²_𝔞(A/fA)` are finite `A`-modules if and only if
>
>     `depth((A/f)_𝔭) + dim((A/𝔭)_𝔮) > 2`
>
>   for all `𝔭 ∈ V(f) \ V(𝔞)` and `𝔮 ∈ V(𝔭) ∩ V(𝔞)`. This is the Local Cohomology Theorem 0BJV at
>   the cutoff `s_{A,𝔞}(A/fA)` of Tag 0BJR: the displayed inequality says exactly that the cutoff
>   exceeds `2`, the pairs with `𝔭 ∉ V(f)` contributing nothing because `(A/fA)_𝔭` vanishes there.
>
> * The example: if moreover `A/fA` satisfies Serre's condition `(S₂)` and every irreducible
>   component of `Z = V(𝔞)` has codimension at least `3` in `Y = Spec(A/fA)`, then `H¹_𝔞(A/fA)`
>   and `H²_𝔞(A/fA)` are finite.
>
> The two cohomology modules are the local cohomology of `A/fA` with support in `V(𝔞)`, in the
> spelling Tag 0BJV uses. `depth((A/f)_𝔭)` and `dim((A/𝔭)_𝔮)` are spelled as in the cutoff of Tag
> 0BJR, namely as `Module.depth` of `(A/fA)_𝔭` over `A_𝔭` and as the height of the image of `𝔮` in
> `A/𝔭`. The irreducible components of `Z` are the minimal primes of `𝔞`, and the codimension in
> `Y` of the component cut out by such a prime `𝔷` is the height of the image of `𝔷` in
> `A/fA`.
>
> The two hypotheses `_hfa : f ∈ 𝔞` and `_hf : f ∈ nonZeroDivisors A` are the situation the source
> places the remark in — Tag 0DXW's `I = (f)` principal, generated by a nonzerodivisor of `𝔞`. They
> are recorded so the statement has the source's scope and no more; the argument itself never uses
> them, which is why they are underscored.

```lean
public theorem finite_localCohomology_quotient_span_iff_two_lt_depth_add_height
    (A : Type u) [CommRing A] [IsNoetherianRing A] (a : Ideal A) (f : A) (_hfa : f ∈ a)
    (_hf : f ∈ nonZeroDivisors A) :
    (∀ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K →
        Ring.IsUniversallyCatenary A ∧
          ∀ p : PrimeSpectrum A,
            FormalFibersAreCohenMacaulay (Localization.AtPrime p.asIdeal)) ∧
      (Ring.IsUniversallyCatenary A →
        (∀ p : PrimeSpectrum A,
            FormalFibersAreCohenMacaulay (Localization.AtPrime p.asIdeal)) →
        ((Module.Finite A
              (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (a : Set A))
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A (A ⧸ Ideal.span {f}))) 1) ∧
            Module.Finite A
              (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (a : Set A))
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A (A ⧸ Ideal.span {f}))) 2) ↔
            ∀ p q : PrimeSpectrum A, f ∈ p.asIdeal → ¬ a ≤ p.asIdeal → a ≤ q.asIdeal →
              p.asIdeal ≤ q.asIdeal →
                2 < Module.depth (Localization.AtPrime p.asIdeal)
                      (maximalIdeal (Localization.AtPrime p.asIdeal))
                      (LocalizedModule p.asIdeal.primeCompl (A ⧸ Ideal.span {f})) +
                    (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)).height) ∧
          (PropertySkRing (A ⧸ Ideal.span {f}) 2 →
            (∀ z ∈ a.minimalPrimes,
              3 ≤ (z.map (Ideal.Quotient.mk (Ideal.span {f}))).height) →
            Module.Finite A
                (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (a : Set A))
                  ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                    (ModuleCat.of A (A ⧸ Ideal.span {f}))) 1) ∧
              Module.Finite A
                (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (a : Set A))
                  ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                    (ModuleCat.of A (A ⧸ Ideal.span {f}))) 2))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.16, Tag 0DXS](https://stacks.math.columbia.edu/tag/0DXS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
