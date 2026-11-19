---
declaration: theorem
origin: cited
lean: Cayley.Pack.bern_real, Cayley.Pack.bernGE_le
statement: formalized
proof: formalized
---

# Bernstein bound

If every Bernstein coefficient of $p$ is at least $m$, then $p(t) \ge m$ for all $t \in [-1,1]^5$.

## Depends on

- [bernstein](def-bernstein.md)

## Proof

$p(t) = \sum_\kappa b_\kappa \prod_i \beta_{\kappa_i}(t_i)$, a convex combination of the Bernstein coefficients.

## Lean

Formalized as [`Cayley.Pack.bern_real`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.bern_real), [`Cayley.Pack.bernGE_le`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.bernGE_le).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 67](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L67)
