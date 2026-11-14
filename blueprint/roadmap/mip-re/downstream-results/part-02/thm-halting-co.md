---
declaration: theorem
origin: cited
lean: MIPRE.Halting.halting_reduction_upper, MIPRE.Halting.halting_reduction_upper_strings, MIPRE.Halting.halting_reduction_upper_of, MIPRE.Halting.halting_reduction_commuting_of, MIPRE.Halting.classOne, MIPRE.Halting.classA_subset_classOne, MIPRE.Halting.val_tab_eq_one_of_mem_classOne
statement: formalized
proof: formalized
---

# Halting reduces to the commuting-operator value, from co-soundness

Assume a gap compression is sound in the model ${\omega^{\mathrm{co}}}$ (Definition [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)). Then there is a computable map $\mathcal{M} \mapsto \mathfrak{G}_\mathcal{M}$ from machines to game descriptions such that ${\omega^{\mathrm{co}}}(\mathfrak{G}_\mathcal{M}) \leq \frac12$ if $\mathcal{M}$ halts on the empty input and ${\omega^{\mathrm{co}}}(\mathfrak{G}_\mathcal{M}) = 1$ otherwise. More generally, every value model that is r.e. from above and in which compression is sound has a halting reduction of $\mathrm{coRE}$ shape.

## Depends on

- [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)
- [Compressibility criterion, nested classes](../../computability/lem-compressible-criterion-nested.md)
- [Upper semidecision of the commuting-operator value](../part-01/lem-valco-upper-re.md)
- [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md)
- [Values of the halting verifier](../../structure-of-the-proof/part-09/lem-dhalt-values.md)
- [The self-referential decider is well defined](../../structure-of-the-proof/part-09/lem-halt-construction.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Value models](../part-01/def-value-model.md)

## Proof depends on

- [$\mathrm{MIP}^{\mathrm{co}} \subseteq \mathrm{coRE}$](../part-01/lem-mipco-sub-core.md)

## Proof

The halting reduction of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) in a value model $\omega$, with the direction of the semidecider reversed. Lemma [Compressibility criterion, nested classes](../../computability/lem-compressible-criterion-nested.md) is run with three classes of strings, each read as a normal form verifier as in Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) and with the same answer bounds:

- $A(n)$: the verifier is $n$-bounded, rejects every answer longer than the bound, and $\omega(\mathsf{V}_n) \leq \frac12$ — the class $B$ of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) in the model $\omega$. It contains the trivially rejecting string $y_{\mathrm{no}}$ of that theorem, whose game has value $0$ in every model, and the compressor of that theorem preserves it by soundness in the model, through the class transfer of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) read in $\omega$: the described verifier rejects beyond its answer bound, so raising the bound keeps the value; freezing keeps it; soundness carries it through compression; and the output's decider accepts what the compressed decider accepts.
- $B_0(n)$: the class $A$ of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) — $n$-bounded, rejecting long answers, with a perfect PCC strategy. It contains $y_{\mathrm{yes}}$, and the compressor preserves it by the *tensor* completeness of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md).
- $B_1(n)$: the strings whose tabulated game at level $n$ (the game description of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md), item 2) does not have $\omega < 1$. It contains $B_0(n)$, because a perfect PCC strategy gives $\mathrm{val}^* = 1$ and every model dominates $\mathrm{val}^*$; its complement is recursively enumerable by the upper semidecider of the model, at $p = q = 1$, composed with the computable tabulation.

The criterion gives a polynomial-time $g$ with $g(\mathcal{M}) \in A$ at the start level when $\mathcal{M}$ halts and $g(\mathcal{M}) \in B_1$ otherwise. The game of $\mathcal{M}$ is the tabulation of $g(\mathcal{M})$ at that level. In the first case it has $\omega(\mathsf{V}_n) \leq \frac12$, the tabulation having the value of the verifier's game in every model at every bounded string, which is item 2 of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md) read in $\omega$; in the second it does not have $\omega < 1$, so $\omega = 1$. No perfect strategy of the model is constructed. At $\omega = {\omega^{\mathrm{co}}}$ this is Lin's verifier sequence (Lin25), with the compressor's preservation of the accepting game read as tensor completeness, and with Lemma [Upper semidecision of the commuting-operator value](../part-01/lem-valco-upper-re.md) in place of the NPA hierarchy.

## Lean

Formalized as [`MIPRE.Halting.halting_reduction_upper`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_upper), [`MIPRE.Halting.halting_reduction_upper_strings`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_upper_strings), [`MIPRE.Halting.halting_reduction_upper_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_upper_of), [`MIPRE.Halting.halting_reduction_commuting_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.halting_reduction_commuting_of), [`MIPRE.Halting.classOne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classOne), [`MIPRE.Halting.classA_subset_classOne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.classA_subset_classOne), [`MIPRE.Halting.val_tab_eq_one_of_mem_classOne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.val_tab_eq_one_of_mem_classOne).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 902](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L902)
