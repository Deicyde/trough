---
declaration: section
origin: cited
lean: MathlibExt.SelbergSieve.levelSet, MathlibExt.SelbergSieve.levelSum, MathlibExt.SelbergSieve.levelY, MathlibExt.SelbergSieve.levelWeights, MathlibExt.SelbergSieve.levelSum_ge_one, MathlibExt.SelbergSieve.levelWeights_inner, MathlibExt.SelbergSieve.levelWeights_one, MathlibExt.SelbergSieve.levelWeights_mainSum
statement: formalized
proof: formalized
---

# Selberg sieve

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html).

## Selberg level set

For a bounding sieve whose sifting primes have product $P$ and a
natural number $R$, the level-$R$ set is the set of divisors $l$ of $P$ with $l \le R$.

Formalized by `MathlibExt.SelbergSieve.levelSet`, a definition declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-set).

## Selberg level sum

For a bounding sieve whose sifting primes have product $P$, with
multiplicative density function $\nu$, and a natural number $R$, the level-$R$ Selberg sum is
$G = \sum_{l \mid P,\ l \le R} g(l)$, where $g(l) = \nu(l) \prod_{p \mid l} (1 - \nu(p))^{-1}$,
the product running over the primes $p$ dividing $l$.

Formalized by `MathlibExt.SelbergSieve.levelSum`, a definition declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-sum).

## Normalized Selberg coefficients

Let $s$ be a bounding sieve with density function $\nu$
and Selberg terms $g(l) = \nu(l) \prod_{p \mid l} (1 - \nu(p))^{-1}$, the product running over
the primes $p$ dividing $l$, and let $R$ be a natural number. Write $D_R$ for the level set of $s$
at level $R$ (the divisors of the sifting product of $s$ that are at most $R$) and
$G(R) = \sum_{l \in D_R} g(l)$ for the level sum. The normalized Selberg coefficient of $s$ at
level $R$ is the function on natural numbers given by $y_l = \mu(l)\, g(l) / G(R)$ for
$l \in D_R$ and $y_l = 0$ otherwise, where $\mu$ is the Möbius function.

Formalized by `MathlibExt.SelbergSieve.levelY`, a definition declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-y).

## Selberg sieve weights

Let $s$ be a bounding sieve with sifting product $P$ (the product
of its sifting primes) and density function $\nu$, let $R$ be a natural number, and let $y_m$
denote the normalized Selberg coefficients of $s$ at level $R$. For a natural number $d$, the
level-$R$ Selberg weight of $s$ at $d$ is

$$\lambda_d = \nu(d)^{-1} \sum_{m \mid P,\ d \mid m} \mu(m/d)\, y_m,$$

where $\mu$ is the Möbius function, $m$ runs over the divisors of $P$, and $\nu(d)^{-1}$ is read
as $0$ when $\nu(d) = 0$.

Formalized by `MathlibExt.SelbergSieve.levelWeights`, a definition declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights).

## The Selberg level sum is at least one

For every bounding sieve and every natural number
$R \ge 1$, the level-$R$ Selberg sum is at least $1$.

Formalized by `MathlibExt.SelbergSieve.levelSum_ge_one`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-sum-ge-one).

## Inversion formula for the Selberg level weights

For a bounding sieve whose sifting primes
have product $P$, with density function $\nu$, a natural number $R$ and a divisor $l$ of $P$, the
level-$R$ Selberg weights $\lambda_d$ satisfy $\sum_{d \mid P,\ l \mid d} \nu(d)\,\lambda_d = y_l$,
where $y_l$ is the normalized level-$R$ Selberg $y$-coefficient at $l$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_inner`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-inner).

## The Selberg level weight at one

For every bounding sieve and every natural number
$R \ge 1$, the level-$R$ Selberg weight at $1$ equals $1$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_one`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-one).

## Main term of the Selberg level weights

For a bounding sieve whose sifting primes have
product $P$, with density function $\nu$, and a natural number $R \ge 1$, let $\lambda_d$ be the
level-$R$ Selberg weights and
$\Lambda_d = \sum_{d_1, d_2 \mid d,\ \operatorname{lcm}(d_1, d_2) = d} \lambda_{d_1} \lambda_{d_2}$
their $\Lambda^2$ coefficients. Then $\sum_{d \mid P} \Lambda_d\,\nu(d) = 1/G$, where $G$ is the
level-$R$ Selberg sum.

Formalized by `MathlibExt.SelbergSieve.levelWeights_mainSum`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-main-sum).

## Weighted bound for the Selberg level weights

For a bounding sieve whose sifting primes
have product $P$, with density function $\nu$, a natural number $R \ge 1$ and a divisor $d$ of
$P$, the level-$R$ Selberg weight $\lambda_d$ at $d$ satisfies $|\nu(d)\,\lambda_d| \le 1$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_nu_mul_abs_le`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-nu-mul-abs-le).

## Selberg level weights are bounded by one

For a bounding sieve whose sifting primes have
product $P$, a natural number $R \ge 1$ and a divisor $d$ of $P$, the level-$R$ Selberg weight
$\lambda_d$ at $d$ satisfies $|\lambda_d| \le 1$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_abs_le`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-abs-le).

## Support of the Selberg level weights

For every bounding sieve and all natural numbers $R$
and $d$, if the level-$R$ Selberg weight $\lambda_d$ at $d$ is nonzero, then $d \le R$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_support`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-support).

## Error bound for the Selberg level weights

Take a bounding sieve whose sifting primes have
product $P$, with density function $\nu$ and remainders $r_d = A_d - \nu(d) X$, where $A_d$ is the
total weight of the multiples of $d$ in the set to be sifted and $X$ approximates its total
weight. Let $R \ge 1$ be a natural number and suppose that $d\,\nu(d) \ge 1$ and $|r_d| \le d$ for
every divisor $d$ of $P$. Let $\lambda_d$ be the level-$R$ Selberg weights and
$\Lambda_d = \sum_{d_1, d_2 \mid d,\ \operatorname{lcm}(d_1, d_2) = d} \lambda_{d_1} \lambda_{d_2}$
their $\Lambda^2$ coefficients. Then $\sum_{d \mid P} |\Lambda_d|\,|r_d| \le R^{12}$.

Formalized by `MathlibExt.SelbergSieve.levelWeights_errSum_le`, a theorem declared in [MathlibExt/NumberTheory/SelbergSieve.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SelbergSieve.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html#level-weights-err-sum-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Selberg sieve](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/selberg-sieve)
