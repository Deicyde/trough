---
declaration: theorem
origin: cited
lean: TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank
statement: formalized
proof: formalized
---

# TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank

Build a strict s-number sequence from the first four axioms and identity normalization
below the dimension. The Euclidean normalization follows, since the Euclidean space of
dimension `n + 1` has rank `n + 1 > n`.

```lean
TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank.{u} {𝕜 : Type u}
  [NontriviallyNormedField 𝕜] {s : TauCeti.SNumbers.SNumberFamily 𝕜}
  (norm :
    ∀ {X Y : Type u} [inst : NormedAddCommGroup X] [inst_1 : NormedSpace 𝕜 X]
      [inst_2 : NormedAddCommGroup Y] [inst_3 : NormedSpace 𝕜 Y] (T : X →L[𝕜] Y), s T 0 = ‖T‖₊)
  (antitone :
    ∀ {X Y : Type u} [inst : NormedAddCommGroup X] [inst_1 : NormedSpace 𝕜 X]
      [inst_2 : NormedAddCommGroup Y] [inst_3 : NormedSpace 𝕜 Y] (T : X →L[𝕜] Y), Antitone (s T))
  (add_le :
    ∀ {X Y : Type u} [inst : NormedAddCommGroup X] [inst_1 : NormedSpace 𝕜 X]
      [inst_2 : NormedAddCommGroup Y] [inst_3 : NormedSpace 𝕜 Y] (S T : X →L[𝕜] Y) (n : ℕ),
      s (S + T) n ≤ s S n + ‖T‖₊)
  (comp_le :
    ∀ {W X Y Z : Type u} [inst : NormedAddCommGroup W] [inst_1 : NormedSpace 𝕜 W]
      [inst_2 : NormedAddCommGroup X] [inst_3 : NormedSpace 𝕜 X] [inst_4 : NormedAddCommGroup Y]
      [inst_5 : NormedSpace 𝕜 Y] [inst_6 : NormedAddCommGroup Z] [inst_7 : NormedSpace 𝕜 Z]
      (B : Y →L[𝕜] Z) (T : X →L[𝕜] Y) (A : W →L[𝕜] X) (n : ℕ),
      s (B ∘SL T ∘SL A) n ≤ ‖B‖₊ * s T n * ‖A‖₊)
  (eq_zero_of_rank_le :
    ∀ {X Y : Type u} [inst : NormedAddCommGroup X] [inst_1 : NormedSpace 𝕜 X]
      [inst_2 : NormedAddCommGroup Y] [inst_3 : NormedSpace 𝕜 Y] {T : X →L[𝕜] Y} {n : ℕ},
      (↑T).rank ≤ ↑n → s T n = 0)
  (normalize_of_lt_rank :
    ∀ {X : Type u} [inst : NormedAddCommGroup X] [inst_1 : NormedSpace 𝕜 X] (n : ℕ),
      ↑n < Module.rank 𝕜 X → s (ContinuousLinearMap.id 𝕜 X) n = 1) :
  TauCeti.SNumbers.IsStrictSNumberSequence
    fun {X Y} [NormedAddCommGroup X] [NormedSpace 𝕜 X] [NormedAddCommGroup Y] [NormedSpace 𝕜 Y] => s
```

## Depends on

- [TauCeti.SNumbers.IsStrictSNumberSequence](tauceti-snumbers-isstrictsnumbersequence.md)
- [TauCeti.SNumbers.SNumberFamily](tauceti-snumbers-snumberfamily.md)

## Proof depends on

- [TauCeti.SNumbers.IsSNumberSequence](tauceti-snumbers-issnumbersequence.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank).

## Sources

- [Tau Ceti documentation: `TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.html#TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank)
- [Source of `TauCeti.SNumbers.IsStrictSNumberSequence.of_normalize_of_lt_rank` in TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/SNumbers/Basic.lean#L85)
- [Tau Ceti roadmap status: s-numbers and entropy numbers of operators between Banach spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SNumbers/STATUS.md)
