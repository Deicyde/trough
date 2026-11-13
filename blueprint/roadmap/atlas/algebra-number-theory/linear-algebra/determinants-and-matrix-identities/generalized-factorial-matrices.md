---
declaration: section
origin: cited
lean: MetaMathlibExt.pan_vandermonde_general, MetaMathlibExt.pan_vandermonde
statement: formalized
proof: formalized
---

# Generalized factorial matrices

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/generalized-factorial-matrices/index.html).

## Generalized factorial matrices: decomposition, determinant and inverse

Let $K$ be
$\mathbb{R}$ or $\mathbb{C}$, let $p$ be a natural number, let $x_0, \dots, x_{p-1} \in K$ be
pairwise distinct, and let $\alpha, \beta, \gamma \in \mathbb{R}$. For $y \in K$,
$a \in \mathbb{R}$ and $n \in \mathbb{N}$ write $(y \mid a)_n = \prod_{j=0}^{n-1} (y - ja)$.
Let numbers $S(a, b, c; n, k) \in K$, for $a, b, c \in \mathbb{R}$ and $n, k \in \mathbb{N}$,
satisfy $S(a, b, c; n, k) = 0$ whenever $k > n$, and
$(y \mid a)_n = \sum_{k=0}^{n} S(a, b, c; n, k)\,(y - c \mid b)_k$ for all
$a, b, c \in \mathbb{R}$, $y \in K$ and $n \in \mathbb{N}$. For $a, b, c \in \mathbb{R}$ let
$\mathbf{S}(a, b, c)$ be the $p \times p$ matrix with entries $S(a, b, c; i, k)$, let $G_a$
be the $p \times p$ matrix with entries $(x_k \mid a)_i$, and let $H$ be the $p \times p$
matrix with entries $(x_k - \gamma \mid \beta)_i$, where $0 \le i, k < p$. Then
$G_\alpha = \mathbf{S}(\alpha, \beta, \gamma)\, H$; $\det G_\alpha = \det G_0$;
$\det G_0 = \prod_{0 \le i < k < p} (x_k - x_i)$; $G_\alpha$ is invertible; and
$G_\alpha^{-1} = G_0^{-1}\, \mathbf{S}(0, \alpha, 0)$.

This holds for every $p$, including $p = 0$.

Formalized by `MetaMathlibExt.pan_vandermonde_general`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PanVandermonde.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PanVandermonde.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/generalized-factorial-matrices/index.html#pan-vandermonde-general).

## Pan's theorem on generalized factorial matrices

Let $K$ be $\mathbb{R}$ or $\mathbb{C}$,
let $p$ be a positive integer, let $x_0, \dots, x_{p-1} \in K$ be pairwise distinct, and let
$\alpha, \beta, \gamma \in \mathbb{R}$. For $y \in K$, $a \in \mathbb{R}$ and $n \in \mathbb{N}$
write $(y \mid a)_n = \prod_{j=0}^{n-1} (y - ja)$. Let numbers $S(a, b, c; n, k) \in K$, for
$a, b, c \in \mathbb{R}$ and $n, k \in \mathbb{N}$, satisfy $S(a, b, c; n, k) = 0$ whenever
$k > n$, and $(y \mid a)_n = \sum_{k=0}^{n} S(a, b, c; n, k)\,(y - c \mid b)_k$ for all
$a, b, c \in \mathbb{R}$, $y \in K$ and $n \in \mathbb{N}$. For $a, b, c \in \mathbb{R}$ let
$\mathbf{S}(a, b, c)$ be the $p \times p$ matrix with entries $S(a, b, c; i, k)$, let $G_a$
be the $p \times p$ matrix with entries $(x_k \mid a)_i$, and let $H$ be the $p \times p$
matrix with entries $(x_k - \gamma \mid \beta)_i$, where $0 \le i, k < p$. Then
$G_\alpha = \mathbf{S}(\alpha, \beta, \gamma)\, H$; $\det G_\alpha = \det G_0$;
$\det G_0 = \prod_{0 \le i < k < p} (x_k - x_i)$; $G_\alpha$ is invertible; and
$G_\alpha^{-1} = G_0^{-1}\, \mathbf{S}(0, \alpha, 0)$.

## Sources

- Jiaqiang Pan, "Matrix Decomposition of the Unified Generalized Stirling Numbers and Inversion of the Generalized Factorial Matrices," Journal of Integer Sequences 15 (2012), Article 12.6.6, Theorem, lines 428–460, https://cs.uwaterloo.ca/journals/JIS/VOL15/Pan/pan19.tex. It follows from `pan_vandermonde_general`; the hypothesis `hp` is unused and keeps the source's shape.

Formalized by `MetaMathlibExt.pan_vandermonde`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PanVandermonde.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PanVandermonde.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/generalized-factorial-matrices/index.html#pan-vandermonde).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized factorial matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/generalized-factorial-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities/generalized-factorial-matrices)
