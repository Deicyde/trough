---
declaration: section
origin: cited
lean: MetaMathlibExt.CyclicSumFormula.toIndex, MetaMathlibExt.CyclicSumFormula.leftIndex, MetaMathlibExt.CyclicSumFormula.rightIndex, MetaMathlibExt.CyclicSumFormula.leftIndex_isAdmissibleOrEmpty, MetaMathlibExt.CyclicSumFormula.rightIndex_isAdmissibleOrEmpty, MetaMathlibExt.hoffman_ohno_cyclic_sum_formula_strict, MetaMathlibExt.hoffman_ohno_cyclic_sum_formula, MetaMathlibExt.cyclic_sum_formula_multiple_zeta_star_values
statement: formalized
proof: formalized
---

# Cyclic sum formula

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html).

## The index of a list of positive integers

A list $(l_1, \dots, l_r)$ of positive
integers determines the multiple-zeta index whose entries are $l_1, \dots, l_r$ in this order;
its weight is $l_1 + \cdots + l_r$.

Formalized by `MetaMathlibExt.CyclicSumFormula.toIndex`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#to-index).

## Left-hand indices of the cyclic sum formula

Let $k = (k_1, \dots, k_l)$ be a list of
positive integers, with subscripts read modulo $l$. For $1 \le j \le l$ and a natural number
$i$, the left-hand index of $k$ at $(j, i)$ is the index
$(k_j - i + 1, k_{j+1}, \dots, k_{j+l-1}, i)$ when $1 \le i \le k_j - 1$, and the index $(2)$
otherwise. The run $k_{j+1}, \dots, k_{j+l-1}$ is empty when $l = 1$.

Formalized by `MetaMathlibExt.CyclicSumFormula.leftIndex`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#left-index).

## Right-hand indices of the cyclic sum formula

Let $k = (k_1, \dots, k_l)$ be a list of
positive integers, with subscripts read modulo $l$. For $1 \le j \le l$, the right-hand index of
$k$ at $j$ is the index $(k_j + 1, k_{j+1}, \dots, k_{j+l-1})$, where the run
$k_{j+1}, \dots, k_{j+l-1}$ is empty when $l = 1$.

Formalized by `MetaMathlibExt.CyclicSumFormula.rightIndex`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#right-index).

## Left-hand indices of the cyclic sum formula are admissible or empty

For every list
$k = (k_1, \dots, k_l)$ of positive integers, every $1 \le j \le l$ and every natural number $i$,
the left-hand index of the cyclic sum formula of $k$ at $(j, i)$ is admissible or empty.

Formalized by `MetaMathlibExt.CyclicSumFormula.leftIndex_isAdmissibleOrEmpty`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#left-index-is-admissible-or-empty).

## Right-hand indices of the cyclic sum formula are admissible or empty

For every list
$k = (k_1, \dots, k_l)$ of positive integers and every $1 \le j \le l$, the right-hand index of
the cyclic sum formula of $k$ at $j$ is admissible or empty.

Formalized by `MetaMathlibExt.CyclicSumFormula.rightIndex_isAdmissibleOrEmpty`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#right-index-is-admissible-or-empty).

## Cyclic sum formula for strict multiple zeta values of indices

Let $k = (k_1, \dots, k_l)$
be a nonempty list of positive integers, not all equal to $1$, with subscripts read modulo $l$,
and write $\zeta$ for the strict multiple zeta value. For $1 \le j \le l$ and
$1 \le i \le k_j - 1$ the left-hand index of the cyclic sum formula of $k$ at $(j, i)$ is
$(k_j - i + 1, k_{j+1}, \dots, k_{j+l-1}, i)$, and its right-hand index at $j$ is
$(k_j + 1, k_{j+1}, \dots, k_{j+l-1})$; the run $k_{j+1}, \dots, k_{j+l-1}$ is empty when
$l = 1$. Then

$$
\sum_{j=1}^{l} \sum_{i=1}^{k_j - 1} \zeta(k_j - i + 1, k_{j+1}, \dots, k_{j+l-1}, i)
= \sum_{j=1}^{l} \zeta(k_j + 1, k_{j+1}, \dots, k_{j+l-1}),
$$

where the inner sum is empty when $k_j = 1$.

Formalized by `MetaMathlibExt.hoffman_ohno_cyclic_sum_formula_strict`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 1555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L1555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#hoffman-ohno-cyclic-sum-formula-strict).

## Cyclic sum formula (Hoffman–Ohno)

For a finite list $(n_1, \dots, n_r)$ of natural numbers
let $\zeta(n_1, \dots, n_r)$ be the sum of $(m_1^{n_1} \cdots m_r^{n_r})^{-1}$ over all integers
$m_1 > m_2 > \cdots > m_r > 0$, taken to be $0$ when this family is not summable. Let
$k = (k_1, \dots, k_l)$ be a nonempty list of positive integers, not all equal to $1$, with
subscripts read modulo $l$. Then

$$
\sum_{j=1}^{l} \sum_{i=1}^{k_j - 1} \zeta(k_j - i + 1, k_{j+1}, \dots, k_{j+l-1}, i)
= \sum_{j=1}^{l} \zeta(k_j + 1, k_{j+1}, \dots, k_{j+l-1}),
$$

where the inner sum is empty when $k_j = 1$ and the run $k_{j+1}, \dots, k_{j+l-1}$ is empty
when $l = 1$.

## Sources

- Shingo Saito, Tatsushi Tanaka, and Noriko Wakabayashi, "Combinatorial Remarks on the Cyclic Sum Formula for Multiple Zeta Values," Journal of Integer Sequences 14 (2011), Article 11.2.4, Theorem `thm:CSF` ("Cyclic sum formula," first proved by Hoffman-Ohno), lines 242–248; index set `check{I}^1` at lines 150–166, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Saito/saito22.tex>.

Formalized by `MetaMathlibExt.hoffman_ohno_cyclic_sum_formula`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean, line 1725](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumFormula.lean#L1725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#hoffman-ohno-cyclic-sum-formula).

## Cyclic sum formula for multiple zeta-star values

Let $l \ge 1$ and let $k_0, \dots, k_{l-1}$
be positive integers, not all equal to $1$, with subscripts read modulo $l$, and put
$K = k_0 + \cdots + k_{l-1}$. Write $\zeta^\star$ for the multiple zeta-star value and $\zeta$ for
the strict multiple zeta value. Suppose that for each $0 \le j \le l - 1$ and each natural number
$i$ an index $\mathbf{c}_{j,i}$ is given that is admissible or empty, and that for
$1 \le i \le k_j - 1$ its entries are $(k_j - i + 1, k_{j+1}, \dots, k_{j+l-1}, i)$, the run
$k_{j+1}, \dots, k_{j+l-1}$ being empty when $l = 1$. Let $\mathbf{t}$ be an index, admissible
or empty, whose only entry is $K + 1$. Then

$$
\sum_{j=0}^{l-1} \sum_{i=1}^{k_j - 1} \zeta^\star(\mathbf{c}_{j,i}) = K \, \zeta(\mathbf{t}).
$$

## Sources

- S. Saito, T. Tanaka, and N. Wakabayashi, "Combinatorial Remarks on the Cyclic Sum Formula for Multiple Zeta Values", Journal of Integer Sequences 14 (2011), Article 11.2.4, Theorem `thm:CSF_MZSVs`, line 869, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Saito/saito22.tex>.

Formalized by `MetaMathlibExt.cyclic_sum_formula_multiple_zeta_star_values`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/CyclicSumMultipleZetaStar.lean, line 2085](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleZeta/CyclicSumMultipleZetaStar.lean#L2085). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html#cyclic-sum-formula-multiple-zeta-star-va).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cyclic sum formula](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/cyclic-sum-formula)
