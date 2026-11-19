---
declaration: lemma
origin: cited
lean: Cayley.Pack.pLowerL_eq, Cayley.Pack.pStatsL_eq, Cayley.Pack.bern3_pv, Cayley.Pack.bernGE_spec
statement: formalized
proof: formalized
---

# packed_bounds

If the coefficient norm of $p$ is below the bound fixed by the slot width, then the checker's mask computations applied to $p$ at the Kronecker point return exactly the coefficient bound of Theorem [Coefficient bound](../the-coefficient-bound/thm-coef-bound.md), and its packed Bernstein transform returns the packed Bernstein coefficients. A Bernstein test that passes therefore certifies that every Bernstein coefficient is at least $m$.

## Depends on

- [kronecker](lem-kronecker.md)
- [Coefficient bound](../the-coefficient-bound/thm-coef-bound.md)
- [bernstein](../the-bernstein-bound/def-bernstein.md)

## Proof depends on

- [packN](lem-packn.md)

## Proof

Digit-by-digit arithmetic on packed numbers (Lemma [packN](lem-packn.md)). The Bernstein transform along variable $i$ separates the slots by their digit $i$ with masks, shifts them to a common position, and recombines them.

## Lean

Formalized as [`Cayley.Pack.pLowerL_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pLowerL_eq), [`Cayley.Pack.pStatsL_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pStatsL_eq), [`Cayley.Pack.bern3_pv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.bern3_pv), [`Cayley.Pack.bernGE_spec`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.bernGE_spec).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 124](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L124)
