---
declaration: section
origin: cited
lean: OAI.MarkovSuperreflexivity.hasNontrivialMarkovType_iff_hasEquivalentUCNorm
statement: formalized
proof: formalized
---

# 327. Markov type characterizes superreflexivity

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every real Banach space with Markov type *p* for some *p* > 1 admits an equivalent uniformly convex norm, answering Naor's renorming question. Together with the known converse, this characterizes superreflexivity by nontrivial Markov type.

## Nontrivial Markov Type Forces Superreflexivity

We prove that every real Banach space with Markov type *p* > 1 is superreflexive. Together with the known converse, this characterizes superreflexivity by nontrivial Markov type. This answers Naor's question: every real Banach space with nontrivial Markov type admits an equivalent uniformly smooth norm.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves that a real Banach space has nontrivial Markov type exactly when it admits an equivalent uniformly convex norm, hence exactly when it is superreflexive. Nontrivial Markov type means a uniform Markov-type bound for some exponent $p>1$ over all finite stationary reversible chains and all positive times. The exponent and equivalent norm may depend on the space, and the zero space is included. Additional formalized consequences concern uniformly smooth renormings and reflexivity of finitely representable spaces.

## Lean: Nontrivial Markov type and superreflexivity

Stated in [MarkovType.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MarkovType.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem hasNontrivialMarkovType_iff_hasEquivalentUCNorm [CompleteSpace X] :
    HasNontrivialMarkovType X ↔ HasEquivalentUCNorm X
```

Proved in [lean/OAI/Analysis/MarkovType/Main.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/MarkovType/Main.lean#L36).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/327.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/327.md)
