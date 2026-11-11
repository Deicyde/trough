---
declaration: section
origin: cited
lean: MathlibExt.Topology.HouseWithTwoRoomsWanted.Topology.HouseWithTwoRooms, MathlibExt.Topology.HouseWithTwoRoomsWanted.Topology.contractibleSpace_houseWithTwoRooms
statement: formalized
---

# Bing's house with two rooms

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/bing-s-house-with-two-rooms/index.html).

## Bing's house with two rooms

Bing's house with two rooms, in the version drawn in
Hatcher's *Algebraic Topology*, is the subset $H$ of $\mathbb{R} \times \mathbb{R} \times
\mathbb{R}$ consisting of the points of $[0,4] \times [0,3] \times \{0,1,2\}$ that lie in none of
$(2,3) \times (1,2) \times \{0\}$, $(1,3) \times (1,2) \times \{1\}$ and
$(1,2) \times (1,2) \times \{2\}$ (three floors with holes), together with the inner walls
$\{1\} \times [1,2] \times [1,2]$, $\{2\} \times [1,3] \times [0,2]$,
$\{3\} \times [1,2] \times [0,1]$, $[1,2] \times \{1,2\} \times [1,2]$ and
$[2,3] \times \{1,2\} \times [0,1]$, and the outer walls $[0,4] \times \{0,3\} \times [0,2]$ and
$\{0,4\} \times [0,3] \times [0,2]$.

Formalized by `MathlibExt.Topology.HouseWithTwoRoomsWanted.Topology.HouseWithTwoRooms`, a definition declared in [WantedExt/Topology/HouseWithTwoRoomsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HouseWithTwoRoomsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/bing-s-house-with-two-rooms/index.html#house-with-two-rooms).

## Bing's house with two rooms is contractible

Bing's house with two rooms, regarded as a
subspace of $\mathbb{R} \times \mathbb{R} \times \mathbb{R}$, is contractible.

## Sources

- Allen Hatcher, *Algebraic Topology*. Problem `contractibleSpace_houseWithTwoRooms` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.HouseWithTwoRoomsWanted.Topology.contractibleSpace_houseWithTwoRooms` is written with `theorem_wanted` in [WantedExt/Topology/HouseWithTwoRoomsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HouseWithTwoRoomsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/bing-s-house-with-two-rooms/index.html#contractible-space-house-with-two-rooms).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bing's house with two rooms](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/bing-s-house-with-two-rooms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/algebraic-topology/bing-s-house-with-two-rooms)
