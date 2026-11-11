---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ConjectureOfMartonWanted.ConjectureOfMarton.F, MathlibExt.Combinatorics.ConjectureOfMartonWanted.ConjectureOfMarton.theorem_1_2, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.conjecture, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.conjecture_holds, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.BinaryAmbientSpace, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.IsAsymptoticCosetCoverExponent, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.asymptoticCosetCoverExponents, MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.martonPFRCoverExponent
statement: formalized
---

# Polynomial Freiman–Ruzsa theorem

19 results, 12 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html).

## The vector space $\mathbb{F}_2^n$

For a natural number $n$, $\mathbb{F}_2^n$ is the
space of functions from $\{0, \dots, n - 1\}$ to the field $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$
with two elements, the $n$-dimensional vector space over $\mathbb{F}_2$.

Formalized by `MathlibExt.Combinatorics.ConjectureOfMartonWanted.ConjectureOfMarton.F`, an abbreviation declared in [WantedExt/Combinatorics/ConjectureOfMartonWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConjectureOfMartonWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#f).

## Polynomial Freiman–Ruzsa theorem over $\mathbb{F}_2$

Let $n$ be a natural number, let
$A$ be a nonempty subset of $\mathbb{F}_2^n$, and let $K$ be a real number such that the sumset
$A + A = \{a + b : a, b \in A\}$ satisfies $|A + A| \le K |A|$. Then there is a subgroup $H$ of
$\mathbb{F}_2^n$ with $|H| \le |A|$ such that $A$ is covered by at most $2K^{12}$ cosets of $H$:
there is a finite set $T \subseteq \mathbb{F}_2^n$ with $|T| \le 2K^{12}$ and $A \subseteq T + H$.

The set $A$ must be nonempty, which the paper leaves implicit.

## Sources

- W. T. Gowers, B. Green, F. Manners, and T. Tao, `On a conjecture of Marton`, Annals of Math, 201 (2) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_conjecture_of_marton` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.ConjectureOfMartonWanted.ConjectureOfMarton.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Combinatorics/ConjectureOfMartonWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ConjectureOfMartonWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#theorem-1-2).

## Polynomial Freiman–Ruzsa conjecture over $\mathbb{F}_2$

There are real polynomials $P$
and $Q$, with $P(K) > 0$ and $Q(K) > 0$ for every real $K \ge 1$, such that for every
$n \in \mathbb{N}$, every nonempty finite set $A \subseteq \mathbb{F}_2^n$ and every real $K \ge 1$
with $|A + A| \le K|A|$, there is a subset $A' \subseteq A$ with $|A| / P(K) \le |A'|$ and
$|\operatorname{span}(A')| \le Q(K)\,|A'|$, where $\operatorname{span}(A')$ is the
$\mathbb{F}_2$-linear span of $A'$.

The problem is recorded as OWR-12177-008. It was proved by Gowers, Green, Manners and Tao
(arXiv:2311.05762).

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#conjecture).

## Gowers–Green–Manners–Tao theorem (polynomial Freiman–Ruzsa over $\mathbb{F}_2$)

The
polynomial Freiman–Ruzsa conjecture over $\mathbb{F}_2$ holds: there are real polynomials $P$ and
$Q$, with $P(K) > 0$ and $Q(K) > 0$ for every real $K \ge 1$, such that for every
$n \in \mathbb{N}$, every nonempty finite set $A \subseteq \mathbb{F}_2^n$ and every real $K \ge 1$
with $|A + A| \le K|A|$, there is a subset $A' \subseteq A$ with $|A| / P(K) \le |A'|$ and
$|\operatorname{span}(A')| \le Q(K)\,|A'|$, where $\operatorname{span}(A')$ is the
$\mathbb{F}_2$-linear span of $A'$.

Gowers, Green, Manners and Tao prove that such a set $A$ is covered by polynomially many (in $K$)
cosets of a subspace of size at most $|A|$; the densest of these cosets gives the subset $A'$.

## Sources

- W. T. Gowers, B. Green, F. Manners, T. Tao, On a conjecture of Marton, arXiv:2311.05762 (November 2023), https://arxiv.org/abs/2311.05762.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#conjecture-holds).

## The binary vector space $\mathbb{F}_2^n$

For a natural number $n$, the ambient space
$\mathbb{F}_2^n$ of all functions from $\{0, 1, \dots, n - 1\}$ to the two-element field
$\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$.

## Sources

- Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.BinaryAmbientSpace`, an abbreviation declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#binary-ambient-space).

## Admissible asymptotic coset-cover exponents

A real number $C$ is an admissible asymptotic
coset-cover exponent if for every real $\varepsilon > 0$ there is a real $K_0 \ge 1$ such that
for every real $K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set
$A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is an $\mathbb{F}_2$-linear subspace
$H$ of $\mathbb{F}_2^n$ with $|H| \le |A|$ such that $A$ is covered by at most $K^{C + \varepsilon}$
translates of $H$: there is a finite set $F \subseteq \mathbb{F}_2^n$ with
$|F| \le K^{C + \varepsilon}$ and $A \subseteq F + H$.

This makes the source's bound of $K^{C + o(1)}$ translates uniform: once $K$ is large enough,
the same bound works in every dimension and for every nonempty set of doubling at most $K$.

## Sources

- Optimization Problems constant 18a, with the uniform asymptotic quantifiers made explicit.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.IsAsymptoticCosetCoverExponent`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#is-asymptotic-coset-cover-exponent).

## The set of admissible coset-cover exponents

This is the set of all real numbers $C$
that are admissible asymptotic coset-cover exponents: for every real $\varepsilon > 0$ there is a
real $K_0 \ge 1$ such that for every real $K \ge K_0$, every $n \in \mathbb{N}$ and every
nonempty finite set $A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there are an
$\mathbb{F}_2$-linear subspace $H$ of $\mathbb{F}_2^n$ with $|H| \le |A|$ and a finite set
$F \subseteq \mathbb{F}_2^n$ with $|F| \le K^{C + \varepsilon}$ and $A \subseteq F + H$.

## Sources

- Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.asymptoticCosetCoverExponents`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#asymptotic-coset-cover-exponents).

## The Marton coset-cover exponent

Call a real number $C$ an admissible asymptotic
coset-cover exponent if for every $\varepsilon > 0$ there is $K_0 \ge 1$ such that for every real
$K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set $A \subseteq \mathbb{F}_2^n$
with $|A + A| \le K|A|$, there is a subspace $H$ of $\mathbb{F}_2^n$ with $|H| \le |A|$ such that
$A$ is covered by at most $K^{C + \varepsilon}$ translates of $H$. The Marton coset-cover exponent
is the infimum in $\mathbb{R}$ of the set of admissible exponents, with the convention that this
infimum is $0$ when the set is empty or unbounded below.

## Sources

- Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.martonPFRCoverExponent`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#marton-pfrcover-exponent).

## Statement that the Marton coset-cover exponent is attained

The proposition that the
Marton coset-cover exponent $C^*$, the infimum of the admissible asymptotic coset-cover exponents,
is the least admissible exponent: $C^*$ is itself an admissible asymptotic coset-cover exponent,
and $C^* \le C$ for every admissible asymptotic coset-cover exponent $C$.

## Sources

- Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.leastCoverExponentClaim`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#least-cover-exponent-claim).

## Statement that an admissible coset-cover exponent exists

The proposition that some
real number $C$ is an admissible asymptotic coset-cover exponent: for every $\varepsilon > 0$
there is $K_0 \ge 1$ such that for every real $K \ge K_0$, every $n \in \mathbb{N}$ and every
nonempty finite set $A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is a subspace $H$
of $\mathbb{F}_2^n$ with $|H| \le |A|$ such that $A$ is covered by at most $K^{C + \varepsilon}$
translates of $H$.

This is an asymptotic form of Marton's conjecture over $\mathbb{F}_2^n$, which was proved by
Gowers, Green, Manners and Tao.

## Sources

- Optimization Problems constant 18a and GGMT, arXiv:2311.05762.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.martonPFRFinitenessTheorem`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#marton-pfrfiniteness-theorem).

## Statement of the Gowers–Green–Manners–Tao exponent $7 + \sqrt{17}$

The proposition that
$7 + \sqrt{17}$ is an admissible asymptotic coset-cover exponent.

## Sources

- GGMT, arXiv:2311.05762, and Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.ggmt2025UpperBound7Sqrt17`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#ggmt2025-upper-bound7-sqrt17).

## Statement of Liao's exponent-9 coset-cover bound

The proposition that $9$ is an admissible
asymptotic coset-cover exponent: for every $\varepsilon > 0$ there is $K_0 \ge 1$ such that for
every real $K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set
$A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is a subspace $H$ of $\mathbb{F}_2^n$
with $|H| \le |A|$ such that $A$ is covered by at most $K^{9 + \varepsilon}$ translates
of $H$.

## Sources

- J.-J. Liao, arXiv:2404.09639, Theorem 1.1.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.liao2024UpperBound9`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#liao2024-upper-bound9).

## Statement of Liao's simplified exponent-11 coset-cover bound

The proposition that $11$
is an admissible asymptotic coset-cover exponent: for every $\varepsilon > 0$ there is $K_0 \ge 1$
such that for every real $K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set
$A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is a subspace $H$ of $\mathbb{F}_2^n$
with $|H| \le |A|$ such that $A$ is covered by at most $K^{11 + \varepsilon}$ translates of $H$.

## Sources

- J.-J. Liao, arXiv:2404.09639, Theorem 1.2 and the implication `C ≤ C' + 1`.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.liao2024SimplifiedUpperBound11`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#liao2024-simplified-upper-bound11).

## Statement of the basis-vector lower bound

The proposition that every admissible
asymptotic coset-cover exponent $C$ satisfies $C \ge 1$.

The obstruction comes from sets of basis vectors.

## Sources

- Optimization Problems constant 18a.

Formalized by `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.basisVectorsLowerBound1`, a definition declared in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#basis-vectors-lower-bound1).

## The least coset-cover exponent is attained

The set of admissible asymptotic coset-cover
exponents has a least element, namely its infimum $C^*$ (the Marton cover exponent): $C^*$ is
itself admissible, and $C^* \le C$ for every admissible asymptotic coset-cover exponent $C$.

## Sources

- Optimization Problems constant 18a.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.leastCoverExponentClaim_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#least-cover-exponent-claim-holds).

## Gowers–Green–Manners–Tao exponent $7 + \sqrt{17}$

The number $7 + \sqrt{17}$ is an
admissible asymptotic coset-cover exponent.

## Sources

- GGMT, arXiv:2311.05762, and Optimization Problems constant 18a.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.ggmt2025UpperBound7Sqrt17_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#ggmt2025-upper-bound7-sqrt17-holds).

## Liao's coset-cover bound with exponent 9

The number $9$ is an admissible
asymptotic coset-cover exponent: for every $\varepsilon > 0$ there is $K_0 \ge 1$ such that for
every real $K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set
$A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is a subspace $H$ of $\mathbb{F}_2^n$
with $|H| \le |A|$ such that $A$ is covered by at most $K^{9 + \varepsilon}$ translates
of $H$.

## Sources

- J.-J. Liao, arXiv:2404.09639, Theorem 1.1.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.liao2024UpperBound9_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#liao2024-upper-bound9-holds).

## Liao's simplified coset-cover bound with exponent 11

The number $11$ is an admissible
asymptotic coset-cover exponent: for every $\varepsilon > 0$ there is $K_0 \ge 1$ such that for
every real $K \ge K_0$, every $n \in \mathbb{N}$ and every nonempty finite set
$A \subseteq \mathbb{F}_2^n$ with $|A + A| \le K|A|$, there is a subspace $H$ of $\mathbb{F}_2^n$
with $|H| \le |A|$ such that $A$ is covered by at most $K^{11 + \varepsilon}$ translates
of $H$.

## Sources

- J.-J. Liao, arXiv:2404.09639, Theorem 1.2 and the implication `C ≤ C' + 1`.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.liao2024SimplifiedUpperBound11_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#liao2024-simplified-upper-bound11-holds).

## Basis-vector lower bound for coset-cover exponents

Every admissible asymptotic
coset-cover exponent $C$ satisfies $C \ge 1$.

The obstruction comes from sets of basis vectors.

## Sources

- Optimization Problems constant 18a.

Stated but not proved: `MathlibExt.Combinatorics.PolynomialFreimanRuzsaBinaryWanted.basisVectorsLowerBound1_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PolynomialFreimanRuzsaBinaryWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html#basis-vectors-lower-bound1-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial Freiman–Ruzsa theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/polynomial-freiman-ruzsa-theorem)
