---
declaration: lemma
origin: cited
lean: MIPRE.HaltingReductionQuantum, MIPRE.exists_quantumValue_lt_commutingOperatorValue, MIPRE.exists_mem_Cqc_not_mem_Cqa, MIPRE.exists_Cqa_ne_Cqc, MIPRE.tsirelson_of_upperRE_of_isClosed
statement: formalized
proof: formalized
---

# Conditional separation

Suppose that there is a computable map $g$ from machines to game descriptions with $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) = 1$ when $\mathcal{M}$ halts on the empty input and $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) \leq \frac12$ otherwise (the conclusion of Corollary [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md)), and that the relation ${\omega^{\mathrm{co}}}(\mathfrak{G}_d) < p/q$ on game descriptions $d$ and $p, q \in \mathbb{N}$ is recursively enumerable, with $p/0 = 0$ (the form of Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md) used here). Then some described game has $\mathrm{val}^*(\mathfrak{G}_d) < {\omega^{\mathrm{co}}}(\mathfrak{G}_d)$, and in its scenario some correlation lies in $C_{qc}$ but not in $C_{qa}$. If moreover $C_{qc}$ is closed in every finite scenario, then $C_{qa} \subsetneq C_{qc}$ in that scenario, whose two players share the question alphabet and the answer alphabet.

## Depends on

- [Basic properties of the correlation sets](lem-correlation-sets-basic.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Upper semidecision of the commuting-operator value](def-commuting-upper-re.md)

## Proof

If ${\omega^{\mathrm{co}}}(\mathfrak{G}_d) \leq \mathrm{val}^*(\mathfrak{G}_d)$ for every $d$, the two values agree on every described game, since $\mathrm{val}^* \leq {\omega^{\mathrm{co}}}$. Then $\mathcal{M}$ fails to halt exactly when ${\omega^{\mathrm{co}}}(\mathfrak{G}_{g(\mathcal{M})}) < \frac34$, so non-halting is the pullback of an r.e. relation along a computable map, hence r.e., which it is not (Theorem [Turing](../../background-results/part-03/thm-halting-undecidable.md)). So some $d$ has $\mathrm{val}^*(\mathfrak{G}_d) < {\omega^{\mathrm{co}}}(\mathfrak{G}_d)$, and some commuting-operator strategy has value above $\mathrm{val}^*(\mathfrak{G}_d)$; its correlation is in $C_{qc}$, and its payoff exceeds the bound $\mathrm{val}^*(\mathfrak{G}_d)$ that holds on $C_{qa}$ (Lemma [Basic properties of the correlation sets](lem-correlation-sets-basic.md)). With $C_{qc}$ closed, $C_{qa} \subseteq C_{qc}$, and the inclusion is strict.

## Lean

Formalized as [`MIPRE.HaltingReductionQuantum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HaltingReductionQuantum), [`MIPRE.exists_quantumValue_lt_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_quantumValue_lt_commutingOperatorValue), [`MIPRE.exists_mem_Cqc_not_mem_Cqa`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_mem_Cqc_not_mem_Cqa), [`MIPRE.exists_Cqa_ne_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_Cqa_ne_Cqc), [`MIPRE.tsirelson_of_upperRE_of_isClosed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.tsirelson_of_upperRE_of_isClosed).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 412](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L412)
