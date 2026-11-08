---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isCompactOperator_precomp_iff, IsCompactOperator.of_precomp, IsCompactOperator.precomp
statement: formalized
proof: formalized
---

# Schauder's theorem

an operator into a Banach space over `ℝ` or `ℂ` is compact if and only
if its adjoint is compact.

```lean
ContinuousLinearMap.isCompactOperator_precomp_iff.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F} :
  IsCompactOperator ⇑(ContinuousLinearMap.precomp 𝕜 T) ↔ IsCompactOperator ⇑T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isCompactOperator_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Adjoint.html#ContinuousLinearMap.isCompactOperator_precomp_iff).

## Other forms

**Schauder's theorem, reverse direction.** Formalized in Tau Ceti as [`IsCompactOperator.of_precomp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Adjoint.html#IsCompactOperator.of_precomp).

```lean
IsCompactOperator.of_precomp.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [CompleteSpace F] {T : E →L[𝕜] F} (hT : IsCompactOperator ⇑(ContinuousLinearMap.precomp 𝕜 T)) :
  IsCompactOperator ⇑T
```

**Schauder's theorem, forward direction.** Formalized in Tau Ceti as [`IsCompactOperator.precomp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Adjoint.html#IsCompactOperator.precomp).

```lean
IsCompactOperator.precomp.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [NontriviallyNormedField 𝕜] [ProperSpace 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] {T : E →L[𝕜] F} (hT : IsCompactOperator ⇑T) :
  IsCompactOperator ⇑(ContinuousLinearMap.precomp 𝕜 T)
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isCompactOperator_precomp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Adjoint.html#ContinuousLinearMap.isCompactOperator_precomp_iff)
- [Source of `ContinuousLinearMap.isCompactOperator_precomp_iff` in TauCeti/Analysis/Normed/Operator/Compact/Adjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Compact/Adjoint.lean#L201)
