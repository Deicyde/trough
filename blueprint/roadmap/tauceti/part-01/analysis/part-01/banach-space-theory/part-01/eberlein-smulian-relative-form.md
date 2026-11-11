---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_closure_toWeakSpace_iff
statement: formalized
proof: formalized
---

# Eberlein–Šmulian, relative form

A set in a real or complex normed space has
weakly compact closure exactly when every sequence in it has a weakly convergent subsequence
with limit in the ambient space.

```lean
TauCeti.isCompact_closure_toWeakSpace_iff.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {K : Set E} :
  IsCompact (closure (⇑(toWeakSpace 𝕜 E) '' K)) ↔
    ∀ (u : ℕ → E),
      (∀ (n : ℕ), u n ∈ K) →
        ∃ x σ,
          StrictMono σ ∧
            Filter.Tendsto (fun n => (toWeakSpace 𝕜 E) (u (σ n))) Filter.atTop
              (nhds ((toWeakSpace 𝕜 E) x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Šmulian's theorem](../part-02/smulians-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_closure_toWeakSpace_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_closure_toWeakSpace_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_closure_toWeakSpace_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.html#TauCeti.isCompact_closure_toWeakSpace_iff)
- [Source of `TauCeti.isCompact_closure_toWeakSpace_iff` in TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/WeakSpace/EberleinSmulian.lean#L134)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
