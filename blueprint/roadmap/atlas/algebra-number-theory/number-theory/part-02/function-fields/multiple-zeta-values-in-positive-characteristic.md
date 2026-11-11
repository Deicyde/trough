---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.monicStrictAntiNatDegree, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.ζ_A, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝔖_w, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.ζ_A_weight, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒵, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯_aux, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯, MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯0_aux
statement: formalized
---

# Multiple zeta values in positive characteristic

13 results, 10 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html).

## Tuples of monic polynomials with strictly decreasing degrees

Let $F$ be a finite field
and $r$ a natural number. This is the set of $r$-tuples $(a_1, \dots, a_r)$ of monic polynomials
in $F[t]$ such that $\deg a_1 > \deg a_2 > \dots > \deg a_r$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.monicStrictAntiNatDegree`, an abbreviation declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#monic-strict-anti-nat-degree).

## Multiple zeta values in positive characteristic

Let $F$ be a finite field, $A = F[t]$,
and $K_\infty = F((1/t))$ the completion of the rational function field $F(t)$ at the place
at infinity. For a natural number $r$ and positive integers $s_1, \dots, s_r$, the multiple
zeta value is

$$\zeta_A(s_1, \dots, s_r) = \sum \frac{1}{a_1^{s_1} \cdots a_r^{s_r}} \in K_\infty,$$

where the sum runs over all $r$-tuples $(a_1, \dots, a_r)$ of monic polynomials in $A$ with
$\deg a_1 > \deg a_2 > \dots > \deg a_r$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.ζ_A`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#a).

## Compositions of $w$ into $r$ parts

For natural numbers $w$ and $r$, $\mathfrak{S}_w$
is the set of $r$-tuples $(s_1, \dots, s_r)$ of positive integers with $s_1 + \dots + s_r = w$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝔖_w`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#w).

## Multiple zeta values of given depth and weight

Let $F$ be a finite field and let $w$
and $r$ be natural numbers. The weight of a multiple zeta value $\zeta_A(s_1, \dots, s_r)$ over
$F$, with $s_1, \dots, s_r$ positive integers, is $s_1 + \dots + s_r$. This is the set of multiple
zeta values $\zeta_A(s_1, \dots, s_r)$ over $F$ of weight $w$, that is, with $s_1, \dots, s_r$
positive integers and $s_1 + \dots + s_r = w$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.ζ_A_weight`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#a-weight).

## The space $\mathcal{Z}_w$ of multiple zeta values of weight $w$

Let $K$ be the field of
rational functions in one variable over the finite field $F$, and $K_\infty$ its completion at
infinity. For $w \in \mathbb{N}$, $\mathcal{Z}_w$ is the $K$-linear subspace of $K_\infty$ spanned
by the multiple zeta values $\zeta_A(s_1, \dots, s_r)$ for all $r \ge 0$ and all positive integers
$s_1, \dots, s_r$ with $s_1 + \dots + s_r = w$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒵`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#untitled).

## Restricted multiple zeta values of given depth

Let $F$ be a finite field with $q$
elements, $w$ a natural number and $r$ a positive integer. This is the set of multiple zeta
values $\zeta_A(s_1, \dots, s_r)$ over $F$ with positive integers $s_1, \dots, s_r$ such that
$s_1 + \dots + s_r = w$, $s_i \le q$ for $1 \le i \le r - 1$, and $s_r < q$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯_aux`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#aux).

## The set $\mathcal{T}_w$ of restricted multiple zeta values

Let $q$ be the number of
elements of the finite field $F$. For $w \in \mathbb{N}$, $\mathcal{T}_w$ is the set of multiple
zeta values $\zeta_A(s_1, \dots, s_r)$, over all $r \ge 1$ and all positive integers
$s_1, \dots, s_r$ with $s_1 + \dots + s_r = w$, $s_i \le q$ for $1 \le i \le r - 1$,
and $s_r < q$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#untitled-2).

## Multiple zeta values of given depth with small entries

Let $F$ be a finite field with
$q$ elements, $w$ a natural number and $r$ a positive integer. This is the set of multiple
zeta values $\zeta_A(s_1, \dots, s_r)$ over $F$ with positive integers $s_1, \dots, s_r$ such
that $s_1 + \dots + s_r = w$ and $s_i < q$ for all $i$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯0_aux`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#0-aux).

## Multiple zeta values with small entries

Let $F$ be a finite field with $q$ elements and
$w$ a natural number. The set $\mathcal{T}^0_w$ consists of the multiple zeta values
$\zeta_A(s_1, \dots, s_r)$ over $F$, for all positive integers $r$ and $s_1, \dots, s_r$ such
that $s_1 + \dots + s_r = w$ and $s_i < q$ for all $i$.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.𝒯0`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#0).

## Dimension sequence for multiple zeta values

Let $F$ be a finite field with $q$ elements.
The sequence $d(w)$, for natural numbers $w$, is defined by $d(0) = 1$, $d(w) = 2^{w-1}$ for
$1 \le w \le q - 1$, $d(q) = 2^{q-1} - 1$, and
$d(w) = d(w - 1) + d(w - 2) + \dots + d(w - q)$ for $w > q$.

This is the sequence of Conjecture 1.5 and Theorems A and D of T. N. Dac, On Zagier-Hoffman's
conjectures in positive characteristic.

Formalized by `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.d`, a definition declared in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#d).

## Brown's theorem in positive characteristic

Let $F$ be a finite field with $q$ elements,
$K = F(t)$, and $w$ a positive integer. Let $\mathcal{Z}_w$ be the $K$-vector space spanned by
the multiple zeta values over $F$ of weight $w$, and let $\mathcal{T}_w$ be the set of multiple
zeta values $\zeta_A(s_1, \dots, s_r)$ with $r \ge 1$, positive integers $s_1, \dots, s_r$ with
sum $w$, $s_i \le q$ for $1 \le i \le r - 1$, and $s_r < q$. Then $\mathcal{Z}_w$ is the
$K$-linear span of $\mathcal{T}_w$, so every multiple zeta value of weight $w$ is a $K$-linear
combination of elements of $\mathcal{T}_w$, and $\dim_K \mathcal{Z}_w \le d(w)$, where $d$ is
the dimension sequence for multiple zeta values.

## Sources

- T. N. Dac, `On Zagier-Hoffman's conjectures in positive characteristic`, Annals of Math, 194 (1) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_zagier_hoffman_positive_char` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.theorem_A` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#theorem-a).

## Linear independence of multiple zeta values with small entries

Let $F$ be a finite field
with $q$ elements, $K = F(t)$, and $w$ a positive integer. Let $\mathcal{T}^0_w$ be the set of
multiple zeta values $\zeta_A(s_1, \dots, s_r)$ over $F$ with $r \ge 1$, positive integers
$s_1, \dots, s_r$ with sum $w$, and $s_i < q$ for all $i$, and let $\mathcal{Z}_w$ be the
$K$-vector space spanned by all multiple zeta values of weight $w$. Then the elements of
$\mathcal{T}^0_w$ are linearly independent over $K$, and
$\dim_K \mathcal{Z}_w \ge |\mathcal{T}^0_w|$.

## Sources

- T. N. Dac, `On Zagier-Hoffman's conjectures in positive characteristic`, Annals of Math, 194 (1) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_zagier_hoffman_positive_char` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.theorem_B` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#theorem-b).

## Dimension of multiple zeta values in low weight

Let $F$ be a finite field with $q$
elements, $K = F(t)$, and $w$ a positive integer with $w \le 2q - 2$. Let $\mathcal{T}_w$ be the
set of multiple zeta values $\zeta_A(s_1, \dots, s_r)$ over $F$ with $r \ge 1$, positive integers
$s_1, \dots, s_r$ with sum $w$, $s_i \le q$ for $1 \le i \le r - 1$, and $s_r < q$, and let
$\mathcal{Z}_w$ be the $K$-vector space spanned by all multiple zeta values of weight $w$. Then
the elements of $\mathcal{T}_w$ are linearly independent over $K$, and
$\dim_K \mathcal{Z}_w = d(w)$, where $d$ is the dimension sequence for multiple zeta values.

Together with Brown's theorem in positive characteristic (Theorem A of the source), which says
that $\mathcal{T}_w$ spans $\mathcal{Z}_w$, this means that $\mathcal{T}_w$ is a $K$-basis of
$\mathcal{Z}_w$.

## Sources

- T. N. Dac, `On Zagier-Hoffman's conjectures in positive characteristic`, Annals of Math, 194 (1) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_zagier_hoffman_positive_char` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ZagierHoffmanPositiveCharWanted.ZagierHoffmanPositiveChar.theorem_D` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ZagierHoffmanPositiveCharWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html#theorem-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple zeta values in positive characteristic](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/multiple-zeta-values-in-positive-characteristic)
