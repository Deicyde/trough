---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.encTbl, MIPRE.Tailored.AnsRed.RTables, MIPRE.Tailored.AnsRed.LTables, MIPRE.Tailored.AnsRed.induce
statement: formalized
---

# The honest PCP; $\mathsf{Induce}_C$

The *encoding* of a table $t$ on $\mathbb{N}$ in $k$ variables is the multilinear polynomial whose value at the binary digits of $c < 2^k$ is $t(c)$. From Boolean *readable tables* (the cells of the two readable answers, the table $O$ and the three witness blocks) and $\mathbb{F}_2$-valued *linear tables* (the cells of the two linear answers and the three copies), the *honest PCP* of a circuit polynomial $T$ has the encodings of the tables as its assignments, and as helpers the linear certificates (Lemma [Linear certificates for vanishing on the cube](lem-ar-linear-certificates.md)) of the left-hand sides of its checks: of the formula polynomial at degree $17$, of the system polynomial at degree $3$, and of $g(1 - g)$ for each assignment $g$ at degree $2$.

## Depends on

- [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)
- [Linear certificates for vanishing on the cube](lem-ar-linear-certificates.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.encTbl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.encTbl), [`MIPRE.Tailored.AnsRed.RTables`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.RTables), [`MIPRE.Tailored.AnsRed.LTables`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.LTables), [`MIPRE.Tailored.AnsRed.induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.induce).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2722](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2722)
