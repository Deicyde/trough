---
declaration: theorem
origin: cited
lean: IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add
statement: formalized
proof: formalized
---

# Finsler's lemma for a positive semidefinite form, over a compact family

On a
finite-dimensional real normed space, let `a x` and `b x` be families of continuous bilinear
forms, continuous on a compact set `K`. Suppose that for every `x ∈ K` the diagonal of `a x` is
nonnegative, and the diagonal of `b x` is positive at every nonzero vector where that of `a x`
vanishes. Then for every sufficiently large `t` one positive constant `c` gives
`c ‖v‖² ≤ t a x v v + b x v v` for every `x ∈ K` and every `v`. Symmetry of the forms is not
needed. For a single pair of forms this is the case of Finsler's lemma where `a` is positive
semidefinite (P. Finsler, Comment. Math. Helv. 9 (1937)).

```lean
IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add.{u_1, u_2} {X : Type u_1}
  {E : Type u_2} [TopologicalSpace X] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] {K : Set X} (hK : IsCompact K) {a b : X → E →L[ℝ] E →L[ℝ] ℝ}
  (ha : ContinuousOn a K) (hb : ContinuousOn b K) (ha₀ : ∀ x ∈ K, ∀ (v : E), 0 ≤ ((a x) v) v)
  (hpos : ∀ x ∈ K, ∀ (v : E), v ≠ 0 → ((a x) v) v = 0 → 0 < ((b x) v) v) :
  ∀ᶠ (t : ℝ) in Filter.atTop,
    ∃ c > 0, ∀ x ∈ K, ∀ (v : E), c * ‖v‖ ^ 2 ≤ t * ((a x) v) v + ((b x) v) v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/BilinearForm.html#IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add).

## Sources

- [Tau Ceti documentation: `IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/BilinearForm.html#IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add)
- [Source of `IsCompact.eventually_exists_pos_forall_mul_norm_sq_le_mul_add` in TauCeti/Topology/Algebra/Module/BilinearForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Module/BilinearForm.lean#L436)
