---
declaration: section
origin: cited
lean: MetaMathlibExt.norm_le_one_of_aeval_eq_zero_of_monotone_coeff, MetaMathlibExt.exists_dominant_root_of_pos_coeff_charPoly, MetaMathlibExt.tprod_one_sub_inv_add_eq_one_sub_tsum_add_isBigO
statement: formalized
---

# Dominant roots and reciprocal sums of recurrences

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence/index.html).

## Eneström–Kakeya theorem

Let $a_0 + a_1 x + \cdots + a_n x^n$ be a nonzero real
polynomial of degree $n$ with $0 \le a_0 \le a_1 \le \cdots \le a_n$. Then every complex root $z$
of this polynomial satisfies $|z| \le 1$.

## Sources

- Tingting Du, *On the Reciprocal Sums and Products of m th-order Linear Recursive Sequences*, Journal of Integer Sequences 27 (2024), Article 24.2.3, Lemma 3 (`jis-2024-24.2.3-lem-3`), quoted there as the Eneström–Kakeya theorem.

Stated but not proved: `MetaMathlibExt.norm_le_one_of_aeval_eq_zero_of_monotone_coeff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence/index.html#norm-le-one-of-aeval-eq-zero-of-monotone).

## Dominant root of $x^m - a_1 x^{m-1} - \cdots - a_m$ with positive coefficients

Let
$m \ge 2$ and let $a_1, \dots, a_m$ be positive integers. Then the polynomial
$\varphi(x) = x^m - a_1 x^{m-1} - \cdots - a_m$ has exactly one positive real root $\lambda$,
this root satisfies $\lambda > 1$, and the complex roots of $\varphi$, counted with
multiplicity, are $\lambda$ (a simple root) together with $m - 1$ roots of modulus less than
$\lambda$.

## Sources

- Tingting Du, *On the Reciprocal Sums and Products of m th-order Linear Recursive Sequences*, Journal of Integer Sequences 27 (2024), Article 24.2.3, Lemma 4 (`jis-2024-24.2.3-lem-4`).

Stated but not proved: `MetaMathlibExt.exists_dominant_root_of_pos_coeff_charPoly` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence/index.html#exists-dominant-root-of-pos-coeff-char-p).

## Asymptotic expansion of a perturbed tail product

Let $\mu$ and $\lambda$ be real numbers
with $1 < \mu < \lambda$, let $c \ne 0$ be a real number, and let $(e_k)_{k \ge 0}$ be a real
sequence with $e_k = O\bigl((\mu/\lambda^3)^{k/2}\bigr)$ as $k \to \infty$. Then, as
$n \to \infty$,
$\prod_{k \ge n} \bigl(1 - 1/(c\lambda^k) + e_k\bigr) = 1 - \sum_{k \ge n} 1/(c\lambda^k) +
O\bigl((\mu/\lambda^3)^{n/2}\bigr)$.

## Sources

- Tingting Du, *On the Reciprocal Sums and Products of m th-order Linear Recursive Sequences*, Journal of Integer Sequences 27 (2024), Article 24.2.3, Lemma 7 (`jis-2024-24.2.3-lem-7`).

Stated but not proved: `MetaMathlibExt.tprod_one_sub_inv_add_eq_one_sub_tsum_add_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ReciprocalSumsLinearRecurrenceWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence/index.html#tprod-one-sub-inv-add-eq-one-sub-tsum-ad).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dominant roots and reciprocal sums of recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/dominant-roots-and-reciprocal-sums-of-recurrence)
