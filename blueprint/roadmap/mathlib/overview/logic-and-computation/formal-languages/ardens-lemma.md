# Arden's lemma

**Arden's lemma**

```lean
Language.self_eq_mul_add_iff.{u_1} {α : Type u_1} {l m n : Language α} (hm : [] ∉ m) :
  l = m * l + n ↔ l = KStar.kstar m * n
```

## Depends on

- [Language](language.md)

## Proof depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Language.self_eq_mul_add_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/Language.html#Language.self_eq_mul_add_iff)
- [Source of `Language.self_eq_mul_add_iff` in Mathlib/Computability/Language.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/Language.lean#L304)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L614)
