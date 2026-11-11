---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.PetersenMatchingWanted.petersen_bridgeless_cubic_has_perfect_matching_general, MathlibExt.Combinatorics.SimpleGraph.PetersenMatchingWanted.petersen_bridgeless_cubic_has_perfect_matching
statement: formalized
proof: formalized
---

# Petersen's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/petersen-s-theorem/index.html).

## Petersen's theorem on cubic graphs

Every finite simple graph that is $3$-regular
and has no bridge, that is, no edge whose removal disconnects its endpoints, has a perfect
matching: a set of edges of the graph such that every vertex lies on exactly one of them.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PetersenMatchingWanted.petersen_bridgeless_cubic_has_perfect_matching_general`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/PetersenMatching.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/PetersenMatching.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/petersen-s-theorem/index.html#petersen-bridgeless-cubic-has-perfect-ma).

## Petersen's perfect matching theorem

Every finite simple graph that is $3$-regular and
has no bridge, that is, no edge whose removal disconnects its endpoints, has a perfect
matching: a set of edges of the graph such that every vertex lies on exactly one of them.

## Sources

- J. Petersen, "Die Theorie der regulären graphs", Acta Mathematica 15 (1891), 193-220, DOI 10.1007/BF02392606. It follows from `petersen_bridgeless_cubic_has_perfect_matching_general`; the instance `[DecidableEq V]` is unused and keeps the source's shape.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PetersenMatchingWanted.petersen_bridgeless_cubic_has_perfect_matching`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/PetersenMatching.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/PetersenMatching.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/petersen-s-theorem/index.html#petersen-bridgeless-cubic-has-perfect-ma-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Petersen's theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/petersen-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/matchings-and-flows/petersen-s-theorem)
