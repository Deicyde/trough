---
declaration: section
origin: cited
lean: MetaMathlibExt.ten_pow_blockLength_modEq_two_pow, MetaMathlibExt.mersenne_reciprocal_block_recurrence
statement: formalized
---

# Decimal expansion of reciprocals of Mersenne primes

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/decimal-expansion-of-reciprocals-of-mersenne-pri/index.html).

## The block-length power of ten is a power of two modulo the Mersenne prime

Let $p$ be a
natural number such that $M = 2^p - 1$ is prime, let $L$ be the multiplicative order of $10$ modulo
$M$ (the period of the decimal expansion of $1/M$), and suppose that $p$ divides $L$. Then there is
a natural number $r$ with $1 \le r \le p - 1$ such that $10^{L/p} \equiv 2^r \pmod{M}$.

## Sources

- Amitabha Tripathi, *A Note on the Decimal Expansion of Reciprocals of Mersenne Primes*, INTEGERS 24 (2024), Article A14, Proposition 1.

Stated but not proved: `MetaMathlibExt.ten_pow_blockLength_modEq_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MersenneReciprocalBlocksWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MersenneReciprocalBlocksWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/decimal-expansion-of-reciprocals-of-mersenne-pri/index.html#ten-pow-block-length-mod-eq-two-pow).

## Doubling recurrence for the blocks of $1/(2^p - 1)$

Let $p$ be a natural number such
that $M = 2^p - 1$ is prime, let $L$ be the multiplicative order of $10$ modulo $M$ (the period of
the decimal expansion of $1/M$), and suppose that $p$ divides $L$. Put $\ell = L/p$ and let
$N = (10^L - 1)/M$ be the repeating block of $1/M$, read as an $L$-digit integer with leading
zeros. For $1 \le k \le p$ let $B_k = \lfloor N / 10^{\ell (p - k)} \rfloor \bmod 10^\ell$ be
the $k$-th block of $\ell$ digits of $N$ from the left, and extend the indices to all $j \ge 1$
by $B_j = B_k$ where $k = ((j - 1) \bmod p) + 1$. Let $r$ and $s$ be natural numbers with
$1 \le r \le p - 1$, $10^\ell \equiv 2^r \pmod{M}$ and $rs \equiv 1 \pmod{p}$. Then, as
integers:

(i) for every $k$ with $1 \le k \le p$, $B_{ks+1} = 2B_{(k-1)s+1} - 10^\ell$ if $k = p$,
$B_{ks+1} = 2B_{(k-1)s+1} + 1$ if $k = p - r$, and $B_{ks+1} = 2B_{(k-1)s+1}$ otherwise;

(ii) if $r = 1$, then for every $k$ with $1 \le k \le p$, $B_{k+1} = 2B_k - 10^\ell$ if $k = p$,
$B_{k+1} = 2B_k + 1$ if $k = p - 1$, and $B_{k+1} = 2B_k$ otherwise;

(iii) $B_1 + B_2 + \dots + B_p = 10^\ell - 1$.

## Sources

- Amitabha Tripathi, *A Note on the Decimal Expansion of Reciprocals of Mersenne Primes*, INTEGERS 24 (2024), Article A14, Theorem 1.

Stated but not proved: `MetaMathlibExt.mersenne_reciprocal_block_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MersenneReciprocalBlocksWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MersenneReciprocalBlocksWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/decimal-expansion-of-reciprocals-of-mersenne-pri/index.html#mersenne-reciprocal-block-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decimal expansion of reciprocals of Mersenne primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/decimal-expansion-of-reciprocals-of-mersenne-pri/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/decimal-expansion-of-reciprocals-of-mersenne-pri)
