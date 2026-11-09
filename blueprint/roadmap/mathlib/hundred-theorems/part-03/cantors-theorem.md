# Cantor’s Theorem

**Cantor's diagonal argument** implies that there are no surjective functions from `α`
to `Set α`.

```lean
Function.cantor_surjective.{u_4} {α : Type u_4} (f : α → Set α) : ¬Function.Surjective f
```

## Depends on

- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Function.cantor_surjective`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Logic/Function/Basic.html#Function.cantor_surjective)
- [Source of `Function.cantor_surjective` in Mathlib/Logic/Function/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Logic/Function/Basic.lean#L372)
- [Freek Wiedijk's 100 theorems, no. 63](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L319)
- [1000+ theorems list: Q474881](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L483)
- [1000+ theorems project: Q474881](https://1000-plus.github.io/all.html?length=-1#Q474881)
- [Wikipedia: Cantor's theorem](https://en.wikipedia.org/wiki/Cantor's_theorem)
- [Wikidata: Q474881](https://www.wikidata.org/wiki/Q474881)
