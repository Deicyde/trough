---
declaration: theorem
origin: cited
lean: TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one, ContinuousLinearMap.IsFredholm.of_isCompactOperator_comp_sub_one
statement: formalized
proof: formalized
---

# Atkinson's theorem

an operator between Banach spaces is Fredholm if and only if it is
invertible modulo compact operators.

```lean
TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [IsRCLikeNormedField 𝕜]
  [CompleteSpace 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F} :
  T.IsFredholm ↔ ∃ S, IsCompactOperator ⇑(S ∘SL T - 1) ∧ IsCompactOperator ⇑(T ∘SL S - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz--Schauder](riesz-schauder.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one).

## Other forms

**Atkinson's theorem, parametrix direction.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsFredholm.of_isCompactOperator_comp_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#ContinuousLinearMap.IsFredholm.of_isCompactOperator_comp_sub_one).

```lean
ContinuousLinearMap.IsFredholm.of_isCompactOperator_comp_sub_one.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [IsRCLikeNormedField 𝕜]
  [CompleteSpace 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] {T : E →L[𝕜] F} {S : F →L[𝕜] E}
  (hST : IsCompactOperator ⇑(S ∘SL T - 1)) (hTS : IsCompactOperator ⇑(T ∘SL S - 1)) : T.IsFredholm
```

## Sources

- [Tau Ceti documentation: `TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one)
- [Source of `TauCeti.isFredholm_iff_exists_isCompactOperator_comp_sub_one` in TauCeti/Analysis/Fredholm/CompactPerturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fredholm/CompactPerturbation.lean#L167)
