---
declaration: section
origin: cited
lean: MetaMathlibExt.IsNuLambdaPascalMatrix, MetaMathlibExt.IsNuLambdaPascalMatrix.finite_support, MetaMathlibExt.IsNuLambdaPascalMatrix.skew, MetaMathlibExt.IsNuLambdaPascalMatrix.corner, MetaMathlibExt.IsNuLambdaPascalMatrix.last_column, MetaMathlibExt.IsNuLambdaPascalMatrix.interior
statement: formalized
proof: formalized
---

# Pascal-like matrices

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html).

## Nu-lambda Pascal matrix with coefficients

Let $N$ and $n$ be natural numbers with
$n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$.
An array $S = (S_{i,j})_{i,j \ge 0}$ of complex numbers, indexed from $0$, is a
$(\nu, \lambda)$-Pascal matrix of size $2n$ with coefficients $\beta$ when the following
hold: $S_{i,j} = 0$ whenever $i \ge 2n$ or $j \ge 2n$; $S_{i,j} = -S_{j,i}$ for all $i, j$;
$S_{2n-2,\,2n-1} = 1$; $S_{j,\,2n-1} = \sum_{t=0}^{N-1} \beta_t S_{j+t+1,\,2n-1}$ for every
$j < 2n - 2$; and $S_{i,j} = \lambda S_{i+1,j+1} + \nu (S_{i+1,j} + S_{i,j+1})$ for all
$i, j < 2n - 1$.

The definition also allows $N = 0$; then the sum is empty, so the entries $S_{j,\,2n-1}$
with $j < 2n - 2$ vanish. The intended coefficient families have $N > 0$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#is-nu-lambda-pascal-matrix).

## Finite support of a nu-lambda Pascal matrix

Let $N$ and $n$ be natural numbers
with $n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$,
and let $S = (S_{i,j})_{i,j \ge 0}$ be a $(\nu, \lambda)$-Pascal matrix of size $2n$ with
coefficients $\beta$. Then $S_{i,j} = 0$ for all $i, j$ with $i \ge 2n$ or
$j \ge 2n$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix.finite_support`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#finite-support).

## Nu-lambda Pascal matrices are skew-symmetric

Let $N$ and $n$ be natural numbers
with $n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$,
and let $S = (S_{i,j})_{i,j \ge 0}$ be a $(\nu, \lambda)$-Pascal matrix of size $2n$ with
coefficients $\beta$. Then $S_{i,j} = -S_{j,i}$ for all $i, j$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix.skew`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#skew).

## Corner entry of a nu-lambda Pascal matrix

Let $N$ and $n$ be natural numbers
with $n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$,
and let $S = (S_{i,j})_{i,j \ge 0}$ be a $(\nu, \lambda)$-Pascal matrix of size $2n$ with
coefficients $\beta$. Then $S_{2n-2,\,2n-1} = 1$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix.corner`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#corner).

## Last-column recurrence of a nu-lambda Pascal matrix

Let $N$ and $n$ be natural numbers
with $n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$,
and let $S = (S_{i,j})_{i,j \ge 0}$ be a $(\nu, \lambda)$-Pascal matrix of size $2n$ with
coefficients $\beta$. Then for every $j < 2n - 2$,
$S_{j,\,2n-1} = \sum_{t=0}^{N-1} \beta_t S_{j+t+1,\,2n-1}$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix.last_column`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#last-column).

## Interior recurrence of a nu-lambda Pascal matrix

Let $N$ and $n$ be natural numbers
with $n > 0$, let $\nu, \lambda \in \mathbb{C}$ and $\beta_0, \dots, \beta_{N-1} \in \mathbb{C}$,
and let $S = (S_{i,j})_{i,j \ge 0}$ be a $(\nu, \lambda)$-Pascal matrix of size $2n$ with
coefficients $\beta$. Then for all $i, j < 2n - 1$,
$S_{i,j} = \lambda S_{i+1,j+1} + \nu (S_{i+1,j} + S_{i,j+1})$.

Formalized by `MetaMathlibExt.IsNuLambdaPascalMatrix.interior`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NuLambdaPascalMatrix.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html#interior).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pascal-like matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/pascal-like-matrices)
