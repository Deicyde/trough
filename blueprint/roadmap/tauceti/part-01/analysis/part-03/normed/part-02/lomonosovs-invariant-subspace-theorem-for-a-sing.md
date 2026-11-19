---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute
statement: formalized
proof: formalized
---

# Lomonosov's invariant-subspace theorem for a single operator

on an infinite-dimensional
real or complex normed space, an operator `T` commuting with a nonzero compact operator `K` has a
nonzero proper closed invariant subspace.

```lean
IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {K T : E →L[𝕜] E} (hK : IsCompactOperator ⇑K) (hK0 : K ≠ 0) (hTK : Commute T K)
  (hE : ¬FiniteDimensional 𝕜 E) : ∃ M, IsClosed ↑M ∧ M ≠ ⊥ ∧ M ≠ ⊤ ∧ M ∈ Module.End.invtSubmodule ↑T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lomonosov's lemma](lomonosovs-lemma.md)

## Lean

Formalized in Tau Ceti as [`IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute).

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute)
- [Source of `IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule_of_commute` in TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean#L150)
