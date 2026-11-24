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

- [Noperthedron blueprint: chapters/data.tex, line 69](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/data.tex#L69)
