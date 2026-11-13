---
declaration: section
origin: cited
lean: MetaMathlibExt.binomial_double_sum_eq_pow_sub_fib, MetaMathlibExt.alternating_binomial_partial_sum, MetaMathlibExt.catalanLarcombeFrenchNumber, MathlibExt.Combinatorics.HockeyStickWanted.sum_choose_two_mul_add, MetaMathlibExt.strehl_franel_binomial_identity, MetaMathlibExt.chu_vandermonde_terminating_specialization
statement: formalized
---

# Binomial sums and hypergeometric identities: its own results

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html).

Evaluations and bounds of sums of products of binomial coefficients: Chu–Vandermonde, Dixon, Knuth's old sum, Staver, Frisch, Klamkin, hockey-stick and Filipponi identities, partial-sum bounds, multisection identities, and Franel, Domb, Zagier and Catalan–Larcombe–French numbers defined by binomial sums.

## A binomial double sum equal to a power of two minus a Fibonacci number

For every natural
number $n$,

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \sum_{q=0}^{n-2k} \binom{n-k}{q} = 2^{n+1} - F_{n+2},$$

where $F_m$ is the $m$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$.

## Sources

- Denis Neiter and Amsha Proag, "Links Between Sums Over Paths in Bernoulli's Triangles and the Fibonacci Numbers," Journal of Integer Sequences 19 (2016), Article 16.8.3, Theorem, lines 247–252, https://cs.uwaterloo.ca/journals/JIS/VOL19/Proag/proag3.tex

Formalized by `MetaMathlibExt.binomial_double_sum_eq_pow_sub_fib`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BinomialDoubleSum.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BinomialDoubleSum.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#binomial-double-sum-eq-pow-sub-fib).

## Alternating binomial sums of partial sums

For every sequence $a_0, a_1, a_2, \dots$ of
complex numbers and every natural number $n$,

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \sum_{j=1}^{k} a_j =
\sum_{k=0}^{n-1} (-1)^{k+1} \binom{n-1}{k} a_{k+1},$$

where an empty sum is $0$, so both sides vanish when $n = 0$.

## Sources

- Necdet Batır and Anthony Sofo, "A Unified Treatment of Certain Classes of Combinatorial Identities," Journal of Integer Sequences 24 (2021), Article 21.3.2, Theorem A.

Formalized by `MetaMathlibExt.alternating_binomial_partial_sum`, a theorem declared in [MathlibExt/Combinatorics/AlternatingBinomialPartialSum.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/AlternatingBinomialPartialSum.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#alternating-binomial-partial-sum).

## Catalan–Larcombe–French numbers

For a natural number $n$, the $n$th
Catalan–Larcombe–French number (OEIS A053175) is

$$
P_n = 2^n \sum_{k=0}^{n} \binom{n}{2k} \binom{2k}{k}^2 4^{n-2k},
$$

where the terms with $2k > n$ vanish because $\binom{n}{2k} = 0$.

Formalized by `MetaMathlibExt.catalanLarcombeFrenchNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/CatalanLarcombeFrenchNumber.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CatalanLarcombeFrenchNumber.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#catalan-larcombe-french-number).

## Generalized hockey stick identity of Lynch and Weselcouch

For all natural numbers
$n$ and $k$,

$$\sum_{i=0}^{k} \binom{2i + n}{i} =
\sum_{i=0}^{\lfloor k/2 \rfloor} (-1)^i \binom{2k + 1 + n - i}{k - 2i}.$$

## Sources

- Molly Lynch and Michael Weselcouch, "A Generalized Hockey Stick Theorem", Corollary 15.

Stated but not proved: `MathlibExt.Combinatorics.HockeyStickWanted.sum_choose_two_mul_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/HockeyStickWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HockeyStickWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#sum-choose-two-mul-add).

## Strehl's identity for the Franel numbers

For every natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k}^2 \binom{2k}{n} = \sum_{k=0}^{n} \binom{n}{k}^3,$$

where the right-hand side is the $n$-th Franel number.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, equation `1est`, lines 110–114, <https://cs.uwaterloo.ca/journals/JIS/VOL29/Fried/fried21.tex>, recalling V. Strehl, *Binomial identities — combinatorial and algorithmic aspects*, Discrete Math. 136 (1994), formula (29).

Formalized by `MetaMathlibExt.strehl_franel_binomial_identity`, a theorem declared in [MathlibExt/Combinatorics/StrehlFranel.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/StrehlFranel.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#strehl-franel-binomial-identity).

## Terminating Chu–Vandermonde specialization

For every natural number $n \ge 1$, the
following sum of rational numbers vanishes:

$$\sum_{k=0}^{n} \binom{n}{k} \binom{n+k}{k} \frac{(-1)^k}{k+1} = 0.$$

The source identifies the sum as the terminating Gauss hypergeometric value
${}_2F_1(n+1, -n; 2; 1) = (1-n)_n / (2)_n = 0$, where $(a)_n$ is the rising factorial.

## Sources

- Carsten Elsner, "On Prime-Detecting Sequences From Apéry's Recurrence Formulae for ζ(3) and ζ(2)", Journal of Integer Sequences 11 (2008), Article 08.5.1, lines 606–608, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Elsner/elsner7.tex>.

Formalized by `MetaMathlibExt.chu_vandermonde_terminating_specialization`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ChuVandermondeTerminatingSpecialization.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ChuVandermondeTerminatingSpecialization.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html#chu-vandermonde-terminating-specializati).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial sums and hypergeometric identities](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums)
