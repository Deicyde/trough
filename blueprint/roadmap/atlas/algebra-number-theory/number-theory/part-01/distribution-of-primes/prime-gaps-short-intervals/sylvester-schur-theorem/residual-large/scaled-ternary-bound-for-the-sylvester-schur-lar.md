---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.sqrt_le_div_fifteen_of_le_four_mul, Nat.SylvesterSchur.Internal.nthRoot_three_mul_log_le_one_fifth_of_le_four_mul, Nat.SylvesterSchur.Internal.first_residual_large_scaled_ternary_bound
statement: formalized
proof: formalized
---

# Scaled ternary bound for the Sylvester-Schur large residual estimate

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar/index.html).

## Algebraic reductions

## Square root bound on a linear range

Let $n$ and $N$ be natural numbers with
$900 \le n$ and $N \le 4n$. Then $\lfloor \sqrt{N} \rfloor \le \lfloor n/15 \rfloor$.

Formalized by `Nat.SylvesterSchur.Internal.sqrt_le_div_fifteen_of_le_four_mul`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar/index.html#sqrt-le-div-fifteen-of-le-four-mul).

## Cube root times logarithm on a linear range

Let $n$ and $N$ be natural numbers with
$945 \le n$ and $N \le 4n$. Then $\lfloor N^{1/3} \rfloor \cdot \lfloor \log_2 N \rfloor \le
\lfloor n/5 \rfloor$, where $\lfloor \log_2 N \rfloor$ is read as $0$ when $N = 0$.

Formalized by `Nat.SylvesterSchur.Internal.nthRoot_three_mul_log_le_one_fifth_of_le_four_mul`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar/index.html#nth-root-three-mul-log-le-one-fifth-of-l).

## Scaled ternary bound for the first residual estimate

Let $n$ and $N$ be natural numbers
with $945 \le n$ and $3n \le N \le n^2 + n$. Then

$$
n \cdot 2^{n} \cdot (3n)^{n} \cdot 4^{n + \lfloor \sqrt{N} \rfloor + \lfloor N^{1/3} \rfloor
\lfloor \log_2 N \rfloor} < 3^{n} \cdot 4^{n} \cdot N^{n}.
$$

Formalized by `Nat.SylvesterSchur.Internal.first_residual_large_scaled_ternary_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean, line 915](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/ResidualLarge/ScaledTernaryBound.lean#L915). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar/index.html#first-residual-large-scaled-ternary-boun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scaled ternary bound for the Sylvester-Schur large residual estimate](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/residual-large/scaled-ternary-bound-for-the-sylvester-schur-lar)
