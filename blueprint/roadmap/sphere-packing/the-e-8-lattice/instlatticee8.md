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

- [Sphere packing in dimension 8 blueprint: subsections/E8-defs.tex, line 87](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/E8-defs.tex#L87)
