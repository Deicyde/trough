---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint, AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_exists_isAssociatedPoint_restrictToChart, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_forall_isAssociatedPoint_restrictToChart, AlgebraicGeometry.Space.exists_isAssociatedPoint_restrictToChart_iff_forall, AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPrime, AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isAssociatedPrimeStacks, AlgebraicGeometry.Space.isWeaklyAssociatedPrime_maximalIdeal_iff_isAssociatedPrimeStacks
statement: formalized
proof: formalized
---

# 71.2 Associated and weakly associated points

Section 71.2 of the Stacks Project, [Tag 0CTV](https://stacks.math.columbia.edu/tag/0CTV). 12 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CTW, a lemma

[Tag 0CTW](https://stacks.math.columbia.edu/tag/0CTW) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreChartScheme.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFibreChartScheme.lean#L94). The attribute's comment: “conditions (1) and (2) at a point of a chart scheme, with no geometric point in the statement”.

> **Zariski and étale weak association agree at a point of a chart scheme.** Let `F` be a
> quasi-coherent `𝒪_Z`-module and let `w` be a point of the scheme of an étale chart `W` of `Z`.
> Then `w` is weakly associated to the restriction `F|_W`, in the Zariski sense of Stacks 056L,
> exactly when the point of `Z` it lies over is weakly associated to `F` in the sense of
> Stacks 0CTX.

```lean
theorem isWeaklyAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint
    (Z : AlgebraicSpaces B S hS) (F : Modules.{u, u} B S hS Z.1 Z.2)
    [F.IsQuasicoherentOnSite] (W : SmallEtale B S hS Z.1) (w : chartScheme W) :
    Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS Z.2 F W) w ↔
      IsWeaklyAssociatedPoint B S hS Z F (chartSchemeToPoints B S hS Z.1 W w)
```

**`AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L99). The attribute's comment: “conditions (4) and (5) at a point of a chart scheme”.

> **Stacks 0CTW, conditions (4) and (5) at a point of a chart scheme.** Let `X` be a locally
> Noetherian algebraic space, `F` a quasi-coherent `𝒪_X`-module and `w` a point of the scheme of
> an étale chart `W` of `X`. Then `w` is *associated* to the restriction `F|_W`, in the Zariski
> sense of Stacks 02OJ, exactly when the point of `X` it lies over is weakly associated to `F` in
> the sense of Stacks 0CTX.
>
> The chart's scheme is locally Noetherian by Stacks 03E8, so the maximal ideal of `𝒪_{W, w}` is
> finitely generated and association at `w` is weak association at `w` by Stacks 05AR; that is
> conditions (1) and (2).

```lean
theorem isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPoint
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (W : SmallEtale B S hS X.1) (w : chartScheme W) :
    Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F W) w ↔
      IsWeaklyAssociatedPoint B S hS X F (chartSchemeToPoints B S hS X.1 W w)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_exists_isAssociatedPoint_restrictToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L116). The attribute's comment: “condition (4)”.

> **Stacks 0CTW, condition (4).** Let `X` be a locally Noetherian algebraic space and `F` a
> quasi-coherent `𝒪_X`-module. A point `x` of `X` is weakly associated to `F` exactly when there
> is *some* étale scheme chart `W` of `X` and some point `w` of its scheme above `x` which is
> associated to the restriction `F|_W`.

```lean
theorem isWeaklyAssociatedPoint_iff_exists_isAssociatedPoint_restrictToChart
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X F x ↔
      ∃ (W : SmallEtale B S hS X.1) (w : chartScheme W),
        chartSchemeToPoints B S hS X.1 W w = x ∧
          Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F W) w
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_forall_isAssociatedPoint_restrictToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L136). The attribute's comment: “condition (5)”.

> **Stacks 0CTW, condition (5).** Let `X` be a locally Noetherian algebraic space and `F` a
> quasi-coherent `𝒪_X`-module. A point `x` of `X` is weakly associated to `F` exactly when
> *every* point of the scheme of *every* étale chart of `X` lying above `x` is associated to the
> restriction of `F` to that chart.

```lean
theorem isWeaklyAssociatedPoint_iff_forall_isAssociatedPoint_restrictToChart
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X F x ↔
      ∀ (W : SmallEtale B S hS X.1) (w : chartScheme W),
        chartSchemeToPoints B S hS X.1 W w = x →
          Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F W) w
```

**`AlgebraicGeometry.Space.exists_isAssociatedPoint_restrictToChart_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L156). The attribute's comment: “conditions (4) and (5)”.

> **Stacks 0CTW, conditions (4) and (5).** On a locally Noetherian algebraic space ordinary
> association of some point of some étale scheme chart above `x` is ordinary association of every
> point of every such chart.

```lean
theorem exists_isAssociatedPoint_restrictToChart_iff_forall
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    (∃ (W : SmallEtale B S hS X.1) (w : chartScheme W),
        chartSchemeToPoints B S hS X.1 W w = x ∧
          Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F W) w) ↔
      ∀ (W : SmallEtale B S hS X.1) (w : chartScheme W),
        chartSchemeToPoints B S hS X.1 W w = x →
          Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F W) w
```

**`AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L177). The attribute's comment: “conditions (4) and (5) against condition (3)”.

> **Stacks 0CTW, conditions (4) and (5) against condition (3).** Let `X` be a locally
> Noetherian algebraic space, `F` a quasi-coherent `𝒪_X`-module and `φ : (U, ū) → (X, x̄)` an
> étale neighbourhood of a geometric point whose chart `U` is a scheme. Then `u` is associated to
> `φ^*F` exactly when the maximal ideal of `𝒪_{X, x̄}` is a weakly associated prime of the
> geometric stalk `F_{x̄}`.

```lean
theorem isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPrime
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] :
    Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
        (chartPoint B S hS X.1 V) ↔
      letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
        isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
      letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
        (geometricModuleStalk B S hS X xbar F).isModule
      IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
        (geometricModuleStalk B S hS X xbar F)
        (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))
```

**`AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isAssociatedPrimeStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AssociatedPointsChartTFAE.lean#L200). The attribute's comment: “conditions (4) and (5) against condition (6)”.

> **Stacks 0CTW, conditions (4) and (5) against condition (6).** In the situation of
> `AlgebraicGeometry.Space.isAssociatedPoint_restrictToChart_iff_isWeaklyAssociatedPrime`, `u` is
> associated to `φ^*F` exactly when the maximal ideal of the étale local ring `𝒪_{X, x̄}` is an
> associated prime of the geometric stalk `F_{x̄}`.

```lean
theorem isAssociatedPoint_restrictToChart_iff_isAssociatedPrimeStacks
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] :
    letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
      isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
    letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
      (geometricModuleStalk B S hS X xbar F).isModule
    (Stacks.Divisors.IsAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
        (chartPoint B S hS X.1 V) ↔
      IsAssociatedPrimeStacks (etaleLocalRing B S hS X.1 xbar)
        (geometricModuleStalk B S hS X xbar F)
        (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar)))
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPrime_maximalIdeal_iff_isAssociatedPrimeStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L236). The attribute's comment: “conditions (3) and (6) at a geometric point”.

> **Stacks 0CTW, (3) ⟺ (6).** Let `F` be an `𝒪_X`-module on an algebraic space and `x̄` a
> geometric point of `X` at which the maximal ideal of `𝒪_{X, x̄}` is finitely generated. That
> maximal ideal is a weakly associated prime of the geometric stalk `F_{x̄}` if and only if it is
> an associated prime of `F_{x̄}`.

```lean
theorem isWeaklyAssociatedPrime_maximalIdeal_iff_isAssociatedPrimeStacks
    (F : Modules.{u, m} B S hS X.1 X.2) (xbar : GeometricPoint B S hS X.1) :
    letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
      isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
    letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
      (geometricModuleStalk B S hS X xbar F).isModule
    (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar)).FG →
      (IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar)) ↔
        IsAssociatedPrimeStacks (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar)))
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_exists_isAssociatedPrimeStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L255). The attribute's comment: “conditions (3) and (6) on a Noetherian algebraic space”.

> **Stacks 0CTW, (3) ⟺ (6)** on a Noetherian algebraic space: a point is weakly associated to
> an `𝒪_X`-module exactly when, at some geometric point above it, the maximal ideal of the étale
> local ring is an associated prime of the geometric stalk.

```lean
theorem isWeaklyAssociatedPoint_iff_exists_isAssociatedPrimeStacks
    (hZ : B.Contains (⊤_ Scheme.{u})) (hNoetherian : IsNoetherian B S hS hZ X.1)
    (F : Modules.{u, m} B S hS X.1 X.2) (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X F x ↔
      ∃ xbar : GeometricPoint B S hS X.1, xbar.LiesOver x ∧
        letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
          isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
        letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
          (geometricModuleStalk B S hS X xbar F).isModule
        IsAssociatedPrimeStacks (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))
```

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_eq_setOf_exists_isAssociatedPrimeStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L279). The attribute's comment: “conditions (3) and (6) as a set of points”.

> **Stacks 0CTW, (3) ⟺ (6)** on a Noetherian algebraic space, as an equality of sets of
> points: `WeakAss(F)` is the set of points carrying a geometric point at whose stalk the maximal
> ideal of the étale local ring is an associated prime.

```lean
theorem weaklyAssociatedPoints_eq_setOf_exists_isAssociatedPrimeStacks
    (hZ : B.Contains (⊤_ Scheme.{u})) (hNoetherian : IsNoetherian B S hS hZ X.1)
    (F : Modules.{u, m} B S hS X.1 X.2) :
    weaklyAssociatedPoints B S hS X F =
      {x : points B S hS X.1 | ∃ xbar : GeometricPoint B S hS X.1, xbar.LiesOver x ∧
        letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
          isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
        letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
          (geometricModuleStalk B S hS X xbar F).isModule
        IsAssociatedPrimeStacks (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))}
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPrime_maximalIdeal_geometricModuleStalk_of_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L325). The attribute's comment: “condition (1) implies condition (3) at a geometric point”.

> **Stacks 0CTW, (1) ⟹ (3).** Let `F` be a quasi-coherent `𝒪_X`-module and let
> `φ : (U, ū) → (X, x̄)` be an étale neighbourhood of a geometric point `x̄` whose chart `U` is a
> scheme. If `u` is weakly associated to `φ^*F`, then the maximal ideal of `𝒪_{X, x̄}` is a weakly
> associated prime of the geometric stalk `F_{x̄}`.
>
> By Stacks 05VP the geometric stalk is `(φ^*F)_u ⊗_{𝒪_{U, u}} 𝒪_{X, x̄}` and the comparison map
> is flat and carries the maximal ideal of `𝒪_{U, u}` onto that of `𝒪_{X, x̄}`.

```lean
theorem isWeaklyAssociatedPrime_maximalIdeal_geometricModuleStalk_of_chart
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (h : Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
      (chartPoint B S hS X.1 V)) :
    letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
      isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
    letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
      (geometricModuleStalk B S hS X xbar F).isModule
    IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
      (geometricModuleStalk B S hS X xbar F)
      (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L365). The attribute's comment: “condition (3) implies condition (1) at an étale neighbourhood”.

> **Stacks 0CTW, (3) ⟹ (1).** Let `F` be a quasi-coherent `𝒪_X`-module and let
> `φ : (U, ū) → (X, x̄)` be an étale neighbourhood of a geometric point `x̄` whose chart `U` is a
> scheme. If the maximal ideal of `𝒪_{X, x̄}` is a weakly associated prime of `F_{x̄}` then `u` is
> weakly associated to `φ^*F`.
>
> This is the descent of weak association from a strict henselization, Stacks 0CTU: the étale
> local ring at `x̄` is the strict henselization of `𝒪_{U, u}` chosen in
> `AlgebraicGeometry.Space.chartHenselizationTower` by Stacks 04KF, and the geometric stalk is the
> base change of the Zariski stalk `(φ^*F)_u` along it by Stacks 05VP.

```lean
theorem isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (h : letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
          isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
        letI : Module (etaleLocalRing B S hS X.1 xbar)
            (geometricModuleStalk B S hS X xbar F) :=
          (geometricModuleStalk B S hS X xbar F).isModule
        IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))) :
    Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
      (chartPoint B S hS X.1 V)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L432). The attribute's comment: “condition (3) implies condition (1) at a chart whose Zariski module stalk has finitely many weakly associated primes”.

> **Stacks 0CTW, (3) ⟹ (1), by flat descent over finitely many weakly associated primes.**
> The conclusion of
> `AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime`,
> reached instead by flat descent of weak association along the comparison map of Stacks 05VP,
> under finiteness of the set of weakly associated primes of the Zariski module stalk of the
> chart.
>
> `Stacks.WeaklyAssociatedPrimes.isWeaklyAssociatedPrime_comap_tensorProduct`, used here, turns
> the covering of the maximal ideal by the weakly associated primes of the localization into an
> equality by prime avoidance over finitely many primes. That is not the source's own route:
> Stacks 0CTW proves (1), (2) and (3) equivalent with nothing beyond quasi-coherence, by
> More on Flatness, Lemma 38.2.9, which is Tag 0CTU, and which
> `AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime`
> above now takes. This form is retained as the one a local finiteness statement about the weakly
> associated points of the chart discharges directly, since the primes of the local ring at a
> point all lie in every neighbourhood of it.

```lean
theorem isWeaklyAssociatedPoint_restrictToChart_of_isWeaklyAssociatedPrime_of_finite
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hfin : (weaklyAssociatedPrimes (chartLocalRing B S hS X.1 V)
      (chartZariskiModuleStalk B S hS X.1 X.2 V F)).Finite)
    (h : letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
          isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
        letI : Module (etaleLocalRing B S hS X.1 xbar)
            (geometricModuleStalk B S hS X xbar F) :=
          (geometricModuleStalk B S hS X xbar F).isModule
        IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
          (geometricModuleStalk B S hS X xbar F)
          (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))) :
    Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
      (chartPoint B S hS X.1 V)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L474). The attribute's comment: “conditions (1) and (3) at an étale neighbourhood”.

> **Stacks 0CTW, (1) ⟺ (3)** at an étale neighbourhood: the point `u` of the chart is weakly
> associated to `φ^*F` exactly when the maximal ideal of `𝒪_{X, x̄}` is a weakly associated prime
> of `F_{x̄}`.

```lean
theorem isWeaklyAssociatedPoint_restrictToChart_iff
    {xbar : GeometricPoint B S hS X.1} (V : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] :
    Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
        (chartPoint B S hS X.1 V) ↔
      letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
        isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
      letI : Module (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F) :=
        (geometricModuleStalk B S hS X xbar F).isModule
      IsWeaklyAssociatedPrime (etaleLocalRing B S hS X.1 xbar)
        (geometricModuleStalk B S hS X xbar F)
        (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar))
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_isWeaklyAssociatedPoint_restrictToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L493). The attribute's comment: “condition (1) implies the weak association of Stacks 0CTX”.

> **Stacks 0CTW, (1) ⟹ (3) in the form of Stacks 0CTX.** If the point `u` of an étale scheme
> chart is weakly associated to `φ^*F` then the point of `X` it lies over is weakly associated
> to `F`.

```lean
theorem isWeaklyAssociatedPoint_of_isWeaklyAssociatedPoint_restrictToChart
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1)
    {xbar : GeometricPoint B S hS X.1} (hxbar : xbar.LiesOver x)
    (V : SmallEtaleNeighborhood xbar)
    (h : Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
      (chartPoint B S hS X.1 V)) :
    IsWeaklyAssociatedPoint B S hS X F x
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_restrictToChart_of_restrictToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L507). The attribute's comment: “conditions (1) and (2) for the étale neighbourhoods of a geometric point”.

> **Stacks 0CTW, conditions (1) and (2).** Weak association at a chart point does not depend
> on the chart: if the point of one étale scheme chart of `x̄` is weakly associated to the
> restriction of `F` there, so is the point of any other.

```lean
theorem isWeaklyAssociatedPoint_restrictToChart_of_restrictToChart
    {xbar : GeometricPoint B S hS X.1} (V V' : SmallEtaleNeighborhood xbar)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (h : Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
      (chartPoint B S hS X.1 V)) :
    Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V'.chart)
      (chartPoint B S hS X.1 V')
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_exists_restrictToChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTFAE.lean#L522). The attribute's comment: “conditions (1) and (2) as the weak association of Stacks 0CTX”.

> **Stacks 0CTW, conditions (1) and (2) in the form of Stacks 0CTX.** A point of `X` is weakly
> associated to a quasi-coherent `F` exactly when, at some geometric point above it, the
> corresponding point of some étale scheme chart is weakly associated to the restriction of `F`
> there.

```lean
theorem isWeaklyAssociatedPoint_iff_exists_restrictToChart
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X F x ↔
      ∃ (xbar : GeometricPoint B S hS X.1), xbar.LiesOver x ∧
        ∃ V : SmallEtaleNeighborhood xbar,
          Stacks.Divisors.IsWeaklyAssociatedPoint (restrictToChart B S hS X.2 F V.chart)
            (chartPoint B S hS X.1 V)
```

## Tag 0CTX, a definition

[Tag 0CTX](https://stacks.math.columbia.edu/tag/0CTX) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_iff_moduleStalkLarge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedChart.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedChart.lean#L129). The attribute's comment: “weak association on the stalk at the point of the small étale site”.

> **Stacks 0CTX**, weak association read before the extension of scalars: a point of an
> algebraic space is weakly associated to an `𝒪_X`-module exactly when, at some geometric point
> above it, the maximal ideal of the stalk of the structure sheaf at the corresponding point of
> the small étale site is weakly associated to the stalk of the module there.

```lean
theorem isWeaklyAssociatedPoint_iff_moduleStalkLarge (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS) (F : Modules.{u, m} B S hS X.1 X.2)
    (x : points B S hS X.1) :
    IsWeaklyAssociatedPoint B S hS X F x ↔
      ∃ xbar : GeometricPoint B S hS X.1, xbar.LiesOver x ∧
        letI : IsLocalRing (etaleLocalRing B S hS X.1 xbar) :=
          isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
        letI : IsLocalRing
            (((etaleSitePoint B S hS X.1 xbar X.2).presheafFiber (A := CommRingCat.{u})).obj
              (smallEtaleRingedTopos B S hS X).O.obj) :=
          (pointStalkRingEquiv B S hS X xbar).symm.isLocalRing
        IsWeaklyAssociatedPrime
          (((etaleSitePoint B S hS X.1 xbar X.2).presheafFiber (A := CommRingCat.{u})).obj
            (smallEtaleRingedTopos B S hS X).O.obj)
          (Stacks.moduleStalkLarge (etaleSitePoint B S hS X.1 xbar X.2)
            (smallEtaleRingedTopos B S hS X).O F)
          (IsLocalRing.maximalIdeal _)
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_forall_exists_pow_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedMinimalSupport.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedMinimalSupport.lean#L217). The attribute's comment: “weak association from a stalk element killed by powers of the non-units”.

> **Stacks 0CTX**, the algebraic criterion for weak association. A point of an algebraic space
> is weakly associated to an `𝒪_X`-module as soon as, at some geometric point above it, the
> geometric stalk has a nonzero element some power of each non-unit of the étale local ring
> annihilates: the annihilator of that element lies in the maximal ideal because the ring is local,
> and a prime below the maximal ideal containing the annihilator then contains every non-unit.

```lean
theorem isWeaklyAssociatedPoint_of_forall_exists_pow_smul_eq_zero
    (F : Modules.{u, m} B S hS X.1 X.2) (x : points B S hS X.1)
    (xbar : GeometricPoint B S hS X.1) (hxbar : xbar.LiesOver x)
    (t : geometricModuleStalk B S hS X xbar F) (ht : t ≠ 0)
    (hpow : ∀ a : etaleLocalRing B S hS X.1 xbar, ¬ IsUnit a → ∃ n : ℕ, a ^ n • t = 0) :
    IsWeaklyAssociatedPoint B S hS X F x
```

**`AlgebraicGeometry.Space.IsWeaklyAssociatedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean#L73). The attribute's comment: “weakly associated point”.

> **Stacks 0CTX, part (1).** A point `x` of an algebraic space `X` is *weakly associated* to
> an `𝒪_X`-module `F` when, at some geometric point above `x`, the maximal ideal of the étale
> local ring is a weakly associated prime of the geometric stalk of `F`, that is, when it is
> minimal among the primes containing the annihilator of some element of that stalk.

```lean
noncomputable def IsWeaklyAssociatedPoint (F : Modules.{u, m} B S hS X.1 X.2)
    (x : points B S hS X.1) : Prop
```

**`AlgebraicGeometry.Space.weaklyAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean#L86). The attribute's comment: “set of weakly associated points”.

> **Stacks 0CTX, part (2).** The set `WeakAss(F)` of points of an algebraic space weakly
> associated to an `𝒪_X`-module `F`.

```lean
noncomputable abbrev weaklyAssociatedPoints (F : Modules.{u, m} B S hS X.1 X.2) :
    Set (points B S hS X.1)
```

**`AlgebraicGeometry.Space.weaklyAssociatedPointsOfSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPoints.lean#L101). The attribute's comment: “weakly associated points of the space”.

> **Stacks 0CTX, part (3).** The weakly associated points `WeakAss(X)` of an algebraic space
> `X` are the weakly associated points of its structure sheaf.

```lean
noncomputable abbrev weaklyAssociatedPointsOfSpace : Set (points B S hS X.1)
```

## Tag 0CTY, a lemma

[Tag 0CTY](https://stacks.math.columbia.edu/tag/0CTY) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_subset_supportOfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedSupport.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedSupport.lean#L153).

> **Stacks 0CTY.** The weakly associated points of an `𝒪_X`-module on an algebraic space lie
> in the support of its underlying abelian sheaf.

```lean
theorem weaklyAssociatedPoints_subset_supportOfSheaf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : AlgebraicSpaces B S hS) (F : Modules.{u, m} B S hS X.1 X.2) :
    weaklyAssociatedPoints B S hS X F ⊆
      supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)
```

## Tag 0CTZ, a lemma

[Tag 0CTZ](https://stacks.math.columbia.edu/tag/0CTZ) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_subset_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExact.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExact.lean#L313). The attribute's comment: “subsheaf”.

> **Stacks 0CTZ, first inclusion.** In a short exact sequence of `𝒪_X`-modules on an
> algebraic space, every weakly associated point of the first module is weakly associated to the
> middle module.

```lean
theorem weaklyAssociatedPoints_subset_of_shortExact
    (σ : ShortComplex (Modules.{u, m} B S hS X.1 X.2)) (hσ : σ.ShortExact) :
    weaklyAssociatedPoints B S hS X σ.X₁ ⊆ weaklyAssociatedPoints B S hS X σ.X₂
```

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_subset_union_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExact.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExact.lean#L328). The attribute's comment: “middle_term”.

> **Stacks 0CTZ, second inclusion.** In a short exact sequence of `𝒪_X`-modules on an
> algebraic space, every weakly associated point of the middle module is weakly associated to one
> of the outer modules.

```lean
theorem weaklyAssociatedPoints_subset_union_of_shortExact
    [Balanced (Modules.{u, m} B S hS X.1 X.2)]
    (σ : ShortComplex (Modules.{u, m} B S hS X.1 X.2)) (hσ : σ.ShortExact) :
    weaklyAssociatedPoints B S hS X σ.X₂ ⊆
      weaklyAssociatedPoints B S hS X σ.X₁ ∪ weaklyAssociatedPoints B S hS X σ.X₃
```

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_subset_union_of_shortExact_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExactBalanced.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedShortExactBalanced.lean#L48). The attribute's comment: “middle_term, for sections in any universe containing the universe of the schemes and with no assumed inputs: the balancedness of the category of modules that the general form takes as an instance hypothesis is discharged here”.

> **Stacks 0CTZ, second inclusion.** In a short exact sequence of `𝒪_X`-modules on an
> algebraic space, every weakly associated point of the middle module is weakly associated to one
> of the outer modules.
>
> This is `AlgebraicGeometry.Space.weaklyAssociatedPoints_subset_union_of_shortExact` with its
> balancedness instance supplied by `AlgebraicGeometry.Space.balanced_modules_max`: the `𝒪_X`-modules
> with sections in a universe containing the universe of the schemes are abelian, the small étale
> site being essentially small there, and an abelian category is balanced.

```lean
theorem weaklyAssociatedPoints_subset_union_of_shortExact_unconditional
    (σ : ShortComplex (Modules.{u, max u m} B S hS X.1 X.2)) (hσ : σ.ShortExact) :
    weaklyAssociatedPoints B S hS X σ.X₂ ⊆
      weaklyAssociatedPoints B S hS X σ.X₁ ∪ weaklyAssociatedPoints B S hS X σ.X₃
```

## Tag 0CU0, a lemma

[Tag 0CU0](https://stacks.math.columbia.edu/tag/0CU0) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_eq_empty_of_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedVanishing.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedVanishing.lean#L74). The attribute's comment: “a zero module has no weakly associated points”.

> **Stacks 0CU0**, the direction that a vanishing module has no weakly associated points: a
> zero `𝒪_X`-module on an algebraic space has empty set of weakly associated points.

```lean
theorem weaklyAssociatedPoints_eq_empty_of_isZero
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : AlgebraicSpaces B S hS) (F : Modules.{u, m} B S hS X.1 X.2) (hF : IsZero F) :
    weaklyAssociatedPoints B S hS X F = ∅
```

**`AlgebraicGeometry.Space.isZero_iff_weaklyAssociatedPoints_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedVanishingQuasicoherent.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedVanishingQuasicoherent.lean#L100).

> **Stacks 0CU0.** A quasi-coherent `𝒪_X`-module on an algebraic space is zero if and only if
> it has no weakly associated point.

```lean
theorem isZero_iff_weaklyAssociatedPoints_eq_empty (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] : IsZero F ↔ weaklyAssociatedPoints B S hS X F = ∅
```

## Tag 0CUL, a lemma

[Tag 0CUL](https://stacks.math.columbia.edu/tag/0CUL) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_mem_supportOfSheaf_of_localRingDimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedCodimensionZero.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedCodimensionZero.lean#L90). The attribute's comment: “the first assertion, that a codimension-zero point of the support is weakly associated, stated for every module in place of a quasi-coherent one”.

> **Stacks 0CUL, the first assertion.** A point of an algebraic space which lies in the
> support of an `𝒪_X`-module and has codimension zero, in the sense that the local ring of the
> space there has Krull dimension zero, is weakly associated to that module.

```lean
theorem isWeaklyAssociatedPoint_of_mem_supportOfSheaf_of_localRingDimension_eq_zero
    (F : Modules.{u, m} B S hS X.1 X.2) (x : points B S hS X.1)
    (hsupp : x ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F))
    (codim : localRingDimension B S hS x = 0) :
    IsWeaklyAssociatedPoint B S hS X F x
```

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_localRingDimension_schemeTheoreticSupport_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedCodimensionZero.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedCodimensionZero.lean#L152). The attribute's comment: “the second assertion, for a codimension-zero point of the scheme theoretic support of a quasi-coherent module of finite type”.

> **Stacks 0CUL, the second assertion.** Let `F` be a quasi-coherent `𝒪_X`-module of finite
> type with scheme theoretic support `Z`. A point of `Z` of codimension zero in `Z`, in the sense
> that the local ring of `Z` there has Krull dimension zero, has an image in `X` weakly associated
> to `F`.
>
> The scheme theoretic support is a closed subspace and `F` is the direct image of a
> quasi-coherent module `G` on it, by Stacks 07U0; the direct image of Stacks 03LU along the
> closed immersion is the direct image along base change of étale charts. The image of the point
> lies in the support of `F`, which is the set of points of `Z`, so the stalk of `G` at a
> geometric point above it is nonzero, and the first assertion's argument applies on `Z`.

```lean
theorem isWeaklyAssociatedPoint_of_localRingDimension_schemeTheoreticSupport_eq_zero
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteTypeOnSite F]
    (x : points B S hS (schemeTheoreticSupport B S hS X F).toFunctor)
    (codim : localRingDimension B S hS x = 0) :
    IsWeaklyAssociatedPoint B S hS X F
      (pointsMap B S hS (schemeTheoreticSupport B S hS X F).toFunctor
        (schemeTheoreticSupport B S hS X F).ι x)
```

## Tag 0CUM, a lemma

[Tag 0CUM](https://stacks.math.columbia.edu/tag/0CUM) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_of_mem_supportOfSheaf_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedMinimalSupportDecent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedMinimalSupportDecent.lean#L206). The attribute's comment: “with decency read as condition (α) of Stacks 03JX, which is all Stacks 03K5 needs, and with no assumed inputs”.

> **Stacks 0CUM.** Let `X` be an algebraic space over `S` all of whose chart fibres are
> finite — in particular a decent one — and let `F` be a quasi-coherent `𝒪_X`-module. A point of
> `|X|` which lies in the support of `F` and is not a specialization of another point of that
> support is weakly associated to `F`.

```lean
theorem isWeaklyAssociatedPoint_of_mem_supportOfSheaf_of_specializes
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hdecent : HasFiniteChartFibersAtEveryPoint B S hS X.1)
    (x : points B S hS X.1)
    (hx : x ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F))
    (hmin : ∀ y, y ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) →
      y ⤳ x → y = x) :
    IsWeaklyAssociatedPoint B S hS X F x
```

## Tag 0CUN, a lemma

[Tag 0CUN](https://stacks.math.columbia.edu/tag/0CUN) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_inter_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedFinite.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedFinite.lean#L92).

> **Stacks 0CUN.** Let `X` be a locally Noetherian algebraic space over a scheme `S` and let
> `F` be a coherent `𝒪_X`-module.  Then the weakly associated points of `F` — the associated
> points, in the terminology of the source — meet every quasi-compact open subset of `|X|` in a
> finite set.

```lean
theorem weaklyAssociatedPoints_inter_finite
    (hX : HasEtaleLocalProperty B S hS X.1 (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (F : Modules.{u, u} B S hS X.1 X.2) [hF : IsCoherent B S hS X.1 X.2 F]
    (W : Set (points B S hS X.1)) (_hWopen : IsOpen W) (hWcompact : IsCompact W) :
    (weaklyAssociatedPoints B S hS X F ∩ W).Finite
```

## Tag 0CUP, a lemma

[Tag 0CUP](https://stacks.math.columbia.edu/tag/0CUP) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_sections_eval_of_weaklyAssociatedPoints_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedSectionsInjective.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedSectionsInjective.lean#L106).

> **Stacks Project, Tag 0CUP.** Let `F` be a quasi-coherent `𝒪_X`-module on an algebraic space
> `X` and let `U` be an étale chart of `X` such that every weakly associated point of `F` lies in
> the image of `|U| → |X|`.  Then the restriction `Γ(X, F) → Γ(U, F)` of global sections to the
> chart is injective.

```lean
theorem injective_sections_eval_of_weaklyAssociatedPoints_subset
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (U : SmallEtale B S hS X.1)
    (weakAss_subset :
      weaklyAssociatedPoints B S hS X F ⊆ Set.range (chartSchemeToPoints B S hS X.1 U)) :
    Function.Injective fun s : F.sections => s.eval (op U)
```

## Tag 0CUQ, a lemma

[Tag 0CUQ](https://stacks.math.columbia.edu/tag/0CUQ) in the Stacks Project.

**`AlgebraicGeometry.Space.not_isWeaklyAssociatedPoint_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePushforwardWeaklyAssociatedRange.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePushforwardWeaklyAssociatedRange.lean#L53).

> **Stacks 0CUQ.** Let `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces over `S`,
> let `F` be a quasi-coherent `𝒪_X`-module and let `y` be a point of `Y` outside the image of
> `|f|`. Then `y` is not weakly associated to `f_*F`.
>
> This is
> `AlgebraicGeometry.Space.not_isWeaklyAssociatedPoint_modulePushforward_of_notMem_range` with its
> Stacks 0CU2 hypothesis discharged by
> `AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_subset_image_of_isAffineHom`.
> Quasi-separatedness of `f`, which the source assumes, is not needed; see the implementation notes
> of `StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPushforward.lean`.

```lean
theorem not_isWeaklyAssociatedPoint_modulePushforward
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (y : points B S hS Y.1) (hy : y ∉ Set.range (pointsMap B S hS X.1 f.hom)) :
    ¬ IsWeaklyAssociatedPoint B S hS Y ((modulePushforward B S hS f).obj F) y
```

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_modulePushforward_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePushforwardWeaklyAssociatedRange.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpacePushforwardWeaklyAssociatedRange.lean#L70). The attribute's comment: “as an inclusion of sets of points”.

> **Stacks 0CUQ, as an inclusion of sets of points.** Let `f : X ⟶ Y` be a quasi-compact
> morphism of algebraic spaces over `S` and let `F` be a quasi-coherent `𝒪_X`-module. Then every
> weakly associated point of `f_*F` lies in the image of `|f|`.
>
> This is the pointwise statement
> `AlgebraicGeometry.Space.not_isWeaklyAssociatedPoint_modulePushforward` contraposed.

```lean
theorem weaklyAssociatedPoints_modulePushforward_subset_range
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    weaklyAssociatedPoints B S hS Y ((modulePushforward B S hS f).obj F) ⊆
      Set.range (pointsMap B S hS X.1 f.hom)
```

**`AlgebraicGeometry.Space.not_isWeaklyAssociatedPoint_modulePushforward_of_notMem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPushforward.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedPushforward.lean#L390). The attribute's comment: “granting Stacks 0CU2”.

> **Stacks 0CUQ**, granting Stacks 0CU2.
>
> Let `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces over `S`, let `F` be a
> quasi-coherent `𝒪_X`-module and let `y` be a point of `Y` outside the image of `|f|`. Then `y`
> is not weakly associated to `f_*F`.
>
> The hypothesis `h0CU2` is Stacks 0CU2, the inclusion `WeakAss(g_*H) ⊆ |g|(WeakAss(H))` for an
> affine morphism `g`; it is the one step of the source's argument that this development does not
> have. Quasi-separatedness of `f`, which the source assumes, is not needed: it enters the source
> only through Stacks 03M9, and the argument below does not use quasi-coherence of the direct
> image, so Stacks 03M9 is not needed either.

```lean
theorem not_isWeaklyAssociatedPoint_modulePushforward_of_notMem_range
    (h0CU2 : AffinePushforwardWeaklyAssociatedImage B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (y : points B S hS Y.1) (hy : y ∉ Set.range (pointsMap B S hS X.1 f.hom)) :
    ¬ IsWeaklyAssociatedPoint B S hS Y ((modulePushforward B S hS f).obj F) y
```

## Tag 0CUR, a lemma

[Tag 0CUR](https://stacks.math.columbia.edu/tag/0CUR) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_of_stalk_injective_or_notMem_weaklyAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedInjective.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedInjective.lean#L250).

> **Stacks Project, Tag 0CUR**.
>
> Let `φ : F ⟶ G` be a map of quasi-coherent `𝒪_X`-modules on an algebraic space `X` such that
> every point `x` of `X` satisfies at least one of: the induced map `F_x̄ → G_x̄` is injective for
> a geometric point `x̄` above `x`, or `x` is not a weakly associated point of `F`.  Then `φ` is
> injective.
>
> The proof follows the source: `Ker(φ)` is quasi-coherent by the kernel clause of Stacks 03M1(3),
> `WeakAss(Ker(φ)) = ∅`, and `Ker(φ)` vanishes by Stacks 0CU0.

```lean
theorem mono_of_stalk_injective_or_notMem_weaklyAssociatedPoints
    (F G : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite] (φ : F ⟶ G)
    (hφ : ∀ y : points B S hS X.1,
      (∃ ybar : GeometricPoint B S hS X.1, ybar.LiesOver y ∧
          Function.Injective (geometricModuleStalkMap B S hS X ybar φ)) ∨
        y ∉ weaklyAssociatedPoints B S hS X F) :
    Mono φ
```

## Tag 0EN1, a lemma

[Tag 0EN1](https://stacks.math.columbia.edu/tag/0EN1) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPointsOfSpace_eq_setOf_localRingDimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedReduced.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedReduced.lean#L198).

> **Stacks 0EN1.** The weakly associated points of a reduced algebraic space are exactly its
> points of codimension zero, that is the points whose local ring has Krull dimension zero.

```lean
theorem weaklyAssociatedPointsOfSpace_eq_setOf_localRingDimension_eq_zero
    (hred : HasEtaleLocalProperty B S hS X.1 (fun Y : Scheme.{u} => IsReduced Y)) :
    weaklyAssociatedPointsOfSpace B S hS X =
      {x : points B S hS X.1 | localRingDimension B S hS x = 0}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.2, Tag 0CTV](https://stacks.math.columbia.edu/tag/0CTV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
