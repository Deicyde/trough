---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TotientSumSimplicityKourovka19Problem25Wanted.sameOrderTotientSumSimple, MathlibExt.GroupTheory.TotientSumSimplicityKourovka19Problem25Wanted.sameOrderTotientSumSimple_refuted
statement: formalized
---

# Totient sums of element orders

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/totient-sums-of-element-orders/index.html).

## Curtin–Pourgholi question on totient sums and simplicity (Kourovka 19.25)

The statement
that for all finite groups $G$ and $H$ of the same order with
$\sum_{g \in G} \varphi(|g|) = \sum_{h \in H} \varphi(|h|)$, where $|g|$ is the order of $g$ and
$\varphi$ is Euler's totient function, if $G$ is simple then $H$ is simple.

Formalized by `MathlibExt.GroupTheory.TotientSumSimplicityKourovka19Problem25Wanted.sameOrderTotientSumSimple`, a definition declared in [WantedExt/GroupTheory/TotientSumSimplicityKourovka19Problem25Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotientSumSimplicityKourovka19Problem25Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/totient-sums-of-element-orders/index.html#same-order-totient-sum-simple).

## Order and totient sum do not determine simplicity (Kourovka 19.25)

There are finite groups
$G$ and $H$ of the same order with $\sum_{g \in G} \varphi(|g|) = \sum_{h \in H} \varphi(|h|)$,
where $|g|$ is the order of $g$ and $\varphi$ is Euler's totient function, such that $G$ is
simple and $H$ is not simple. So the Curtin–Pourgholi question has a negative answer.

Van Doorn, Judin, Monticone and Morrison (Theorem 4.1) take for $G$ the projective special
unitary group $\mathrm{PSU}(3, 3)$, which is simple of order $6048$, and
$H = C_6 \times S_4 \times F$, where $C_6$ is the cyclic group of order $6$, $S_4$ is the symmetric
group on four letters and $F$ is the Frobenius group of order $42$; both totient sums equal
$23984$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.25 (B. Curtin, G. R. Pourgholi); resolution: P. Monticone, Kourovka Notebook Problem 19.25, solution note (2026); W. van Doorn, E. Judin, P. Monticone and D. Morrison, On Some Problems from the Kourovka Notebook, preprint, arXiv:2607.17477 (2026), Section 4, Theorem 4.1 with Lemma 4.2 (G = PSU(3, 3) is simple, by Iwasawa's criterion, of order 6048 with totient sum 23984) and Lemma 4.3 (H = C₆ × S₄ × F, F the Frobenius group of order 42, has the same order and totient sum and is not simple); the solution was found and verified in Lean by the AI system Aristotle (abstract and Appendix A); the Kourovka Notebook (21st issue) marks 19.25 solved: No, it need not be (AI solution confirmed by GAP), https://arxiv.org/abs/2607.17477.

Stated but not proved: `MathlibExt.GroupTheory.TotientSumSimplicityKourovka19Problem25Wanted.sameOrderTotientSumSimple_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TotientSumSimplicityKourovka19Problem25Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TotientSumSimplicityKourovka19Problem25Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/totient-sums-of-element-orders/index.html#same-order-totient-sum-simple-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Totient sums of element orders](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/totient-sums-of-element-orders/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orders-and-spectra/totient-sums-of-element-orders)
