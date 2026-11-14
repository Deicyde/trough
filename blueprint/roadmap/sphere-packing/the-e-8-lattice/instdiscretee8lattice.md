---
declaration: lemma
origin: cited
lean: instDiscreteE8Lattice
statement: formalized
proof: formalized
---

# instDiscreteE8Lattice

$c\Lambda_8$ is discrete, i.e. that the subspace topology induced by its inclusion into $\mathbb{R}^8$ is the discrete topology.

## Depends on

- [E8-vector-norms](e8-vector-norms.md)

## Proof

Since $\Lambda_8$ is a topological group and $+$ is continuous, it suffices to prove that $\{0\}$ is open in $\Lambda_8$. This follows from the fact that there is an open ball $\mathcal{B}(\sqrt{2}) \subseteq \mathbb{R}^8$ around it containing no other lattice points, since the shortest nonzero vector has norm $\sqrt{2}$.

## Lean

Formalized as [`instDiscreteE8Lattice`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/instDiscreteE8Lattice).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/E8-defs.tex, line 80](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/E8-defs.tex#L80)
