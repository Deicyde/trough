---
declaration: lemma
origin: cited
lean: MIPRE.MIPStarComputable.isRE, MIPRE.MIPStarComputable.exists_semidecider, MIPRE.MIPClass.isRE, MIPRE.MIPClass.exists_semidecider, MIPRE.ValueModel.tensor_lowerRE
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^* \subseteq \mathrm{RE}$

Every language in $\mathrm{MIP}^*$ is recursively enumerable.

## Depends on

- [The computable class](../foundations/part-03/def-mipstar-computable.md)
- [Recursively enumerable](../foundations/part-02/def-re.md)
- [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md)
- [Value models](../downstream-results/part-01/def-value-model.md)

## Proof

Let $z \mapsto \mathfrak{G}_z$ witness $L \in \mathrm{MIP}^*$. Under the promise, $z \in L$ if and only if $\mathrm{val}^*(\mathfrak{G}_z) > \frac12$: the value is $1$ on $L$ and at most $\frac12$ off it. By Lemma [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md) the set of game descriptions $g$ with $\mathrm{val}^*(\mathfrak{G}_g) > \frac12$ is recursively enumerable, and $L$ is its preimage under the computable map $z \mapsto \mathfrak{G}_z$; the preimage of an r.e. set under a computable map is r.e. Concretely: given $z$, compute $\mathfrak{G}_z$, enumerate tensor-product strategies and accept upon finding one of value greater than $\frac12$; this semi-decides $L$. In Lean the class is the computable one (Definition [The computable class](../foundations/part-03/def-mipstar-computable.md)), and `MIPStarComputable.exists_semidecider` gives the semidecider as a program of the ambient model.

## Lean

Formalized as [`MIPRE.MIPStarComputable.isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStarComputable.isRE), [`MIPRE.MIPStarComputable.exists_semidecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPStarComputable.exists_semidecider), [`MIPRE.MIPClass.isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPClass.isRE), [`MIPRE.MIPClass.exists_semidecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPClass.exists_semidecider), [`MIPRE.ValueModel.tensor_lowerRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor_lowerRE).

## Sources

- [MIP* = RE blueprint: content/07_main_theorem.tex, line 160](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/07_main_theorem.tex#L160)
