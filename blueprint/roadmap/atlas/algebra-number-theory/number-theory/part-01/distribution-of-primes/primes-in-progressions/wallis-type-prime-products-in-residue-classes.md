---
declaration: section
origin: cited
lean: MetaMathlibExt.wallis_prime_factor_eq, MetaMathlibExt.thinned_wallis_prime_product_asymptotic, MetaMathlibExt.thinned_wallis_prime_product_tendsto_pos_iff, MetaMathlibExt.thinned_wallis_prime_product_constant
statement: formalized
---

# Wallis-type prime products in residue classes

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html).

## Factor identity for Wallis-type prime products

For every odd prime $p$,

$$\frac{p - \chi_4(p)}{p + \chi_4(p)} = \frac{(1 - \chi_4(p)/p)^2}{1 - 1/p^2},$$

where $\chi_4$ is the nontrivial Dirichlet character modulo $4$.

## Sources

- Mike Winkler, *Thinned Wallis-Type Prime Products in Residue Classes Modulo 2^m*, INTEGERS 26 (2026), Article A90, Lemma 1.

Stated but not proved: `MetaMathlibExt.wallis_prime_factor_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html#wallis-prime-factor-eq).

## Asymptotic for thinned Wallis-type prime products

Let $m \ge 2$, let $q = 2^m$, and let
$S$ be a set of units of $\mathbb{Z}/q\mathbb{Z}$. Let $\varphi$ be Euler's totient function and
$\chi_4$ the nontrivial Dirichlet character modulo $4$, put $\mu(S) = \sum_{a \in S} \chi_4(a)$,
where $\chi_4(a)$ means $\chi_4$ of the reduction of $a$ modulo $4$, and for real $x$ let

$$P_S(x) = \prod_{p \le x,\ p \bmod q \in S} \frac{p - \chi_4(p)}{p + \chi_4(p)},$$

the product running over primes $p$. Then there is a real number $K > 0$ such that
$P_S(x) / \left(K (\log x)^{-2\mu(S)/\varphi(q)}\right) \to 1$ as $x \to \infty$.

## Sources

- Mike Winkler, *Thinned Wallis-Type Prime Products in Residue Classes Modulo 2^m*, INTEGERS 26 (2026), Article A90, Theorem 1.

Stated but not proved: `MetaMathlibExt.thinned_wallis_prime_product_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html#thinned-wallis-prime-product-asymptotic).

## Convergence of thinned Wallis-type prime products

Let $m \ge 2$, let $q = 2^m$, and let
$S$ be a set of units of $\mathbb{Z}/q\mathbb{Z}$. Let $\chi_4$ be the nontrivial Dirichlet
character modulo $4$, put $\mu(S) = \sum_{a \in S} \chi_4(a)$, where $\chi_4(a)$ means $\chi_4$ of
the reduction of $a$ modulo $4$, and for real $x$ let

$$P_S(x) = \prod_{p \le x,\ p \bmod q \in S} \frac{p - \chi_4(p)}{p + \chi_4(p)},$$

the product running over primes $p$. Then $P_S(x)$ converges as $x \to \infty$ to a positive real
limit if and only if $\mu(S) = 0$.

## Sources

- Mike Winkler, *Thinned Wallis-Type Prime Products in Residue Classes Modulo 2^m*, INTEGERS 26 (2026), Article A90, Corollary 1.

Stated but not proved: `MetaMathlibExt.thinned_wallis_prime_product_tendsto_pos_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html#thinned-wallis-prime-product-tendsto-pos).

## The constant in the thinned Wallis-type prime product asymptotic

Let $m \ge 2$, let
$q = 2^m$, and let $S$ be a set of units of $\mathbb{Z}/q\mathbb{Z}$. Let $\varphi$ be Euler's
totient function and $\chi_4$ the nontrivial Dirichlet character modulo $4$, put
$\mu(S) = \sum_{a \in S} \chi_4(a)$, where $\chi_4(a)$ means $\chi_4$ of the reduction of $a$
modulo $4$, and for real $x$ let

$$P_S(x) = \prod_{p \le x,\ p \bmod q \in S} \frac{p - \chi_4(p)}{p + \chi_4(p)},$$

the product running over primes $p$. Suppose that $C(a)$ and $D(a)$, for $a \in S$, are real
numbers with

$$C(a) = \lim_{x \to \infty} (\log x)^{1/\varphi(q)} \prod_{p \le x,\ p \equiv a \ (q)} (1 - 1/p),$$



$$D(a) = \lim_{x \to \infty} \prod_{p \le x,\ p \equiv a \ (q)} (1 - 1/p^2),$$

the products running over primes $p$. Put
$K = \prod_{a \in S} \left(C(a)^2 / D(a)\right)^{\chi_4(a)}$. Then
$P_S(x) / \left(K (\log x)^{-2\mu(S)/\varphi(q)}\right) \to 1$ as $x \to \infty$, and if
$\mu(S) = 0$ then $P_S(x) \to K$ as $x \to \infty$.

## Sources

- Mike Winkler, *Thinned Wallis-Type Prime Products in Residue Classes Modulo 2^m*, INTEGERS 26 (2026), Article A90, Theorem 2.

Stated but not proved: `MetaMathlibExt.thinned_wallis_prime_product_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/ThinnedWallisPrimeProductWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html#thinned-wallis-prime-product-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wallis-type prime products in residue classes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/wallis-type-prime-products-in-residue-classes)
