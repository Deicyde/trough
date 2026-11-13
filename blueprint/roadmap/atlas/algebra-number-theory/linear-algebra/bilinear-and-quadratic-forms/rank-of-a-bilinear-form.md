---
declaration: section
origin: cited
lean: LinearMap.BilinForm.rank_toMatrix_eq_rank_toMatrix, MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank, MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank_eq_matrix_rank, MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank_basis_independent
statement: formalized
proof: formalized
---

# Rank of a bilinear form

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html).

## Bilin Form

## The Gram matrices of a bilinear form in two bases have the same rank

Let $V$ be a vector
space over a field $K$, let $B$ be a bilinear form on $V$, and let $b = (b_i)_{i \in n_1}$ and
$c = (c_j)_{j \in n_2}$ be bases of $V$ indexed by finite types $n_1$ and $n_2$. Then the Gram
matrices $(B(b_i, b_j))_{i, j \in n_1}$ and $(B(c_i, c_j))_{i, j \in n_2}$ have the same rank.

Formalized by `LinearMap.BilinForm.rank_toMatrix_eq_rank_toMatrix`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearFormRank.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearFormRank.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html#rank-to-matrix-eq-rank-to-matrix).

## Rank of a bilinear form

Let $V$ be a vector space over a field $K$, let $B$ be a bilinear
form on $V$, and let $b = (b_i)_{i \in n}$ be a basis of $V$ indexed by a finite type $n$. The
rank of $B$ with respect to $b$ is the rank of the Gram matrix $(B(b_i, b_j))_{i, j \in n}$ of $B$
in $b$.

By the basis independence theorem, this number does not depend on the choice of $b$.

## Sources

- N. Bourbaki, Algebra I, Chapters 1-3, Springer (1989), Chapter III.

Formalized by `MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank`, a definition declared in [MathlibExt/LinearAlgebra/BilinearFormRank.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearFormRank.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html#bilin-form-rank).

## Rank of a bilinear form via its Gram matrix

Let $V$ be a vector space over a field $K$, let
$B$ be a bilinear form on $V$, and let $b = (b_i)_{i \in n}$ be a basis of $V$ indexed by a finite
type $n$. Then the rank of $B$ with respect to $b$ equals the rank of the Gram matrix
$(B(b_i, b_j))_{i, j \in n}$. This holds by definition.

## Sources

- N. Bourbaki, Algebra I, Chapters 1-3, Springer (1989), Chapter III.

Formalized by `MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank_eq_matrix_rank`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearFormRank.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearFormRank.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html#bilin-form-rank-eq-matrix-rank).

## Basis independence of the rank of a bilinear form

Let $V$ be a vector space over a field
$K$, let $B$ be a bilinear form on $V$, and let $b = (b_i)_{i \in n_1}$ and
$c = (c_j)_{j \in n_2}$ be bases of $V$ indexed by finite types $n_1$ and $n_2$. Then the rank of
$B$ with respect to $b$ equals the rank of the Gram matrix $(B(c_i, c_j))_{i, j \in n_2}$ of $B$
in $c$.

Proof: The Gram matrix in one basis is the Gram matrix in the other multiplied on both sides by
change-of-basis matrices. Since the rank of a product is at most the rank of each factor, each
rank is at most the other, hence they are equal.

## Sources

- N. Bourbaki, Algebra I, Chapters 1-3, Springer (1989), Chapter III.

Formalized by `MathlibExt.LinearAlgebra.BilinearFormRankWanted.bilinFormRank_basis_independent`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearFormRank.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearFormRank.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html#bilin-form-rank-basis-independent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rank of a bilinear form](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/rank-of-a-bilinear-form)
