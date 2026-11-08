---
declaration: theorem
origin: cited
lean: TauCeti.dense_setOf_exists_norm_apply_eq_norm, StrongDual.exists_pos_norm_sub_ofReal_smul_le, Convex.exists_isMaxOn_re_of_bddAbove, Convex.dense_setOf_ne_zero_isMaxOn_re, Convex.mem_closure_setOf_ne_zero_isMaxOn_re_of_bddAbove, Convex.frontier_subset_closure_setOf_isMaxOn_re
statement: formalized
proof: formalized
---

# The Bishop–Phelps theorem

The continuous linear functionals on a Banach space which
attain their norm on the closed unit ball are norm dense in the dual.

```lean
TauCeti.dense_setOf_exists_norm_apply_eq_norm.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] :
  Dense {g | ∃ x, ‖x‖ ≤ 1 ∧ ‖g x‖ = ‖g‖}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ekeland's variational principle](../../../topology/metric-space/ekelands-variational-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_setOf_exists_norm_apply_eq_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#TauCeti.dense_setOf_exists_norm_apply_eq_norm).

## Other forms

**The Bishop–Phelps lemma.** Formalized in Tau Ceti as [`StrongDual.exists_pos_norm_sub_ofReal_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#StrongDual.exists_pos_norm_sub_ofReal_smul_le).

```lean
StrongDual.exists_pos_norm_sub_ofReal_smul_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] (f h : StrongDual 𝕜 E) {k : ℝ} (hk₀ : 0 ≤ k)
  (hk₁ : k < 1) (hf : f ≠ 0)
  (hpos : ∀ (x : E), k * ‖f‖ * ‖x‖ < RCLike.re (f x) → 0 < RCLike.re (h x)) :
  ∃ c, 0 < c ∧ ‖f - ↑c • h‖ ≤ k * ‖f‖
```

**Bishop–Phelps support lemma.** Formalized in Tau Ceti as [`Convex.exists_isMaxOn_re_of_bddAbove`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.exists_isMaxOn_re_of_bddAbove).

```lean
Convex.exists_isMaxOn_re_of_bddAbove.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E] {C : Set E}
  (hconv : Convex ℝ C) (hC : IsComplete C) {f : StrongDual 𝕜 E} (hf : f ≠ 0)
  (hbdd : BddAbove ((fun y => RCLike.re (f y)) '' C)) {k : ℝ} (hk₀ : 0 < k) (hk₁ : k < 1) {z : E}
  (hz : z ∈ C) :
  ∃ x ∈ C,
    k * ‖f‖ * ‖x - z‖ ≤ RCLike.re (f (x - z)) ∧
      ∃ h,
        h ≠ 0 ∧
          IsMaxOn (fun y => RCLike.re (h y)) C x ∧
            ∀ (w : E), k * ‖f‖ * ‖w‖ < RCLike.re (f w) → 0 < RCLike.re (h w)
```

**The Bishop–Phelps theorem for support functionals.** Formalized in Tau Ceti as [`Convex.dense_setOf_ne_zero_isMaxOn_re`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.dense_setOf_ne_zero_isMaxOn_re).

```lean
Convex.dense_setOf_ne_zero_isMaxOn_re.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E] {C : Set E}
  [Nontrivial E] (hconv : Convex ℝ C) (hC : IsComplete C) (hb : Bornology.IsBounded C)
  (hne : C.Nonempty) : Dense {g | g ≠ 0 ∧ ∃ x ∈ C, IsMaxOn (fun y => RCLike.re (g y)) C x}
```

**The Bishop–Phelps theorem for support functionals, in Phelps' general form.** Formalized in Tau Ceti as [`Convex.mem_closure_setOf_ne_zero_isMaxOn_re_of_bddAbove`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.mem_closure_setOf_ne_zero_isMaxOn_re_of_bddAbove).

```lean
Convex.mem_closure_setOf_ne_zero_isMaxOn_re_of_bddAbove.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E]
  {C : Set E} (hconv : Convex ℝ C) (hC : IsComplete C) (hne : C.Nonempty) {f : StrongDual 𝕜 E}
  (hf : f ≠ 0) (hbdd : BddAbove ((fun y => RCLike.re (f y)) '' C)) :
  f ∈ closure {g | g ≠ 0 ∧ ∃ x ∈ C, IsMaxOn (fun y => RCLike.re (g y)) C x}
```

**The Bishop–Phelps theorem for support points.** Formalized in Tau Ceti as [`Convex.frontier_subset_closure_setOf_isMaxOn_re`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.frontier_subset_closure_setOf_isMaxOn_re).

```lean
Convex.frontier_subset_closure_setOf_isMaxOn_re.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E] {C : Set E}
  (hconv : Convex ℝ C) (hC : IsComplete C) :
  frontier C ⊆ closure {x | x ∈ C ∧ ∃ g, g ≠ 0 ∧ IsMaxOn (fun y => RCLike.re (g y)) C x}
```

## Sources

- [Tau Ceti documentation: `TauCeti.dense_setOf_exists_norm_apply_eq_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#TauCeti.dense_setOf_exists_norm_apply_eq_norm)
- [Source of `TauCeti.dense_setOf_exists_norm_apply_eq_norm` in TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean#L326)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
