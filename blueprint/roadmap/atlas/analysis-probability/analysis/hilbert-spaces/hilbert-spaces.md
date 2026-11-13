---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.OrthogonalPolynomialHilbertBasisWanted.orthogonalPolynomial_hilbertBasis
statement: formalized
---

# Hilbert spaces: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/index.html).

Geometry of inner product spaces: nearest-point projections, orthonormal and Hilbert bases, separability and ℓ², frames and Riesz bases, weak convergence (Opial, Radon–Riesz), Kirszbraun extension, derivatives of the norm, representer theorems; operators on Hilbert spaces go to Operator theory, analytic RKHS to Complex analysis.

## Hilbert basis of orthogonal polynomials on $(-1, 1)$

Let $L^2([-1, 1])$ be the real
Hilbert space of square-integrable real-valued functions on $[-1, 1]$ with respect to
Lebesgue measure. There is a Hilbert basis $(b_n)_{n \in \mathbb{N}}$ of $L^2([-1, 1])$ such
that for every $n \in \mathbb{N}$ there is a real polynomial $q_n$ of degree exactly $n$ (for
$n = 0$, a constant polynomial) with $b_n(x) = q_n(x)$ for almost every $x \in [-1, 1]$.

The normalized Legendre polynomials form such a basis.

## Sources

- NIST Digital Library of Mathematical Functions, §18.3, Table 18.3.1 (Legendre polynomials: weight `1` on `(-1, 1)`, `∫ P_n ^ 2 = 2 / (2n + 1)`).
- E. Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1978, §3.6 ("Total Orthonormal Sets and Sequences") and §3.7 ("Legendre, Hermite and Laguerre Polynomials": the normalized Legendre polynomials are a total orthonormal sequence in `L²[-1, 1]`).
- https://en.wikipedia.org/wiki/Legendre_polynomials#Orthogonality_and_completeness

Stated but not proved: `MathlibExt.Analysis.InnerProductSpace.OrthogonalPolynomialHilbertBasisWanted.orthogonalPolynomial_hilbertBasis` is written with `theorem_wanted` in [WantedExt/Analysis/InnerProductSpace/OrthogonalPolynomialHilbertBasisWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/InnerProductSpace/OrthogonalPolynomialHilbertBasisWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/index.html#orthogonal-polynomial-hilbert-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces)
