---
declaration: theorem
origin: cited
lean: NumberField.card_ideal_absNorm_le
statement: formalized
proof: formalized
---

# NumberField.card_ideal_absNorm_le

In any number field `F`, the set of nonzero integral ideals with norm at most `X` is
finite, and for `X ≥ 1` its cardinality is at most `X² * 2^[F:ℚ]`.

```lean
NumberField.card_ideal_absNorm_le.{u_1} (F : Type u_1) [Field F] [NumberField F] {X : ℝ}
  (hX : 1 ≤ X) :
  {I | I ≠ ⊥ ∧ ↑(Ideal.absNorm I) ≤ X}.Finite ∧
    ↑{I | I ≠ ⊥ ∧ ↑(Ideal.absNorm I) ≤ X}.ncard ≤ X ^ 2 * 2 ^ Module.finrank ℚ F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.card_ideal_absNorm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/IdealCount/Basic.html#NumberField.card_ideal_absNorm_le).

## Sources

- [Tau Ceti documentation: `NumberField.card_ideal_absNorm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/IdealCount/Basic.html#NumberField.card_ideal_absNorm_le)
- [Source of `NumberField.card_ideal_absNorm_le` in TauCeti/NumberTheory/EffectiveBounds/IdealCount/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/EffectiveBounds/IdealCount/Basic.lean#L397)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
