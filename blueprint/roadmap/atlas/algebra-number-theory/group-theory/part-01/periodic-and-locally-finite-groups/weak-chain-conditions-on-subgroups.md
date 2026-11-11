---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.WeakMaximalCondition, MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.WeakMinimalCondition, MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.minimalImpliesWeakMaximal, MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.maximalImpliesWeakMinimal, MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.minimalImpliesWeakMaximal_refuted, MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.maximalImpliesWeakMinimal_refuted
statement: formalized
---

# Weak chain conditions on subgroups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html).

## Weak maximal condition on subgroups

A group $G$ satisfies the weak maximal condition on
subgroups when there is no infinite ascending chain $H_0 \le H_1 \le \cdots$ of subgroups of $G$
in which every index $|H_{i+1} : H_i|$ is infinite.

Formalized by `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.WeakMaximalCondition`, a definition declared in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#weak-maximal-condition).

## Weak minimal condition on subgroups

The weak minimal condition on subgroups: there is no infinite descending chain
`H₀ ≥ H₁ ≥ ⋯` of subgroups with every index `|Hᵢ : Hᵢ₊₁|` infinite.

Formalized by `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.WeakMinimalCondition`, a definition declared in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#weak-minimal-condition).

## Minimal condition implies weak maximal condition

Kourovka 10.14(a) (D. I. Zaitsev): every group with the minimal condition on subgroups
satisfies the weak maximal condition on subgroups.

Formalized by `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.minimalImpliesWeakMaximal`, a definition declared in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#minimal-implies-weak-maximal).

## Maximal condition implies weak minimal condition

Kourovka 10.14(b): every group with the maximal condition on subgroups satisfies the weak
minimal condition on subgroups.

Formalized by `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.maximalImpliesWeakMinimal`, a definition declared in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#maximal-implies-weak-minimal).

## A group with the minimal condition can fail the weak maximal condition

There is a group $G$
satisfying the minimal condition on subgroups (there is no infinite strictly descending chain of
subgroups of $G$) that has an infinite ascending chain $H_0 \le H_1 \le \cdots$ of subgroups in
which every index $|H_{i+1} : H_i|$ is infinite. This answers Kourovka Problem 10.14(a) negatively.

The Kourovka Archive answers 10.14(a) "No, not always", citing Obraztsov (1990).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.14 (D. I. Zaitsev); resolution: V. N. Obraztsov, Math. USSR-Sb. 66, no. 2 (1990), 541-553 (a); V. N. Obraztsov, Siberian Math. J. 32, no. 1 (1991), 79-84 (b), Kourovka Archive, Problem 10.14 (both parts "No, not always").

Stated but not proved: `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.minimalImpliesWeakMaximal_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#minimal-implies-weak-maximal-refuted).

## A group with the maximal condition can fail the weak minimal condition

There is a group $G$
satisfying the maximal condition on subgroups (there is no infinite strictly ascending chain of
subgroups of $G$) that has an infinite descending chain $H_0 \ge H_1 \ge \cdots$ of subgroups in
which every index $|H_i : H_{i+1}|$ is infinite. This answers Kourovka Problem 10.14(b) negatively.

The Kourovka Archive answers 10.14(b) "No, not always", citing Obraztsov (1991).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.14 (D. I. Zaitsev); resolution: V. N. Obraztsov, Math. USSR-Sb. 66, no. 2 (1990), 541-553 (a); V. N. Obraztsov, Siberian Math. J. 32, no. 1 (1991), 79-84 (b), Kourovka Archive, Problem 10.14 (both parts "No, not always").

Stated but not proved: `MathlibExt.GroupTheory.WeakChainConditionsKourovka10Problem14Wanted.maximalImpliesWeakMinimal_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WeakChainConditionsKourovka10Problem14Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html#maximal-implies-weak-minimal-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weak chain conditions on subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/weak-chain-conditions-on-subgroups)
