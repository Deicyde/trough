---
declaration: definition
origin: cited
lean: Cayley.Pack.Layout, Cayley.Pack.Layout.idx, Cayley.Pack.kron
statement: formalized
---

# layout

A *layout* assigns to every exponent vector $m$ with $m_i < r_i$ the slot $\mathrm{idx}(m) = \sum_i m_i s_i$, where $s_i = \prod_{i' < i} r_{i'}$. For a slot width $W$, the *Kronecker point* is $t_i = 2^{W s_i}$.

## Depends on

- [pe](../def-pe.md)

## Lean

Formalized as [`Cayley.Pack.Layout`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Layout), [`Cayley.Pack.Layout.idx`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Layout.idx), [`Cayley.Pack.kron`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.kron).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 92](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L92)
