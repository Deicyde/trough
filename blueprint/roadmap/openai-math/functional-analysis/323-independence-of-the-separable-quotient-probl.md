---
declaration: section
origin: cited
lean: OAI.SeparableQuotient.negative_main
statement: formalized
proof: formalized
---

# 323. Independence of the separable quotient problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Establishes, relative to the consistency of a measurable cardinal, that the separable quotient problem is independent of ZFC. The assertion that every infinite-dimensional Banach space has a separable infinite-dimensional quotient can hold for all real and complex Banach spaces, whereas the continuum hypothesis yields counterexamples over both fields.

## Relative independence of the separable quotient problem

The separable quotient problem asks whether every infinite-dimensional Banach space has a separable infinite-dimensional quotient. We prove that this statement is independent of ZFC, relative to the consistency of ZFC with a measurable cardinal. This holds over both the real and complex fields. For spaces of norm density ℵ$_{1}$, we obtain independence relative to the consistency of ZFC alone.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The separable quotient problem asks whether every infinite-dimensional Banach space has an infinite-dimensional separable quotient. The linked formalization proves the negative direction under the continuum hypothesis: over both the real and complex fields, there is an infinite-dimensional Banach space admitting no bounded linear surjection onto an infinite-dimensional separable Banach space.

This is the conditional counterexample direction. The positive consistency direction and the paper's full relative-independence conclusions are outside the selected statement.

## Lean: Failure of the separable quotient assertion under the continuum hypothesis

```lean
theorem negative_main (hCH : CH) : ¬ SQ.{u} ℝ ∧ ¬ SQ.{u} ℂ
```

Stated in [SeparableQuotientNegative.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SeparableQuotientNegative.lean#L26). Proved in [lean/OAI/Analysis/SeparableQuotients/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/SeparableQuotients/Main.lean#L9).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/323.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/323.md)
