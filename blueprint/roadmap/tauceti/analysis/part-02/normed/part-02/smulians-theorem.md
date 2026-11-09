---
declaration: theorem
origin: cited
lean: TauCeti.isSeqCompact_toWeakSpace_of_isCompact, TauCeti.tendsto_subseq_toWeakSpace_of_isCompact_closure
statement: formalized
proof: formalized
---

# Šmulian's theorem

in a real or complex normed space, a weakly compact set is weakly
sequentially compact. Neither completeness nor separability of the space is assumed.

```lean
TauCeti.isSeqCompact_toWeakSpace_of_isCompact.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {K : Set E} (hK : IsCompact (⇑(toWeakSpace 𝕜 E) '' K)) :
  IsSeqCompact (⇑(toWeakSpace 𝕜 E) '' K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isSeqCompact_toWeakSpace_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/SeqCompact.html#TauCeti.isSeqCompact_toWeakSpace_of_isCompact).

## Other forms

**Šmulian's theorem, relative form.** Formalized in Tau Ceti as [`TauCeti.tendsto_subseq_toWeakSpace_of_isCompact_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/SeqCompact.html#TauCeti.tendsto_subseq_toWeakSpace_of_isCompact_closure).

```lean
TauCeti.tendsto_subseq_toWeakSpace_of_isCompact_closure.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {K : Set E}
  (hK : IsCompact (closure (⇑(toWeakSpace 𝕜 E) '' K))) {u : ℕ → E} (hu : ∀ (n : ℕ), u n ∈ K) :
  ∃ x φ,
    StrictMono φ ∧
      Filter.Tendsto (fun n => (toWeakSpace 𝕜 E) (u (φ n))) Filter.atTop
        (nhds ((toWeakSpace 𝕜 E) x))
```

## Sources

- [Tau Ceti documentation: `TauCeti.isSeqCompact_toWeakSpace_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/SeqCompact.html#TauCeti.isSeqCompact_toWeakSpace_of_isCompact)
- [Source of `TauCeti.isSeqCompact_toWeakSpace_of_isCompact` in TauCeti/Analysis/Normed/Module/WeakSpace/SeqCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/WeakSpace/SeqCompact.lean#L104)
