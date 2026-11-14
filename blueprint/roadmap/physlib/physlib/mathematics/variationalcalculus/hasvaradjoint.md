---
declaration: module
origin: cited
lean: HasVarAdjoint, HasVarAdjoint.symm, HasVarAdjoint.id, HasVarAdjoint.zero, HasVarAdjoint.comp, HasVarAdjoint.congr_fun, HasVarAdjoint.of_eq, HasVarAdjoint.unique_on_test_functions
statement: formalized
proof: formalized
---

# Variational adjoint

The module `Physlib.Mathematics.VariationalCalculus.HasVarAdjoint`, [Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean): 28 declarations, 3 with a docstring.

> Definition of adjoint of linear function between function spaces. It is inspired by the definition
> of distributional adjoint of linear maps between test functions as described here:
> https://en.wikipedia.org/wiki/Distribution\_(mathematics) under 'Preliminaries: Transpose of a linear
> operator' but we require that the adjoint is function between test functions too.
>
> The key results are:
>   - variational adjoint is unique on test functions
>   - variational adjoint of identity is identity, `HasVarAdjoint.id`
>   - variational adjoint of composition is composition of adjoint in reverse order,
>     `HasVarAdjoint.comp`
>   - variational adjoint of deriv is `- deriv`, `HasVarAdjoint.deriv`
>   - variational adjoint of algebraic operations is algebraic operation of adjoints,
>     `HasVarAdjoint.neg`, `HasVarAdjoint.add`, `HasVarAdjoint.sub`, `HasVarAdjoint.mul_left`,
>     `HasVarAdjoint.mul_right`, `HasVarAdjoint.smul_left`, `HasVarAdjoint.smul_right`

**`HasVarAdjoint`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L51).

> Map `F` from `(X → U)` to `(X → V)` has a variational adjoint `F'` if it preserves
> test functions and satisfies the adjoint relation `⟪F φ, ψ⟫ = ⟪φ, F' ψ⟫`for all test functions
> `φ` and `ψ` for `⟪φ, ψ⟫ = ∫ x, ⟪φ x, ψ x⟫_ℝ ∂μ`.
>
> The canonical example is the function `F = deriv` that has adjoint `F' = - deriv`.
>
> This notion of adjoint allows us to do formally variational calculus as often encountered in physics
> textbooks. In mathematical literature, the adjoint is often defined for unbounded operators, but
> such formal treatment is unnecessarily complicated for physics applications.

```lean
structure HasVarAdjoint
    (F : (X → U) → (Y → V)) (F' : (Y → V) → (X → U)) where
  test_fun_preserving : ∀ φ, IsTestFunction φ → IsTestFunction (F φ)
  test_fun_preserving' : ∀ φ, IsTestFunction φ → IsTestFunction (F' φ)
  adjoint : ∀ φ ψ, IsTestFunction φ → IsTestFunction ψ →
    ∫ y, ⟪F φ y, ψ y⟫_ℝ = ∫ x, ⟪φ x, F' ψ x⟫_ℝ
  ext' : IsLocalizedFunctionTransform F'
```

**`HasVarAdjoint.symm`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L62).

```lean
lemma symm {F : (X → U) → (Y → V)} {F' : (Y → V) → (X → U)}
    (hF : HasVarAdjoint F F') (h : IsLocalizedFunctionTransform F) :
    HasVarAdjoint F' F
```

**`HasVarAdjoint.id`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L77).

```lean
lemma id : HasVarAdjoint (fun φ : X → U => φ) (fun φ => φ)
```

**`HasVarAdjoint.zero`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L83).

```lean
lemma zero : HasVarAdjoint (fun (_ : X → U) (_ : Y) => (0 : V)) (fun _ _ => 0)
```

**`HasVarAdjoint.comp`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L89).

```lean
lemma comp {F : (Y → V) → (Z → W)} {G : (X → U) → (Y → V)} {F' G'}
    (hF : HasVarAdjoint F F') (hG : HasVarAdjoint G G') :
    HasVarAdjoint (fun φ => F (G φ)) (fun φ => G' (F' φ))
```

**`HasVarAdjoint.congr_fun`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L99).

```lean
lemma congr_fun {F G : (X → U) → (Y → V)} {F' : (Y → V) → (X → U)}
    (h : HasVarAdjoint G F') (h' : ∀ φ, IsTestFunction φ → F φ = G φ) :
    HasVarAdjoint F F'
```

**`HasVarAdjoint.of_eq`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L111).

```lean
lemma of_eq {F : (X → U) → (Y → V)} {F' G' : (Y → V) → (X → U)}
    (hF' : HasVarAdjoint F F') (h : ∀ φ, IsTestFunction φ → F' φ = G' φ)
    (hlin : IsLocalizedFunctionTransform G') :
    HasVarAdjoint F G'
```

**`HasVarAdjoint.unique_on_test_functions`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L125).

> Variational adjoint is unique only when applied to test functions.

```lean
lemma unique_on_test_functions {F : (X → U) → (Y → V)} {F' G' : (Y → V) → (X → U)}
    [IsFiniteMeasureOnCompacts (@volume X _)] [(@volume X _).IsOpenPosMeasure]
    [OpensMeasurableSpace X] (hF' : HasVarAdjoint F F') (hG' : HasVarAdjoint F G') :
    ∀ φ, IsTestFunction φ → F' φ = G' φ
```

**`HasVarAdjoint.unique`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L151).

> Variational adjoint is unique only when applied to smooth functions.

```lean
lemma unique
    {X : Type*} [NormedAddCommGroup X] [InnerProductSpace ℝ X]
    [MeasureSpace X] [OpensMeasurableSpace X]
    {Y : Type*} [NormedAddCommGroup Y] [InnerProductSpace ℝ Y]
    [FiniteDimensional ℝ Y] [MeasureSpace Y]
    {F : (X → U) → (Y → V)} {F' G' : (Y → V) → (X → U)}
    [IsFiniteMeasureOnCompacts (@volume X _)] [(@volume X _).IsOpenPosMeasure]
    (hF : HasVarAdjoint F F') (hG : HasVarAdjoint F G') :
    ∀ f, ContDiff ℝ ∞ f → F' f = G' f
```

**`HasVarAdjoint.neg`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L197).

```lean
lemma neg {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)}
    (hF : HasVarAdjoint F F') :
    HasVarAdjoint (fun φ x => - F φ x) (fun φ x => - F' φ x)
```

**`HasVarAdjoint.of_neg`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L207).

```lean
lemma of_neg {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)}
    (hF : HasVarAdjoint (fun φ x => - F φ x) (fun φ x => - F' φ x)) :
    HasVarAdjoint F F'
```

**`HasVarAdjoint.add`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L218).

```lean
lemma add {F G : (X → U) → (X → V)} {F' G' : (X → V) → (X → U)}
    (hF : HasVarAdjoint F F') (hG : HasVarAdjoint G G') :
    HasVarAdjoint (fun φ x => F φ x + G φ x) (fun φ x => F' φ x + G' φ x)
```

**`HasVarAdjoint.sum`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L237).

```lean
lemma sum {ι : Type} [Fintype ι] {F : ι → (X → U) → (X → V)} {F' : ι → (X → V) → (X → U)}
    (hF : ∀ i, HasVarAdjoint (F i) (F' i)) :
    HasVarAdjoint (fun φ x => ∑ i, F i φ x) (fun φ x => ∑ i, F' i φ x)
```

**`HasVarAdjoint.sub`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L260).

```lean
lemma sub {F G : (X → U) → (X → V)} {F' G' : (X → V) → (X → U)}
    (hF : HasVarAdjoint F F') (hG : HasVarAdjoint G G') :
    HasVarAdjoint (fun φ x => F φ x - G φ x) (fun φ x => F' φ x - G' φ x)
```

**`HasVarAdjoint.mul_left`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L267).

```lean
lemma mul_left {F : (X → U) → (X → ℝ)} {ψ : X → ℝ} {F' : (X → ℝ) → (X → U)}
    (hF : HasVarAdjoint F F') (hψ : ContDiff ℝ ∞ ψ) :
    HasVarAdjoint (fun φ x => ψ x * F φ x) (fun φ x => F' (fun x => ψ x * φ x) x)
```

**`HasVarAdjoint.mul_right`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L283).

```lean
lemma mul_right {F : (X → U) → (X → ℝ)} {ψ : X → ℝ} {F' : (X → ℝ) → (X → U)}
    (hF : HasVarAdjoint F F') (hψ : ContDiff ℝ ∞ ψ) :
    HasVarAdjoint (fun φ x => F φ x * ψ x) (fun φ x => F' (fun x => φ x * ψ x) x)
```

**`HasVarAdjoint.smul_left`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L299).

```lean
lemma smul_left {F : (X → U) → (X → V)} {ψ : X → ℝ} {F' : (X → V) → (X → U)}
    (hF : HasVarAdjoint F F') (hψ : ContDiff ℝ ∞ ψ) :
    HasVarAdjoint (fun φ x => ψ x • F φ x) (fun φ x => F' (fun x' => ψ x' • φ x') x)
```

**`HasVarAdjoint.smul_right`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L316).

```lean
lemma smul_right {F : (X → U) → (X → V)} {ψ : X → ℝ} {F' : (X → V) → (X → U)}
    (hF : HasVarAdjoint F F') (hψ : ContDiff ℝ ∞ ψ) :
    HasVarAdjoint (fun φ x => ψ x • F φ x) (fun φ x => F' (fun x' => ψ x' • φ x') x)
```

**`HasVarAdjoint.clm_apply`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L325).

```lean
lemma clm_apply
    [CompleteSpace U] [CompleteSpace V] (f : X → (U →L[ℝ] V))
    (hf : ContDiff ℝ ∞ f) :
    HasVarAdjoint (fun (φ : X → U) x => f x (φ x)) (fun ψ x => _root_.adjoint ℝ (f x) (ψ x))
```

**`HasVarAdjoint.deriv`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L362).

```lean
protected lemma deriv :
    HasVarAdjoint (fun φ : ℝ → U => deriv φ) (fun φ x => - deriv φ x)
```

**`HasVarAdjoint.fderiv_apply`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L394).

```lean
lemma fderiv_apply {dx}
    [ProperSpace X] [BorelSpace X]
    [FiniteDimensional ℝ X] [(@volume X _).IsAddHaarMeasure] :
    HasVarAdjoint (fun φ : X → U => (fderiv ℝ φ · dx)) (fun φ x => - fderiv ℝ φ x dx)
```

**`HasVarAdjoint.adjFDeriv_apply`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L431).

```lean
lemma adjFDeriv_apply
    [InnerProductSpace' ℝ X] [InnerProductSpace' ℝ Y]
    [ProperSpace X] [BorelSpace X] [FiniteDimensional ℝ X]
    [CompleteSpace Y] [(@volume X _).IsAddHaarMeasure] {dy} :
    HasVarAdjoint (fun φ : X → Y => (adjFDeriv ℝ φ · dy)) (fun ψ x => - divergence ℝ ψ x • dy)
```

**`HasVarAdjoint.gradient`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L547).

```lean
protected lemma gradient {d} :
    HasVarAdjoint (fun φ : Space d → ℝ => gradient φ)
    (fun φ x => - Space.div (Space.basis.repr ∘ φ) x)
```

**`HasVarAdjoint.grad`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L563).

```lean
lemma grad {d} : HasVarAdjoint (fun (φ : Space d → ℝ) x => Space.grad φ x)
    (fun ψ x => - Space.div ψ x)
```

**`HasVarAdjoint.div`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L579).

```lean
lemma div {d} : HasVarAdjoint (fun (φ : Space d → EuclideanSpace ℝ (Fin d)) x => Space.div φ x)
    (fun ψ x => - Space.grad ψ x)
```

**`HasVarAdjoint.prod`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L589).

```lean
lemma prod
    [IsFiniteMeasureOnCompacts (@volume X _)] [OpensMeasurableSpace X]
    {F : (X → U) → (X → V)} {G : (X → U) → (X → W)} {F' G'}
    (hF : HasVarAdjoint F F') (hG : HasVarAdjoint G G') :
    HasVarAdjoint
      (fun φ x => (F φ x, G φ x))
      (fun φ x => F' (fun x' => (φ x').1) x + G' (fun x' => (φ x').2) x)
```

**`HasVarAdjoint.fst`**, a lemma, [line 631](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L631).

```lean
lemma fst {F'} {F : (X → U) → (X → W×V)}
    (hF : HasVarAdjoint F F') :
    HasVarAdjoint
      (fun φ x => (F φ x).1)
      (fun φ x => F' (fun x' => (φ x', 0)) x)
```

**`HasVarAdjoint.snd`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean#L653).

```lean
lemma snd {F'} {F : (X → U) → (X → W×V)}
    (hF : HasVarAdjoint F F') :
    HasVarAdjoint
      (fun φ x => (F φ x).2)
      (fun φ x => F' (fun x' => (0, φ x')) x)
```

## Depends on

- [Localized function transforms](islocalizedfunctiontransform.md)
- [Test functions](istestfunction.md)

## Proof depends on

- [Fundamental lemma of the calculus of variations](basic.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjoint.lean)
