---
declaration: lemma
origin: cited
lean: MIPRE.MIPCo.isCoRE, MIPRE.MIPCo.exists_cosemidecider, MIPRE.MIPClass.isCoRE, MIPRE.MIPClass.exists_cosemidecider, MIPRE.ValueModel.commuting_upperRE
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} \subseteq \mathrm{coRE}$

Every language in $\mathrm{MIP}^{\mathrm{co}}$ is co-recursively enumerable. More generally $\mathrm{MIP}(\omega) \subseteq \mathrm{coRE}$ for every value model $\omega$ that is r.e. from above.

## Depends on

- [The class $\mathrm{MIP}^{\mathrm{co}}$](def-mipco.md)
- [Co-recursively enumerable](def-core.md)
- [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md)
- [Value models](def-value-model.md)

## Proof

Let $z \mapsto \mathfrak{G}_z$ witness $L \in \mathrm{MIP}(\omega)$. Under the promise, $z \notin L$ if and only if $\omega(\mathfrak{G}_z) < 1$. The set of game descriptions $d$ with $\omega(\mathfrak{G}_d) < 1$ is recursively enumerable, at $p = q = 1$, and the complement of $L$ is its preimage under the computable map $z \mapsto \mathfrak{G}_z$. For ${\omega^{\mathrm{co}}}$ the semidecider is Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md); Lin's proof runs the NPA hierarchy here (Lin25), and the Lean runs the sum-of-squares certificates of Lemma [Exact sum-of-squares certificates](lem-sos-certificates.md). The same argument at the threshold $\frac12$, for a model r.e. from below, is Lemma [$\mathrm{MIP}^* \subseteq \mathrm{RE}$](../../the-main-theorem/lem-mipstar-sub-re.md).

## Lean

Formalized as [`MIPRE.MIPCo.isCoRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPCo.isCoRE), [`MIPRE.MIPCo.exists_cosemidecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPCo.exists_cosemidecider), [`MIPRE.MIPClass.isCoRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPClass.isCoRE), [`MIPRE.MIPClass.exists_cosemidecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPClass.exists_cosemidecider), [`MIPRE.ValueModel.commuting_upperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting_upperRE).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 805](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L805)
