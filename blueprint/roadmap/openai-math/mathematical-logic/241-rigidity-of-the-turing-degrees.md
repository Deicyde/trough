---
declaration: section
origin: cited
lean: OAI.TuringRigidity.ManuscriptMain.rigidity
statement: formalized
proof: formalized
---

# 241. Rigidity of the Turing degrees

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every order automorphism of the Turing degrees is the identity, resolving their rigidity problem. Thus no nontrivial relabeling of degrees preserves the ordering by relative computability.

## Rigidity of the Turing degrees

We prove that every order automorphism of the full partial order of Turing degrees is the identity, resolving the rigidity conjecture for the Turing degrees positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The rigidity problem asks whether the ordering of Turing degrees by relative computability has any nontrivial automorphism. The formalized result gives a negative answer: every order automorphism of the full Turing degrees of subsets of $\mathbb N$ fixes every degree, with no definability or genericity assumption. The additional representation corollaries are not included.

## Lean: Rigidity of the Turing degrees

Stated in [DegreeRigidity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DegreeRigidity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem rigidity : MainTheorem
```

Proved in [lean/OAI/Computability/DegreeRigidity/Main.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/DegreeRigidity/Main.lean#L27).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/241.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/241.md)
