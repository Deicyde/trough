---
declaration: section
origin: cited
lean: OAI.ThompsonNonamenability.thompson_F_nonamenable_composition
statement: formalized
proof: formalized
---

# 248. Thompson's group \*F\* is nonamenable

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that Thompson's group *F*, the group of dyadic piecewise linear homeomorphisms of the interval, is nonamenable, resolving its longstanding amenability problem.

## Thompson's group F is nonamenable

We prove that Thompson's group *F* is nonamenable. This confirms Geoghegan's conjecture and resolves the amenability problem for *F*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The amenability problem for Thompson's group $F$ asks whether it admits a positive normalized left-invariant mean on bounded real functions. The formalized result rules out such a mean for the standard group of dyadic piecewise-linear homeomorphisms of the interval, proving nonamenability. No explicit boundary constant or prescribed generating set is given.

## Lean: Nonamenability of Thompson's group $F$

Stated in [ThompsonNonamenability.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThompsonNonamenability.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem thompson_F_nonamenable_composition :
    ∃ group : Group F, letI := group;
      (∀ (h g : F) (x : UnitInterval),
        (h * g).val.toHomeomorph x = h.val.toHomeomorph (g.val.toHomeomorph x)) ∧
      ¬ Nonempty (InvariantMean F)
```

Proved in [lean/OAI/GroupTheory/Thompson/Main.lean, line 69](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/Thompson/Main.lean#L69).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/248.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/248.md)
