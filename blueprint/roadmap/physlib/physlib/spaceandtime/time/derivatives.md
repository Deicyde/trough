---
declaration: module
origin: cited
lean: Time.deriv, Time.deriv_eq, Time.toRealCLE_symm_one, Time.hasDerivAt_comp_toRealCLE_symm, Time.deriv_comp_toRealCLE_of_hasDerivAt, Time.deriv_eq_of_hasDerivAt, Time.hasDerivAt_mk_of_differentiableAt, Time.manifoldDeriv
statement: formalized
proof: formalized
---

# Time Derivatives

The module `Physlib.SpaceAndTime.Time.Derivatives`, [Physlib/SpaceAndTime/Time/Derivatives.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean): 39 declarations, 19 with a docstring.

## i. Overview

> In this module we define and prove basic lemmas about derivatives of functions on `Time`.

## ii. Key results

> - `deriv` : The derivative of a function `Time → M` at a given time.
> - `manifoldDeriv` : The derivative of a function from `Time` to a manifold.
> - `derivVec` : The derivative of a function from `Time` into a torsor, such as `Space d`,
>   valued in the vector space of displacements of that torsor.
> - `hasDerivAt_comp_toRealCLE_symm` : The time derivative as a `HasDerivAt` on `ℝ`, for a curve
>   reparametrised through the canonical equivalence `toRealCLE.symm : ℝ ≃L[ℝ] Time`.
> - `deriv_comp_toRealCLE_of_hasDerivAt` : Its converse, a `HasDerivAt` on `ℝ` read as the time
>   derivative of the curve pulled back to `Time` through `toRealCLE`.
> - `hasDerivAt_mk_of_differentiableAt` and `deriv_eq_of_hasDerivAt` : The same two bridges for a
>   real-valued curve `f : Time → ℝ`, stated at `t : Time` through the curve `τ ↦ f ⟨τ⟩` on `ℝ`.
> - `deriv_comp_neg` and `deriv_deriv_comp_neg` : The first and second time derivatives under the
>   reversal of time `t ↦ -t`.

## iv. References

> * None.

## A. The definition of the derivative

### A.1. Derivatives of functions into vector spaces

**`Time.deriv`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L74).

> Given a function `f : Time → M` the derivative of `f`.

```lean
noncomputable def deriv [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (f : Time → M) : Time → M
```

**`Time.deriv_eq`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L81).

```lean
lemma deriv_eq [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (f : Time → M) (t : Time) : Time.deriv f t = fderiv ℝ f t 1
```

### A.2. The derivative through the canonical equivalence with `ℝ`

> `Time` is identified with `ℝ` by the continuous linear equivalence `toRealCLE`. Precomposing a
> curve `w : Time → M` with `toRealCLE.symm : ℝ ≃L[ℝ] Time` gives a curve on `ℝ`, whose Mathlib
> derivative (`HasDerivAt`) at `τ` is the time derivative `∂ₜ w` evaluated at `toRealCLE.symm τ`.
> This is the bridge through which Mathlib's calculus and ODE theory on `ℝ` applies to curves on
> `Time`. Conversely, a `HasDerivAt` on `ℝ` at `toRealCLE t` is the time derivative at `t` of the
> curve pulled back to `Time` through `toRealCLE`.

**`Time.toRealCLE_symm_one`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L98).

> The canonical equivalence `toRealCLE.symm : ℝ ≃L[ℝ] Time` sends `1 : ℝ` to `1 : Time`.

```lean
lemma toRealCLE_symm_one : toRealCLE.symm (1 : ℝ) = (1 : Time)
```

**`Time.hasDerivAt_comp_toRealCLE_symm`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L104).

> Bridge from the time derivative to `HasDerivAt`: if `w : Time → M` is differentiable at
> `toRealCLE.symm τ`, then the curve `τ ↦ w (toRealCLE.symm τ)` on `ℝ` has derivative
> `∂ₜ w (toRealCLE.symm τ)` at `τ`.

```lean
lemma hasDerivAt_comp_toRealCLE_symm [NormedAddCommGroup M] [NormedSpace ℝ M]
    (w : Time → M) (τ : ℝ) (hw : DifferentiableAt ℝ w (toRealCLE.symm τ)) :
    HasDerivAt (fun τ : ℝ => w (toRealCLE.symm τ)) (∂ₜ w (toRealCLE.symm τ)) τ
```

**`Time.deriv_comp_toRealCLE_of_hasDerivAt`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L113).

> The converse of the bridge `hasDerivAt_comp_toRealCLE_symm`: if the curve `γ : ℝ → M` has
> derivative `v` at `toRealCLE t`, then the curve `t ↦ γ (toRealCLE t)` on `Time` has time
> derivative `v` at `t`.

```lean
lemma deriv_comp_toRealCLE_of_hasDerivAt [NormedAddCommGroup M] [NormedSpace ℝ M]
    (γ : ℝ → M) (t : Time) (v : M) (h : HasDerivAt γ v (toRealCLE t)) :
    ∂ₜ (fun s => γ (toRealCLE s)) t = v
```

**`Time.deriv_eq_of_hasDerivAt`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L123).

> The time derivative of any `f : Time → ℝ` at `t` is the derivative at `t.val` of the curve
> `τ ↦ f ⟨τ⟩` on `ℝ`.

```lean
lemma deriv_eq_of_hasDerivAt {f : Time → ℝ} {t : Time} {v : ℝ}
    (h : HasDerivAt (fun τ : ℝ => f ⟨τ⟩) v t.val) : ∂ₜ f t = v
```

**`Time.hasDerivAt_mk_of_differentiableAt`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L129).

> A curve `f : Time → ℝ` differentiable at `t` gives the curve `σ ↦ f ⟨σ⟩` on `ℝ`,
> whose Mathlib derivative at `t.val` is the time derivative `∂ₜ f t`.

```lean
lemma hasDerivAt_mk_of_differentiableAt {f : Time → ℝ} {t : Time}
    (hf : DifferentiableAt ℝ f t) :
    HasDerivAt (fun σ : ℝ => f ⟨σ⟩) (∂ₜ f t) t.val
```

### A.3. Derivatives of functions into manifolds

**`Time.manifoldDeriv`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L143).

> The time derivative of a function from `Time` to a manifold, as a tangent vector at
> the value of the function.

```lean
noncomputable def manifoldDeriv {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] (f : Time → N) : (t : Time) → TangentSpace I (f t)
```

**`Time.manifoldDeriv_eq`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L149).

```lean
lemma manifoldDeriv_eq {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] (f : Time → N) (t : Time) :
    manifoldDeriv I f t =
      mfderiv 𝓘(ℝ, Time) I f t ((1 : Time) : TangentSpace 𝓘(ℝ, Time) t)
```

**`Time.deriv_eq_mfderiv`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L157).

> The time derivative is the manifold derivative for functions into normed spaces.

```lean
lemma deriv_eq_mfderiv [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → M) (t : Time) :
    deriv f t =
      mfderiv 𝓘(ℝ, Time) 𝓘(ℝ, M) f t
        ((1 : Time) : TangentSpace 𝓘(ℝ, Time) t)
```

**`Time.deriv_eq_manifoldDeriv`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L166).

```lean
lemma deriv_eq_manifoldDeriv [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → M) (t : Time) :
    deriv f t = manifoldDeriv 𝓘(ℝ, M) f t
```

**`Time.manifoldDeriv_const`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L174).

```lean
lemma manifoldDeriv_const {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] (n : N) :
    manifoldDeriv I (fun _ : Time => n) t = 0
```

### A.4. Derivatives of functions into torsors

> A trajectory in physical space is a curve of points, and its velocity is a displacement per
> unit time, that is a vector. For a torsor `P` over a vector space `V`, for example
> `Space d` over `EuclideanSpace ℝ (Fin d)`, the derivative of a curve `f : Time → P` is
> therefore valued in `V` rather than in `P`. It is defined by differentiating the displacement
> curve `s ↦ f s -ᵥ f t`, which is `V`-valued, so that no origin of `P` is ever chosen. The
> reference point used to form the displacement is irrelevant, see `derivVec_eq_fderiv_vsub`.

**`Time.derivVec`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L196).

> The time derivative of a trajectory into a torsor `P` over a vector space `V`,
> valued in `V`. For a trajectory `f : Time → Space d` this is the velocity, a spatial vector in
> `EuclideanSpace ℝ (Fin d)` rather than a point of `Space d`.

```lean
noncomputable def derivVec {V P : Type} [AddCommGroup V] [Module ℝ V] [TopologicalSpace V]
    [AddTorsor V P] (f : Time → P) : Time → V
```

**`Time.derivVec_eq`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L203).

```lean
lemma derivVec_eq {V P : Type} [AddCommGroup V] [Module ℝ V] [TopologicalSpace V]
    [AddTorsor V P] (f : Time → P) (t : Time) :
    ∂ₜᵥ f t = fderiv ℝ (fun s => f s -ᵥ f t) t 1
```

**`Time.derivVec_eq_fderiv_vsub`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L211).

> The derivative of a trajectory into a torsor does not depend on the reference point used
> to form the displacement: any base point `p` gives the same derivative. The normed hypotheses on
> `V` here come from `fderiv_add_const`; the definition itself needs only a topological vector
> space.

```lean
lemma derivVec_eq_fderiv_vsub {V P : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    [AddTorsor V P] (f : Time → P) (p : P) (t : Time) :
    ∂ₜᵥ f t = fderiv ℝ (fun s => f s -ᵥ p) t 1
```

## B. Linearlity properties of the derivative

**`Time.deriv_smul`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L225).

```lean
lemma deriv_smul (f : Time → EuclideanSpace ℝ (Fin d)) (k : ℝ)
    (hf : Differentiable ℝ f) :
    ∂ₜ (fun t => k • f t) t = k • ∂ₜ (fun t => f t) t
```

**`Time.deriv_neg`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L232).

```lean
lemma deriv_neg [NormedAddCommGroup M] [NormedSpace ℝ M] (f : Time → M) :
    ∂ₜ (-f) t = -∂ₜ f t
```

**`Time.deriv_add`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L237).

```lean
lemma deriv_add [NormedAddCommGroup M] [NormedSpace ℝ M] (f g : Time → M)
    (hf : DifferentiableAt ℝ f t) (hg : DifferentiableAt ℝ g t) :
    ∂ₜ (fun s => f s + g s) t = ∂ₜ f t + ∂ₜ g t
```

**`Time.deriv_fun_sum`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L243).

```lean
lemma deriv_fun_sum {ι : Type*} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (s : Finset ι) (a : ι → Time → M) (ha : ∀ i ∈ s, DifferentiableAt ℝ (a i) t) :
    ∂ₜ (fun x => ∑ i ∈ s, a i x) t = ∑ i ∈ s, ∂ₜ (a i) t
```

**`Time.deriv_mul_const`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L249).

```lean
lemma deriv_mul_const (f : Time → ℝ) (c : ℝ) (hf : DifferentiableAt ℝ f t) :
    ∂ₜ (fun s => f s * c) t = ∂ₜ f t * c
```

**`Time.deriv_div`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L257).

> Quotient rule for `Time.deriv` on real-valued functions: if `c` and `g` are
> differentiable at `t` and `g t ≠ 0`, then
> `∂ₜ (c / g) t = (∂ₜ c t * g t - c t * ∂ₜ g t) / (g t)^2`.

```lean
lemma deriv_div {c g : Time → ℝ}
    (hc : DifferentiableAt ℝ c t) (hg : DifferentiableAt ℝ g t) (hgz : g t ≠ 0) :
    ∂ₜ (fun s => c s / g s) t =
      (∂ₜ c t * g t - c t * ∂ₜ g t) / (g t) ^ 2
```

## C. Derivative of constant functions

**`Time.deriv_const`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L275).

```lean
lemma deriv_const [NormedAddCommGroup M] [NormedSpace ℝ M] (m : M) :
    ∂ₜ (fun _ => m) t = 0
```

**`Time.derivVec_const`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L282).

> A trajectory constant at a point of a torsor has zero derivative.

```lean
lemma derivVec_const {V P : Type} [AddCommGroup V] [Module ℝ V] [TopologicalSpace V]
    [AddTorsor V P] (p : P) :
    ∂ₜᵥ (fun _ => p) t = (0 : V)
```

## D. Smoothness properties and the reversal of time

**`Time.val_contDiff`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L296).

```lean
lemma val_contDiff {n : WithTop ℕ∞} : ContDiff ℝ n Time.val
```

**`Time.deriv_differentiable_of_contDiff`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L301).

```lean
lemma deriv_differentiable_of_contDiff {M : Type}
    [NormedAddCommGroup M] [NormedSpace ℝ M] (f : Time → M) (hf : ContDiff ℝ ∞ f) :
    Differentiable ℝ (∂ₜ f)
```

**`Time.deriv_contDiff_of_contDiff`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L312).

```lean
lemma deriv_contDiff_of_contDiff {M : Type}
    [NormedAddCommGroup M] [NormedSpace ℝ M] (f : Time → M) (hf : ContDiff ℝ ∞ f) :
    ContDiff ℝ ∞ (∂ₜ f)
```

**`Time.deriv_contDiff_of_contDiff_succ`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L321).

> The time derivative of a `C^(n+1)` curve is `C^n`.

```lean
lemma deriv_contDiff_of_contDiff_succ {M : Type} {n : WithTop ℕ∞}
    [NormedAddCommGroup M] [NormedSpace ℝ M] (f : Time → M) (hf : ContDiff ℝ (n + 1) f) :
    ContDiff ℝ n (∂ₜ f)
```

**`Time.deriv_differentiable_of_contDiff_two`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L330).

> The time derivative of a `C²` curve is differentiable.

```lean
lemma deriv_differentiable_of_contDiff_two {M : Type}
    [NormedAddCommGroup M] [NormedSpace ℝ M] (f : Time → M) (hf : ContDiff ℝ 2 f) :
    Differentiable ℝ (∂ₜ f)
```

**`Time.deriv_contDiff_of_space`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L337).

```lean
lemma deriv_contDiff_of_space {n} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → Space d → M) (hf : ContDiff ℝ (n + 1) ↿f) :
    ContDiff ℝ n fun (x : Space d) => (∂ₜ fun t => f t x) t
```

**`Time.deriv_comp_neg`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L345).

> The chain rule for the time derivative under the reversal of time: the derivative of
> `t ↦ f (-t)` at `t` is minus the derivative of `f` at `-t`.

```lean
lemma deriv_comp_neg {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → M) (t : Time) (hf : DifferentiableAt ℝ f (-t)) :
    ∂ₜ (fun s => f (-s)) t = -∂ₜ f (-t)
```

**`Time.deriv_deriv_comp_neg`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L354).

> The second derivative is unchanged by the reversal of time: for a `C²` curve `f`, the second
> derivative of `t ↦ f (-t)` at `t` is the second derivative of `f` at `-t`, the two changes of sign
> cancelling.

```lean
lemma deriv_deriv_comp_neg {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → M) (hf : ContDiff ℝ 2 f) (t : Time) :
    ∂ₜ (∂ₜ (fun s => f (-s))) t = ∂ₜ (∂ₜ f) (-t)
```

## E. Derivatives of components

**`Time.differentiable_euclid`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L369).

```lean
lemma differentiable_euclid {f : Time → EuclideanSpace ℝ (Fin n)}
    (hf : ∀ i, Differentiable ℝ (fun t => f t i)) :
    Differentiable ℝ f
```

**`Time.deriv_comp_coord`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L378).

> Chain rule for a real function of one coordinate of a curve in Euclidean space: the time
> derivative of `t ↦ f (r t i)` is `f'` times the `i`-th component of the velocity, where `f'` is
> the derivative of `f` at `r t i`.

```lean
lemma deriv_comp_coord {ι : Type} [Fintype ι] {f : ℝ → ℝ} {f' : ℝ}
    {r : Time → EuclideanSpace ℝ ι} {t : Time}
    (i : ι) (hr : DifferentiableAt ℝ r t) (hf : HasDerivAt f f' (r t i)) :
    ∂ₜ (fun s => f (r s i)) t = f' * ∂ₜ r t i
```

**`Time.deriv_euclid`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L389).

```lean
lemma deriv_euclid { μ} {f : Time→ EuclideanSpace ℝ (Fin n)}
    (hf : Differentiable ℝ f) (t : Time) :
    deriv (fun t => f t μ) t = deriv (fun t => f t) t μ
```

**`Time.fderiv_euclid`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L401).

```lean
lemma fderiv_euclid { μ} {f : Time→ EuclideanSpace ℝ (Fin n)}
    (hf : Differentiable ℝ f) (t dt : Time) :
    fderiv ℝ (fun t => f t μ) t dt = fderiv ℝ (fun t => f t) t dt μ
```

**`Time.deriv_lorentzVector`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L410).

```lean
lemma deriv_lorentzVector {d : ℕ} {f : Time → Lorentz.Vector d}
    (hf : Differentiable ℝ f) (t : Time) (i : Fin 1 ⊕ Fin d) :
    deriv (fun t => f t i) t = deriv (fun t => f t) t i
```

**`Time.deriv_space`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L422).

```lean
lemma deriv_space {d : ℕ} {f : Time → Space d}
    (hf : Differentiable ℝ f) (t : Time) (i : Fin d) :
    deriv (fun s => f s i) t = deriv f t i
```

## F. Derivatives of trajectories into `Space`

> For a trajectory `f : Time → Space d` of points in space, the torsor derivative `∂ₜᵥ f` is
> valued in the displacement space `EuclideanSpace ℝ (Fin d)`. Componentwise it agrees with the
> time derivatives of the coordinates, and under the identification of `Space d` with its
> displacement space given by the (arbitrary) zero point it recovers the vector space derivative
> `∂ₜ f`. The latter bridges `∂ₜᵥ` to the existing `∂ₜ` API.
>
> Note that `Space d` carries two `AddTorsor` instances: the intended one over
> `EuclideanSpace ℝ (Fin d)`, and one over itself coming from the module structure on `Space d`.
> Instance resolution selects the former, so `∂ₜᵥ` of a trajectory in `Space d` is valued in
> `EuclideanSpace ℝ (Fin d)` as intended.

**`Time.derivVec_space`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L446).

> The components of the torsor derivative of a trajectory in `Space d` are the time
> derivatives of the coordinates of the trajectory.

```lean
lemma derivVec_space {f : Time → Space d} (hf : Differentiable ℝ f) (t : Time) (i : Fin d) :
    ∂ₜᵥ f t i = ∂ₜ (fun s => f s i) t
```

**`Time.derivVec_eq_deriv_vsub_zero`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean#L460).

> The torsor derivative of a trajectory in `Space d` agrees with the vector space derivative
> `∂ₜ` under the identification of `Space d` with its displacement space given by the zero
> point.

```lean
lemma derivVec_eq_deriv_vsub_zero {f : Time → Space d} (hf : Differentiable ℝ f) (t : Time) :
    ∂ₜᵥ f t = ∂ₜ f t -ᵥ (0 : Space d)
```

## Depends on

- [Lorentz Vectors](../../relativity/tensors/part-03/realtensor-vector-basic.md)
- [The structure of a module on Space](../space/part-01/module.md)
- [Time as an inner product space](innerproductspace.md)

## Sources

- [Physlib/SpaceAndTime/Time/Derivatives.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Derivatives.lean)
