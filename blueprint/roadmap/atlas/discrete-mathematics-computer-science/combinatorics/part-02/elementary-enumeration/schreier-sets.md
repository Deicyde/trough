---
declaration: section
origin: cited
lean: MetaMathlibExt.schreierCount, MetaMathlibExt.maximalSchreierCount, MetaMathlibExt.schreierPadovan, MetaMathlibExt.maximalSchreierPadovan, MetaMathlibExt.schreierPadovan_rec, MetaMathlibExt.maximalSchreierPadovan_rec, MetaMathlibExt.schreierPadovan_small, MetaMathlibExt.maximalSchreierPadovan_small
statement: formalized
---

# Schreier sets

96 results, 61 proved and 35 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html).

## Number of (p, q)-Schreier sets with given maximum

For natural numbers $p$, $q$ and $n$,
$|S^{p/q}_n|$ is the number of $(p, q)$-Schreier sets with maximum $n$, that is, of subsets
$F \subseteq \{1, \dots, n\}$ with $n \in F$ and $p|F| \le qx$ for every $x \in F$ (equivalently,
$p|F| \le q \min F$).

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.schreierCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-count).

## Number of maximal $(p, q)$-Schreier sets

For natural numbers $p$, $q$ and $n$,
$|M^{p/q}_n|$ is the number of maximal $(p, q)$-Schreier sets with maximum $n$, that is, of sets
$F \subseteq \{1, \dots, n\}$ with $n \in F$ and $q \min F = p |F|$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.maximalSchreierCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-count).

## Padovan-like sequence for Schreier sets

For natural numbers $p$ and $q$, the sequence
$a_{p,q,n}$, $n \ge 0$, is defined as follows. If $q \ge 1$ and $n \ge p + q$, then
$a_{p,q,n} = a_{p,q,n-q} + a_{p,q,n-p-q}$. Otherwise, if $p \ge q$, then $a_{p,q,n} = 0$ for
$n < p - q$ and $a_{p,q,n} = 1$ for $n \ge p - q$; and if $p < q$, then $a_{p,q,n} = 1$ for
$n < 2p$ and $a_{p,q,n} = 2$ for $n \ge 2p$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.schreierPadovan`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-padovan).

## Padovan-like sequence of maximal Schreier sets

For natural numbers $p$ and $q$, the
sequence $a^{(m)}_{p,q,n}$, $n \ge 0$, is defined as follows. If $q \ge 1$ and $n \ge p + q$, then
$a^{(m)}_{p,q,n} = a^{(m)}_{p,q,n-q} + a^{(m)}_{p,q,n-p-q}$. Otherwise, if $q \le p$, then
$a^{(m)}_{p,q,n}$ is $1$ for $n = p - q$ and $0$ for every other $n$, and if $p < q$, then
$a^{(m)}_{p,q,n}$ is $1$ for $n = 2p$ and $0$ for every other $n$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.maximalSchreierPadovan`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-padovan).

## Recurrence for the Padovan-like sequence

For natural numbers $p$, $q$ and $n$ with
$q \ge 1$ and $n \ge p + q$, the Padovan-like sequence satisfies
$a_{p,q,n} = a_{p,q,n-q} + a_{p,q,n-p-q}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.schreierPadovan_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-padovan-rec).

## Recurrence for the Padovan-like sequence of maximal Schreier sets

For natural numbers
$p$, $q$ and $n$ with $q \ge 1$ and $n \ge p + q$, the Padovan-like sequence $a^{(m)}_{p,q,n}$ of
maximal Schreier sets satisfies $a^{(m)}_{p,q,n} = a^{(m)}_{p,q,n-q} + a^{(m)}_{p,q,n-p-q}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 1.

Formalized by `MetaMathlibExt.maximalSchreierPadovan_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-padovan-rec).

## Small values of the Padovan-like sequences

For $n = 0, 1, \dots, 7$, the Padovan-like
sequence $a_{1,2,n}$ takes the values $1, 1, 2, 2, 3, 4, 5, 7$, and $a_{2,1,n}$ takes the values
$0, 1, 1, 1, 2, 3, 4, 6$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Table 3.

Formalized by `MetaMathlibExt.schreierPadovan_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-padovan-small).

## First values of the Padovan-like sequences of maximal Schreier sets

For
$n = 0, 1, \dots, 7$, the Padovan-like sequence $a^{(m)}_{1,2,n}$ of maximal Schreier sets takes
the values $0, 0, 1, 0, 1, 1, 1, 2$, and $a^{(m)}_{2,1,n}$ takes the values
$0, 1, 0, 0, 1, 1, 1, 2$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Table 4.

Formalized by `MetaMathlibExt.maximalSchreierPadovan_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-padovan-small).

## Small values of the (1, 2)-Schreier counts

For $n = 1, 2, 3, 4$, the number $|S^{1/2}_n|$
of $(1, 2)$-Schreier sets with maximum $n$ takes the values $1, 2, 3, 5$, and the number
$|M^{1/2}_n|$ of maximal $(1, 2)$-Schreier sets with maximum $n$ takes the values $0, 1, 1, 1$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Tables 1 and 2.

Formalized by `MetaMathlibExt.schreierCount_one_two_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-count-one-two-small).

## Sequences satisfying a polynomial

Let $P = c_0 + c_1 x + \dots + c_r x^r$ be a real
polynomial, where $r$ is the degree of $P$ (and $r = 0$ for $P = 0$). A real sequence
$(a_n)_{n \ge 0}$ satisfies $P$ if $c_0 a_n + c_1 a_{n-1} + \dots + c_r a_{n-r} = 0$ for every
$n \ge r$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 4, Definition 4.

Formalized by `MetaMathlibExt.SatisfiesPoly`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#satisfies-poly).

## Every sequence satisfies the zero polynomial

Every real sequence $(a_n)_{n \ge 0}$
satisfies the zero polynomial.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Section 4, Definition 4.

Formalized by `MetaMathlibExt.satisfiesPoly_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#satisfies-poly-zero).

## Schreier counts as Padovan-like sequences

Write $a_{p,q,k}$ and $a^{(m)}_{p,q,k}$ for the
Padovan-like sequences for Schreier sets and for maximal Schreier sets. For positive integers $p$,
$q$ and $n$, the number $|S^{p/q}_n|$ of $(p, q)$-Schreier sets with maximum $n$ equals
$a_{p,q,(n-1)q}$, and the number $|M^{p/q}_n|$ of maximal $(p, q)$-Schreier sets with maximum $n$
equals $a^{(m)}_{p,q,(n-1)q}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Theorem 1 (`jis-2026-26.2.2-thm-1`).

Stated but not proved: `MetaMathlibExt.schreierCount_eq_schreierPadovan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-count-eq-schreier-padovan).

## Closed formula and recurrence for Schreier counts

Let $p$ and $q$ be positive integers,
and write $|S^{p/q}_n|$ for the number of $(p, q)$-Schreier sets with maximum $n$. For every
natural number $n$,

$$|S^{p/q}_n| = \sum_{i=1}^{\lfloor (n+1)q/(p+q) \rfloor} \binom{n - \lceil pi/q \rceil}{i - 1},$$

and for every $n \ge p + q + 1$,

$$|S^{p/q}_n| = \sum_{i=1}^{q} (-1)^{i+1} \binom{q}{i} |S^{p/q}_{n-i}| + |S^{p/q}_{n-(p+q)}|.$$

The printed initial-term formula has $\lceil ni/q \rceil$ in place of $\lceil pi/q \rceil$, which is
false (for $p = 1$, $q = 2$, $n = 2$ one has $|S^{1/2}_2| = 2$ but the printed sum is $1$);
$\lceil pi/q \rceil$ is the paper's own formula (Section 3, equation for $|S^{p/q}_n|$). The
corollary states the formula for $1 \le n \le p + q$; it holds for every $n$, so the range
restriction is dropped.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Corollary 2 (`jis-2026-26.2.2-cor-2`).

Stated but not proved: `MetaMathlibExt.schreierCount_formula_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-count-formula-and-recurrence).

## Closed form and recurrence for maximal $(p, q)$-Schreier sets

Let $p$ and $q$ be positive
integers, put $p' = p / \gcd(p, q)$ and $q' = q / \gcd(p, q)$, and for each $n$ let
$|M^{p/q}_n|$ be the number of maximal $(p, q)$-Schreier sets with maximum $n$, that is, of sets
$F \subseteq \{1, \dots, n\}$ with $n \in F$ and $q \min F = p |F|$. For each $n$, let $K_n$ be
the set of integers $k$ with $1 \le k \le \lfloor (n+1)/(p'+q') \rfloor$ and $q'k \ge 2$, and let
$\delta_n$ be $1$ if $q' = 1$ and $n = p'$, and $0$ otherwise. Then for every $n \ge 0$,

$$|M^{p/q}_n| = \sum_{k \in K_n} \binom{n - p'k - 1}{q'k - 2} + \delta_n,$$

and for every $n \ge p + q + 1$,

$$|M^{p/q}_n| = \sum_{i=1}^{q} (-1)^{i+1} \binom{q}{i} |M^{p/q}_{n-i}| + |M^{p/q}_{n-(p+q)}|.$$

The paper prints the first formula as a sum over all $1 \le k \le \lfloor (n+1)/(p'+q') \rfloor$,
without $\delta_n$, and only for $1 \le n \le p + q$. Read with binomial coefficients vanishing
at negative lower index, it fails at $p = q = n = 1$, where $|M^{1/1}_1| = 1$ but the sum is $0$;
the term $\delta_n$ counts the singleton $\{n\}$, as in equation (10) of the paper's proof of
Theorem 1.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Corollary 3 (`jis-2026-26.2.2-cor-3`).

Stated but not proved: `MetaMathlibExt.maximalSchreierCount_formula_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-count-formula-and-recur).

## A sequence satisfying a polynomial satisfies its multiples

Let $P$ and $Q$ be real
polynomials with $P \mid Q$. If a real sequence $(a_n)_{n \ge 0}$ satisfies $P$, then it
satisfies $Q$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Lemma 5 (`jis-2026-26.2.2-lem-5`).

Stated but not proved: `MetaMathlibExt.SatisfiesPoly.of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#of-dvd).

## Counting $(p, 1)$-Schreier sets by maximal $(p, 1)$-Schreier sets

Fix a positive integer
$p$. For each $m$, let $|S^{p/1}_m|$ be the number of sets $F \subseteq \{1, \dots, m\}$ with
$m \in F$ and $\min F \ge p |F|$, and let $|M^{p/1}_m|$ be the number of those with
$\min F = p |F|$. Then $|S^{p/1}_n| = |M^{p/1}_{n+p+1}|$ for every natural number $n$.

The paper states this for $n \ge 1$; at $n = 0$ both sides are $0$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Theorem 8 (`jis-2026-26.2.2-thm-8`).

Stated but not proved: `MetaMathlibExt.schreierCount_eq_maximalSchreierCount_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-count-eq-maximal-schreier-count).

## Maximal $(1, q)$-Schreier sets counted by $(1, q)$-Schreier sets

Fix a positive integer
$q$. For each $m$, let $|S^{1/q}_m|$ be the number of sets $F \subseteq \{1, \dots, m\}$ with
$m \in F$ and $q \min F \ge |F|$, and let $|M^{1/q}_m|$ be the number of those with
$q \min F = |F|$. Then $|M^{1/q}_n| = 2|S^{1/q}_n| - |S^{1/q}_{n+1}|$ for every positive integer
$n$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Linear Recurrences of Generalized Schreier Sets Revisited*, Journal of Integer Sequences 29 (2026), Article 26.2.2, Theorem 9 (`jis-2026-26.2.2-thm-9`).

Stated but not proved: `MetaMathlibExt.maximalSchreierCount_eq_two_mul_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedSchreierPadovanWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#maximal-schreier-count-eq-two-mul-sub).

## Schreier sets

A finite set $A$ of natural numbers is *Schreier* if $|A| \le a$ for
every $a \in A$; equivalently, $A$ is empty or $\min A \ge |A|$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.IsSchreier`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#is-schreier).

## Strong Schreier sets

For a natural number $\ell$, a finite set $A$ of natural numbers is
*$\ell$-strong Schreier* if $\ell |A| + 1 \le a + \ell$ for every $a \in A$; equivalently, $A$ is
empty or $\min A \ge \ell |A| - \ell + 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.IsStrongSchreier`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#is-strong-schreier).

## Sparse sets

A finite set of natural numbers is *sparse* if the differences between
consecutive elements in increasing order are non-decreasing.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.IsSparse`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#is-sparse).

## Strongly sparse sets

A finite set of natural numbers is *strongly sparse* if the
differences between consecutive elements in increasing order are strictly increasing.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.IsStronglySparse`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#is-strongly-sparse).

## Partitions into exactly $k$ parts

For natural numbers $u$ and $k$, $p(u, k)$ is the
number of partitions of $u$ into exactly $k$ parts.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionExactCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-exact-count).

## The partition number $p(u)$

For a natural number $u$, $p(u)$ is the number of partitions
of $u$, that is, of multisets of positive integers summing to $u$; in particular $p(0) = 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-count).

## Number of Schreier sparse sets with given minimum and maximum

For natural numbers $n$
and $m$, $|F_{n,m}|$ is the number of sets $F \subseteq \{1, \dots, n\}$ that are Schreier and
sparse, contain $n$, and have minimum $m$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.schreierSparseMinCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-sparse-min-count).

## Number of Schreier sparse sets with maximum $n$

For a natural number $n$, $|F_n|$ is the
number of sets $F \subseteq \{1, \dots, n\}$ with $n \in F$ that are Schreier and sparse.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.schreierSparseCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-sparse-count).

## Number of sparse strong Schreier sets with maximum $n$

For natural numbers $n$ and
$\ell$, $|A_{n,\ell}|$ is the number of sets $A \subseteq \{1, \dots, n\}$ with $n \in A$ that
are sparse and $\ell$-strong Schreier.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.sparseStrongCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#sparse-strong-count).

## Number of strongly sparse strong Schreier sets with a given maximum

For natural numbers
$n$ and $\ell$, $|A^s_{n,\ell}|$ is the number of sets $A \subseteq \{1, \dots, n\}$ with $n \in A$
that are strongly sparse, meaning that the differences between consecutive elements of $A$ in
increasing order are strictly increasing, and $\ell$-strong Schreier, meaning that every element
of $A$ is at least $\ell|A| - \ell + 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.stronglySparseStrongCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strongly-sparse-strong-count).

## Number of strong Schreier sets with a given maximum

For natural numbers $n$ and $\ell$,
$|B_{n,\ell}|$ is the number of sets $B \subseteq \{1, \dots, n\}$ with $n \in B$ that are
$\ell$-strong Schreier, that is, every element of $B$ is at least $\ell|B| - \ell + 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.strongSchreierCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strong-schreier-count).

## Number of strong Schreier sets of given size with maximum $n$

For natural numbers $n$,
$\ell$ and $m$, $|B_{n,\ell,m}|$ is the number of $\ell$-strong Schreier sets
$B \subseteq \{1, \dots, n\}$ with $n \in B$ and exactly $m$ elements.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.strongSchreierCardCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strong-schreier-card-count).

## Partitions with all parts at least a given size

For natural numbers $n$ and $\ell$,
$|E_{n,\ell}|$ is the number of partitions of $n$ all of whose parts are at least $\ell$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionMinPartCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-min-part-count).

## Partitions into distinct parts at least $\ell$

For natural numbers $n$ and $\ell$, let
$E^d_{n,\ell}$ be the set of partitions of $n$ into pairwise distinct parts, each at least
$\ell$. This is its number of elements $|E^d_{n,\ell}|$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionDistinctMinPartCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-distinct-min-part-count).

## Partitions with a given number of parts, all at least a given size

For natural numbers
$n$, $\ell$ and $k$, $|E_{n,\ell,k}|$ is the number of partitions of $n$ into exactly $k$ parts,
all of which are at least $\ell$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionMinPartExactCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-min-part-exact-count).

## Partitions with a given gap between the two largest parts

For natural numbers $n$,
$\ell$, $k$ and $q$, $|E_{n,\ell,k,q}|$ is the number of partitions of $n$ into exactly $k$ parts,
all at least $\ell$, whose largest part exceeds the second largest part (counted with
multiplicity) by exactly $q$; such a partition has at least two parts, so the count is $0$ for
$k < 2$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionMinPartGapCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-min-part-gap-count).

## Partitions avoiding parts from 2 up to a bound

For natural numbers $n$ and $\ell$,
$|G_{n,\ell}|$ is the number of partitions of $n$ none of whose parts lies in
$\{2, \dots, \ell\}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionNoSmallPartCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-no-small-part-count).

## Partitions avoiding parts from 2 up to a bound and large even parts

For natural numbers
$n$ and $\ell$, $|H_{n,\ell}|$ is the number of partitions of $n$ none of whose parts lies in
$\{2, \dots, \ell\}$ and none of whose parts is an even number greater than $2\ell$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionNoSmallNoEvenCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-no-small-no-even-count).

## Compositions with exactly $s$ parts, each at least $v$

For natural numbers $u$, $v$
and $s$, $c(u, v, s)$ is the number of compositions of $u$ (ordered sequences of positive
integers summing to $u$) into exactly $s$ parts, each at least $v$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.compositionMinPartExactCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#composition-min-part-exact-count).

## Compositions with parts at least $v$

For natural numbers $u$ and $v$, $c(u, v)$ is the
number of compositions of $u$ (ordered sequences of positive integers summing to $u$) all of
whose parts are at least $v$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.compositionMinPartCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#composition-min-part-count).

## The refined Schreier family $F_{n,\ell}$

For natural numbers $n$ and $\ell$, a finite
set $A$ of natural numbers belongs to $F_{n,\ell}$ if $n + 1$ is the largest element of $A$,
$A$ has at least three elements, $A$ is sparse and $\ell$-strong Schreier, and the two largest
elements $a < b$ of $A$ below $n + 1$ satisfy $n + 1 + a = 2b$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.IsRefinedSchreier`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#is-refined-schreier).

## Refined Schreier count

For natural numbers $n$ and $\ell$, $|F_{n,\ell}|$ is the number of
finite sets $A$ of natural numbers such that $n + 1 \in A$, every element of $A$ is at most
$n + 1$, $A$ has at least three elements, $A$ is sparse and $\ell$-strong Schreier, and the two
largest elements $a < b$ of $A$ below $n + 1$ satisfy $n + 1 + a = 2b$. Every such set is
contained in $\{0, \dots, n + 1\}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.refinedSchreierCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#refined-schreier-count).

## Refined Schreier sets with a given number of elements

For natural numbers $n$ and
$\ell$, let $F_{n,\ell}$ be the family of finite sets $A$ of natural numbers such that $A$ has
largest element $n + 1$ and at least three elements, $A$ is sparse (the differences of
consecutive elements, in increasing order, are non-decreasing) and $\ell$-strong Schreier
($\ell|A| + 1 \le a + \ell$ for every $a \in A$), and the second and third largest elements
$b > a$ of $A$ satisfy $n + 1 + a = 2b$. For a natural number $k$, $|F_{n,\ell,k}|$ is the
number of sets in $F_{n,\ell}$ with exactly $k$ elements.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.refinedSchreierCardCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#refined-schreier-card-count).

## Refined Schreier sets with a given size and minimum

For natural numbers $n$ and
$\ell$, let $F_{n,\ell}$ be the family of finite sets $A$ of natural numbers such that $A$ has
largest element $n + 1$ and at least three elements, $A$ is sparse (the differences of
consecutive elements, in increasing order, are non-decreasing) and $\ell$-strong Schreier
($\ell|A| + 1 \le a + \ell$ for every $a \in A$), and the second and third largest elements
$b > a$ of $A$ satisfy $n + 1 + a = 2b$. For natural numbers $k$ and $q$, $|F_{n,\ell,k,q}|$
is the number of sets in $F_{n,\ell}$ with exactly $k$ elements whose smallest element is
$q$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.refinedSchreierCardMinCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#refined-schreier-card-min-count).

## Schreier sparse sets with given minimum and maximum

For natural numbers $m$ and $n$
with $m + 1 \le n$, the number of Schreier sparse sets $F \subseteq \{1, \dots, n\}$ with
$n \in F$ and $\min F = m + 1$ equals $p(n - 1, m)$, the number of partitions of $n - 1$ into
exactly $m$ parts.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Proposition 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.schreierSparseMinCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-sparse-min-count-eq).

## Counting Schreier sparse sets by partition numbers

For every integer $n \ge 1$, the
number of Schreier sparse sets $F \subseteq \{1, \dots, n\}$ with $n \in F$ equals $p(n - 1)$,
the number of partitions of $n - 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Corollary 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.schreierSparseCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-sparse-count-eq).

## Sparse strong Schreier sets as a sum of partition counts

For every integer $n \ge 1$
and every natural number $\ell$, the number of sparse $\ell$-strong Schreier sets
$A \subseteq \{1, \dots, n\}$ with $n \in A$ equals $\sum_{i=0}^{n-1} |E_{i,\ell+1}|$, where
$|E_{i,\ell+1}|$ is the number of partitions of $i$ into parts that are all at least $\ell + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.sparseStrongCount_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#sparse-strong-count-eq-sum).

## Strongly sparse strong Schreier sets and partitions into distinct parts

For all natural
numbers $n \ge 1$ and $\ell \ge 0$, the number $|A^s_{n,\ell}|$ of strongly sparse $\ell$-strong
Schreier sets $A \subseteq \{1, \dots, n\}$ with $n \in A$ equals
$\sum_{i=0}^{n-1} |E^d_{i,\ell+1}|$, where $|E^d_{i,\ell+1}|$ is the number of partitions of $i$
into distinct parts that are all at least $\ell + 1$ (so $|E^d_{0,\ell+1}| = 1$). Here $A$ is
strongly sparse when the differences between consecutive elements of $A$, listed in increasing
order, are strictly increasing, and $\ell$-strong Schreier when every element of $A$ is at least
$\ell|A| - \ell + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.stronglySparseStrongCount_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strongly-sparse-strong-count-eq-sum).

## Sparse strong Schreier sets and partitions avoiding small parts

For all integers
$n \ge 1$ and $\ell \ge 1$, the number of sparse $\ell$-strong Schreier sets
$A \subseteq \{1, \dots, n\}$ with $n \in A$ equals the number of partitions of $n - 1$ with no
part in $\{2, \dots, \ell\}$.

The identity fails at $\ell = 0$; the paper's $\mathbb{N}$ is the positive integers.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.sparseStrongCount_eq_noSmall` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#sparse-strong-count-eq-no-small).

## Strongly sparse strong Schreier sets and partitions with restricted parts

For all natural
numbers $n \ge 1$ and $\ell \ge 1$, the number $|A^s_{n,\ell}|$ of strongly sparse $\ell$-strong
Schreier sets $A \subseteq \{1, \dots, n\}$ with $n \in A$ equals $|H_{n-1,\ell}|$, the number of
partitions of $n - 1$ with no part in $\{2, \dots, \ell\}$ and no even part greater than $2\ell$.
Here $A$ is strongly sparse when the differences between consecutive elements of $A$, listed in
increasing order, are strictly increasing, and $\ell$-strong Schreier when every element of $A$ is
at least $\ell|A| - \ell + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.stronglySparseStrongCount_eq_noSmallNoEven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strongly-sparse-strong-count-eq-no-small).

## Strong Schreier sets of given size and compositions

For all integers $n \ge 1$ and
$m \ge 1$ and every natural number $\ell$, the number of $\ell$-strong Schreier sets
$B \subseteq \{1, \dots, n\}$ with $n \in B$ and exactly $m$ elements equals the number of
compositions of $n + \ell$ into exactly $m$ parts, each at least $\ell + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.strongSchreierCardCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strong-schreier-card-count-eq).

## Strong Schreier sets with a given maximum are counted by compositions

For all natural
numbers $n \ge 1$ and $\ell \ge 0$, the number $|B_{n,\ell}|$ of $\ell$-strong Schreier sets
$B \subseteq \{1, \dots, n\}$ with $n \in B$ equals $c(n + \ell, \ell + 1)$, the number of
compositions of $n + \ell$ into parts that are all at least $\ell + 1$. Here a set $B$ is
$\ell$-strong Schreier when every element of $B$ is at least $\ell|B| - \ell + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Theorem 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.strongSchreierCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#strong-schreier-count-eq).

## Refined Schreier sets with a given minimum and partitions with a given top gap

Let
$n$, $\ell$, $k$ and $q$ be natural numbers with $n \ge \ell + 1$, $k \ge 2$ and $q \ge 1$.
Let $F_{n,\ell}$ be the family of finite sets $A$ of natural numbers such that $A$ has largest
element $n + 1$ and at least three elements, $A$ is sparse (the differences of consecutive
elements, in increasing order, are non-decreasing) and $\ell$-strong Schreier
($\ell|A| + 1 \le a + \ell$ for every $a \in A$), and the second and third largest elements
$b > a$ of $A$ satisfy $n + 1 + a = 2b$. Then the number $|F_{n,\ell,k+1,\ell k+q}|$ of sets
in $F_{n,\ell}$ with exactly $k + 1$ elements and smallest element $\ell k + q$ equals the
number $|E_{n,\ell+1,k,q-1}|$ of partitions of $n$ into exactly $k$ parts, all at least
$\ell + 1$, whose largest part exceeds the second largest part (counted with multiplicity) by
exactly $q - 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Lemma 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.refinedSchreierCardMinCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#refined-schreier-card-min-count-eq).

## Partitions with a fixed number of large parts and refined Schreier sets

Let $n$,
$\ell$ and $k$ be natural numbers with $n \ge \ell + 1$ and $k \ge 2$. Let $F_{n,\ell}$ be the
family of finite sets $A$ of natural numbers such that $A$ has largest element $n + 1$ and at
least three elements, $A$ is sparse (the differences of consecutive elements, in increasing
order, are non-decreasing) and $\ell$-strong Schreier ($\ell|A| + 1 \le a + \ell$ for every
$a \in A$), and the second and third largest elements $b > a$ of $A$ satisfy
$n + 1 + a = 2b$. Then the number $|E_{n,\ell+1,k}|$ of partitions of $n$ into exactly $k$
parts, all at least $\ell + 1$, equals the number $|F_{n,\ell,k+1}|$ of sets in $F_{n,\ell}$
with exactly $k + 1$ elements.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Corollary 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionMinPartExactCount_eq_refined` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-min-part-exact-count-eq-refine).

## Partitions into large parts and the refined Schreier family

Let $n$ and $\ell$ be
natural numbers with $n \ge \ell + 1$. Let $F_{n,\ell}$ be the family of finite sets $A$ of
natural numbers such that $A$ has largest element $n + 1$ and at least three elements, $A$ is
sparse (the differences of consecutive elements, in increasing order, are non-decreasing) and
$\ell$-strong Schreier ($\ell|A| + 1 \le a + \ell$ for every $a \in A$), and the second and
third largest elements $b > a$ of $A$ satisfy $n + 1 + a = 2b$. Then the number
$|E_{n,\ell+1}|$ of partitions of $n$ into parts that are all at least $\ell + 1$ equals
$|F_{n,\ell}| + 1$.

## Sources

- Kevin Beanland and Hùng Việt Chu, "On Schreier-Type Sets, Partitions, and Compositions", Corollary 13.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SchreierTypeSetsWanted.partitionMinPartCount_eq_refined_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeSetsWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#partition-min-part-count-eq-refined-add).

## Ground multiset for Schreier-type multisets

For natural numbers $s$ and $n$, this is the
multiset $\{1^s, \dots, (n - 1)^s, n\}$, in which each of $1, \dots, n - 1$ has multiplicity $s$
and $n$ appears once.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1 (definition of `A^{(s)}_{p,n}`).

Formalized by `MetaMathlibExt.schreierMultisetPool`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-multiset-pool).

## Number of Schreier-type multisets

For natural numbers $s$, $p$ and $n$, $|A^{(s)}_{p,n}|$
is the number of distinct sub-multisets $F$ of $\{1^s, \dots, (n - 1)^s, n\}$ (each of
$1, \dots, n - 1$ with multiplicity $s$, and $n$ once) such that $n \in F$ and every element of $F$
is at least $p|F|$, where $|F|$ counts multiplicity.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1 (definition of `A^{(s)}_{p,n}`).

Formalized by `MetaMathlibExt.schreierMultisetCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-multiset-count).

## Small values of the Schreier multiset count

Let $|A^{(s)}_{p,n}|$ be the number of
distinct sub-multisets $F$ of $\{1^s, \dots, (n - 1)^s, n\}$ with $n \in F$ and every element of
$F$ at least $p|F|$, where $|F|$ counts multiplicity. Then $|A^{(2)}_{1,4}| = 4$ and
$|A^{(2)}_{2,5}| = 2$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Table 1.

Formalized by `MetaMathlibExt.schreierMultisetCount_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-multiset-count-small).

## Counting colored Schreier-type multisets

For natural numbers $s$, $p$ and $n$, give each
of $1, \dots, n - 1$ the $s$ colors $0, \dots, s - 1$, writing $k_c$ for $k$ with color $c$, and
let $n$ appear once, uncolored. Then $|B^{(s)}_{p,n}|$ is the number of sets $F$ of colored
integers drawn from $\{1_0, \dots, 1_{s-1}, \dots, (n-1)_0, \dots, (n-1)_{s-1}, n\}$ that
contain $n$ and satisfy $\min F \ge p|F|$, where the minimum is taken over the underlying
integers.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1 (definition of `B^{(s)}_{p,n}`).

Formalized by `MetaMathlibExt.coloredSchreierMultisetCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#colored-schreier-multiset-count).

## Small values of the colored Schreier multiset count

The numbers of colored Schreier-type
multisets satisfy $|B^{(2)}_{1,4}| = 6$ and $|B^{(2)}_{2,5}| = 3$ (Table 2 of the paper).

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Table 2.

Formalized by `MetaMathlibExt.coloredSchreierMultisetCount_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#colored-schreier-multiset-count-small).

## First non-multiples of an integer

For natural numbers $u$ and $n$, $G_{u,n}$ is the set of
positive integers $k \le un$ with $u \nmid k$ such that at most $n$ of the integers in $[1, k]$
are not divisible by $u$. For $u \ge 1$ the bound $k \le un$ is automatic, and $G_{u,n}$ is the
set of the first $n$ positive integers not divisible by $u$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1 (definition of `G_{u,n}`).

Formalized by `MetaMathlibExt.firstNonMultiples`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#first-non-multiples).

## The first four positive integers not divisible by 3

The set $G_{3,4}$ of the first four
positive integers not divisible by $3$ is $\{1, 2, 4, 5\}$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1.

Formalized by `MetaMathlibExt.firstNonMultiples_three_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#first-non-multiples-three-four).

## Schreier sets avoiding multiples

For natural numbers $u$ and $n$, let $G_{u,n}$ be the
set of the first $n$ positive integers not divisible by $u$ (taken to be empty when $u = 0$), and
call a finite set $F$ of natural numbers Schreier when every element of $F$ is at least $|F|$.
Then $|D_{u,n}|$ is the number of Schreier sets $F \subseteq G_{u,n}$ with
$\lfloor (un - 1)/(u - 1) \rfloor \in F$.

For $u \le 1$ or $n = 0$ the set $G_{u,n}$ is empty and the count is $0$; otherwise $un - 1$ and
$u - 1$ are positive, so the natural-number subtraction and floor division agree with the real
expression.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 1 (definition of `D_{u,n}`).

Formalized by `MetaMathlibExt.schreierAvoidingMultiplesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-avoiding-multiples-count).

## Small values of the count of Schreier sets avoiding multiples

The numbers of Schreier-type
sets avoiding multiples satisfy $|D_{2,6}| = 12$ and $|D_{3,6}| = 9$ (Table 3 of the paper).

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Table 3.

Formalized by `MetaMathlibExt.schreierAvoidingMultiplesCount_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-avoiding-multiples-count-small).

## Parent sequence b for Schreier-type multisets

For natural numbers $s$ and $p$, the
sequence $b^{(s)}_{p,n}$, $n \ge 0$, is defined by $b^{(s)}_{p,n} = 0$ for $n \le (p - 1)s$,
$b^{(s)}_{p,n} = 1$ for $(p - 1)s < n \le ps + 1$, and
$b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for $n \ge ps + 2$, where $p - 1$ is read
as $0$ when $p = 0$.

The paper indexes from $n = 1$; here $b^{(s)}_{p,0} = 0$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 3 (definition of `b^{(s)}_{p,n}`).

Formalized by `MetaMathlibExt.schreierParentB`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-b).

## The parent sequence b vanishes for small indices

For natural numbers $s$ and $p$, let
$b^{(s)}_{p,n}$ be the parent sequence: $0$ for $n \le (p - 1)s$, $1$ for
$(p - 1)s < n \le ps + 1$, and $b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for
$n \ge ps + 2$, where $p - 1$ is read as $0$ when $p = 0$. Then $b^{(s)}_{p,n} = 0$
for every natural number $n$ with $n \le (p - 1)s$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 3.

Formalized by `MetaMathlibExt.schreierParentB_of_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-b-of-le).

## The parent sequence b equals one on its initial window

For natural numbers $s$ and $p$,
let $b^{(s)}_{p,n}$ be the parent sequence: $0$ for $n \le (p - 1)s$, $1$ for
$(p - 1)s < n \le ps + 1$, and $b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for
$n \ge ps + 2$, where $p - 1$ is read as $0$ when $p = 0$. Then $b^{(s)}_{p,n} = 1$ for every
natural number $n$ with $(p - 1)s < n \le ps + 1$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 3.

Formalized by `MetaMathlibExt.schreierParentB_of_mem`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-b-of-mem).

## Recurrence for the parent sequence b

For natural numbers $s$ and $p$, let
$b^{(s)}_{p,n}$ be the parent sequence: $0$ for $n \le (p - 1)s$, $1$ for
$(p - 1)s < n \le ps + 1$, and $b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for
$n \ge ps + 2$, where $p - 1$ is read as $0$ when $p = 0$. Then
$b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for every natural number $n \ge ps + 2$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 3.

Formalized by `MetaMathlibExt.schreierParentB_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-b-rec).

## The parent sequence $d_{u,n}$

For natural numbers $u$ and $n$, define $d_{u,n}$ by
recursion on $n$: $d_{u,n} = 1$ if $n < 2u$ or $u = 0$, and otherwise
$d_{u,n} = d_{u,n-u} + d_{u,n-2u+1}$.

The paper takes $u \ge 2$ and indexes from $n = 1$, with $d_{u,n} = 1$ for $1 \le n \le 2u - 1$;
here $d_{u,0} = 1$ as well, and the degenerate case $u = 0$ is set to $1$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 4 (definition of `d_{u,n}`).

Formalized by `MetaMathlibExt.schreierParentD`, a definition declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-d).

## Initial values of the parent sequence

For all natural numbers $u$ and $n$ with $n < 2u$,
the parent sequence $d_{u,n}$ satisfies $d_{u,n} = 1$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 4.

Formalized by `MetaMathlibExt.schreierParentD_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-d-of-lt).

## Recurrence for the parent sequence

For all natural numbers $u \ge 1$ and $n \ge 2u$, the
parent sequence $d_{u,n}$ satisfies $d_{u,n} = d_{u,n-u} + d_{u,n-2u+1}$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Section 4.

Formalized by `MetaMathlibExt.schreierParentD_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-d-rec).

## Formula and recurrence for Schreier-type multisets

Let $s, p \ge 1$, and for $n \ge 1$
let $|A^{(s)}_{p,n}|$ be the number of distinct sub-multisets $F$ of
$\{1^s, \dots, (n - 1)^s, n\}$ with $n \in F$ and $\min F \ge p|F|$, where $|F|$ counts
multiplicity. For $1 \le n \le sp + 1$,

$$|A^{(s)}_{p,n}| = \sum_{k=1}^{\lfloor (sn+1)/(sp+1) \rfloor} \binom{n - pk + k - 2}{k - 1},$$

and for $n \ge sp + 2$,

$$|A^{(s)}_{p,n}| = \sum_{i=0}^{s} |A^{(s)}_{p,n-1-ip}|.$$

In the first sum $pk \le n$, so the top $n - pk + k - 2$ is negative only for $k = 1$ and $n = p$,
where the coefficient is $\binom{-1}{0} = 1$; the natural-number subtraction gives
$\binom{0}{0} = 1$ there as well.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Theorem 1.

Stated but not proved: `MetaMathlibExt.schreierMultisetCount_formula_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-multiset-count-formula-and-recu).

## Closed form and recurrence for colored Schreier multiset counts

Let $s \ge 1$ and
$p \ge 1$, and write $|B^{(s)}_{p,n}|$ for the number of colored Schreier-type multisets. For
$1 \le n \le sp + 1$,

$$|B^{(s)}_{p,n}| = \sum_{k=1}^{\lfloor (ns+1)/(ps+1) \rfloor} \binom{(n - kp)s}{k - 1},$$

and for $n \ge sp + 2$,

$$|B^{(s)}_{p,n}| = \sum_{i=0}^{s} \binom{s}{i} \, |B^{(s)}_{p,n-1-ip}|.$$

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Theorem 2.

Stated but not proved: `MetaMathlibExt.coloredSchreierMultisetCount_formula_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#colored-schreier-multiset-count-formula).

## Binomial-sum formula for the parent sequence b

Let $b^{(s)}_{p,n}$ be the parent
sequence: $0$ for $n \le (p - 1)s$, $1$ for $(p - 1)s < n \le ps + 1$, and
$b^{(s)}_{p,n} = b^{(s)}_{p,n-1} + b^{(s)}_{p,n-1-ps}$ for $n \ge ps + 2$. For positive integers
$s$, $p$ and $n$,

$$b^{(s)}_{p,n} = \sum_{i=0}^{\lfloor (n - s(p-1) - 1)/(sp+1) \rfloor}
\binom{n - s(p-1) - 1 - spi}{i},$$

where the sum is empty when $n \le s(p - 1)$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Proposition 1.

Stated but not proved: `MetaMathlibExt.schreierParentB_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-b-eq-sum-choose).

## Colored Schreier multiset counts are a subsequence of the parent sequence

For all
positive integers $s$, $p$ and $n$, the number $|B^{(s)}_{p,n}|$ of colored Schreier-type
multisets equals the term $b^{(s)}_{p,ns-s+1}$ of the parent sequence $b^{(s)}_{p,m}$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Lemma 1.

Stated but not proved: `MetaMathlibExt.coloredSchreierMultisetCount_eq_schreierParentB` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#colored-schreier-multiset-count-eq-schre).

## The non-multiples of an integer as values of a floor function

For every integer $u \ge 2$,
the set $\{\lfloor (un - 1)/(u - 1) \rfloor : n \ge 1\}$, with $n$ ranging over the positive
integers, is the set of positive integers not divisible by $u$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Lemma 2.

Stated but not proved: `MetaMathlibExt.image_floor_eq_nonMultiples` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#image-floor-eq-non-multiples).

## Binomial sum formula for the parent sequence

For all natural numbers $u \ge 2$ and
$n \ge 1$, the parent sequence $d_{u,n}$ satisfies

$$
d_{u,n} = \sum_{i=0}^{\lfloor (n-1)/u \rfloor} \binom{\lfloor (n + (u-1)i - u)/(2u-1) \rfloor}{i}.
$$

The numerator $n + (u-1)i - u$ is negative only when $i = 0$ and $n < u$. There it is read as
$0$ (truncated subtraction), so the term is $\binom{0}{0} = 1$, which agrees with the paper's
$\binom{-1}{0} = 1$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Proposition 2.

Stated but not proved: `MetaMathlibExt.schreierParentD_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-parent-d-eq-sum-choose).

## Schreier sets avoiding multiples are counted by a subsequence of the parent sequence

For every integer $u \ge 2$ and every integer $n \ge 1$, the number $|D_{u,n}|$ of Schreier-type
sets avoiding multiples of $u$ equals the term $d_{u,un-(u-1)}$ of the parent sequence $d_{u,m}$.

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Proposition 3.

Stated but not proved: `MetaMathlibExt.schreierAvoidingMultiplesCount_eq_schreierParentD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-avoiding-multiples-count-eq-sch).

## Fibonacci values and a recurrence for Schreier sets avoiding multiples

Let $u \ge 2$,
write $|D_{u,n}|$ for the number of Schreier-type sets avoiding multiples of $u$, and write $F_n$
for the Fibonacci numbers, with $F_0 = 0$ and $F_1 = 1$. For $1 \le n \le 2u - 1$,
$|D_{u,n}| = F_n$, and for $n \ge 2u$, as an identity of integers,

$$|D_{u,n}| = \sum_{i=1}^{u} (-1)^{i-1} \binom{u}{i} |D_{u,n-i}| + |D_{u,n-2u+1}|.$$

## Sources

- Hùng Việt Chu, Yubo Geng, Julian King, Steven J. Miller, Garrett Tresch and Zachary Louis Vasseur, *Linear Recurrences from Counting Schreier-Type Multisets*, INTEGERS 26 (2026), Article A53, Theorem 3.

Stated but not proved: `MetaMathlibExt.schreierAvoidingMultiplesCount_fib_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SchreierTypeMultisetsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#schreier-avoiding-multiples-count-fib-an).

## Weighted Schreier-type sets

For natural numbers $k$ and $n$, let $\omega_k(E)$ denote the
number of elements of a finite set $E$ that are different from $k$. The weighted Schreier count
$a_{k,n}$ is the number of subsets $E \subseteq \{1, \dots, n\}$ that are empty or satisfy
$\omega_k(E) < \min E$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 1 (definition of `A_{k,n}` and `a_{k,n}`).

Formalized by `MetaMathlibExt.weightedSchreierCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count).

## Weighted Schreier count $a_{1,1}$

The weighted Schreier count $a_{1,1}$ equals $2$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 1, Table 1.

Formalized by `MetaMathlibExt.weightedSchreierCount_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-one-one).

## Weighted Schreier count $a_{2,1}$

The weighted Schreier count $a_{2,1}$ equals $1$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 1, Table 1.

Formalized by `MetaMathlibExt.weightedSchreierCount_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-two-one).

## Weighted Schreier count $a_{3,3}$

The weighted Schreier count $a_{3,3}$ equals $4$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 1, Table 1.

Formalized by `MetaMathlibExt.weightedSchreierCount_three_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-three-three).

## Weighted Schreier count $a_{1,4}$

The weighted Schreier count $a_{1,4}$ equals $6$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 1, Table 1.

Formalized by `MetaMathlibExt.weightedSchreierCount_one_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-one-four).

## Seeded partial sums

Let $M$ be an additive commutative monoid, and let
$s = (s_n)_{n \ge 0}$ (the seed sequence) and $a = (a_n)_{n \ge 0}$ be sequences in $M$. The
seeded partial sums $t^s_{k,n}$, for $k, n \ge 0$, are defined by recursion on $k$:
$t^s_{0,n} = a_n$ and $t^s_{k+1,n} = s_k + \sum_{i\lt n} t^s_{k,i}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 3 (partial sum operator `P_b` and the sequences `t^s_{k,n}`).

Formalized by `MetaMathlibExt.seededPartialSums`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#seeded-partial-sums).

## Iterated partial sums

Let $M$ be an additive commutative monoid and let
$a = (a_n)_{n \ge 0}$ be a sequence in $M$. For $k, m \ge 0$, the $k$-fold iterated partial sum
$P^{(k)}(a)(m)$ is the seeded partial sum $t^s_{k,m}$ of $a$ for the zero seed sequence $s = 0$.
Thus $P^{(0)}(a)(m) = a_m$ and $P^{(k+1)}(a)(m) = \sum_{i\lt m} P^{(k)}(a)(i)$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 3 (definition of `P^{(k)}`).

Formalized by `MetaMathlibExt.iteratedPartialSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#iterated-partial-sum).

## Seeded partial sums start at the seed

Let $M$ be an additive commutative monoid, let
$s = (s_n)_{n \ge 0}$ and $a = (a_n)_{n \ge 0}$ be sequences in $M$, and write $t^s_{k,n}$ for
the seeded partial sums of $a$ with seed sequence $s$. Then $t^s_{k+1,0} = s_k$ for every
$k \ge 0$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 3 (partial sum operator `P_b`).

Formalized by `MetaMathlibExt.seededPartialSums_succ_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#seeded-partial-sums-succ-zero).

## The first iterated partial sum

Let $M$ be an additive commutative monoid and let
$(a_n)_{n \ge 0}$ be a sequence in $M$. For every $m \ge 0$, the $1$-fold iterated partial sum
of $(a_n)$ at $m$ is the ordinary partial sum: $P^{(1)}((a_n)_{n \ge 0})(m) = \sum_{i\lt m} a_i$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 3 (definition of `P^{(k)}`).

Formalized by `MetaMathlibExt.iteratedPartialSum_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#iterated-partial-sum-one).

## Recurrence for iterated partial sums

Let $M$ be an additive commutative monoid, let
$a = (a_n)_{n \ge 0}$ be a sequence in $M$, and write $P^{(k)}(a)(m)$ for its $k$-fold iterated
partial sum at $m$. Then for all $k, m \ge 0$,
$P^{(k+1)}(a)(m+1) = P^{(k+1)}(a)(m) + P^{(k)}(a)(m)$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Section 3 (definition of `P^{(k)}`; recurrence used in the proofs of Lemmas 3.3 and 3.4).

Formalized by `MetaMathlibExt.iteratedPartialSum_succ_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#iterated-partial-sum-succ-succ).

## Diagonal weighted Schreier counts

For every natural number $n \ge 1$, the weighted
Schreier count satisfies $a_{n,n} = 2F_n$, where $F_n$ is the $n$-th Fibonacci number
($F_0 = 0$, $F_1 = 1$).

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_diag` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-diag).

## Weighted Schreier counts for $k = 1$

For every natural number $\ell$, the weighted
Schreier count satisfies $a_{1,1+\ell} = F_{\ell+2} + 1$, where $F_j$ is the $j$-th Fibonacci
number ($F_0 = 0$, $F_1 = 1$).

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Theorem 1.2, case `k = 1`.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-one).

## Weighted Schreier counts on and above the diagonal

Let $a_{k,n}$ be the weighted
Schreier count and let $F_n$ denote the Fibonacci numbers, with $F_0 = 0$ and $F_1 = 1$. For all
$k \ge 2$ and $\ell \ge 0$,
$a_{k,k+\ell} = 2\sum_{i=0}^{k-2} \binom{\ell}{i} F_{k-i} + 2\binom{\ell}{k-1} +
\sum_{j=1}^{\ell} \binom{j}{\ell-j+k}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Theorem 1.2, case `k ≥ 2`, `ℓ ≥ 0`.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-add).

## Weighted Schreier counts for $0 < m < k$

For natural numbers $k \ge 2$ and $m$ with
$0 < m < k$, the weighted Schreier count satisfies $a_{k,m} = F_{m+1}$, where $F_j$ is the
$j$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$).

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Theorem 1.2, case `k ≥ 2`, `-k < ℓ < 0`.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_of_pos_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-of-pos-of-lt).

## Weighted Schreier counts equal twice a Fibonacci number for small offsets

Let
$a_{k,n}$ be the weighted Schreier count and let $F_n$ denote the Fibonacci numbers, with
$F_0 = 0$ and $F_1 = 1$. For all $k, \ell \ge 0$ with $k \ge \ell + 2$, we have
$a_{k,k+\ell} = 2F_{k+\ell}$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_add_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-add-of-le).

## Recurrence for weighted Schreier counts

For natural numbers $k$ and $n$ with $k \ge 1$,
$n > k$ and $n > 2$, the weighted Schreier counts satisfy $a_{k,n} = a_{k,n-1} + a_{k-1,n-2}$.
At $k = 1$ the term $a_{0,n-2}$ is the same count with $\omega_0(E)$, the number of elements of
$E$ different from $0$, equal to the number $|E|$ of all elements of $E$, since no element of a
set $E \subseteq \{1, \dots, n-2\}$ equals $0$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Proposition 3.1.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-recurrence).

## Effect of the seed on seeded partial sums

Let $R$ be a commutative ring, let
$a = (a_n)_{n \ge 0}$ and $b = (b_n)_{n \ge 0}$ be sequences in $R$, and write $t^b_{k,n}$ for
the seeded partial sums of $a$ with seed sequence $b$ and $t^0_{k,n}$ for those with the zero
seed sequence. Then for all $k, n \ge 0$,
$t^b_{k,n} - t^0_{k,n} = \sum_{i\lt k} \binom{n}{i} b_{k-1-i}$, where the binomial coefficients
are read as elements of $R$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.seededPartialSums_sub_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#seeded-partial-sums-sub-zero).

## Adding one to a sequence shifts its iterated partial sums by a binomial coefficient

Let $R$ be a commutative ring, let $(a_n)_{n \ge 0}$ be a sequence in $R$, and let $k, m \ge 0$.
Writing $P^{(k)}(x)(m)$ for the $k$-fold iterated partial sum of a sequence $x$ at $m$, we have
$P^{(k)}((a_n + 1)_{n \ge 0})(m) - P^{(k)}((a_n)_{n \ge 0})(m) = \binom{m}{k}$, where
$\binom{m}{k}$ is read as an element of $R$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Lemma 3.3.

Stated but not proved: `MetaMathlibExt.iteratedPartialSum_add_one_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#iterated-partial-sum-add-one-sub).

## Iterated partial sums of shifted Fibonacci numbers

Let $F_n$ denote the Fibonacci
numbers, with $F_0 = 0$ and $F_1 = 1$, and write $P^{(k)}(x)(m)$ for the $k$-fold iterated
partial sum of a sequence $x$ of natural numbers at $m$. Then for all $k, \ell \ge 0$,
$P^{(k)}((F_{n+2})_{n \ge 0})(\ell) = P^{(k)}((F_n)_{n \ge 0})(\ell) +
P^{(k)}((F_n)_{n \ge 0})(\ell + 1)$.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Lemma 3.4.

Stated but not proved: `MetaMathlibExt.iteratedPartialSum_fib_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#iterated-partial-sum-fib-add-two).

## Weighted Schreier counts for $n < k$

For all natural numbers $n < k$, the weighted
Schreier count satisfies $a_{k,n} = F_{n+1}$, where $F_j$ is the $j$-th Fibonacci number
($F_0 = 0$, $F_1 = 1$).

This includes $n = 0$, where $a_{k,0} = 1 = F_1$; the source takes $n$ positive.

## Sources

- Hùng Việt Chu and Zachary Louis Vasseur, *Weighted Schreier-type Sets and the Fibonacci Sequence*, The Fibonacci Quarterly 62 (2024), no. 4, Proposition 3.5.

Stated but not proved: `MetaMathlibExt.weightedSchreierCount_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WeightedSchreierWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html#weighted-schreier-count-of-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schreier sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/schreier-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/elementary-enumeration/schreier-sets)
