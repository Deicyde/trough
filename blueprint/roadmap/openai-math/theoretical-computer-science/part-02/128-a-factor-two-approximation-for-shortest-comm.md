---
declaration: section
origin: cited
lean: OAI.Superstring.main
statement: formalized
proof: formalized
---

# 128. A factor-two approximation for shortest common superstring

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a deterministic polynomial-time algorithm constructing a common superstring of length at most twice the optimum for every finite family of explicitly represented strings. The running time is polynomial in the full encoded input length, including symbol labels.

## A Polynomial-Time 2-Approximation for Shortest Common Superstring

We give a deterministic algorithm that, for every finite family of explicitly represented ordinary strings, outputs a common superstring of length at most twice the optimum in time polynomial in the total encoded input size, including symbol labels. The guarantee applies to the algorithm constructed here, not the classical maximum-overlap Greedy procedure.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The shortest common superstring problem asks for the shortest string containing each input string as a contiguous substring. The formalized result gives one deterministic polynomial-time algorithm whose output is a common superstring of length at most twice the unrestricted optimum. It applies to every finite list of explicitly encoded strings, with running time measured in input bits and the approximation ratio measured in symbol length.

## Lean: Polynomial-time 2-approximation for shortest common superstring

```lean
theorem main : ∃ f : Instance → Word,
    HasPolynomialImplementation f ∧
    ∀ S, IsCommonSuperstring S (f S) ∧ (f S).length ≤ 2 * opt S
```

Stated in [Superstring.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Superstring.lean#L36). Proved in [lean/OAI/Computability/Superstring/Main.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/Superstring/Main.lean#L57). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/128.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/128.md)
