---
declaration: section
origin: cited
lean: MetaMathlibExt.trinomialCoefficient_self_eq_sum, MetaMathlibExt.motzkin_central_trinomial_recurrence, MetaMathlibExt.motzkinNumber, MetaMathlibExt.motzkinNumber_zero, MetaMathlibExt.motzkinNumber_one, MetaMathlibExt.motzkinNumber_two, MetaMathlibExt.motzkinNumber_eq_sum_range_half, MetaMathlibExt.trinomialCoefficient_succ_eq_add_motzkinNumber
statement: formalized
proof: formalized
---

# Motzkin numbers

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html).

## Central trinomial coefficients as a binomial sum

For every natural number $n$, the
coefficient of $X^n$ in $(1 + X + X^2)^n$ equals
$\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} \binom{2k}{k}$.

Formalized by `MetaMathlibExt.trinomialCoefficient_self_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinCentralTrinomial.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinCentralTrinomial.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#trinomial-coefficient-self-eq-sum).

## Recurrence linking central trinomial coefficients and Motzkin numbers

For $n \in \mathbb{N}$
let $T_n$ be the central trinomial coefficient, the coefficient of $X^n$ in $(1 + X + X^2)^n$.
Let $M : \mathbb{N} \to \mathbb{N}$ be any function with
$M_n = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} C_k$ for every $n$, where $C_k$ is the
$k$-th Catalan number (these sums are the Motzkin numbers). Then for every $n \ge 1$,
$T_{n+1} = T_n + 2n \, M_{n-1}$.

The source attributes the recurrence to Barcucci, Pinzani, and Sprugnoli, "The Motzkin family",
and proves it with hybrid-polynomial operator calculus; the proof here instead uses the binomial
sum for $T_n$ and an elementary termwise binomial identity.

## Sources

- P. Blasiak, G. Dattoli, A. Horzela, K. A. Penson, and K. Zhukovsky, "Motzkin Numbers, Central Trinomial Coefficients and Hybrid Polynomials," Journal of Integer Sequences 11 (2008), Article 08.1.1, Theorem (equation eq34), lines 459–464, https://cs.uwaterloo.ca/journals/JIS/VOL11/Penson/penson131.tex

Formalized by `MetaMathlibExt.motzkin_central_trinomial_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinCentralTrinomial.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinCentralTrinomial.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-central-trinomial-recurrence).

## Motzkin numbers as a Catalan-weighted binomial sum

Let $C_k$ denote the $k$-th Catalan
number (OEIS A000108). For a natural number $n$, the $n$-th Motzkin number (OEIS A001006) is

$$M(n) = \sum_{k=0}^{n} \binom{n}{2k} C_k.$$

The terms with $2k > n$ vanish.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 19 (2).

Formalized by `MetaMathlibExt.motzkinNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number).

## Value of the Motzkin number at 0

The $0$-th Motzkin number is $M(0) = 1$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 19 (2).

Formalized by `MetaMathlibExt.motzkinNumber_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number-zero).

## Value of the Motzkin number at 1

The first Motzkin number is $M(1) = 1$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 19 (2).

Formalized by `MetaMathlibExt.motzkinNumber_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number-one).

## Value of the Motzkin number at 2

The second Motzkin number is $M(2) = 2$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 19 (2).

Formalized by `MetaMathlibExt.motzkinNumber_two`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number-two).

## Truncated Catalan-weighted sum for Motzkin numbers

Let $C_k$ denote the $k$-th Catalan
number. For every natural number $n$, the $n$-th Motzkin number $M(n)$ satisfies

$$M(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} C_k.$$

The terms dropped from the defining sum vanish, since $\binom{n}{2k} = 0$ for $2k > n$.

## Sources

- Geng-Rui Zhang, *Realizability of Some Combinatorial Sequences*, Journal of Integer Sequences 27 (2024), Article 24.3.3, Definition 19 (2).

Formalized by `MetaMathlibExt.motzkinNumber_eq_sum_range_half`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number-eq-sum-range-half).

## Central trinomial recurrence via Motzkin numbers

Write $T(n)$ for the central trinomial
coefficient, the coefficient of $X^n$ in $(1 + X + X^2)^n$, and $M(n)$ for the $n$-th Motzkin
number. For every natural number $n \ge 1$,

$$T(n+1) = T(n) + 2n\,M(n-1).$$

## Sources

- P. Blasiak, G. Dattoli, A. Horzela, K. A. Penson, and K. Zhukovsky, *Motzkin Numbers, Central Trinomial Coefficients and Hybrid Polynomials*, Journal of Integer Sequences 11 (2008), Article 08.1.1, equation (34).

Formalized by `MetaMathlibExt.trinomialCoefficient_succ_eq_add_motzkinNumber`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#trinomial-coefficient-succ-eq-add-motzki).

## The Motzkin recurrence

`M(n + 1) = M(n) + ∑_{k < n} M(k) M(n - 1 - k)`. (Combinatorially, a Motzkin path of
length `n + 1` starts with a flat step, or with an up step whose matching down step splits the
rest into two shorter Motzkin paths.)

## Sources

- R. Donaghey and L. W. Shapiro, *Motzkin numbers*, Journal of Combinatorial Theory, Series A 23 (1977), 291–301.

Formalized by `MetaMathlibExt.motzkinNumber_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/MotzkinNumber.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html#motzkin-number-succ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Motzkin numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/motzkin-numbers)
