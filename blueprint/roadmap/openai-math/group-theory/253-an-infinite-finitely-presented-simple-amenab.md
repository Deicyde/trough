---
declaration: section
origin: cited
lean: OAI.SimpleAmenable.main
statement: formalized
proof: formalized
---

# 253. An infinite finitely presented simple amenable group

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs an infinite finitely presented simple amenable group, answering the longstanding question of whether these properties can occur simultaneously.

## An infinite finitely presented simple amenable group

We construct an infinite finitely presented simple amenable group, giving a positive answer to the finite-presentation existence question for simple amenable groups.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result answers the existence question affirmatively: there is one group that is infinite, finitely presented, simple, and amenable. Amenability is expressed by the Følner condition.

The later general claims about central kernels and enlargements across families are not included.

## Lean: Infinite finitely presented simple amenable group

Stated in [SimpleAmenable.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SimpleAmenable.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : ∃ (G : Type) (_ : Group G),
    Infinite G ∧ Group.IsFinitelyPresented G ∧ IsSimpleGroup G ∧ FolnerAmenable G
```

Proved in [lean/OAI/GroupTheory/SimpleAmenable/Main.lean, line 102](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/SimpleAmenable/Main.lean#L102).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/253.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/253.md)
