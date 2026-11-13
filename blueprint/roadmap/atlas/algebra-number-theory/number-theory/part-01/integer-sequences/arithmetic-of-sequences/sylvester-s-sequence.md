---
declaration: section
origin: cited
lean: Nat.generalizedSylvester, Nat.generalizedSylvester_zero, Nat.generalizedSylvester_succ, Nat.generalizedSylvester_pos, MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvesterNumber, MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_sub_dvd, MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_modEq_three_mod_four, MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_modEq_seven_mod_thirty_six
statement: formalized
---

# Sylvester's sequence

20 results, 5 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html).

## Generalized Sylvester sequence

For a natural number $n$, the generalized Sylvester sequence
$(s_k(n))_{k \ge 0}$ is the sequence of natural numbers defined by $s_0(n) = n + 1$ and
$s_{k+1}(n) = s_k(n)^2 - s_k(n) + 1$ for $k \ge 0$.

The source indexes the sequence from one: its $s_1(n)$ is $s_0(n)$ here.

Formalized by `Nat.generalizedSylvester`, a definition declared in [MathlibExt/NumberTheory/GeneralizedSylvester.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedSylvester.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#generalized-sylvester).

## Initial term of the generalized Sylvester sequence

For every natural number $n$, the
generalized Sylvester sequence $(s_k(n))_{k \ge 0}$ satisfies $s_0(n) = n + 1$.

Formalized by `Nat.generalizedSylvester_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedSylvester.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedSylvester.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#generalized-sylvester-zero).

## Recurrence for the generalized Sylvester sequence

For all natural numbers $n$ and $k$, the
generalized Sylvester sequence $(s_k(n))_{k \ge 0}$ satisfies
$s_{k+1}(n) = s_k(n)^2 - s_k(n) + 1$.

Formalized by `Nat.generalizedSylvester_succ`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedSylvester.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedSylvester.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#generalized-sylvester-succ).

## Positivity of the generalized Sylvester sequence

For all natural numbers $n$ and $k$, the
term $s_k(n)$ of the generalized Sylvester sequence is positive.

Formalized by `Nat.generalizedSylvester_pos`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedSylvester.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedSylvester.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#generalized-sylvester-pos).

## Sylvester numbers

The Sylvester numbers $S_0, S_1, S_2, \dots$ are the natural numbers
given by $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$ for $n \ge 0$, so the sequence begins
$2, 3, 7, 43, 1807, \dots$. It is the generalized Sylvester sequence with parameter $1$.

Formalized by `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvesterNumber`, an abbreviation declared in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-number).

## Divisibility of differences of Sylvester numbers

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For all natural numbers $k$, $m$ and $n$
with $k \ge 1$, $m \ge k$ and $n \ge k$, the integer $(S_k - 1)^2$ divides $S_n - S_m$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 1, divisibility (4).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_sub_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-sub-dvd).

## Sylvester numbers modulo 4

Let $(S_n)_{n \ge 0}$ be the Sylvester sequence,
$S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n \ge 1$, $S_n \equiv 3 \pmod 4$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 1, congruence (5).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_modEq_three_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-mod-eq-three-mod-four).

## Sylvester numbers modulo 36

Let $(S_n)_{n \ge 0}$ be the Sylvester sequence,
$S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n \ge 2$, $S_n \equiv 7 \pmod{36}$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 1, congruence (6).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_modEq_seven_mod_thirty_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-mod-eq-seven-mod-thirty-six).

## Sylvester numbers modulo 1764

Let $(S_n)_{n \ge 0}$ be the Sylvester sequence,
$S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n \ge 3$, $S_n \equiv 43 \pmod{1764}$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 1, congruence (7).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_modEq_forty_three_mod_1764` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-mod-eq-forty-three-mod-1764).

## Alternating divisibility for Sylvester numbers

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For all natural numbers $k$ and $n$ with
$1 \le k \le n$, the integer $S_k^2 + 1$ divides the integer $S_n - (-1)^{n-k} S_k$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 2, divisibility (8).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_sq_add_one_dvd_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-sq-add-one-dvd-sub).

## Sylvester numbers of even index modulo 10

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $i \ge 1$,
$S_{2i} \equiv 7 \pmod{10}$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 2, congruence (9), even indices.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_even_index_mod_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-even-index-mod-ten).

## Sylvester numbers of odd index modulo 10

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $i \ge 1$,
$S_{2i+1} \equiv 3 \pmod{10}$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 2, congruence (9), odd indices.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_odd_index_mod_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-odd-index-mod-ten).

## Mersenne numbers in the Sylvester sequence

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. The natural numbers $x$ such that $x = S_n$
for some $n$ and $x = 2^r - 1$ for some $r \ge 1$ are exactly $3$ and $7$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Corollary 1(a).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.mersenne_sylvester_values_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#mersenne-sylvester-values-eq).

## The only triangular Sylvester number is $3$

Let $S_n$ denote the $n$-th Sylvester
number. A natural number $x$ equals $S_n$ for some $n$ and satisfies $2x = m(m + 1)$ for some
natural number $m \ge 1$ if and only if $x = 3$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Corollary 1(b).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.triangular_sylvester_values_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#triangular-sylvester-values-eq).

## No Sylvester number is perfect

For every natural number $n$, the $n$-th Sylvester number
$S_n$ is not a perfect number.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Corollary 1(c).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_not_perfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-not-perfect).

## Prime divisors congruent to 3 modulo 4 of Sylvester numbers

Let $(S_n)_{n \ge 0}$ be the
Sylvester sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n \ge 1$, $S_n$ has a
prime divisor $p$ with $p \equiv 3 \pmod 4$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Corollary 1(d).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_exists_prime_divisor_mod_four_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-exists-prime-divisor-mod-four).

## Sylvester numbers are not perfect powers

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n$ there are no natural numbers
$a \ge 2$ and $m \ge 2$ with $S_n = a^m$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 3(a).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_not_perfect_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-not-perfect-power).

## Sylvester numbers next to perfect powers

Let $(S_n)_{n \ge 0}$ be the Sylvester
sequence, $S_0 = 2$ and $S_{n+1} = S_n^2 - S_n + 1$. For every $n$ other than $1$ and $2$ there
are no natural numbers $a \ge 2$ and $m \ge 2$ with $S_n = a^m + 1$ or $S_n = a^m - 1$.

## Sources

- Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Proposition 3(b).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.sylvester_ne_pow_add_or_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#sylvester-ne-pow-add-or-sub-one).

## Coprime solutions of $x^2 + 3 = 4y^n$

For natural numbers $n$, $x$ and $y$, the
conditions $n \ge 3$, $x \ge 1$, $y \ge 1$, $\gcd(x, y) = 1$ and $x^2 + 3 = 4y^n$ hold if and only
if $n \ge 3$ and either $x = y = 1$ or $(n, x, y) = (3, 37, 7)$ (Luca–Tengely–Togbé).

## Sources

- F. Luca, Sz. Tengely, and A. Togbé, "On the Diophantine equation x² + C = 4yⁿ", Theorem 1.1, as quoted in Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Theorem 1, equation with C = 3.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.lebesgue_nagell_three_solutions_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#lebesgue-nagell-three-solutions-iff).

## Coprime solutions of $x^2 + 7 = 4y^n$

For natural numbers $n$, $x$ and $y$, the
conditions $n \ge 3$, $x \ge 1$, $y \ge 1$, $\gcd(x, y) = 1$ and $x^2 + 7 = 4y^n$ hold if and only
if $(n, x, y)$ is $(3, 5, 2)$, $(5, 11, 2)$ or $(13, 181, 2)$ (Luca–Tengely–Togbé).

## Sources

- F. Luca, Sz. Tengely, and A. Togbé, "On the Diophantine equation x² + C = 4yⁿ", Theorem 1.1, as quoted in Abderrahim Makki Naciri, "A Note on Sylvester's Sequence", Theorem 1, equation with C = 7.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.SylvesterSequenceWanted.lebesgue_nagell_seven_solutions_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SylvesterSequenceWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html#lebesgue-nagell-seven-solutions-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sylvester's sequence](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sylvester-s-sequence)
