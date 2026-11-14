---
declaration: lemma
origin: cited
lean: instIsZLatticeE8Lattice
statement: formalized
proof: formalized
---

# instLatticeE8

$c\Lambda_8$ is a $\mathbb{Z}$-lattice, i.e. it is discrete and spans $\mathbb{R}^8$ over $\mathbb{R}$.

## Depends on

- [instDiscreteE8Lattice](instdiscretee8lattice.md)
- [E8-is-basis](e8-is-basis.md)

## Proof

The first part is by [Lemma instDiscreteE8Lattice](instdiscretee8lattice.md), and the second part follows from that $\mathcal{B}_8$ is a basis ([Lemma E8-is-basis](e8-is-basis.md)) and hence linearly independent over $\mathbb{R}$.

## Lean

Formalized as [`instIsZLatticeE8Lattice`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/instIsZLatticeE8Lattice).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/E8-defs.tex, line 87](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/E8-defs.tex#L87)
