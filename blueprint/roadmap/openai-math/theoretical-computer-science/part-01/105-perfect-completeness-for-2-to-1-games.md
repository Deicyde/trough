---
declaration: section
origin: cited
lean: OAI.PerfectCompleteness.Theorem11.exists_reduction
statement: formalized
proof: formalized
---

# 105. Perfect completeness for 2-to-1 games

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Khot's 2-to-1 Games Conjecture with perfect completeness: for every fixed rational $\delta\in(0,1)$, it is NP-hard to distinguish satisfiable games from games whose optimum is at most *δ*, on explicit unweighted instances. The alphabet depends only on *δ*, and every right-hand label has exactly two preimages under each constraint map.

## Perfect completeness for 2-to-1 games

We prove the 2-to-1 Games Conjecture with perfect completeness. For every fixed rational $\delta\in(0,1)$, it is NP-hard to distinguish satisfiable 2-to-1 games from games of value at most *δ*, with a fixed alphabet and an explicitly listed unweighted multiset of constraints.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result establishes perfect-completeness hardness for 2-to-1 games. For every fixed rational $0<\delta<1$, a deterministic polynomial-time reduction from binary 3SAT produces a nonempty unweighted game of value exactly $1$ on satisfiable inputs and at most $\delta$ on unsatisfiable inputs. Each constraint projection has exactly two preimages for each output label. The alphabet depends only on $\delta$, and the runtime is measured in the original input bit length.

## Lean: Perfect-completeness reduction for 2-to-1 games

Stated in [PerfectCompleteness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PerfectCompleteness.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_reduction (δ : ℚ) (positive : 0 < δ) (less_than_one : δ < 1) :
    Nonempty (PerfectCompleteness.BinaryGapReduction δ)
```

Proved in [lean/OAI/Computability/PerfectCompleteness/Theorem11.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/PerfectCompleteness/Theorem11.lean#L21).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/105.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/105.md)
