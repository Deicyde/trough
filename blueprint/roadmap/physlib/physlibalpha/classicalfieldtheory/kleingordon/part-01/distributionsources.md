---
declaration: module
origin: cited
lean: KleinGordon.Spacetime.nativeTestDerivative_coe, KleinGordon.Spacetime.nativeTestOperator_equiv, KleinGordon.Spacetime.retardedPointSource, KleinGordon.Spacetime.advancedPointSource, KleinGordon.Spacetime.distributionOperator_retardedPointSource, KleinGordon.Spacetime.distributionOperator_advancedPointSource, KleinGordon.Spacetime.retardedPointSource_vanishes, KleinGordon.Spacetime.advancedPointSource_vanishes
statement: formalized
proof: formalized
---

# Distributional sources

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DistributionSources`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean): 37 declarations, 31 with a docstring.

> Compactly supported distributions have retarded and advanced responses.

## i. Overview

> Compactly supported distributions have retarded and advanced responses. The point source is a
> corollary.

## ii. Key results

> - `retardedPointSource` : The retarded native point-source distribution obtained by transposing
>   advanced evaluation.
> - `advancedPointSource` : The advanced native point-source distribution obtained by transposing
>   retarded evaluation.
> - `realRetardedCutoff` : The continuous cut off real retarded response on native smooth tests.
> - `realAdvancedCutoff` : The continuous cut off real advanced response on native smooth tests.
> - `retardedLocalizedResponse` : Transposing the cut off advanced test map gives a retarded response
>   on all distributions.
> - `advancedLocalizedResponse` : Transposing the cut off retarded test map gives an advanced response
>   on all distributions.
> - `retardedCompactResponse` : The retarded response of a compactly supported distribution.
> - `advancedCompactResponse` : The advanced response of a compactly supported distribution.

## iv. References

> None.

## A. Causal Klein–Gordon responses to a Dirac source

> - `retardedPointSource` : The retarded native point-source distribution obtained by transposing
>   advanced evaluation.
> - `advancedPointSource` : The advanced native point-source distribution obtained by transposing
>   retarded evaluation.
>
> Lemmas: `nativeTestDerivative_coe`, `nativeTestOperator_equiv`,
> `distributionOperator_retardedPointSource`, `distributionOperator_advancedPointSource`,
> `retardedPointSource_vanishes`, `advancedPointSource_vanishes`,
> `dsupport_retardedPointSource_subset`, `dsupport_advancedPointSource_subset`.

## B. The retarded point source through the spatial Fourier multiplier

> Lemmas: `retardedPointSource_apply`.

## C. Distributional Klein–Gordon Green operators in every dimension

> - `realRetardedCutoff` : The continuous cut off real retarded response on native smooth tests.
> - `realAdvancedCutoff` : The continuous cut off real advanced response on native smooth tests.
> - `retardedLocalizedResponse` : Transposing the cut off advanced test map gives a retarded response
>   on all distributions.
> - `advancedLocalizedResponse` : Transposing the cut off retarded test map gives an advanced response
>   on all distributions.
> - `retardedCompactResponse` : The retarded response of a compactly supported distribution.
> - `advancedCompactResponse` : The advanced response of a compactly supported distribution.
> - `compactDistributionOperator` : The field operator restricts to an endomorphism of compactly
>   supported distributions.
>
> Lemmas: `realRetardedCutoff_apply`, `realAdvancedCutoff_apply`, `retardedLocalizedResponse_solves`,
> `advancedLocalizedResponse_solves`, `retardedLocalizedResponse_vanishes`,
> `advancedLocalizedResponse_vanishes`, `retardedDistribution_eq_zero`,
> `advancedDistribution_eq_zero`, `retardedDistribution_unique`, `advancedDistribution_unique` and
> more.

**`KleinGordon.Spacetime.nativeTestDerivative_coe`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L99).

```lean
lemma nativeTestDerivative_coe (μ : Fin 1 ⊕ Fin d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    (TestFunction.lineDerivCLM (n := ⊤) (k := ⊤) ℝ (Lorentz.Vector.basis μ) φ : SpaceTime d → ℝ) =
      SpaceTime.deriv μ φ
```

**`KleinGordon.Spacetime.nativeTestOperator_equiv`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L107).

```lean
lemma nativeTestOperator_equiv (m : ℝ) (f : TestField d ℝ) :
    testOperator m (testFieldEquiv ℝ f) =
      testFieldEquiv ℝ ((equation m).compactOperator f)
```

**`KleinGordon.Spacetime.retardedPointSource`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L123).

> The retarded native point-source distribution obtained by transposing advanced evaluation.

```lean
def retardedPointSource (m : ℝ) (p : SpaceTime d) : Distribution (⊤ : Opens (SpaceTime d)) ℝ ⊤
```

**`KleinGordon.Spacetime.advancedPointSource`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L130).

> The advanced native point-source distribution obtained by transposing retarded evaluation.

```lean
def advancedPointSource (m : ℝ) (p : SpaceTime d) : Distribution (⊤ : Opens (SpaceTime d)) ℝ ⊤
```

**`KleinGordon.Spacetime.distributionOperator_retardedPointSource`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L137).

> The retarded point-source distribution solves the weak equation with source `δₚ`.

```lean
lemma distributionOperator_retardedPointSource (m : ℝ) (p : SpaceTime d) :
    distributionOperator m (retardedPointSource m p) = Distribution.delta p
```

**`KleinGordon.Spacetime.distributionOperator_advancedPointSource`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L149).

> The advanced point-source distribution solves the weak equation with source `δₚ`.

```lean
lemma distributionOperator_advancedPointSource (m : ℝ) (p : SpaceTime d) :
    distributionOperator m (advancedPointSource m p) = Distribution.delta p
```

**`KleinGordon.Spacetime.retardedPointSource_vanishes`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L161).

> The retarded point-source response annihilates all tests outside the source event's future.

```lean
lemma retardedPointSource_vanishes (m : ℝ) (p : SpaceTime d) :
    Distribution.IsVanishingOn (retardedPointSource m p)
      ((causalRelation d).causalFuture {p})ᶜ
```

**`KleinGordon.Spacetime.advancedPointSource_vanishes`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L176).

> The advanced point-source response annihilates all tests outside the source event's past.

```lean
lemma advancedPointSource_vanishes (m : ℝ) (p : SpaceTime d) :
    Distribution.IsVanishingOn (advancedPointSource m p)
      ((causalRelation d).causalPast {p})ᶜ
```

**`KleinGordon.Spacetime.dsupport_retardedPointSource_subset`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L191).

> Native distributional support of the retarded fundamental solution is causal.

```lean
lemma dsupport_retardedPointSource_subset (m : ℝ) (p : SpaceTime d) :
    Distribution.dsupport (retardedPointSource m p) ⊆ (causalRelation d).causalFuture {p}
```

**`KleinGordon.Spacetime.dsupport_advancedPointSource_subset`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L197).

> Native distributional support of the advanced fundamental solution is causal.

```lean
lemma dsupport_advancedPointSource_subset (m : ℝ) (p : SpaceTime d) :
    Distribution.dsupport (advancedPointSource m p) ⊆ (causalRelation d).causalPast {p}
```

**`KleinGordon.Spacetime.retardedPointSource_apply`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L206).

> **The retarded fundamental solution as propagated Dirac distributions.** Tested against a
> real test function `φ` the retarded point source at the event `p` is the real part of the time
> integral of the Fourier multiplier `sincPropagator (s - t₀)` applied to the Dirac distribution at
> the position `y₀` of `p`, paired with the spatial slice of `φ` at the time `s`.

```lean
lemma retardedPointSource_apply (m : ℝ) (p : SpaceTime d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    retardedPointSource m p φ =
      (∫ s in Set.Ioi (coordinates d p).1,
        sineEvolutionTempered ℂ (s - (coordinates d p).1) (m ^ 2)
          (TemperedDistribution.delta (coordinates d p).2)
          (slice ℂ (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ)) s)).re
```

**`KleinGordon.Spacetime.realRetardedCutoff`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L217).

> The continuous cut off real retarded response on native smooth tests.

```lean
def realRetardedCutoff (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    𝓓((⊤ : Opens (SpaceTime d)), ℝ) →L[ℝ] 𝓓((⊤ : Opens (SpaceTime d)), ℝ)
```

**`KleinGordon.Spacetime.realAdvancedCutoff`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L227).

> The continuous cut off real advanced response on native smooth tests.

```lean
def realAdvancedCutoff (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    𝓓((⊤ : Opens (SpaceTime d)), ℝ) →L[ℝ] 𝓓((⊤ : Opens (SpaceTime d)), ℝ)
```

**`KleinGordon.Spacetime.realRetardedCutoff_apply`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L236).

```lean
lemma realRetardedCutoff_apply (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (f : TestField d ℝ) (p : SpaceTime d) :
    realRetardedCutoff m χ (testFieldEquiv ℝ f) p =
      χ p * ((realRetardedGreenOperator m).toLinearMap f).val p
```

**`KleinGordon.Spacetime.realAdvancedCutoff_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L246).

```lean
lemma realAdvancedCutoff_apply (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (f : TestField d ℝ) (p : SpaceTime d) :
    realAdvancedCutoff m χ (testFieldEquiv ℝ f) p =
      χ p * ((realAdvancedGreenOperator m).toLinearMap f).val p
```

**`KleinGordon.Spacetime.retardedLocalizedResponse`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L268).

> Transposing the cut off advanced test map gives a retarded response on all distributions.

```lean
def retardedLocalizedResponse (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    DistributionField d V →L[ℝ] DistributionField d V
```

**`KleinGordon.Spacetime.advancedLocalizedResponse`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L273).

> Transposing the cut off retarded test map gives an advanced response on all distributions.

```lean
def advancedLocalizedResponse (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    DistributionField d V →L[ℝ] DistributionField d V
```

**`KleinGordon.Spacetime.retardedLocalizedResponse_solves`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L277).

```lean
lemma retardedLocalizedResponse_solves (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (T : DistributionField d V) :
    distributionOperator m (retardedLocalizedResponse m χ T) =
      multiplyDistribution χ χ.contDiff T
```

**`KleinGordon.Spacetime.advancedLocalizedResponse_solves`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L295).

```lean
lemma advancedLocalizedResponse_solves (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (T : DistributionField d V) :
    distributionOperator m (advancedLocalizedResponse m χ T) =
      multiplyDistribution χ χ.contDiff T
```

**`KleinGordon.Spacetime.retardedLocalizedResponse_vanishes`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L314).

> Retarded propagation respects every distributional source support bound.

```lean
lemma retardedLocalizedResponse_vanishes (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (T : DistributionField d V) (K : Set (SpaceTime d))
    (hT : Distribution.IsVanishingOn T Kᶜ) :
    Distribution.IsVanishingOn (retardedLocalizedResponse m χ T)
      ((causalRelation d).causalFuture K)ᶜ
```

**`KleinGordon.Spacetime.advancedLocalizedResponse_vanishes`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L339).

> Advanced propagation respects every distributional source support bound.

```lean
lemma advancedLocalizedResponse_vanishes (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (T : DistributionField d V) (K : Set (SpaceTime d))
    (hT : Distribution.IsVanishingOn T Kᶜ) :
    Distribution.IsVanishingOn (advancedLocalizedResponse m χ T)
      ((causalRelation d).causalPast K)ᶜ
```

**`KleinGordon.Spacetime.retardedDistribution_eq_zero`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L364).

> A weak homogeneous field with future support in a compact causal future vanishes.

```lean
lemma retardedDistribution_eq_zero (m : ℝ) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (T : DistributionField d V)
    (hT : Distribution.IsVanishingOn T ((causalRelation d).causalFuture K)ᶜ)
    (hzero : distributionOperator m T = 0) : T = 0
```

**`KleinGordon.Spacetime.advancedDistribution_eq_zero`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L379).

> A weak homogeneous field with past support in a compact causal past vanishes.

```lean
lemma advancedDistribution_eq_zero (m : ℝ) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (T : DistributionField d V)
    (hT : Distribution.IsVanishingOn T ((causalRelation d).causalPast K)ᶜ)
    (hzero : distributionOperator m T = 0) : T = 0
```

**`KleinGordon.Spacetime.retardedDistribution_unique`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L395).

> The same source and retarded support determine a unique distributional solution.

```lean
lemma retardedDistribution_unique (m : ℝ) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (u v : DistributionField d V)
    (hu : Distribution.IsVanishingOn u ((causalRelation d).causalFuture K)ᶜ)
    (hv : Distribution.IsVanishingOn v ((causalRelation d).causalFuture K)ᶜ)
    (hsource : distributionOperator m u =
      distributionOperator m v) : u = v
```

**`KleinGordon.Spacetime.advancedDistribution_unique`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L409).

> The same source and advanced support determine a unique distributional solution.

```lean
lemma advancedDistribution_unique (m : ℝ) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (u v : DistributionField d V)
    (hu : Distribution.IsVanishingOn u ((causalRelation d).causalPast K)ᶜ)
    (hv : Distribution.IsVanishingOn v ((causalRelation d).causalPast K)ᶜ)
    (hsource : distributionOperator m u =
      distributionOperator m v) : u = v
```

**`KleinGordon.Spacetime.retardedCompactResponse`**, a def, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L423).

> The retarded response of a compactly supported distribution.

```lean
def retardedCompactResponse (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    DistributionField d V
```

**`KleinGordon.Spacetime.advancedCompactResponse`**, a def, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L428).

> The advanced response of a compactly supported distribution.

```lean
def advancedCompactResponse (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    DistributionField d V
```

**`KleinGordon.Spacetime.retardedCompactResponse_solves`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L433).

> The retarded response solves the equation for the source itself.

```lean
lemma retardedCompactResponse_solves (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    distributionOperator m (retardedCompactResponse m T) = T.val
```

**`KleinGordon.Spacetime.advancedCompactResponse_solves`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L440).

> The advanced response solves the equation for the source itself.

```lean
lemma advancedCompactResponse_solves (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    distributionOperator m (advancedCompactResponse m T) = T.val
```

**`KleinGordon.Spacetime.retardedCompactResponse_vanishes`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L447).

> The retarded response is supported in the causal future of the source's compact bound.

```lean
lemma retardedCompactResponse_vanishes (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    Distribution.IsVanishingOn (retardedCompactResponse m T)
      ((causalRelation d).causalFuture (compactDistributionBound T))ᶜ
```

**`KleinGordon.Spacetime.advancedCompactResponse_vanishes`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L453).

> The advanced response is supported in the causal past of the source's compact bound.

```lean
lemma advancedCompactResponse_vanishes (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    Distribution.IsVanishingOn (advancedCompactResponse m T)
      ((causalRelation d).causalPast (compactDistributionBound T))ᶜ
```

**`KleinGordon.Spacetime.retardedCompactResponse_unique`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L459).

> Any distributional solution with future support is the retarded response.

```lean
lemma retardedCompactResponse_unique (m : ℝ) (T : compactDistributions (SpaceTime d) V)
    (u : DistributionField d V) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (hu : Distribution.IsVanishingOn u ((causalRelation d).causalFuture K)ᶜ)
    (hsource : distributionOperator m u = T.val) :
    u = retardedCompactResponse m T
```

**`KleinGordon.Spacetime.advancedCompactResponse_unique`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L473).

> Any distributional solution with past support is the advanced response.

```lean
lemma advancedCompactResponse_unique (m : ℝ) (T : compactDistributions (SpaceTime d) V)
    (u : DistributionField d V) (K : Set (SpaceTime d)) (hK : IsCompact K)
    (hu : Distribution.IsVanishingOn u ((causalRelation d).causalPast K)ᶜ)
    (hsource : distributionOperator m u = T.val) :
    u = advancedCompactResponse m T
```

**`KleinGordon.Spacetime.distributionOperator_vanishes`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L487).

> The massive weak operator preserves every source annihilation bound.

```lean
lemma distributionOperator_vanishes (m : ℝ) (T : DistributionField d V) (K : Set (SpaceTime d))
    (hT : Distribution.IsVanishingOn T Kᶜ) :
    Distribution.IsVanishingOn (distributionOperator m T) Kᶜ
```

**`KleinGordon.Spacetime.compactDistributionOperator`**, a def, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L503).

> The field operator restricts to an endomorphism of compactly supported distributions.

```lean
def compactDistributionOperator (m : ℝ) :
    compactDistributions (SpaceTime d) V →ₗ[ℝ] compactDistributions (SpaceTime d) V
```

**`KleinGordon.Spacetime.retardedCompactResponse_operator`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L512).

> The retarded response inverts the field operator on compactly supported distributions.

```lean
lemma retardedCompactResponse_operator (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    retardedCompactResponse m (compactDistributionOperator m T) = T.val
```

**`KleinGordon.Spacetime.advancedCompactResponse_operator`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean#L522).

> The advanced response inverts the field operator on compactly supported distributions.

```lean
lemma advancedCompactResponse_operator (m : ℝ) (T : compactDistributions (SpaceTime d) V) :
    advancedCompactResponse m (compactDistributionOperator m T) = T.val
```

## Depends on

- [Green operators on spacetime](greenoperators.md)
- [Compactly supported distributions and cutoffs](../../../mathematics/part-02/distribution/compactsupport.md)

## Proof depends on

- [The solution as a tempered distribution in space](temperedslice.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DistributionSources.lean)
