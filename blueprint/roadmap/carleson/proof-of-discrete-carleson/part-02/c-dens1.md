---
declaration: lemma
origin: cited
lean: dens1_le
statement: formalized
proof: formalized
---

# C dens1

For each set $\mathfrak{A} \subset \mathfrak{C}(k,n)$, we have

$$
\operatorname{\operatorname{dens}}_1(\mathfrak{A}) \le 2^{4a}2^{-n+1}\,.
$$

## Depends on

- [dens compare](dens-compare.md)

## Proof

We have by [dens compare](dens-compare.md) that $\operatorname{\operatorname{dens}}_1(\mathfrak{A}) \le \operatorname{\operatorname{dens}}_k'(\mathfrak{A})$. Since $\mathfrak{A} \subset {\mathfrak C}(k,n)$, it follows from monotonicity of suprema and the definition [(6)](../README.md) that $\operatorname{\operatorname{dens}}_k'(\mathfrak{A}) \le \operatorname{\operatorname{dens}}_k'({\mathfrak C}(k,n))\,.$ By [(6)](../README.md) and [(7)](../README.md), we have

$$
\operatorname{\operatorname{dens}}_k'({\mathfrak C}(k,n)) = \sup_{{\mathfrak p} \in {\mathfrak C}(k,n)} \operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}\}) \le 2^{4a}2^{-n+1}\,.
$$

## Lean

Formalized as [`dens1_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dens1_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2893](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2893)
