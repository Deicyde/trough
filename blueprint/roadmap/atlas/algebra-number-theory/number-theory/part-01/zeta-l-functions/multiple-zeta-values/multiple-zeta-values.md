---
declaration: section
origin: cited
lean: MetaMathlibExt.MultipleZeta.summable_strictSummand
statement: formalized
proof: formalized
---

# Multiple zeta values: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/index.html).

Multiple zeta and zeta-star values, Hoffman bases, word algebras, cyclic sum formulas, finite and q-analogue multiple zeta values.

## Convergence of multiple zeta series

Let $\mathbf{k} = (k_1, \dots, k_r)$ be an admissible
index, that is, a nonempty index of positive integers with $k_1 \ge 2$. Then the strict
multiple-zeta series of $\mathbf{k}$, the family of terms $(m_1^{k_1} \cdots m_r^{k_r})^{-1}$
indexed by the strictly decreasing tuples $m_1 > \cdots > m_r$ of positive integers, is summable.

## Sources

- arXiv:2307.09867, lines 60–63, and arXiv:2309.07569, lines 76–80; equivalent increasing-variable formulations occur in arXiv:2304.08722, 2312.13525, 2608.10675, 2608.15480, and 2608.22280 after reversing both the variables and exponents.

Formalized by `MetaMathlibExt.MultipleZeta.summable_strictSummand`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/Convergence.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/Convergence.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/index.html#summable-strict-summand).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple zeta values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values)
