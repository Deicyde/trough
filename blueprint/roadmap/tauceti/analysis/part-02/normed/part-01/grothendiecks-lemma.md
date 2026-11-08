---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact
statement: formalized
proof: formalized
---

# Grothendieck's lemma

In a real or complex Banach space, a set has weakly compact closure
if, for every `ε > 0`, each of its points lies within norm distance `ε` of a fixed weakly compact
set.

```lean
TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] {A : Set E}
  (h : ∀ ε > 0, ∃ K, IsCompact (⇑(toWeakSpace 𝕜 E) '' K) ∧ ∀ x ∈ A, ∃ y ∈ K, ‖x - y‖ ≤ ε) :
  IsCompact (closure (⇑(toWeakSpace 𝕜 E) '' A))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/Approximation.html#TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/Approximation.html#TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact)
- [Source of `TauCeti.isCompact_closure_toWeakSpace_of_forall_exists_isCompact` in TauCeti/Analysis/Normed/Module/WeakSpace/Approximation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/WeakSpace/Approximation.lean#L46)
