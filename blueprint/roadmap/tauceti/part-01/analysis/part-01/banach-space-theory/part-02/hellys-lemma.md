---
declaration: theorem
origin: cited
lean: StrongDual.exists_norm_lt_and_forall_apply_eq, StrongDual.exists_norm_lt_and_forall_mem_apply_eq, StrongDual.norm_sum_apply_comp_single_le
statement: formalized
proof: formalized
---

# Helly's lemma

For an element `φ` of the bidual of `E`, finitely many continuous linear
functionals `f i` on `E` and `ε > 0`, some `x : E` with `‖x‖ < ‖φ‖ + ε` satisfies
`f i x = φ (f i)` for every `i`.

```lean
StrongDual.exists_norm_lt_and_forall_apply_eq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] (φ : StrongDual 𝕜 (StrongDual 𝕜 E))
  {ι : Type u_3} [Finite ι] (f : ι → StrongDual 𝕜 E) {ε : ℝ} (hε : 0 < ε) :
  ∃ x, ‖x‖ < ‖φ‖ + ε ∧ ∀ (i : ι), (f i) x = φ (f i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Goldstine's theorem](goldstines-theorem.md)

## Lean

Formalized in Tau Ceti as [`StrongDual.exists_norm_lt_and_forall_apply_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#StrongDual.exists_norm_lt_and_forall_apply_eq).

## Other forms

**Helly's lemma for a finite-dimensional subspace `W` of the dual.** Formalized in Tau Ceti as [`StrongDual.exists_norm_lt_and_forall_mem_apply_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#StrongDual.exists_norm_lt_and_forall_mem_apply_eq).

```lean
StrongDual.exists_norm_lt_and_forall_mem_apply_eq.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] (φ : StrongDual 𝕜 (StrongDual 𝕜 E))
  (W : Submodule 𝕜 (StrongDual 𝕜 E)) [FiniteDimensional 𝕜 ↥W] {ε : ℝ} (hε : 0 < ε) :
  ∃ x, ‖x‖ < ‖φ‖ + ε ∧ ∀ f ∈ W, f x = φ f
```

**Helly's lemma, coordinatewise.** Formalized in Tau Ceti as [`StrongDual.norm_sum_apply_comp_single_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#StrongDual.norm_sum_apply_comp_single_le).

```lean
StrongDual.norm_sum_apply_comp_single_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] {κ : Type u_3} [Fintype κ] [DecidableEq κ]
  (f : StrongDual 𝕜 (κ → E)) (hf : ‖f‖ ≤ 1) (z : κ → StrongDual 𝕜 (StrongDual 𝕜 E))
  (hz : ∀ (i : κ), ‖z i‖ ≤ 1) : ‖∑ i, (z i) (f ∘SL ContinuousLinearMap.single 𝕜 (fun x => E) i)‖ ≤ 1
```

## Sources

- [Tau Ceti documentation: `StrongDual.exists_norm_lt_and_forall_apply_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#StrongDual.exists_norm_lt_and_forall_apply_eq)
- [Source of `StrongDual.exists_norm_lt_and_forall_apply_eq` in TauCeti/Analysis/Normed/Module/Dual/Helly.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/Helly.lean#L59)
