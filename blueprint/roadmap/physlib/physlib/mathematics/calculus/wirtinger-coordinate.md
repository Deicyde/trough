---
declaration: module
origin: cited
lean: Physlib.Wirtinger.differentiableAt_complex_iff_dWirtingerAntiCoord_eq_zero, Physlib.Wirtinger.dWirtingerCoord_dWirtingerAntiCoord_comm, Physlib.Wirtinger.dWirtingerCoord, Physlib.Wirtinger.dWirtingerAntiCoord, Physlib.Wirtinger.dWirtingerCoord_apply, Physlib.Wirtinger.dWirtingerAntiCoord_apply, Physlib.Wirtinger.dWirtingerCoord_congr_of_eventuallyEq_apply, Physlib.Wirtinger.dWirtingerCoord_const
statement: formalized
proof: formalized
---

# Partial Wirtinger derivatives `∂_I`, `∂̄_I` in a complex coordinate basis on `ℂ^n`

The module `Physlib.Mathematics.Calculus.Wirtinger.Coordinate`, [Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean): 42 declarations, 42 with a docstring, 2 listed as significant; 6 private, not shown.

## Notation

> The conventions of `Wirtinger.Basic` carry over verbatim, with the directional subscript `v`
> replaced by a coordinate index `I` (standing for the direction `Pi.single I 1`).
>
> * `∂_I f` and `∂̄_I f` are the holomorphic and anti-holomorphic coordinate Wirtinger
>   derivatives of `f` in the I-th coordinate direction `Pi.single I 1` — the bar sits on the
>   operator, never on the subscript. They are the directional `∂_v f` / `∂̄_v f` of
>   `Wirtinger.Basic` at `v = Pi.single I 1`. For iterated derivatives the operators compose,
>   `∂_I ∂̄_J f`.
> * `z^I` is the I-th coordinate `u ↦ u^I`; `z̄^I = star z^I` is its pointwise conjugate (the
>   `f̄` convention of `Wirtinger.Basic`).
> * `∂_x`, `∂_y` are the slot-I real and imaginary Fréchet derivatives, along the directions
>   `Pi.single I 1` and `Pi.single I i`.
> * `δ_IJ` is the Kronecker delta.

## i. Overview

> Coordinate specialization of `Wirtinger.Basic` to `V = ℂ^n` (spelled `ι → ℂ`,
> `n = |ι|`, `ι` a `Fintype`), fixing the direction to the I-th basis vector
> `Pi.single I 1`:
>
>   `∂_I f  := ∂_v f`   at `v = Pi.single I 1`   (`dWirtingerCoord`)
>   `∂̄_I f := ∂̄_v f`  at `v = Pi.single I 1`   (`dWirtingerAntiCoord`)
>
> `∂_I`, `∂̄_I` are the partial Wirtinger derivatives w.r.t. coordinate `I`, the
> other coordinates fixed. Coordinate values:
>
>   `∂_I z^J = δ_IJ`,   `∂̄_I z̄^J = δ_IJ`,   `∂̄_I z^J = ∂_I z̄^J = 0`.
>
> The basis makes the directional calculus computational. The operators
> `dWirtingerCoord` / `dWirtingerAntiCoord` (§A, with real-Fréchet unfolding
> `(1/2)(∂_x ∓ i ∂_y)`) come with:
>
> - independence: `∂_I` annihilates every `z̄` and `∂̄_I` every `z` (the coordinate
>   values above), so `z` and `z̄` behave as independent variables;
> - additivity, `ℂ`-linearity, the Leibniz product rule, and the finite-sum rule
>   (§B–C), so any polynomial in the coordinates and their conjugates differentiates
>   termwise;
> - conjugation, swapping the two operators (§B–C): `∂_I f̄ = conj (∂̄_I f)` and
>   `∂̄_I f̄ = conj (∂_I f)`;
> - holomorphic collapse (§B–C): for holomorphic `f`, `∂̄_I f = 0` and `∂_I f` is
>   the ordinary complex partial `fderiv ℂ f u (Pi.single I 1)` (anti-holomorphic
>   `f` dually);
> - the per-coordinate chain rule for an outer `g : ℂ → ℂ` (§D), collapsing to a
>   single term `∂_I (g ∘ f) = deriv g (f u) · ∂_I f` on holomorphic `g` (and `∂̄_I`
>   likewise);
> - the coordinate difference `z^J − z̄^J` (§C);
> - Schwarz's theorem `∂_I ∂̄_J f = ∂̄_J ∂_I f` on `C²` `f` (§E,
>   `dWirtingerCoord_dWirtingerAntiCoord_comm`).
>
> Indexing by `I` casts the calculus in the language of several complex variables.
> The first derivatives assemble into a gradient, the family of partials `∂_I f`
> ranging over the coordinates `I`; the critical points of a holomorphic `h` are
> then where `∂_I h = 0` for every `I`. The mixed second derivatives assemble into a
> complex Hessian, the matrix with entries `∂_I ∂̄_J f` indexed by the pair `(I, J)`;
> for a real function `Φ` the entries `∂_I ∂̄_J Φ` record its second-order behaviour.
>
> That Hessian is Hermitian, by Schwarz (§E). For a real `K`, write the Kähler
> metric `g_{IJ̄} = ∂_I ∂̄_J K`; conjugation gives `star (g_{JĪ}) = ∂̄_J ∂_I K`,
> which Schwarz equates with `∂_I ∂̄_J K`, so `g_{IJ̄} = star (g_{JĪ})`. That is
> Kähler-metric hermiticity.
>
> The coordinate maps are Mathlib primitives — `z^I` is `ContinuousLinearMap.proj`, `z̄^I` its
> `star` — and the holomorphic collapse reads `fderiv ℝ f = fderiv ℂ f` off the `restrictScalars`
> bridge (§B).
>
> Differentiability convention: hypothesis-bearing rules are pointwise (at `u`,
> `DifferentiableAt`), valid on a proper subdomain (e.g. a slit-domain log Kähler
> potential); `funext` locally for a function-level form. Hypothesis-free constant
> and coordinate facts are function equalities.

## ii. Key results

> - `Physlib.Wirtinger.dWirtingerCoord` / `dWirtingerAntiCoord` : the
>     coordinate Wirtinger operators, definitionally the directional operators
>     along `Pi.single I 1`; their real-Fréchet form `dWirtingerCoord_apply` /
>     `dWirtingerAntiCoord_apply` is `∂_I f = (1/2)(∂_x ∓ i ∂_y) f`.
> - `Physlib.Wirtinger.dWirtingerCoord_coordProj` /
>     `dWirtingerAntiCoord_coordProj` / `dWirtingerCoord_conjCoord` /
>     `dWirtingerAntiCoord_conjCoord` : the four Kronecker coordinate values
>     `∂_I z^J = δ_IJ`, `∂̄_I z̄^J = δ_IJ`, `∂̄_I z^J = ∂_I z̄^J = 0`.
> - `Physlib.Wirtinger.dWirtingerCoord_add_apply` / `dWirtingerCoord_smul_apply` /
>     `dWirtingerCoord_mul_apply` / `dWirtingerCoord_fun_sum_apply` : additivity,
>     `ℂ`-linearity, the Leibniz rule, and the finite-sum rule (with
>     anti-holomorphic duals).
> - `Physlib.Wirtinger.dWirtingerCoord_star_comp_apply` /
>     `dWirtingerAntiCoord_star_comp_apply` : conjugating the inner field swaps the
>     two operators, `∂_I f̄ = conj (∂̄_I f)`.
> - `Physlib.Wirtinger.dWirtingerCoord_eq_complex_fderiv_apply` /
>     `dWirtingerAntiCoord_eq_zero_of_holomorphic_apply` : holomorphic collapse for
>     the coordinate operators (with anti-holomorphic duals).
> - `Physlib.Wirtinger.dWirtingerCoord_comp_apply` /
>     `dWirtingerCoord_comp_holomorphic_apply` (and their anti-holomorphic duals): the
>     two-term Wirtinger chain rule for an outer `g : ℂ → ℂ`, collapsing to the
>     single-term `deriv g (f u) · ∂_I f` for holomorphic `g`.
> - `Physlib.Wirtinger.dWirtingerCoord_coordDiff` /
>     `dWirtingerAntiCoord_coordDiff` : Wirtinger derivatives of the
>     coordinate difference `z^J − z̄^J`.
> - `Physlib.Wirtinger.differentiableAt_dWirtingerCoord` /
>     `differentiableAt_dWirtingerAntiCoord` : a first coordinate Wirtinger derivative of a
>     `C²` function is itself real-differentiable (§E).
> - `Physlib.Wirtinger.dWirtingerCoord_dWirtingerAntiCoord_comm` : Schwarz's
>     theorem for the coordinate operators, `∂_I ∂̄_J f = ∂̄_J ∂_I f` on
>     `C²` `f`.
> - `Physlib.Wirtinger.dWirtingerCoord_comp_clm_zero` / `dWirtingerCoord_comp_clm_col` (and their
>     anti-holomorphic duals): the derivative of `h ∘ P` for a continuous ℝ-linear map `P`, read off
>     from how `P` acts on the coordinate column (§F).

## A. The coordinate Wirtinger operators

> The two coordinate Wirtinger operators are the directional Wirtinger derivatives
> of `Wirtinger.Basic` along the I-th coordinate direction `Pi.single I 1`:
>
>   dWirtingerCoord f I    = (1/2) · (∂\_x − i · ∂\_y) f
>   dWirtingerAntiCoord f I = (1/2) · (∂\_x + i · ∂\_y) f
>
> where `∂_x` and `∂_y` are the real Fréchet derivatives of `f` along the slot-I
> real and imaginary coordinate directions `Pi.single I 1` and
> `Pi.single I Complex.I` (the latter is `Complex.I • Pi.single I 1`). The sign on
> the imaginary-direction term is the only difference, making the two operators
> dual on (anti)holomorphic functions (§B, §C).
>
> Each `∂_I` is thus a 1-D directional derivative taken along the standard basis vector
> `Pi.single I 1` — the whole calculus is the one-variable theory applied direction by
> direction. The coordinates decouple (`∂_I z^J = δ_IJ`, §B) because the coordinate functionals
> `z^J` are the dual basis to the standard basis: `z^J (Pi.single I 1) = δ_IJ`.

**`Physlib.Wirtinger.dWirtingerCoord`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L168).

> Holomorphic Wirtinger derivative along the I-th coordinate of `ι → ℂ`.

```lean
def dWirtingerCoord (f : (ι → ℂ) → ℂ) (I : ι) : (ι → ℂ) → ℂ
```

**`Physlib.Wirtinger.dWirtingerAntiCoord`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L172).

> Anti-holomorphic Wirtinger derivative along the I-th coordinate of `ι → ℂ`.

```lean
def dWirtingerAntiCoord (f : (ι → ℂ) → ℂ) (I : ι) : (ι → ℂ) → ℂ
```

**`Physlib.Wirtinger.dWirtingerCoord_apply`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L181).

> Real-Fréchet form of `dWirtingerCoord`:
> `dWirtingerCoord f I u = (1/2)(∂_x − i · ∂_y) f`,
> the derivatives along the slot-I real and imaginary coordinate directions.
> Unconditional — the directional definition makes it definitional
> (`Complex.I • Pi.single I 1 = Pi.single I Complex.I`); no differentiability
> hypothesis is needed.

```lean
lemma dWirtingerCoord_apply {f : (ι → ℂ) → ℂ}
    {u : (ι → ℂ)} (I : ι) :
    dWirtingerCoord f I u = (1 / 2 : ℂ) * (fderiv ℝ f u (Pi.single I 1)
      - Complex.I * fderiv ℝ f u (Pi.single I Complex.I))
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L191).

> Real-Fréchet form of `dWirtingerAntiCoord`:
> `∂̄_I f = (1/2)(∂_x + i · ∂_y) f`,
> mirror of `dWirtingerCoord_apply` with the sign flip on the imaginary-direction term.
> Unconditional, as for `dWirtingerCoord_apply`.

```lean
lemma dWirtingerAntiCoord_apply {f : (ι → ℂ) → ℂ}
    {u : (ι → ℂ)} (I : ι) :
    dWirtingerAntiCoord f I u = (1 / 2 : ℂ) * (fderiv ℝ f u (Pi.single I 1)
      + Complex.I * fderiv ℝ f u (Pi.single I Complex.I))
```

## B. Properties of `dWirtingerCoord`

> Each rule is the `d = Pi.single I 1` specialisation of its `Wirtinger`
> foundation analogue. Rules carrying a differentiability hypothesis are stated
> **pointwise** (at `u`, hypothesis `DifferentiableAt`) — the weakest form, and the
> one to reach for on a function differentiable only on a proper domain; a consumer wanting
> a function-level equation `funext`s locally. The hypothesis-free constant and
> coordinate facts are stated as function equalities — the constant and
> holomorphic-coordinate ones (`dWirtingerCoord_const`, `dWirtingerCoord_coordProj`) `@[simp]`.
>
> The holomorphic collapse `∂_I f = fderiv ℂ f` for holomorphic `f` below (with the dual
> `∂̄_I f = 0` in §C) needs the *real* derivative `fderiv ℝ f u` to be `ℂ`-linear. For holomorphic
> `f`, `fderiv ℝ f u` is the `ℂ`-linear `fderiv ℂ f u` with scalars restricted to
> `ℝ`, `fderiv ℝ f u = (fderiv ℂ f u).restrictScalars ℝ` (`HasFDerivAt.restrictScalars`).
> Restricting scalars drops the `ℂ`-linear *bundling*, not the behaviour: the map still commutes
> with `i`, `fderiv ℝ f u (i • d) = i • fderiv ℝ f u d` — the `ℂ`-linearity the collapse consumes.
> `clinear_of_holomorphic` packages this, via `DifferentiableAt.fderiv_restrictScalars` and
> `ContinuousLinearMap.coe_restrictScalars'`; `DifferentiableAt.restrictScalars` supplies the
> `ℝ`-differentiability.

**`Physlib.Wirtinger.dWirtingerCoord_congr_of_eventuallyEq_apply`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L240).

> `dWirtingerCoord` is local: functions agreeing on a neighbourhood of `u` have equal
> holomorphic Wirtinger derivative at `u` (`f₁ =ᶠ[nhds u] f₂ ⟹ ∂_I f₁ u = ∂_I f₂ u`).

```lean
lemma dWirtingerCoord_congr_of_eventuallyEq_apply {f₁ f₂ : (ι → ℂ) → ℂ}
    {u : (ι → ℂ)} (h : f₁ =ᶠ[nhds u] f₂) (I : ι) :
    dWirtingerCoord f₁ I u = dWirtingerCoord f₂ I u
```

**`Physlib.Wirtinger.dWirtingerCoord_const`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L246).

> Constants have zero coordinate derivative: `∂_I c = 0`.

```lean
lemma dWirtingerCoord_const (c : ℂ) (I : ι) :
    dWirtingerCoord (fun _ : (ι → ℂ) => c) I = 0
```

**`Physlib.Wirtinger.dWirtingerCoord_neg_apply`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L253).

> Pointwise negation rule for the holomorphic coordinate derivative at `u`:
> `∂_I (−f) = −∂_I f`. Used with `dWirtingerCoord_add_apply` to assemble the
> coordinate-difference rule `dWirtingerCoord_coordDiff` (§C).

```lean
lemma dWirtingerCoord_neg_apply {u : (ι → ℂ)} (I : ι) :
    dWirtingerCoord (fun v => -(f v)) I u = -(dWirtingerCoord f I u)
```

**`Physlib.Wirtinger.dWirtingerCoord_coordProj`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L268).

> `∂_I z^J = δ_IJ`. The holomorphic coordinate-independence value; also feeds the
> coordinate-difference rule `dWirtingerCoord_coordDiff` and the conjugate-coordinate value
> `dWirtingerAntiCoord_conjCoord` (§C).

```lean
lemma dWirtingerCoord_coordProj (I J : ι) :
    dWirtingerCoord (fun u : (ι → ℂ) => u J) I =
      fun _ => if I = J then 1 else 0
```

**`Physlib.Wirtinger.dWirtingerCoord_add_apply`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L280).

> Pointwise additivity of the holomorphic coordinate derivative at `u`:
> `∂_I (f + g) = ∂_I f + ∂_I g`. Used to assemble the coordinate-difference rule
> `dWirtingerCoord_coordDiff` (§C).

```lean
lemma dWirtingerCoord_add_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (hg : DifferentiableAt ℝ g u) (I : ι) :
    dWirtingerCoord (f + g) I u = dWirtingerCoord f I u + dWirtingerCoord g I u
```

**`Physlib.Wirtinger.dWirtingerCoord_smul_apply`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L287).

> Pointwise compatibility with complex scalar multiplication at `u`:
> `∂_I (c • f) = c • ∂_I f`.

```lean
lemma dWirtingerCoord_smul_apply {u : (ι → ℂ)}
    (c : ℂ) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerCoord (c • f) I u = c • dWirtingerCoord f I u
```

**`Physlib.Wirtinger.dWirtingerCoord_mul_apply`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L294).

> Pointwise Leibniz rule for the holomorphic coordinate derivative at `u`:
> `∂_I (f · g) = ∂_I f · g + f · ∂_I g`.

```lean
lemma dWirtingerCoord_mul_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (hg : DifferentiableAt ℝ g u) (I : ι) :
    dWirtingerCoord (f * g) I u =
      dWirtingerCoord f I u * g u + f u * dWirtingerCoord g I u
```

**`Physlib.Wirtinger.dWirtingerCoord_fun_sum_apply`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L302).

> Pointwise finite-sum rule for holomorphic coordinate derivatives at `u`:
> `∂_I (∑ a ∈ s, F a) = ∑ a ∈ s, ∂_I (F a)`.

```lean
lemma dWirtingerCoord_fun_sum_apply {α : Type*} {s : Finset α}
    {F : α → (ι → ℂ) → ℂ} {u : (ι → ℂ)}
    (hF : ∀ a ∈ s, DifferentiableAt ℝ (F a) u) (I : ι) :
    dWirtingerCoord (fun v => ∑ a ∈ s, F a v) I u =
      ∑ a ∈ s, dWirtingerCoord (F a) I u
```

**`Physlib.Wirtinger.dWirtingerCoord_eq_complex_fderiv_apply`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L311).

> For a holomorphic function, `dWirtingerCoord` is the complex Fréchet derivative in
> the corresponding coordinate direction: `∂_I f = fderiv ℂ f u (Pi.single I 1)`.

```lean
lemma dWirtingerCoord_eq_complex_fderiv_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℂ f u) (I : ι) :
    dWirtingerCoord f I u = fderiv ℂ f u (Pi.single I 1)
```

**`Physlib.Wirtinger.dWirtingerCoord_eq_zero_of_antiHolomorphic_apply`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L345).

> An *anti-holomorphic* function `v ↦ g (star v)` (a holomorphic `g` precomposed
> with conjugation) depends on the coordinates only through their conjugates `z̄`. Its
> holomorphic derivative therefore vanishes, `∂_I (g ∘ star) = 0`, since `∂_I`
> differentiates w.r.t. `z` and treats `z̄` as constant. Dual to `∂̄_I f = 0` for
> holomorphic `f`.

```lean
lemma dWirtingerCoord_eq_zero_of_antiHolomorphic_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℂ g (star u)) (I : ι) :
    dWirtingerCoord (fun v : (ι → ℂ) => g (star v)) I u = 0
```

## C. Properties of `dWirtingerAntiCoord`

> This section is the `dWirtingerAntiCoord` mirror of §B: every rule with `z` and `z̄`
> swapped (locality, constants, negation, additivity, scalar compatibility, Leibniz, the
> finite-sum rule), together with the holomorphic collapse `∂̄_I f = 0`.
>
> It also collects the two *conjugate-coordinate* values, one per operator:
> `∂_I z̄^J = 0` (`dWirtingerCoord_conjCoord`) and `∂̄_I z̄^J = δ_IJ`
> (`dWirtingerAntiCoord_conjCoord`). Since `z̄^J = star z^J`, each is the conjugate of the
> corresponding value on the holomorphic coordinate `z^J`, read off through the foundation
> conjugation lemmas `dWirtingerDir_star_comp` / `dWirtingerAntiDir_star_comp` rather than
> recomputed.

**`Physlib.Wirtinger.dWirtingerAntiCoord_congr_of_eventuallyEq_apply`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L377).

> `dWirtingerAntiCoord` is local (`f₁ =ᶠ[nhds u] f₂ ⟹ ∂̄_I f₁ u = ∂̄_I f₂ u`).

```lean
lemma dWirtingerAntiCoord_congr_of_eventuallyEq_apply {f₁ f₂ : (ι → ℂ) → ℂ}
    {u : (ι → ℂ)} (h : f₁ =ᶠ[nhds u] f₂) (I : ι) :
    dWirtingerAntiCoord f₁ I u = dWirtingerAntiCoord f₂ I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_const`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L383).

> Constants have zero anti-holomorphic coordinate derivative: `∂̄_I c = 0`.

```lean
lemma dWirtingerAntiCoord_const (c : ℂ) (I : ι) :
    dWirtingerAntiCoord (fun _ : (ι → ℂ) => c) I = 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_neg_apply`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L390).

> Pointwise negation rule for the anti-holomorphic coordinate derivative at `u`:
> `∂̄_I (−f) = −∂̄_I f`. Used with `dWirtingerAntiCoord_add_apply` to assemble the
> coordinate-difference rule `dWirtingerAntiCoord_coordDiff` (§C).

```lean
lemma dWirtingerAntiCoord_neg_apply {u : (ι → ℂ)} (I : ι) :
    dWirtingerAntiCoord (fun v => -(f v)) I u = -(dWirtingerAntiCoord f I u)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_coordProj`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L397).

> `∂̄_I z^J = 0`. The anti-holomorphic coordinate-independence value; also feeds the
> coordinate-difference rule `dWirtingerAntiCoord_coordDiff` and the conjugate-coordinate
> value `dWirtingerCoord_conjCoord` (§C).

```lean
lemma dWirtingerAntiCoord_coordProj (I J : ι) :
    dWirtingerAntiCoord (fun u : (ι → ℂ) => u J) I = 0
```

**`Physlib.Wirtinger.dWirtingerCoord_conjCoord`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L406).

> `∂_I z̄^J = 0`. The conjugate of `dWirtingerAntiCoord_coordProj` (`z̄^J = star z^J`),
> read off through `dWirtingerDir_star_comp` rather than recomputed. Used to assemble the
> coordinate-difference rule `dWirtingerCoord_coordDiff` (§C).

```lean
lemma dWirtingerCoord_conjCoord (I J : ι) :
    dWirtingerCoord (fun u : (ι → ℂ) => star (u J)) I = 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_conjCoord`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L415).

> `∂̄_I z̄^J = δ_IJ`. The conjugate of `dWirtingerCoord_coordProj`, read off through
> `dWirtingerAntiDir_star_comp` rather than recomputed. Used to assemble the
> coordinate-difference rule `dWirtingerAntiCoord_coordDiff` (§C).

```lean
lemma dWirtingerAntiCoord_conjCoord (I J : ι) :
    dWirtingerAntiCoord (fun u : (ι → ℂ) => star (u J)) I =
      fun _ => if I = J then 1 else 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_add_apply`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L429).

> Pointwise additivity of the anti-holomorphic coordinate derivative at `u`:
> `∂̄_I (f + g) = ∂̄_I f + ∂̄_I g`. Used to assemble the coordinate-difference rule
> `dWirtingerAntiCoord_coordDiff` (§C).

```lean
lemma dWirtingerAntiCoord_add_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (hg : DifferentiableAt ℝ g u) (I : ι) :
    dWirtingerAntiCoord (f + g) I u = dWirtingerAntiCoord f I u + dWirtingerAntiCoord g I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_smul_apply`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L436).

> Pointwise compatibility with complex scalar multiplication at `u`:
> `∂̄_I (c • f) = c • ∂̄_I f`.

```lean
lemma dWirtingerAntiCoord_smul_apply {u : (ι → ℂ)}
    (c : ℂ) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerAntiCoord (c • f) I u = c • dWirtingerAntiCoord f I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_mul_apply`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L443).

> Pointwise Leibniz rule for the anti-holomorphic coordinate derivative at `u`:
> `∂̄_I (f · g) = ∂̄_I f · g + f · ∂̄_I g`.

```lean
lemma dWirtingerAntiCoord_mul_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (hg : DifferentiableAt ℝ g u) (I : ι) :
    dWirtingerAntiCoord (f * g) I u =
      dWirtingerAntiCoord f I u * g u + f u * dWirtingerAntiCoord g I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_fun_sum_apply`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L451).

> Pointwise finite-sum rule for anti-holomorphic coordinate derivatives at `u`:
> `∂̄_I (∑ a ∈ s, F a) = ∑ a ∈ s, ∂̄_I (F a)`.

```lean
lemma dWirtingerAntiCoord_fun_sum_apply {α : Type*} {s : Finset α}
    {F : α → (ι → ℂ) → ℂ} {u : (ι → ℂ)}
    (hF : ∀ a ∈ s, DifferentiableAt ℝ (F a) u) (I : ι) :
    dWirtingerAntiCoord (fun v => ∑ a ∈ s, F a v) I u =
      ∑ a ∈ s, dWirtingerAntiCoord (F a) I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_eq_complex_fderiv_apply`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L462).

> For an anti-holomorphic function the anti-holomorphic Wirtinger derivative equals
> the complex Fréchet derivative of `g` at `star u` along the slot-I real
> coordinate direction, `∂̄_I (g ∘ star) = fderiv ℂ g (star u) (Pi.single I 1)`.
> Dual of `dWirtingerCoord_eq_complex_fderiv_apply`.

```lean
lemma dWirtingerAntiCoord_eq_complex_fderiv_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℂ g (star u)) (I : ι) :
    dWirtingerAntiCoord (fun v : (ι → ℂ) => g (star v)) I u =
      fderiv ℂ g (star u) (Pi.single I 1)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_eq_zero_of_holomorphic_apply`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L475).

> Holomorphic functions have zero anti-holomorphic coordinate derivative: `∂̄_I f = 0`.

```lean
lemma dWirtingerAntiCoord_eq_zero_of_holomorphic_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℂ f u) (I : ι) :
    dWirtingerAntiCoord f I u = 0
```

**`Physlib.Wirtinger.differentiableAt_complex_iff_dWirtingerAntiCoord_eq_zero`**, a theorem, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L482). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Cauchy–Riemann in coordinates**, the form `∂̄_Ī W = 0` used in physics. Coordinate
> directions suffice by `LinearMap.commutesI_of_basis`.

```lean
theorem differentiableAt_complex_iff_dWirtingerAntiCoord_eq_zero
    (f : (ι → ℂ) → ℂ) (u : ι → ℂ) :
    DifferentiableAt ℂ f u ↔
      DifferentiableAt ℝ f u ∧ ∀ I, dWirtingerAntiCoord f I u = 0
```

### Coordinate-difference Wirtinger derivatives

> The Wirtinger derivatives of the coordinate difference `z^J − z̄^J = 2 i Im(u^J)`, the
> combination any function of the coordinates' imaginary parts differentiates against.
> Collected here for reuse: `∂_I (z^J − z̄^J) = δ_IJ` and `∂̄_I (z^J − z̄^J) = −δ_IJ`.

**`Physlib.Wirtinger.dWirtingerCoord_coordDiff`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L513).

> `∂_I (z^J − z̄^J) = δ_IJ`, from `∂_I z^J = δ_IJ` and
> `∂_I z̄^J = 0`.

```lean
lemma dWirtingerCoord_coordDiff (I J : ι) :
    dWirtingerCoord (fun v : (ι → ℂ) => v J - star (v J)) I
      = fun _ => if I = J then 1 else 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_coordDiff`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L523).

> `∂̄_I (z^J − z̄^J) = −δ_IJ`, from `∂̄_I z^J = 0` and
> `∂̄_I z̄^J = δ_IJ`.

```lean
lemma dWirtingerAntiCoord_coordDiff (I J : ι) :
    dWirtingerAntiCoord (fun v : (ι → ℂ) => v J - star (v J)) I
      = fun _ => if I = J then -1 else 0
```

## D. Wirtinger chain rules for an outer function

> Composing with an outer `g : ℂ → ℂ` gives a **two-term** coordinate chain rule, the
> `d = Pi.single I 1` case of the foundation `dWirtingerDir_comp`:
>
>   `∂_I (g ∘ f) = (∂g/∂f) · ∂_I f + (∂g/∂f̄) · ∂_I f̄`.
>
> A non-holomorphic `g` depends on both its argument and its conjugate, so both channels
> contribute: the holomorphic coefficient `∂g/∂f` and the anti-holomorphic `∂g/∂f̄`, each
> times the matching inner coordinate derivative — two terms where the complex-analytic rule
> has one. The outer `g` enters only through these two coefficients, the directional
> derivatives `dWirtingerDir g 1` and `dWirtingerAntiDir g 1` evaluated at `z = f u` (the
> image of `u` under the inner function, where the chain rule reads off `g`). They are the
> holomorphic and anti-holomorphic parts of `g`'s real Fréchet derivative: every `ℝ`-linear
> map `ℂ → ℂ` splits uniquely as `h ↦ a · h + b · star h`, and on `L = fderiv ℝ g z` the
> weights are `(a, b) = (∂g/∂f, ∂g/∂f̄)`.
>
> For holomorphic `g` the anti-holomorphic coefficient `dWirtingerAntiDir g 1` vanishes and
> `dWirtingerDir g 1` collapses to `deriv g z`, leaving the single-term rule
> `∂_I (g ∘ f) = deriv g (f u) · ∂_I f` (`dWirtingerCoord_comp_holomorphic_apply`, with its
> `∂̄_I` dual). Both collapses are the same `restrictScalars` step as §B — the real derivative
> of a holomorphic `g : ℂ → ℂ` is `ℂ`-linear (`clinear_of_holomorphic` at `E = ℂ`).

**`Physlib.Wirtinger.dWirtingerCoord_comp_apply`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L569).

> The two-term coordinate chain rule for a real-differentiable outer `g`, pointwise at `u`:
> `∂_I (g ∘ f) = (∂g/∂f) · ∂_I f + (∂g/∂f̄) · ∂_I f̄`,
> with coefficients `∂g/∂f = dWirtingerDir g 1 (f u)` and `∂g/∂f̄ = dWirtingerAntiDir g 1 (f u)`.
> The `d = Pi.single I 1` case of the foundation `dWirtingerDir_comp`. The single-term
> holomorphic specialization `dWirtingerCoord_comp_holomorphic_apply` is proved from this.

```lean
lemma dWirtingerCoord_comp_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℝ g (f u)) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerCoord (fun v => g (f v)) I u =
      dWirtingerDir g 1 (f u) * dWirtingerCoord f I u
        + dWirtingerAntiDir g 1 (f u) *
          dWirtingerCoord (fun v : (ι → ℂ) => star (f v)) I u
```

**`Physlib.Wirtinger.dWirtingerCoord_comp_holomorphic_apply`**, a lemma, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L582).

> The single-term coordinate chain rule for a holomorphic outer `g`, pointwise at `u`:
> `∂_I (g ∘ f) = deriv g (f u) · ∂_I f`. From the two-term `dWirtingerCoord_comp_apply`: for
> holomorphic `g` the anti-holomorphic coefficient `dWirtingerAntiDir g 1 (f u)` vanishes and
> `dWirtingerDir g 1 (f u)` collapses to `deriv g (f u)`, both off the `ℂ`-linearity
> `clinear_of_holomorphic` (§B).

```lean
lemma dWirtingerCoord_comp_holomorphic_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℂ g (f u)) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerCoord (fun v => g (f v)) I u =
      deriv g (f u) * dWirtingerCoord f I u
```

**`Physlib.Wirtinger.dWirtingerCoord_star_comp_apply`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L594).

> Conjugating the inner field swaps the two operators: `∂_I f̄ = conj (∂̄_I f)`. The
> `d = Pi.single I 1` case of the foundation `dWirtingerDir_star_comp`.

```lean
lemma dWirtingerCoord_star_comp_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerCoord (fun v : (ι → ℂ) => star (f v)) I u =
      star (dWirtingerAntiCoord f I u)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_comp_apply`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L606).

> The two-term coordinate chain rule for a real-differentiable outer `g`, anti-holomorphic
> version, pointwise at `u`: `∂̄_I (g ∘ f) = (∂g/∂f) · ∂̄_I f + (∂g/∂f̄) · ∂̄_I f̄`. Same outer
> coefficients as `dWirtingerCoord_comp_apply`, now multiplying the anti-holomorphic inner
> derivatives. The `d = Pi.single I 1` case of the foundation `dWirtingerAntiDir_comp`. The
> single-term holomorphic specialization `dWirtingerAntiCoord_comp_holomorphic_apply` is proved
> from this.

```lean
lemma dWirtingerAntiCoord_comp_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℝ g (f u)) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerAntiCoord (fun v => g (f v)) I u =
      dWirtingerDir g 1 (f u) * dWirtingerAntiCoord f I u
        + dWirtingerAntiDir g 1 (f u) *
          dWirtingerAntiCoord (fun v : (ι → ℂ) => star (f v)) I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_comp_holomorphic_apply`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L618).

> The single-term coordinate chain rule for a holomorphic outer `g`, anti-holomorphic
> version, pointwise at `u`: `∂̄_I (g ∘ f) = deriv g (f u) · ∂̄_I f`. As in
> `dWirtingerCoord_comp_holomorphic_apply`, the `∂g/∂f̄` channel vanishes and `∂g/∂f`
> collapses to `deriv g (f u)`.

```lean
lemma dWirtingerAntiCoord_comp_holomorphic_apply {u : (ι → ℂ)}
    (hg : DifferentiableAt ℂ g (f u)) (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerAntiCoord (fun v => g (f v)) I u =
      deriv g (f u) * dWirtingerAntiCoord f I u
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_star_comp_apply`**, a lemma, [line 631](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L631).

> Conjugating the inner field swaps the two operators: `∂̄_I f̄ = conj (∂_I f)`. Dual of
> `dWirtingerCoord_star_comp_apply`, the `d = Pi.single I 1` case of the foundation
> `dWirtingerAntiDir_star_comp`.

```lean
lemma dWirtingerAntiCoord_star_comp_apply {u : (ι → ℂ)}
    (hf : DifferentiableAt ℝ f u) (I : ι) :
    dWirtingerAntiCoord (fun v : (ι → ℂ) => star (f v)) I u =
      star (dWirtingerCoord f I u)
```

## E. Schwarz's theorem for the coordinate operators

> Specialisations of the multivariable theory along `Pi.single I 1`: a first coordinate
> Wirtinger derivative is again real-differentiable, and **Schwarz's theorem** for the mixed
> second derivative on a `C²` function,
>
>   `∂_I ∂̄_J f = ∂̄_J ∂_I f`     (`dWirtingerCoord_dWirtingerAntiCoord_comm`)
>
> This commutation is Kähler-metric hermiticity: with `K` real, `g_{IJ̄} = ∂_I ∂̄_J K` and
> `star (g_{JĪ}) = ∂̄_J ∂_I K`.

**`Physlib.Wirtinger.differentiableAt_dWirtingerCoord`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L661).

> On a `C²` function the holomorphic coordinate Wirtinger derivative is itself
> real-differentiable (`DifferentiableAt ℝ (∂_I f) u`) — the `d = Pi.single I 1` case of
> `differentiableAt_dWirtingerDir`.

```lean
lemma differentiableAt_dWirtingerCoord (hf2 : ContDiffAt ℝ 2 f u) (I : ι) :
    DifferentiableAt ℝ (fun v => dWirtingerCoord f I v) u
```

**`Physlib.Wirtinger.differentiableAt_dWirtingerAntiCoord`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L668).

> On a `C²` function the anti-holomorphic coordinate Wirtinger derivative is itself
> real-differentiable (`DifferentiableAt ℝ (∂̄_J f) u`) — the `d = Pi.single J 1` case of
> `differentiableAt_dWirtingerAntiDir`.

```lean
lemma differentiableAt_dWirtingerAntiCoord (hf2 : ContDiffAt ℝ 2 f u) (J : ι) :
    DifferentiableAt ℝ (fun v => dWirtingerAntiCoord f J v) u
```

**`Physlib.Wirtinger.dWirtingerCoord_dWirtingerAntiCoord_comm`**, a theorem, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L676). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Schwarz's theorem** for the coordinate Wirtinger operators: on a `C²` function the
> holomorphic and anti-holomorphic derivatives commute, `∂_I ∂̄_J f = ∂̄_J ∂_I f`. The
> `d = Pi.single I 1`, `e = Pi.single J 1` case of the general
> `dWirtingerDir_dWirtingerAntiDir_comm`.

```lean
theorem dWirtingerCoord_dWirtingerAntiCoord_comm (hf2 : ContDiffAt ℝ 2 f u) (I J : ι) :
    dWirtingerCoord (fun v => dWirtingerAntiCoord f J v) I u
      = dWirtingerAntiCoord (fun v => dWirtingerCoord f I v) J u
```

## F. Chain rule for an inner continuous linear map

> Pre-composition of a coordinate Wirtinger derivative with a continuous ℝ-linear map `P` into a
> coordinate space, over an arbitrary domain `D`. The directional vanishing/routing is controlled
> entirely by `P`'s action on the coordinate columns `Pi.single c 1` and `Pi.single c Complex.I`.

**`Physlib.Wirtinger.dWirtingerCoord_comp_clm_zero`**, a lemma, [line 697](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L697).

> If the inner continuous ℝ-linear map `P` kills the coordinate column `c`, the holomorphic
> coordinate Wirtinger derivative of `h ∘ P` along `c` vanishes.

```lean
lemma dWirtingerCoord_comp_clm_zero {C_s : Type} [Fintype C_s]
    (P : (D → ℂ) →L[ℝ] (C_s → ℂ)) (h : (C_s → ℂ) → ℂ) (c : D) (u : D → ℂ)
    (hh : DifferentiableAt ℝ h (P u))
    (h1 : P (Pi.single c 1) = 0) (hI : P (Pi.single c Complex.I) = 0) :
    dWirtingerCoord (fun v => h (P v)) c u = 0
```

**`Physlib.Wirtinger.dWirtingerCoord_comp_clm_col`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L708).

> If the inner continuous ℝ-linear map `P` reads the coordinate column `c` as the sector
> coordinate `a₀`, the holomorphic coordinate Wirtinger derivative of `h ∘ P` along `c` is that
> of `h` along `a₀`, evaluated at `P u`.

```lean
lemma dWirtingerCoord_comp_clm_col {C_s : Type} [Fintype C_s] [DecidableEq C_s]
    (P : (D → ℂ) →L[ℝ] (C_s → ℂ)) (h : (C_s → ℂ) → ℂ) (c : D) (a₀ : C_s)
    (u : D → ℂ) (hh : DifferentiableAt ℝ h (P u))
    (h1 : P (Pi.single c 1) = Pi.single a₀ 1)
    (hI : P (Pi.single c Complex.I) = Pi.single a₀ Complex.I) :
    dWirtingerCoord (fun v => h (P v)) c u = dWirtingerCoord h a₀ (P u)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_comp_clm_zero`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L718).

> Anti-holomorphic mirror of `dWirtingerCoord_comp_clm_zero`.

```lean
lemma dWirtingerAntiCoord_comp_clm_zero {C_s : Type} [Fintype C_s]
    (P : (D → ℂ) →L[ℝ] (C_s → ℂ)) (h : (C_s → ℂ) → ℂ) (c : D) (u : D → ℂ)
    (hh : DifferentiableAt ℝ h (P u))
    (h1 : P (Pi.single c 1) = 0) (hI : P (Pi.single c Complex.I) = 0) :
    dWirtingerAntiCoord (fun v => h (P v)) c u = 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_comp_clm_col`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean#L727).

> Anti-holomorphic mirror of `dWirtingerCoord_comp_clm_col`.

```lean
lemma dWirtingerAntiCoord_comp_clm_col {C_s : Type} [Fintype C_s] [DecidableEq C_s]
    (P : (D → ℂ) →L[ℝ] (C_s → ℂ)) (h : (C_s → ℂ) → ℂ) (c : D) (a₀ : C_s)
    (u : D → ℂ) (hh : DifferentiableAt ℝ h (P u))
    (h1 : P (Pi.single c 1) = Pi.single a₀ 1)
    (hI : P (Pi.single c Complex.I) = Pi.single a₀ Complex.I) :
    dWirtingerAntiCoord (fun v => h (P v)) c u = dWirtingerAntiCoord h a₀ (P u)
```

## Depends on

- [Wirtinger calculus](wirtinger-basic.md)

## Sources

- [Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Coordinate.lean)
