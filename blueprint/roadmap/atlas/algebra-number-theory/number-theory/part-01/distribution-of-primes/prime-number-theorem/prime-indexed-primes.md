---
declaration: section
origin: cited
lean: MetaMathlibExt.primePrimes_ratio_tendsto_one', MetaMathlibExt.primePrimes_oneBased_ratio_tendsto_one, MetaMathlibExt.primePrimes_ratio_tendsto_one
statement: formalized
proof: formalized
---

# Prime-indexed primes

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes/index.html).

## Ratio of consecutive zero-based prime-indexed primes tends to one

Let
$p_0 = 2$, $p_1 = 3$, $p_2 = 5$, $\dots$ be the primes in increasing order, indexed from zero,
and let $q_n = p_{p_n}$. Then $q_n / q_{n+1} \to 1$ as $n \to \infty$.

Formalized by `MetaMathlibExt.primePrimes_ratio_tendsto_one'`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes/index.html#prime-primes-ratio-tendsto-one).

## Ratio of consecutive prime-indexed primes tends to one

Let $p_1 = 2$, $p_2 = 3$, $p_3 = 5$,
$\dots$ be the primes in increasing order and let $q_n = p_{p_n}$. Then $q_n / q_{n+1} \to 1$ as
$n \to \infty$.

This is part (c) of the Broughan–Barnett corollary, in the source's one-based indexing.

Formalized by `MetaMathlibExt.primePrimes_oneBased_ratio_tendsto_one`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes/index.html#prime-primes-one-based-ratio-tendsto-one).

## Broughan–Barnett ratio limit, zero-based form

Assume that there are infinitely many primes
(which always holds). Let $p_0 = 2$, $p_1 = 3$, $p_2 = 5$, $\dots$ be the primes in increasing
order, indexed from zero, and let $q_n = p_{p_n}$. Then $q_n / q_{n+1} \to 1$ as $n \to \infty$.

In the source's one-based indexing $p'_1 = 2$, $p'_2 = 3$, $\dots$, this $q_n$ equals
$p'_{p'_{n+1} + 1}$ rather than the source's prime-indexed prime $p'_{p'_{n+1}}$; the source
states the same limit for its sequence.

## Sources

- Kevin A. Broughan and A. Ross Barnett, "On the Subsequence of Primes Having Prime Subscripts," Journal of Integer Sequences 12 (2009), Article 09.2.3, Corollary to the Theorem, part (c), lines 193–199, https://cs.uwaterloo.ca/journals/JIS/VOL12/Broughan/broughan16.tex

Formalized by `MetaMathlibExt.primePrimes_ratio_tendsto_one`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/PrimePrimeRatio.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes/index.html#prime-primes-ratio-tendsto-one-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime-indexed primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-indexed-primes)
