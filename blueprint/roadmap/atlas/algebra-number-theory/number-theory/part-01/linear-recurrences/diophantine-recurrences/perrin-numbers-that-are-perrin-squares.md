---
declaration: section
origin: cited
lean: MetaMathlibExt.perrinNeg, MetaMathlibExt.perrinNeg_bridge, MetaMathlibExt.perrinNeg_rec, MetaMathlibExt.perrinNeg_small_values, MetaMathlibExt.perrinSequence_eq_sq_iff, MetaMathlibExt.perrinNeg_eq_pm_perrinSequence_sq, MetaMathlibExt.perrinSequence_ne_perrinNeg_sq, MetaMathlibExt.perrinNeg_eq_pm_perrinNeg_sq
statement: formalized
---

# Perrin numbers that are Perrin squares

13 results, 4 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html).

## Perrin sequence at negative indices

The Perrin sequence $R_k$, given by $R_0 = 3$,
$R_1 = 0$, $R_2 = 2$ and $R_{k+3} = R_{k+1} + R_k$, extends uniquely to all integers $k$ by
running the recurrence backward. This defines the integers $R_{-n}$ for natural numbers $n$:
$R_0 = 3$, $R_{-1} = -1$, $R_{-2} = 1$ and $R_{-(n+3)} = R_{-n} - R_{-(n+2)}$ for every $n \ge 0$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorems 2–4.

Formalized by `MetaMathlibExt.perrinNeg`, a definition declared in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg).

## The Perrin sequence and its backward extension fit together at index zero

Write $R_n$
for the Perrin sequence and $R_{-n}$ for its extension to negative indices, for natural numbers
$n$. The two definitions give the same value at index $0$, and the Perrin recurrence holds across
index $0$: $R_2 = R_0 + R_{-1}$ and $R_1 = R_{-1} + R_{-2}$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorems 2–4.

Formalized by `MetaMathlibExt.perrinNeg_bridge`, a theorem declared in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-bridge).

## Perrin recurrence at negative indices

Let $R_{-k}$ denote the Perrin sequence extended
to negative indices. For every natural number $n$, $R_{-n} = R_{-(n+2)} + R_{-(n+3)}$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorems 2–4.

Formalized by `MetaMathlibExt.perrinNeg_rec`, a theorem declared in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-rec).

## Some values of the Perrin sequence at negative indices

The Perrin sequence $R_k$
extended to negative indices satisfies $R_{-5} = 4$, $R_{-18} = 25$,
$R_{-1} = R_{-7} = R_{-11} = R_{-29} = -1$ and $R_{-2} = 1$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorems 2 and 4.

Formalized by `MetaMathlibExt.perrinNeg_small_values`, a theorem declared in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-small-values).

## Perrin numbers that are squares of Perrin numbers

Let $R_n$ denote the $n$-th term of
the Perrin sequence. For positive integers $n$ and $m$, $R_n = R_m^2$ holds if and only if
$n = m = 1$ (where $R_1 = 0 = R_1^2$).

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 1.

Stated but not proved: `MetaMathlibExt.perrinSequence_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-sequence-eq-sq-iff).

## Negative-index Perrin numbers equal to plus or minus a Perrin square

Let $R_k$ denote the
Perrin sequence, extended to negative indices. The pairs of positive integers $(n, m)$ with
$R_{-n} = R_m^2$ or $R_{-n} = -R_m^2$ are exactly $(5, 2)$, $(5, 4)$, $(18, 5)$ and $(18, 6)$;
that is, $R_{-5} = 4 = R_2^2 = R_4^2$ and $R_{-18} = 25 = R_5^2 = R_6^2$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 2.

Stated but not proved: `MetaMathlibExt.perrinNeg_eq_pm_perrinSequence_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-eq-pm-perrin-sequence-sq).

## No positive-index Perrin number is the square of a negative-index one

Let $R_n$ denote
the $n$-th term of the Perrin sequence and $R_{-m}$ the term at index $-m$ of its backward
extension to negative indices. For all positive integers $n$ and $m$, $R_n \ne R_{-m}^2$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 3.

Stated but not proved: `MetaMathlibExt.perrinSequence_ne_perrinNeg_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-sequence-ne-perrin-neg-sq).

## Negative-index Perrin numbers equal to plus or minus a negative-index Perrin square

Let
$R_{-k}$ denote the Perrin sequence extended to negative indices. The pairs of positive integers
$(n, m)$ with $R_{-n} = R_{-m}^2$ or $R_{-n} = -R_{-m}^2$ are exactly the pairs with
$n, m \in \{1, 2, 7, 11, 29\}$, together with $(5, 3)$, $(5, 6)$, $(5, 20)$, $(18, 8)$ and
$(18, 16)$.

Here $R_{-m} = \pm 1$ for $m \in \{1, 2, 7, 11, 29\}$, while
$R_{-5} = 4 = R_{-3}^2 = R_{-6}^2 = R_{-20}^2$ and $R_{-18} = 25 = R_{-8}^2 = R_{-16}^2$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 4.

Stated but not proved: `MetaMathlibExt.perrinNeg_eq_pm_perrinNeg_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-eq-pm-perrin-neg-sq).

## The only zero of the two-sided Perrin sequence

Let $R_n$ denote the $n$-th term of
the Perrin sequence and $R_{-n}$ the term at index $-n$ of its backward extension to negative
indices. For every natural number $n$, $R_n = 0$ if and only if $n = 1$, and $R_{-n} \ne 0$.
Thus $R_1 = 0$ is the only zero of the sequence $(R_k)_{k \in \mathbb{Z}}$.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 5.

Stated but not proved: `MetaMathlibExt.perrin_zero_unique` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-zero-unique).

## Size of the Perrin numbers at negative indices

Let $\alpha$ be a real number with
$\alpha^3 = \alpha + 1$ (the real root of $X^3 - X - 1$), and let $R_{-k}$ denote the Perrin
sequence extended to negative indices. For every integer $k \ge 6$,

$$\alpha^{k/2 - 3 \cdot 10^{15} \log k} < |R_{-k}| < 2.01 \, \alpha^{k/2}.$$

The source quotes this bound from Bravo, Bravo and Luca.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Lemma 1.

Stated but not proved: `MetaMathlibExt.perrinNeg_abs_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#perrin-neg-abs-bounds).

## Matveev's lower bound for two logarithms (complex case)

Let $K$ be a number field of
degree $D = [K : \mathbb{Q}]$ with a field embedding $f : K \to \mathbb{C}$, let
$\eta_1, \eta_2 \in K$ be nonzero, and let $b_1, b_2$ be integers. Let $B$ be a real number with
$|b_1| \le B$ and $|b_2| \le B$, and let $A_1, A_2$ be real numbers with
$A_j \ge \max(D\,h(\eta_j), |\log f(\eta_j)|, 0.16)$ for $j = 1, 2$, where $h$ is the absolute
logarithmic Weil height and $\log$ is the principal branch of the complex logarithm. Put
$\Lambda = f(\eta_1)^{b_1} f(\eta_2)^{b_2} - 1$. If $\Lambda \ne 0$, then

$$|\Lambda| > \exp\bigl(-9.20483 \cdot 10^{11} \, D^2 A_1 A_2 (1 + \log D)(1 + \log(2B))\bigr).$$

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 6.

Stated but not proved: `MetaMathlibExt.matveev_two_logs_complex_lower_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#matveev-two-logs-complex-lower-bound).

## Lower bound for $|x - p/q|$ from bounded partial quotients

Let $x$ be an irrational real
number with continued fraction expansion $[a_0; a_1, a_2, \dots]$, where $a_0 = \lfloor x \rfloor$,
and with convergents $p_k / q_k$. Let $M \ge 1$ and $N \ge 0$ be integers with
$q_N \le M < q_{N+1}$, and let $a$ be a real number with $a \ge a_j$ for every $0 \le j \le N + 1$.
Then

$$\left|x - \frac{p}{q}\right| > \frac{1}{(a + 2) q^2}$$

for all integers $p$ and $q$ with $0 < q < M$.

The source takes $a$ to be the maximum of $a_0, \dots, a_{N+1}$; since the bound weakens as $a$
grows, the two forms are equivalent.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Lemma 3.

Stated but not proved: `MetaMathlibExt.one_div_partialQuotient_bound_lt_abs_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#one-div-partial-quotient-bound-lt-abs-su).

## Convergents minimize $|p - qx|$ up to their denominator

Let $x$ be an irrational real
number with continued fraction convergents $p_k / q_k$, where $p_0 / q_0 = \lfloor x \rfloor / 1$.
If $n > 1$ is a natural number and $p, q$ are integers with $0 < q \le q_n$ and
$p / q \ne p_n / q_n$, then $|p_n - q_n x| < |p - q x|$.

This is Theorem 182 of Hardy and Wright.

## Sources

- Karen J. Sacanamboy, Eric F. Bravo, and Jhon J. Bravo, *Perrin Squares Which Are Again Perrin*, INTEGERS 25 (2025), Article A70, Theorem 10.

Stated but not proved: `MetaMathlibExt.abs_convergent_num_sub_lt_of_le_den` is written with `theorem_wanted` in [WantedExt/NumberTheory/PerrinSquaresWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PerrinSquaresWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html#abs-convergent-num-sub-lt-of-le-den).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perrin numbers that are Perrin squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/perrin-numbers-that-are-perrin-squares)
