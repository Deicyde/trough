---
declaration: lemma
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.cyclotomic_card_normalizedFactors
statement: formalized
proof: formalized
---

# Two irreducible factors

Over $\mathbb{F}_q$ with $q \equiv 5 \pmod 8$, the polynomial $X^{2^\alpha}+1 = \Phi_{2^{\alpha+1}}(X)$ factors as a product of exactly two distinct monic irreducible polynomials, each of degree $2^{\alpha-1} = d/2$.

## Depends on

- [Order of $q$ modulo the conductor](lem-order-q.md)

## Proof

$X^{2^\alpha}+1$ is the $2^{\alpha+1}$-th cyclotomic polynomial. Since $q \nmid 2^{\alpha+1}$ it is separable over $\mathbb{F}_q$, and over a finite field every irreducible factor of $\Phi_n$ has degree $\operatorname{ord}_n(q)$; the number of factors is $\varphi(n)/\operatorname{ord}_n(q)$. With $n = 2^{\alpha+1}$, $\varphi(n) = 2^\alpha$ and $\operatorname{ord}_n(q) = 2^{\alpha-1}$ (Lemma [Order of $q$ modulo the conductor](lem-order-q.md)), giving exactly $2$ factors of degree $2^{\alpha-1}$. Formalized directly from Mathlib's `Polynomial.normalizedFactors_cyclotomic_card` (factor count $= \varphi(n)/\operatorname{ord}$) together with `Nat.totient_prime_pow_succ`.

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.cyclotomic_card_normalizedFactors`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.cyclotomic_card_normalizedFactors).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 131](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L131)
