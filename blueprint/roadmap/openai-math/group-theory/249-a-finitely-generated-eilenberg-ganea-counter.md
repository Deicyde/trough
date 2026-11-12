---
declaration: section
origin: cited
lean: OAI.EilenbergGanea.source_main
statement: formalized
proof: formalized
---

# 249. A finitely generated Eilenberg–Ganea counterexample

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a finitely generated residually finite group with integral cohomological dimension two and geometric dimension three, disproving the Eilenberg–Ganea conjecture. It has no two-dimensional classifying space, even with infinitely many cells.

## A finitely generated counterexample to the Eilenberg–Ganea conjecture

We construct a finitely generated residually finite group of integral cohomological dimension two and geometric dimension three, disproving the Eilenberg–Ganea conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Eilenberg–Ganea conjecture predicts that a group of integral cohomological dimension two has a two-dimensional classifying space. The formalization constructs a finitely generated residually finite group of cohomological dimension two that has a three-dimensional classifying space but no two-dimensional one. Thus its geometric dimension is three, contradicting the conjecture.

## Lean: Counterexample to the Eilenberg–Ganea conjecture

Stated in [EilenbergGanea.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EilenbergGanea.lean).

```lean
theorem source_main :
    Group.FG SourceGroup ∧ Group.ResiduallyFinite SourceGroup ∧
    cohomologicalDimension SourceGroup = 2 ∧
    HasClassifyingSpace.{0} SourceGroup 3 ∧
    ¬ HasClassifyingSpace.{u} SourceGroup 2
```

Proved in [lean/OAI/Topology/EilenbergGanea/Main.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/EilenbergGanea/Main.lean#L30).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/249.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/249.md)
