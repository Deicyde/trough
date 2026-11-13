---
declaration: section
origin: cited
lean: Stacks.nodalModel, Stacks.nodalModelHom, Stacks.smooth_nodalModelHom_zero, Stacks.span_nodalGen_eq_nodalModelOrigin_one, Stacks.span_nodalGen_lt_nodalModelOrigin_of_two_le, Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelHom_zero, Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelHom, Stacks.isRegular_nodalModel_one
statement: formalized
proof: formalized
---

# 55.14 Semistable reduction

Section 55.14 of the Stacks Project, [Tag 0CDB](https://stacks.math.columbia.edu/tag/0CDB). 8 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CDC, an example

[Tag 0CDC](https://stacks.math.columbia.edu/tag/0CDC) in the Stacks Project.

**`Stacks.nodalModel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L106). The attribute's comment: “the scheme X = Spec A of the family A = R[x, y]/(xy - πⁿ)”.

> The standard nodal model `X = Spec R[x, y]/(xy - πⁿ)` of exponent `n`, an affine scheme over
> `S = Spec R`.

```lean
public def nodalModel (R : Type u) [CommRing R] (π : R) (n : ℕ) : Scheme.{u}
```

**`Stacks.nodalModelHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L112). The attribute's comment: “the morphism X ⟶ S = Spec R induced by R → A = R[x, y]/(xy - πⁿ)”.

> The structure morphism `X ⟶ S = Spec R` of the standard nodal model, the morphism of schemes
> induced by the ring map `R → A = R[x, y]/(xy - πⁿ)`.

```lean
public def nodalModelHom (R : Type u) [CommRing R] (π : R) (n : ℕ) :
    nodalModel R π n ⟶ Spec (CommRingCat.of R)
```

**`Stacks.smooth_nodalModelHom_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L121). The attribute's comment: “if n = 0 then X → S is smooth”.

> **The exponent zero model is smooth over the base.** For `n = 0` the defining relation reads
> `xy = 1`, and `X ⟶ S` is smooth; no hypothesis on `R` or `π` is needed.

```lean
public theorem smooth_nodalModelHom_zero (π : R) : Smooth (nodalModelHom R π 0)
```

**`Stacks.span_nodalGen_eq_nodalModelOrigin_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L187). The attribute's comment: “if n = 1 then (x, y) generate the maximal ideal 𝔪 = (π, x, y)”.

> **At exponent one the two coordinates generate the maximal ideal of the origin.** The
> defining relation reads `π = xy`, so the uniformizer already lies in `(x, y)` and
> `𝔪 = (π, x, y) = (x, y)`.

```lean
public theorem span_nodalGen_eq_nodalModelOrigin_one (π : R) :
    Ideal.span {nodalGen R (π ^ 1) 0, nodalGen R (π ^ 1) 1} = nodalModelOrigin R π 1
```

**`Stacks.span_nodalGen_lt_nodalModelOrigin_of_two_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L226). The attribute's comment: “if n > 1 then (x, y) no longer generate the maximal ideal 𝔪 = (π, x, y)”.

> **For exponent at least two the two coordinates no longer generate the maximal ideal of the
> origin.** The ideal `(x, y)` of `R[x, y]/(xy - πⁿ)` is strictly smaller than `𝔪 = (π, x, y)`.

```lean
public theorem span_nodalGen_lt_nodalModelOrigin_of_two_le [IsDomain R] {π : R}
    (hπ : Irreducible π) {n : ℕ} (hn : 2 ≤ n) :
    Ideal.span {nodalGen R (π ^ n) 0, nodalGen R (π ^ n) 1} < nodalModelOrigin R π n
```

**`Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelHom_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L313). The attribute's comment: “the exponent zero member of the family is at-worst-nodal of relative dimension one”.

> **The exponent zero model is at-worst-nodal of relative dimension one over the base.** It is
> smooth of relative dimension one, and a smooth family of curves has empty relative singular
> subscheme.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_nodalModelHom_zero (π : R) :
    IsAtWorstNodalOfRelativeDimensionOne (nodalModelHom R π 0)
```

**`Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L323). The attribute's comment: “for all n the morphism X → S is at-worst-nodal of relative dimension 1”.

> **Every member of the family is at-worst-nodal of relative dimension one over the base.** For
> every exponent `n` the morphism `X = Spec R[x, y]/(xy - πⁿ) ⟶ S = Spec R` is syntomic of relative
> dimension one and its relative singular subscheme, cut out by the two coordinates, is unramified
> over `S`. No hypothesis on `R` or `π` is needed.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_nodalModelHom (π : R) (n : ℕ) :
    IsAtWorstNodalOfRelativeDimensionOne (nodalModelHom R π n)
```

**`Stacks.isRegular_nodalModel_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L336). The attribute's comment: “if n = 1 then X is regular”. References: SGA 7 XVI (1.13), “Case 1, special case”.

> **The exponent one model is regular.** For `π` a uniformizer of a discrete valuation ring the
> scheme `Spec R[x, y]/(xy - π)` is regular.

```lean
public theorem isRegular_nodalModel_one {π : R} (hπ : Irreducible π) :
    IsRegular (nodalModel R π 1)
```

**`Stacks.not_isRegular_nodalModel_of_one_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModel.lean#L343). The attribute's comment: “if n > 1 then X is not regular”.

> **A model of exponent greater than one is not regular.** It is singular at the origin
> `(π, x, y)`, where the two coordinates no longer span the maximal ideal.

```lean
public theorem not_isRegular_nodalModel_of_one_lt {π : R} (hπ : Irreducible π) {n : ℕ}
    (hn : 1 < n) : ¬ IsRegular (nodalModel R π n)
```

**`Stacks.nodalModelBlowup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L157). The attribute's comment: “to ameliorate the situation in case n > 1 we consider the blowup b : X' → X of X in 𝔪: the scheme X'”.

> **The blowup `X'` of the standard nodal model `X = Spec R[x, y]/(xy - πⁿ)` in the ideal
> `𝔪 = (π, x, y)` of its singular point.** It is the `Proj` of the Rees algebra of `𝔪`; that this
> is the blowup of the scheme `X` in the ideal sheaf attached to `𝔪` is
> `Stacks.Blowup.nonempty_over_iso_blowUpToBase`.

```lean
public def nodalModelBlowup (R : Type u) [CommRing R] (π : R) (n : ℕ) : Scheme.{u}
```

**`Stacks.nodalModelBlowupHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L163). The attribute's comment: “to ameliorate the situation in case n > 1 we consider the blowup b : X' → X of X in 𝔪: the morphism b”.

> **The blowup morphism `b : X' ⟶ X` of the standard nodal model in `𝔪 = (π, x, y)`.**

```lean
public def nodalModelBlowupHom (R : Type u) [CommRing R] (π : R) (n : ℕ) :
    nodalModelBlowup R π n ⟶ nodalModel R π n
```

**`Stacks.iSup_opensRange_nodalModelBlowupChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L190). The attribute's comment: “by construction X' is covered by three affine pieces corresponding to the blowup algebras A[𝔪/π], A[𝔪/x] and A[𝔪/y]”.

> **By construction `X'` is covered by three affine pieces, the spectra of the blowup algebras
> `A[𝔪/π]`, `A[𝔪/x]` and `A[𝔪/y]`.**

```lean
public theorem iSup_opensRange_nodalModelBlowupChart (π : R) (n : ℕ) :
    ⨆ i, (nodalModelBlowupChart R π n i).opensRange = ⊤
```

**`Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L390). The attribute's comment: “thus we see that X' → S is at-worst-nodal of relative dimension 1”.

> **`X' ⟶ S` is at-worst-nodal of relative dimension one.** The three charts cover `X'`, an
> open immersion is étale, and over `S` each chart is a standard nodal model: the central one with
> parameter `π^(n-2)`, the two outer ones with parameter `π`.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_nodalModelBlowupToBase
    (hπ : π ≠ 0) (hn : 2 ≤ n) :
    IsAtWorstNodalOfRelativeDimensionOne (nodalModelBlowupToBase R π n)
```

**`Stacks.exists_isOpenImmersion_nodalModel_sub_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L443). The attribute's comment: “X' is regular, except for one point which has an affine open neighbourhood exactly as above but with n replaced by n - 2: that neighbourhood, as the standard nodal model of exponent n - 2 over S”.

> **The one point at which `X'` can fail to be regular has an affine open neighbourhood
> exactly as the original situation, with `n` replaced by `n - 2`.** The central chart `A[𝔪/π]` is
> an affine open of `X'` which, over `S`, is the standard nodal model of exponent `n - 2`; the two
> outer charts are regular by `Stacks.isRegular_spec_nodalXChart` and
> `Stacks.isRegular_spec_nodalYChart`.

```lean
public theorem exists_isOpenImmersion_nodalModel_sub_two (hπ : π ≠ 0) (hn : 2 ≤ n) :
    ∃ j : nodalModel R π (n - 2) ⟶ nodalModelBlowup R π n,
      IsOpenImmersion j ∧ j ≫ nodalModelBlowupToBase R π n = nodalModelHom R π (n - 2) ∧
        Set.range j.base = Set.range (nodalModelBlowupChart R π n 0).base
```

**`Stacks.isRegular_nodalModelBlowup_of_le_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelBlowup.lean#L516). The attribute's comment: “using induction on n: for 2 ≤ n ≤ 3 the sequence of blowing ups in closed points X\_\{⌊n/2⌋} → … → X₁ → X₀ = X is the single blowup b : X' → X, and X\_\{⌊n/2⌋} = X' is regular”.

> **For `2 ≤ n ≤ 3` the single blowup already resolves the singularity: `X'` is regular.** The
> exponent drop `n ↦ n - 2` of the central chart lands on `0` or `1`, where the standard nodal
> model is regular, and the two outer charts are regular for every `n ≥ 2`. Since `⌊n/2⌋ = 1` for
> these `n`, the chain of blowing ups in closed points of [Stacks, Tag 0CDC] is here the single
> blowup `b : X' ⟶ X`, and `X' ⟶ S` is at-worst-nodal of relative dimension one by
> `Stacks.isAtWorstNodalOfRelativeDimensionOne_nodalModelBlowupToBase`.

```lean
public theorem isRegular_nodalModelBlowup_of_le_three {π : R} (hπ : Irreducible π) {n : ℕ}
    (h2 : 2 ≤ n) (h3 : n ≤ 3) : IsRegular (nodalModelBlowup R π n)
```

**`Stacks.exists_pointBlowupChainOfLength_nodalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelResolution.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/StandardNodalModelResolution.lean#L330). The attribute's comment: “using induction on n we conclude that there is a sequence of blowing ups in closed points X\_\{⌊n/2⌋} → … → X₁ → X₀ = X such that X\_\{⌊n/2⌋} → S is at-worst-nodal of relative dimension 1 and X\_\{⌊n/2⌋} is regular”.

> **Stacks Project, Tag 0CDC.** Using induction on `n` there is a sequence of blowups at closed
> points
> ```
> X_{⌊n/2⌋} → … → X₁ → X₀ = X
> ```
> of the standard nodal model `X = Spec R[x, y]/(xy - πⁿ)` over `S = Spec R` such that
> `X_{⌊n/2⌋} → S` is at-worst-nodal of relative dimension one and `X_{⌊n/2⌋}` is regular.

```lean
public theorem exists_pointBlowupChainOfLength_nodalModel {π : R} (hπ : Irreducible π) (n : ℕ) :
    ∃ (Y : Scheme.{u}) (g : Y ⟶ nodalModel R π n),
      PointBlowupChainOfLength (nodalModel R π n) Set.univ (n / 2) Y g ∧
      IsAtWorstNodalOfRelativeDimensionOne (g ≫ nodalModelHom R π n) ∧ IsRegular Y
```

**`Stacks.nodalXChart_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodalChart/Blowup.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NodalChart/Blowup.lean#L386). The attribute's comment: “the algebra A[𝔪/x] has generators x, u = π/x subject to the relation xu - π”.

> **The `x`-chart of the blowup of the standard nodal model.** For `n ≥ 2` the affine blowup
> algebra `A[𝔪/x]` of `A = R[x, y]/(xy - πⁿ)` at `x`, where `𝔪 = (π, x, y)`, is
> `R[x, u]/(xu - π)`, the identification carrying `x` to `x` and `y` to `u·π^(n-1)`.

```lean
public theorem nodalXChart_equiv [IsDomain R] [UniqueFactorizationMonoid R]
    (hπ : π ≠ 0) (hn : 2 ≤ n) :
    ∃ e : ↥(nodalXChart π n S) ≃+* nodalChartRing R π,
      (∀ r : R, e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalXChart π n S)
          (algebraMap R (nodalChartRing R (π ^ n)) r))
        = algebraMap R (nodalChartRing R π) r) ∧
      e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalXChart π n S) (nodalGen R (π ^ n) 0))
        = nodalGen R π 0 ∧
      e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalXChart π n S) (nodalGen R (π ^ n) 1))
        = nodalGen R π 1 * algebraMap R (nodalChartRing R π) (π ^ (n - 1))
```

**`Stacks.nodalCentralChart_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodalChart/Blowup.lean, line 585](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NodalChart/Blowup.lean#L585). The attribute's comment: “the algebra A[𝔪/π] has generators x' = x/π and y' = y/π with x'y' = π^(n-2), so this part of X' is the spectrum of R[x', y']/(x'y' - π^(n-2))”.

> **The central chart of the blowup of the standard nodal model, and the drop `n ↦ n - 2`.**
> For `n ≥ 2` the affine blowup algebra `A[𝔪/π]` of `A = R[x, y]/(xy - πⁿ)` at `π`, where
> `𝔪 = (π, x, y)`, is again a standard nodal model, with the exponent lowered by two:
> `R[x', y']/(x'y' - π^(n-2))`, the identification carrying `x` to `πx'` and `y` to `πy'`.

```lean
public theorem nodalCentralChart_equiv [IsDomain R] [UniqueFactorizationMonoid R]
    (hπ : π ≠ 0) (hn : 2 ≤ n) :
    ∃ e : ↥(nodalCentralChart π n S) ≃+* nodalChartRing R (π ^ (n - 2)),
      (∀ r : R, e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalCentralChart π n S)
          (algebraMap R (nodalChartRing R (π ^ n)) r))
        = algebraMap R (nodalChartRing R (π ^ (n - 2))) r) ∧
      (∀ i : Fin 2,
        e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalCentralChart π n S)
            (nodalGen R (π ^ n) i))
          = algebraMap R (nodalChartRing R (π ^ (n - 2))) π *
              nodalGen R (π ^ (n - 2)) i)
```

**`Stacks.nodalYChart_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodalChart/Blowup.lean, line 771](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NodalChart/Blowup.lean#L771). The attribute's comment: “by symmetry the case of the algebra A[𝔪/y] is the same as the case of A[𝔪/x]”.

> **The `y`-chart of the blowup of the standard nodal model.** For `n ≥ 2` the affine blowup
> algebra `A[𝔪/y]` of `A = R[x, y]/(xy - πⁿ)` at `y`, where `𝔪 = (π, x, y)`, is
> `R[y, v]/(yv - π)`, the identification carrying `y` to `y` and `x` to `v·π^(n-1)`.

```lean
public theorem nodalYChart_equiv [IsDomain R] [UniqueFactorizationMonoid R]
    (hπ : π ≠ 0) (hn : 2 ≤ n) :
    ∃ e : ↥(nodalYChart π n S) ≃+* nodalChartRing R π,
      (∀ r : R, e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalYChart π n S)
          (algebraMap R (nodalChartRing R (π ^ n)) r))
        = algebraMap R (nodalChartRing R π) r) ∧
      e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalYChart π n S) (nodalGen R (π ^ n) 1))
        = nodalGen R π 0 ∧
      e (algebraMap (nodalChartRing R (π ^ n)) ↥(nodalYChart π n S) (nodalGen R (π ^ n) 0))
        = nodalGen R π 1 * algebraMap R (nodalChartRing R π) (π ^ (n - 1))
```

**`Stacks.isRegular_spec_nodalXChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodalChart/Regularity.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NodalChart/Regularity.lean#L555). The attribute's comment: “the x-chart of X' is regular”.

> **The `x`-chart of the blowup of the standard nodal model is regular.** It is the exponent one
> model `R[x, u]/(xu - π)`, by `Stacks.nodalXChart_equiv`.

```lean
public theorem isRegular_spec_nodalXChart {π : R} (hπ : Irreducible π) {n : ℕ} (hn : 2 ≤ n)
    (S : Type u) [CommRing S] [Algebra (nodalChartRing R (π ^ n)) S]
    [IsLocalization.Away (nodalGen R (π ^ n) 0) S] [Algebra R S]
    [IsScalarTower R (nodalChartRing R (π ^ n)) S] :
    IsRegular (Spec (CommRingCat.of ↥(nodalXChart π n S)))
```

**`Stacks.isRegular_spec_nodalYChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NodalChart/Regularity.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NodalChart/Regularity.lean#L565). The attribute's comment: “the y-chart of X' is regular”.

> **The `y`-chart of the blowup of the standard nodal model is regular.**

```lean
public theorem isRegular_spec_nodalYChart {π : R} (hπ : Irreducible π) {n : ℕ} (hn : 2 ≤ n)
    (S : Type u) [CommRing S] [Algebra (nodalChartRing R (π ^ n)) S]
    [IsLocalization.Away (nodalGen R (π ^ n) 1) S] [Algebra R S]
    [IsScalarTower R (nodalChartRing R (π ^ n)) S] :
    IsRegular (Spec (CommRingCat.of ↥(nodalYChart π n S)))
```

## Tag 0CDD, a lemma

[Tag 0CDD](https://stacks.math.columbia.edu/tag/0CDD) in the Stacks Project.

**`Stacks.Models.exists_etale_nodalChart_pow_uniformizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableNodalChart.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableNodalChart.lean#L538).

> **Stacks 0CDD.** Let `R` be a discrete valuation ring, let `f : X ⟶ Spec R` be at-worst-nodal
> of relative dimension one, and let `x` be a point of the special fibre. Then there is an étale
> extension `R ⊆ R'` of discrete valuation rings, a scheme `U` with étale morphisms `U ⟶ X` and
> `U ⟶ Spec A` over `Spec R'`, and a point `x'` of `U` above `x`, with
>
> `A = R'[u, v]/(uv)`  or  `A = R'[u, v]/(uv - π ^ n)`
>
> for a uniformizer `π` of `R'` and `n ≥ 0`; the two cases are the vanishing and the nonvanishing
> of the parameter `h`, which is a power of a uniformizer in the second case.
>
> The étale local structure in chart form is
> `Stacks.NodalEtaleLocalStructure.nonempty_nodalChartNeighbourhood_of_atWorstNodal` (Tag 0CBY at
> a singular point of the fibre, Tag 054L at a smooth one), and the translation into the
> statement of the tag is
> `Stacks.Models.exists_etale_nodalChart_pow_uniformizer_of_nodalChartNeighbourhood`.

```lean
public theorem exists_etale_nodalChart_pow_uniformizer
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    (hf : IsAtWorstNodalOfRelativeDimensionOne f)
    (x : X) (hx : f.base x = IsLocalRing.closedPoint R) :
    ∃ (R' : Type u) (_ : CommRing R') (_ : IsDomain R')
      (_ : IsDiscreteValuationRing R') (_ : Algebra R R')
      (_ : IsDiscreteValuationRing.IsExtension R R') (_ : Algebra.Etale R R') (h : R'),
      (h = 0 ∨ ∃ (π : R') (n : ℕ), Irreducible π ∧ h = π ^ n) ∧
        ∃ (U : Scheme.{u}) (g : U ⟶ X) (j : U ⟶ Spec (.of (nodalChartRing R' h))) (x' : U),
          Etale g ∧ Etale j ∧ g.base x' = x ∧
            g ≫ f = j ≫
              Spec.map (CommRingCat.ofHom (algebraMap R' (nodalChartRing R' h))) ≫
                Spec.map (CommRingCat.ofHom (algebraMap R R'))
```

## Tag 0CDE, a lemma

[Tag 0CDE](https://stacks.math.columbia.edu/tag/0CDE) in the Stacks Project.

**`Stacks.SemistableReduction.exists_nodalBlowupChain_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NodalResolution.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NodalResolution.lean#L542).

> **Stacks Project, Tag 0CDE.** Let `R` be a discrete valuation ring and let `X` be a
> quasi-compact scheme which is at-worst-nodal of relative dimension one over `R`, with smooth
> generic fibre. Then there is a finite sequence `X_m ⟶ ⋯ ⟶ X_1 ⟶ X_0 = X` such that
> 1. each `X_{i+1} ⟶ X_i` is the blowing up of `X_i` in a closed point at which `X_i` is singular,
> 2. each `X_i ⟶ Spec R` is at-worst-nodal of relative dimension one, and
> 3. `X_m` is regular.
>
> The sequence is `Stacks.SemistableReduction.NodalBlowupChain f Y h` with `h : Y ⟶ X` its
> composite, which records (1) and (2) at every step, and (3) is `IsRegular Y`. The generic fibre is
> the fibre of `f` over the generic point `⊥` of `Spec R`.

```lean
public theorem exists_nodalBlowupChain_isRegular {X : Scheme.{u}} [CompactSpace X]
    (f : X ⟶ Spec (.of R)) (hf : IsAtWorstNodalOfRelativeDimensionOne f)
    (hsmooth : Smooth (f.fiberToSpecResidueField (⊥ : PrimeSpectrum R))) :
    ∃ (Y : Scheme.{u}) (h : Y ⟶ X), NodalBlowupChain f Y h ∧ IsRegular Y
```

## Tag 0CDF, a lemma

[Tag 0CDF](https://stacks.math.columbia.edu/tag/0CDF) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_of_isContractionOfExceptionalCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NodalContraction/Nodal.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NodalContraction/Nodal.lean#L50).

> **Stacks Project, Tag 0CDF.** Let `R` be a discrete valuation ring and let
> `f : X ⟶ Spec R` be at-worst-nodal of relative dimension one. Let `b : X ⟶ X'` be the
> contraction of an exceptional curve `E ⊆ X` of the first kind, presented by its ideal sheaf `D`
> and an isomorphism `e : 𝐏¹_κ ≅ E`. Then `X'` is at-worst-nodal of relative dimension one over
> `R`: there is a morphism `f' : X' ⟶ Spec R` with `b ≫ f' = f`, and it is at-worst-nodal of
> relative dimension one.
>
> Away from the contracted point `b` is an isomorphism, so the only issue is a neighbourhood of
> that point. The closed fibre of `f` is reduced, so the uniformizer of `R` vanishes to order one
> along `E` and therefore lies in the maximal ideal at the contracted point but not in its square.
> The local ring there being regular of dimension two, the local ring of the closed fibre is
> regular of dimension one; its residue field is geometrically reduced over the residue field of
> `R` because the closed fibre of `f` is. Hence the closed fibre of `f'` is smooth at the
> contracted point, and with flatness so is `f'`; a morphism smooth of relative dimension one is
> at-worst-nodal of relative dimension one.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_of_isContractionOfExceptionalCurve
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X X' : Scheme.{u}} (D : X.IdealSheafData) (κ : Type u) [Field κ]
    (e : projectiveLineProj κ ≅ D.subscheme)
    (hE : D.IsExceptionalCurveOfFirstKind κ e)
    (b : X ⟶ X') (hb : IsContractionOfExceptionalCurve D b)
    (f : X ⟶ Spec (CommRingCat.of R))
    (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    ∃ f' : X' ⟶ Spec (CommRingCat.of R),
      b ≫ f' = f ∧ IsAtWorstNodalOfRelativeDimensionOne f'
```

## Tag 0CDG, a lemma

[Tag 0CDG](https://stacks.math.columbia.edu/tag/0CDG) in the Stacks Project.

**`Stacks.Models.tfae_hasSemistableReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/ReductionTypes.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/ReductionTypes.lean#L139).

> **Stacks Project, Tag 0CDG.** Let `R` be a discrete valuation ring with fraction field `K` and
> let `C` be a smooth projective curve over `K` with `H⁰(C, 𝒪_C) = K`. The following are equivalent:
> 1. there exists a proper model of `C` which is at-worst-nodal of relative dimension one over `R`,
> 2. there exists a minimal model of `C` which is at-worst-nodal of relative dimension one over
>    `R`, and
> 3. any minimal model of `C` is at-worst-nodal of relative dimension one over `R`.
>
> Condition (1) is the base's `Stacks.Models.HasSemistableReduction`, the definition of semistable
> reduction ([Stacks, Tag 0CDH]); minimal models are `Stacks.Models.IsMinimalModel`
> ([Stacks, Tag 0C2V]).

```lean
public theorem tfae_hasSemistableReduction {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (hc : IsProjective c)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] :
    List.TFAE [HasSemistableReduction R c hc,
      ∃ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
        (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
        IsMinimalModel c p e ∧ IsAtWorstNodalOfRelativeDimensionOne p,
      ∀ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
        (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
        IsMinimalModel c p e → IsAtWorstNodalOfRelativeDimensionOne p]
```

## Tag 0CDH, a definition

[Tag 0CDH](https://stacks.math.columbia.edu/tag/0CDH) in the Stacks Project.

**`Stacks.Models.HasSemistableReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/Reduction.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/Reduction.lean#L70). The attribute's comment: “existence of a proper model of the curve that is at-worst-nodal of relative dimension one”.

> **Stacks Project, Tag 0CDH.** A smooth projective curve `C` over the fraction field `K` of
> a discrete valuation ring `R`, with `H⁰(C, 𝒪_C) = K`, has *semistable reduction* if there is a
> proper model `X ⟶ Spec R` of `C` which is at-worst-nodal of relative dimension one.

```lean
def HasSemistableReduction {C : Scheme.{u}} (C_to_K : C ⟶ Spec (.of K))
    [IsCurve K C_to_K] [Smooth C_to_K] (_ : IsProjective C_to_K)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ C_to_K.appTop)] : Prop
```

## Tag 0CDI, a lemma

[Tag 0CDI](https://stacks.math.columbia.edu/tag/0CDI) in the Stacks Project.

**`Stacks.Models.tfae_hasGoodReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/ReductionTypes.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/ReductionTypes.lean#L170).

> **Stacks Project, Tag 0CDI.** Let `R` be a discrete valuation ring with fraction field `K` and
> let `C` be a smooth projective curve over `K` with `H⁰(C, 𝒪_C) = K`. The following are equivalent:
> 1. there exists a proper smooth model for `C`,
> 2. there exists a minimal model for `C` which is smooth over `R`,
> 3. any minimal model is smooth over `R`.
>
> Condition (1) is the base's `Stacks.Models.HasGoodReduction`, the definition of good reduction
> ([Stacks, Tag 0CDJ]). A smooth proper model is minimal: its special fibre is connected
> ([Stacks, Tag 0C62]) and smooth, hence irreducible, so its numerical type is minimal
> ([Stacks, Tag 0CA6]).

```lean
public theorem tfae_hasGoodReduction {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (hc : IsProjective c)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] :
    List.TFAE [HasGoodReduction R c hc,
      ∃ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
        (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
        IsMinimalModel c p e ∧ Smooth p,
      ∀ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
        (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
        IsMinimalModel c p e → Smooth p]
```

## Tag 0CDJ, a definition

[Tag 0CDJ](https://stacks.math.columbia.edu/tag/0CDJ) in the Stacks Project.

**`Stacks.Models.HasGoodReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/Reduction.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/Reduction.lean#L81). The attribute's comment: “existence of a proper smooth model of the curve”.

> **Stacks Project, Tag 0CDJ.** A smooth projective curve `C` over the fraction field `K` of
> a discrete valuation ring `R`, with `H⁰(C, 𝒪_C) = K`, has *good reduction* if there is a
> proper model `X ⟶ Spec R` of `C` which is smooth over `R`.

```lean
def HasGoodReduction {C : Scheme.{u}} (C_to_K : C ⟶ Spec (.of K))
    [IsCurve K C_to_K] [Smooth C_to_K] (_ : IsProjective C_to_K)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ C_to_K.appTop)] : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.14, Tag 0CDB](https://stacks.math.columbia.edu/tag/0CDB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
