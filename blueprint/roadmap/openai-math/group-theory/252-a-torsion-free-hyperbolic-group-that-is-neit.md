---
declaration: section
origin: cited
lean: OAI.Release075.main
statement: formalized
proof: formalized
---

# 252. A torsion-free hyperbolic group that is neither residually finite nor linear over any field

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question negatively. One fixed nonidentity element is killed by every finite-dimensional linear representation over every commutative field, so the group is not linear over any such field.

## A torsion-free hyperbolic group that is not residually finite

We construct a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question for hyperbolic groups negatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The residual-finiteness question for hyperbolic groups asks whether every nonidentity element survives in some finite quotient. The formalized result gives a negative answer by constructing a torsion-free word-hyperbolic group that is not residually finite.

Nonlinearity over every field is not a separate conclusion of the statement linked below.

## Lean: Torsion-free hyperbolic group that is not residually finite

```lean
theorem main : ∃ (G : Type) (_ : Group G),
    TorsionFree G ∧ WordHyperbolic G ∧ ¬ Group.ResiduallyFinite G
```

Stated in [TorsionFreeHyperbolic.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TorsionFreeHyperbolic.lean#L37). Proved in [lean/OAI/GroupTheory/Hyperbolic/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/Hyperbolic/Main.lean#L7). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/252.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/252.md)
