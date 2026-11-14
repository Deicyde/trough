---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.PolyR, MIPRE.Tailored.AnsRed.Typed.dS, MIPRE.Tailored.AnsRed.Typed.epsR, MIPRE.Tailored.AnsRed.Typed.GA, MIPRE.Tailored.AnsRed.Typed.GB
statement: formalized
---

# The polynomial measurements

At a role $r$ with $k_r$ codewords, $\delta_r(\varepsilon) = \delta_{\mathrm{sim}}(q, M, d, k_r, \varepsilon)$ is the error of the seeded test's soundness. When the test is sound in the model, $G^\textsc{A}_{r,y}$ and $G^\textsc{B}_{r,y}$ are the projective measurements, in the two players' algebras, of $k_r$-tuples of polynomials of individual degree at most $d$ in $M$ variables that the test's soundness gives for the per-role strategy at a role $r$ and an oracularized question $y$; $G^\textsc{A}_r$ and $G^\textsc{B}_r$ are those at $y_r(z)$.

## Depends on

- [The per-role low-degree strategies](../part-06/def-ar-sound-roles.md)
- [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)
- [Absorbing the simultaneous reduction's error](../../background-results/part-01/lem-lidt-ldc-error.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.PolyR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.PolyR), [`MIPRE.Tailored.AnsRed.Typed.dS`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.dS), [`MIPRE.Tailored.AnsRed.Typed.epsR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.epsR), [`MIPRE.Tailored.AnsRed.Typed.GA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.GA), [`MIPRE.Tailored.AnsRed.Typed.GB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.GB).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3174](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3174)
