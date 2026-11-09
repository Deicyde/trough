---
declaration: theorem
origin: cited
lean: TauCeti.isFredholm_one_add, TauCeti.isFredholm_one_sub
statement: formalized
proof: formalized
---

# Riesz--Schauder

**Riesz--Schauder**, in the form in which compact perturbations of the identity arise below.

```lean
TauCeti.isFredholm_one_add.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [NontriviallyNormedField 𝕜]
  [IsRCLikeNormedField 𝕜] [CompleteSpace 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {K : E →L[𝕜] E} (hK : IsCompactOperator ⇑K) : (1 + K).IsFredholm
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](../normed/part-02/rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isFredholm_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#TauCeti.isFredholm_one_add).

## Other forms

**Riesz--Schauder.** Formalized in Tau Ceti as [`TauCeti.isFredholm_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#TauCeti.isFredholm_one_sub).

```lean
TauCeti.isFredholm_one_sub.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [NontriviallyNormedField 𝕜]
  [IsRCLikeNormedField 𝕜] [CompleteSpace 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {K : E →L[𝕜] E} (hK : IsCompactOperator ⇑K) : (1 - K).IsFredholm
```

## Sources

- [Tau Ceti documentation: `TauCeti.isFredholm_one_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/CompactPerturbation.html#TauCeti.isFredholm_one_add)
- [Source of `TauCeti.isFredholm_one_add` in TauCeti/Analysis/Fredholm/CompactPerturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fredholm/CompactPerturbation.lean#L93)
