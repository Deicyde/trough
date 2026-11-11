---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DelannoyTriangleWanted.harmonicMod, MathlibExt.NumberTheory.DelannoyTriangleWanted.harmonic2Mod, MathlibExt.NumberTheory.DelannoyTriangleWanted.delannoy_two_mul, MathlibExt.NumberTheory.DelannoyTriangleWanted.delannoy_mul_sub_one, MathlibExt.NumberTheory.DelannoyTriangleWanted.choose_mul_sub_one_mod, MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_two_pow_div, MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_harmonic_two_pow_div, MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_delannoy
statement: formalized
---

# Congruences for Delannoy numbers

10 results, 2 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html).

## Harmonic numbers modulo $m$

For natural numbers $m$ and $k$, the harmonic number
$H_k$ modulo $m$ is the residue $\sum_{i=1}^{k} i^{-1}$ in $\mathbb{Z}/m\mathbb{Z}$, where
$i^{-1}$ is the inverse of $i$ modulo $m$ when $i$ is coprime to $m$; for other $i$ it is the
conventional value that Mathlib assigns to the inverse of a non-unit.

Formalized by `MathlibExt.NumberTheory.DelannoyTriangleWanted.harmonicMod`, a definition declared in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#harmonic-mod).

## Harmonic numbers of order two modulo $m$

For natural numbers $m$ and $k$, the
harmonic number $H_{k,2}$ of order two modulo $m$ is the residue $\sum_{i=1}^{k} (i^2)^{-1}$
in $\mathbb{Z}/m\mathbb{Z}$, where $(i^2)^{-1}$ is the inverse of $i^2$ modulo $m$ when $i$ is
coprime to $m$; for other $i$ it is the conventional value that Mathlib assigns to the
inverse of a non-unit.

Formalized by `MathlibExt.NumberTheory.DelannoyTriangleWanted.harmonic2Mod`, a definition declared in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#harmonic2-mod).

## Delannoy triangle entries $T(2p, p; 1)$ and $T(2p-1, p-1; 1)$ modulo $p^3$

Let
$p \ge 5$ be a prime, let $q_p(2) = (2^{p-1} - 1)/p$ be the Fermat quotient of $2$, and let
$T(n, k; 1)$ denote the entry of the ordinary Riordan Pascal-like triangle with $r = 1$ (the
Delannoy triangle). Then

$$T(2p, p; 1) \equiv 3 + 2p\,q_p(2) - p^2 q_p(2)^2 \pmod{p^3}$$

and

$$T(2p-1, p-1; 1) \equiv 1 + 2p\,q_p(2) - p^2 q_p(2)^2 \pmod{p^3}.$$

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.delannoy_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#delannoy-two-mul).

## Delannoy triangle entry $T(np-1, p-1; 1)$ modulo $p^3$

Let $p \ge 5$ be a prime and
$n \ge 1$ a natural number, let $q_p(2) = (2^{p-1} - 1)/p$ be the Fermat quotient of $2$, and
let $T(a, b; 1)$ denote the entry of the ordinary Riordan Pascal-like triangle with $r = 1$
(the Delannoy triangle). Then

$$T(np - 1, p - 1; 1) \equiv 1 + (n - 1)\,p\,q_p(2)\,\bigl(2 - p\,q_p(2)\bigr) \pmod{p^3}.$$

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.delannoy_mul_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#delannoy-mul-sub-one).

## Expansion of $\binom{sp-1}{k}$ modulo $p^3$

Let $p$ be an odd prime, $s$ an integer
and $k$ a natural number with $1 \le k \le p - 1$, and let $H_k = \sum_{i=1}^{k} i^{-1}$ and
$H_{k,2} = \sum_{i=1}^{k} (i^2)^{-1}$ be the harmonic numbers of orders one and two in
$\mathbb{Z}/p^3\mathbb{Z}$. Then in $\mathbb{Z}/p^3\mathbb{Z}$

$$
\frac{1}{k!} \prod_{i=1}^{k} (sp - i) =
(-1)^k \Bigl(1 - sp\,H_k + \frac{s^2 p^2}{2} \bigl(H_k^2 - H_{k,2}\bigr)\Bigr),
$$

where $1/k!$ and $1/2$ are inverses in $\mathbb{Z}/p^3\mathbb{Z}$; the left side is the
binomial coefficient $\binom{sp-1}{k}$.

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.choose_mul_sub_one_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#choose-mul-sub-one-mod).

## Sums of $2^k/k$ and $2^k/k^2$ over $1 \le k \le p - 1$

Let $p > 3$ be a prime and let
$q_p(2) = (2^{p-1} - 1)/p$ be the Fermat quotient of $2$. Then

$$\sum_{k=1}^{p-1} \frac{2^k}{k} \equiv -2\,q_p(2) \pmod{p^2}$$

and

$$\sum_{k=1}^{p-1} \frac{2^k}{k^2} \equiv -q_p(2)^2 \pmod{p},$$

where $1/k$ is the inverse of $k$ modulo $p^2$ and $1/k^2$ the inverse of $k^2$ modulo $p$.

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_two_pow_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#sum-two-pow-div).

## Sum of $H_k 2^k / k$ over $1 \le k \le p - 1$ modulo $p$

Let $p \ge 5$ be a prime, let
$q_p(2) = (2^{p-1} - 1)/p$ be the Fermat quotient of $2$, and let $H_k = \sum_{i=1}^{k} 1/i$
be the harmonic number modulo $p$, where $1/i$ is the inverse of $i$ modulo $p$. Then

$$\sum_{k=1}^{p-1} \frac{H_k\, 2^k}{k} \equiv -q_p(2)^2 \pmod{p}.$$

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Lemma 7.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_harmonic_two_pow_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#sum-harmonic-two-pow-div).

## Sum of the Delannoy triangle entries in rows $0$ to $p - 1$ modulo $p$

Let $p$ be an
odd prime and let $T(n, k; 1)$ denote the entry of the ordinary Riordan Pascal-like triangle
with $r = 1$ (the Delannoy triangle). Then

$$\sum_{n=0}^{p-1} \sum_{k=0}^{n} T(n, k; 1) \equiv \left(\frac{2}{p}\right) \pmod{p},$$

where $\left(\frac{2}{p}\right)$ is the Legendre symbol.

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Theorem 9.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_delannoy` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#sum-delannoy).

## Reflection congruence for binomial coefficients modulo a prime

For a prime $p$ and
natural numbers $j$ and $k$ with $j \le k \le p - 2$,

$$\binom{p-j}{k+1} + (-1)^k \binom{k+j}{k+1} \equiv 0 \pmod{p}.$$

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Lemma 11.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.choose_add_choose_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#choose-add-choose-mod).

## A binomial sum through central Delannoy numbers

For every natural number $k$,

$$4 \sum_{j=0}^{k} \binom{k}{j} \binom{k+j}{k+1} = D_{k+1} - 3 D_k,$$

where $D_n = A_{1,1}(n) = \sum_{i=0}^{n} \binom{n}{i} \binom{n+i}{i}$ is the binomial-power
number with $r = s = 1$, that is, the $n$-th central Delannoy number.

## Sources

- Chahinaze Djadi and Hacène Belbachir, "Congruence Properties for the Delannoy Triangle Coefficients", Lemma 13.

Stated but not proved: `MathlibExt.NumberTheory.DelannoyTriangleWanted.sum_choose_choose_binomialPowerSeq` is written with `theorem_wanted` in [WantedExt/NumberTheory/DelannoyTriangleWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DelannoyTriangleWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html#sum-choose-choose-binomial-power-seq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Congruences for Delannoy numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/congruences-for-delannoy-numbers)
