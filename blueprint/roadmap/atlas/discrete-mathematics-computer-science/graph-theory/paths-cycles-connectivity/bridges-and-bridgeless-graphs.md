---
declaration: section
origin: cited
lean: SimpleGraph.IsBridgeless, SimpleGraph.isBridgeless_iff, SimpleGraph.IsBridgeless.mk, SimpleGraph.IsBridgeless.not_isBridge, SimpleGraph.isBridgeless_bot
statement: formalized
proof: formalized
---

# Bridges and bridgeless graphs

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html).

## Bridgeless graph

A simple graph is bridgeless when no edge is a bridge.

Formalized by `SimpleGraph.IsBridgeless`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean, line 18](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean#L18). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html#is-bridgeless).

## Characterization of bridgeless graphs

A simple graph $G$ is bridgeless if and only if no
edge of $G$ is a bridge.

Formalized by `SimpleGraph.isBridgeless_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html#is-bridgeless-iff).

## Bridgeless from non-bridge edges

If no edge of a simple graph $G$ is a bridge, then $G$ is
bridgeless.

Formalized by `SimpleGraph.IsBridgeless.mk`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html#mk).

## Edges of a bridgeless graph are not bridges

Every edge of a bridgeless graph is not a
bridge.

Formalized by `SimpleGraph.IsBridgeless.not_isBridge`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html#not-is-bridge).

## The edgeless graph is bridgeless

The edgeless graph on any vertex set is vacuously
bridgeless.

Formalized by `SimpleGraph.isBridgeless_bot`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Bridgeless.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html#is-bridgeless-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bridges and bridgeless graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/paths-cycles-connectivity/bridges-and-bridgeless-graphs)
