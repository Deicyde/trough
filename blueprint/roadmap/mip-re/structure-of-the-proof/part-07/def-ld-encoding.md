---
declaration: definition
origin: cited
lean: MIPRE.LowDegree.ofBool, MIPRE.LowDegree.pt, MIPRE.LowDegree.ind, MIPRE.LowDegree.eval_ind, MIPRE.LowDegree.degreeOf_ind_le, MIPRE.LowDegree.ldEnc, MIPRE.LowDegree.eval_ldEnc, MIPRE.LowDegree.degreeOf_ldEnc_le, MIPRE.LowDegree.codedOn, MIPRE.LowDegree.codedOn_ldEnc, MIPRE.LowDegree.coded, MIPRE.LowDegree.coded_eq, MIPRE.LowDegree.totalDegree_ind_le, MIPRE.LowDegree.totalDegree_ldEnc_le
statement: formalized
---

# The low-degree code

For $y \in \{0,1\}^m$ let ${\mathrm{ind}}_{m,y}(x) = \prod_{i : y_i = 1} x_i \prod_{i : y_i = 0} (1 - x_i)$, a multilinear polynomial over $\mathbb{F}_q$ which on the subcube $\{0,1\}^m$ is $1$ at $y$ and $0$ elsewhere. For $a \in \mathbb{F}_q^M$, $M = 2^m$, with coordinates indexed by $\{0,1\}^m$, the *low-degree encoding* of $a$ is $g_a = \sum_y a_y {\mathrm{ind}}_{m,y}$; it is multilinear and $g_a(y) = a_y$. For $H \subseteq \mathbb{F}_q$ the *decoding* map ${\mathrm{Coded}}_H$ sends a polynomial $g$ to the vector with $y$-coordinate $g(y)$ if $g(y) \in H$ and $0$ otherwise, so that ${\mathrm{Coded}}_H(g_a) = a$ for $a \in H^M$; ${\mathrm{Coded}} = {\mathrm{Coded}}_{\{0,1\}}$ is the Boolean decoding map, and ${\mathrm{Coded}}(g) \in \{0,1\}^M$ for every $g$. Being multilinear, $g_a$ has individual degree at most $1$ and total degree at most $m$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.LowDegree.ofBool`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.ofBool), [`MIPRE.LowDegree.pt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.pt), [`MIPRE.LowDegree.ind`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.ind), [`MIPRE.LowDegree.eval_ind`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eval_ind), [`MIPRE.LowDegree.degreeOf_ind_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.degreeOf_ind_le), [`MIPRE.LowDegree.ldEnc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.ldEnc), [`MIPRE.LowDegree.eval_ldEnc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eval_ldEnc), [`MIPRE.LowDegree.degreeOf_ldEnc_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.degreeOf_ldEnc_le), [`MIPRE.LowDegree.codedOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.codedOn), [`MIPRE.LowDegree.codedOn_ldEnc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.codedOn_ldEnc), [`MIPRE.LowDegree.coded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.coded), [`MIPRE.LowDegree.coded_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.coded_eq), [`MIPRE.LowDegree.totalDegree_ind_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.totalDegree_ind_le), [`MIPRE.LowDegree.totalDegree_ldEnc_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.totalDegree_ldEnc_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4687](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4687)
