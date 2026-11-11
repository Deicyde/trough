---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.PerronFrobeniusWanted.toComplexMatrix, Matrix.IsIrreducible.perron_frobenius, MathlibExt.LinearAlgebra.Matrix.PerronFrobeniusWanted.perron_frobenius
statement: formalized
proof: formalized
---

# Perron–Frobenius theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem/index.html).

## Complexification of a real matrix

For a real square matrix $A$ with rows and columns
indexed by a nonempty finite set $S$, its complexification $A_{\mathbb{C}}$ is the complex matrix
with entries $(A_{\mathbb{C}})_{ij} = A_{ij}$ for $i, j \in S$, each real entry viewed as a
complex number.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PerronFrobeniusWanted.toComplexMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem/index.html#to-complex-matrix).

## Perron–Frobenius theorem for irreducible nonnegative matrices

Let $A$ be a real square matrix
with rows and columns indexed by a nonempty finite set $S$, and suppose $A$ is irreducible: its
entries are nonnegative, and for all $i, j \in S$ there is a path $i = i_0, i_1, \dots, i_k = j$ of
length $k \ge 1$ with $A_{i_{t-1} i_t} > 0$ for every $t$. Then there are a real number $r > 0$ and
a vector $v \in \mathbb{R}^S$ with $v_i > 0$ for every $i \in S$ such that $Av = rv$, and every
complex number $\mu$ with $\det(\mu E - A_{\mathbb{C}}) = 0$ satisfies $|\mu| \le r$, where $E$ is
the identity matrix and $A_{\mathbb{C}}$ is the complex matrix with the same entries as $A$.

Formalized by `Matrix.IsIrreducible.perron_frobenius`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem/index.html#perron-frobenius).

## Perron–Frobenius theorem for nonzero irreducible nonnegative matrices

Let $A$ be a nonzero
real square matrix with rows and columns indexed by a nonempty finite set $S$, and suppose $A$ is
irreducible: its entries are nonnegative, and for all $i, j \in S$ there is a path
$i = i_0, i_1, \dots, i_k = j$ of length $k \ge 1$ with $A_{i_{t-1} i_t} > 0$ for every $t$. Then
there are a real number $r > 0$ and a vector $v \in \mathbb{R}^S$ with $v_i > 0$ for every
$i \in S$ such that $Av = rv$, and every complex number $\mu$ with
$\det(\mu E - A_{\mathbb{C}}) = 0$ satisfies $|\mu| \le r$, where $E$ is the identity matrix and
$A_{\mathbb{C}}$ is the complexification of $A$.

The hypothesis $A \ne 0$ is not needed: irreducibility already forces some entry to be positive.

## Sources

- O. Perron, Math. Ann. 64 (1907), 248-263, DOI 10.1007/BF01449896; G. Frobenius, S.-Ber. Preuss. Akad. Wiss. Berlin (1912), 456-477.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PerronFrobeniusWanted.perron_frobenius`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PerronFrobenius.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem/index.html#perron-frobenius-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perron–Frobenius theorem](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/perron-frobenius-theorem)
