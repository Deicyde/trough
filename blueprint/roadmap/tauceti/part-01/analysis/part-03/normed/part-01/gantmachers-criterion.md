---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isWeaklyCompact_iff_range_subset, ContinuousLinearMap.IsWeaklyCompact.of_range_precomp_precomp_subset, ContinuousLinearMap.IsWeaklyCompact.range_precomp_precomp_subset
statement: formalized
proof: formalized
---

# Gantmacher's criterion

A bounded operator is weakly compact iff its bidual adjoint
`T**` takes values in the canonical image of the codomain in its bidual. No completeness is
assumed.

```lean
ContinuousLinearMap.isWeaklyCompact_iff_range_subset.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {T : E →L[𝕜] F} :
  T.IsWeaklyCompact ↔
    Set.range ⇑(ContinuousLinearMap.precomp 𝕜 (ContinuousLinearMap.precomp 𝕜 T)) ⊆
      Set.range ⇑(NormedSpace.inclusionInDoubleDual 𝕜 F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Goldstine's theorem](../../../part-01/banach-space-theory/part-02/goldstines-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isWeaklyCompact_iff_range_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.isWeaklyCompact_iff_range_subset).

## Other forms

**Gantmacher's criterion, reverse direction.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsWeaklyCompact.of_range_precomp_precomp_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.IsWeaklyCompact.of_range_precomp_precomp_subset).

```lean
ContinuousLinearMap.IsWeaklyCompact.of_range_precomp_precomp_subset.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {T : E →L[𝕜] F}
  (h :
    Set.range ⇑(ContinuousLinearMap.precomp 𝕜 (ContinuousLinearMap.precomp 𝕜 T)) ⊆
      Set.range ⇑(NormedSpace.inclusionInDoubleDual 𝕜 F)) :
  T.IsWeaklyCompact
```

**Gantmacher's criterion, forward direction.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsWeaklyCompact.range_precomp_precomp_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.IsWeaklyCompact.range_precomp_precomp_subset).

```lean
ContinuousLinearMap.IsWeaklyCompact.range_precomp_precomp_subset.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {T : E →L[𝕜] F} (hT : T.IsWeaklyCompact) :
  Set.range ⇑(ContinuousLinearMap.precomp 𝕜 (ContinuousLinearMap.precomp 𝕜 T)) ⊆
    Set.range ⇑(NormedSpace.inclusionInDoubleDual 𝕜 F)
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isWeaklyCompact_iff_range_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.isWeaklyCompact_iff_range_subset)
- [Source of `ContinuousLinearMap.isWeaklyCompact_iff_range_subset` in TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.lean#L236)
