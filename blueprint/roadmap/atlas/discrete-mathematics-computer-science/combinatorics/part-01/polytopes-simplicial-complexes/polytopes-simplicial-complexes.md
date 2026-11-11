---
declaration: section
origin: cited
lean: MetaMathlibExt.ordinaryEhrhartCount
statement: formalized
proof: formalized
---

# Polytopes, Ehrhart theory and simplicial complexes: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/index.html).

Face numbers and h-vectors of simplicial spheres and polytopes (Dehn–Sommerville, upper bound theorem), Cohen–Macaulay, partitionable and interval-decomposable complexes, simplicial homology, Ehrhart polynomials, h*-vectors and the integer decomposition property, lattice parallelograms, and hyperplane arrangements.

## Ordinary Ehrhart count

For a natural number $d$, a set $P \subseteq \mathbb{Q}^d$ and a
natural number $m$, the ordinary Ehrhart count is the number $|mP \cap \mathbb{Z}^d|$ of integer
points in the dilate $mP = \{m x : x \in P\}$, where $\mathbb{Z}^d$ is viewed inside
$\mathbb{Q}^d$; it is $0$ when $mP \cap \mathbb{Z}^d$ is infinite.

For polytopes the intersection is finite.

## Sources

- Ryuichi Sakamoto, "The h*-Polynomial of the Cut Polytope of K_{2,m} in the Lattice Spanned by its Vertices," Journal of Integer Sequences 23 (2020), Article 20.7.5.

Formalized by `MetaMathlibExt.ordinaryEhrhartCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OrdinaryEhrhartCount.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/OrdinaryEhrhartCount.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/index.html#ordinary-ehrhart-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polytopes, Ehrhart theory and simplicial complexes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes)
