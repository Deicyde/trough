---
declaration: theorem
origin: cited
lean: Cayley.gap_core
statement: formalized
proof: formalized
---

# Gap core

Let $X$ be an admissible point of a box in chart $j$, let $S$ be an inner vertex and $w \ne 0$. Suppose that for every outer vertex $T$, either

$$
\mathrm{err} \le D_o\, \kappa_j\, D_r \bigl(\langle w, s Q_j(r) \hat S\rangle - \langle w, s \hat T\rangle\bigr),
$$

or $j \in \{0, 4\}$, $T = \sigma(S)$ and $\mathrm{err} \le 2 \hat L(X)$, where $\hat L$ is $L$ computed with $\hat S$. Then $\bigl(s, s\, Q_j(r)\bigr)$ is not a Rupert pair.

## Depends on

- [Separation criterion](../../rupert-pairs/shadows-and-the-separation-criterion/thm-separation.md)
- [Gap polynomial](../the-gap-polynomial/lem-gap-poly.md)
- [Blow-up identity](lem-blowup-identity.md)
- [vertex_approx](../../irrational-data/lem-vertex-approx.md)

## Proof

In both cases the true gap $\mathrm{gap}_T(X)$ is nonnegative once the approximation error is accounted for, so the separation criterion (Theorem [Separation criterion](../../rupert-pairs/shadows-and-the-separation-criterion/thm-separation.md)) applies with the inner vertex $S$ and direction $w$.

## Lean

Formalized as [`Cayley.gap_core`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.gap_core).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 127](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L127)
