---
declaration: section
origin: cited
lean: OAI.TorsionFreeZeroDivisors.main
statement: formalized
proof: formalized
---

# 196. A counterexample to Kaplansky’s zero-divisor conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a finitely presented torsion-free group *G* whose group algebra $\mathbb F_2[G]$ has nonzero zero divisors, disproving Kaplansky's zero-divisor conjecture. The group has a finite two-dimensional classifying space.

## A Torsion-Free Group Algebra with Zero Divisors

We disprove Kaplansky's zero-divisor conjecture by constructing a finitely presented torsion-free group *G* for which $\mathbb F_2[G]$ has nonzero zero divisors. The group admits a finite two-dimensional classifying space.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kaplansky's zero-divisor conjecture asserts that the group algebra of a torsion-free group over a field has no zero divisors. The formalized result constructs a finitely presented torsion-free group $G$ and nonzero elements $\alpha,\beta\in\mathbb F_2[G]$ with $\alpha\beta=0$, giving a counterexample.

The same group admits a finite two-dimensional classifying space $K(G,1)$.

## Lean: Torsion-free group-algebra counterexample

Stated in [TorsionFreeZeroDivisors.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainTheorem
```

Proved in [lean/OAI/Algebra/GroupRing/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/GroupRing/Main.lean#L13).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/196.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/196.md)
