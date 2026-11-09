# Kleene's recursion theorem

**Kleene's second recursion theorem**

```lean
Nat.Partrec.Code.fixed_point₂ {f : Nat.Partrec.Code → ℕ →. ℕ} (hf : Partrec₂ f) : ∃ c, c.eval = f c
```

## Depends on

- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [In terms of general recursive functions](../../overview/logic-and-computation/computability/computable-function/in-terms-of-general-recursive-functions.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)
- [List](../../overview/data-structures/list-like-structures/list.md)
- [Primitive recursive function](../../overview/logic-and-computation/computability/primitive-recursive-function.md)

## Sources

- [Mathlib documentation: `Nat.Partrec.Code.fixed_point₂`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/PartrecCode.html#Nat.Partrec.Code.fixed_point%E2%82%82)
- [Source of `Nat.Partrec.Code.fixed_point₂` in Mathlib/Computability/PartrecCode.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/PartrecCode.lean#L1039)
- [1000+ theorems list: Q1933521](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1940)
- [1000+ theorems project: Q1933521](https://1000-plus.github.io/all.html?length=-1#Q1933521)
- [Wikipedia: Kleene's recursion theorem](https://en.wikipedia.org/wiki/Kleene's_recursion_theorem)
- [Wikidata: Q1933521](https://www.wikidata.org/wiki/Q1933521)
