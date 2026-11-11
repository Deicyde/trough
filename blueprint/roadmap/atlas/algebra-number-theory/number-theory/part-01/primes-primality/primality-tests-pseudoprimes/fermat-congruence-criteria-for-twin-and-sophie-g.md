---
declaration: section
origin: cited
lean: MetaMathlibExt.twinPrime_iff_forall_fermat_congruence, MetaMathlibExt.not_isCarmichaelNumber_two_pow_mul_prime_add_one, MetaMathlibExt.isSophieGermainPrime_iff_forall_fermat_congruence, MetaMathlibExt.sophieGermainChain_fermat_congruence, MetaMathlibExt.sophieGermainChain_length_le_orderOf_two, MetaMathlibExt.forall_fermat_congruence_iff_of_coprime
statement: formalized
---

# Fermat congruence criteria for twin and Sophie Germain primes

6 results, 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html).

## Fermat-type characterizations of twin primes

Let $n \ge 3$ be odd, and suppose neither $n$
nor $n + 2$ is a Carmichael number. Then $n$ and $n + 2$ are both prime if and only if
$2a^{n+1} \equiv (n + 2)\,a^2 - n \pmod{n(n + 2)}$ for every integer $a$ coprime to $n(n + 2)$;
and $n$ and $n + 2$ are both prime if and only if
$n\,a^{n+1} \equiv (n + 2)\,a^{n-1} - 2 \pmod{n(n + 2)}$ for every integer $a$ coprime to
$n(n + 2)$.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Theorem 3.1, Congruences (3.2).

Stated but not proved: `MetaMathlibExt.twinPrime_iff_forall_fermat_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#twin-prime-iff-forall-fermat-congruence).

## Alahmadi–Luca theorem on Carmichael numbers

For every natural number $n$ and every odd
prime $p$, the number $2^n p + 1$ is not a Carmichael number.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Theorem 3.2, quoting A. Alahmadi and F. Luca, C. R. Math. Acad. Sci. Paris 360 (2022).

Stated but not proved: `MetaMathlibExt.not_isCarmichaelNumber_two_pow_mul_prime_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#not-is-carmichael-number-two-pow-mul-pri).

## Fermat-type characterizations of Sophie Germain primes

Let $p$ be a prime. Then $p$ is a
Sophie Germain prime if and only if $a^{2p} \equiv (2p + 1)\,a^{p+1} - 2p \pmod{p(2p + 1)}$ for
every integer $a$ coprime to $p(2p + 1)$; and $p$ is a Sophie Germain prime if and only if
$(2p + 1)\,a^{p-1} \equiv p\,a^{2p} + p + 1 \pmod{p(2p + 1)}$ for every integer $a$ coprime to
$p(2p + 1)$.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Theorem 3.3, Congruences (3.5).

Stated but not proved: `MetaMathlibExt.isSophieGermainPrime_iff_forall_fermat_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#is-sophie-germain-prime-iff-forall-ferma).

## Fermat-type congruences along a Sophie Germain prime chain

Let $p$ and $j$ be natural
numbers and put $q_{i+1} = 2^i (p + 1) - 1$ for $i \ge 0$, so that $q_1 = p$ and
$q_{i+2} = 2q_{i+1} + 1$. Suppose $q_1, \dots, q_{j+2}$ are all prime, and write $q = q_{j+1}$
and $q' = q_{j+2} = 2q + 1$. Then for every integer $a$ coprime to $qq'$,
$a^{q'-1} \equiv q'\,a^{q+1} - 2q \pmod{qq'}$ and
$q'\,a^{q-1} \equiv q\,a^{q'-1} + q + 1 \pmod{qq'}$.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Corollary 3.4, Congruences (3.8).

Stated but not proved: `MetaMathlibExt.sophieGermainChain_fermat_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#sophie-germain-chain-fermat-congruence).

## Length of a Sophie Germain prime chain

Let $p$ be an odd prime and let
$\mathrm{ord}_p(2)$ be the multiplicative order of $2$ modulo $p$. Then there is some
$j \le \mathrm{ord}_p(2)$ such that $2^j (p + 1) - 1$ is not prime. Thus the Sophie Germain prime
chain $q_1 = p$, $q_{i+1} = 2q_i + 1 = 2^i (p + 1) - 1$ begins with at most $\mathrm{ord}_p(2)$
consecutive primes.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Theorem 3.5, quoting T. Agoh, Tatra Mt. Math. Publ. 20 (2000), Proposition 3.1.

Stated but not proved: `MetaMathlibExt.sophieGermainChain_length_le_orderOf_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#sophie-germain-chain-length-le-order-of).

## Fermat's congruence for a product of coprime moduli

Let $n$ and $m$ be coprime natural
numbers with $0 < n < m$. Since $\gcd(m - n, nm) = 1$, the residue of $m - n$ is invertible in
$\mathbb{Z}/nm\mathbb{Z}$; write $u$ for its inverse. Then the equalities
$a^{m-1} = (a^{m-n} - 1)\,u\,n + a^{m-n}$ and
$(a^{m-n} - 1)\,u\,n + a^{m-n} = (a^{m-n} - 1)\,u\,m + 1$ in $\mathbb{Z}/nm\mathbb{Z}$ hold for
every integer $a$ coprime to $nm$ if and only if both $n$ and $m$ have the Fermat property: for
$k = n$ and for $k = m$, $a^{k-1} \equiv 1 \pmod{k}$ for every integer $a$ coprime to $k$.

This is the source's congruence
$a^{m-1} \equiv \frac{a^{m-n} - 1}{m - n}\,n + a^{m-n} \equiv \frac{a^{m-n} - 1}{m - n}\,m + 1
\pmod{nm}$, with the division by $m - n$ read as multiplication by $u$.

## Sources

- Takashi Agoh, *A Note on Fermat's Congruence*, INTEGERS 25 (2025), Article A31, Theorem 1.1 (a).

Stated but not proved: `MetaMathlibExt.forall_fermat_congruence_iff_of_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatCongruenceTwinSophieGermainWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html#forall-fermat-congruence-iff-of-coprime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fermat congruence criteria for twin and Sophie Germain primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-congruence-criteria-for-twin-and-sophie-g)
