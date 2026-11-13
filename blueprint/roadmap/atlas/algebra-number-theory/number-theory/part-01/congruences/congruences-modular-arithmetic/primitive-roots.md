---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaDelta, MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaH, MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.primitiveLambdaRootCount, MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.carmichael_mul_eq_lcm, MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaH_mul_ge_and_gt_iff, MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.primitiveLambdaRootCount_mul_ge_and_eq_iff
statement: formalized
---

# Primitive λ-roots

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html).

## The count $\Delta_q(n)$ for primitive λ-roots

Let $\lambda$ be the Carmichael function
and, for natural numbers $p$ and $m$, let $v_p(m)$ be the exponent of $p$ in the prime
factorization of $m$ (taken to be $0$ when $p$ is not prime or $m = 0$). For natural numbers
$q$ and $n$, the natural number $\Delta_q(n)$ is defined as follows. If $q = 2$, $v_2(n) = 3$
and $v_2(\lambda(n)) = 1$, then $\Delta_q(n)$ is one more than the number of distinct prime
factors of $n$. Otherwise, if $q$ divides $\lambda(n)$, then $\Delta_q(n)$ is the number of
prime factors $p$ of $n$ (there are none when $n = 0$) such that $q^{v_q(\lambda(n))}$ divides
$\lambda(p^{v_p(n)})$. In all remaining cases $\Delta_q(n) = 0$.

The argument $q$ is intended to be prime; the definition is the displayed formula for every
natural $q$.

Formalized by `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaDelta`, a definition declared in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#lambda-delta).

## The local factor $h_q(n)$ for primitive λ-roots

Let $\Delta_q(n)$ be the count for
primitive λ-roots. For natural numbers $q$ and $n$, the rational number $h_q(n)$ equals $1$ if
$\Delta_q(n) = 0$, and $1 - 1/q^{\Delta_q(n)}$ otherwise.

Formalized by `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaH`, a definition declared in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#lambda-h).

## Number of primitive λ-roots

For a natural number $n$, $R(n)$ is the number of units $a$
of $\mathbb{Z}/n\mathbb{Z}$ whose multiplicative order equals $\lambda(n)$, where $\lambda$ is
the Carmichael function.

Formalized by `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.primitiveLambdaRootCount`, a definition declared in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#primitive-lambda-root-count).

## Carmichael's function on coprime products

For coprime natural numbers $m, n > 1$,
the Carmichael function $\lambda$ satisfies
$\lambda(mn) = \operatorname{lcm}(\lambda(m), \lambda(n))$.

## Sources

- Benjamin Huang and Shuguang Li, "Notes on the Number of Primitive λ-roots mod n and Its Multiplicative Properties", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.carmichael_mul_eq_lcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#carmichael-mul-eq-lcm).

## Huang–Li inequality for the local factors $h_q$

Let $\lambda$ be the Carmichael function,
and let $\Delta_q$ and $h_q$ be the count and the local factor for primitive λ-roots. Let
$m, n > 1$ be coprime natural numbers and let $q$ be a prime dividing $\lambda(mn)$. Then
$h_q(m)\,h_q(n) \le h_q(mn)$. Moreover, $h_q(m)\,h_q(n) < h_q(mn)$ if and only if at least one
of the following holds: $0 < \Delta_q(m) < \Delta_q(mn)$; $0 < \Delta_q(n) < \Delta_q(mn)$; or
$\Delta_q(m) > 0$, $\Delta_q(n) > 0$, and $\Delta_q(mn)$ equals $\Delta_q(m)$ or $\Delta_q(n)$.

## Sources

- Benjamin Huang and Shuguang Li, "Notes on the Number of Primitive λ-roots mod n and Its Multiplicative Properties", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.lambdaH_mul_ge_and_gt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#lambda-h-mul-ge-and-gt-iff).

## Supermultiplicativity of the number of primitive λ-roots

Let $R(n)$ be the number of
primitive λ-roots modulo $n$. For coprime natural numbers $m, n > 1$, we have
$R(m)\,R(n) \le R(mn)$, and $R(mn) = R(m)\,R(n)$ if and only if $m = 2$ and $n$ is odd, or
$n = 2$ and $m$ is odd.

## Sources

- Benjamin Huang and Shuguang Li, "Notes on the Number of Primitive λ-roots mod n and Its Multiplicative Properties", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveLambdaRootsWanted.primitiveLambdaRootCount_mul_ge_and_eq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitiveLambdaRootsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html#primitive-lambda-root-count-mul-ge-and-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive λ-roots](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots)
