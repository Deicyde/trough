---
declaration: module
origin: cited
lean: HasVarAdjDerivAt, HasVarAdjDerivAt.apply_smooth_of_smooth, HasVarAdjDerivAt.apply_smooth_self, HasVarAdjDerivAt.smooth_R, HasVarAdjDerivAt.smooth_linear, HasVarAdjDerivAt.smooth_adjoint, HasVarAdjDerivAt.differentiable_linear, HasVarAdjDerivAt.linearize_of_linear
statement: formalized
proof: formalized
---

# Variational adjoint derivative

The module `Physlib.Mathematics.VariationalCalculus.HasVarAdjDeriv`, [Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean): 33 declarations, 1 with a docstring.

> Variational adjoint derivative of `F` at `u` is a generalization of `(fderiv ℝ F u).adjoint`
> to function spaces. In particular, variational gradient is an analog of
> `gradient F u := (fderiv ℝ F u).adjoint 1`.
>
> The definition of `HasVarAdjDerivAt` is constructed exactly such that we can prove composition
> theorem saying
> ```
>   HasVarAdjDerivAt F F' (G u)) → HasVarAdjDerivAt G G' u →
>     HasVarAdjDerivAt (F ∘ G) (G' ∘ F') u
> ```
> This theorem is the main tool to mechanistically compute variational gradient.

**`HasVarAdjDerivAt`**, a structure, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L41).

> This is analogue of saying `F' = (fderiv ℝ F u).adjoint`.
>
> This definition is useful as we can prove composition theorem for it and `HasVarGradient F grad u`
> can be computed by `grad := F' (fun _ => 1)`.

```lean
structure HasVarAdjDerivAt (F : (X → U) → (Y → V)) (F' : (Y → V) → (X → U)) (u : X → U) : Prop
    where
  smooth_at : ContDiff ℝ ∞ u
  diff : ∀ (φ : ℝ → X → U), ContDiff ℝ ∞ ↿φ →
    ContDiff ℝ ∞ (fun sx : ℝ×Y => F (φ sx.1) sx.2)
  linearize :
    ∀ (φ : ℝ → X → U), ContDiff ℝ ∞ ↿φ →
      ∀ x,
        deriv (fun s' : ℝ => F (φ s') x) 0
        =
        deriv (fun s' : ℝ => F (fun x => φ 0 x + s' • deriv (φ · x) 0) x) 0
  adjoint : HasVarAdjoint (fun δu x => deriv (fun s : ℝ => F (fun x' => u x' + s • δu x') x) 0) F'
```

**`HasVarAdjDerivAt.apply_smooth_of_smooth`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L58).

```lean
lemma apply_smooth_of_smooth {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u v : X → U}
    (h : HasVarAdjDerivAt F F' u) (hv : ContDiff ℝ ∞ v) : ContDiff ℝ ∞ (F v)
```

**`HasVarAdjDerivAt.apply_smooth_self`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L62).

```lean
lemma apply_smooth_self {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u : X → U}
    (h : HasVarAdjDerivAt F F' u) : ContDiff ℝ ∞ (F u)
```

**`HasVarAdjDerivAt.smooth_R`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L66).

```lean
lemma smooth_R {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u : X → U}
    (h : HasVarAdjDerivAt F F' u) {φ : ℝ → X → U} (hφ : ContDiff ℝ ∞ ↿φ) (x : X) :
    ContDiff ℝ ∞ (fun s : ℝ => F (fun x' => φ s x') x)
```

**`HasVarAdjDerivAt.smooth_linear`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L71).

```lean
lemma smooth_linear {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u : X → U}
    (h : HasVarAdjDerivAt F F' u) {φ : ℝ → X → U} (hφ : ContDiff ℝ ∞ ↿φ) :
    ContDiff ℝ ∞ (fun s' : ℝ => F (fun x => φ 0 x + s' • deriv (φ · x) 0) x)
```

**`HasVarAdjDerivAt.smooth_adjoint`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L77).

```lean
lemma smooth_adjoint {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u : X → U}
    (h : HasVarAdjDerivAt F F' u) {δu : X → U} (h' : ContDiff ℝ ∞ δu) (x : X) :
    ContDiff (E:= ℝ) (F := V) ℝ ∞ ((fun s : ℝ => F (fun x' => u x' + s • δu x') x))
```

**`HasVarAdjDerivAt.differentiable_linear`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L83).

```lean
lemma differentiable_linear {F : (X → U) → (X → V)} {F' : (X → V) → (X → U)} {u : X → U}
    (h : HasVarAdjDerivAt F F' u) {φ : ℝ → X → U} (hφ : ContDiff ℝ ∞ ↿φ) (x : X) :
    Differentiable ℝ (fun s' : ℝ => F (fun x => φ 0 x + s' • deriv (φ · x) 0) x)
```

**`HasVarAdjDerivAt.linearize_of_linear`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L89).

```lean
lemma linearize_of_linear {F : (X → U) → (X → V)}
    (add : ∀ φ1 φ2 : X → U,
    ContDiff ℝ ∞ φ1 → ContDiff ℝ ∞ φ2 → F (φ1 + φ2) = F φ1 + F φ2)
    (smul : ∀ (c : ℝ) (φ : X → U), ContDiff ℝ ∞ φ → F (c • φ) = c • F φ)
    (deriv_comm : ∀ {φ : ℝ → X → U} (_ : ContDiff ℝ ∞ ↿φ) (x : X),
      deriv (fun s' => F (φ s') x) 0 = F (fun x' => deriv (fun x => φ x x') 0) x)
    {φ : ℝ → X → U}
    (hφ : ContDiff ℝ ∞ ↿φ) (x : X) :
    deriv (fun s' : ℝ => F (φ s') x) 0
    =
    deriv (fun s' : ℝ => F (fun x' => φ 0 x' + s' • deriv (φ · x') 0) x) 0
```

**`HasVarAdjDerivAt.deriv_adjoint_of_linear`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L117).

```lean
lemma deriv_adjoint_of_linear {F'} {F : (X → U) → (X → V)}
    (add : ∀ φ1 φ2 : X → U,
    ContDiff ℝ ∞ φ1 → ContDiff ℝ ∞ φ2 → F (φ1 + φ2) = F φ1 + F φ2)
    (smul : ∀ (c : ℝ) (φ : X → U), ContDiff ℝ ∞ φ → F (c • φ) = c • F φ)
    (u : X → U) (smooth : ContDiff ℝ ∞ u)
    (h : HasVarAdjoint F F') :
    HasVarAdjoint (fun δu x => deriv (fun s : ℝ => F (fun x' => u x' + s • δu x') x) 0) F'
```

**`HasVarAdjDerivAt.hasVarAdjDerivAt_of_hasVarAdjoint_of_linear`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L143).

```lean
lemma hasVarAdjDerivAt_of_hasVarAdjoint_of_linear
    {F'} {F : (X → U) → (X → V)}
    (diff : ∀ (φ : ℝ → X → U), ContDiff ℝ ∞ ↿φ →
      ContDiff ℝ ∞ (fun sx : ℝ×X => F (φ sx.1) sx.2))

    (add : ∀ φ1 φ2 : X → U,
    ContDiff ℝ ∞ φ1 → ContDiff ℝ ∞ φ2 → F (φ1 + φ2) = F φ1 + F φ2)
    (smul : ∀ (c : ℝ) (φ : X → U), ContDiff ℝ ∞ φ → F (c • φ) = c • F φ)
    (deriv_comm : ∀ {φ : ℝ → X → U} (_ : ContDiff ℝ ∞ ↿φ) (x : X),
      deriv (fun s' => F (φ s') x) 0 = F (fun x' => deriv (fun x => φ x x') 0) x)
    (u : X → U) (smooth : ContDiff ℝ ∞ u)
    (h : HasVarAdjoint F F') :
    HasVarAdjDerivAt F F' u
```

**`HasVarAdjDerivAt.id`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L161).

```lean
lemma id (u) (hu : ContDiff ℝ ∞ u) : HasVarAdjDerivAt (fun φ : X → U => φ) (fun ψ => ψ) u
```

**`HasVarAdjDerivAt.const`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L167).

```lean
lemma const (u : X → U) (v : X → V) (hu : ContDiff ℝ ∞ u) (hv : ContDiff ℝ ∞ v) :
    HasVarAdjDerivAt (fun _ : X → U => v) (fun _ => 0) u
```

**`HasVarAdjDerivAt.comp`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L175).

```lean
lemma comp {F : (Y → V) → (Z → W)} {G : (X → U) → (Y → V)} {u : X → U}
    {F' G'} (hF : HasVarAdjDerivAt F F' (G u)) (hG : HasVarAdjDerivAt G G' u) :
    HasVarAdjDerivAt (fun u => F (G u)) (fun ψ => G' (F' ψ)) u
```

**`HasVarAdjDerivAt.congr`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L202).

```lean
lemma congr {F G : (X → U) → (Y → V)} {F' } {u : X → U}
    (hF : HasVarAdjDerivAt F F' u) (h : ∀ φ, ContDiff ℝ ∞ φ → F φ = G φ) :
    HasVarAdjDerivAt G F' u
```

**`HasVarAdjDerivAt.unique_on_test_functions`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L230).

```lean
lemma unique_on_test_functions
    [IsFiniteMeasureOnCompacts (@volume X _)] [(@volume X _).IsOpenPosMeasure]
    [OpensMeasurableSpace X]
    (F : (X → U) → (Y → V)) (u : X → U)
    (F' G') (hF : HasVarAdjDerivAt F F' u) (hG : HasVarAdjDerivAt F G' u)
    (φ : Y → V) (hφ : IsTestFunction φ) :
    F' φ = G' φ
```

**`HasVarAdjDerivAt.unique`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L238).

```lean
lemma unique {X : Type*} [NormedAddCommGroup X] [InnerProductSpace ℝ X]
    [MeasureSpace X] [OpensMeasurableSpace X]
    [IsFiniteMeasureOnCompacts (@volume X _)] [(@volume X _).IsOpenPosMeasure]
    {Y : Type*} [NormedAddCommGroup Y] [InnerProductSpace ℝ Y]
    [FiniteDimensional ℝ Y] [MeasureSpace Y]
    {F : (X → U) → (Y → V)} {u : X → U}
    {F' G'} (hF : HasVarAdjDerivAt F F' u) (hG : HasVarAdjDerivAt F G' u)
    (φ : Y → V) (hφ : ContDiff ℝ ∞ φ) :
    F' φ = G' φ
```

**`HasVarAdjDerivAt.prod`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L249).

```lean
lemma prod [OpensMeasurableSpace X] [IsFiniteMeasureOnCompacts (volume (α := X))]
    {F : (X → U) → (X → V)} {G : (X → U) → (X → W)} {F' G'}
    (hF : HasVarAdjDerivAt F F' u) (hG : HasVarAdjDerivAt G G' u) :
    HasVarAdjDerivAt
      (fun φ x => (F φ x, G φ x))
      (fun φ x => F' (fun x' => (φ x').1) x + G' (fun x' => (φ x').2) x) u
```

**`HasVarAdjDerivAt.fst`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L297).

```lean
lemma fst {F : (X → U) → (X → W×V)}
    (hF : HasVarAdjDerivAt F F' u) :
    HasVarAdjDerivAt
      (fun φ x => (F φ x).1)
      (fun φ x => F' (fun x' => (φ x', 0)) x) u
```

**`HasVarAdjDerivAt.snd`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L330).

```lean
lemma snd {F : (X → U) → (X → W×V)}
    (hF : HasVarAdjDerivAt F F' u) :
    HasVarAdjDerivAt
      (fun φ x => (F φ x).2)
      (fun φ x => F' (fun x' => (0, φ x')) x) u
```

**`HasVarAdjDerivAt.deriv'`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L363).

```lean
lemma deriv' (u : ℝ → U) (hu : ContDiff ℝ ∞ u) :
    HasVarAdjDerivAt (fun φ : ℝ → U => deriv φ) (fun φ x => - deriv φ x) u
```

**`HasVarAdjDerivAt.deriv`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L415).

```lean
protected lemma deriv (F : (ℝ → U) → (ℝ → V)) (F') (u) (hF : HasVarAdjDerivAt F F' u) :
    HasVarAdjDerivAt (fun φ : ℝ → U => deriv (F φ))
    (fun ψ x => F' (fun x' => - deriv ψ x') x) u
```

**`HasVarAdjDerivAt.fmap`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L420).

```lean
lemma fmap
    {U} [NormedAddCommGroup U] [NormedSpace ℝ U] [InnerProductSpace' ℝ U]
    {V} [NormedAddCommGroup V] [NormedSpace ℝ V] [InnerProductSpace' ℝ V]
    [CompleteSpace U] [CompleteSpace V]
    (f : X → U → V) {f' : X → U → _ }
    (u : X → U) (hu : ContDiff ℝ ∞ u)
    (hf' : ContDiff ℝ ∞ ↿f) (hf : ∀ x u, HasAdjFDerivAt ℝ (f x) (f' x u) u) :
    HasVarAdjDerivAt (fun (φ : X → U) x => f x (φ x)) (fun ψ x => f' x (u x) (ψ x)) u
```

**`HasVarAdjDerivAt.neg`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L486).

```lean
lemma neg (F : (X → U) → (X → V)) (F') (u) (hF : HasVarAdjDerivAt F F' u) :
    HasVarAdjDerivAt (fun φ x => -F φ x) (fun ψ x => - F' ψ x) u
```

**`HasVarAdjDerivAt.add`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L510).

```lean
lemma add
    (F G : (X → U) → (X → V)) (F' G') (u)
    (hF : HasVarAdjDerivAt F F' u) (hG : HasVarAdjDerivAt G G' u) :
    HasVarAdjDerivAt (fun φ x => F φ x + G φ x) (fun ψ x => F' ψ x + G' ψ x) u
```

**`HasVarAdjDerivAt.sum`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L539).

```lean
lemma sum {ι : Type} [Fintype ι]
    (F : ι → (X → U) → (X → V)) (F' : ι → (X → V) → X → U) (u)
    (hu : ContDiff ℝ ∞ u)
    (hF : ∀ i, HasVarAdjDerivAt (F i) (F' i) u) :
    HasVarAdjDerivAt (fun φ x => ∑ i, F i φ x) (fun ψ x => ∑ i, F' i ψ x) u
```

**`HasVarAdjDerivAt.mul`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L566).

```lean
lemma mul
    (F G : (X → U) → (X → ℝ)) (F' G') (u)
    (hF : HasVarAdjDerivAt F F' u) (hG : HasVarAdjDerivAt G G' u) :
    HasVarAdjDerivAt (fun φ x => F φ x * G φ x)
      (fun ψ x => F' (fun x' => ψ x' * G u x') x + G' (fun x' => F u x' * ψ x') x) u
```

**`HasVarAdjDerivAt.const_mul`**, a lemma, [line 610](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L610).

```lean
lemma const_mul
    (F : (X → U) → (X → ℝ)) (F') (u)
    (hF : HasVarAdjDerivAt F F' u) (c : ℝ) :
    HasVarAdjDerivAt (fun φ x => c * F φ x) (fun ψ x => F' (fun x' => c * ψ x') x) u
```

**`HasVarAdjDerivAt.fun_mul`**, a lemma, [line 619](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L619).

```lean
lemma fun_mul {f : X → ℝ} (hf : ContDiff ℝ ∞ f)
    (F : (X → U) → (X → ℝ)) (F') (u)
    (hF : HasVarAdjDerivAt F F' u) :
    HasVarAdjDerivAt (fun φ x => f x * F φ x) (fun ψ x => F' (fun x' => f x' * ψ x') x) u
```

**`HasVarAdjDerivAt.fderiv`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L629).

```lean
protected lemma fderiv (u : X → U) (dx : X) (hu : ContDiff ℝ ∞ u)
    [ProperSpace X] [BorelSpace X]
    [FiniteDimensional ℝ X] [(@volume X _).IsAddHaarMeasure]:
    HasVarAdjDerivAt
      (fun (φ : X → U) x => fderiv ℝ φ x dx)
      (fun ψ x => - fderiv ℝ ψ x dx) u
```

**`HasVarAdjDerivAt.fderiv'`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L660).

```lean
protected lemma fderiv' (F : (X → U) → (X → V)) (F') (u) (dx : X)
    (hF : HasVarAdjDerivAt F F' u)[ProperSpace X] [BorelSpace X]
    [FiniteDimensional ℝ X] [(@volume X _).IsAddHaarMeasure] :
    HasVarAdjDerivAt (fun φ : X → U => fun x => fderiv ℝ (F φ) x dx)
    (fun ψ x => F' (fun x' => - fderiv ℝ ψ x' dx) x) u
```

**`HasVarAdjDerivAt.gradient`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L668).

```lean
protected lemma gradient {d} (u : Space d → ℝ) (hu : ContDiff ℝ ∞ u) :
    HasVarAdjDerivAt
      (fun (φ : Space d → ℝ) x => gradient φ x)
      (fun ψ x => - Space.div (Space.basis.repr ∘ ψ) x) u
```

**`HasVarAdjDerivAt.grad`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L718).

```lean
protected lemma grad {d} (u : Space d → ℝ) (hu : ContDiff ℝ ∞ u) :
    HasVarAdjDerivAt
      (fun (φ : Space d → ℝ) x => Space.grad φ x)
      (fun ψ x => - Space.div ψ x) u
```

**`HasVarAdjDerivAt.div`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean#L761).

```lean
lemma div {d} (u : Space d → EuclideanSpace ℝ (Fin d)) (hu : ContDiff ℝ ∞ u) :
    HasVarAdjDerivAt
      (fun (φ : Space d → EuclideanSpace ℝ (Fin d)) x => Space.div φ x)
      (fun ψ x => - Space.grad ψ x) u
```

## Depends on

- [Variational adjoint](hasvaradjoint.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarAdjDeriv.lean)
