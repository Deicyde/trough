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
- [Source of `Language.IsRegular` in Mathlib/Computability/DFA.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/DFA.lean#L346)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L615)
