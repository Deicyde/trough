---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.M23TensorSquareWanted.RepresentationTheory.m23_irrep_tensor_square_decomp
statement: formalized
---

# Characters of finite groups: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/index.html).

Complex characters and representations used to study finite groups: class functions and orthogonality, irreducible character bases, character degrees and values, McKay conjecture, rational groups, permutation characters, blocks of defect zero, Frobenius group determinant, convolution on finite groups, and Burnside's p^a q^b theorem; general representation theory of algebras and Lie groups belongs to RepresentationTheory.

## Four isotypic components in a tensor square for a simple group of order 10200960

There
exist a finite simple group $G$ of order $10200960$ and an irreducible complex representation
$\rho$ of $G$ on a vector space $V$ of dimension $22$ such that the tensor square $V \otimes V$,
regarded as a module over the group algebra $\mathbb{C}[G]$ through the diagonal action
$g \mapsto \rho(g) \otimes \rho(g)$, has exactly $4$ isotypic components.

## Sources

- É. Mathieu, Sur les fonctions cinq fois transitives de 24 quantités, J. Math. Pures Appl. (1873); ATLAS of Finite Groups, M₂₃ character table. Problem `m23_irrep_tensor_square_decomp` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.M23TensorSquareWanted.RepresentationTheory.m23_irrep_tensor_square_decomp` is written with `theorem_wanted` in [WantedExt/GroupTheory/M23TensorSquareWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/M23TensorSquareWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/index.html#m23-irrep-tensor-square-decomp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Characters of finite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups)
