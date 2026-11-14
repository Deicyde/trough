---
declaration: lemma
origin: cited
lean: E8_norm_eq_sqrt_even
statement: formalized
proof: formalized
---

# E8-vector-norms

All vectors in $\Lambda_8$ have norm of the form $\sqrt{2n}$, where $n$ is a nonnegative integer.

## Depends on

- [E8-defs-equivalent](e8-defs-equivalent.md)

## Proof

Writing $\vec{v} = \sum_i c_i\mathcal{B}_8^i$, we have $\|v\|^2 = \sum_i \sum_j c_ic_j (\mathcal{B}_8^i \cdot \mathcal{B}_8^j)$. Computing all $64$ pairs of dot products and simplifying, we get a massive term that is a quadratic form in $c_i$ with even integer coefficients, concluding the proof.

## Lean

Formalized as [`E8_norm_eq_sqrt_even`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/E8_norm_eq_sqrt_even).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/E8-defs.tex, line 73](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/E8-defs.tex#L73)
