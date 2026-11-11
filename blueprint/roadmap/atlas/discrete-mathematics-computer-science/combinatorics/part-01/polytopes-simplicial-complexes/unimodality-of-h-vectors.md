---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.latticePolytope, MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.hibiSymmetricUnimodal, MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.hibiSymmetricUnimodal_refuted
statement: formalized
---

# Unimodality of h\*-vectors

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors/index.html).

## Lattice polytope spanned by integer points

The lattice polytope in `ℝ^d` spanned by the finite set `S ⊆ ℤ^d` of integer points.

Formalized by `MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.latticePolytope`, a definition declared in [WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors/index.html#lattice-polytope).

## Hibi's conjecture on symmetric $h^*$-vectors

**Hibi's conjecture on symmetric $h^*$-vectors.** For every natural number $d$, every finite
set $S \subseteq \mathbb{Z}^d$ whose convex hull $P \subseteq \mathbb{R}^d$ has nonempty interior,
and every polynomial $h = \sum_i h^*_i z^i \in \mathbb{Z}[z]$ that is an $h^*$-polynomial of $P$,
that is,

$$\Big(\sum_{t \ge 0} \#(tP \cap \mathbb{Z}^d)\, z^t\Big) (1 - z)^{d+1} = h(z)$$

as formal power series, if $h^*_i = h^*_{d-i}$ for all $0 \le i \le d$, then $h$ is unimodal.

This is Hibi's conjecture, Conjecture 2 of C. A. Athanasiadis's Oberwolfach report (Oberwolfach
Reports 1 (2004), no. 39, p. 2078), stated there for $d$-dimensional integral polytopes; every
such polytope is lattice-equivalent to a full-dimensional lattice polytope in $\mathbb{R}^d$.

Formalized by `MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.hibiSymmetricUnimodal`, a definition declared in [WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors/index.html#hibi-symmetric-unimodal).

## Hibi's conjecture on symmetric $h^*$-vectors is false

**Hibi's conjecture on symmetric $h^*$-vectors is false.** There are a natural number $d$, a
finite set $S \subseteq \mathbb{Z}^d$ whose convex hull $P \subseteq \mathbb{R}^d$ has nonempty
interior, and a polynomial $h = \sum_i h^*_i z^i \in \mathbb{Z}[z]$ that is an $h^*$-polynomial
of $P$, that is,

$$\Big(\sum_{t \ge 0} \#(tP \cap \mathbb{Z}^d)\, z^t\Big) (1 - z)^{d+1} = h(z)$$

as formal power series, such that $h^*_i = h^*_{d-i}$ for all $0 \le i \le d$ but $h$ is not
unimodal.

Mustaţă and Payne (Example 1.1) give a reflexive $6$-dimensional lattice polytope with
$h^*$-vector $(1, 6, 8, 6, 8, 6, 1)$, which is symmetric and not unimodal.

## Sources

- C. A. Athanasiadis, On the unimodality of h*-vectors, in Ehrhart Quasipolynomials: Algebra, Combinatorics, and Geometry, Oberwolfach Reports 1 (2004), no. 39, p. 2078, Conjecture 2, DOI 10.4171/OWR/2004/39; resolution: M. Mustaţă and S. Payne, Ehrhart polynomials and stringy Betti numbers, Math. Ann. 333 (2005), 787-795, DOI 10.1007/s00208-005-0691-x, arXiv:math/0504486, Example 1.1: for f = (e1 + ... + e6)/3, N = ℤ⁶ + ℤ f and P the polytope with vertices e1, ..., e6, e1 - f, ..., e6 - f, P is reflexive with δ_P = (1, 6, 8, 6, 8, 6, 1), a counterexample to Hibi's conjecture for d = 6 (abstract: 'counterexamples to Hibi's conjecture on the unimodality of delta-vectors of reflexive polytopes'), https://arxiv.org/abs/math/0504486.

Stated but not proved: `MathlibExt.Combinatorics.HibiSymmetricHStarUnimodalOWR741Problem003Wanted.hibiSymmetricUnimodal_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HibiSymmetricHStarUnimodalOWR741Problem003Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors/index.html#hibi-symmetric-unimodal-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unimodality of h*-vectors](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/unimodality-of-h-vectors)
