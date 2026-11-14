---
declaration: section
origin: cited
lean: OAI.HyperbolicObstruction.main
statement: formalized
proof: formalized
---

# 257. A hyperbolic group without a geometric CAT(0) action

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Answers negatively whether every word-hyperbolic group is a CAT(0) group. Constructs one with a finite classifying space but no proper cocompact isometric action on any proper complete $\mathop{\mathrm{CAT}}\nolimits (0)$ space, in any dimension.

## A hyperbolic group with no geometric CAT(0) action

We construct a hyperbolic group with a finite classifying space that admits no geometric action on a proper complete CAT(0) space. Consequently, a finite aspherical simplicial complex with a linear combinatorial disk-filling inequality need not have a finite locally CAT(0) homotopy model, and hence need not have a finite locally CAT(−1) model. Here metric models carry geodesic length metrics inducing the given complex topology.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result constructs a finite connected aspherical complex with a linear disk-filling bound whose fundamental group is word-hyperbolic but admits no geometric action on a nonempty proper complete $\mathrm{CAT}(0)$ space. It also excludes locally $\mathrm{CAT}(-1)$ geodesic metrics on every finite complex homotopy equivalent to the witness. The stronger claims that the witness is two-dimensional and that those models admit no locally $\mathrm{CAT}(0)$ metric are not included.

## Lean: Hyperbolic group with no geometric CAT(0) action

```lean
theorem main : MainStatement.{u}
```

Stated in [HyperbolicObstruction.lean, line 154](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HyperbolicObstruction.lean#L154). Proved in [lean/OAI/Geometry/HyperbolicGroups/Main.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/HyperbolicGroups/Main.lean#L15). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/257.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/257.md)
