---
declaration: definition
origin: cited
lean: SubgroupTestValue.SubgroupTestData, SubgroupTestValue.SubgroupTestData.equivTuple, SubgroupTestValue.FiniteAction, SubgroupTestValue.FiniteAction.letterPerm, SubgroupTestValue.FiniteAction.wordPerm, SubgroupTestValue.FiniteAction.InStab, SubgroupTestValue.FiniteAction.LitHolds, SubgroupTestValue.FiniteAction.Passes, SubgroupTestValue.FiniteAction.passProb, SubgroupTestValue.SubgroupTestData.totalWeight, SubgroupTestValue.SubgroupTestData.value, SubgroupTestValue.SubgroupTestData.valSof
statement: formalized
---

# Subgroup tests and their sofic value; I:439–520

A subgroup test over the free group $F$ on $n$ generators is a finite list of weighted challenges, each a finite list $K$ of words and a decision on the subsets of $K$, here in disjunctive normal form over the literals “the $i$-th word of $K$ lies in (or out of) the subgroup”. A finite action $\sigma$ of $F$ on a set of size $N \geq 1$ gives the finitely described IRS $\Phi(\sigma)$, the stabilizer of a uniform point; its value against the test is the probability that the stabilizer passes a challenge drawn with probability proportional to its weight. The sofic value of the test is the supremum of the values of finite actions.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`SubgroupTestValue.SubgroupTestData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData), [`SubgroupTestValue.SubgroupTestData.equivTuple`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.equivTuple), [`SubgroupTestValue.FiniteAction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction), [`SubgroupTestValue.FiniteAction.letterPerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.letterPerm), [`SubgroupTestValue.FiniteAction.wordPerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.wordPerm), [`SubgroupTestValue.FiniteAction.InStab`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.InStab), [`SubgroupTestValue.FiniteAction.LitHolds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.LitHolds), [`SubgroupTestValue.FiniteAction.Passes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.Passes), [`SubgroupTestValue.FiniteAction.passProb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.FiniteAction.passProb), [`SubgroupTestValue.SubgroupTestData.totalWeight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.totalWeight), [`SubgroupTestValue.SubgroupTestData.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.value), [`SubgroupTestValue.SubgroupTestData.valSof`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/SubgroupTestValue.SubgroupTestData.valSof).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 31](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L31)
