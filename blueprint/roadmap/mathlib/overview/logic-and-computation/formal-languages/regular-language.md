# Regular language

A regular language is a language that is defined by a DFA with finite states.

```lean
Language.IsRegular.{u} {T : Type u} (L : Language T) : Prop
```

## Depends on

- [DFA](dfa.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Language](language.md)

## Sources

- [Mathlib documentation: `Language.IsRegular`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/DFA.html#Language.IsRegular)
- [Source of `Language.IsRegular` in Mathlib/Computability/DFA.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Computability/DFA.lean#L346)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L615)
