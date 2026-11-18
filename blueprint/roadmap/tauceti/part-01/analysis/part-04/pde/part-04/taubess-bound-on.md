---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq, TauCeti.SeibergWitten.norm_sq_add_norm_sq_le_one_add_div, TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq, TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax, TauCeti.SeibergWitten.norm_sq_le_div_mul_max_add_div_sq, TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax_of_le_const, TauCeti.SeibergWitten.sq_add_sq_le_one_add_div
statement: formalized
proof: formalized
---

# Taubes's bound on `β`

On a compact boundaryless Riemannian manifold, let `A`, `B`, `Dα`,
`Dβ` stand for `|α|`, `|β|`, `|∇_a α|` and `|∇_a β|`, with `A²` and `B²` of class `C²`, and
suppose they satisfy the projected Weitzenböck inequalities with constant `c ≥ 0`. Then for every
`κ ≥ 4 c²` and every `r ≥ max 1 (16 c)`,

`|β|² ≤ (κ / r) max (1 - |α|²) 0 + C / r²`,

with `C = (16 κ c + 128 c² + 132 κ² c²) (1 + 8 c + c²) + κ (8 c + c²)`. In terms of the vacuum
defect `w₊ = max (1 - |α|²) 0` this is `|β|² ≤ (κ / r) w₊ + C / r²`.

```lean
TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [CompactSpace M] {A B Dα Dβ : M → ℝ}
  {r c κ : ℝ} (hc : 0 ≤ c) (hκc : 4 * c ^ 2 ≤ κ) (hr₁ : 1 ≤ r) (hrc : 16 * c ≤ r)
  (hA : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => A x ^ 2)
  (hB : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => B x ^ 2)
  (hα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => A y ^ 2) x / 2 + Dα x ^ 2 +
          r / 4 * (A x ^ 2 + B x ^ 2 - 1) * A x ^ 2 ≤
        c * A x * (Dβ x + A x + B x))
  (hβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => B y ^ 2) x / 2 + Dβ x ^ 2 +
          r / 4 * (A x ^ 2 + B x ^ 2 + 1) * B x ^ 2 ≤
        c * B x * (Dα x + A x + B x))
  (x : M) :
  B x ^ 2 ≤
    κ / r * max (1 - A x ^ 2) 0 +
      ((16 * κ * c + 128 * c ^ 2 + 132 * κ ^ 2 * c ^ 2) * (1 + 8 * c + c ^ 2) +
          κ * (8 * c + c ^ 2)) /
        r ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](../../../../geometry/part-01/morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/SpinorBounds.html#TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq).

## Other forms

**Taubes's bound `|α|² + |β|² ≤ 1 + O(1 / r)`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_add_norm_sq_le_one_add_div`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/PointwiseBounds.html#TauCeti.SeibergWitten.norm_sq_add_norm_sq_le_one_add_div).

```lean
TauCeti.SeibergWitten.norm_sq_add_norm_sq_le_one_add_div.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] {α : (x : M) → A x} {β : (x : M) → B x} {c r : ℝ}
  [CompactSpace M] {F₁ : M → Type u_6} {F₂ : M → Type u_7} [(x : M) → SeminormedAddCommGroup (F₁ x)]
  [(x : M) → SeminormedAddCommGroup (F₂ x)] {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} (hc : 0 ≤ c)
  (hr : 0 < r) (hα₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hβ₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hWα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖α x‖ ^ 2) x / 2 + ‖Dα x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 - 1) * ‖α x‖ ^ 2 ≤
        c * ‖α x‖ * (‖Dβ x‖ + ‖α x‖ + ‖β x‖))
  (hWβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖β x‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖))
  (x : M) : ‖α x‖ ^ 2 + ‖β x‖ ^ 2 ≤ 1 + (c ^ 2 + 8 * c) / r
```

**Taubes's bound `|β|² ≤ (4 c² / r) (1 - |α|²) + O(r⁻²)`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/PointwiseBounds.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq).

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] {α : (x : M) → A x} {β : (x : M) → B x} {c r : ℝ}
  [CompactSpace M] {F₁ : M → Type u_6} {F₂ : M → Type u_7} [(x : M) → SeminormedAddCommGroup (F₁ x)]
  [(x : M) → SeminormedAddCommGroup (F₂ x)] {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} (hc : 0 ≤ c)
  (hr1 : 1 ≤ r) (hr32 : 32 * c ≤ r) (hrK : c ^ 2 + 8 * c ≤ r)
  (hα₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hβ₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hWα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖α x‖ ^ 2) x / 2 + ‖Dα x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 - 1) * ‖α x‖ ^ 2 ≤
        c * ‖α x‖ * (‖Dβ x‖ + ‖α x‖ + ‖β x‖))
  (hWβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖β x‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖))
  (x : M) :
  ‖β x‖ ^ 2 ≤
    4 * c ^ 2 / r * (1 - ‖α x‖ ^ 2) + (128 * c ^ 2 + 128 * c ^ 3 + 4 * c ^ 4 + 64 * c ^ 6) / r ^ 2
```

**Taubes's bound `|β|² ≤ (4 c² / r) (1 - |α|²) + O(r⁻²)` at a local maximum.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/PointwiseBounds.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax).

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] {α : (x : M) → A x} {β : (x : M) → B x} {c r : ℝ}
  {G₁ : Type u_6} {G₂ : Type u_7} [SeminormedAddCommGroup G₁] [SeminormedAddCommGroup G₂] {Dα₀ : G₁}
  {Dβ₀ : G₂} {x₀ : M} (hc : 0 ≤ c) (hr1 : 1 ≤ r) (hr32 : 32 * c ≤ r) (hrK : c ^ 2 + 8 * c ≤ r)
  (hα₂ : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun x => ‖α x‖ ^ 2) x₀)
  (hβ₂ : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun x => ‖β x‖ ^ 2) x₀)
  (hmax : IsLocalMax (fun x => ‖β x‖ ^ 2 + 4 * c ^ 2 / r * ‖α x‖ ^ 2) x₀)
  (hs : ‖α x₀‖ ^ 2 + ‖β x₀‖ ^ 2 ≤ 1 + (c ^ 2 + 8 * c) / r)
  (hWα :
    -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖α x‖ ^ 2) x₀ / 2 + ‖Dα₀‖ ^ 2 +
        r / 4 * (‖α x₀‖ ^ 2 + ‖β x₀‖ ^ 2 - 1) * ‖α x₀‖ ^ 2 ≤
      c * ‖α x₀‖ * (‖Dβ₀‖ + ‖α x₀‖ + ‖β x₀‖))
  (hWβ :
    -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖β x‖ ^ 2) x₀ / 2 + ‖Dβ₀‖ ^ 2 +
        r / 4 * (‖α x₀‖ ^ 2 + ‖β x₀‖ ^ 2 + 1) * ‖β x₀‖ ^ 2 ≤
      c * ‖β x₀‖ * (‖Dα₀‖ + ‖α x₀‖ + ‖β x₀‖)) :
  ‖β x₀‖ ^ 2 ≤
    4 * c ^ 2 / r * (1 - ‖α x₀‖ ^ 2) + (128 * c ^ 2 + 128 * c ^ 3 + 4 * c ^ 4 + 64 * c ^ 6) / r ^ 2
```

**Taubes's bound `|β|² ≤ (C / r) w₊ + C / r²`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_max_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/PointwiseBounds.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_add_div_sq).

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_max_add_div_sq.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] {α : (x : M) → A x} {β : (x : M) → B x} {c r : ℝ}
  [CompactSpace M] {F₁ : M → Type u_6} {F₂ : M → Type u_7} [(x : M) → SeminormedAddCommGroup (F₁ x)]
  [(x : M) → SeminormedAddCommGroup (F₂ x)] {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} (hc : 0 ≤ c)
  (hr1 : 1 ≤ r) (hr32 : 32 * c ≤ r) (hrK : c ^ 2 + 8 * c ≤ r)
  (hα₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hβ₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hWα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖α x‖ ^ 2) x / 2 + ‖Dα x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 - 1) * ‖α x‖ ^ 2 ≤
        c * ‖α x‖ * (‖Dβ x‖ + ‖α x‖ + ‖β x‖))
  (hWβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖β x‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖))
  (x : M) :
  ‖β x‖ ^ 2 ≤
    (128 * c ^ 2 + 128 * c ^ 3 + 4 * c ^ 4 + 64 * c ^ 6) / r * max (1 - ‖α x‖ ^ 2) 0 +
      (128 * c ^ 2 + 128 * c ^ 3 + 4 * c ^ 4 + 64 * c ^ 6) / r ^ 2
```

**Taubes's bound on `β` at a maximum point.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax_of_le_const`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax_of_le_const).

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_one_sub_add_div_sq_of_isLocalMax_of_le_const.{u_1, u_2,
    u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F : M → Type u_6} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] [(x : M) → SeminormedAddCommGroup (F x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F x} {r c K₁ K₃ : ℝ} (hr : 0 < r)
  (hK₁ : 0 ≤ K₁) (hK₃ : 0 ≤ K₃) {x₀ : M}
  (hα : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖α y‖ ^ 2) x₀)
  (hβ : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖β y‖ ^ 2) x₀)
  (hWα :
    -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) x₀ / 2) + ‖Dα x₀‖ ^ 2 -
        r / 4 * (1 - ‖α x₀‖ ^ 2) * ‖α x₀‖ ^ 2 ≤
      K₁)
  (hWβ :
    -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) x₀ / 2) +
        r / 4 * (‖α x₀‖ ^ 2 + 1) * ‖β x₀‖ ^ 2 ≤
      c * ‖β x₀‖ * (‖Dα x₀‖ + ‖α x₀‖ + ‖β x₀‖))
  (hC : ‖α x₀‖ ^ 2 + ‖β x₀‖ ^ 2 ≤ 1 + K₃ / r)
  (hmax : IsLocalMax (fun y => ‖β y‖ ^ 2 + 4 * c ^ 2 / r * ‖α y‖ ^ 2) x₀) :
  ‖β x₀‖ ^ 2 ≤
    4 * c ^ 2 / r * (1 - ‖α x₀‖ ^ 2) + 32 * c ^ 2 * (K₁ + K₃ / 8 + 2 * (1 + K₃ / r)) / r ^ 2
```

**Taubes's bound on the full spinor.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.sq_add_sq_le_one_add_div`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/SpinorBounds.html#TauCeti.SeibergWitten.sq_add_sq_le_one_add_div).

```lean
TauCeti.SeibergWitten.sq_add_sq_le_one_add_div.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 2 M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [CompactSpace M] {A B Dα Dβ : M → ℝ}
  {r c : ℝ} (hr : 0 < r) (hc : 0 ≤ c)
  (hA : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => A x ^ 2)
  (hB : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => B x ^ 2)
  (hα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => A y ^ 2) x / 2 + Dα x ^ 2 +
          r / 4 * (A x ^ 2 + B x ^ 2 - 1) * A x ^ 2 ≤
        c * A x * (Dβ x + A x + B x))
  (hβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => B y ^ 2) x / 2 + Dβ x ^ 2 +
          r / 4 * (A x ^ 2 + B x ^ 2 + 1) * B x ^ 2 ≤
        c * B x * (Dα x + A x + B x))
  (x : M) : A x ^ 2 + B x ^ 2 ≤ 1 + (8 * c + c ^ 2) / r
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/SpinorBounds.html#TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq)
- [Source of `TauCeti.SeibergWitten.sq_le_div_mul_max_add_div_sq` in TauCeti/Analysis/PDE/SeibergWitten/SpinorBounds.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/SpinorBounds.lean#L204)
