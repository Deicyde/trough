---
declaration: section
origin: cited
lean: AlgebraicGeometry.selfIntersectionNumber_pos_and_invertibleCurveDegree_pos_of_isAmple, AlgebraicGeometry.curveDegree_dualizingSheafOverField_eq_neg_two_mul_and_chowDegree, AlgebraicGeometry.curveDegree, AlgebraicGeometry.curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental, AlgebraicGeometry.eulerCharacteristic_eq_chowDegree_firstChernCapOnCycles_add, AlgebraicGeometry.eq_invertibleCurveDegree_of_isSelfIntersectionNumber, AlgebraicGeometry.isSelfIntersectionNumber_one_iff_of_topologicalKrullDim_eq_one, AlgebraicGeometry.eulerCharacteristic_unit_eq_neg_eulerCharacteristic_dualizingSheafOverField
statement: formalized
proof: formalized
---

# 53.5 Riemann-Roch

Section 53.5 of the Stacks Project, [Tag 0B5B](https://stacks.math.columbia.edu/tag/0B5B). 8 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B5B, the section

[Tag 0B5B](https://stacks.math.columbia.edu/tag/0B5B) in the Stacks Project.

**`AlgebraicGeometry.selfIntersectionNumber_pos_and_invertibleCurveDegree_pos_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannRochSection.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannRochSection.lean#L122). The attribute's comment: “the section's positivity claim: if L is ample then the integer (L . X) = deg(L) is positive. Stated for dim X = 1: under the section's standing dim X <= 1 the claim fails at dimension zero (X = Spec k, L = O\_X ample, deg(O\_X) = chi(O\_X) - chi(O\_X) = 0 = (O\_X . X)), and dim X = 1 is the dimension at which the section's name deg\_L(X) = (L . X) (Tag 0BEW) applies”.

> **"If `𝓛` is ample, then this integer is positive"** (Section [Stacks, Tag 0B5B]): on a
> proper scheme `X` of dimension one over a field `k`, an ample invertible `𝒪_X`-module `𝓛` has
> positive numerical intersection number `(𝓛 · X)` ([Stacks, Tag 0BEP], at the closed subscheme
> `X ⊆ X`) and positive degree `deg(𝓛)` ([Stacks, Tag 0AYR]).
>
> The section states this under its standing hypothesis `dim X ≤ 1`; at dimension zero it is false
> (`X = Spec k`, `𝓛 = 𝒪_X`, where both integers are `0`), so the hypothesis here is `dim X = 1`,
> the dimension at which the section's name `deg_𝓛(X) = (𝓛 · X)` for this integer
> ([Stacks, Tag 0BEW]) applies. See the module documentation.

```lean
theorem selfIntersectionNumber_pos_and_invertibleCurveDegree_pos_of_isAmple
    (hdim : topologicalKrullDim X = 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) :
    0 < selfIntersectionNumber k f (𝟙 X) 1 hdim.le L ∧
      0 < invertibleCurveDegree k f hdim.le L
```

**`AlgebraicGeometry.curveDegree_dualizingSheafOverField_eq_neg_two_mul_and_chowDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannRochSection.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannRochSection.lean#L155). The attribute's comment: “the section's Riemann-Roch claim: in the case that omega\_X is invertible, -1/2 c\_1(omega\_X) cap [X]\_1 is a zero cycle (with half-integer coefficients) whose degree is chi(X, O\_X), together with deg(omega\_X) = -2 chi(X, O\_X); obtained, as the section says, from Tag 0BS5 (at omega^bullet = omega[1], Tag 0BS3), whose hypotheses X Cohen-Macaulay and equidimensional of dimension 1 it keeps. omega\_X invertible is the instance that the module of Tag 0BS2 is finite locally free of rank 1. The section's gloss 'omega\_X invertible, i.e., X Gorenstein' is clause (1) of Tag 0BS6”.

> **The Riemann--Roch claim of Section [Stacks, Tag 0B5B]**: let `X` be a proper scheme over a
> field `k`, Cohen--Macaulay and equidimensional of dimension one, and let
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` be the module of [Stacks, Tag 0BS2]. If `ω_X` is invertible, then
>
> * `deg(ω_X) = -2 χ(X, 𝒪_X)`, with `deg` the degree of [Stacks, Tag 0AYR], and
> * the zero cycle `-½ c₁(ω_X) ∩ [X]_1` has degree `χ(X, 𝒪_X)`.
>
> This is what the section obtains from Lemma [Stacks, Tag 0BS5] "in the case that `ω_X` is
> invertible". The proof is the section's: `χ(X, 𝒪_X) = -χ(X, ω_X)` by [Stacks, Tag 0BS5] at
> `ω_X^• = ω_X[1]` ([Stacks, Tag 0BS3]), then [Stacks, Tag 0BRX] and [Stacks, Tag 0BRY]. Nothing
> beyond the stated hypotheses is used; in particular not `H⁰(X, 𝒪_X) = k`. See the module
> documentation.

```lean
theorem curveDegree_dualizingSheafOverField_eq_neg_two_mul_and_chowDegree
    (hcm : IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (Stacks.Duality.dualizingSheafOverField f) 1] :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : (Stacks.Ample.unitModule X).IsCoherent :=
      Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent X
    curveDegree k f hdim.le (Stacks.Duality.dualizingSheafOverField f) 1 =
        -2 * eulerCharacteristic k f (Stacks.Ample.unitModule X) ∧
      (-(1 / 2 : ℚ)) *
          (chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) f
            (IsLocalRing.closedPoint k)
            (chowGroupCast (fieldChowSituation k) f (show (1 : ℤ) - 1 = 0 by simp)
              (GenuineChern.firstChernCapOnCycles (fieldChowSituation k) f
                (Stacks.Duality.dualizingSheafOverField f) 1 1
                (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f (𝟙 X) 1))) : ℚ) =
        (eulerCharacteristic k f (Stacks.Ample.unitModule X) : ℚ)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.curveDegree`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean#L34) (StacksFrontier): “equation (0BRX): deg(E) = χ(X, E) - rank(E) χ(X, O\_X)”.
- [`AlgebraicGeometry.curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochGenuine.lean#L305), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean#L37) (StacksFrontier): “equation (0BRY): deg(E) = deg(c\_1(E) ∩ [X]\_1)”.
- [`AlgebraicGeometry.eulerCharacteristic_eq_chowDegree_firstChernCapOnCycles_add`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochChern.lean#L57), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean#L40) (StacksFrontier): “equation (0BRZ): the first version of Riemann-Roch”.
- [`AlgebraicGeometry.eq_invertibleCurveDegree_of_isSelfIntersectionNumber`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean#L169), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean#L43) (StacksFrontier): “equation (0BS0): (L · X) = deg(L)”.
- [`AlgebraicGeometry.isSelfIntersectionNumber_one_iff_of_topologicalKrullDim_eq_one`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean#L217), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochSection.lean#L46) (StacksFrontier): “equation (0BS1): deg\_L(X) = (L · X)”.

## Tag 0BRX, an equation

[Tag 0BRX](https://stacks.math.columbia.edu/tag/0BRX) in the Stacks Project.

**`AlgebraicGeometry.curveDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Degree.lean#L82). The attribute's comment: “the degree formula”.

> The degree of a finite locally free sheaf of constant rank on a proper scheme of
> dimension at most one over a field.

```lean
public noncomputable def curveDegree (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (_hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (rank : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E rank] : ℤ
```

## Tag 0BRY, an equation

[Tag 0BRY](https://stacks.math.columbia.edu/tag/0BRY) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochGenuine.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochGenuine.lean#L305).

> **Equation [Stacks, Tag 0BRY]**, in the orientation of the source:
> `deg(ℰ) = deg(c₁(ℰ) ∩ [X]_1)` for `ℰ` finite locally free of constant rank on a proper scheme of
> dimension at most one over a field, with `c₁(ℰ) ∩ -` the operation of Stacks 02U5 at the Chern
> classes of Stacks 02U0 and `deg` the degree of Stacks 0AZ1.
>
> Two conventions are fixed here. In rank zero Stacks 02U5 defines no `c₁`; the total Chern class
> of a module of rank zero is `1`, so `c₁ = 0`, and `GenuineChern.firstChernCapOnCycles` is zero
> there by definition. The operation of Stacks 02U5 extends `[W] ↦ i_*(c₁(i^*ℰ) ∩ [W])` over
> cycles through representatives of the classes of Stacks 02U0 (`GenuineChern.chowRep`); the choice
> does not matter here, since `[X]_1` is a finite sum of fundamental cycles of one-dimensional
> components and on each the class is the one of Stacks 02U0
> (`GenuineChern.chernCapOnCycles_integral_cycle`).

```lean
theorem curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] :
    curveDegree k p hdim E r =
      chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) p
        (IsLocalRing.closedPoint k)
        (chowGroupCast (fieldChowSituation k) p (show (1 : ℤ) - 1 = 0 by simp)
          (GenuineChern.firstChernCapOnCycles (fieldChowSituation k) p E r 1
            (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p (𝟙 X) 1)))
```

## Tag 0BRZ, an equation

[Tag 0BRZ](https://stacks.math.columbia.edu/tag/0BRZ) in the Stacks Project.

**`AlgebraicGeometry.eulerCharacteristic_eq_chowDegree_firstChernCapOnCycles_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochChern.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochChern.lean#L57). References: SGA 6 XIII (4.6), “more general”.

> **Riemann-Roch**: on a proper scheme `X` of dimension at most one over a field `k`, a finite
> locally free `𝒪_X`-module `ℰ` of constant rank `r` satisfies
>
> `χ(X, ℰ) = deg(c₁(ℰ) ∩ [X]_1) + rank(ℰ) · χ(X, 𝒪_X)`.
>
> Here `c₁(ℰ) ∩ -` is intersection with the first Chern class of [Stacks, Tag 02U5],
> `Stacks.Chow.GenuineChern.firstChernCapOnCycles`: on an integral closed subscheme `i : W ⟶ X` it is
> `i_*(c₁(i^*ℰ) ∩ [W])` with the class of [Stacks, Tag 02U0] read off the projective space bundle
> formula, extended coefficientwise; in rank zero it is zero. It is applied to the fundamental
> one-cycle `[X]_1` ([Stacks, Tag 02QU]), and `deg` is the degree of zero cycles of
> [Stacks, Tag 0AZ1]. `X` is not assumed integral, reduced, or of dimension exactly one, and every
> rank is covered, rank zero included. The Euler characteristics ([Stacks, Tag 0BEJ]) are taken at
> the coherence of `ℰ` and of `𝒪_X` that properness over `k` provides.

```lean
theorem eulerCharacteristic_eq_chowDegree_firstChernCapOnCycles_add
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] :
    letI :=
      Stacks.AlgebraicGeometry.CurveEulerBridge.isCoherent_of_isFiniteLocallyFreeOfRank k p E r
    letI := Stacks.AlgebraicGeometry.CurveEulerBridge.isCoherent_unit k p
    eulerCharacteristic k p E =
      chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) p
          (IsLocalRing.closedPoint k)
          (chowGroupCast (fieldChowSituation k) p (show (1 : ℤ) - 1 = 0 by simp)
            (GenuineChern.firstChernCapOnCycles (fieldChowSituation k) p E r 1
              (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p (𝟙 X) 1))) +
        (r : ℤ) * eulerCharacteristic k p (SheafOfModules.unit X.ringCatSheaf)
```

## Tag 0BS0, an equation

[Tag 0BS0](https://stacks.math.columbia.edu/tag/0BS0) in the Stacks Project.

**`AlgebraicGeometry.eq_invertibleCurveDegree_of_isSelfIntersectionNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean#L169). The attribute's comment: “the numerical intersection number is the degree”.

> **[Stacks, Tag 0BS1] and [Stacks, Tag 0BS0]**: on a proper scheme of dimension at most one
> over a field, the numerical intersection number of an invertible module with the whole space is
> the degree of that module,
>
> `(𝓛 · X) = deg(𝓛)`.
>
> The polynomial of [Stacks, Tag 0BEM] has total degree at most one, so it is determined by its
> values at `0` and `1`, where the twists of `𝒪_X` are `𝒪_X` and `𝓛`; its linear coefficient is
> therefore `χ(X, 𝓛) - χ(X, 𝒪_X)`, which is the degree of [Stacks, Tag 0AYR].

```lean
theorem eq_invertibleCurveDegree_of_isSelfIntersectionNumber
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] {c : ℚ}
    (hc : IsSelfIntersectionNumber k f 1 L c) :
    c = (invertibleCurveDegree k f hdim L : ℚ)
```

## Tag 0BS1, an equation

[Tag 0BS1](https://stacks.math.columbia.edu/tag/0BS1) in the Stacks Project.

**`AlgebraicGeometry.eq_invertibleCurveDegree_of_isSelfIntersectionNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean#L169). The attribute's comment: “the intersection number and the degree”.

> **[Stacks, Tag 0BS1] and [Stacks, Tag 0BS0]**: on a proper scheme of dimension at most one
> over a field, the numerical intersection number of an invertible module with the whole space is
> the degree of that module,
>
> `(𝓛 · X) = deg(𝓛)`.
>
> The polynomial of [Stacks, Tag 0BEM] has total degree at most one, so it is determined by its
> values at `0` and `1`, where the twists of `𝒪_X` are `𝒪_X` and `𝓛`; its linear coefficient is
> therefore `χ(X, 𝓛) - χ(X, 𝒪_X)`, which is the degree of [Stacks, Tag 0AYR].

```lean
theorem eq_invertibleCurveDegree_of_isSelfIntersectionNumber
    (hdim : topologicalKrullDim X ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] {c : ℚ}
    (hc : IsSelfIntersectionNumber k f 1 L c) :
    c = (invertibleCurveDegree k f hdim L : ℚ)
```

**`AlgebraicGeometry.isSelfIntersectionNumber_one_iff_of_topologicalKrullDim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CurveIntersectionNumber/Basic.lean#L217). The attribute's comment: “the degree of X with respect to an invertible module”.

> **The number of factors that [Stacks, Tag 0BEW] prescribes on a scheme of dimension one is
> one.** This is the left equality `deg_𝓛(X) = (𝓛 · X)` of [Stacks, Tag 0BS1]: the degree of `X`
> with respect to `𝓛` is the self-intersection number with `dim X` factors.
>
> Ampleness of `𝓛`, which [Stacks, Tag 0BEW] assumes, is not needed: it makes the notation
> `deg_𝓛(X)` defined and the integer positive, the latter being [Stacks, Tag 0B5X].

```lean
theorem isSelfIntersectionNumber_one_iff_of_topologicalKrullDim_eq_one
    (hdim : topologicalKrullDim X = 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] (c : ℚ) :
    IsSelfIntersectionNumber k f ((topologicalKrullDim X).unbotD 0).toNat L c ↔
      IsSelfIntersectionNumber k f 1 L c
```

## Tag 0BS5, a lemma

[Tag 0BS5](https://stacks.math.columbia.edu/tag/0BS5) in the Stacks Project.

**`AlgebraicGeometry.eulerCharacteristic_unit_eq_neg_eulerCharacteristic_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayEulerCharacteristic.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayEulerCharacteristic.lean#L80). The attribute's comment: “second formula, chi(X, O\_X) = - chi(X, omega\_X), for X proper over a field, Cohen-Macaulay and equidimensional of dimension one, omega\_X = H^(-1)(f^x(O\_Spec k)) of Tag 0BS2”.

> **The second formula of [Stacks, Tag 0BS5]: `χ(X, 𝒪_X) = -χ(X, ω_X)`** for a proper scheme
> `X` over a field `k` which is Cohen--Macaulay and equidimensional of dimension one, with
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` the dualizing sheaf of [Stacks, Tag 0BS2].
>
> As in the source, it is the first formula
> `eulerCharacteristic_unit_eq_eulerCharacteristicDerived_dualizingComplexOverField` read through
> `ω_X^• = ω_X[1]` of [Stacks, Tag 0BS3]
> (`Stacks.Duality.dualizingSheafShiftOneIsoOfIsCohenMacaulay`), in the form
> `AlgebraicGeometry.finsum_alternating_finrank_unit_eq_neg_dualizingSheafOverField_of_iso`.

```lean
public theorem eulerCharacteristic_unit_eq_neg_eulerCharacteristic_dualizingSheafOverField
    (hcm : IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : (Stacks.Ample.unitModule X).IsCoherent :=
      Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent X
    letI : (Stacks.Duality.dualizingSheafOverField f).IsCoherent :=
      Stacks.Duality.isCoherent_homology_of_isDualizingComplex
        (Stacks.Duality.isDualizingComplex_dualizingComplexOverField_of_topologicalKrullDim_le_one
          f hdim.le) (-1)
    eulerCharacteristic k f (Stacks.Ample.unitModule X) =
      -eulerCharacteristic k f (Stacks.Duality.dualizingSheafOverField f)
```

**`AlgebraicGeometry.eulerCharacteristic_unit_eq_eulerCharacteristicDerived_dualizingComplexOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexEulerCharacteristic.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexEulerCharacteristic.lean#L323). The attribute's comment: “first formula, chi(X, O\_X) = chi(X, omega^bullet), for X proper of dimension at most one over a field, omega^bullet = f^x(O\_Spec k) of Tag 0BS2, and chi(X, omega^bullet) the alternating sum of the dimensions of its hypercohomology, as the source defines it”.

> **The first formula of [Stacks, Tag 0BS5]: `χ(X, 𝒪_X) = χ(X, ω_X^•)`** for a proper scheme `X`
> of dimension at most one over a field `k`, with `ω_X^• = f^×(𝒪_{Spec k})` the dualizing complex of
> [Stacks, Tag 0BS2] and `χ(X, ω_X^•)` the alternating sum
> `∑_{i ∈ ℤ} (-1)^i dim_k H^i(X, ω_X^•)` that the source defines it to be.
>
> Both sides collapse to `dim_k H⁰(X, 𝒪_X) - dim_k H¹(X, 𝒪_X)`: on the right by the duality
> `dim_k H^i(X, ω_X^•) = dim_k H^{-i}(X, 𝒪_X)`
> (`AlgebraicGeometry.eulerCharacteristicDerived_dualizingComplexOverField_eq_sub`), on the left
> because `X` is at most one-dimensional ([Stacks, Tag 02UZ]).

```lean
public theorem eulerCharacteristic_unit_eq_eulerCharacteristicDerived_dualizingComplexOverField
    (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : (Stacks.Ample.unitModule X).IsCoherent :=
      Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent X
    eulerCharacteristic k f (Stacks.Ample.unitModule X) =
      eulerCharacteristicDerived f (Stacks.Duality.dualizingComplexOverField f).obj
```

## Tag 0BS6, a lemma

[Tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_dualizingSheafOverField_eq_neg_two_mul_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinCurveRiemannRoch.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinCurveRiemannRoch.lean#L85). The attribute's comment: “(2)”.

> **[Stacks, Tag 0BS6], clause (2).** Let `X` be a proper scheme over a field `k` which is
> Gorenstein and equidimensional of dimension one, and `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` the
> dualizing sheaf of [Stacks, Tag 0BS2], which is invertible by clause (1). Then
>
>   `deg(ω_X) = -2 χ(X, 𝒪_X)`,
>
> with `deg` the degree of [Stacks, Tag 0AYR] (`AlgebraicGeometry.curveDegree`, at rank one).
> The proof is the source's: `deg(ω_X) = χ(X, ω_X) - χ(X, 𝒪_X)` and
> `χ(X, 𝒪_X) = -χ(X, ω_X)` by [Stacks, Tag 0BS5].

```lean
public theorem curveDegree_dualizingSheafOverField_eq_neg_two_mul_of_isGorenstein
    (hG : IsGorenstein X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : (Stacks.Ample.unitModule X).IsCoherent :=
      Stacks.AlgebraicGeometry.CoherenceCriteria.structureSheaf_isCoherent X
    letI := (Stacks.Duality.isInvertible_dualizingSheafOverField_of_isGorenstein f hG hequi
      hdim).2
    curveDegree k f hdim.le (Stacks.Duality.dualizingSheafOverField f) 1 =
      -2 * eulerCharacteristic k f (Stacks.Ample.unitModule X)
```

**`AlgebraicGeometry.eulerCharacteristic_eq_and_finrank_cohomology_eq_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinCurveRiemannRoch.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinCurveRiemannRoch.lean#L180). The attribute's comment: “(3)”.

> **[Stacks, Tag 0BS6], clause (3).** Let `X` be a proper scheme over a field `k` which is
> Gorenstein and equidimensional of dimension one, `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` the dualizing
> sheaf of [Stacks, Tag 0BS2] (invertible by clause (1)), and `ℰ` a finite locally free
> `𝒪_X`-module of constant rank `r`. Then
>
>   `χ(X, ℰ) = deg(ℰ) - ½ rank(ℰ) deg(ω_X)`
>
> with `deg` the degree of [Stacks, Tag 0AYR], and
>
>   `dim_k H^i(X, ℰ) = dim_k H^{1-i}(X, ℰ^∨ ⊗_{𝒪_X} ω_X)` for all `i ∈ ℤ`,
>
> with `H^i(X, -)` the hypercohomology of a module placed in degree zero, which is sheaf cohomology
> for `i ≥ 0`.

```lean
public theorem eulerCharacteristic_eq_and_finrank_cohomology_eq_of_isGorenstein
    (hG : IsGorenstein X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) (E : X.Modules) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] :
    letI : E.IsCoherent :=
      Stacks.AlgebraicGeometry.CurveEulerBridge.isCoherent_of_isFiniteLocallyFreeOfRank k f E r
    letI := (Stacks.Duality.isInvertible_dualizingSheafOverField_of_isGorenstein f hG hequi
      hdim).2
    (eulerCharacteristic k f E : ℚ) =
        (curveDegree k f hdim.le E r : ℚ) -
          1 / 2 * (r : ℚ) *
            (curveDegree k f hdim.le (Stacks.Duality.dualizingSheafOverField f) 1 : ℚ) ∧
      ∀ i : ℤ, Module.finrank k (Stacks.Duality.derivedCohomologyOverField f
          ((DerivedCategory.singleFunctor X.Modules 0).obj E) i) =
        Module.finrank k (Stacks.Duality.derivedCohomologyOverField f
          ((DerivedCategory.singleFunctor X.Modules 0).obj
            (dualTensorDualizingSheafOverField f E)) (1 - i))
```

**`Stacks.Duality.isInvertible_dualizingSheafOverField_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinDualizingInvertible.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GorensteinDualizingInvertible.lean#L143). The attribute's comment: “(1)”.

> **The dualizing sheaf of a proper Gorenstein curve is invertible.** Let `X` be a proper scheme
> over a field `k` which is Gorenstein and equidimensional of dimension one, and let
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` be the dualizing sheaf of [Stacks, Tag 0BS2]. Then `ω_X` is an
> invertible `𝒪_X`-module, and it is finite locally free of rank one.

```lean
theorem isInvertible_dualizingSheafOverField_of_isGorenstein
    (hG : AlgebraicGeometry.IsGorenstein X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2
        (dualizingSheafOverField f) ∧
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
        (dualizingSheafOverField f) 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.5, Tag 0B5B](https://stacks.math.columbia.edu/tag/0B5B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
