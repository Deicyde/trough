---
declaration: module
origin: cited
lean: SpaceTime.deriv, SpaceTime.deriv_eq, SpaceTime.manifoldDeriv, SpaceTime.manifoldDeriv_eq, SpaceTime.deriv_eq_mfderiv, SpaceTime.deriv_eq_manifoldDeriv, SpaceTime.manifoldDeriv_const, SpaceTime.differentiable_vector
statement: formalized
proof: formalized
---

# Derivatives on SpaceTime

The module `Physlib.SpaceAndTime.SpaceTime.Derivatives`, [Physlib/SpaceAndTime/SpaceTime/Derivatives.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean): 44 declarations, 18 with a docstring.

## i. Overview

> In this module we define and prove basic lemmas about derivatives of functions and
> distributions on `SpaceTime d`.

## ii. Key results

> - `deriv` : The derivative of a function `SpaceTime d → M` along the `μ` coordinate.
> - `manifoldDeriv` : The derivative of a function from `SpaceTime d` to a manifold along
>   the `μ` coordinate.
> - `contDiff_deriv` : If `f` is `C^{n+1}` then `∂_ μ f` is `C^n`.
> - `differentiable_deriv` : If `f` is `C^2` then `∂_ μ f` is differentiable.
> - `deriv_commute` : Derivatives on `SpaceTime d` commute (Clairaut's theorem).
> - `deriv_sum_inr` : The derivative along a spatial coordinate in terms of the
>   derivative on `Space d`.
> - `deriv_sum_inl` : The derivative along the temporal coordinate in terms of the
>   derivative on `Time`.
> - `iteratedDeriv` : Iterated derivatives along a multiset of coordinates.
> - `distDeriv` : The derivative of a distribution on `SpaceTime d` along the `μ` coordinate.
> - `distDeriv_commute` : Derivatives of distributions on `SpaceTime d` commute.

## iv. References

> * None.

## A. Derivatives of functions on `SpaceTime d`

### A.1. The definition of the derivative

**`SpaceTime.deriv`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L84).

> The derivative of a function `SpaceTime d → ℝ` along the `μ` coordinate.

```lean
noncomputable def deriv {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) : SpaceTime d → M
```

**`SpaceTime.deriv_eq`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L91).

```lean
lemma deriv_eq {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (y : SpaceTime d) :
    ∂_ μ f y =
    fderiv ℝ f y (Lorentz.Vector.basis μ)
```

**`SpaceTime.manifoldDeriv`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L99).

> The derivative of a function from `SpaceTime d` to a manifold along the `μ`
> coordinate, as a tangent vector at the value of the function.

```lean
noncomputable def manifoldDeriv {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → N) :
    (y : SpaceTime d) → TangentSpace I (f y)
```

**`SpaceTime.manifoldDeriv_eq`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L106).

```lean
lemma manifoldDeriv_eq {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → N)
    (y : SpaceTime d) :
    manifoldDeriv I μ f y =
      mfderiv 𝓘(ℝ, SpaceTime d) I f y
        ((Lorentz.Vector.basis μ : SpaceTime d) : TangentSpace 𝓘(ℝ, SpaceTime d) y)
```

**`SpaceTime.deriv_eq_mfderiv`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L115).

> The spacetime derivative is the manifold derivative for functions into normed spaces.

```lean
lemma deriv_eq_mfderiv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (y : SpaceTime d) :
    deriv μ f y =
      mfderiv 𝓘(ℝ, SpaceTime d) 𝓘(ℝ, M) f y
        ((Lorentz.Vector.basis μ : SpaceTime d) : TangentSpace 𝓘(ℝ, SpaceTime d) y)
```

**`SpaceTime.deriv_eq_manifoldDeriv`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L123).

```lean
lemma deriv_eq_manifoldDeriv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (y : SpaceTime d) :
    deriv μ f y = manifoldDeriv 𝓘(ℝ, M) μ f y
```

**`SpaceTime.manifoldDeriv_const`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L130).

```lean
lemma manifoldDeriv_const {E H N : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] (I : ModelWithCorners ℝ E H) [TopologicalSpace N]
    [ChartedSpace H N] {d : ℕ} (μ : Fin 1 ⊕ Fin d) (n : N) (y : SpaceTime d) :
    manifoldDeriv I μ (fun _ : SpaceTime d => n) y = 0
```

### A.2. Basic equality lemmas

**`SpaceTime.differentiable_vector`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L144).

```lean
lemma differentiable_vector {d : ℕ} (f : SpaceTime d → Lorentz.Vector d) :
    (∀ ν, Differentiable ℝ (fun x => f x ν)) ↔ Differentiable ℝ f
```

**`SpaceTime.contDiff_vector`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L151).

```lean
lemma contDiff_vector {d : ℕ} (f : SpaceTime d → Lorentz.Vector d) :
    (∀ ν, ContDiff ℝ n (fun x => f x ν)) ↔ ContDiff ℝ n f
```

**`SpaceTime.fderiv_vector`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L158).

```lean
lemma fderiv_vector {d : ℕ} (f : SpaceTime d → Lorentz.Vector d)
    (hf : Differentiable ℝ f) (y dt : SpaceTime d) (ν : Fin 1 ⊕ Fin d) :
    fderiv ℝ f y dt ν = fderiv ℝ (fun x => f x ν) y dt
```

**`SpaceTime.deriv_apply_eq`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L166).

```lean
lemma deriv_apply_eq {d : ℕ} (μ ν : Fin 1 ⊕ Fin d) (f : SpaceTime d → Lorentz.Vector d)
    (hf : Differentiable ℝ f)
    (y : SpaceTime d) :
    ∂_ μ f y ν = fderiv ℝ (fun x => f x ν) y (Lorentz.Vector.basis μ)
```

**`SpaceTime.deriv_coord`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L173).

```lean
lemma deriv_coord {d : ℕ} (μ ν : Fin 1 ⊕ Fin d) :
    ∂_ μ (fun x => x ν) = if μ = ν then 1 else 0
```

### A.3. Linearity of the derivative

**`SpaceTime.deriv_zero`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L189).

```lean
lemma deriv_zero {d : ℕ} (μ : Fin 1 ⊕ Fin d) : SpaceTime.deriv μ (fun _ => (0 : ℝ)) = 0
```

**`SpaceTime.deriv_add`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L195).

> Derivatives on spacetime distribute over addition.

```lean
lemma deriv_add {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (μ : Fin 1 ⊕ Fin d) (f g : SpaceTime d → M) (hf : Differentiable ℝ f)
    (hg : Differentiable ℝ g) :
    ∂_ μ (f + g) = ∂_ μ f + ∂_ μ g
```

**`SpaceTime.deriv_const_smul`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L203).

> Derivatives on spacetime commute with multiplication by a constant.

```lean
lemma deriv_const_smul {M R : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] [Semiring R]
    [Module R M] [SMulCommClass ℝ R M] [ContinuousConstSMul R M] {d : ℕ}
    (μ : Fin 1 ⊕ Fin d) (c : R) {f : SpaceTime d → M} (hf : Differentiable ℝ f) :
    ∂_ μ (c • f) = c • ∂_ μ f
```

### A.4. Smoothness and differentiability of the derivative

**`SpaceTime.contDiff_deriv`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L220).

> If `f` is `C^{n+1}` then `∂_ μ f` is `C^n`.

```lean
lemma contDiff_deriv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    {n : WithTop ℕ∞} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (hf : ContDiff ℝ (n + 1) f) :
    ContDiff ℝ n (∂_ μ f)
```

**`SpaceTime.differentiable_deriv`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L229).

> If `f` is `C^2` then `∂_ μ f` is differentiable.

```lean
lemma differentiable_deriv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (hf : ContDiff ℝ 2 f) :
    Differentiable ℝ (∂_ μ f)
```

### A.5. Derivatives commute

**`SpaceTime.deriv_commute`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L241).

> Derivatives on spacetime commute with one another (Clairaut's theorem).

```lean
lemma deriv_commute {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (μ ν : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) (hf : ContDiff ℝ 2 f) :
    ∂_ μ (∂_ ν f) = ∂_ ν (∂_ μ f)
```

**`SpaceTime.foldl_deriv_perm`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L258).

> For a smooth function, iterated derivatives along a list of directions do not depend on the
> order of the list.

```lean
lemma foldl_deriv_perm {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    {l₁ l₂ : List (Fin 1 ⊕ Fin d)} (h : l₁.Perm l₂) {f : SpaceTime d → M}
    (hf : ContDiff ℝ ∞ f) :
    l₁.foldl (fun g μ => ∂_ μ g) f = l₂.foldl (fun g μ => ∂_ μ g) f
```

### A.6. The derivative of a function composed with a Lorentz transformation

**`SpaceTime.deriv_comp_lorentz_action`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L276).

```lean
lemma deriv_comp_lorentz_action {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (μ : Fin 1 ⊕ Fin d)
    (f : SpaceTime d → M) (hf : Differentiable ℝ f) (Λ : LorentzGroup d)
    (x : SpaceTime d) :
    ∂_ μ (fun x => f (Λ • x)) x = ∑ ν, Λ.1 ν μ • ∂_ ν f (Λ • x)
```

**`SpaceTime.deriv_equivariant`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L294).

```lean
lemma deriv_equivariant (f : SpaceTime d → M) (Λ : LorentzGroup d) (x : SpaceTime d)
    (hf : Differentiable ℝ f) (μ : Fin 1 ⊕ Fin d) :
    ∂_ μ (fun x => Λ • f (Λ⁻¹ • x)) x =
    ∑ ν, Λ⁻¹.1 ν μ • Λ • ∂_ ν f (Λ⁻¹ • x)
```

### A.7. Spacetime derivatives in terms of time and space derivatives

**`SpaceTime.deriv_sum_inr`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L317).

```lean
lemma deriv_sum_inr {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : SpaceTime d → M)
    (hf : Differentiable ℝ f) (x : SpaceTime d) (i : Fin d) :
    ∂_ (Sum.inr i) f x
    = Space.deriv i (fun y => f ((toTimeAndSpace c).symm ((toTimeAndSpace c x).1, y)))
      (toTimeAndSpace c x).2
```

**`SpaceTime.deriv_sum_inl`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L342).

```lean
lemma deriv_sum_inl {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] (c : SpeedOfLight) (f : SpaceTime d → M)
    (hf : Differentiable ℝ f) (x : SpaceTime d) :
    ∂_ (Sum.inl 0) f x
    = (1/(c : ℝ)) • Time.deriv (fun t => f ((toTimeAndSpace c).symm (t, (toTimeAndSpace c x).2)))
      (toTimeAndSpace c x).1
```

### A.8. Iterated derivatives

> Derivatives along different directions commute for smooth functions, so an iterated derivative of
> a smooth function depends only on how many times each direction occurs. We therefore index iterated
> derivatives by a multiset `s` of directions and write `iteratedDeriv s f`. For an arbitrary function
> the derivatives are taken in the order of the list `s.toList`, and the lemmas that reorder
> directions assume that `f` is smooth.

**`SpaceTime.iteratedDeriv`**, a def, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L385).

> The iterated derivative of `f`, differentiating once along each element of `s`.

```lean
noncomputable def iteratedDeriv {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    {d : ℕ} (s : Multiset (Fin 1 ⊕ Fin d)) (f : SpaceTime d → M) : SpaceTime d → M
```

**`SpaceTime.iteratedDeriv_zero`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L390).

```lean
lemma iteratedDeriv_zero {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M] {d : ℕ}
    (f : SpaceTime d → M) :
    iteratedDeriv 0 f = f
```

**`SpaceTime.iteratedDeriv_singleton`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L396).

```lean
lemma iteratedDeriv_singleton {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    {d : ℕ} (μ : Fin 1 ⊕ Fin d) (f : SpaceTime d → M) :
    iteratedDeriv {μ} f = ∂_ μ f
```

**`SpaceTime.contDiff_iteratedDeriv`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L402).

> Iterated derivatives of a smooth function are smooth.

```lean
lemma contDiff_iteratedDeriv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (s : Multiset (Fin 1 ⊕ Fin d)) {f : SpaceTime d → M} (hf : ContDiff ℝ ∞ f) :
    ContDiff ℝ ∞ (iteratedDeriv s f)
```

**`SpaceTime.iteratedDeriv_cons`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L411).

> An iterated derivative of a smooth function may begin with any of its directions.

```lean
lemma iteratedDeriv_cons {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (μ : Fin 1 ⊕ Fin d) (s : Multiset (Fin 1 ⊕ Fin d)) {f : SpaceTime d → M}
    (hf : ContDiff ℝ ∞ f) :
    iteratedDeriv (μ ::ₘ s) f = iteratedDeriv s (∂_ μ f)
```

**`SpaceTime.iteratedDeriv_add`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L420).

> Iterated derivatives of smooth functions distribute over addition.

```lean
lemma iteratedDeriv_add {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (s : Multiset (Fin 1 ⊕ Fin d)) {f g : SpaceTime d → M} (hf : ContDiff ℝ ∞ f)
    (hg : ContDiff ℝ ∞ g) :
    iteratedDeriv s (f + g) = iteratedDeriv s f + iteratedDeriv s g
```

**`SpaceTime.iteratedDeriv_const_smul`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L433).

> Iterated derivatives of smooth functions commute with multiplication by a constant.

```lean
lemma iteratedDeriv_const_smul {M R : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] [Semiring R]
    [Module R M] [SMulCommClass ℝ R M] [ContinuousConstSMul R M] {d : ℕ}
    (s : Multiset (Fin 1 ⊕ Fin d)) (c : R) {f : SpaceTime d → M} (hf : ContDiff ℝ ∞ f) :
    iteratedDeriv s (c • f) = c • iteratedDeriv s f
```

## B. Derivatives of distributions

**`SpaceTime.distDeriv`**, a def, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L455).

> Given a distribution (function) `f : SpaceTime d →d[ℝ] M` the derivative
> of `f` in direction `μ`.

```lean
noncomputable def distDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin 1 ⊕ Fin d) : ((SpaceTime d) →d[ℝ] M) →ₗ[ℝ] (SpaceTime d) →d[ℝ] M
```

**`SpaceTime.distDeriv_apply`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L470).

```lean
lemma distDeriv_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin 1 ⊕ Fin d) (f : (SpaceTime d) →d[ℝ] M) (ε : 𝓢(SpaceTime d, ℝ)) :
    distDeriv μ f ε = fderivD ℝ f ε (Lorentz.Vector.basis μ)
```

**`SpaceTime.distDeriv_apply'`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L475).

```lean
lemma distDeriv_apply' {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin 1 ⊕ Fin d) (f : (SpaceTime d) →d[ℝ] M) (ε : 𝓢(SpaceTime d, ℝ)) :
    distDeriv μ f ε =
    - f ((SchwartzMap.evalCLM ℝ (SpaceTime d) ℝ (Lorentz.Vector.basis μ))
    ((fderivCLM ℝ (SpaceTime d) ℝ) ε))
```

**`SpaceTime.apply_fderiv_eq_distDeriv`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L482).

```lean
lemma apply_fderiv_eq_distDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin 1 ⊕ Fin d) (f : (SpaceTime d) →d[ℝ] M) (ε : 𝓢(SpaceTime d, ℝ)) :
    f ((SchwartzMap.evalCLM ℝ (SpaceTime d) ℝ (Lorentz.Vector.basis μ))
    ((fderivCLM ℝ (SpaceTime d) ℝ) ε)) =
    - distDeriv μ f ε
```

### B.1. Commutation of derivatives of distributions

**`SpaceTime.distDeriv_commute`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L496).

```lean
lemma distDeriv_commute {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ ν : Fin 1 ⊕ Fin d) (f : (SpaceTime d) →d[ℝ] M) :
    distDeriv μ (distDeriv ν f) = distDeriv ν (distDeriv μ f)
```

### B.2. Lorentz group action on derivatives of distributions

> We now show how the Lorentz group action on distributions interacts with derivatives.

**`SpaceTime.distDeriv_comp_lorentz_action`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L513).

```lean
lemma distDeriv_comp_lorentz_action {μ : Fin 1 ⊕ Fin d} (Λ : LorentzGroup d)
    (f : (SpaceTime d) →d[ℝ] M) :
    distDeriv μ (Λ • f) = ∑ ν, Λ⁻¹.1 ν μ • (Λ • distDeriv ν f)
```

## C. Derivatives of tensors

> Given a function `f : SpaceTime d → M` where `M` is a tensor space, we can define the
> derivative of `f` as a tensor. In particular this is `∂_μ f` viewed as a tensor in
> `Lorentz.CoVector d ⊗[ℝ] M`.

**`SpaceTime.tensorDeriv`**, a def, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L566).

> The derivative of a tensor, as a tensor.

```lean
def tensorDeriv (f : SpaceTime d → M) :
    SpaceTime d → Lorentz.CoVector d ⊗[ℝ] M
```

**`SpaceTime.tensorDeriv_equivariant`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L570).

```lean
lemma tensorDeriv_equivariant (f : SpaceTime d → M) (Λ : LorentzGroup d) (x : SpaceTime d)
    (hf : Differentiable ℝ f) :
    tensorDeriv (fun x => Λ • f (Λ⁻¹ • x)) x =
    Λ • tensorDeriv f (Λ⁻¹ • x)
```

**`SpaceTime.tensorDeriv_toTensor_basis_repr`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L589).

```lean
lemma tensorDeriv_toTensor_basis_repr
    {f : SpaceTime d → M}
    (hf : Differentiable ℝ f) (x : SpaceTime d)
    (b : Tensor.ComponentIdx (Fin.append ![realLorentzTensor.Color.down] c)) :
    (Tensor.basis _).repr (Tensorial.toTensor (tensorDeriv f x)) b =
    ∂_ (Lorentz.CoVector.indexEquiv (ComponentIdx.prod b).1)
      (fun x => (Tensor.basis _).repr (Tensorial.toTensor (f x))
        (ComponentIdx.prod b).2) x
```

**`SpaceTime.tensorDeriv_eq_sum_tensor_basis`**, a lemma, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L624).

> The expansion of `tensorDeriv` in terms of the tensor basis vector.

```lean
lemma tensorDeriv_eq_sum_tensor_basis
    {f : SpaceTime d → M} (hf : Differentiable ℝ f) (x : SpaceTime d) :
    tensorDeriv f x = ∑ b, ∂_ (CoVector.indexEquiv (ComponentIdx.prod b).1)
      (fun x => (Tensor.basis _).repr (toTensor (f x)) (ComponentIdx.prod b).2) x •
    toTensor.symm (Tensor.basis _ b)
```

### C.1. Derivatives of tensors for distributions

**`SpaceTime.distTensorDeriv`**, a def, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L641).

> The derivative of a tensor, as a tensor for distributions.

```lean
def distTensorDeriv {M d} [NormedAddCommGroup M]
    [InnerProductSpace ℝ M] [FiniteDimensional ℝ M] :
    ((SpaceTime d) →d[ℝ] M) →ₗ[ℝ] ((SpaceTime d) →d[ℝ] Lorentz.CoVector d ⊗[ℝ] M)
```

**`SpaceTime.distTensorDeriv_apply`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L671).

```lean
lemma distTensorDeriv_apply {M d} [NormedAddCommGroup M]
    [InnerProductSpace ℝ M] [FiniteDimensional ℝ M] (f : (SpaceTime d) →d[ℝ] M)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    distTensorDeriv f ε = ∑ μ, (Lorentz.CoVector.basis μ) ⊗ₜ distDeriv μ f ε
```

**`SpaceTime.distTensorDeriv_equivariant`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L677).

```lean
lemma distTensorDeriv_equivariant {M : Type} [NormedAddCommGroup M]
    [InnerProductSpace ℝ M] [FiniteDimensional ℝ M] [(realLorentzTensor d).Tensorial c M]
    (f : (SpaceTime d) →d[ℝ] M) (Λ : LorentzGroup d) :
    distTensorDeriv (Λ • f) = Λ • distTensorDeriv f
```

**`SpaceTime.distTensorDeriv_toTensor_basis_repr`**, a lemma, [line 701](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean#L701).

```lean
lemma distTensorDeriv_toTensor_basis_repr {M : Type} [NormedAddCommGroup M]
    [InnerProductSpace ℝ M] [FiniteDimensional ℝ M] [(realLorentzTensor d).Tensorial c M]
    {f : (SpaceTime d) →d[ℝ] M}
    (ε : 𝓢(SpaceTime d, ℝ))
    (b : Tensor.ComponentIdx (Fin.append ![realLorentzTensor.Color.down] c)) :
    (Tensor.basis _).repr (Tensorial.toTensor (distTensorDeriv f ε)) b =
    (Tensor.basis _).repr (Tensorial.toTensor
    (distDeriv (Lorentz.CoVector.indexEquiv (ComponentIdx.prod b).1) f ε))
    (ComponentIdx.prod b).2
```

## Depends on

- [Tensorial nature of Lorentz covectors](../../relativity/tensors/part-03/realtensor-covector-tensorial.md)
- [Derivatives on Space](../space/part-01/derivatives-basic.md)
- [Lorentz group actions related to SpaceTime](lorentzaction.md)
- [Time Derivatives](../time/derivatives.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/Derivatives.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Derivatives.lean)
