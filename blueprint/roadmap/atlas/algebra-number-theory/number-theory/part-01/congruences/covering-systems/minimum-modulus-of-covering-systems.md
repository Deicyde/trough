---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_modulus_ge_108_of_distinct_covering_min_five, MetaMathlibExt.exists_distinct_covering_min_six_max_168, MetaMathlibExt.lcm_moduli_ge_1440_of_distinct_covering_min_five, MetaMathlibExt.lcm_moduli_ge_5040_of_distinct_covering_min_six, MetaMathlibExt.exists_distinct_covering_min_seven_lcm_15120, MetaMathlibExt.isCoveringSystem_filter_not_dvd_of_lt, MetaMathlibExt.exists_isCoveringSystem_merge_prime_power, MetaMathlibExt.isCoveringSystem_translate
statement: formalized
---

# Minimum modulus of covering systems

13 results, 1 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html).

## Krukenberg's conjecture for minimum modulus five

Let $C$ be a distinct covering
system: a finite set of congruences $x \equiv r \pmod m$ with $r \in \mathbb{Z}$ and
$m \in \mathbb{N}$, no two with the same modulus, such that every integer satisfies at least one
of them. If every modulus of $C$ is at least $5$ and some modulus equals $5$, then some modulus
of $C$ is at least $108$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_modulus_ge_108_of_distinct_covering_min_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#exists-modulus-ge-108-of-distinct-coveri).

## A distinct covering system with moduli from 6 to 168

There is a distinct covering
system, that is, a finite set of congruences $x \equiv r \pmod m$ with $r \in \mathbb{Z}$,
$m \in \mathbb{N}$ and no two with the same modulus, such that every integer satisfies at least
one of them, whose moduli all lie between $6$ and $168$ and include both $6$ and $168$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Theorem 2; the paper's witness is due to Ognian Trifonov.

Stated but not proved: `MetaMathlibExt.exists_distinct_covering_min_six_max_168` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#exists-distinct-covering-min-six-max-168).

## Least common multiple of a covering system with minimum modulus five

Let $C$ be a
distinct covering system: a finite set of congruences $x \equiv r \pmod m$ with
$r \in \mathbb{Z}$ and $m \in \mathbb{N}$, no two with the same modulus, such that every integer
satisfies at least one of them. If every modulus of $C$ is at least $5$ and some modulus equals
$5$, then the least common multiple of the moduli of $C$ is at least $1440$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Theorem 3.

Stated but not proved: `MetaMathlibExt.lcm_moduli_ge_1440_of_distinct_covering_min_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#lcm-moduli-ge-1440-of-distinct-covering).

## Least common multiple of a covering system with minimum modulus six

Let $C$ be a
distinct covering system: a finite set of congruences $x \equiv r \pmod m$ with
$r \in \mathbb{Z}$ and $m \in \mathbb{N}$, no two with the same modulus, such that every integer
satisfies at least one of them. If every modulus of $C$ is at least $6$ and some modulus equals
$6$, then the least common multiple of the moduli of $C$ is at least $5040$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Theorem 4.

Stated but not proved: `MetaMathlibExt.lcm_moduli_ge_5040_of_distinct_covering_min_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#lcm-moduli-ge-5040-of-distinct-covering).

## A distinct covering system with minimum modulus 7 and moduli of lcm 15120

There is a
distinct covering system, that is, a finite set of congruences $x \equiv r \pmod m$ with
$r \in \mathbb{Z}$, $m \in \mathbb{N}$ and no two with the same modulus, such that every
integer satisfies at least one of them, whose moduli are all at least $7$, include $7$, and have
least common multiple $15120$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Theorem 5.

Stated but not proved: `MetaMathlibExt.exists_distinct_covering_min_seven_lcm_15120` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#exists-distinct-covering-min-seven-lcm-1).

## Discarding the classes whose modulus is divisible by a large prime power

Let $C$ be a
distinct covering system: a finite set of congruences $x \equiv r \pmod m$ with
$r \in \mathbb{Z}$ and $m \in \mathbb{N}$ (where $x \equiv r \pmod 0$ means $x = r$), no two
with the same modulus, such that every integer satisfies at least one of them. Let
$B \in \mathbb{N}$ be at least every modulus of $C$, let $p$ be a prime and $a \ge 1$. If
$B < p^a (p + 1)$, then the congruences of $C$ whose modulus is not divisible by $p^a$ still
cover every integer.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 1, quoting Krukenberg, Corollary 2.3, and Dalton–Trifonov, Corollary 8.

Stated but not proved: `MetaMathlibExt.isCoveringSystem_filter_not_dvd_of_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#is-covering-system-filter-not-dvd-of-lt).

## Merging the p classes whose modulus is divisible by a prime power

Let $C$ be a
covering system with positive moduli: a finite set of congruences $x \equiv r \pmod m$ with
$r \in \mathbb{Z}$ and $m \ge 1$ such that every integer satisfies at least one of them. Let $p$
be a prime and $a \ge 1$, and suppose exactly $p$ congruences of $C$ have modulus divisible by
$p^a$, with moduli $p^a m_1, \dots, p^a m_p$. Then for some $r \in \mathbb{Z}$, replacing these
$p$ congruences by the single congruence $x \equiv r \pmod{p^{a-1} \operatorname{lcm}(m_1,
\dots, m_p)}$ still gives a covering system.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 2, quoting Dalton–Trifonov, Corollary 9.

Stated but not proved: `MetaMathlibExt.exists_isCoveringSystem_merge_prime_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#exists-is-covering-system-merge-prime-po).

## Translating a covering system

Let $C$ be a covering system: a finite set of
congruences $x \equiv a_i \pmod{m_i}$ with $a_i \in \mathbb{Z}$ and $m_i \in \mathbb{N}$ (where
$x \equiv a_i \pmod 0$ means $x = a_i$) such that every integer satisfies at least one of them.
Then for every $t \in \mathbb{Z}$ the congruences $x \equiv a_i + t \pmod{m_i}$ also form a
covering system.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 3.

Stated but not proved: `MetaMathlibExt.isCoveringSystem_translate` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#is-covering-system-translate).

## Swapping two residues modulo a prime in a covering system

Let $C$ be a covering system
with positive moduli: a finite set of congruences $x \equiv a \pmod m$ with $a \in \mathbb{Z}$
and $m \ge 1$ such that every integer satisfies at least one of them. Let $L$ be the least
common multiple of its moduli, $p$ a prime dividing $L$, and $a_1 < a_2 \le p - 1$ natural
numbers. For a prime $\ell$ write $\nu_\ell(L)$ for the exponent of $\ell$ in $L$, and let
$C_p(\alpha)$ be the set of congruences $x \equiv a \pmod m$ in $C$ with $p \mid m$ and
$a \equiv \alpha \pmod p$. Let $t \in \mathbb{Z}$ satisfy $t \equiv a_2 - a_1 \pmod{p^{\nu_p(L)}}$
and $t \equiv 0 \pmod{q^{\nu_q(L)}}$ for every prime $q \ne p$ dividing $L$. Then the
congruences of $C$ outside $C_p(a_1) \cup C_p(a_2)$, together with $x \equiv a + t \pmod m$ for
each $x \equiv a \pmod m$ in $C_p(a_1)$ and $x \equiv a - t \pmod m$ for each
$x \equiv a \pmod m$ in $C_p(a_2)$, form a covering system.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 4, from the author's thesis, Lemma 2.13.

Stated but not proved: `MetaMathlibExt.isCoveringSystem_swap_residues_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#is-covering-system-swap-residues-mod-pri).

## Mirsky–Newman bound for distinct covering systems

Let $a_1 \bmod m_1, \dots,
a_k \bmod m_k$ be residue classes that cover $\mathbb{Z}$, that is, every integer lies in at
least one of them. If the moduli $m_1, \dots, m_k$ are pairwise distinct and all at least $2$,
then $\sum_{i=1}^{k} 1/m_i > 1$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 5, quoting Mirsky and Newman.

Stated but not proved: `MetaMathlibExt.one_lt_sum_inv_moduli_of_distinct_covering` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#one-lt-sum-inv-moduli-of-distinct-coveri).

## Replacing the largest prime factor of the modulus set

Let $m, L \in \mathbb{N}$, let
$p \ge m$ be a prime with $p \nmid L$, let $q > p$ be the largest prime dividing $L$, and write
$\nu_q(L)$ for the exponent of $q$ in $L$. Suppose there are residues $r_d \in \mathbb{Z}$, one
for each divisor $d \ge m$ of $L$, such that every integer $x$ satisfies $x \equiv r_d \pmod d$
for some such $d$. Then the same holds with $L$ replaced by $p^{\nu_q(L)} L / q^{\nu_q(L)}$:
there are residues $s_d \in \mathbb{Z}$, one for each divisor $d \ge m$ of
$p^{\nu_q(L)} L / q^{\nu_q(L)}$, such that every integer $x$ satisfies $x \equiv s_d \pmod d$
for some such $d$.

## Sources

- Jonah Klein, *On a Conjecture of Krukenberg and a Problem of Dalton and Trifonov*, INTEGERS 26 (2026), Article A38, Lemma 6.

Stated but not proved: `MetaMathlibExt.exists_covering_divisors_replace_largest_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KleinCoveringSystemsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#exists-covering-divisors-replace-largest).

## Covering systems with arbitrarily large distinct moduli (OPG-493)

The statement that
for every natural number $N$ there are finitely many residue classes $a_1 \bmod m_1, \dots,
a_k \bmod m_k$ that cover $\mathbb{Z}$ (every integer lies in at least one of them) whose moduli
are pairwise distinct and all at least $N$.

Formalized by `MathlibExt.NumberTheory.LargeModulusCoveringSystemsWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/LargeModulusCoveringSystemsWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeModulusCoveringSystemsWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#conjecture).

## Hough's minimum modulus theorem

There is a natural number $N$ such that no finite set of
residue classes covering $\mathbb{Z}$ has pairwise distinct moduli that are all at least $N$.
Hence the conjecture of Open Garden problem OPG-493 is false.

## Sources

- Bob Hough, Solution of the minimum modulus problem for covering systems, Annals of Mathematics 181 (2015), 361-382; arXiv:1307.0874, https://arxiv.org/abs/1307.0874.

Stated but not proved: `MathlibExt.NumberTheory.LargeModulusCoveringSystemsWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/LargeModulusCoveringSystemsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LargeModulusCoveringSystemsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum modulus of covering systems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/covering-systems/minimum-modulus-of-covering-systems)
