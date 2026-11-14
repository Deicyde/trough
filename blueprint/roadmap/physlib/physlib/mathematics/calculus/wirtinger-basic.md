---
declaration: module
origin: cited
lean: Physlib.Wirtinger.differentiableAt_complex_iff_dWirtingerAntiDir_eq_zero, Physlib.Wirtinger.dWirtingerDir_dWirtingerAntiDir_comm, Physlib.Wirtinger.weightedDirDeriv, Physlib.Wirtinger.dWirtingerDir, Physlib.Wirtinger.dWirtingerAntiDir, Physlib.Wirtinger.dWirtingerDir_apply, Physlib.Wirtinger.dWirtingerAntiDir_apply, Physlib.Wirtinger.dWirtingerDir_const
statement: formalized
proof: formalized
---

# Wirtinger calculus

The module `Physlib.Mathematics.Calculus.Wirtinger.Basic`, [Physlib/Mathematics/Calculus/Wirtinger/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean): 37 declarations, 37 with a docstring, 2 listed as significant; 8 private, not shown.

## Notation

> * The differentiation direction is a *subscript*: `∂_v f` and `∂̄_v f` are the holomorphic and
>   anti-holomorphic Wirtinger derivatives of `f` in direction `v`, splitting the total real
>   derivative `d_v f` (straight `d` for the total, `∂`/`∂̄` for the parts). For iterated
>   derivatives (§I) the operators compose, `∂_v ∂̄_w f`.
> * A `/∂` fraction differentiates with respect to a *variable*, not a direction: a real
>   coordinate `∂f/∂x`, or the argument of a one-variable function in the chain rule, `∂g/∂f`,
>   `∂g/∂f̄` (outer `g : ℂ → ℂ`, inner `f : V → ℂ`).
> * `f̄` is the pointwise conjugate `p ↦ conj (f p)`.
>
> * `v`, `w` are directions in `V`.
> * `u : V` is the *fixed* base point a derivative is evaluated at — the implicit point in the
>   subscript notation.
> * `p : V` is the *bound* base-point variable when a derivative is repackaged as a function of
>   position: the inner field of an iterated operator (`fun p => dWirtingerAntiDir f w p`, §I),
>   or the composite in the chain rule (`fun p => g (f p)`, §D).
>
> Base points (`u`, `p`) and directions (`v`, `w`) all live in `V`: a vector space is its own
> tangent space, so a displacement from a point is again an element of `V` (`u + t·v`).

## i. Overview

> This module is the **foundation** of physlib's Wirtinger calculus. It defines the
> **directional Wirtinger derivatives** of `f : V → ℂ` on a complex vector space `V`, along a
> direction `v : V` (a complex number when `V = ℂ`, a vector in general):
>
>   `∂_v f  = (1/2)(d_v f − i·d_{i·v} f)`     (`dWirtingerDir`)
>   `∂̄_v f = (1/2)(d_v f + i·d_{i·v} f)`     (`dWirtingerAntiDir`)
>
> Here `d_v f = fderiv ℝ f u v` is the real Fréchet derivative along `v`, the limit
> `lim_{t→0} (f(u + t·v) − f(u)) / t` over real `t`; so "real" names the scalar `t`, not the
> direction `v`, and over all `v` these limits form the `ℝ`-linear map `fderiv ℝ f u : V → ℂ`.
> The second direction `i·v` is `v` turned 90° by the complex structure on `V`, so `(v, i·v)`
> is an orthogonal frame in `v`'s own (arbitrary) direction, a rotated and rescaled copy of the
> axes `(1, i)`. For `V = ℂ` one may take `v = 1`, giving `d_v f = ∂f/∂x` and
> `d_{i·v} f = ∂f/∂y`; writing `z = x + i y` and `z̄ = x − i y`, the formulas recover the
> classical `∂f/∂z = (1/2)(∂_x − i ∂_y)f` and `∂f/∂z̄ = (1/2)(∂_x + i ∂_y)f`.
>
> The two operators measure the failure of `ℂ`-linearity. The real derivative always commutes
> with real scaling and addition; `ℂ`-linearity asks in addition that it commute with `i`, that
> is `d_{i·v} f = i·d_v f`. The gap `d_{i·v} f − i·d_v f` to that condition is exactly
> `−2i·∂̄_v f`, so `∂̄_v f` is the obstruction to `ℂ`-linearity and vanishes precisely when `f`
> is holomorphic. Equivalently, the operators split the real derivative into its holomorphic and
> anti-holomorphic parts, the directional form of the Dolbeault decomposition `d = ∂ + ∂̄`,
> which sum back to
>
>   `d_v f = ∂_v f + ∂̄_v f`.
>
> This is the coordinate-free form of treating `z` and `z̄` as independent (the `V = ℂ` case
> above). When `f` is holomorphic the anti-holomorphic half vanishes and `∂_v f` is the ordinary
> complex derivative (§F). Everything rests on `fderiv ℝ`, with no lower Wirtinger layer.
>
> On these operators the module builds the **full directional calculus**:
>
> * real-linearity, the Leibniz rule, and the finite-sum rule (§B);
> * the inner-field conjugation lemmas, swapping the two operators (§C);
> * the two-term Wirtinger chain rule for an outer `g : ℂ → ℂ` (§D);
> * domain conjugation: precomposing with a conjugate-linear map swaps the two
>   operators (§E);
> * the holomorphic / anti-holomorphic collapse, keyed on `ℂ`-linearity or
>   conjugate-linearity of the real derivative along `v` (§F);
> * differentiability and locality of the operators on a `C²` field (§H).
>
> The capstone (§I) is **Schwarz's theorem** in Wirtinger form. On a `C²` field the
> holomorphic and anti-holomorphic derivatives in any two directions commute:
>
>   `∂_v ∂̄_w f = ∂̄_w ∂_v f`     (`dWirtingerDir_dWirtingerAntiDir_comm`)
>
> It is no new analytic fact: it reduces to the symmetry of the second real Fréchet
> derivative (`ContDiffAt.isSymmSndFDerivAt`), carried out via the `weightedDirDeriv` bridge
> of §G.

## ii. Key results

> - `Physlib.Wirtinger.dWirtingerDir` / `dWirtingerAntiDir` : directional Wirtinger
>     derivatives of `f : V → ℂ` along `v`.
> - `Physlib.Wirtinger.dWirtingerDir_add` / `dWirtingerDir_smul` /
>     `dWirtingerDir_mul` / `dWirtingerDir_fun_sum` : real-linearity, the Leibniz
>     rule, and the finite-sum rule (each with an anti-holomorphic dual).
> - `Physlib.Wirtinger.dWirtingerDir_star_comp` / `dWirtingerAntiDir_star_comp` :
>     conjugating the inner field swaps the holomorphic and anti-holomorphic operators.
> - `Physlib.Wirtinger.dWirtingerDir_comp` / `dWirtingerAntiDir_comp` : the two-term
>     Wirtinger chain rule for an outer `g : ℂ → ℂ`.
> - `Physlib.Wirtinger.dWirtingerDir_comp_conjLinear` /
>     `dWirtingerAntiDir_comp_conjLinear` : precomposing with a conjugate-`ℂ`-linear
>     map swaps the two operators (with the base point and direction transported
>     through the map).
> - `Physlib.Wirtinger.dWirtingerDir_eq_of_clinear` /
>     `dWirtingerAntiDir_eq_zero_of_clinear` : the holomorphic collapse, keyed on
>     `ℂ`-linearity of the real derivative along the direction (each with a
>     conjugate-`ℂ`-linear dual).
> - `Physlib.Wirtinger.clinear_of_dWirtingerAntiDir_eq_zero` : `∂̄_v f = 0` implies
>     `d_{i·v} f = i·d_v f`, the converse of `dWirtingerAntiDir_eq_zero_of_clinear`.
> - `Physlib.Wirtinger.differentiableAt_complex_iff_dWirtingerAntiDir_eq_zero` : the
>     Cauchy–Riemann criterion.
> - `Physlib.Wirtinger.differentiableAt_dWirtingerDir` /
>     `differentiableAt_dWirtingerAntiDir` : the directional derivative of a `C²`
>     field is itself real-differentiable.
> - `Physlib.Wirtinger.dWirtingerDir_congr_of_eventuallyEq` /
>     `dWirtingerAntiDir_congr_of_eventuallyEq` : the directional derivative depends
>     only on the field near the point.
> - `Physlib.Wirtinger.dWirtingerDir_dWirtingerAntiDir_comm` : Schwarz's theorem,
>     `∂_v ∂̄_w f = ∂̄_w ∂_v f` for a `C²` `f`.
> - `Physlib.Wirtinger.realLinear_apply_eq_wirtinger` : the real-linear Wirtinger split
>     `L w = a·w + b·star w` of any `L : ℂ →L[ℝ] ℂ`, the algebraic input to the chain rule (§D).
> - `Physlib.Wirtinger.fderiv_star_eq` : the real derivative of a pointwise conjugate
>     `p ↦ star (f p)` is `conjCLE` composed with `fderiv ℝ f`, the analytic input to the
>     conjugation lemmas (§C).

## iv. References

> * Kreutz-Delgado, The Complex Gradient Operator and the CR-Calculus, arXiv:0906.4835 —
>   directional/multivariable formulation and two-term chain rule (§D); second-order theory behind
>   §G–I. [ref: kreutz\_delgado\_cr\_calculus]
> * Mortini & Rupp, The Clairaut–Schwarz Theorem for Mixed Wirtinger Derivatives, Bull. Iranian
>   Math. Soc. 48 (2022), 2643–2647 — the mixed holomorphic/anti-holomorphic symmetry of §I under the
>   same `C²` hypothesis, with the same reduction to real Schwarz used here. [ref: mortini\_rupp\_2022]
> * Koor, Qiu, Kwek & Rebentrost, A short tutorial on Wirtinger Calculus with applications in quantum
>   information, arXiv:2312.04858 — companion exposition of the scalar single/multivariable calculus
>   and sign conventions. [ref: koor\_et\_al\_2023\_wirtinger]
> * Complex differential form, Wikipedia (section "The Dolbeault operators") — the `d = ∂ + ∂̄`
>   splitting and the `∂`/`∂̄` notation this module's operators are named after.
>   [ref: wiki\_complex\_differential\_form]

## A. The directional Wirtinger operators

> The two directional operators repackage the real Fréchet derivative of `f` along
> `v` and `i·v` into a holomorphic part `∂_v f` and an anti-holomorphic part `∂̄_v f`,
> the combinations `(1/2)(d_v f ∓ i·d_{i·v} f)`. Both share one shape, `weightedDirDeriv`,
> the base-point field `p ↦ (1/2)(d_{b₁} f + c·d_{b₂} f)`, and are its two specializations
> at `c = ∓i`, `(b₁, b₂) = (v, i·v)`. Defining the operators through it makes their second
> derivative — the engine of Schwarz's theorem (§G, §I) — a single bridge lemma. Both are
> `ℂ`-valued and depend on the base point `u`.

**`Physlib.Wirtinger.weightedDirDeriv`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L181).

> The base-point field `p ↦ (1/2)(d_{b₁} f + c·d_{b₂} f)`, a weighted combination of the
> real Fréchet derivative of `f` along two directions `b₁`, `b₂`. The directional Wirtinger
> operators are its two specializations: `dWirtingerDir f v` at `c = -i`, `(b₁, b₂) = (v, i·v)`,
> and `dWirtingerAntiDir f v` at `c = i`. Keeping `b₁`, `b₂` free lets §G differentiate it a
> second time once and reuse the bridge for both operators.

```lean
def weightedDirDeriv (f : V → ℂ) (c : ℂ) (b₁ b₂ : V) : V → ℂ
```

**`Physlib.Wirtinger.dWirtingerDir`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L186).

> The holomorphic directional Wirtinger derivative `∂_v f = (1/2)(d_v f − i·d_{i·v} f)`
> of `f : V → ℂ` along the direction vector `v : V`, the `weightedDirDeriv` at `c = -i`.

```lean
def dWirtingerDir (f : V → ℂ) (v u : V) : ℂ
```

**`Physlib.Wirtinger.dWirtingerAntiDir`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L192).

> The anti-holomorphic directional Wirtinger derivative
> `∂̄_v f = (1/2)(d_v f + i·d_{i·v} f)` of `f : V → ℂ` along the direction vector `v : V`,
> the `weightedDirDeriv` at `c = i`.

```lean
def dWirtingerAntiDir (f : V → ℂ) (v u : V) : ℂ
```

**`Physlib.Wirtinger.dWirtingerDir_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L197).

> Definitional unfolding of `dWirtingerDir` to the explicit Wirtinger combination, used to
> expand the outer operator of a composition without touching the inner one.

```lean
lemma dWirtingerDir_apply (g : V → ℂ) (v u : V) :
    dWirtingerDir g v u
      = (1 / 2 : ℂ) * (fderiv ℝ g u v - Complex.I * fderiv ℝ g u (Complex.I • v))
```

**`Physlib.Wirtinger.dWirtingerAntiDir_apply`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L203).

> Definitional unfolding of `dWirtingerAntiDir` to the explicit Wirtinger combination.

```lean
lemma dWirtingerAntiDir_apply (g : V → ℂ) (v u : V) :
    dWirtingerAntiDir g v u
      = (1 / 2 : ℂ) * (fderiv ℝ g u v + Complex.I * fderiv ℝ g u (Complex.I • v))
```

## B. Real-linearity and the Leibniz rule

> The directional operators are built from `fderiv ℝ`, so they inherit its
> vanishing on constants, additivity, negation, complex-scalar compatibility, the
> finite-sum rule, and — through the Fréchet product rule — a Wirtinger Leibniz
> rule.

**`Physlib.Wirtinger.dWirtingerDir_const`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L220).

> Constants have zero holomorphic directional Wirtinger derivative, `∂_v c = 0`.

```lean
lemma dWirtingerDir_const (c : ℂ) (v u : V) :
    dWirtingerDir (fun _ : V => c) v u = 0
```

**`Physlib.Wirtinger.dWirtingerAntiDir_const`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L224).

> Constants have zero anti-holomorphic directional Wirtinger derivative, `∂̄_v c = 0`.

```lean
lemma dWirtingerAntiDir_const (c : ℂ) (v u : V) :
    dWirtingerAntiDir (fun _ : V => c) v u = 0
```

**`Physlib.Wirtinger.dWirtingerDir_neg`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L230).

> `dWirtingerDir` of a negated function, `∂_v(−g) = −∂_v g`. Holds with no
> differentiability hypothesis, since `fderiv` of a negation is unconditional.

```lean
lemma dWirtingerDir_neg (g : V → ℂ) (v u : V) :
    dWirtingerDir (fun p => -(g p)) v u = -(dWirtingerDir g v u)
```

**`Physlib.Wirtinger.dWirtingerAntiDir_neg`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L236).

> `dWirtingerAntiDir` of a negated function, `∂̄_v(−g) = −∂̄_v g`.

```lean
lemma dWirtingerAntiDir_neg (g : V → ℂ) (v u : V) :
    dWirtingerAntiDir (fun p => -(g p)) v u = -(dWirtingerAntiDir g v u)
```

**`Physlib.Wirtinger.dWirtingerDir_add`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L242).

> Additivity of `dWirtingerDir`, `∂_v(g + h) = ∂_v g + ∂_v h`.

```lean
lemma dWirtingerDir_add {g h : V → ℂ} (hg : DifferentiableAt ℝ g u)
    (hh : DifferentiableAt ℝ h u) (v : V) :
    dWirtingerDir (g + h) v u = dWirtingerDir g v u + dWirtingerDir h v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_add`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L249).

> Additivity of `dWirtingerAntiDir`, `∂̄_v(g + h) = ∂̄_v g + ∂̄_v h`.

```lean
lemma dWirtingerAntiDir_add {g h : V → ℂ} (hg : DifferentiableAt ℝ g u)
    (hh : DifferentiableAt ℝ h u) (v : V) :
    dWirtingerAntiDir (g + h) v u = dWirtingerAntiDir g v u + dWirtingerAntiDir h v u
```

**`Physlib.Wirtinger.dWirtingerDir_smul`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L257).

> Compatibility of `dWirtingerDir` with complex scalar multiplication,
> `∂_v(c·g) = c·∂_v g`.

```lean
lemma dWirtingerDir_smul (c : ℂ) {g : V → ℂ} (hg : DifferentiableAt ℝ g u) (v : V) :
    dWirtingerDir (c • g) v u = c • dWirtingerDir g v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_smul`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L264).

> Compatibility of `dWirtingerAntiDir` with complex scalar multiplication,
> `∂̄_v(c·g) = c·∂̄_v g`.

```lean
lemma dWirtingerAntiDir_smul (c : ℂ) {g : V → ℂ} (hg : DifferentiableAt ℝ g u) (v : V) :
    dWirtingerAntiDir (c • g) v u = c • dWirtingerAntiDir g v u
```

**`Physlib.Wirtinger.dWirtingerDir_mul`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L278).

> The Wirtinger Leibniz rule for `dWirtingerDir`,
> `∂_v(g·h) = ∂_v g·h + g·∂_v h`.

```lean
lemma dWirtingerDir_mul {g h : V → ℂ} (hg : DifferentiableAt ℝ g u)
    (hh : DifferentiableAt ℝ h u) (v : V) :
    dWirtingerDir (g * h) v u = dWirtingerDir g v u * h u + g u * dWirtingerDir h v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_mul`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L285).

> The Wirtinger Leibniz rule for `dWirtingerAntiDir`,
> `∂̄_v(g·h) = ∂̄_v g·h + g·∂̄_v h`.

```lean
lemma dWirtingerAntiDir_mul {g h : V → ℂ} (hg : DifferentiableAt ℝ g u)
    (hh : DifferentiableAt ℝ h u) (v : V) :
    dWirtingerAntiDir (g * h) v u =
      dWirtingerAntiDir g v u * h u + g u * dWirtingerAntiDir h v u
```

**`Physlib.Wirtinger.dWirtingerDir_fun_sum`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L292).

> Finite-sum rule for `dWirtingerDir`, `∂_v(∑ₐ Fₐ) = ∑ₐ ∂_v Fₐ`.

```lean
lemma dWirtingerDir_fun_sum {α : Type*} {s : Finset α} {F : α → V → ℂ}
    (hF : ∀ a ∈ s, DifferentiableAt ℝ (F a) u) (v : V) :
    dWirtingerDir (fun p => ∑ a ∈ s, F a p) v u = ∑ a ∈ s, dWirtingerDir (F a) v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_fun_sum`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L299).

> Finite-sum rule for `dWirtingerAntiDir`, `∂̄_v(∑ₐ Fₐ) = ∑ₐ ∂̄_v Fₐ`.

```lean
lemma dWirtingerAntiDir_fun_sum {α : Type*} {s : Finset α} {F : α → V → ℂ}
    (hF : ∀ a ∈ s, DifferentiableAt ℝ (F a) u) (v : V) :
    dWirtingerAntiDir (fun p => ∑ a ∈ s, F a p) v u = ∑ a ∈ s, dWirtingerAntiDir (F a) v u
```

## C. Conjugation

> Conjugating the inner field `f` swaps the two operators, up to an outer conjugation on the
> value (`fderiv_star_eq`):
>
>   `∂_v f̄ = conj (∂̄_v f)`,     `∂̄_v f̄ = conj (∂_v f)`.
>
> Each operator applied to the conjugate field `f̄` returns the *other* operator on `f`,
> conjugated — the bar exchanges holomorphic and anti-holomorphic dependence. Concretely, on
> `V = ℂ` take the holomorphic `f(z) = z`, with `∂_z z = 1`, `∂̄_z z = 0`:
>
> * `∂_v f̄ = conj (∂̄_v f)` reads `∂_z z̄ = conj 0 = 0` — the conjugate `z̄` has no
>   holomorphic part;
> * the dual `∂̄_v f̄ = conj (∂_v f)` reads `∂̄_z z̄ = conj 1 = 1` — all of `z̄`'s dependence
>   sits in the anti-holomorphic operator.
>
> The chain rule of §D builds on these to handle a conjugated inner argument.

**`Physlib.Wirtinger.fderiv_star_eq`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L338).

> Differentiation commutes with conjugation: the real Fréchet derivative of the
> pointwise conjugate `p ↦ star (f p)` is `conjCLE` (conjugation on `ℂ`) composed with
> `fderiv ℝ f u`; in physicists' notation, `d f̄ = conj(d f)`. Conjugation is `ℝ`-linear,
> so it slides through the real derivative unchanged, whereas it does *not* commute with
> the holomorphic Wirtinger derivative `∂_v`. The `star` conjugates the *output* `f p`,
> so this is not a derivative in a conjugate variable.
>
> This is the analytic core of the conjugation lemmas below
> (`dWirtingerDir_star_comp` and its dual): distributed over the Wirtinger split of
> `fderiv ℝ f u` (`realLinear_apply_eq_wirtinger`, §D), the outer `conjCLE` conjugates the two
> coefficients and swaps the holomorphic and anti-holomorphic parts.

```lean
lemma fderiv_star_eq {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {f : E → ℂ} {u : E} (hf : DifferentiableAt ℝ f u) :
    fderiv ℝ (fun p : E => star (f p)) u =
      Complex.conjCLE.toContinuousLinearMap.comp (fderiv ℝ f u)
```

**`Physlib.Wirtinger.dWirtingerDir_star_comp`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L346).

> Conjugating the function swaps the operators up to an outer conjugation:
> `∂_v f̄ = conj (∂̄_v f)`.

```lean
lemma dWirtingerDir_star_comp (hf : DifferentiableAt ℝ f u) (v : V) :
    dWirtingerDir (fun p => star (f p)) v u = star (dWirtingerAntiDir f v u)
```

**`Physlib.Wirtinger.dWirtingerAntiDir_star_comp`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L357).

> Conjugating the function swaps the operators up to an outer conjugation:
> `∂̄_v f̄ = conj (∂_v f)`. Dual of `dWirtingerDir_star_comp`.

```lean
lemma dWirtingerAntiDir_star_comp (hf : DifferentiableAt ℝ f u) (v : V) :
    dWirtingerAntiDir (fun p => star (f p)) v u = star (dWirtingerDir f v u)
```

## D. The Wirtinger chain rule

> Composing with an outer `g : ℂ → ℂ` gives a **two-term** chain rule:
>
>   `∂_v(g∘f) = (∂g/∂f)·∂_v f + (∂g/∂f̄)·∂_v f̄`.
>
> A non-holomorphic `g` depends on both its argument and its conjugate, so both channels
> contribute: the holomorphic `∂g/∂f` and the anti-holomorphic `∂g/∂f̄`, each times the
> matching inner derivative — two terms where the complex-analytic rule has one. The two
> coefficients come from `realLinear_apply_eq_wirtinger`: every `ℝ`-linear `L : ℂ → ℂ`
> splits as `L w = a·w + b·conj w`, and on the outer real derivative `L = fderiv ℝ g (f u)`
> that gives `a = ∂g/∂f`, `b = ∂g/∂f̄`. The proof applies this split to the outer factor and
> reuses the §C conjugation lemmas for the `∂_v f̄` term.

**`Physlib.Wirtinger.realLinear_apply_eq_wirtinger`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L394).

> Split a real-linear map `ℂ → ℂ` into its Wirtinger components. Any
> real-linear `L : ℂ →L[ℝ] ℂ` splits into a holomorphic and an anti-holomorphic part
> with the Wirtinger coefficients `a = ½(L 1 - i * L i)`, `b = ½(L 1 + i * L i)` as
> weights:
>
>   `L w = a * w + b * star w`.
>
> This is purely algebraic: `L` is an arbitrary real-linear map, no derivative
> involved. Its use is the Wirtinger chain rule (`dWirtingerDir_comp` below), where the
> weights of the outer differential `L = fderiv ℝ g (f u)` are the coefficients `∂g/∂f`,
> `∂g/∂f̄`.

```lean
lemma realLinear_apply_eq_wirtinger (L : ℂ →L[ℝ] ℂ) (w : ℂ) :
    L w =
      ((1 / 2 : ℂ) * (L 1 - Complex.I * L Complex.I)) * w
        + ((1 / 2 : ℂ) * (L 1 + Complex.I * L Complex.I)) * star w
```

**`Physlib.Wirtinger.dWirtingerDir_comp`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L411).

> The two-term Wirtinger chain rule for `dWirtingerDir`, outer `g : ℂ → ℂ` and inner
> `f : V → ℂ`:
>
>   `∂_v(g∘f) = (∂g/∂f)·∂_v f + (∂g/∂f̄)·∂_v f̄`.
>
> `realLinear_apply_eq_wirtinger` splits the chain rule's outer `ℝ`-linear factor into the
> `∂g/∂f`, `∂g/∂f̄` coefficients, each multiplying its inner directional derivative `∂_v f`,
> `∂_v f̄`.

```lean
lemma dWirtingerDir_comp {g : ℂ → ℂ} (hg : DifferentiableAt ℝ g (f u))
    (hf : DifferentiableAt ℝ f u) (v : V) :
    dWirtingerDir (fun p => g (f p)) v u =
      dWirtingerDir g 1 (f u) * dWirtingerDir f v u
        + dWirtingerAntiDir g 1 (f u) * dWirtingerDir (fun p => star (f p)) v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_comp`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L431).

> The two-term Wirtinger chain rule for `dWirtingerAntiDir`, the anti-holomorphic dual of
> `dWirtingerDir_comp`:
>
>   `∂̄_v(g∘f) = (∂g/∂f)·∂̄_v f + (∂g/∂f̄)·∂̄_v f̄`.
>
> Same outer `∂g/∂f`, `∂g/∂f̄` coefficients, now each multiplying its anti-holomorphic inner
> derivative `∂̄_v f`, `∂̄_v f̄`; same proof as `dWirtingerDir_comp`.

```lean
lemma dWirtingerAntiDir_comp {g : ℂ → ℂ} (hg : DifferentiableAt ℝ g (f u))
    (hf : DifferentiableAt ℝ f u) (v : V) :
    dWirtingerAntiDir (fun p => g (f p)) v u =
      dWirtingerDir g 1 (f u) * dWirtingerAntiDir f v u
        + dWirtingerAntiDir g 1 (f u) * dWirtingerAntiDir (fun p => star (f p)) v u
```

## E. Domain conjugation

> The goal is to differentiate anti-holomorphic functions: a holomorphic `g` precomposed with
> conjugation of its input (the scalar case is `g(z̄)`, but the input is a general vector). So
> this section conjugates a function's *input*: precomposing `g` with a domain map
> `L : V → V'` (forming `g ∘ L`) swaps the two operators, whereas §C conjugated the output.
> The map `L` is **conjugate-`ℂ`-linear**: real-linear and continuous, but anti-commuting with
> `i`:
>
>   `L (i · x) = −(i · L x)`,
>
> the abstract form of `conj (i·x) = −i · conj x`. That sign flip swaps the two operators: in
> the holomorphic combination `(1/2)(d_v f − i·d_{i·v} f)` the `d_{i·v} f` term picks up the
> minus from `L`, turning it anti-holomorphic. So precomposition `g ∘ L` swaps `∂ ↔ ∂̄`, with
> `g`'s derivative taken at the mapped point `L u` in the mapped direction `L v`:
>
>   `∂_v(g ∘ L)`  at `u`  =  `∂̄_{L v} g`  at `L u`
>   `∂̄_v(g ∘ L)`  at `u`  =  `∂_{L v} g`  at `L u`
>
> (`dWirtingerDir_comp_conjLinear` and its dual `dWirtingerAntiDir_comp_conjLinear`).
>
> Concretely on `ℂ`, let `L : z ↦ z̄` and `g(z) = log(z)`, so `g ∘ L` is `z ↦ log(z̄)`. The
> theorem computes this composite's derivatives from the known derivative of `log`, swapping
> the operator. Its anti-holomorphic derivative is `log`'s ordinary derivative `1/z` at the
> mapped point `z̄`:
>
>   `∂̄_z log(z̄) = 1/z̄`,
>
> while its holomorphic derivative vanishes, `∂_z log(z̄) = 0`, because `log` is holomorphic.
> So `log(z̄)` is purely anti-holomorphic, with its dependence carried by `∂̄`.
>
> So precomposing with conjugation turns `∂` into `∂̄` and vice versa: a holomorphic `g(z̄)`
> has zero holomorphic derivative, and its anti-holomorphic derivative is just `g`'s ordinary
> complex derivative (§F, and the example above). The proof uses only `L`'s anti-commutation
> with `i`, so it holds over any complex `V`, `V'`.

**`Physlib.Wirtinger.fderiv_comp_clm_apply`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L492).

> Chain rule for an inner continuous linear map `L`. Because the derivative of a linear
> map is the map itself, the real Fréchet derivative of `g ∘ L` at `u`, applied to `x`, equals
> the derivative of `g` at `L u` applied to `L x`.

```lean
lemma fderiv_comp_clm_apply {g : V' → ℂ} {L : V →L[ℝ] V'} {u : V}
    (hg : DifferentiableAt ℝ g (L u)) (x : V) :
    fderiv ℝ (fun p => g (L p)) u x = fderiv ℝ g (L u) (L x)
```

**`Physlib.Wirtinger.dWirtingerDir_comp_conjLinear`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L501).

> Domain conjugation swaps the operators: precomposing with a conjugate-`ℂ`-linear `L`
> turns the holomorphic derivative of `g ∘ L` at `u` into the anti-holomorphic derivative of
> `g` at the mapped point `L u`, in the mapped direction `L v`:
> `∂_v(g ∘ L)` at `u` equals `∂̄_{L v} g` at `L u`.

```lean
lemma dWirtingerDir_comp_conjLinear {g : V' → ℂ} {L : V →L[ℝ] V'} {u : V}
    (hL : ∀ x : V, L (Complex.I • x) = -(Complex.I • L x))
    (hg : DifferentiableAt ℝ g (L u)) (v : V) :
    dWirtingerDir (fun p => g (L p)) v u = dWirtingerAntiDir g (L v) (L u)
```

**`Physlib.Wirtinger.dWirtingerAntiDir_comp_conjLinear`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L512).

> Dual of `dWirtingerDir_comp_conjLinear`: the anti-holomorphic derivative of `g ∘ L` at
> `u` is the holomorphic derivative of `g` at the mapped point `L u`, in the mapped direction
> `L v`: `∂̄_v(g ∘ L)` at `u` equals `∂_{L v} g` at `L u`.

```lean
lemma dWirtingerAntiDir_comp_conjLinear {g : V' → ℂ} {L : V →L[ℝ] V'} {u : V}
    (hL : ∀ x : V, L (Complex.I • x) = -(Complex.I • L x))
    (hg : DifferentiableAt ℝ g (L u)) (v : V) :
    dWirtingerAntiDir (fun p => g (L p)) v u = dWirtingerDir g (L v) (L u)
```

## F. The holomorphic collapse

> The two-operator split collapses to one exactly when `f` is holomorphic along `v`, i.e. its
> real derivative is `ℂ`-linear there (`d_{i·v} f = i·d_v f`, the Cauchy–Riemann condition):
> then `∂_v f` is the full real derivative `d_v f` and `∂̄_v f` vanishes. Dually, a
> conjugate-`ℂ`-linear derivative makes `∂_v f` vanish and `∂̄_v f` the full derivative.
>
> The lemmas take this `ℂ`-linearity condition directly as hypothesis, not holomorphy itself.
> The reason is a clean division of labor.
>
> **The domain-general collapse.** Given the identity `d_{i·v} f = i·d_v f`, the collapse is pure
> algebra: unfold `∂_v f = (1/2)(d_v f − i·d_{i·v} f)`, substitute the identity, and `∂_v f`
> reduces to `d_v f` while `∂̄_v f` cancels to `0`. No property of the domain `V` enters, so a
> single proof covers every complex `V`.
>
> **The bridge.** Holomorphy is stated through `fderiv ℂ`, the identity `d_{i·v} f = i·d_v f`
> through `fderiv ℝ`. The Cauchy–Riemann criterion
> `differentiableAt_complex_iff_dWirtingerAntiDir_eq_zero` relates them.

**`Physlib.Wirtinger.dWirtingerDir_eq_of_clinear`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L547).

> Holomorphic collapse: along a direction where the real derivative is `ℂ`-linear, the
> holomorphic derivative is the full real derivative, `∂_v f = d_v f`.

```lean
lemma dWirtingerDir_eq_of_clinear {v : V}
    (h : fderiv ℝ f u (Complex.I • v) = Complex.I • fderiv ℝ f u v) :
    dWirtingerDir f v u = fderiv ℝ f u v
```

**`Physlib.Wirtinger.dWirtingerAntiDir_eq_zero_of_clinear`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L555).

> Holomorphic collapse: the anti-holomorphic derivative vanishes along a direction
> of `ℂ`-linearity, `∂̄_v f = 0`.

```lean
lemma dWirtingerAntiDir_eq_zero_of_clinear {v : V}
    (h : fderiv ℝ f u (Complex.I • v) = Complex.I • fderiv ℝ f u v) :
    dWirtingerAntiDir f v u = 0
```

**`Physlib.Wirtinger.dWirtingerDir_eq_zero_of_antilinear`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L563).

> Anti-holomorphic collapse: a direction of conjugate-`ℂ`-linearity kills the
> holomorphic derivative, `∂_v f = 0`.

```lean
lemma dWirtingerDir_eq_zero_of_antilinear {v : V}
    (h : fderiv ℝ f u (Complex.I • v) = -(Complex.I • fderiv ℝ f u v)) :
    dWirtingerDir f v u = 0
```

**`Physlib.Wirtinger.dWirtingerAntiDir_eq_of_antilinear`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L571).

> Anti-holomorphic collapse: the anti-holomorphic derivative is the full real
> derivative along a direction of conjugate-`ℂ`-linearity, `∂̄_v f = d_v f`.

```lean
lemma dWirtingerAntiDir_eq_of_antilinear {v : V}
    (h : fderiv ℝ f u (Complex.I • v) = -(Complex.I • fderiv ℝ f u v)) :
    dWirtingerAntiDir f v u = fderiv ℝ f u v
```

**`Physlib.Wirtinger.clinear_of_dWirtingerAntiDir_eq_zero`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L578).

> The converse of `dWirtingerAntiDir_eq_zero_of_clinear`. It needs no differentiability.

```lean
lemma clinear_of_dWirtingerAntiDir_eq_zero {v : V} (h : dWirtingerAntiDir f v u = 0) :
    fderiv ℝ f u (Complex.I • v) = Complex.I • fderiv ℝ f u v
```

**`Physlib.Wirtinger.differentiableAt_complex_iff_dWirtingerAntiDir_eq_zero`**, a theorem, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L593). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Cauchy–Riemann.** `f` is `ℂ`-differentiable at `u` iff it is real-differentiable there and
> every anti-holomorphic Wirtinger derivative vanishes. Real differentiability is needed: `fderiv`
> is `0` where `f` is not differentiable.

```lean
theorem differentiableAt_complex_iff_dWirtingerAntiDir_eq_zero (f : V → ℂ) (u : V) :
    DifferentiableAt ℂ f u ↔
      DifferentiableAt ℝ f u ∧ ∀ v, dWirtingerAntiDir f v u = 0
```

## G. The second-derivative bridge

> Schwarz's theorem (§I) commutes two Wirtinger operators, so it differentiates a directional
> Wirtinger derivative a *second* time. This section bridges that second derivative to the
> second real Fréchet derivative `fderiv ℝ (fderiv ℝ f) u`, where mixed partials are already
> symmetric.
>
> Each directional operator is, definitionally, a combination `(1/2)(d_{b₁} f + c·d_{b₂} f)` of
> the real derivative along two directions (`c = −i` holomorphic with `b₂ = i·b₁`, `c = +i`
> anti-holomorphic). `weightedDirDeriv` records this as a function of the base point, with
> `b₁`, `b₂` left free: the directions stay fixed while the point `p` varies, turning the
> one-point derivative into a field `V → ℂ` that can itself be differentiated. Differentiating
> it once more sends each first derivative to `fderiv ℝ (fderiv ℝ f) u` on two slots.
>
> The two inner directions `b₁`, `b₂` are intrinsic: they are the pair a Wirtinger derivative
> already combines (`v` and `i·v`). The second differentiation, by contrast, is an ordinary
> Fréchet derivative along one new direction `a`, so the bridge lands directly on the plain
> second derivative `fderiv ℝ (fderiv ℝ f) u` in the outer slot `a` and inner slot `b₁`/`b₂`,
> whose slot symmetry (`ContDiffAt.isSymmSndFDerivAt`) drives Schwarz. The *outer* Wirtinger
> combination is rebuilt afterward by instantiating `a` at `v` and `i·v`.
>
> Because `weightedDirDeriv` and its bridge `fderiv_weightedDirDeriv` are generic in `c`, `b₁`,
> `b₂`, one lemma serves every second-order pairing. The four combinations (holomorphic or
> anti-holomorphic, twice) differ only in their coefficients and all reduce to
> `fderiv ℝ (fderiv ℝ f) u` on the directions `v`, `i·v`, `w`, `i·w`. §I discharges the mixed
> pairing that Kähler geometry needs; the others follow from the same bridge with a different
> `(c, b₁, b₂)`, then `ContDiffAt.isSymmSndFDerivAt` and `ring`.
>
> The operators are already `weightedDirDeriv` by definition (§A); this section differentiates
> that shared field a second time.
>
> **Structure.**
>
> * `hasFDerivAt_fderiv_apply`, `hasFDerivAt_weightedDirDeriv` : the evaluation field
>   `p ↦ d_b f`, and hence `weightedDirDeriv`, is differentiable wherever `fderiv ℝ f` is.
> * `fderiv_weightedDirDeriv` : the bridge, sending a derivative of `weightedDirDeriv` along a
>   direction `a` to the second Fréchet derivative `fderiv ℝ (fderiv ℝ f) u` in the two slots.
> * `dWirtingerDir_eq_weightedDirDeriv`, `dWirtingerAntiDir_eq_weightedDirDeriv` : the operators
>   `∂_v f`, `∂̄_v f` are `weightedDirDeriv` at `(c, b₁, b₂) = (−i, v, i·v)` and `(i, w, i·w)`.
> * `fderiv_dWirtingerDir`, `fderiv_dWirtingerAntiDir` : specialize the bridge, so a second
>   derivative of `∂_v f`, `∂̄_v f` lands on `fderiv ℝ (fderiv ℝ f) u` in the two slots.

## H. Differentiability and locality

> Schwarz (§I) and the coordinate layer treat a directional derivative as a field in the base
> point `p`, and need two regularity facts about it. Both are public packagings of §G, consumed
> in `Coordinate.lean`.
>
> **Differentiability.** On a `C²` field the directional derivative `p ↦ ∂_v f` is itself
> real-differentiable (`differentiableAt_dWirtingerDir`): by §G it is a `weightedDirDeriv`, and
> `fderiv ℝ f` is differentiable for a `C²` `f`. Without this a Wirtinger derivative could not
> be differentiated a second time, as Schwarz (§I) does.
>
> **Locality.** The value `∂_v f` at `u` depends only on how `f` behaves near `u`, inherited
> from `fderiv ℝ f u`: the operator is built from it, and a Fréchet derivative is fixed by `f`
> on an arbitrarily small neighbourhood. So if `f₁` and `f₂` coincide on some neighbourhood of
> `u` (in Lean `f₁ =ᶠ[nhds u] f₂`, where `=ᶠ` is equality on a filter-large set and `[nhds u]`
> is the neighbourhood filter of `u`) they have the same directional derivative at `u`
> (`dWirtingerDir_congr_of_eventuallyEq`). This is what makes the operators usable on functions
> regular only on a restricted domain (the Kähler potentials, defined on a slit domain rather
> than all of `V`): the derivative at `u` needs only `f` near `u`, so a consumer may swap `f`
> for a locally-equal representative and rely on the local `C²`/holomorphy hypotheses
> (`ContDiffAt`, `DifferentiableAt`), which likewise depend only on `f` near `u`: their `...At`
> form asks for regularity only on a neighbourhood of `u`, which a restricted-domain function
> has at each point of its domain.

**`Physlib.Wirtinger.differentiableAt_dWirtingerDir`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L746).

> On a `C²` field the holomorphic directional derivative is itself
> real-differentiable.

```lean
lemma differentiableAt_dWirtingerDir (hf2 : ContDiffAt ℝ 2 f u) (v : V) :
    DifferentiableAt ℝ (fun p => dWirtingerDir f v p) u
```

**`Physlib.Wirtinger.differentiableAt_dWirtingerAntiDir`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L753).

> On a `C²` field the anti-holomorphic directional derivative is itself
> real-differentiable.

```lean
lemma differentiableAt_dWirtingerAntiDir (hf2 : ContDiffAt ℝ 2 f u) (w : V) :
    DifferentiableAt ℝ (fun p => dWirtingerAntiDir f w p) u
```

**`Physlib.Wirtinger.dWirtingerDir_congr_of_eventuallyEq`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L760).

> The holomorphic directional derivative depends only on the field near the point:
> fields agreeing on a neighbourhood have equal derivative.

```lean
lemma dWirtingerDir_congr_of_eventuallyEq {f₁ f₂ : V → ℂ} {u : V}
    (h : f₁ =ᶠ[nhds u] f₂) (v : V) :
    dWirtingerDir f₁ v u = dWirtingerDir f₂ v u
```

**`Physlib.Wirtinger.dWirtingerAntiDir_congr_of_eventuallyEq`**, a lemma, [line 767](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L767).

> The anti-holomorphic directional derivative depends only on the field near the
> point; dual of `dWirtingerDir_congr_of_eventuallyEq`.

```lean
lemma dWirtingerAntiDir_congr_of_eventuallyEq {f₁ f₂ : V → ℂ} {u : V}
    (h : f₁ =ᶠ[nhds u] f₂) (v : V) :
    dWirtingerAntiDir f₁ v u = dWirtingerAntiDir f₂ v u
```

## I. Schwarz's theorem

**`Physlib.Wirtinger.dWirtingerDir_dWirtingerAntiDir_comm`**, a theorem, [line 787](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean#L787). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Schwarz's theorem** for the directional Wirtinger operators: on a `C²` field `f` the
> holomorphic and anti-holomorphic directional derivatives commute in any two directions,
> `∂_v ∂̄_w f = ∂̄_w ∂_v f`.
>
> The commutation adds no analytic input. By the §G bridge each order expands into a real-linear
> combination of the second real Fréchet derivative `fderiv ℝ (fderiv ℝ f) u` on the four
> directions `v`, `i·v`, `w`, `i·w`. The two orders give the same combination up to transposing
> the two slots of that second derivative, and `ContDiffAt.isSymmSndFDerivAt`, the symmetry of
> ordinary mixed second partials, equates them.

```lean
theorem dWirtingerDir_dWirtingerAntiDir_comm (hf2 : ContDiffAt ℝ 2 f u) (v w : V) :
    dWirtingerDir (fun p => dWirtingerAntiDir f w p) v u
      = dWirtingerAntiDir (fun p => dWirtingerDir f v p) w u
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Upgrading a real-linear map to a complex-linear one](../formathlib/complexlinear.md)

## Sources

- [Physlib/Mathematics/Calculus/Wirtinger/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Basic.lean)
