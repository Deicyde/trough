---
declaration: section
origin: cited
lean: MetaMathlibExt.inner_toEuclideanLin_self_eq_sum, MetaMathlibExt.trace_mul_eq_sum_eigenvalues, MetaMathlibExt.overlap_mem_doublyStochastic, MetaMathlibExt.exists_perm_sum_le_of_mem_doublyStochastic, MetaMathlibExt.exists_perm_sum_mul_eigenvalues_le_trace_mul, MetaMathlibExt.exists_perm_trace_mul_le_sum_mul_eigenvalues
statement: formalized
proof: formalized
---

# Von Neumann's trace inequality

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html).

## The quadratic form of a symmetric matrix in an orthonormal eigenbasis

Let $B$ be a real
symmetric matrix with rows and columns indexed by a finite set $I$, and let $(v_j)_{j \in I}$ be
the orthonormal basis of $\mathbb{R}^I$ of eigenvectors of $B$ chosen by the spectral theorem,
with $B v_j = \beta_j v_j$. Then for every $x \in \mathbb{R}^I$,
$\langle x, Bx \rangle = \sum_j \beta_j \langle v_j, x \rangle^2$.

Formalized by `MetaMathlibExt.inner_toEuclideanLin_self_eq_sum`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#inner-to-euclidean-lin-self-eq-sum).

## The trace of a product of symmetric matrices in their eigenbases

Let $A$ and $B$ be real
symmetric matrices with rows and columns indexed by a finite set $I$. Let $(u_i)_{i \in I}$ and
$(v_j)_{j \in I}$ be the orthonormal bases of $\mathbb{R}^I$ of eigenvectors of $A$ and $B$ chosen
by the spectral theorem, with $A u_i = \alpha_i u_i$ and $B v_j = \beta_j v_j$. Then
$\operatorname{tr}(AB) = \sum_i \sum_j \alpha_i \beta_j \langle v_j, u_i \rangle^2$.

Formalized by `MetaMathlibExt.trace_mul_eq_sum_eigenvalues`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#trace-mul-eq-sum-eigenvalues).

## The overlap matrix of two orthonormal bases is doubly stochastic

Let $I$ be a finite set
and let $(u_i)_{i \in I}$ and $(v_j)_{j \in I}$ be orthonormal bases of $\mathbb{R}^I$ with its
standard inner product. Then the $I \times I$ matrix with entries
$P_{ij} = \langle v_j, u_i \rangle^2$ is doubly stochastic: its entries are nonnegative and each
of its rows and columns sums to $1$.

Formalized by `MetaMathlibExt.overlap_mem_doublyStochastic`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#overlap-mem-doubly-stochastic).

## Linear functionals on doubly stochastic matrices are bounded below at a permutation

Let $I$ be a finite set, let $P$ be a doubly stochastic real $I \times I$ matrix (its entries are
nonnegative and each of its rows and columns sums to $1$), and let $c_{ij} \in \mathbb{R}$ for
$i, j \in I$. Then there is a permutation $\sigma$ of $I$ with
$\sum_i c_{i \sigma(i)} \le \sum_i \sum_j c_{ij} P_{ij}$. That is, the linear functional
$M \mapsto \sum_{i, j} c_{ij} M_{ij}$ takes a value at some permutation matrix that is at most its
value at $P$.

The proof uses Birkhoff's theorem.

Formalized by `MetaMathlibExt.exists_perm_sum_le_of_mem_doublyStochastic`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#exists-perm-sum-le-of-mem-doubly-stochas).

## A pairing of eigenvalues bounds the trace of a product from below

Let $A$ and $B$ be
real symmetric matrices with rows and columns indexed by a finite set $I$, and let
$(\alpha_i)_{i \in I}$ and $(\beta_i)_{i \in I}$ be their eigenvalues, listed with multiplicity.
Then there is a permutation $\sigma$ of $I$ with
$\sum_i \alpha_i \beta_{\sigma(i)} \le \operatorname{tr}(AB)$.

This is the lower half of von Neumann's trace inequality, in pairing form.

Formalized by `MetaMathlibExt.exists_perm_sum_mul_eigenvalues_le_trace_mul`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#exists-perm-sum-mul-eigenvalues-le-trace).

## A pairing of eigenvalues bounds the trace of a product from above

Let $A$ and $B$ be
real symmetric matrices with rows and columns indexed by a finite set $I$, and let
$(\alpha_i)_{i \in I}$ and $(\beta_i)_{i \in I}$ be their eigenvalues, listed with multiplicity.
Then there is a permutation $\sigma$ of $I$ with
$\operatorname{tr}(AB) \le \sum_i \alpha_i \beta_{\sigma(i)}$.

This is the upper half of von Neumann's trace inequality, in pairing form.

Formalized by `MetaMathlibExt.exists_perm_trace_mul_le_sum_mul_eigenvalues`, a theorem declared in [MathlibExt/Analysis/Matrix/TraceEigenvalues.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Matrix/TraceEigenvalues.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html#exists-perm-trace-mul-le-sum-mul-eigenva).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Von Neumann's trace inequality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/von-neumann-s-trace-inequality)
