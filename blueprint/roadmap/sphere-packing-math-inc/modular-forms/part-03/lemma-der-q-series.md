---
declaration: lemma
origin: cited
lean: D_qexp_tsum_pnat
statement: formalized
proof: formalized
---

# der-q-series

We have an equality of operators $D = q \frac{\mathrm{d}}{\mathrm{d} q}$. In particular, the $q$-series of the derivative of a quasimodular form $F(z) = \sum_{n \ge n_0} a_n q^n$ is $F'(z) = \sum_{n \ge n_0} n a_n q^n$.

## Depends on

- [derivative](def-derivative.md)

## Proof

Directly follows from the definition [Definition derivative](def-derivative.md), where $\frac{1}{2 \pi i}\frac{\mathrm{d}}{\mathrm{d} z}e^{2\pi i n z} = n e^{2\pi i n z}$.

## Lean

Formalized as [`D_qexp_tsum_pnat`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/D_qexp_tsum_pnat).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 547](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L547)
