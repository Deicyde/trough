---
declaration: theorem
origin: cited
lean: MIPRE.separation, MIPRE.separation_of_upperRE, MIPRE.exists_quantumValue_le_half_commutingOperatorValue_eq_one, MIPRE.exists_mem_Cqc_payoff_eq_commutingOperatorValue
statement: formalized
proof: formalized
---

# Separation

There is an explicit finite bipartite game $\mathfrak{G}^{\textsc{Sep}}$, given by a game description, with $\mathrm{val}^*(\mathfrak{G}^{\textsc{Sep}}) \leq \frac12$ and ${\omega^{\mathrm{co}}}(\mathfrak{G}^{\textsc{Sep}}) = 1$. Moreover, some correlation $p \in C_{qc}$ in the scenario of $\mathfrak{G}^{\textsc{Sep}}$ has payoff $1$ in $\mathfrak{G}^{\textsc{Sep}}$ and lies outside $C_{qa}$.

## Depends on

- [Correlation sets](def-correlation-sets.md)
- [Basic properties of the correlation sets](lem-correlation-sets-basic.md)
- [Upper semidecision of the commuting-operator value](def-commuting-upper-re.md)
- [Conditional separation](lem-tsirelson-conditional.md)
- [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md)
- [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md)
- [$C_{qc}$ is compact](lem-cqc-compact.md)

## Proof

Let $g$ be the computable map of Corollary [Halting reduces to the quantum value](../../the-main-theorem/cor-main-quantum.md), from machines to game descriptions, with $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) = 1$ when $\mathcal{M}$ halts on the empty input and $\mathrm{val}^*(\mathfrak{G}_{g(\mathcal{M})}) \leq \frac12$ otherwise. By Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md) at $p = q = 1$, the set of machines $\mathcal{M}$ with ${\omega^{\mathrm{co}}}(\mathfrak{G}_{g(\mathcal{M})}) < 1$ is recursively enumerable. Kleene's recursion theorem therefore gives a machine $\mathcal{M}_{\textsc{Sep}}$ that halts on the empty input exactly when ${\omega^{\mathrm{co}}}(\mathfrak{G}_{g(\mathcal{M}_{\textsc{Sep}})}) < 1$. Put $\mathfrak{G}^{\textsc{Sep}} = \mathfrak{G}_{g(\mathcal{M}_{\textsc{Sep}})}$.

If $\mathcal{M}_{\textsc{Sep}}$ halted, then $\mathrm{val}^*(\mathfrak{G}^{\textsc{Sep}}) = 1$, so ${\omega^{\mathrm{co}}}(\mathfrak{G}^{\textsc{Sep}}) = 1$ by $\mathrm{val}^* \leq {\omega^{\mathrm{co}}}$ (Lemma [Basic properties of the correlation sets](lem-correlation-sets-basic.md)), and $\mathcal{M}_{\textsc{Sep}}$ would not halt. So $\mathcal{M}_{\textsc{Sep}}$ does not halt. Hence $\mathrm{val}^*(\mathfrak{G}^{\textsc{Sep}}) \leq \frac12$, and ${\omega^{\mathrm{co}}}(\mathfrak{G}^{\textsc{Sep}})$ is not below $1$, so it equals $1$.

For the correlation: the payoff is continuous, and $C_{qc}$ is compact (Lemma [$C_{qc}$ is compact](lem-cqc-compact.md)) and nonempty, so the payoff attains its maximum on $C_{qc}$ at some $p$. That maximum is ${\omega^{\mathrm{co}}}(\mathfrak{G}^{\textsc{Sep}}) = 1$, since every commuting-operator strategy has value equal to the payoff of its correlation. Payoffs on $C_{qa}$ are at most $\mathrm{val}^*(\mathfrak{G}^{\textsc{Sep}}) \leq \frac12$ (Lemma [Basic properties of the correlation sets](lem-correlation-sets-basic.md)), so $p \notin C_{qa}$.

## Lean

Formalized as [`MIPRE.separation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.separation), [`MIPRE.separation_of_upperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.separation_of_upperRE), [`MIPRE.exists_quantumValue_le_half_commutingOperatorValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_quantumValue_le_half_commutingOperatorValue_eq_one), [`MIPRE.exists_mem_Cqc_payoff_eq_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_mem_Cqc_payoff_eq_commutingOperatorValue).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 476](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L476)
