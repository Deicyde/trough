---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSDiophantineTuple, MetaMathlibExt.isSDiophantineTuple_two_one_three, MetaMathlibExt.isSDiophantineTuple_two_three_five_one_three_eight, MetaMathlibExt.not_mul_add_one_dvd_mul_add_one, MetaMathlibExt.padicValNat_two_smallest_eq, MetaMathlibExt.dvd_gcd_sub_div_gcd, MetaMathlibExt.not_exists_sDiophantine_system_four, MetaMathlibExt.sDiophantine_quadruple_exponent_cases
statement: formalized
---

# S-Diophantine tuples

13 results, 3 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html).

## $S$-Diophantine tuples

Let $S$ be a finite set of natural numbers. A finite set $s$ of
natural numbers is an $S$-Diophantine tuple if all its elements are positive and, for all
distinct $a, b \in s$, every prime factor of $ab + 1$ lies in $S$. A tuple $(a_1, \dots, a_m)$ of
distinct positive integers is encoded by the set of its entries, which has $m$ elements.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Section 1 (definition of `S`-Diophantine `m`-tuples).

Formalized by `MetaMathlibExt.IsSDiophantineTuple`, a definition declared in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#is-sdiophantine-tuple).

## $(1, 3)$ is a $\{2\}$-Diophantine pair

The set $\{1, 3\}$ is a $\{2\}$-Diophantine
tuple, since $1 \cdot 3 + 1 = 2^2$.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Section 1 (definition of `S`-Diophantine `m`-tuples).

Formalized by `MetaMathlibExt.isSDiophantineTuple_two_one_three`, a theorem declared in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#is-sdiophantine-tuple-two-one-three).

## $(1, 3, 8)$ is a $\{2, 3, 5\}$-Diophantine triple

The set $\{1, 3, 8\}$ is a
$\{2, 3, 5\}$-Diophantine tuple, since $1 \cdot 3 + 1 = 2^2$, $1 \cdot 8 + 1 = 3^2$ and
$3 \cdot 8 + 1 = 5^2$.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Section 1 (definition of `S`-Diophantine `m`-tuples).

Formalized by `MetaMathlibExt.isSDiophantineTuple_two_three_five_one_three_eight`, a theorem declared in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#is-sdiophantine-tuple-two-three-five-one).

## $ac + 1$ does not divide $bc + 1$

If $a < b < c$ are positive integers, then $ac + 1$
does not divide $bc + 1$.

The source states this for $S$-Diophantine triples; that hypothesis is not needed.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 1, quoting Szalay and Ziegler (2013), Lemma 2.1.

Stated but not proved: `MetaMathlibExt.not_mul_add_one_dvd_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#not-mul-add-one-dvd-mul-add-one).

## The two smallest valuations coincide

Let $\ell$ be a prime and $a, b, c, d$ natural
numbers. Put $s_1 = ab + 1$, $s_2 = ac + 1$, $s_3 = ad + 1$, $s_4 = bc + 1$, $s_5 = bd + 1$,
$s_6 = cd + 1$, and let $v_i$ be the $\ell$-adic valuation of $s_i$. Then in each of the tuples
$(v_2, v_3, v_4, v_5)$, $(v_1, v_2, v_5, v_6)$ and $(v_1, v_3, v_4, v_6)$ the minimum value occurs
at two different positions.

Taking $\ell = p$ and $\ell = q$ gives the source's statements for the exponents of a
$\{p, q\}$-Diophantine quadruple. No Diophantine hypothesis is needed: the proof uses only the
identities $abcd = (s_1 - 1)(s_6 - 1) = (s_2 - 1)(s_5 - 1) = (s_3 - 1)(s_4 - 1)$.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 2, quoting Szalay and Ziegler (2013), Proposition 1.

Stated but not proved: `MetaMathlibExt.padicValNat_two_smallest_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#padic-val-nat-two-smallest-eq).

## $a$, $b$, $c$, $d$ divide gcds of reduced differences

Let $a, b, c, d$ be natural numbers
and put $s_1 = ab + 1$, $s_2 = ac + 1$, $s_3 = ad + 1$, $s_4 = bc + 1$, $s_5 = bd + 1$,
$s_6 = cd + 1$. For indices $i, j$ let $t_{ij}$ be the integer $(s_j - s_i) / \gcd(s_j, s_i)$.
Then $a \mid \gcd(t_{12}, t_{13}, t_{23})$, $b \mid \gcd(t_{14}, t_{15}, t_{45})$,
$c \mid \gcd(t_{24}, t_{26}, t_{46})$ and $d \mid \gcd(t_{35}, t_{36}, t_{56})$ in $\mathbb{Z}$.

The source assumes that $\{a, b, c, d\}$ is $S$-Diophantine; that hypothesis is not needed.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 3, quoting Szalay and Ziegler (2013), Lemma 3.

Stated but not proved: `MetaMathlibExt.dvd_gcd_sub_div_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#dvd-gcd-sub-div-gcd).

## The Szalay–Ziegler system (4) has no solutions

Let $p \ne q$ be odd primes and let
$a, b, c, d$ be integers with $0 < a < b < c < d$. Then there are no natural numbers
$\beta_1, \alpha_4, \beta_4, \alpha_2, \alpha_5, \alpha_3, \beta_3, \beta_6$ with
$ab + 1 = q^{\beta_1}$, $bc + 1 = p^{\alpha_4} q^{\beta_4}$, $ac + 1 = p^{\alpha_2}$,
$bd + 1 = p^{\alpha_5}$, $ad + 1 = p^{\alpha_3} q^{\beta_3}$ and $cd + 1 = q^{\beta_6}$.

Any solution would make $\{a, b, c, d\}$ a $\{p, q\}$-Diophantine quadruple.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 4, System (4), quoting Szalay and Ziegler, INTEGERS 13 (2013), Section 4.

Stated but not proved: `MetaMathlibExt.not_exists_sDiophantine_system_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#not-exists-s-diophantine-system-four).

## Exponent cases for $\{p, q\}$-Diophantine quadruples with $p \equiv 3 \pmod 4$

Let
$p \ne q$ be primes with $p \equiv 3 \pmod 4$, and let $a < b < c < d$ be natural numbers such
that $\{a, b, c, d\}$ is a $\{p, q\}$-Diophantine tuple. Write $s_1, \dots, s_6$ for
$ab + 1, ac + 1, ad + 1, bc + 1, bd + 1, cd + 1$, and let $\alpha_i$ and $\beta_i$ be the
exponents of $p$ and $q$ in the prime factorization of $s_i$. Then one of the following holds:
(I) $0 = \alpha_1 = \alpha_6 < \alpha_4 = \alpha_5 < \alpha_2 < \alpha_3$ and
$\beta_1 = \beta_2 = \beta_3 < \beta_4 < \beta_5 < \beta_6$;
(II) $0 = \alpha_1 = \alpha_6 < \alpha_2 = \alpha_5$, $\alpha_5 < \alpha_3$, $\alpha_5 < \alpha_4$
and $\beta_3 = \beta_4 < \beta_1 = \beta_2 < \beta_5 < \beta_6$;
(III) $0 = \alpha_2 = \alpha_5 < \alpha_1 = \alpha_3 \le \alpha_4 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_3 = \beta_4 < \beta_2 < \beta_5$;
(IV) $0 = \alpha_3 = \alpha_4 < \alpha_1 = \alpha_2 < \alpha_5 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_2 = \beta_5$, $\beta_5 < \beta_3$, $\beta_5 < \beta_4$.

These are the four cases of Table 1 of the source.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 5 and Table 1, quoting Ziegler, Glas. Mat. 54 (2019), Proposition 5.1.

Stated but not proved: `MetaMathlibExt.sDiophantine_quadruple_exponent_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#s-diophantine-quadruple-exponent-cases).

## No $\{p, q\}$-Diophantine quadruple when $p$ or $q$ is $3$ modulo $4$

Let $p \ne q$ be
primes with $p \equiv 3 \pmod 4$ or $q \equiv 3 \pmod 4$. Then no four-element set of natural
numbers is a $\{p, q\}$-Diophantine tuple; that is, there is no $\{p, q\}$-Diophantine quadruple.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_exists_sDiophantine_quadruple_of_mod_four_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#not-exists-s-diophantine-quadruple-of-mo).

## There is no $\{p, q\}$-Diophantine quintuple

Let $p < q$ be primes. Then no five-element
set of natural numbers is a $\{p, q\}$-Diophantine tuple; that is, there is no
$\{p, q\}$-Diophantine quintuple.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Theorem 2.

Stated but not proved: `MetaMathlibExt.not_exists_sDiophantine_quintuple` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#not-exists-s-diophantine-quintuple).

## Bounds in Case III for $\{p, q\}$-Diophantine quadruples

Let $p$ and $q$ be primes with
$p \equiv 3 \pmod 4$, $p \ge 7$ and $q \equiv 1 \pmod 4$, and let $a < b < c < d$ be natural
numbers such that $\{a, b, c, d\}$ is a $\{p, q\}$-Diophantine tuple. Put $s_1 = ab + 1$,
$s_2 = ac + 1$, $s_3 = ad + 1$, $s_4 = bc + 1$, $s_5 = bd + 1$, $s_6 = cd + 1$, and let
$\alpha_i$ and $\beta_i$ be the $p$-adic and $q$-adic valuations of $s_i$. Suppose that
$0 = \alpha_2 = \alpha_5 < \alpha_1 = \alpha_3 \le \alpha_4 < \alpha_6$ and
$0 < \beta_1 = \beta_6 < \beta_3 = \beta_4 < \beta_2 < \beta_5$ (Case III of Table 1, with
$\beta_1 > 0$). Then, with $\beta = \beta_1$ and $\beta' = \beta_3$, we have
$d < 1.03\, q^{2(\beta' - \beta)}$ and $b < 1.03\, q^{\beta' - \beta}$.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 6.

Stated but not proved: `MetaMathlibExt.sDiophantine_quadruple_caseIII_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#s-diophantine-quadruple-case-iii-bounds).

## Bound on $b$ in Case IV for $\{p, q\}$-Diophantine quadruples

Let $p$ and $q$ be
primes with $p \equiv 3 \pmod 4$, $p \ge 7$ and $q \equiv 1 \pmod 4$, and let $a < b < c < d$
be natural numbers such that $\{a, b, c, d\}$ is a $\{p, q\}$-Diophantine tuple. Write
$s_1, \dots, s_6$ for $ab + 1, ac + 1, ad + 1, bc + 1, bd + 1, cd + 1$, and let $\alpha_i$ and
$\beta_i$ be the exponents of $p$ and $q$ in the prime factorization of $s_i$. Suppose that
$0 = \alpha_3 = \alpha_4 < \alpha_1 = \alpha_2 < \alpha_5 < \alpha_6$ and
$0 < \beta_1 = \beta_6 < \beta_2 = \beta_5$, $\beta_5 < \beta_3$, $\beta_5 < \beta_4$. Then
$b < 1.042 \, q^{\beta_2 - \beta_1}$.

The assumptions on the exponents are Case IV of Table 1 of the source together with
$\beta_1 > 0$.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Lemma 7.

Stated but not proved: `MetaMathlibExt.sDiophantine_quadruple_caseIV_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#s-diophantine-quadruple-case-iv-bound).

## The fourteen exponent cases for $\{p, q\}$-Diophantine quadruples

Let $p \ne q$ be
primes and let $a < b < c < d$ be natural numbers such that $\{a, b, c, d\}$ is a
$\{p, q\}$-Diophantine tuple. Write $s_1, \dots, s_6$ for
$ab + 1, ac + 1, ad + 1, bc + 1, bd + 1, cd + 1$, and let $\alpha_i$ and $\beta_i$ be the
exponents of $p$ and $q$ in the prime factorization of $s_i$. Then one of the following
fourteen cases holds:
(I) $\alpha_1 = \alpha_2 = \alpha_3 < \alpha_4 < \alpha_5$, $\alpha_3 < \alpha_6 < \alpha_5$,
$\beta_1 = \beta_4 = \beta_5 < \beta_2 < \beta_3$ and $\beta_5 < \beta_6 < \beta_3$;
(II) $\alpha_1 = \alpha_2 = \alpha_3 < \alpha_4 < \alpha_5 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_4 = \beta_5 < \beta_2 < \beta_3$;
(III) $\alpha_1 = \alpha_6 < \alpha_2 = \alpha_3 < \alpha_4 < \alpha_5$ and
$\beta_1 = \beta_4 = \beta_5 < \beta_2 < \beta_3 < \beta_6$;
(IV) $\alpha_2 = \alpha_5 < \alpha_1 = \alpha_3 < \alpha_4 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_3 = \beta_4 < \beta_2 < \beta_5$;
(V) $\alpha_2 = \alpha_5 < \alpha_1 = \alpha_4 < \alpha_3 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_3 = \beta_4 < \beta_2 < \beta_5$;
(VI) $\alpha_1 = \alpha_6 < \alpha_2 = \alpha_5$, $\alpha_5 < \alpha_3$, $\alpha_5 < \alpha_4$ and
$\beta_3 = \beta_4 < \beta_1 = \beta_2 < \beta_5 < \beta_6$;
(VII) $\alpha_2 = \alpha_5 < \alpha_3 = \alpha_4 < \alpha_1 < \alpha_6$ and
$\beta_1 = \beta_6 < \beta_3 = \beta_4 < \beta_2 < \beta_5$;
(VIII)-(XIV) the conditions of (I)-(VII) with $\alpha_i$ and $\beta_i$ exchanged for every $i$.

These are the cases of Table 2 of the source.

## Sources

- Volker Ziegler, *On the Existence of `{p, q}`-Diophantine Quadruples and Quintuples*, INTEGERS 25 (2025), Article A92, Proposition 1 and Table 2.

Stated but not proved: `MetaMathlibExt.sDiophantine_quadruple_fourteen_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PQDiophantineTuplesWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html#s-diophantine-quadruple-fourteen-cases).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: S-Diophantine tuples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/s-diophantine-tuples)
