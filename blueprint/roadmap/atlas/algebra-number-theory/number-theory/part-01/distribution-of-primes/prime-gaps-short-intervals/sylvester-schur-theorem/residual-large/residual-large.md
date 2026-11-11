---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.second_residual_large_central_offset_bound, Nat.SylvesterSchur.Internal.second_residual_tiny_primeCounting_lt_start_pow
statement: formalized
proof: formalized
---

# Large residual estimates for the Sylvester-Schur theorem: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/index.html).

## Central-offset residual bound

Let $n$ and $k$ be natural numbers with $945 \le n < k$
and $k + n - 1 < 3n$, and put $N = k + n - 1$ and $i = k - n - 1$. For a natural number $m$
let $m\#$ denote the product of all primes $p \le m$, and let $P_0 = \lfloor N/3 \rfloor\#$ and
$P_j = \lfloor N^{1/(j+1)} \rfloor\#$ for $j \ge 1$. Then

$$
n \cdot 2^{i} \cdot \prod_{0 \le j < \lfloor \log_2 N \rfloor} P_j < 3^{i} \cdot 4^{n}.
$$

Formalized by `Nat.SylvesterSchur.Internal.second_residual_large_central_offset_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/CentralOffsetBound.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/CentralOffsetBound.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/index.html#second-residual-large-central-offset-bou).

## Tiny-range prime-counting bound

Let $n$ and $k$ be natural numbers with $7 \le n < 38$
and $k \ge 100$, and let $\pi(n)$ be the number of primes $p \le n$. Then
$n! \cdot (k + n - 1)^{\pi(n)} < k^{n}$.

Formalized by `Nat.SylvesterSchur.Internal.second_residual_tiny_primeCounting_lt_start_pow`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/TinyPrimeCountingBound.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/TinyPrimeCountingBound.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/index.html#second-residual-tiny-prime-counting-lt-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large residual estimates for the Sylvester-Schur theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large)
