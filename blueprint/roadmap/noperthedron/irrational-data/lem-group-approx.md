---
declaration: lemma
origin: cited
lean: Cayley.group_approx
statement: formalized
proof: formalized
---

# group_approx

Every entry of every tabulated rotation $\hat g_k$ is within $2^{-60}$ of the corresponding entry of $g_k = R_z(2\pi k/15)$.

## Depends on

- [trig_table](lem-trig-table.md)

## Proof

Immediate from Lemma [trig_table](lem-trig-table.md).

## Lean

Formalized as [`Cayley.group_approx`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.group_approx).

## Sources

- [Noperthedron blueprint: chapters/data.tex, line 67](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/data.tex#L67)
