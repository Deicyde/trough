---
declaration: section
origin: cited
lean: MetaMathlibExt.generating_function_term_extraction_of_one_third_growth, MetaMathlibExt.generating_function_term_representation_mono_base, MetaMathlibExt.neg_ediv_eq_ediv_add_one_of_not_dvd, MetaMathlibExt.mul_mod_eq_mul_mod_of_mul_lt, MetaMathlibExt.add_one_mod_eq_mod_add_one_of_ne, MetaMathlibExt.emod_emod_eq_abs_mul_ediv_emod_of_neg, MetaMathlibExt.neg_emod_emod_eq_mul_one_add_ediv_emod_of_pos, MetaMathlibExt.exists_mod_mod_representation_of_neg_free_term
statement: formalized
---

# Mod-mod representations of C-recursive sequences

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html).

## Term extraction from the generating function under cube-root growth

Let
$t_0, t_1, t_2, \dots$ be natural numbers and let $c \ge 8$ be a natural number. Suppose that
the real series $\sum_{k \ge 0} t_k c^{-k}$ is summable and that $t_n < c^{n/3}$, a real power,
for every $n \ge 1$. Then for every $n \ge 1$,

$$t_n = \Bigl\lfloor c^{n^2} \sum_{k \ge 0} t_k \, (c^{-n})^k \Bigr\rfloor \bmod c^n.$$

Summability at $c^{-1}$ stands in for the paper's hypothesis that $c^{-1}$ lies inside the
radius of convergence of the generating function. It is implied by that hypothesis but is
strictly weaker, so this statement is stronger than the paper's.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Theorem 2, second part.

Stated but not proved: `MetaMathlibExt.generating_function_term_extraction_of_one_third_growth` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#generating-function-term-extraction-of-o).

## Term extraction from the generating function persists in larger bases

Let
$t_0, t_1, t_2, \dots$ be natural numbers and let $c$, $m$ and $r$ be natural numbers with
$c \ge 2$, $m \ge 2$ and $c \le r$. Suppose that for every $n \ge m$ the real series
$\sum_{k \ge 0} t_k \, (c^{-n})^k$ is summable and

$$t_n = \Bigl\lfloor c^{n^2} \sum_{k \ge 0} t_k \, (c^{-n})^k \Bigr\rfloor \bmod c^n.$$

Then for every $n \ge m$,

$$t_n = \Bigl\lfloor r^{n^2} \sum_{k \ge 0} t_k \, (r^{-n})^k \Bigr\rfloor \bmod r^n.$$

No summability at $r^{-n}$ is assumed: the hypothesis gives $t_n < c^n \le r^n$ for $n \ge m$,
which makes the series at $r^{-n}$ converge.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Corollary 3.

Stated but not proved: `MetaMathlibExt.generating_function_term_representation_mono_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#generating-function-term-representation).

## Floor quotient of a negated non-multiple

Let $A$ and $B$ be integers with $A \ge 1$ and
$B \ge 2$ such that $B$ does not divide $A$. Then
$-\lfloor -A/B \rfloor = \lfloor A/B \rfloor + 1$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma 4.

Stated but not proved: `MetaMathlibExt.neg_ediv_eq_ediv_add_one_of_not_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#neg-ediv-eq-ediv-add-one-of-not-dvd).

## Pulling a factor out of a remainder

Let $a$, $y$ and $C$ be natural numbers with $ay < C$.
Then $(ay) \bmod C = a \cdot (y \bmod C)$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma 5.

Stated but not proved: `MetaMathlibExt.mul_mod_eq_mul_mod_of_mul_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#mul-mod-eq-mul-mod-of-mul-lt).

## Adding one to a remainder without wrap-around

Let $x$ and $C$ be natural numbers with
$C \ge 2$. If $x \bmod C \ne (C - 1) \bmod C$, that is, if $x$ is not congruent to $C - 1$
modulo $C$, then $(x + 1) \bmod C = (x \bmod C) + 1$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma 6.

Stated but not proved: `MetaMathlibExt.add_one_mod_eq_mod_add_one_of_ne` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#add-one-mod-eq-mod-add-one-of-ne).

## Remainder of a remainder, negative residue case

Let $a$, $A$, $B$ and $C$ be integers with
$A > 0$, $B > 0$ and $C \ge 2$ such that $C$ divides $A$, $B$ does not divide $A$, $a < 0$ and
$B \equiv a \pmod C$. Write $\lfloor A/B \rfloor$ for the floor of $A/B$ and $X \bmod M$ for the
remainder of $X$ modulo $M$ in $\{0, 1, \dots, M - 1\}$. If
$|a| \cdot (\lfloor A/B \rfloor \bmod C) < C$, then
$(A \bmod B) \bmod C = |a| \cdot (\lfloor A/B \rfloor \bmod C)$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma 7(i).

Stated but not proved: `MetaMathlibExt.emod_emod_eq_abs_mul_ediv_emod_of_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#emod-emod-eq-abs-mul-ediv-emod-of-neg).

## Remainder of a remainder, positive residue case

Let $a$, $A$, $B$ and $C$ be integers with
$A > 0$, $B > 0$ and $C \ge 2$ such that $C$ divides $A$, $B$ does not divide $A$, $a > 0$ and
$B \equiv a \pmod C$. Write $\lfloor A/B \rfloor$ for the floor of $A/B$ and $X \bmod M$ for the
remainder of $X$ modulo $M$ in $\{0, 1, \dots, M - 1\}$. If
$a + a \cdot (\lfloor A/B \rfloor \bmod C) < C$, then
$((-A) \bmod B) \bmod C = a \cdot \bigl(1 + (\lfloor A/B \rfloor \bmod C)\bigr)$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma 7(ii).

Stated but not proved: `MetaMathlibExt.neg_emod_emod_eq_mul_one_add_ediv_emod_of_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#neg-emod-emod-eq-mul-one-add-ediv-emod-o).

## Mod-mod representation of C-recursive sequences, negative free term

Let
$t_0, t_1, t_2, \dots$ be natural numbers, let $c$ be a natural number, and let $A$ and $B$ be
polynomials with integer coefficients such that $A \ne 0$, $B(0) = 1$ and
$k = \deg A < d = \deg B$. Suppose that $\bigl(\sum_{n \ge 0} t_n z^n\bigr) B(z) = A(z)$ as
formal power series. Let $\tilde A(x) = x^k A(1/x)$ and $\tilde B(x) = x^d B(1/x)$ be the
reversed polynomials, let $\alpha$ be the constant term of $\tilde B$, that is, the leading
coefficient of $B$, and for an integer $x$ put $P_x(n) = x^{n^2} x^{n(d-k)} \tilde A(x^n)$. For
integers $X$ and $M \ne 0$, write $X \bmod M$ for the remainder of $X$ modulo $M$ in
$\{0, 1, \dots, |M| - 1\}$, and set $X \bmod 0 = X$. Suppose that for every $n \ge 1$,

$$t_n = \bigl\lfloor P_c(n) / \tilde B(c^n) \bigr\rfloor \bmod c^n,$$

where the quotient is taken in $\mathbb{Q}$ and is $0$ when $\tilde B(c^n) = 0$. If $\alpha < 0$,
then there is a natural number $r$ such that for every $n \ge 1$,

$$|\alpha| \, t_n = \bigl( P_r(n) \bmod \tilde B(r^n) \bigr) \bmod r^n.$$

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Theorem 8, negative free term.

Stated but not proved: `MetaMathlibExt.exists_mod_mod_representation_of_neg_free_term` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#exists-mod-mod-representation-of-neg-fre).

## Mod-mod representation of C-recursive sequences, positive free term

Let
$t_0, t_1, t_2, \dots$ be natural numbers, let $c$ be a natural number, and let $A$ and $B$ be
polynomials with integer coefficients such that $A \ne 0$, $B(0) = 1$ and
$k = \deg A < d = \deg B$. Suppose that $\bigl(\sum_{n \ge 0} t_n z^n\bigr) B(z) = A(z)$ as
formal power series. Let $\tilde A(x) = x^k A(1/x)$ and $\tilde B(x) = x^d B(1/x)$ be the
reversed polynomials, let $\alpha$ be the constant term of $\tilde B$, that is, the leading
coefficient of $B$, and for an integer $x$ put $P_x(n) = x^{n^2} x^{n(d-k)} \tilde A(x^n)$. For
integers $X$ and $M \ne 0$, write $X \bmod M$ for the remainder of $X$ modulo $M$ in
$\{0, 1, \dots, |M| - 1\}$, and set $X \bmod 0 = X$. Suppose that for every $n \ge 1$,

$$t_n = \bigl\lfloor P_c(n) / \tilde B(c^n) \bigr\rfloor \bmod c^n,$$

where the quotient is taken in $\mathbb{Q}$ and is $0$ when $\tilde B(c^n) = 0$. If $\alpha > 0$,
then there is a natural number $r$ such that for every $n \ge 1$,

$$\alpha \, (t_n + 1) = \bigl( (-P_r(n)) \bmod \tilde B(r^n) \bigr) \bmod r^n.$$

The hypothesis $A \ne 0$ is needed: for $A = 0$ and $B(z) = 1 + z$ the left side is $1$ and the
right side is $0$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Theorem 8, positive free term.

Stated but not proved: `MetaMathlibExt.exists_mod_mod_representation_of_pos_free_term` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#exists-mod-mod-representation-of-pos-fre).

## Single-formula mod-mod representation of C-recursive sequences

Let
$t_0, t_1, t_2, \dots$ be natural numbers, let $c$ be a natural number, and let $A$ and $B$ be
polynomials with integer coefficients such that $A \ne 0$, $B(0) = 1$ and
$k = \deg A < d = \deg B$. Suppose that $\bigl(\sum_{n \ge 0} t_n z^n\bigr) B(z) = A(z)$ as
formal power series. Let $\tilde A(x) = x^k A(1/x)$ and $\tilde B(x) = x^d B(1/x)$ be the
reversed polynomials, let $\alpha$ be the constant term of $\tilde B$, that is, the leading
coefficient of $B$, and for an integer $x$ put $P_x(n) = x^{n^2} x^{n(d-k)} \tilde A(x^n)$. For
integers $X$ and $M \ne 0$, write $X \bmod M$ for the remainder of $X$ modulo $M$ in
$\{0, 1, \dots, |M| - 1\}$, and set $X \bmod 0 = X$. Suppose that for every $n \ge 1$,

$$t_n = \bigl\lfloor P_c(n) / \tilde B(c^n) \bigr\rfloor \bmod c^n,$$

where the quotient is taken in $\mathbb{Q}$ and is $0$ when $\tilde B(c^n) = 0$. Put
$\sigma = \operatorname{sgn} \alpha$; note $\alpha \ne 0$ because $B \ne 0$. Then there is a
natural number $r \ge c$ such that for every $n \ge 1$, writing
$\rho_n = \bigl( (-\sigma P_r(n)) \bmod \tilde B(r^n) \bigr) \bmod r^n$, the rational numbers
satisfy

$$t_n = \frac{-1 - \sigma}{2} + \frac{\rho_n}{|\alpha|}.$$

The hypothesis $A \ne 0$ excludes the zero sequence: for $A = 0$ and $B(z) = 1 + z$ the right
side is $-1$.

## Sources

- M. Prunescu and J. M. Shunia, *On Modular Representations of C-Recursive Integer Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.3, Corollary 9.

Stated but not proved: `MetaMathlibExt.exists_mod_mod_representation_sign` is written with `theorem_wanted` in [WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CRecursiveModularRepresentationsWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html#exists-mod-mod-representation-sign).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mod-mod representations of C-recursive sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mod-mod-representations-of-c-recursive-sequences)
