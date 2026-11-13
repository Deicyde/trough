---
declaration: section
origin: cited
lean: MetaMathlibExt.stieltjesMatrix, MetaMathlibExt.stieltjesMatrixOf
statement: formalized
proof: formalized
---

# Stieltjes production matrices

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/stieltjes-production-matrices/index.html).

## Tridiagonal Stieltjes production matrix

Let $R$ be an additive monoid with one and let
$a_1, b_1, a, b \in R$. The Stieltjes matrix $S$ is the infinite matrix with rows and columns
indexed by $\mathbb{N} = \{0, 1, 2, \dots\}$ whose entries are $S_{i, i+1} = 1$ for every $i$,
$S_{0,0} = a_1$, $S_{1,0} = b_1$, $S_{i,i} = a$ and $S_{i+1,i} = b$ for every $i \ge 1$, and
$S_{i,j} = 0$ for all other $i, j$. So row $0$ is $a_1, 1, 0, \dots$, row $1$ is
$b_1, a, 1, 0, \dots$, and each row $i \ge 2$ has $b$ below the diagonal, $a$ on the diagonal, $1$
above the diagonal and $0$ elsewhere.

Formalized by `MetaMathlibExt.stieltjesMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/StieltjesMatrix.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/StieltjesMatrix.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/stieltjes-production-matrices/index.html#stieltjes-matrix).

## Specialized Stieltjes matrix

Let $R$ be an additive monoid with one and let
$a, b, \lambda, \mu \in R$. The specialized Stieltjes matrix is the tridiagonal Stieltjes
production matrix with $a_1 = a + \lambda$, $b_1 = b + \mu$ and the same $a$ and $b$: the infinite
matrix $S$ with rows and columns indexed by $\mathbb{N} = \{0, 1, 2, \dots\}$ whose entries are
$S_{i, i+1} = 1$ for every $i$, $S_{0,0} = a + \lambda$, $S_{1,0} = b + \mu$, $S_{i,i} = a$ and
$S_{i+1,i} = b$ for every $i \ge 1$, and $S_{i,j} = 0$ for all other $i, j$.

This specialization corresponds to the inverse Riordan pair with numerator
$1 - \lambda x - \mu x^2$ over $1 + a x + b x^2$.

Formalized by `MetaMathlibExt.stieltjesMatrixOf`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/StieltjesMatrix.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/StieltjesMatrix.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/stieltjes-production-matrices/index.html#stieltjes-matrix-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stieltjes production matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/stieltjes-production-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/stieltjes-production-matrices)
