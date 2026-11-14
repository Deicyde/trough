---
declaration: lemma
origin: cited
lean: Cayley.cayleyMatrix_mem_SO3, Cayley.cayleyDenom_pos
statement: formalized
proof: formalized
---

# cayley_so3

$D(r) > 0$ and $\mathrm{Cay}(r) \in SO(3)$ for every $r \in \operatorname{\mathbb{R}}^3$.

## Depends on

- [cayley](def-cayley.md)

## Proof

Direct computation: $N(r) N(r)^T = D(r)^2 I$ and $\det N(r) = D(r)^3$.

## Lean

Formalized as [`Cayley.cayleyMatrix_mem_SO3`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyMatrix_mem_SO3), [`Cayley.cayleyDenom_pos`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cayleyDenom_pos).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 34](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L34)
