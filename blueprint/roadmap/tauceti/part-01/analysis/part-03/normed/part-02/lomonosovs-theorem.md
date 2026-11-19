---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute, IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule
statement: formalized
proof: formalized
---

# Lomonosov's theorem

a nonscalar operator `T` on a complex normed space commuting with a
nonzero compact operator `K` has a nonzero proper closed hyperinvariant subspace, that is, a
subspace invariant under every operator commuting with `T`.

```lean
IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {K T : E →L[ℂ] E}
  (hK : IsCompactOperator ⇑K) (hK0 : K ≠ 0) (hTK : Commute T K) (hT : ∀ (c : ℂ), T ≠ c • 1) :
  ∃ M,
    IsClosed ↑M ∧ M ≠ ⊥ ∧ M ≠ ⊤ ∧ ∀ (S : E →L[ℂ] E), Commute S T → M ∈ Module.End.invtSubmodule ↑S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lomonosov's lemma](lomonosovs-lemma.md)

## Lean

Formalized in Tau Ceti as [`IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute).

## Other forms

**Lomonosov's theorem for compact operators.** Formalized in Tau Ceti as [`IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule).

```lean
IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {T : E →L[ℂ] E}
  (hT : IsCompactOperator ⇑T) (hTs : ∀ (c : ℂ), T ≠ c • 1) :
  ∃ M,
    IsClosed ↑M ∧ M ≠ ⊥ ∧ M ≠ ⊤ ∧ ∀ (S : E →L[ℂ] E), Commute S T → M ∈ Module.End.invtSubmodule ↑S
```

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute)
- [Source of `IsCompactOperator.exists_isClosed_ne_bot_ne_top_forall_commute_mem_invtSubmodule_of_commute` in TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean#L192)
