---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isWeaklyCompact_precomp_iff, ContinuousLinearMap.IsWeaklyCompact.of_precomp, ContinuousLinearMap.IsWeaklyCompact.precomp
statement: formalized
proof: formalized
---

# Gantmacher's theorem

An operator into a Banach space is weakly compact iff its adjoint
is weakly compact.

```lean
ContinuousLinearMap.isWeaklyCompact_precomp_iff.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F} :
  (ContinuousLinearMap.precomp 𝕜 T).IsWeaklyCompact ↔ T.IsWeaklyCompact
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gantmacher's criterion](gantmachers-criterion.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isWeaklyCompact_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.isWeaklyCompact_precomp_iff).

## Other forms

**Gantmacher's theorem, reverse direction.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsWeaklyCompact.of_precomp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.IsWeaklyCompact.of_precomp).

```lean
ContinuousLinearMap.IsWeaklyCompact.of_precomp.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F}
  (hT : (ContinuousLinearMap.precomp 𝕜 T).IsWeaklyCompact) : T.IsWeaklyCompact
```

**Gantmacher's theorem, forward direction.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsWeaklyCompact.precomp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.IsWeaklyCompact.precomp).

```lean
ContinuousLinearMap.IsWeaklyCompact.precomp.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {T : E →L[𝕜] F} (hT : T.IsWeaklyCompact) :
  (ContinuousLinearMap.precomp 𝕜 T).IsWeaklyCompact
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isWeaklyCompact_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.html#ContinuousLinearMap.isWeaklyCompact_precomp_iff)
- [Source of `ContinuousLinearMap.isWeaklyCompact_precomp_iff` in TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/WeaklyCompact/Basic.lean#L300)
