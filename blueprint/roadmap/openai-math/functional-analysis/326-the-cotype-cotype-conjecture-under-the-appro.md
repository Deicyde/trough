---
declaration: section
origin: cited
lean: OAI.Cotype.mainTarget_proved
statement: formalized
proof: formalized
---

# 326. The cotype–cotype conjecture under the approximation property

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the cotype–cotype conjecture for real Banach spaces with the approximation property. Such a nonzero space is *K*-convex if and only if both it and its dual have finite Rademacher cotype, with possibly different exponents. Equivalently, these cotype assumptions force nontrivial Rademacher type.

## The cotype–cotype conjecture under the approximation property

We prove the cotype–cotype conjecture under the ordinary approximation property. A nonzero real Banach space with this property is *K*-convex if and only if both the space and its dual have finite Rademacher cotype, possibly with different exponents.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The cotype–cotype problem asks whether finite cotype of a Banach space and its dual characterizes $K$-convexity. The formalized result establishes this equivalence for every nonzero real Banach space with the approximation property: $X$ is $K$-convex exactly when both $X$ and $X^*$ have finite cotype.

## Lean: Cotype–cotype equivalence with approximation property

Stated in [Cotype.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Cotype.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem mainTarget_proved [Nontrivial X] : MainTarget X
```

Proved in [lean/OAI/Analysis/Cotype/Main.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Cotype/Main.lean#L26).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/326.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/326.md)
