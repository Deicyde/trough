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
- [Source of `Language.self_eq_mul_add_iff` in Mathlib/Computability/Language.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/Language.lean#L303)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L614)
