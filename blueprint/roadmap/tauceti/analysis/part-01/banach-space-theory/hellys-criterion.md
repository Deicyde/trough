---
declaration: theorem
origin: cited
lean: TauCeti.exists_norm_lt_and_forall_apply_eq_iff
statement: formalized
proof: formalized
---

# Helly's criterion

Let `f i` be finitely many continuous linear functionals on `E`, let
`c i` be scalars and let `0 ≤ M`. For every `ε > 0` some `x : E` with `‖x‖ < M + ε` satisfies
`f i x = c i` for every `i` if and only if `‖∑ i, a i * c i‖ ≤ M * ‖∑ i, a i • f i‖` for all
scalars `a i`.

```lean
TauCeti.exists_norm_lt_and_forall_apply_eq_iff.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] {ι : Type u_3} [Fintype ι]
  (f : ι → StrongDual 𝕜 E) (c : ι → 𝕜) {M : ℝ} (hM : 0 ≤ M) :
  (∀ ε > 0, ∃ x, ‖x‖ < M + ε ∧ ∀ (i : ι), (f i) x = c i) ↔
    ∀ (a : ι → 𝕜), ‖∑ i, a i * c i‖ ≤ M * ‖∑ i, a i • f i‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Helly's lemma](hellys-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_norm_lt_and_forall_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#TauCeti.exists_norm_lt_and_forall_apply_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_norm_lt_and_forall_apply_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Helly.html#TauCeti.exists_norm_lt_and_forall_apply_eq_iff)
- [Source of `TauCeti.exists_norm_lt_and_forall_apply_eq_iff` in TauCeti/Analysis/Normed/Module/Dual/Helly.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/Helly.lean#L156)
