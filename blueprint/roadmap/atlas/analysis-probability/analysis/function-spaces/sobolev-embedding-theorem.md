---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.HomogeneousSobolevHolderEmbeddingWanted.dotHSeminorm, MathlibExt.Analysis.Fourier.HomogeneousSobolevHolderEmbeddingWanted.exists_holderSeminorm_le_mul_dotHSeminorm, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.E, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.partialDeriv, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.mixedDeriv, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.IsWeakDeriv, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.MemSobolevWk, MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.MemHolder
statement: formalized
---

# Sobolev embedding theorem

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html).

## Homogeneous Sobolev seminorm for the Hölder embedding

For a real number $s$ and a
Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with Fourier transform
$\hat f(\xi) = \int_{\mathbb{R}} e^{-2\pi i x \xi} f(x) \, dx$, the homogeneous Sobolev seminorm
of $f$ is

$$
\|f\|_{\dot H^s} = \left( \int_{\mathbb{R}} |\xi|^{2s} \, |\hat f(\xi)|^2 \, d\xi \right)^{1/2},
$$

where the integral is taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.Fourier.HomogeneousSobolevHolderEmbeddingWanted.dotHSeminorm`, a definition declared in [WantedExt/Analysis/Fourier/HomogeneousSobolevHolderEmbeddingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/HomogeneousSobolevHolderEmbeddingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#dot-hseminorm).

## The homogeneous Sobolev seminorm controls the Hölder seminorm

Let $s \in (\tfrac12, 1]$,
and for a Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with Fourier transform $\hat f$ let
$\|f\|_{\dot H^s} = \left( \int_{\mathbb{R}} |\xi|^{2s} |\hat f(\xi)|^2 \, d\xi \right)^{1/2}$
be its homogeneous Sobolev seminorm. There is a constant $C_3 > 0$ such that for every Schwartz
function $f : \mathbb{R} \to \mathbb{C}$,

$$
\sup_{x \ne y} \frac{|f(x) - f(y)|}{|x - y|^{s - \frac12}} \le C_3 \, \|f\|_{\dot H^s}.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_21`.

Stated but not proved: `MathlibExt.Analysis.Fourier.HomogeneousSobolevHolderEmbeddingWanted.exists_holderSeminorm_le_mul_dotHSeminorm` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/HomogeneousSobolevHolderEmbeddingWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/HomogeneousSobolevHolderEmbeddingWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#exists-holder-seminorm-le-mul-dot-hsemin).

## Euclidean space $\mathbb{R}^n$

For a natural number $n$, $\mathbb{R}^n$ denotes the real
Euclidean space of dimension $n$: real vectors with coordinates indexed by $0, \dots, n-1$, with
the Euclidean inner product and norm.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.E`, an abbreviation declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#e).

## Partial derivative

For a coordinate index $i \in \{0, \dots, n-1\}$ and a function
$\varphi : \mathbb{R}^n \to \mathbb{R}$, the partial derivative $\partial_i \varphi$ is the
function $\mathbb{R}^n \to \mathbb{R}$ sending $x$ to $D\varphi(x)(e_i)$, the Fréchet derivative
of $\varphi$ at $x$ applied to the $i$-th standard basis vector $e_i$. At points where $\varphi$
is not differentiable its value is $0$.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.partialDeriv`, a definition declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#partial-deriv).

## Mixed partial derivative

For a multi-index $m = (m_0, \dots, m_{n-1})$ of natural numbers
and a function $\varphi : \mathbb{R}^n \to \mathbb{R}$, the mixed partial derivative is
$D^m \varphi = \partial_0^{m_0} \partial_1^{m_1} \cdots \partial_{n-1}^{m_{n-1}} \varphi$, where
$\partial_i^{j}$ is the $j$-fold iterate of the partial derivative $\partial_i$; thus
$\partial_{n-1}$ is applied first and $\partial_0$ last.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.mixedDeriv`, a definition declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#mixed-deriv).

## Weak derivative

Let $f, g : \mathbb{R}^n \to \mathbb{R}$ and let
$m = (m_0, \dots, m_{n-1})$ be a multi-index of order $|m| = m_0 + \cdots + m_{n-1}$. Then $g$ is
a weak derivative $D^m f$ of $f$ when every smooth ($C^\infty$) compactly supported function
$\varphi : \mathbb{R}^n \to \mathbb{R}$ satisfies

$$\int_{\mathbb{R}^n} f \, D^m \varphi \, dx = (-1)^{|m|} \int_{\mathbb{R}^n} g \, \varphi \, dx,$$

where $D^m \varphi$ is the classical mixed partial derivative and each integral is the Lebesgue
integral, taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.IsWeakDeriv`, a definition declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#is-weak-deriv).

## Sobolev space $W^{k,p}(\mathbb{R}^n)$

For a natural number $k$ and $p \in [0, \infty]$, a
function $f : \mathbb{R}^n \to \mathbb{R}$ belongs to $W^{k,p}(\mathbb{R}^n)$ when $f$ is locally
integrable and, for every multi-index $m = (m_0, \dots, m_{n-1})$ of natural numbers with
$m_0 + \cdots + m_{n-1} \le k$, $f$ has a weak derivative $D^m f$ that lies in
$L^p(\mathbb{R}^n)$. Local integrability and $L^p$ are with respect to Lebesgue measure.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.MemSobolevWk`, a definition declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#mem-sobolev-wk).

## Hölder space $C^{r,\alpha}(\mathbb{R}^n)$

For a natural number $r$ and a real number
$\alpha$, a function $g : \mathbb{R}^n \to \mathbb{R}$ belongs to $C^{r,\alpha}(\mathbb{R}^n)$ when
$g$ is $r$ times continuously differentiable, its iterated derivatives $D^j g$ for $j \le r$ are
bounded on $\mathbb{R}^n$, and its $r$-th derivative is $\alpha$-Hölder: there is $C \ge 0$ with
$\|D^r g(x) - D^r g(y)\| \le C \|x - y\|^{\alpha}$ for all $x, y \in \mathbb{R}^n$. Here
$D^j g(x)$ is the $j$-th Fréchet derivative of $g$ at $x$, a $j$-linear map measured in the
operator norm, and a negative $\alpha$ is replaced by $0$.

Formalized by `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.MemHolder`, a definition declared in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#mem-holder).

## Sobolev embedding theorem (Morrey regime)

Let $n, k, r$ be natural numbers and
$\alpha, p$ real numbers with $n < p$, $0 < \alpha \le 1$ and $r + \alpha < k - n/p$. Then every
function $f : \mathbb{R}^n \to \mathbb{R}$ in the Sobolev space $W^{k,p}(\mathbb{R}^n)$ is equal
almost everywhere, for Lebesgue measure, to some function $g$ in the Hölder space
$C^{r,\alpha}(\mathbb{R}^n)$.

## Sources

- C.B. Morrey, 'Functions of several variables and absolute continuity, II', Duke Math. J. 6 (1940) 187–215; full Sobolev-embedding development in *Multiple Integrals in the Calculus of Variations*, Springer 1966. Listed as §111 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `sobolev_embedding_morrey` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.SobolevMorreyWanted.Analysis.SobolevMorreyProblem.sobolev_embedding` is written with `theorem_wanted` in [WantedExt/Analysis/SobolevMorreyWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SobolevMorreyWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html#sobolev-embedding).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sobolev embedding theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sobolev-embedding-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/function-spaces/sobolev-embedding-theorem)
