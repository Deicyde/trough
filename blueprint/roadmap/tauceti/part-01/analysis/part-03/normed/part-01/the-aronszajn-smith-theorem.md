---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule
statement: formalized
proof: formalized
---

# The Aronszajn–Smith theorem

every compact operator on an infinite-dimensional real or
complex normed space has a nonzero proper closed invariant subspace.

```lean
IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {T : E →L[𝕜] E}
  (hT : IsCompactOperator ⇑T) (hE : ¬FiniteDimensional 𝕜 E) :
  ∃ M, IsClosed ↑M ∧ M ≠ ⊥ ∧ M ≠ ⊤ ∧ M ∈ Module.End.invtSubmodule ↑T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lomonosov's invariant-subspace theorem for a single operator](../part-02/lomonosovs-invariant-subspace-theorem-for-a-sing.md)

## Lean

Formalized in Tau Ceti as [`IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule).

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule)
- [Source of `IsCompactOperator.exists_isClosed_ne_bot_ne_top_mem_invtSubmodule` in TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean#L170)
