---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.chkPolys, MIPRE.Tailored.AnsRed.passes_iff, MIPRE.Tailored.AnsRed.degreeOf_chkPolys_le, MIPRE.Tailored.AnsRed.chkPolys_eq_zero, MIPRE.Tailored.AnsRed.identities_of_chkPolys_eq_zero, MIPRE.Tailored.AnsRed.identities_of_dense
statement: formalized
proof: formalized
---

# The checks as polynomials, and Schwartz–Zippel

The thirteen checks pass at a point exactly when thirteen polynomials vanish there, of individual degree at most $d_T + 6(d + 1)$ for a PCP of degree $d$ and a circuit polynomial of individual degree $d_T$. A PCP of degree $d$ over $\mathbb{F}_q$ passing the checks on a set of points of density more than $m (d_T + 6(d + 1))/q$ has all thirteen polynomials zero, and so satisfies the checks identically.

## Depends on

- [The PCP and its thirteen checks](def-ar-pcp.md)

## Proof depends on

- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)

## Proof

Each of the six literal factors has individual degree at most $d + 1$ and each certificate sum at most $d + 2$; an assignment check is renamed along an injective map of the variables, which keeps degrees. A nonzero polynomial of individual degree $e$ in $m$ variables vanishes on a set of density at most $m e/q$ (Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.chkPolys`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.chkPolys), [`MIPRE.Tailored.AnsRed.passes_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.passes_iff), [`MIPRE.Tailored.AnsRed.degreeOf_chkPolys_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.degreeOf_chkPolys_le), [`MIPRE.Tailored.AnsRed.chkPolys_eq_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.chkPolys_eq_zero), [`MIPRE.Tailored.AnsRed.identities_of_chkPolys_eq_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.identities_of_chkPolys_eq_zero), [`MIPRE.Tailored.AnsRed.identities_of_dense`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.identities_of_dense).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2619](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2619)
