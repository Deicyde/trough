---
declaration: lemma
origin: cited
lean: MIPRE.Cost.hardcode_time, MIPRE.Cost.hardcode_time_rev, MIPRE.Cost.hardcode_size, MIPRE.Cost.smn_polyTime
statement: formalized
proof: formalized
---

# Efficient s-m-n

There is a polynomial-time computable $s$ such that $\phi_{s(e,x)}(y) = \phi_e(x, y)$ for all $e, x, y$, with the runtimes of $e$ and $s(e,x)$ polynomially equivalent.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

In the ambient list language, $s(e, x)$ is the program that pairs the literal $x$ with its input and runs $e$ on the pair (`MIPRE.Cost.hardcode`). The time overhead is additive and linear in $\left\vert {x} \right\vert$ and the input size, in both directions, and the description of $s(e, x)$ is that of $e$ plus $\left\vert {x} \right\vert$ plus a constant. The map $s$ itself is computed in linear time by a fixed program assembling the description (`smnProg`).

## Lean

Formalized as [`MIPRE.Cost.hardcode_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.hardcode_time), [`MIPRE.Cost.hardcode_time_rev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.hardcode_time_rev), [`MIPRE.Cost.hardcode_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.hardcode_size), [`MIPRE.Cost.smn_polyTime`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.smn_polyTime).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 158](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L158)
