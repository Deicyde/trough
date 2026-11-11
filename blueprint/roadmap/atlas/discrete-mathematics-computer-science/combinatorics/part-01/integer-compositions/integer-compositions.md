---
declaration: section
origin: cited
lean: MetaMathlibExt.munagi_restricted_compositions, MetaMathlibExt.palindromic_compositions_without_two, MetaMathlibExt.pow_div_one_sub_pow_eq_sum
statement: formalized
---

# Integer compositions: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/index.html).

Ordered sums of positive integers: compositions with restricted, palindromic, colored or n-color parts, Arndt compositions, perfect compositions, shade, symmetric peaks and valleys, and convolution identities for weighted compositions.

## Munagi's theorem on restricted compositions

For positive integers $n$ and $k$, the number
of compositions of $n$ all of whose parts are congruent to $1$ modulo $k$ equals the number of
compositions of $n + k - 1$ all of whose parts are at least $k$.

## Sources

- Jia Huang, "Even and Odd Compositions with Restricted Parts", Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem `thm:comp2` (Munagi), lines 160-162, <https://cs.uwaterloo.ca/journals/JIS/VOL27/Huang/huang9.tex>.

Formalized by `MetaMathlibExt.munagi_restricted_compositions`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MunagiRestrictedCompositions.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MunagiRestrictedCompositions.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/index.html#munagi-restricted-compositions).

## Palindromic compositions without 2's

For an integer $m \ge 0$, let $C(m)$ be the number of
compositions of $m$ (finite sequences of positive integers with sum $m$) with no part equal to
$2$, so that $C(0) = 1$ counts the empty composition, and set $C(m) = 0$ for $m < 0$. For a
natural number $n$, let $P(n)$ be the number of such compositions of $n$ that are palindromes.
Then for every natural number $k$, $P(2k) = C(k+1)$ and $P(2k+1) = C(k+1) + C(k-1)$, and the
generating function $G_P(x) = \sum_{n \ge 0} P(n)\, x^n$ satisfies
$(1 - x^2 - x^3)\, G_P(x) = 1 + x$ as formal power series with integer coefficients.

The generating-function identity is the source's $G_P(z) = (1 + z)/(1 - z^2 - z^3)$ cleared of
denominators.

## Sources

- Phyllis Chinn and Silvia Heubach, "Integer Sequences Related to Compositions without 2's," Journal of Integer Sequences 6 (2003), Article 03.2.3, Theorem 10, lines 462–471, <https://cs.uwaterloo.ca/journals/JIS/VOL6/Heubach/heubach5.tex>.

Formalized by `MetaMathlibExt.palindromic_compositions_without_two`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PalindromicCompositionsWithoutTwo.lean, line 840](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PalindromicCompositionsWithoutTwo.lean#L840). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/index.html#palindromic-compositions-without-two).

## Roots-of-unity partial fraction identity

Let $\alpha < \beta$ be natural numbers and
let $\zeta = e^{2 \pi i / \beta}$. For every complex number $u$ with $1 - u^\beta \ne 0$,

$$\frac{u^\alpha}{1 - u^\beta} =
\frac{1}{\beta} \sum_{k=0}^{\beta - 1} \frac{\zeta^{-k \alpha}}{1 - \zeta^k u}.$$

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Lemma 7 (`jis-2024-24.3.6-lem-7`).

Stated but not proved: `MetaMathlibExt.pow_div_one_sub_pow_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CompositionsOddPartsWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionsOddPartsWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/index.html#pow-div-one-sub-pow-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions)
