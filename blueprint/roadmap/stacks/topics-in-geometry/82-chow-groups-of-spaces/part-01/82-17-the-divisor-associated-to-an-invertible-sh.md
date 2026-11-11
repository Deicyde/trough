---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.divisorCycleOfSection, AlgebraicGeometry.Space.divisorCycleOfSectionOfGenerating, AlgebraicGeometry.Space.firstChernClassCapFundamental, AlgebraicGeometry.Space.firstChernClassCapFundamental_eq, AlgebraicGeometry.Space.sectionWeilDivisor, AlgebraicGeometry.Space.weilDivisorOfInvertibleSheaf, AlgebraicGeometry.Space.chowClass_sectionWeilDivisor, AlgebraicGeometry.Space.zeroSchemeCycleCoeff_mem_cyclesOfDimension
statement: formalized
proof: formalized
---

# 82.17 The divisor associated to an invertible sheaf

Section 82.17 of the Stacks Project, [Tag 0EQD](https://stacks.math.columbia.edu/tag/0EQD). 4 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQE, a definition

[Tag 0EQE](https://stacks.math.columbia.edu/tag/0EQE) in the Stacks Project.

**`AlgebraicGeometry.Space.divisorCycleOfSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean#L339). The attribute's comment: “part (1): div\_ℒ(s) = ∑ ord\_\{Z,ℒ}(s) [Z] as an element of Z\_\{n-1}(X); the δ-dimension of a prime divisor is n-1 by Stacks 0EPZ, whose dimension-function hypotheses d and hd are Stacks 0EDN, carried; local finiteness of the prime divisors with ord ≠ 0 is Stacks 0EPS, the hypothesis hfin; the ratio family at the generic points is the parameter ratio, as in Stacks 0EPR and 0EPU”.

> **Stacks 0EQE, part (1).** The *Weil divisor associated to a nonzero meromorphic section `s`
> of `ℒ`*, that is `div_ℒ(s) = ∑_Z ord_{Z,ℒ}(s) [Z]` of Stacks 0EPU, as an element of
> `Z_{n-1}(X)`: it is an `(n-1)`-cycle because a prime divisor of an integral good algebraic
> space of δ-dimension `n` has δ-dimension `n - 1` by Stacks 0EPZ.
>
> Local finiteness of the prime divisors with `ord_{Z,ℒ}(s) ≠ 0` is Stacks 0EPS, here the
> hypothesis `hfin`; `AlgebraicGeometry.Space.divisorCycleOfSectionOfGenerating` discharges it
> from a nonempty open subspace over which `s` generates `ℒ`.

```lean
def divisorCycleOfSection (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    CycleGroup D sX (n - 1)
```

**`AlgebraicGeometry.Space.divisorCycleOfSectionOfGenerating`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean#L377). The attribute's comment: “part (1): div\_ℒ(s) in Z\_\{n-1}(X), with local finiteness supplied by Stacks 0EPS from the open subspace U over which s generates ℒ; the δ-dimension of a prime divisor is n-1 by Stacks 0EPZ, whose dimension-function hypotheses d and hd are Stacks 0EDN, carried”.

> **Stacks 0EQE, part (1).** The Weil divisor `div_ℒ(s) = ∑_Z ord_{Z,ℒ}(s) [Z]` of a nonzero
> meromorphic section `s` of `ℒ` as an element of `Z_{n-1}(X)`, with the local finiteness of its
> support supplied by Stacks 0EPS from a nonempty open subset of `|X|` containing the generic
> point of no prime divisor along which `s` has nonzero order — the open subspace over which `s`
> generates `ℒ`.

```lean
def divisorCycleOfSectionOfGenerating
    (hN : HasEtaleLocalProperty D.site D.base D.base_mem X
      (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (U : Set (points D.site D.base D.base_mem X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hgen : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W ≠ 0 →
        W.genericPoint D.site D.base D.base_mem X ∈ Uᶜ)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    CycleGroup D sX (n - 1)
```

**`AlgebraicGeometry.Space.firstChernClassCapFundamental`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean#L463). The attribute's comment: “part (2): c₁(ℒ) ∩ [X] = class of div\_ℒ(s) in CH\_\{n-1}(X); CH\_\{n-1}(X) together with its class map and its principal divisors is carried as the ChowTarget parameter chow, standing in for Stacks 0EQ6 parts (2)-(4); independence of the chosen section s is firstChernClassCapFundamental\_eq”.

> **Stacks 0EQE, part (2).** The *Weil divisor associated to `ℒ`*, that is
> `c₁(ℒ) ∩ [X] = [div_ℒ(s)] ∈ CH_{n-1}(X)`, the class of the Weil divisor of a nonzero
> meromorphic section `s` of `ℒ`.
>
> The class is independent of the chosen section:
> `AlgebraicGeometry.Space.firstChernClassCapFundamental_eq`. The Chow group `CH_{n-1}(X)` is the
> parameter `chow`, only part (1) of Stacks 0EQ6 being available in this library.

```lean
def firstChernClassCapFundamental
    (chow : ChowTarget.{u, w, v} D sX hX (n - 1) CH)
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x)
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) : CH
```

**`AlgebraicGeometry.Space.firstChernClassCapFundamental_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/InvertibleSheafDivisor.lean#L490). The attribute's comment: “part (2), well-definedness: c₁(ℒ) ∩ [X] is independent of the chosen nonzero meromorphic section, by Stacks 0EPT; the principal divisor div(f) of Stacks 0ENP is not carried here, so that the cycle div(f) belongs to the principal divisors of the ChowTarget parameter — the input of Stacks 0EQ6 part (1) — is the hypothesis hprincipal, and Stacks 0EQ6 parts (2) and (4) are the parameter's field cls\_cycleFamilySum\_eq\_zero”.

> **Stacks 0EQE, part (2), well-definedness.** The class `c₁(ℒ) ∩ [X]` does not depend on the
> chosen nonzero meromorphic section of `ℒ`.
>
> If the ratios of `s` and `s'` at the generic points of the prime divisors differ by the image of
> a rational function `f`, then `div_ℒ(s) - div_ℒ(s') = div(f)` by Stacks 0EPT, and `div(f)` is
> rationally equivalent to zero by Stacks 0EQ6: it is the one-member family `∑ (i_j)_* div(f_j)`
> of part (1), taken on `X` itself. That `div(f)` is one of the principal divisors of the Chow
> group parameter is the hypothesis `hprincipal`, the principal divisor of Stacks 0ENP not being
> available in this library.

```lean
theorem firstChernClassCapFundamental_eq
    (chow : ChowTarget.{u, w, v} D sX hX (n - 1) CH)
    (s s' : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hfin' : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s' ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x)
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (emb : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      rationalFunctions D.site D.base D.base_mem hX.1 →+*
        W.genericTotalFractionRing D.site D.base D.base_mem hX.1 hdec)
    (f : rationalFunctions D.site D.base D.base_mem hX.1)
    (hf : ∀ W : PrimeDivisor D.site D.base D.base_mem X, IsUnit (emb W f))
    (hratio : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      ((ratio W s : W.genericTotalFractionRing D.site D.base D.base_mem hX.1 hdec)) =
        emb W f * (ratio W s' : W.genericTotalFractionRing D.site D.base D.base_mem hX.1 hdec))
    (hprincipal : ∃ (Y : IntegralClosedSubspace D.site D.base D.base_mem X)
      (c : CycleGroup D (Y.subspace.ι ≫ sX) (n - 1)), c ∈ chow.principalDivisors Y ∧
        ∀ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
          (integralClosedSubspacePushforward D sX hX Y (n - 1) c).1 Z =
            principalDivisorCycleCoefficients D sX hX hdec emb f hf Z) :
    firstChernClassCapFundamental D sX hX hdec L chow s ratio hfin hint d hd hn =
      firstChernClassCapFundamental D sX hX hdec L chow s' ratio hfin' hint d hd hn
```

**`AlgebraicGeometry.Space.sectionWeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean#L148). The attribute's comment: “part (1): div\_ℒ(s) = ∑ ord\_\{Z,ℒ}(s) [Z] as an element of Z\_\{n-1}(X), for X/B good and integral with n = dim\_δ(X), ℒ invertible and s a nonzero meromorphic section; ord\_\{Z,ℒ}(s) at the generators of Stacks 0EPR, local finiteness by Stacks 0EPS for the section s, the δ-dimension n-1 of a prime divisor by Stacks 0EPZ with the dimension function of Stacks 0EDN, and the properties of the henselian local rings by Stacks 0ENK, all proved”.

> **Stacks 0EQE, part (1).** In Situation 0EDT let `X/B` be good, let `X` be integral with
> `n = dim_δ(X)` and let `ℒ` be an invertible `𝒪_X`-module. The *Weil divisor associated to a
> nonzero meromorphic section `s` of `ℒ`*, the `(n-1)`-cycle
>
>   `div_ℒ(s) = ∑ ord_{Z,ℒ}(s) [Z] ∈ Z_{n-1}(X)`,
>
> the sum over the prime divisors `Z` of `X`, `ord_{Z,ℒ}(s)` being the order of vanishing of
> Stacks 0EPR (`AlgebraicGeometry.Space.sectionWeilDivisor_apply_toIntegralClosedSubspace`).

```lean
def sectionWeilDivisor {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L)
    (hs : s ≠ 0) :
    CycleGroup D sX (n - 1)
```

**`AlgebraicGeometry.Space.weilDivisorOfInvertibleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean#L234). The attribute's comment: “part (2): c₁(ℒ) ∩ [X] = the class of div\_ℒ(s) in CH\_\{n-1}(X) = Z\_\{n-1}(X)/∼\_rat (Stacks 0EQ6), for a nonzero meromorphic section s of ℒ, which exists by Stacks 0EPQ; it is the class of div\_ℒ(s) for every nonzero s by chowClass\_sectionWeilDivisor”.

> **Stacks 0EQE, part (2).** In Situation 0EDT let `X/B` be good, let `X` be integral with
> `n = dim_δ(X)` and let `ℒ` be an invertible `𝒪_X`-module. The *Weil divisor associated to `ℒ`*,
>
>   `c₁(ℒ) ∩ [X] = class of div_ℒ(s) ∈ CH_{n-1}(X)`,
>
> for the nonzero meromorphic section `s` of `ℒ` of Stacks 0EPQ
> (`AlgebraicGeometry.Space.regularMeromorphicSection`); the class does not depend on the choice
> of `s` (`AlgebraicGeometry.Space.chowClass_sectionWeilDivisor`).

```lean
def weilDivisorOfInvertibleSheaf {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    chowGroup.{v} D sX hX (n - 1)
```

**`AlgebraicGeometry.Space.chowClass_sectionWeilDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/WeilDivisorOfInvertibleSheaf.lean#L254). The attribute's comment: “part (2), well-definedness: the class of div\_ℒ(s) in CH\_\{n-1}(X) is c₁(ℒ) ∩ [X] for every nonzero meromorphic section s, by Stacks 0EPT, the principal divisor div(f) of the ratio being rationally equivalent to zero in the sense of Stacks 0EQ6”.

> **Stacks 0EQE, part (2), well-definedness.** `c₁(ℒ) ∩ [X]` is the class of `div_ℒ(s)` in
> `CH_{n-1}(X)` for *every* nonzero meromorphic section `s` of `ℒ`.

```lean
theorem chowClass_sectionWeilDivisor {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L)
    (hs : s ≠ 0) :
    chowClass.{v} D sX hX (n - 1) (sectionWeilDivisor D sX hX hint L hL hn s hs) =
      weilDivisorOfInvertibleSheaf.{v} D sX hX hint L hL hn
```

## Tag 0EQF, a lemma

[Tag 0EQF](https://stacks.math.columbia.edu/tag/0EQF) in the Stacks Project.

**`AlgebraicGeometry.Space.zeroSchemeCycleCoeff_mem_cyclesOfDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean#L201). The attribute's comment: “[Z(s)]\_k is a k-cycle, so that at k = n - 1 the right side of both identities is an element of Z\_\{n-1}(X); the multiplicity of Stacks 0EE9 is read at the chosen geometric representative γ, which by Stacks 0EE1 (geometricLength\_eq\_of\_image\_eq) does not change its value, and local finiteness of the coefficient family is the argument hfin, a property of the input datum (ℒ, s, γ), as it is for div\_ℒ(s) in Stacks 0EQE part (1) and for divisorOfSection in Stacks 0EPU part (1)”.

> **Stacks 0EQF.** The right side of both identities of the source is a `k`-cycle: the
> coefficient family of `[Z(s)]_k` lies in `Z_k(X)`.
>
> The δ-dimension clause holds by construction, the coefficient of Stacks 0EE9 at an integral
> closed subspace of δ-dimension other than `k` being zero. Local finiteness is the argument
> `hfin`, a property of the input datum `(ℒ, s, γ)`, as it is for `div_ℒ(s)` on the other side.

```lean
theorem zeroSchemeCycleCoeff_mem_cyclesOfDimension
    (hfin : LocallyFinite fun Z : IntegralClosedSubspace D.site D.base D.base_mem X =>
      if zeroSchemeCycleCoeff D sX hX L s k γ Z = 0 then ∅
      else subspacePointSet D.site D.base D.base_mem X Z.subspace) :
    zeroSchemeCycleCoeff D sX hX L s k γ ∈ cyclesOfDimension D sX k
```

**`AlgebraicGeometry.Space.divisorCycleOfSection_eq_zeroSchemeCycle_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean#L281). The attribute's comment: “first conclusion REDUCED to its coefficients: div\_ℒ(s) = [Z(s)]\_\{n-1} in Z\_\{n-1}(X) holds IF AND ONLY IF it holds at every prime divisor, where div\_ℒ(s) is Stacks 0EQE part (1) and [Z(s)]\_\{n-1} is Stacks 0EE9 at the chosen geometric representative γ; what is proved here is that the two coefficient families agree away from the prime divisors, by Stacks 0EQE part (1) and Stacks 0EPZ. The coefficient identity ord\_\{Z,ℒ}(s) = m\_\{Z,Z(s)} AT a prime divisor — the right-hand side of this equivalence — is proved separately, in GlobalSectionDivisorCycle.lean, for the canonical meromorphic section of s and with no chart carried”.

> **Stacks 0EQF, the identity in `Z_{n-1}(X)`, reduced to its coefficients at the prime
> divisors.** In Situation 0EDT let `X/B` be good, let `X` be integral with `n = dim_δ(X)`, let
> `ℒ` be an invertible `𝒪_X`-module, let `s ∈ Γ(X, ℒ)` and let `σ` be a nonzero meromorphic
> section of `ℒ`. Then
>
> `div_ℒ(σ) = [Z(s)]_{n-1}` in `Z_{n-1}(X)`
>
> holds exactly when it holds coefficientwise at every prime divisor of `X`, that is when
> `ord_{Z,ℒ}(σ)` is the multiplicity of `Z` in `Z(s)` for every prime divisor `Z ⊆ X`.
>
> Both sides are coefficient families on the integral closed subspaces of `X`, and away from the
> prime divisors both vanish: the coefficient of `div_ℒ(σ)` at an integral closed subspace whose
> point set does not have codimension one is zero by Stacks 0EQE, part (1), and such a subspace
> has δ-dimension other than `n - 1` by Stacks 0EPZ, so its coefficient in `[Z(s)]_{n-1}` is zero
> too. That is the whole content of the reduction. The right-hand side — the coefficient identity
> at a prime divisor — is proved, for the canonical meromorphic section of `s`, by
> `AlgebraicGeometry.Space.invertibleDivisorCoefficients_globalSection_toIntegralClosedSubspace`.

```lean
theorem divisorCycleOfSection_eq_zeroSchemeCycle_iff (_hL : IsInvertibleSheaf D sX hX L)
    (hfin : LocallyFinite fun Z : IntegralClosedSubspace D.site D.base D.base_mem X =>
      if zeroSchemeCycleCoeff D sX hX L s (n - 1) γ Z = 0 then ∅
      else subspacePointSet D.site D.base D.base_mem X Z.subspace) :
    divisorCycleOfSection D sX hX hdec L σ ratio hDv hint dimF hdimF hn =
        zeroSchemeCycle D sX hX L s (n - 1) γ hfin ↔
      ∀ W : PrimeDivisor D.site D.base D.base_mem X,
        divisorCoefficients.{u, u} D.site D.base D.base_mem hX.1 hdec L σ ratio W =
          zeroSchemeCycleCoeff D sX hX L s (n - 1) γ
            (W.toIntegralClosedSubspace D.site D.base D.base_mem)
```

**`AlgebraicGeometry.Space.firstChernClassCapFundamental_eq_cls_zeroSchemeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DivisorOfSectionCycle.lean#L325). The attribute's comment: “second conclusion: c₁(ℒ) ∩ [X] = [Z(s)]\_\{n-1} in CH\_\{n-1}(X), where c₁(ℒ) ∩ [X] is Stacks 0EQE part (2) — the class of div\_ℒ(s) in the ChowTarget parameter standing in for Stacks 0EQ6; this is the source's own derivation of its second conclusion FROM its first, so the argument heq is the FIRST conclusion of this tag (reduced to the prime divisors by divisorCycleOfSection\_eq\_zeroSchemeCycle\_iff) and not this theorem's own conclusion”.

> **Stacks 0EQF, the identity in `CH_{n-1}(X)`, from the identity in `Z_{n-1}(X)`.** In the
> situation above, if
>
> `div_ℒ(σ) = [Z(s)]_{n-1}` in `Z_{n-1}(X)`,
>
> which is the first conclusion of the source and the hypothesis `heq`, then
>
> `c₁(ℒ) ∩ [X] = [Z(s)]_{n-1}` in `CH_{n-1}(X)`.
>
> This is the source's own derivation of its second conclusion from its first: `c₁(ℒ) ∩ [X]` is by
> Stacks 0EQE, part (2), the class of `div_ℒ(σ)` for a nonzero meromorphic section `σ` of `ℒ`, a
> class independent of `σ` by
> `AlgebraicGeometry.Space.firstChernClassCapFundamental_eq`, so the second identity is the image
> of the first under the class map of the Chow group.

```lean
theorem firstChernClassCapFundamental_eq_cls_zeroSchemeCycle
    (_hL : IsInvertibleSheaf D sX hX L) {CH : Type w} [AddCommGroup CH]
    (chow : ChowTarget.{u, w, v} D sX hX (n - 1) CH)
    (hfin : LocallyFinite fun Z : IntegralClosedSubspace D.site D.base D.base_mem X =>
      if zeroSchemeCycleCoeff D sX hX L s (n - 1) γ Z = 0 then ∅
      else subspacePointSet D.site D.base D.base_mem X Z.subspace)
    (heq : divisorCycleOfSection D sX hX hdec L σ ratio hDv hint dimF hdimF hn =
      zeroSchemeCycle D sX hX L s (n - 1) γ hfin) :
    firstChernClassCapFundamental D sX hX hdec L chow σ ratio hDv hint dimF hdimF hn =
      chow.cls (zeroSchemeCycle D sX hX L s (n - 1) γ hfin)
```

**`AlgebraicGeometry.Space.sectionWeilDivisor_eq_zeroSchemeCycle_and_weilDivisorOfInvertibleSheaf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GlobalSectionDivisorCycle.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GlobalSectionDivisorCycle.lean#L380). The attribute's comment: “both identities: div\_ℒ(s) = [Z(s)]\_\{n-1} in Z\_\{n-1}(X) and c₁(ℒ) ∩ [X] = [Z(s)]\_\{n-1} in CH\_\{n-1}(X), for X/B good and integral with n = dim\_δ(X), ℒ invertible and s a nonzero global section; div\_ℒ(s) and c₁(ℒ) ∩ [X] are Stacks 0EQE parts (1) and (2) with every ingredient constructed, CH\_\{n-1}(X) is Stacks 0EQ6, [Z(s)]\_\{n-1} is Stacks 0EE9 of the zero scheme of Stacks 0845 at the canonical geometric representatives; nothing carried”.

> **Stacks 0EQF.** In Situation 0EDT let `X/B` be good, let `X` be integral with
> `n = dim_δ(X)`, let `ℒ` be an invertible `𝒪_X`-module and let `s ∈ Γ(X, ℒ)` be a nonzero global
> section. Then
>
> `div_ℒ(s) = [Z(s)]_{n-1}` in `Z_{n-1}(X)`  and  `c₁(ℒ) ∩ [X] = [Z(s)]_{n-1}` in `CH_{n-1}(X)`.
>
> `div_ℒ(s)` is the Weil divisor of Stacks 0EQE, part (1), of the meromorphic section of `ℒ` that
> `s` is; `c₁(ℒ) ∩ [X]` is Stacks 0EQE, part (2), in the Chow group `CH_{n-1}(X)` of Stacks 0EQ6;
> and `[Z(s)]_{n-1}` is the cycle of Stacks 0EE9 of the zero scheme of Stacks 0845, its
> multiplicities read at the canonical geometric representative of each point — by Stacks 0EE1
> any representatives lying over the points give the same cycle, and
> `sectionWeilDivisor_eq_zeroSchemeCycle_and_weilDivisorOfInvertibleSheaf_eq_of_liesOver` states
> the identities for all of them. That `[Z(s)]_{n-1}` is an `(n-1)`-cycle is part of the
> conclusion: its coefficients are those of `div_ℒ(s)`.

```lean
theorem sectionWeilDivisor_eq_zeroSchemeCycle_and_weilDivisorOfInvertibleSheaf_eq
    {s : L.sections} (hs : s ≠ 0) :
    sectionWeilDivisor D sX hX hint L hL hn
        (globalSectionMeromorphic D.site D.base D.base_mem hX.1 L s)
        (globalSectionMeromorphic_ne_zero_of_isInvertibleSheaf D sX hX L hL hs) =
      zeroSchemeCycle D sX hX L s (n - 1)
        (canonicalGeometricPoint D.site D.base D.base_mem
          (vanishingLocus D sX hX L s).1.toFunctor)
        (locallyFinite_zeroSchemeCycleCoeff_globalSection D sX hX hint L hL hn hs _
          (canonicalGeometricPoint_liesOver D _)) ∧
    weilDivisorOfInvertibleSheaf.{v} D sX hX hint L hL hn =
      chowClass.{v} D sX hX (n - 1) (zeroSchemeCycle D sX hX L s (n - 1)
        (canonicalGeometricPoint D.site D.base D.base_mem
          (vanishingLocus D sX hX L s).1.toFunctor)
        (locallyFinite_zeroSchemeCycleCoeff_globalSection D sX hX hint L hL hn hs _
          (canonicalGeometricPoint_liesOver D _)))
```

## Tag 0EQG, a lemma

[Tag 0EQG](https://stacks.math.columbia.edu/tag/0EQG) in the Stacks Project.

**`AlgebraicGeometry.Space.torsorOfInvertible_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorBaseChange.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorBaseChange.lean#L211). The attribute's comment: “clause (3): in Situation 0EDT with X/B good and L an invertible O\_X-module, for every morphism g : Y ⟶ X of good algebraic spaces the multiplicative torsor (q\_Y : T\_Y ⟶ Y, alpha\_Y) of g^*L, with T\_Y = Spec\_Y(⨁\_n (g^*L)^\{⊗n}), is the base change of (q : T ⟶ X, alpha): there is g' : T\_Y ⟶ T over g making the square cartesian and pulling alpha back to alpha\_Y”.

> **Stacks 0EQG, clause (3): formation of `(q : T ⟶ X, α)` commutes with base change.**  For a
> morphism `g : Y ⟶ X` of good algebraic spaces, let `q_Y : T_Y ⟶ Y` and
> `α_Y : q_Y^*(g^*ℒ) ≅ 𝒪_{T_Y}` be the multiplicative torsor of the invertible `𝒪_Y`-module
> `g^*ℒ`.  There is a morphism `g' : T_Y ⟶ T` with `g' ≫ q = q_Y ≫ g` such that the square is
> cartesian and `α` pulls back along `g'` to `α_Y`: the trivialization `g'^*α` of
> `(g' ≫ q)^*ℒ = (q_Y ≫ g)^*ℒ` is `α_Y` composed with the canonical identification
> `(q_Y ≫ g)^*ℒ ≅ q_Y^*(g^*ℒ)` of Stacks 03LU.

```lean
theorem torsorOfInvertible_baseChange :
    ∃ (g' : torsorOfInvertibleSpace D pY hpY ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL) ⟶
        torsorOfInvertibleSpace D p hp L hL)
      (w : g' ≫ torsorOfInvertibleProjection D p hp L hL =
        torsorOfInvertibleProjection D pY hpY ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL) ≫ g),
      IsPullback g' (torsorOfInvertibleProjection D pY hpY
        ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL))
          (torsorOfInvertibleProjection D p hp L hL) g ∧
        𝔱[p, hp, L, hL, g', w] =
          (modulePullbackTriangle D.site D.base D.base_mem
            (rfl : torsorOfInvertibleProjection D pY hpY
              ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL) ≫ g =
              torsorOfInvertibleProjection D pY hpY
                ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL) ≫ g)).hom.app L ≫
            (torsorOfInvertibleTrivialization D pY hpY
              ((modulePullback D.site D.base D.base_mem g).obj L)
        (isInvertible_modulePullback_obj D.site D.base D.base_mem g L hL)).hom
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorCycles.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorCycles.lean#L78). The attribute's comment: “clause (1): q is surjective, smooth, affine, of relative dimension 1”.

> **Stacks 0EQG, clause (1).** In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible
> `𝒪_X`-module.  The morphism `q : T = \underline{Spec}_X(⨁_{n ∈ ℤ} ℒ^{⊗ n}) ⟶ X` is surjective,
> smooth, affine, and of relative dimension `1`.

```lean
theorem torsorOfInvertible_clause_one :
    IsSurjective D.site D.base D.base_mem (torsorOfInvertibleProjection D p hp L hL).hom ∧
      IsSmooth D.site D.base D.base_mem (torsorOfInvertibleProjection D p hp L hL).hom ∧
      IsAffineHom D.site D.base D.base_mem (torsorOfInvertibleProjection D p hp L hL).hom ∧
      HasRelativeDimension 1 D.site D.base D.base_mem
        (torsorOfInvertibleProjection D p hp L hL).hom
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorCycles.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorCycles.lean#L102). The attribute's comment: “clause (6): q^\{-1}(Z) is a closed subspace of T of delta-dimension at most k + 1 and q^*[Z]\_k = [q^\{-1}(Z)]\_\{k+1}”.

> **Stacks 0EQG, clause (6).** If `Z ⊆ X` is a closed subspace of `δ`-dimension `≤ k`, then
> `q^{-1}(Z)` is a closed subspace of `T` of `δ`-dimension `≤ k + 1`, and
> `q^*[Z]_k = [q^{-1}(Z)]_{k+1}`.

```lean
theorem torsorOfInvertible_clause_six (k : ℤ) (Z : Subfunctor X)
    (hZ : IsClosedSubspace D.site D.base D.base_mem Z)
    (hZk : deltaDimensionSubspace D p hp Z hZ ≤ (k : EInt)) :
    ∃ (hZ' : IsClosedSubspace D.site D.base D.base_mem
        (Z.preimage (torsorOfInvertibleProjection D p hp L hL).hom))
      (hdim : deltaDimensionSubspace D _ (isGood_torsorOfInvertible D p hp L hL)
        (Z.preimage (torsorOfInvertibleProjection D p hp L hL).hom) hZ' ≤ ((k + 1 : ℤ) : EInt)),
      torsorOfInvertibleFlatPullback D p hp L hL k (closedSubspaceCycle D p hp Z hZ k hZk) =
        closedSubspaceCycle D _ (isGood_torsorOfInvertible D p hp L hL)
          (Z.preimage (torsorOfInvertibleProjection D p hp L hL).hom) hZ' (k + 1) hdim
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_seven`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorHenselian.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorHenselian.lean#L620). The attribute's comment: “clause (7): if ξ' ∈ |T| is the generic point of the fibre of |T| → |X| over ξ, then the ring map O^h\_\{X,ξ} → O^h\_\{T,ξ'} induced by q (the local homomorphism compatible with the stalk map of a commuting square of elementary etale neighbourhoods over q) is flat, the maximal ideal of O^h\_\{T,ξ'} is m^h\_ξ O^h\_\{T,ξ'}, and the residue field extension is purely transcendental of transcendence degree 1 (generated by one element transcendental over the residue field of O^h\_\{X,ξ})”.

> **Stacks 0EQG, clause (7).**  In Situation 0EDT let `X/B` be good, let `ℒ` be an invertible
> `𝒪_X`-module and `q : T = \underline{Spec}(⨁_{n ∈ ℤ} ℒ^{⊗ n}) ⟶ X`.  If `ξ' ∈ |T|` is the
> generic point of the fibre of `|T| → |X|` over `ξ = q(ξ')` — every point of that fibre is a
> specialization of `ξ'` — then the ring map `φ : 𝒪^h_{X, ξ} ⟶ 𝒪^h_{T, ξ'}` induced by `q` is flat,
> `𝔪^h_{ξ'} = 𝔪^h_ξ 𝒪^h_{T, ξ'}`, and the residue field extension is purely transcendental of
> transcendence degree `1`: it is generated by a single element transcendental over `κ(ξ)`.
>
> The map `φ` is the one induced by `q`: it is the local homomorphism agreeing on the image of
> `𝒪_{V, v}` with the stalk map of a commuting square of elementary étale neighborhoods
> `U ⟶ V` over `q`, which determines it by the universal property of the henselization.

```lean
theorem torsorOfInvertible_clause_seven
    (ξ' : points D.site D.base D.base_mem (torsorOfInvertibleSpace D p hp L hL).obj)
    (hξ' : ∀ t, pointsMap D.site D.base D.base_mem _
      (torsorOfInvertibleProjection D p hp L hL).hom t =
      pointsMap D.site D.base D.base_mem _ (torsorOfInvertibleProjection D p hp L hL).hom ξ' →
        ξ' ⤳ t) :
    letI := henselianLocalRing_isLocalRing D.site D.base D.base_mem X hp.1
      (pointsMap D.site D.base D.base_mem _ (torsorOfInvertibleProjection D p hp L hL).hom ξ')
      (D.isDecentSpace_of_isGood p hp)
    letI := henselianLocalRing_isLocalRing D.site D.base D.base_mem
      (torsorOfInvertibleSpace D p hp L hL).obj (torsorOfInvertibleSpace D p hp L hL).property ξ'
      (D.isDecentSpace_of_isGood _ (isGood_torsorOfInvertible D p hp L hL))
    ∃ (V : ElementaryEtaleNeighborhood D.site D.base D.base_mem X hp.1
        (pointsMap D.site D.base D.base_mem _ (torsorOfInvertibleProjection D p hp L hL).hom ξ'))
      (U : ElementaryEtaleNeighborhood D.site D.base D.base_mem
        (torsorOfInvertibleSpace D p hp L hL).obj (torsorOfInvertibleSpace D p hp L hL).property ξ')
      (j : U.scheme ⟶ V.scheme) (hj : j.left.1 U.point = V.point)
      (φ : (henselianLocalRing D.site D.base D.base_mem X hp.1
          (pointsMap D.site D.base D.base_mem _ (torsorOfInvertibleProjection D p hp L hL).hom ξ')
          (D.isDecentSpace_of_isGood p hp) : Type (u + 1)) →+*
        (henselianLocalRing D.site D.base D.base_mem (torsorOfInvertibleSpace D p hp L hL).obj
          (torsorOfInvertibleSpace D p hp L hL).property ξ'
          (D.isDecentSpace_of_isGood _ (isGood_torsorOfInvertible D p hp L hL)) : Type (u + 1))),
      yoneda.map j ≫ V.toSpace = U.toSpace ≫ (torsorOfInvertibleProjection D p hp L hL).hom ∧
        (∀ a, φ (stalkToHenselianLocalRing D.site D.base D.base_mem X hp.1 _
            (D.isDecentSpace_of_isGood p hp) V a) =
          stalkToHenselianLocalRing D.site D.base D.base_mem _ _ ξ'
            (D.isDecentSpace_of_isGood _ (isGood_torsorOfInvertible D p hp L hL)) U
            (((V.scheme.left.1.presheaf.stalkCongr (.of_eq hj.symm)).hom ≫
              j.left.1.stalkMap U.point).hom a)) ∧
        ∃ _ : IsLocalHom φ,
          φ.Flat ∧
          Ideal.map φ (maximalIdeal _) = maximalIdeal _ ∧
          letI := (ResidueField.map φ).toAlgebra
          ∃ t : ResidueField (henselianLocalRing D.site D.base D.base_mem
              (torsorOfInvertibleSpace D p hp L hL).obj
                (torsorOfInvertibleSpace D p hp L hL).property
              ξ' (D.isDecentSpace_of_isGood _ (isGood_torsorOfInvertible D p hp L hL)) :
                Type (u + 1)),
            Transcendental (ResidueField (henselianLocalRing D.site D.base D.base_mem X hp.1
              (pointsMap D.site D.base D.base_mem _
                (torsorOfInvertibleProjection D p hp L hL).hom ξ')
              (D.isDecentSpace_of_isGood p hp) : Type (u + 1))) t ∧
            IntermediateField.adjoin (ResidueField
              (henselianLocalRing D.site D.base D.base_mem X hp.1
              (pointsMap D.site D.base D.base_mem _
                (torsorOfInvertibleProjection D p hp L hL).hom ξ')
              (D.isDecentSpace_of_isGood p hp) : Type (u + 1))) {t} = ⊤
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorInjective.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorInjective.lean#L154). The attribute's comment: “clause (4): q^* : Z\_k(X) → Z\_\{k+1}(T) is injective”.

> **Stacks 0EQG, clause (4).** The flat pullback `q^* : Z_k(X) → Z_{k+1}(T)` is injective.

```lean
theorem torsorOfInvertible_clause_four (k : ℤ) :
    Function.Injective (torsorOfInvertibleFlatPullback D p hp L hL k)
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_five`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorIntegral.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorIntegral.lean#L228). The attribute's comment: “clause (5): q^\{-1}(Z) is an integral closed subspace of T for Z an integral closed subspace of X”.

> **Stacks 0EQG, clause (5).** If `Z ⊆ X` is an integral closed subspace, then
> `q^{-1}(Z) ⊆ T` is an integral closed subspace.

```lean
theorem torsorOfInvertible_clause_five (Z : IntegralClosedSubspace D.site D.base D.base_mem X) :
    IsClosedSubspace D.site D.base D.base_mem
        (Z.subspace.preimage (torsorOfInvertibleProjection D p hp L hL).hom) ∧
      IsIntegralSpace D.site D.base D.base_mem
        (Z.subspace.preimage (torsorOfInvertibleProjection D p hp L hL).hom).toFunctor
```

**`AlgebraicGeometry.Space.isQuasicoherent_laurentAlgebraSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean#L123). The attribute's comment: “the quasi-coherence of ⨁\_\{n ∈ ℤ} L^\{⊗n} that clause (1) presupposes in forming T = Spec\_X(⨁\_\{n ∈ ℤ} L^\{⊗n}): in Situation 0EDT with X/B good, the Laurent algebra of an invertible O\_X-module is a quasi-coherent O\_X-algebra, with no hypothesis on L beyond invertibility -- triviality of L on an etale covering is DISCHARGED here from local ringedness of the small etale site, not assumed. Nothing about the morphism q is covered by this declaration”.

> The Laurent algebra sheaf `⨁_{n ∈ ℤ} ℒ^{⊗ n}` of an invertible `𝒪_X`-module `ℒ` is
> quasi-coherent.

```lean
theorem isQuasicoherent_laurentAlgebraSheaf :
    AlgebraSheaf.IsQuasicoherent (laurentAlgebraSheaf D p hp L hL)
```

**`AlgebraicGeometry.Space.isAffineHom_multiplicativeTorsorProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean#L152). The attribute's comment: “clause (1), the affineness part -- BUT VACUOUS AS STATED, and registered here only because the base file carries this line. The statement takes a parameter E : AffineAlgebraAntiEquivalence, this development's rendering of Stacks 081V with the tag's unrestricted target, and that type is EMPTY over any site one of whose algebraic spaces has an affine etale chart with a nonzero ring of functions (not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart). Over such a site this theorem asserts nothing: quasi-coherence of the Laurent algebra, which IS discharged by isQuasicoherent\_laurentAlgebraSheaf, is discharged into a statement with no content. THE REGISTRATION THAT CARRIES THIS CLAUSE is isAffineHom\_multiplicativeTorsorSpectrumProjection (MultiplicativeTorsorSpectrum), which takes no parameter at all; isAffineHom\_boundedMultiplicativeTorsorProjection gives it inside the site of X under the size condition of the corrected 081V, which E implies. Read this line as covering nothing”.

> The projection `q : T = \underline{Spec}_X(⨁_{n ∈ ℤ} ℒ^{⊗ n}) ⟶ X` of the multiplicative
> torsor of an invertible `𝒪_X`-module is an affine morphism of algebraic spaces.
>
> **This statement is vacuous over any nondegenerate site**, since the parameter `E` it takes is
> empty there; see the implementation notes above.  The assertion under the hypotheses of
> Situation 0EDT alone is
> `AlgebraicGeometry.Space.isAffineHom_multiplicativeTorsorSpectrumProjection`.

```lean
theorem isAffineHom_multiplicativeTorsorProjection :
    IsAffineHom D.site D.base D.base_mem (multiplicativeTorsorProjection D p hp L hL E
      (isQuasicoherent_laurentAlgebraSheaf D p hp L hL)).hom
```

**`AlgebraicGeometry.Space.isPullback_multiplicativeTorsorBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorOfInvertible.lean#L207). The attribute's comment: “clause (3) for q: the base change of q along an arbitrary g : Y ⟶ X is cartesian and Y ×\_X T is the relative spectrum over Y of g^*(⨁\_n L^\{⊗n}), the latter being the corner of the cartesian square as stated. VACUOUS AS STATED: it takes the parameters E : AffineAlgebraAntiEquivalence and C its base-change clause, and E is EMPTY over any site one of whose algebraic spaces has an affine etale chart with a nonzero ring of functions (not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart). Over such a site this theorem asserts nothing. In particular, although Stacks 08AI at q -- the input the construction of alpha : q^*L ≅ O\_T consumes -- is genuinely discharged from X/B good and L invertible by affineDirectImageEquivalence\_multiplicativeTorsorProjection, that discharge is itself stated under E and so is equally vacuous; it should not be read as evidence that this clause is in better shape than it is. Two further pieces of the source's clause (3) lie outside this statement in any case: alpha itself, whose construction needs in addition the degree-shift isomorphism of the Laurent algebra over itself, ⨁\_n L^\{⊗(n+1)} ≅ ⨁\_n L^\{⊗n}, which is clause (2)'s own content and which this tree does not have (only the per-degree powSuccIso); and the identification of g^*(⨁\_n L^\{⊗n}) with ⨁\_n (g^*L)^\{⊗n}. No parameter-free counterpart of this base-change square has been formed: MultiplicativeTorsorSpectrum supplies T, q and the affineness of q without parameters, not the base change”.

> The base change of `q : T ⟶ X` along `g : Y ⟶ X` is cartesian, with corner
> `\underline{Spec}_Y(g^*(⨁_{n ∈ ℤ} ℒ^{⊗ n}))`: forming the multiplicative torsor commutes with
> arbitrary base change.
>
> **This statement is vacuous over any nondegenerate site**, since the parameters `E` and `C` it
> takes are empty there; see the implementation notes above.

```lean
theorem isPullback_multiplicativeTorsorBaseChange :
    IsPullback (multiplicativeTorsorBaseChangeProjection D p hp L hL E C g)
      (multiplicativeTorsorBaseChange D p hp L hL E C g).obj.hom
      (multiplicativeTorsorProjection D p hp L hL E
        (isQuasicoherent_laurentAlgebraSheaf D p hp L hL)) g
```

**`AlgebraicGeometry.Space.isAffineHom_multiplicativeTorsorSpectrumProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorSpectrum.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorSpectrum.lean#L183). The attribute's comment: “clause (1), the affineness part only, in Situation 0EDT with X/B good: for an invertible O\_X-module L the projection q of T = Spec\_X(⨁\_\{n ∈ ℤ} L^\{⊗n}) is affine. Carries NO parameter and no size condition: quasi-coherence of the Laurent algebra is discharged by isQuasicoherent\_laurentAlgebraSheaf, itself resting on triviality of L on an etale covering, discharged by isLocallyTrivial\_of\_isInvertibleSheaf from local ringedness of the small etale site, and T is formed by relativeSpectrum, the unconditional form of Stacks 081W. This replaces isAffineHom\_multiplicativeTorsorProjection, which asserts the same thing under a parameter E : AffineAlgebraAntiEquivalence that is EMPTY over any site one of whose algebraic spaces has an affine etale chart with a nonzero ring of functions (not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart) and so asserts nothing there. q lives over relativeSpectrumSite, the Stacks 03FO enlargement of the site of X; isAffineHom\_boundedMultiplicativeTorsorProjection is the same assertion inside the site of X itself, under the size condition of the corrected 081V, which E implies. NOT COVERED by this or any other declaration: the rest of clause (1) -- q surjective, smooth and of relative dimension 1 -- and clauses (2), (4), (5), (6), (7). The source derives the three remaining properties of clause (1) from T x\_X U ≅ G\_m x U for an etale chart U trivialising L, and that identification does not exist in this tree: isPullback\_affineChartSpec identifies the relative spectrum over an affine chart with Spec of the algebra's sections there, nothing identifies the Laurent algebra's sections at a trivialising chart V with O(V)[t,t^\{-1}] (the sheafification step is unaccounted for), and no scheme-level smoothness, surjectivity or relative-dimension statement about multiplicativeGroupBaseChange exists”.

> The projection `q : T ⟶ X` of the multiplicative torsor of an invertible `𝒪_X`-module is
> an affine morphism of algebraic spaces, under the hypotheses of Situation 0EDT and no others:
> `X/B` good and `ℒ` invertible.

```lean
theorem isAffineHom_multiplicativeTorsorSpectrumProjection :
    IsAffineHom
      (relativeSpectrumSite
        (laurentQuasicoherentAlgebra D p hp L hL (isQuasicoherent_laurentAlgebraSheaf D p hp L hL)))
      D.base
      (contains_relativeSpectrumSite
        (laurentQuasicoherentAlgebra D p hp L hL
          (isQuasicoherent_laurentAlgebraSheaf D p hp L hL)))
      (multiplicativeTorsorSpectrumProjection D p hp L hL).hom
```

**`AlgebraicGeometry.Space.torsorOfInvertible_clause_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorTrivialization.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicativeTorsorTrivialization.lean#L426). The attribute's comment: “clause (2): there is an isomorphism alpha : q^*L ≅ O\_T”.

> There is an isomorphism `α : q^*ℒ ≅ 𝒪_T`.

```lean
theorem torsorOfInvertible_clause_two :
    Nonempty ((modulePullback D.site D.base D.base_mem
      (torsorOfInvertibleProjection D p hp L hL)).obj L ≅ SheafOfModules.unit _)
```

## Tag 0EQH, a lemma

[Tag 0EQH](https://stacks.math.columbia.edu/tag/0EQH) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.ord_eq_ord_of_extendedMaximalIdeal_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOrderOfVanishing.lean#L503). The attribute's comment: “coefficientwise at a prime divisor Z = q^\{-1}(Z') of T: ord\_Z(q^*(s)) = ord\_\{Z',L}(s), which is the source's q^* div\_L(s) = div\_T(q^*(s)) read at the coefficient of Z. No component bookkeeping arises: the source assumes the base integral, so the multiplicity of a component is one, and the multiplicity of Z over Z' is one as well by hmax. It is stated coefficientwise because the flat pullback of cycles is Stacks 0EP8, which this repository does not have, and because the principal divisor div(q^*(s)) of Stacks 0ENP is not available either; for the same reason Stacks 0EPT and 0EPV are already carried coefficientwise here. The source's other case, a prime divisor of T dominating Y, where both coefficients vanish, is bookkeeping internal to the flat pullback and does not arise in a statement indexed by a prime divisor lying over a prime divisor. PROVED, not assumed: that the two orders of vanishing are equal, from Stacks 02M1 (length\_baseChange\_eq\_length\_mul\_length\_quotient) through Ring.ord\_map\_of\_flatHom, the multiplicity being one because the extended maximal ideal is the maximal ideal and the residue field has length one. RESTRICTED: carried as explicit named hypotheses are (i) the flat local homomorphism φ : O^h\_\{Y,ξ'} → O^h\_\{T,ξ} with hloc and hflat, and (ii) the identity hmax that the maximal ideal of O^h\_\{Y,ξ'} extends to the maximal ideal of O^h\_\{T,ξ} — these are the two properties of q that Lemma 0EQG supplies and that the source uses here, the morphism q itself being available in this repository only as multiplicativeTorsorProjection, whose surjectivity, smoothness and relative dimension are not proved there; (iii) the rational function qs standing for q^*(s), with the embedding embT of Stacks 0ENK, and hqs, that its ratio at ξ is the image under φ of the ratio of s at ξ' — the trivialization alpha : q^*L ≅ O\_T is not constructed in this repository, as the clause of Stacks 0EQG on multiplicativeTorsorBaseChange records, so the identification of q^*(s) as a function is this hypothesis, which is the source's own step of writing s/s\_\{ξ'} = a/b and pulling the fraction back; and (iv) the ratio of Stacks 0EPR at the generic point of Z' as the parameter ratioY”.

> **Stacks 0EQH, coefficientwise.** *The divisor of a meromorphic section pulls back to the
> divisor of the associated rational function on the multiplicative torsor.* Let `q : T ⟶ Y` be
> the morphism of Stacks 0EQG for an invertible `𝒪_Y`-module `ℒ`, so that `q^*ℒ ≅ 𝒪_T` and a
> nonzero meromorphic section `s` of `ℒ` becomes a nonzero meromorphic function `q^*(s)` on `T`.
> Let `Z' ⊆ Y` be a prime divisor and `Z = q^{-1}(Z')`, and let `φ : 𝒪^h_{Y,ξ'} ⟶ 𝒪^h_{T,ξ}` be
> the induced flat local homomorphism. Because `𝔪^h_{Y,ξ'} 𝒪^h_{T,ξ} = 𝔪^h_{T,ξ}`,
>
>   `ord_Z(q^*(s)) = ord_{Z',ℒ}(s)`,
>
> which is `q^* div_ℒ(s) = div_T(q^*(s))` coefficientwise.
>
> The hypothesis `hmax` is the identity of ideals that Stacks 0EQG supplies, and it is what makes
> the multiplicity one: the quotient is then the residue field of `𝒪^h_{T,ξ}`, whose length is
> one, so `Ring.ord_map_of_flatHom` gives equality of the two orders rather than a multiple.

```lean
theorem PrimeDivisor.ord_eq_ord_of_extendedMaximalIdeal_eq
    (hloc : IsLocalHom φ) (hflat : φ.Flat)
    (hmax : Ideal.map φ
        (IsLocalRing.maximalIdeal ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)) =
      IsLocalRing.maximalIdeal ↥(ZX.genericHenselianLocalRing B S hS hX hdecX))
    (L : Modules.{u, max u z} B S hS Y hY)
    (s : MeromorphicSection.{u, z} B S hS Y hY L)
    (ratioY : LocalRatio.{u, z} B S hS hY hdecY ZY L)
    (embT : rationalFunctions B S hS hX →+* ZX.genericTotalFractionRing B S hS hX hdecX)
    (qs : rationalFunctions B S hS hX)
    (a b : nonZeroDivisors ↥(ZY.genericHenselianLocalRing B S hS hY hdecY))
    (hs : (ratioY s : ZY.genericTotalFractionRing B S hS hY hdecY) =
      IsLocalization.mk' (ZY.genericTotalFractionRing B S hS hY hdecY)
        (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)) b)
    (hqs : embT qs = IsLocalization.mk' (ZX.genericTotalFractionRing B S hS hX hdecX)
      (φ (a : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)))
      (⟨φ (b : ↥(ZY.genericHenselianLocalRing B S hS hY hdecY)),
        Ring.map_mem_nonZeroDivisors_of_flatHom hflat b.2⟩ :
        nonZeroDivisors ↥(ZX.genericHenselianLocalRing B S hS hX hdecX)))
    (hqsu : IsUnit (embT qs)) :
    ZX.ord B S hS hX hdecX (embT qs) hqsu =
      orderOfVanishingSection.{u, z} B S hS hY hdecY ZY L s ratioY
```

**`AlgebraicGeometry.Space.flatPullbackMap_sectionWeilDivisor_torsorOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/TorsorPullbackDivisor.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/TorsorPullbackDivisor.lean#L108). The attribute's comment: “q^* div\_L(s) = div\_T(q^*(s)) as cycles on T, for X/B good and integral, L invertible, s a nonzero meromorphic section and q : T -> X the morphism of 0EQG (torsorOfInvertibleProjection: flat of relative dimension 1, T/B good, T integral, all proved). Stated with div\_\{q^*L}(q^*s) and, for EVERY isomorphism alpha : q^*L ≅ O\_T, with the divisor div\_\{O\_T}(alpha(q^*s)) of the nonzero meromorphic function alpha(q^*s); q^* on cycles is the flat pullback of 0EP8, div is 0EQE, q^*s is the pullback of 0ENC. Proved from 0EQQ for q (T integral, so the component sum collapses) and the invariance of div under an isomorphism of modules”.

> In Situation 0EDT let `X/B` be good and integral with `n = dim_δ(X)`, let
> `ℒ` be an invertible `𝒪_X`-module, let `s` be a nonzero meromorphic section of `ℒ`, and let
> `q : T ⟶ X` be the morphism of Stacks 0EQG. Then
>
>   `q^* div_ℒ(s) = div_T(q^*(s))`
>
> in `Z_n(T)`: the left-hand side is the flat pullback along `q` (flat of relative dimension one) of
> the Weil divisor of `s`; on the right `q^*(s)` is the pullback of `s`, and the identity holds both
> with `div_{q^*ℒ}(q^*s)` and, for every isomorphism `α : q^*ℒ ≅ 𝒪_T`, with the divisor
> `div_{𝒪_T}(α(q^*s))` of the meromorphic function `α(q^*s)` on `T`.

```lean
theorem flatPullbackMap_sectionWeilDivisor_torsorOfInvertible {n : ℤ}
    (hn : deltaDimensionClosed D p hp Set.univ isClosed_univ = (n : EInt))
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hp.1 L) (hs : s ≠ 0) :
    flatPullbackMap D ((torsorOfInvertibleProjection D p hp L hL).hom ≫ p)
        (isGood_torsorOfInvertible D p hp L hL) p hp (torsorOfInvertibleProjection D p hp L hL).hom
        rfl 1 (isFlat_torsorOfInvertibleProjection D p hp L hL)
        (hasRelativeDimension_torsorOfInvertibleProjection D p hp L hL) (n - 1) (n + (1 : ℕ) - 1)
        (by push_cast; ring) (sectionWeilDivisor D p hp hint L hL hn s hs) =
      sectionWeilDivisor D ((torsorOfInvertibleProjection D p hp L hL).hom ≫ p)
        (isGood_torsorOfInvertible D p hp L hL)
        (isIntegralSpace_torsorOfInvertibleSpace D p hp L hL hint)
        ((modulePullback D.site D.base D.base_mem (torsorOfInvertibleProjection D p hp L hL)).obj L)
        (isInvertibleSheaf_modulePullback D p hp _ (isGood_torsorOfInvertible D p hp L hL)
          (torsorOfInvertibleProjection D p hp L hL) hL)
        (deltaDimensionClosed_torsorOfInvertibleSpace D p hp hint L hL hn)
        (pullbackMeromorphicSection D.site D.base D.base_mem
          (torsorOfInvertibleProjection D p hp L hL) L
          (pullbacksMeromorphicSections_of_flat D.site D.base D.base_mem _
            (isFlat_torsorOfInvertibleProjection D p hp L hL)) s)
        (pullbackMeromorphicSection_ne_zero_of_isFlat D p hp hint _
          (isGood_torsorOfInvertible D p hp L hL)
          (isIntegralSpace_torsorOfInvertibleSpace D p hp L hL hint) _
          (isFlat_torsorOfInvertibleProjection D p hp L hL) hL s hs) ∧
    ∀ α : (modulePullback D.site D.base D.base_mem
          (torsorOfInvertibleProjection D p hp L hL)).obj L ≅
        SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite D.site
          D.base D.base_mem (torsorOfInvertibleSpace D p hp L hL).obj
          (isGood_torsorOfInvertible D p hp L hL).1).O),
      flatPullbackMap D ((torsorOfInvertibleProjection D p hp L hL).hom ≫ p)
          (isGood_torsorOfInvertible D p hp L hL) p hp
          (torsorOfInvertibleProjection D p hp L hL).hom
          rfl 1 (isFlat_torsorOfInvertibleProjection D p hp L hL)
          (hasRelativeDimension_torsorOfInvertibleProjection D p hp L hL) (n - 1) (n + (1 : ℕ) - 1)
          (by push_cast; ring) (sectionWeilDivisor D p hp hint L hL hn s hs) =
        sectionWeilDivisor D ((torsorOfInvertibleProjection D p hp L hL).hom ≫ p)
          (isGood_torsorOfInvertible D p hp L hL)
          (isIntegralSpace_torsorOfInvertibleSpace D p hp L hL hint) _
          (isInvertibleSheaf_unit D _ (isGood_torsorOfInvertible D p hp L hL))
          (deltaDimensionClosed_torsorOfInvertibleSpace D p hp hint L hL hn)
          (SheafOfModules.sectionsMap
            (meromorphicSectionSheafMap D.site D.base D.base_mem _
              (isGood_torsorOfInvertible D p hp L hL).1 α.hom)
            (pullbackMeromorphicSection D.site D.base D.base_mem
              (torsorOfInvertibleProjection D p hp L hL) L
              (pullbacksMeromorphicSections_of_flat D.site D.base D.base_mem _
                (isFlat_torsorOfInvertibleProjection D p hp L hL)) s))
          (sectionsMap_meromorphicSectionSheafMap_inv_ne_zero D _
            (isGood_torsorOfInvertible D p hp L hL)
            (isIntegralSpace_torsorOfInvertibleSpace D p hp L hL hint)
            (isInvertibleSheaf_unit D _ (isGood_torsorOfInvertible D p hp L hL))
            (isInvertibleSheaf_modulePullback D p hp _ (isGood_torsorOfInvertible D p hp L hL)
              (torsorOfInvertibleProjection D p hp L hL) hL) α.symm _
            (pullbackMeromorphicSection_ne_zero_of_isFlat D p hp hint _
              (isGood_torsorOfInvertible D p hp L hL)
              (isIntegralSpace_torsorOfInvertibleSpace D p hp L hL hint) _
              (isFlat_torsorOfInvertibleProjection D p hp L hL) hL s hs))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.17, Tag 0EQD](https://stacks.math.columbia.edu/tag/0EQD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
