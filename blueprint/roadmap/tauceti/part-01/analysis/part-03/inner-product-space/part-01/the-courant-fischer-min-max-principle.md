---
declaration: theorem
origin: cited
lean: TauCeti.isLeast_minMax_of_hilbertBasis
statement: formalized
proof: formalized
---

# The Courant–Fischer min–max principle

Let `B` be symmetric with `B v v ≥ 0`, and let
`(eⱼ)` be an orthonormal basis of `H` with `eⱼ = J uⱼ` and `B uⱼ v = κⱼ ⟪eⱼ, J v⟫` for every `v`,
where `κ` is nondecreasing. Then `κₖ` is the least `C` for which some subspace `W` of `V` with
`dim J W ≥ k + 1` satisfies `B v v ≤ C ‖J v‖²` for every `v ∈ W`. The minimum is attained on the
span of `u₀, …, uₖ`.

```lean
TauCeti.isLeast_minMax_of_hilbertBasis.{u_1, u_2} {V : Type u_1} {H : Type u_2} [AddCommGroup V]
  [_root_.Module ℝ V] [NormedAddCommGroup H] [InnerProductSpace ℝ H] {B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ}
  {J : V →ₗ[ℝ] H} {kappa : ℕ → ℝ} {u : ℕ → V} (hsymm : ∀ (v w : V), (B v) w = (B w) v)
  (hnonneg : ∀ (v : V), 0 ≤ (B v) v) (e : HilbertBasis ℕ ℝ H) (hkappa : Monotone kappa)
  (hJu : ∀ (j : ℕ), J (u j) = e j)
  (heq : ∀ (j : ℕ) (v : V), (B (u j)) v = kappa j * inner ℝ (J (u j)) (J v)) (k : ℕ) :
  IsLeast
    {C | ∃ W, k + 1 ≤ Module.finrank ℝ ↥(Submodule.map J W) ∧ ∀ v ∈ W, (B v) v ≤ C * ‖J v‖ ^ 2}
    (kappa k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bessel's inequality for a functional](bessels-inequality-for-a-functional.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLeast_minMax_of_hilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/MinMax.html#TauCeti.isLeast_minMax_of_hilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.isLeast_minMax_of_hilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/MinMax.html#TauCeti.isLeast_minMax_of_hilbertBasis)
- [Source of `TauCeti.isLeast_minMax_of_hilbertBasis` in TauCeti/Analysis/InnerProductSpace/Variational/MinMax.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Variational/MinMax.lean#L169)
