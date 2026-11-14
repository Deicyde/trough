---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Test.MainFormalStep5ExpansionBound, MIPRE.LIDT.Co.Test.mainFormalStep5_expansionBound, MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound, MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound_heterogeneous
statement: formalized
proof: formalized
---

# The Schwartz–Zippel step, in a symmetric model

Let $G$ and $H$ be submeasurements in $\mathcal{P}$ whose outcomes are the polynomials, and for a point $u \in \mathbb{F}_q^m$ let $G^{[u]}$ be $G$ evaluated at $u$, $G^{[u]}_a = \sum_{g : g(u) = a} G_g$, and likewise $H^{[u]}$. If $\mathop{\mathbb{E}}_u \mathrm{cons}(G^{[u]}, H^{[u]}) \leq \eta$ for a uniformly random point $u$, then

$$
\mathrm{cons}(G, H) \leq \eta + \frac{md}{q}.
$$

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.Test.mainFormalStep5_selfConsistency_ofExpansionBound` in `MIPRE/Background/LIDT/MIPStarRE/LDT/Test/SchwartzZippelStep.lean`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M4). Evaluating at $u$ leaves the totals unchanged and adds to the matched mass the pairs $g \neq h$ with $g(u) = h(u)$, so

$$
\mathrm{cons}(G, H) \leq \mathop{\mathbb{E}}_u \mathrm{cons}(G^{[u]}, H^{[u]}) + \sum_{g \neq h} \Pr_u\bigl[g(u)
= h(u)\bigr]\, \mathrm{ev}\bigl(L(G_g)\, R(H_h)\bigr).
$$

Two distinct polynomials of individual degree at most $d$ in $m$ variables agree on at most a fraction $md/q$ of the points, by the Schwartz–Zippel bound of the vendored classical layer, which is imported; and the $\mathrm{ev}(L(G_g)\, R(H_h))$ are nonnegative, $L(G_g)$ and $R(H_h)$ being commuting positive operators, with sum at most $1$. The definitions ported with this step (the restricted strategies of the main induction step, the slice families with their completeness, consistency, strong self-consistency and boundedness, and the statements of the induction step) are definitions, without proofs.

## Lean

Formalized as [`MIPRE.LIDT.Co.Test.MainFormalStep5ExpansionBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Test.MainFormalStep5ExpansionBound), [`MIPRE.LIDT.Co.Test.mainFormalStep5_expansionBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Test.mainFormalStep5_expansionBound), [`MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound), [`MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound_heterogeneous`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Test.mainFormalStep5_selfConsistency_ofExpansionBound_heterogeneous).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3798](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3798)
