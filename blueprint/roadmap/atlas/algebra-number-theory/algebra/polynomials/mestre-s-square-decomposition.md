---
declaration: section
origin: cited
lean: MetaMathlibExt.mestre_monic_square_decomposition_general, MetaMathlibExt.mestre_monic_square_decomposition
statement: formalized
proof: formalized
---

# Mestre's square decomposition

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mestre-s-square-decomposition/index.html).

## Mestre's square decomposition, including the quadratic case

Let $K$ be a field of
characteristic different from $2$ and let $d \ge 0$ be an integer. Every monic polynomial
$P \in K[X]$ of degree $2d + 2$ can be written as $P = Q^2 - R$ with $Q, R \in K[X]$, $Q$ monic
of degree $d + 1$ and $R$ of degree at most $d$ (possibly $R = 0$), and the pair $(Q, R)$ is
unique.

## Sources

- `mestre_monic_square_decomposition` is the source-shaped form, which assumes $d \ge 1$.

Formalized by `MetaMathlibExt.mestre_monic_square_decomposition_general`, a theorem declared in [MathlibExt/Algebra/Polynomial/MestreSquareDecomposition.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/MestreSquareDecomposition.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mestre-s-square-decomposition/index.html#mestre-monic-square-decomposition-genera).

## Mestre's square decomposition

Let $K$ be a field of characteristic different from $2$
and let $d \ge 1$ be an integer. Every monic polynomial $P \in K[X]$ of degree $2d + 2$ can be
written as $P = Q^2 - R$ with $Q, R \in K[X]$, $Q$ monic of degree $d + 1$ and $R$ of degree at
most $d$ (possibly $R = 0$), and the pair $(Q, R)$ is unique.

## Sources

- Arvind Suresh, "Constructing curves of high rank via composite polynomials", arXiv:2102.02113v2, <https://arxiv.org/abs/2102.02113>, TeX lines 1158-1179, Lemma `lem:sqroot`; there coefficient comparison induces a `k`-algebra isomorphism. Follows from `mestre_monic_square_decomposition_general`; the hypothesis `hd` is unused and keeps the source's shape.

Formalized by `MetaMathlibExt.mestre_monic_square_decomposition`, a theorem declared in [MathlibExt/Algebra/Polynomial/MestreSquareDecomposition.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/MestreSquareDecomposition.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mestre-s-square-decomposition/index.html#mestre-monic-square-decomposition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mestre's square decomposition](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mestre-s-square-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/mestre-s-square-decomposition)
