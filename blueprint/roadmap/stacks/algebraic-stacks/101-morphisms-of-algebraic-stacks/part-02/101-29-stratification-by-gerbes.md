---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_openSubstack_dense_isGerbe, AlgebraicGeometry.PPowerWeighted.action, AlgebraicGeometry.PPowerWeighted.action_μ_X, AlgebraicGeometry.PPowerWeighted.pointEval_action_μ_X, AlgebraicGeometry.PPowerWeighted.pointStabilizer_eq_rootsUnitsSubgroup, AlgebraicGeometry.PPowerWeighted.pointStabilizer_eq_top, AlgebraicGeometry.PPowerWeighted.isPointInStratum_smulPoint, AlgebraicGeometry.PPowerWeighted.isPointInStratumInf_smulPoint
statement: formalized
proof: formalized
---

# 101.29 Stratification by gerbes

Section 101.29 of the Stacks Project, [Tag 06RB](https://stacks.math.columbia.edu/tag/06RB). 4 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06RC, a proposition

[Tag 06RC](https://stacks.math.columbia.edu/tag/06RC) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubstack_dense_isGerbe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DenseOpenGerbe.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DenseOpenGerbe.lean#L610).

> **Stacks 06RC.** Let `𝒳` be a reduced algebraic stack over `S` whose inertia projection
> `I_𝒳 ⟶ 𝒳` is quasi-compact. Then there is a dense open substack `𝒰 ⊆ 𝒳` which is a gerbe.
>
> The proof is the source's. Choose a presentation `[U/R] ⟶ 𝒳` whose chart `U ⟶ 𝒳` is smooth and
> surjective (Stacks 04T3); `U` is reduced (Stacks 04YF) and the stabilizer `G ⟶ U` is the base
> change of `I_𝒳 ⟶ 𝒳` (Stacks 06PR), hence of finite type (Stacks 050Q). Generic flatness
> (Stacks 06QS) gives a dense open `W ⊆ U` over which `G` is flat and locally of finite
> presentation. The image `Ω` of `|W|` in `|𝒳|` is open, `W ⟶ 𝒳` being smooth, and dense; `𝒰` is the
> open substack with `|𝒰| = Ω` (Stacks 06FJ), through which `W ⟶ 𝒳` factors by a smooth surjective
> 1-morphism. By Stacks 06R5 and Stacks 06PR the base change of `I_𝒰 ⟶ 𝒰` along `W ⟶ 𝒰` is
> `G ×_U W ⟶ W`, so `I_𝒰 ⟶ 𝒰` is flat and locally of finite presentation, and `𝒰` is a gerbe by
> Stacks 06QJ.

```lean
theorem exists_openSubstack_dense_isGerbe (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hred : IsReducedStack B S hS 𝒳)
    (hqc : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    ∃ W : OpenSubstack 𝒳, @Dense _ (pointTopology B S hS 𝒳.val) (W.pointSet B S hS) ∧
      AlgebraicStacks.IsGerbe B S hS
        (fullSubcategoryAlgebraicStack 𝒳 W.property W.isAlgebraic)
```

## Tag 06RE, an example

[Tag 06RE](https://stacks.math.columbia.edu/tag/06RE) in the Stacks Project.

**`AlgebraicGeometry.PPowerWeighted.action`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExample.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExample.lean#L89). The attribute's comment: “the weighted multiplicative-group action on Spec k[x\_0, x\_1, x\_2, ...]”.

> **Stacks 06RE.** The action of the multiplicative group scheme on
> `U = Spec(k[x_0, x_1, x_2, …])` attached to the grading giving `x_i` the degree `p^i`, namely
> `t · (x_0, x_1, x_2, …) = (t x_0, t^p x_1, t^{p^2} x_2, …)`.

```lean
noncomputable def action (k : Type u) [CommRing k] (p : ℕ) : GradedGmAction (grading k p)
```

**`AlgebraicGeometry.PPowerWeighted.action_μ_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExample.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExample.lean#L95). The attribute's comment: “the coaction on the variables: x\_i goes to x\_i tensor T^\{p^i}”.

> **Stacks 06RE.** The coaction of the action sends the variable `x_i` to `x_i ⊗ T^{p^i}`:
> the group element `t` scales the coordinate `x_i` by `t^{p^i}`.

```lean
theorem action_μ_X (k : Type u) [CommRing k] (p i : ℕ) :
    (action k p).μ (MvPolynomial.X i) =
      (MvPolynomial.X i : MvPolynomial ℕ k) ⊗ₜ[ℤ] LaurentPolynomial.T ((p : ℤ) ^ i)
```

**`AlgebraicGeometry.PPowerWeighted.pointEval_action_μ_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L231). The attribute's comment: “the action on points is the one the coaction defines”.

> **Stacks 06RE.** The action on points is the action the registered coaction defines:
> evaluating the coaction of `x_i` at a point `φ` of `U` and a unit `t` gives the `i`-th
> coordinate `t^{p^i} φ(x_i)` of `t · φ`.  So `smulPoint` is the action of
> `AlgebraicGeometry.PPowerWeighted.action` and not a second one.

```lean
theorem pointEval_action_μ_X (k : Type u) [CommRing k] (p i : ℕ)
    (φ : MvPolynomial ℕ k →+* R) (t : Rˣ) :
    pointEval φ t ((action k p).μ (MvPolynomial.X i)) =
      smulPoint p t (fun j => φ (MvPolynomial.X j)) i
```

**`AlgebraicGeometry.PPowerWeighted.pointStabilizer_eq_rootsUnitsSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L287). The attribute's comment: “the stabilizer along the stratum X\_i is mu\_\{p^i}”.

> **Stacks 06RE.** On the `i`-th stratum the stabilizer of the weighted action is `μ_{p^i}`:
> a unit `t` fixes a point whose first nonvanishing coordinate is the `i`-th exactly when
> `t^{p^i} = 1`.  The subgroup `AlgebraicGeometry.rootsUnitsSubgroup n` of the units is the value
> at `R` of the functor of points of the group scheme `μ_n`
> (`AlgebraicGeometry.rootsOfUnitySections_representableBy_rootsOfUnity`).

```lean
theorem pointStabilizer_eq_rootsUnitsSubgroup (p i : ℕ) (a : ℕ → R)
    (ha : IsPointInStratum i a) :
    pointStabilizer p a = rootsUnitsSubgroup (p ^ i)
```

**`AlgebraicGeometry.PPowerWeighted.pointStabilizer_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L314). The attribute's comment: “the stabilizer along the stratum X\_infinity is G\_m”.

> **Stacks 06RE.** On the last stratum, where all the coordinates vanish, the stabilizer of
> the weighted action is all of `G_m`: the unit group of `R` is the value at `R` of the functor of
> points of the multiplicative group scheme
> (`AlgebraicGeometry.unitsOfGlobalSections_representableBy_multiplicativeGroup`).

```lean
theorem pointStabilizer_eq_top (p : ℕ) (a : ℕ → R) (ha : IsPointInStratumInf a) :
    pointStabilizer p a = ⊤
```

**`AlgebraicGeometry.PPowerWeighted.isPointInStratum_smulPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L321). The attribute's comment: “the stratum X\_i is invariant under the action”.

> **Stacks 06RE.** The `i`-th stratum is invariant under the action.

```lean
theorem isPointInStratum_smulPoint (p i : ℕ) (t : Rˣ) (a : ℕ → R) :
    IsPointInStratum i (smulPoint p t a) ↔ IsPointInStratum i a
```

**`AlgebraicGeometry.PPowerWeighted.isPointInStratumInf_smulPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L330). The attribute's comment: “the stratum X\_infinity is invariant under the action”.

> **Stacks 06RE.** The last stratum is invariant under the action.

```lean
theorem isPointInStratumInf_smulPoint (p : ℕ) (t : Rˣ) (a : ℕ → R) :
    IsPointInStratumInf (smulPoint p t a) ↔ IsPointInStratumInf a
```

**`AlgebraicGeometry.PPowerWeighted.isPointInStratumInf_or_exists_isPointInStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L350). The attribute's comment: “the strata cover: every point lies in exactly one stratum”.

> **Stacks 06RE.** The strata cover `U`: a point with values in a field either has all its
> coordinates zero, or lies in the stratum indexed by the first index where it does not vanish.

```lean
theorem isPointInStratumInf_or_exists_isPointInStratum {K : Type*} [Field K] (a : ℕ → K) :
    IsPointInStratumInf a ∨ ∃ i, IsPointInStratum i a
```

**`AlgebraicGeometry.PPowerWeighted.isLocallyClosed_stratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L394). The attribute's comment: “the stratum X\_i is locally closed”.

> **Stacks 06RE.** The `i`-th stratum is locally closed: it is the intersection of the open
> where `x_i` is invertible with the closed subscheme where `x_0, …, x_{i-1}` vanish.

```lean
theorem isLocallyClosed_stratum (i : ℕ) : IsLocallyClosed (stratum k i)
```

**`AlgebraicGeometry.PPowerWeighted.isClosed_stratumInf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L401). The attribute's comment: “the stratum X\_infinity is closed, hence locally closed”.

> **Stacks 06RE.** The last stratum is closed, being the vanishing locus of all the
> coordinates.

```lean
theorem isClosed_stratumInf : IsClosed (stratumInf k)
```

**`AlgebraicGeometry.PPowerWeighted.iUnion_stratum_union_stratumInf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L419). The attribute's comment: “the strata cover the space”.

> **Stacks 06RE.** The strata cover `U`: a point of the spectrum either kills all the
> coordinates, or lies in the stratum indexed by the first coordinate it does not kill.

```lean
theorem iUnion_stratum_union_stratumInf :
    (⋃ i, stratum k i) ∪ stratumInf k = Set.univ
```

**`AlgebraicGeometry.PPowerWeighted.mem_stratum_ker_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L431). The attribute's comment: “the strata on points and on the spectrum are the same”.

> **Stacks 06RE.** The two readings of the `i`-th stratum agree: a point of `U` with values in
> a field lies in the `i`-th stratum in the sense of `IsPointInStratum` exactly when the prime it
> defines lies in `stratum`.

```lean
theorem mem_stratum_ker_iff {K : Type*} [Field K] (φ : MvPolynomial ℕ k →+* K) (i : ℕ) :
    (⟨RingHom.ker φ, RingHom.ker_isPrime φ⟩ : PrimeSpectrum (MvPolynomial ℕ k)) ∈
        stratum k i ↔
      IsPointInStratum i (fun j => φ (MvPolynomial.X j))
```

**`AlgebraicGeometry.PPowerWeighted.mem_stratumInf_ker_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L440). The attribute's comment: “the last stratum on points and on the spectrum is the same”.

> **Stacks 06RE.** The two readings of the last stratum agree.

```lean
theorem mem_stratumInf_ker_iff {K : Type*} [Field K] (φ : MvPolynomial ℕ k →+* K) :
    (⟨RingHom.ker φ, RingHom.ker_isPrime φ⟩ : PrimeSpectrum (MvPolynomial ℕ k)) ∈
        stratumInf k ↔
      IsPointInStratumInf (fun j => φ (MvPolynomial.X j))
```

**`AlgebraicGeometry.PPowerWeighted.isDomain_stratumRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L516). The attribute's comment: “the stratum X\_i is reduced, being integral”.

> **Stacks 06RE.** The `i`-th stratum is integral, in particular reduced.

```lean
theorem isDomain_stratumRing [IsDomain k] (i : ℕ) : IsDomain (stratumRing k i)
```

**`AlgebraicGeometry.PPowerWeighted.isReduced_stratumRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L525). The attribute's comment: “the stratum X\_i is reduced”.

> **Stacks 06RE.** The `i`-th stratum is reduced.

```lean
theorem isReduced_stratumRing [IsDomain k] (i : ℕ) : IsReduced (stratumRing k i)
```

**`AlgebraicGeometry.PPowerWeighted.isDomain_quotient_coordinateIdeal_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L532). The attribute's comment: “the stratum X\_infinity is reduced”.

> **Stacks 06RE.** The last stratum is reduced: it is the origin, cut out by the prime ideal
> generated by all the coordinates.

```lean
theorem isDomain_quotient_coordinateIdeal_univ [IsDomain k] :
    IsDomain (MvPolynomial ℕ k ⧸ coordinateIdeal k Set.univ)
```

**`AlgebraicGeometry.PPowerWeighted.rootsUnitsSubgroup_pow_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L578). The attribute's comment: “distinct strata have distinct groups mu\_\{p^i}: no coarser stratification”.

> **Stacks 06RE.** Distinct strata have distinct groups: for `1 < p` and `i < j` the group
> `μ_{p^i}` of the stratum `X_i` is not the group `μ_{p^j}` of the stratum `X_j`.  So no two strata
> can be merged into a single locus along which the stabilizer is one group, which is why there is
> no coarser stratification with the same properties.

```lean
theorem rootsUnitsSubgroup_pow_ne (p i j : ℕ) (hp : 1 < p) (hij : i < j) :
    rootsUnitsSubgroup (A := rootsOfUnityCoordinateRing.{u} (p ^ j)) (p ^ i) ≠
      rootsUnitsSubgroup (p ^ j)
```

**`AlgebraicGeometry.PPowerWeighted.rootsUnitsSubgroup_ne_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L587). The attribute's comment: “the group mu\_\{p^i} of X\_i differs from the group G\_m of X\_infinity”.

> **Stacks 06RE.** The group of a stratum `X_i` is never the group `G_m` of the last stratum
> `X_∞`: already in the units of the rationals the `n`-th roots of unity are not everything, since
> `2` is a unit with `2^n ≠ 1`.  So the last stratum cannot be merged with any other one either.

```lean
theorem rootsUnitsSubgroup_ne_top {n : ℕ} (hn : 0 < n) :
    rootsUnitsSubgroup (A := ℚ) n ≠ ⊤
```

**`AlgebraicGeometry.PPowerWeighted.pointStabilizer_ne_pointStabilizer_basisPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L621). The attribute's comment: “the strata X\_i and X\_j cannot be merged: their stabilizers differ”.

> **Stacks 06RE.** The strata `X_i` and `X_j` with `i < j` cannot be merged: already over the
> coordinate ring of `μ_{p^j}` the stabilizer of a point of `X_i` differs from the stabilizer of a
> point of `X_j`, being `μ_{p^i}` against `μ_{p^j}`.  Together with
> `AlgebraicGeometry.PPowerWeighted.pointStabilizer_ne_pointStabilizer_basisPoint_zero` this is the
> source's last assertion, that there is no coarser stratification with the same properties: a
> stratum of a coarser stratification would contain points of two of the strata below and so could
> not be a gerbe with a single group.

```lean
theorem pointStabilizer_ne_pointStabilizer_basisPoint (p i j : ℕ) (hp : 1 < p) (hij : i < j) :
    pointStabilizer p (basisPoint (rootsOfUnityCoordinateRing.{u} (p ^ j)) i) ≠
      pointStabilizer p (basisPoint (rootsOfUnityCoordinateRing.{u} (p ^ j)) j)
```

**`AlgebraicGeometry.PPowerWeighted.pointStabilizer_ne_pointStabilizer_basisPoint_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationExamplePoints.lean#L632). The attribute's comment: “the stratum X\_i cannot be merged with X\_infinity: their stabilizers differ”.

> **Stacks 06RE.** The stratum `X_i` cannot be merged with the last stratum `X_∞`: already over
> the rationals the stabilizer of the point of `X_i` with `i`-th coordinate one is `μ_{p^i}`, while
> the stabilizer of the origin is all of `G_m`.

```lean
theorem pointStabilizer_ne_pointStabilizer_basisPoint_zero (p i : ℕ) (hp : 0 < p) :
    pointStabilizer p (basisPoint ℚ i) ≠ pointStabilizer p (0 : ℕ → ℚ)
```

**`AlgebraicGeometry.PPowerWeighted.quotientStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationQuotientStack.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationQuotientStack.lean#L83). The attribute's comment: “the quotient stack [U/G\_m]”.

> **Stacks 06RE.** The quotient stack `[U/𝐆_m]` of the multiplicative-group action on
> `U = Spec(k[x_0, x_1, x_2, …])` in which `x_i` has weight `p^i`.  It is the quotient stack of
> Stacks 044Q, part (2), for that action, read at the terminal algebraic space of the big fppf
> site over `Spec ℤ`.  The hypothesis is that the site contain `U`.

```lean
noncomputable def quotientStack (hU : 𝒞.Contains (Spec (.of (MvPolynomial ℕ k)))) :
    BasedCategory
      (BigFppfOver 𝒞 (Spec (.of (ULift.{u} ℤ))) (Space.contains_specULiftZ 𝒞))
```

**`AlgebraicGeometry.PPowerWeighted.isAlgebraicStack_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationQuotientStack.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationQuotientStack.lean#L99). The attribute's comment: “the quotient stack [U/G\_m] is an algebraic stack”.

> **Stacks 06RE.** The quotient stack `[U/𝐆_m]` is an algebraic stack over `Spec ℤ`.  This is
> Stacks 04TK for the action: the structure morphism of the group algebraic space
> `B ×_{Spec ℤ} 𝐆_m ⟶ B` is smooth because the Laurent polynomial ring is a smooth algebra, and
> 04TK carries nothing beyond that smoothness.

```lean
theorem isAlgebraicStack_quotientStack
    (hU : 𝒞.Contains (Spec (.of (MvPolynomial ℕ k)))) :
    Stack.IsAlgebraicStack.{u, w} 𝒞 (Spec (.of (ULift.{u} ℤ)))
      (Space.contains_specULiftZ 𝒞) (quotientStack 𝒞 k p hU)
```

**`AlgebraicGeometry.PPowerWeighted.weightedQuotientStack_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L78). The attribute's comment: “X = [U/G\_m] is an algebraic stack: the object of the 2-category of algebraic stacks presented by the action groupoid”.

> **Stacks 06RE**, assertion (1): `𝒳 = [U/𝐆_m]` is an algebraic stack. The algebraic stack
> `weightedQuotientStack` is presented, in the sense of Stacks 04TI, by the action groupoid of `𝐆_m`
> on `U`, whose quotient stack is the `[U/𝐆_m]` of `quotientStack`.

```lean
theorem weightedQuotientStack_presentation :
    ∃ P : Stack.GroupoidPresentation 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
        (weightedQuotientStack.{u, w} 𝒞 k p hU).val.val,
      Stack.quotientStack P.groupoid = quotientStack 𝒞 k p hU
```

**`AlgebraicGeometry.PPowerWeighted.stratumProperty_chart_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L92). The attribute's comment: “the strata X\_i (x\_0 = ... = x\_\{i-1} = 0, x\_i invertible) and X\_infinity (all x\_j = 0)”.

> **Stacks 06RE**, assertion (2), the strata: the stratum of index `i` is the locus where
> `x_0, …, x_{i-1}` vanish and `x_i` does not, and the stratum of index `∞` the locus where all
> `x_j` vanish. Precisely, a point `h : W ⟶ U` with values in any scheme `W` of the site lands in
> `𝒳_i` if and only if `x_0, …, x_{i-1}` pull back to `0` and `x_i` to a unit of `Γ(W, 𝒪_W)`, and in
> `𝒳_∞` if and only if every `x_j` pulls back to `0`.

```lean
theorem stratumProperty_chart_iff {W : BigFppfOver 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)}
    (h : W ⟶ totalSiteObject 𝒞 k hU) :
    (∀ i : ℕ, stratumProperty.{u, w} 𝒞 k p hU i (chartObj.{u, w} p h) ↔
      (∀ j < i, coord h j = 0) ∧ IsUnit (coord h i)) ∧
    (stratumProperty.{u, w} 𝒞 k p hU ⊤ (chartObj.{u, w} p h) ↔ ∀ j, coord h j = 0)
```

**`AlgebraicGeometry.PPowerWeighted.isAlgebraicStack_stratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L108). The attribute's comment: “each stratum is an algebraic stack (locally closed substack)”.

> **Stacks 06RE: each stratum is an algebraic stack.** The full subcategory of `𝒳` on the
> objects of the stratum `𝒳_a` is an algebraic stack, being a locally closed substack of `𝒳`: this
> is the algebraicity component of `isLocallyClosedSubstack_stratumProperty`. It is the algebraic
> stack structure on `𝒳_a` that assertions (2), (3) and (4) below are stated for.

```lean
theorem isAlgebraicStack_stratum (a : WithTop ℕ) :
    Stack.IsAlgebraicStack.{u, w} 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
      (Stack.fullSubcategoryBased (weightedQuotientStack.{u, w} 𝒞 k p hU)
        (stratumProperty.{u, w} 𝒞 k p hU a))
```

**`AlgebraicGeometry.PPowerWeighted.exists_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L122). The attribute's comment: “the strata form a stratification of |X|”.

> **Stacks 06RE**, assertion (2), the stratification: the point sets `|𝒳_a|` of the strata form a
> stratification of `|𝒳|` (Stacks 09Y1) indexed by `ℕ ∪ {∞}` with the reverse order: they are
> pairwise disjoint, cover `|𝒳|`, and the closure of `|𝒳_i|` lies in
> `|𝒳_i| ∪ |𝒳_{i+1}| ∪ ⋯ ∪ |𝒳_∞|`.

```lean
theorem exists_stratification :
    letI := Stack.pointTopology 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
      (weightedQuotientStack.{u, w} 𝒞 k p hU).val
    ∃ σ : Stratification (Stack.AlgebraicStacks.points 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
        (weightedQuotientStack.{u, w} 𝒞 k p hU)) (WithTop ℕ)ᵒᵈ,
      ∀ a : WithTop ℕ,
        σ.strata (OrderDual.toDual a) =
          Set.range (Stack.AlgebraicStacks.pointsMap 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
            (Stack.fullSubcategoryInclusion (weightedQuotientStack.{u, w} 𝒞 k p hU)
              (stratumProperty.{u, w} 𝒞 k p hU a)
              (isAlgebraicStack_stratum.{u, w} 𝒞 k p hU a)))
```

**`AlgebraicGeometry.PPowerWeighted.isReduced_isLocallyClosedSubstack_stratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L141). The attribute's comment: “the strata are reduced locally closed substacks”.

> **Stacks 06RE**, assertion (4): every stratum is a reduced locally closed substack of `𝒳`.

```lean
theorem isReduced_isLocallyClosedSubstack_stratum (a : WithTop ℕ) :
    Stack.IsLocallyClosedSubstack (weightedQuotientStack.{u, w} 𝒞 k p hU)
        (stratumProperty.{u, w} 𝒞 k p hU a) ∧
      Stack.IsReducedStack 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
        (Stack.fullSubcategoryAlgebraicStack (weightedQuotientStack.{u, w} 𝒞 k p hU)
          (stratumProperty.{u, w} 𝒞 k p hU a) (isAlgebraicStack_stratum.{u, w} 𝒞 k p hU a))
```

**`AlgebraicGeometry.PPowerWeighted.isGerbeOverSchemeWithGroup_algebraicStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L155). The attribute's comment: “each stratum is a gerbe over a scheme with group mu\_\{p^i} for X\_i and G\_m for X\_infinity”.

> **Stacks 06RE**, assertion (3): each stratum is a gerbe over a scheme, with group `μ_{p^i}`
> for `𝒳_i` and `𝐆_m` for `𝒳_∞`.

```lean
theorem isGerbeOverSchemeWithGroup_algebraicStratum (a : WithTop ℕ) :
    haveI : NeZero p := ⟨hp.out.ne_zero⟩
    Stack.AlgebraicStacks.IsGerbeOverSchemeWithGroup 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
      (Stack.fullSubcategoryAlgebraicStack (weightedQuotientStack.{u, w} 𝒞 k p hU)
        (stratumProperty.{u, w} 𝒞 k p hU a) (isAlgebraicStack_stratum.{u, w} 𝒞 k p hU a))
      (stratumGroup.{u} p a)
```

**`AlgebraicGeometry.PPowerWeighted.stratification_minimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratificationStatement.lean#L169). The attribute's comment: “there is no coarser stratification by reduced locally closed gerbes over schemes”.

> **Stacks 06RE**, assertion (5): there is no coarser stratification with the same properties.
> If a topological partition of `|𝒳|` (Stacks 09XZ) consists of the point sets of reduced locally
> closed substacks of `𝒳` each of which is a gerbe over a scheme, and the strata `|𝒳_a|` refine it,
> then it is the partition by the strata.

```lean
theorem stratification_minimal :
    letI := Stack.pointTopology 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
      (weightedQuotientStack.{u, w} 𝒞 k p hU).val
    ∀ Qs : Set (Set (Stack.AlgebraicStacks.points 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
        (weightedQuotientStack.{u, w} 𝒞 k p hU))),
      IsTopologicalPartition Qs →
      (∀ s ∈ Qs, ∃ (W : ObjectProperty (weightedQuotientStack.{u, w} 𝒞 k p hU).val.val.obj)
          (_ : Stack.IsLocallyClosedSubstack (weightedQuotientStack.{u, w} 𝒞 k p hU) W),
        (∀ hA, Stack.IsReducedStack 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
            (Stack.fullSubcategoryAlgebraicStack (weightedQuotientStack.{u, w} 𝒞 k p hU) W hA) ∧
          Stack.AlgebraicStacks.IsGerbeOverScheme 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
            (Stack.fullSubcategoryAlgebraicStack (weightedQuotientStack.{u, w} 𝒞 k p hU) W hA)) ∧
        ∀ hA, Set.range (Stack.AlgebraicStacks.pointsMap 𝒞 𝒵 (Space.contains_specULiftZ 𝒞)
          (Stack.fullSubcategoryInclusion (weightedQuotientStack.{u, w} 𝒞 k p hU) W hA)) = s) →
      local_Refines (Set.range (stratumPoints.{u, w} 𝒞 k p hU)) Qs →
      Qs = Set.range (stratumPoints.{u, w} 𝒞 k p hU)
```

## Tag 06RF, a lemma

[Tag 06RF](https://stacks.math.columbia.edu/tag/06RF) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_gerbe_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratification.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratification.lean#L565). The attribute's comment: “existence of the stratification, arranged as in (a), with strata as large as possible, and as in (b)”.

> **Stacks 06RF, the stratifications (a) and (b).** Let `𝒳` be an algebraic stack over `S`
> whose inertia projection `I_𝒳 ⟶ 𝒳` is quasi-compact. Then there are a well-ordered index set
> `I` and for every `i ∈ I` a reduced locally closed substack `𝒰ᵢ ⊆ 𝒳` such that
>
> 1. each `𝒰ᵢ` is a gerbe,
> 2. `|𝒳| = ⋃ᵢ |𝒰ᵢ|`,
> 3. `Tᵢ = |𝒳| \ ⋃_{i' < i} |𝒰ᵢ'|` is closed in `|𝒳|`, and
> 4. `|𝒰ᵢ|` is open in `Tᵢ`,
>
> and this can be arranged so that (a) `|𝒰ᵢ|` is dense in `Tᵢ` for every `i`, with `𝒰ᵢ` chosen as
> large as possible: `|𝒰ᵢ|` is the set of points of `Tᵢ` lying in an open substack, which is a
> gerbe, of the reduced closed substack with points `Tᵢ` (`maximalGerbePointSet`); and also so that
> (b) every `𝒰ᵢ` is quasi-compact. Here `|𝒰ᵢ|` is the image of the points of `𝒰ᵢ` in `|𝒳|`. The
> stratification of case (a) is canonical: `exists_gerbe_stratification_unique`.

```lean
theorem exists_gerbe_stratification
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    (∃ (I : Type (u + 2)) (_ : LinearOrder I) (_ : WellFoundedLT I)
      (Q : I → ObjectProperty 𝒳.val.val.obj)
      (hQ : ∀ i, IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 (Q i))),
      (∀ i, IsLocallyClosedSubstack 𝒳 (Q i) ∧
        IsReducedStack B S hS (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i)) ∧
        AlgebraicStacks.IsGerbe B S hS (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i))) ∧
      (⋃ i, Set.range (AlgebraicStacks.pointsMap B S hS
        (fullSubcategoryInclusion 𝒳 (Q i) (hQ i)))) = Set.univ ∧
      (∀ i, @IsClosed _ (pointTopology B S hS 𝒳.val) (Set.univ \ ⋃ (j : I) (_ : j < i),
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 (Q j) (hQ j))))) ∧
      (∀ i, ∃ O, @IsOpen _ (pointTopology B S hS 𝒳.val) O ∧
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 (Q i) (hQ i))) =
          (Set.univ \ ⋃ (j : I) (_ : j < i), Set.range (AlgebraicStacks.pointsMap B S hS
            (fullSubcategoryInclusion 𝒳 (Q j) (hQ j)))) ∩ O) ∧
      (∀ i, (Set.univ \ ⋃ (j : I) (_ : j < i), Set.range (AlgebraicStacks.pointsMap B S hS
          (fullSubcategoryInclusion 𝒳 (Q j) (hQ j)))) ⊆
        @closure _ (pointTopology B S hS 𝒳.val) (Set.range (AlgebraicStacks.pointsMap B S hS
          (fullSubcategoryInclusion 𝒳 (Q i) (hQ i)))) ∧
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 (Q i) (hQ i))) =
          maximalGerbePointSet B S hS 𝒳 (Set.univ \ ⋃ (j : I) (_ : j < i),
            Set.range (AlgebraicStacks.pointsMap B S hS
              (fullSubcategoryInclusion 𝒳 (Q j) (hQ j)))))) ∧
    (∃ (I : Type (u + 2)) (_ : LinearOrder I) (_ : WellFoundedLT I)
      (Q : I → ObjectProperty 𝒳.val.val.obj)
      (hQ : ∀ i, IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 (Q i))),
      (∀ i, IsLocallyClosedSubstack 𝒳 (Q i) ∧
        IsReducedStack B S hS (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i)) ∧
        AlgebraicStacks.IsGerbe B S hS (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i))) ∧
      (⋃ i, Set.range (AlgebraicStacks.pointsMap B S hS
        (fullSubcategoryInclusion 𝒳 (Q i) (hQ i)))) = Set.univ ∧
      (∀ i, @IsClosed _ (pointTopology B S hS 𝒳.val) (Set.univ \ ⋃ (j : I) (_ : j < i),
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 (Q j) (hQ j))))) ∧
      (∀ i, ∃ O, @IsOpen _ (pointTopology B S hS 𝒳.val) O ∧
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 (Q i) (hQ i))) =
          (Set.univ \ ⋃ (j : I) (_ : j < i), Set.range (AlgebraicStacks.pointsMap B S hS
            (fullSubcategoryInclusion 𝒳 (Q j) (hQ j)))) ∩ O) ∧
      (∀ i, IsQuasiCompactStack.{u, w} B S hS (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i)).val
        (fullSubcategoryAlgebraicStack 𝒳 (Q i) (hQ i)).property))
```

**`AlgebraicGeometry.Stack.exists_gerbe_stratification_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratification.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeStratification.lean#L630). The attribute's comment: “canonicity of the stratification (a) with strata as large as possible”.

> **Stacks 06RF, the canonical stratification (a).** A stratification of `|𝒳|` as in Stacks
> 06RF whose strata are chosen as large as possible is unique: if two well-ordered families of
> nonempty sets of points `Wᵢ` cover `|𝒳|` and each `Wᵢ` is the largest gerbe
> (`maximalGerbePointSet`) in `Tᵢ = |𝒳| \ ⋃_{j < i} Wⱼ`, then the index sets are order-isomorphic
> with the same sets.

```lean
theorem exists_gerbe_stratification_unique (𝒳 : AlgebraicStacks.{u, w} B S hS)
    {I : Type*} [LinearOrder I] [WellFoundedLT I] (W : I → Set (AlgebraicStacks.points B S hS 𝒳))
    (hW : ∀ i, W i = maximalGerbePointSet B S hS 𝒳 (Set.univ \ ⋃ (j : I) (_ : j < i), W j))
    (hWne : ∀ i, (W i).Nonempty) (hWcov : (⋃ i, W i) = Set.univ)
    {I' : Type*} [LinearOrder I'] [WellFoundedLT I']
    (W' : I' → Set (AlgebraicStacks.points B S hS 𝒳))
    (hW' : ∀ i, W' i = maximalGerbePointSet B S hS 𝒳 (Set.univ \ ⋃ (j : I') (_ : j < i), W' j))
    (hW'ne : ∀ i, (W' i).Nonempty) (hW'cov : (⋃ i, W' i) = Set.univ) :
    ∃ e : I ≃o I', ∀ i, W' (e i) = W i
```

## Tag 06RG, a remark

[Tag 06RG](https://stacks.math.columbia.edu/tag/06RG) in the Stacks Project.

**`AlgebraicGeometry.Stack.CanonicalGerbeStratificationIndexCountable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CanonicalGerbeStratification.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/CanonicalGerbeStratification.lean#L178). The attribute's comment: “the open question of the remark, stated as a proposition; neither it nor its negation is proved”.

> **The question of Stacks 06RG.** For every algebraic stack `𝒳` over a scheme `S` whose inertia
> projection `I_𝒳 ⟶ 𝒳` is quasi-compact (the setting of Stacks 06RF), the well-ordered index set `I`
> of the canonical stratification of type (a) (`canonicalGerbeStratificationIndex`) has cardinality
> at most `ℵ₀`.
>
> This is the "natural guess" of the remark Stacks 06RG about the order type of the canonical
> stratifications. The Stacks project does not know whether it is true or false; it is stated here
> as a proposition, and neither it nor its negation is proved. By
> `canonicalGerbeStratificationIndexCountable_iff` it says equally that every stratification of type
> (a) with strata as large as possible has a countable index set.

```lean
def CanonicalGerbeStratificationIndexCountable : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.29, Tag 06RB](https://stacks.math.columbia.edu/tag/06RB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
