---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.FkPerfectWanted.KLDeficientPerfectWith, MathlibExt.NumberTheory.FkPerfectWanted.IsKLDeficientPerfect, MathlibExt.NumberTheory.FkPerfectWanted.KLNearPerfectWith, MathlibExt.NumberTheory.FkPerfectWanted.IsKLNearPerfect, MathlibExt.NumberTheory.FkPerfectWanted.IsDeficientFkPerfect, MathlibExt.NumberTheory.FkPerfectWanted.IsNearFkPerfect, MathlibExt.NumberTheory.FkPerfectWanted.IsDeficientFPerfect, MathlibExt.NumberTheory.FkPerfectWanted.IsNearFPerfect
statement: formalized
---

# Near-perfect and deficient-perfect numbers

52 results, 8 proved and 44 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html).

## $(k,\ell)$-deficient-perfect with a given divisor

For natural numbers $k$, $\ell$, $n$
and $d$, the number $n$ is $[k,\ell]$-deficient-perfect with divisor $d$ when $d$ is a proper
divisor of $n$ ($d \mid n$ and $d < n$) and $\sigma_k(n) + d^k = n^k + \ell n$, where
$\sigma_k(n) = \sum_{e \mid n} e^k$ is the sum of the $k$-th powers of the divisors of $n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.KLDeficientPerfectWith`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#kldeficient-perfect-with).

## $(k,\ell)$-deficient-perfect numbers

For natural numbers $k$, $\ell$ and $n$, write
$\sigma_k(n) = \sum_{e \mid n} e^k$. The number $n$ is $[k,\ell]$-deficient-perfect when there is a
divisor $d$ of $n$ with $d < n$ such that $\sigma_k(n) + d^k = n^k + \ell n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsKLDeficientPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-kldeficient-perfect).

## $(k,\ell)$-near-perfect with a given divisor

For natural numbers $k$, $\ell$, $n$ and
$d$, the number $n$ is $[k,\ell]$-near-perfect with divisor $d$ when $d$ is a proper divisor of
$n$ ($d \mid n$ and $d < n$) and $\sigma_k(n) = n^k + d^k + \ell n$, where
$\sigma_k(n) = \sum_{e \mid n} e^k$ is the sum of the $k$-th powers of the divisors of $n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.KLNearPerfectWith`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#klnear-perfect-with).

## $(k,\ell)$-near-perfect numbers

For natural numbers $k$, $\ell$ and $n$, write
$\sigma_k(n) = \sum_{e \mid n} e^k$. The number $n$ is $[k,\ell]$-near-perfect when there is a
divisor $d$ of $n$ with $d < n$ such that $\sigma_k(n) = n^k + d^k + \ell n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsKLNearPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-klnear-perfect).

## Deficient $F_k$-perfect numbers

For natural numbers $k$ and $n$, write
$\sigma_k(n) = \sum_{e \mid n} e^k$. The number $n$ is deficient $F_k$-perfect when it is
$[k,3]$-deficient-perfect, that is, when there is a divisor $d$ of $n$ with $d < n$ such that
$\sigma_k(n) + d^k = n^k + 3n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsDeficientFkPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-deficient-fk-perfect).

## Near $F_k$-perfect numbers

For natural numbers $k$ and $n$, the number $n$ is near
$F_k$-perfect when it is $[k,3]$-near-perfect, that is, when some proper divisor $d$ of $n$
($d \mid n$ and $d < n$) satisfies $\sigma_k(n) = n^k + d^k + 3n$, where
$\sigma_k(n) = \sum_{e \mid n} e^k$ is the sum of the $k$-th powers of the divisors of $n$.

No condition $k > 1$ is imposed here; the results that need it assume it.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsNearFkPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-near-fk-perfect).

## Deficient $F$-perfect numbers

For a natural number $n$, write
$\sigma_2(n) = \sum_{e \mid n} e^2$. The number $n$ is deficient $F$-perfect when it is
$[2,3]$-deficient-perfect, that is, when there is a divisor $d$ of $n$ with $d < n$ such that
$\sigma_2(n) + d^2 = n^2 + 3n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsDeficientFPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-deficient-fperfect).

## Near $F$-perfect numbers

A natural number $n$ is near $F$-perfect when it is
$[2,3]$-near-perfect, that is, when some proper divisor $d$ of $n$ ($d \mid n$ and $d < n$)
satisfies $\sigma_2(n) = n^2 + d^2 + 3n$, where $\sigma_2(n) = \sum_{e \mid n} e^2$ is the sum
of the squares of the divisors of $n$.

Formalized by `MathlibExt.NumberTheory.FkPerfectWanted.IsNearFPerfect`, a definition declared in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-near-fperfect).

## Odd primes are not $(k,\ell)$-deficient-perfect

Let $p$ be an odd prime. Then for all
natural numbers $k$ and $\ell$, $p$ is not $[k,\ell]$-deficient-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isKLDeficientPerfect_of_prime_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-kldeficient-perfect-of-prime-odd).

## $2$ is $(k,1)$-deficient-perfect

For every natural number $k$, the number $2$ is
$[k,1]$-deficient-perfect.

The divisor is $d = 1$, since $1 + 2^k + 1^k = 2^k + 1 \cdot 2$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isKLDeficientPerfect_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-kldeficient-perfect-two).

## No prime is deficient $F$-perfect

If $p$ is a prime, then $p$ is not deficient
$F$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isDeficientFPerfect_of_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-deficient-fperfect-of-prime).

## Primes are not $(k,\ell)$-near-perfect

Let $k$ and $\ell$ be natural numbers with
$\ell \ge 1$ and let $p$ be a prime. Then $p$ is not $[k,\ell]$-near-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isKLNearPerfect_of_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-klnear-perfect-of-prime).

## No prime power is deficient $F$-perfect or near $F$-perfect

For every prime $p$ and
every natural number $a$, the number $n = p^a$ is neither deficient $F$-perfect nor near
$F$-perfect: there is no divisor $d$ of $n$ with $d < n$ and $\sigma_2(n) + d^2 = n^2 + 3n$, and
no divisor $d$ of $n$ with $d < n$ and $\sigma_2(n) = n^2 + d^2 + 3n$, where $\sigma_2(n)$ is the
sum of the squares of the divisors of $n$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.prime_pow_not_fPerfect` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#prime-pow-not-f-perfect).

## Prime powers that are $(2,\ell)$-near-perfect

Let $p$ be a prime, let $a$, $\ell$ and
$d$ be natural numbers with $\ell \ge 1$, and write $\sigma_2(m)$ for the sum of the squares of
the divisors of $m$. Then $d$ is a proper divisor of $p^a$ ($d \mid p^a$ and $d < p^a$) with
$\sigma_2(p^a) = (p^a)^2 + d^2 + \ell p^a$ if and only if $a = 2$, $\ell = 1$ and $d = 1$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.klNearPerfectWith_prime_pow_two_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#kl-near-perfect-with-prime-pow-two-iff).

## $(2,\ell)$-deficient-perfect prime powers (corrected)

Let $p$ be a prime and let $a$ and
$\ell$ be natural numbers. If $p^a$ is $[2,\ell]$-deficient-perfect, then $\ell = 1$, and either
$a = 2$, or $p = 2$ and $a = 1$.

The printed statement allows only the exception $a = 2$, $\ell = 1$, and so omits the solution
$p = 2$, $a = 1$, $\ell = 1$, $d = 1$ (the number $2$ of Corollary 1).

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isKLDeficientPerfect_prime_pow_two_imp` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-kldeficient-perfect-prime-pow-two-imp).

## Prime powers that are $(k,\ell)$-near-perfect

Let $p$ be a prime, let $a$, $k$, $\ell$
and $d$ be natural numbers with $k \ge 1$ and $\ell \ge 1$, and write
$\sigma_k(m) = \sum_{e \mid m} e^k$. Then $d$ is a proper divisor of $p^a$ ($d \mid p^a$ and
$d < p^a$) with $\sigma_k(p^a) = (p^a)^k + d^k + \ell p^a$ if and only if $2 \le a \le k$,
$d = 1$ and $\ell = p^{k-a} \sum_{i=0}^{a-2} p^{ik}$.

The source prints the conclusion $a = k$, which is false: for $p = 2$, $a = 2$, $k = 3$,
$\ell = 2$, $d = 1$ one has $\sigma_3(4) = 73 = 4^3 + 1^3 + 2 \cdot 4$ with $a \ne k$. The
printed form is the case $a = k$ of the identity $\sum_{i=1}^{a-1} p^{ik} = \ell p^a$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.klNearPerfectWith_prime_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#kl-near-perfect-with-prime-pow-iff).

## $(k,\ell)$-deficient-perfect prime powers for $k \ge 2$

Let $p$ be a prime and let $a$,
$k$ and $\ell$ be natural numbers with $k \ge 2$. If $p^a$ is $[k,\ell]$-deficient-perfect, then
$p = 2$ and $a = 1$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 5.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isKLDeficientPerfect_prime_pow_imp` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-kldeficient-perfect-prime-pow-imp).

## Prime powers that are $(1,\ell)$-deficient-perfect with a given divisor

Let $p$ be a
prime, let $a$, $\ell$ and $d$ be natural numbers, and write $\sigma_1(m)$ for the sum of the
divisors of $m$. Then $d$ is a proper divisor of $p^a$ ($d \mid p^a$ and $d < p^a$) with
$\sigma_1(p^a) + d = p^a + \ell p^a$ if and only if $p = 2$, $\ell = 1$, $d = 1$ and $a \ge 1$.

This is the $k = 1$ part of Theorem 5 of the source.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 5.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.klDeficientPerfectWith_one_prime_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#kl-deficient-perfect-with-one-prime-pow).

## Twice an odd prime is not $(k,\ell)$-near-perfect

Let $k$ and $\ell$ be natural numbers
with $\ell \ge 1$ and let $p$ be an odd prime. Then $2p$ is not $[k,\ell]$-near-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isKLNearPerfect_two_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-klnear-perfect-two-mul-prime).

## Deficient $F$-perfect numbers of the form $2^a p$

Let $p$ be a prime and $a$ a natural
number. If $2^a p$ is deficient $F$-perfect, then $p = 3$ and $a = 1$, so the number is $6$.

The number $6$ is indeed deficient $F$-perfect, with $d = 2$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 7.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isDeficientFPerfect_two_pow_mul_prime_imp` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-deficient-fperfect-two-pow-mul-prime).

## $2^a p$ is not $(k,\ell)$-deficient-perfect with divisor $1$ or $p$

Let $k$, $\ell$, $a$
be natural numbers with $\ell \ge 1$ and let $p$ be an odd prime. Call $n$
$[k,\ell]$-deficient-perfect with divisor $d$ when $d$ divides $n$, $d < n$ and
$\sigma_k(n) + d^k = n^k + \ell n$, where $\sigma_k(n)$ is the sum of the $k$-th powers of the
divisors of $n$. Then $2^a p$ is not $[k,\ell]$-deficient-perfect with divisor $1$, and not with
divisor $p$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 8.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_klDeficientPerfectWith_two_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-kl-deficient-perfect-with-two-pow-mu).

## No near $F$-perfect number of the form $2^a p$

For every prime $p$ and every natural
number $a$, the number $n = 2^a p$ is not near $F$-perfect: there is no divisor $d$ of $n$ with
$d < n$ and $\sigma_2(n) = n^2 + d^2 + 3n$, where $\sigma_2(n)$ is the sum of the squares of the
divisors of $n$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 9.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFPerfect_two_pow_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fperfect-two-pow-mul-prime).

## No $(2,\ell)$-near-perfect number of the form $2^a p$

Let $\ell$ and $a$ be natural
numbers with $\ell \ge 1$, and let $p$ be an odd prime. Then $2^a p$ is not
$[2,\ell]$-near-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 10.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isKLNearPerfect_two_two_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-klnear-perfect-two-two-pow-mul).

## For $a \ge 2$, $2^a p$ is not $(k,\ell)$-near-perfect with divisor $1$ or $p$

Let $k$,
$\ell$, $a$ be natural numbers with $\ell \ge 1$ and $a \ge 2$, and let $p$ be an odd prime. Call
$n$ $[k,\ell]$-near-perfect with divisor $d$ when $d$ divides $n$, $d < n$ and
$\sigma_k(n) = n^k + d^k + \ell n$, where $\sigma_k(n)$ is the sum of the $k$-th powers of the
divisors of $n$. Then $2^a p$ is not $[k,\ell]$-near-perfect with divisor $1$, and not with
divisor $p$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 11.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_klNearPerfectWith_two_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-kl-near-perfect-with-two-pow-mul).

## The only deficient $F$-perfect number of the form $2p^a$ is $6$

The number $6$ is deficient
$F$-perfect, and for every prime $p$ and every natural number $a$, if $2p^a$ is deficient
$F$-perfect then $2p^a = 6$.

The divisor for $6$ is $d = 2$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 12.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isDeficientFPerfect_two_mul_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-deficient-fperfect-two-mul-prime-pow).

## No near $F$-perfect number of the form $2p^a$

For every prime $p$ and every natural
number $a$, the number $n = 2p^a$ is not near $F$-perfect: there is no divisor $d$ of $n$ with
$d < n$ and $\sigma_2(n) = n^2 + d^2 + 3n$, where $\sigma_2(n)$ is the sum of the squares of the
divisors of $n$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 13.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFPerfect_two_mul_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fperfect-two-mul-prime-pow).

## The only $(1,\ell)$-near-perfect number of the form $2p^a$ is $18$

For natural numbers
$\ell$ and $n$, say that $n$ is $[1,\ell]$-near-perfect when some divisor $d$ of $n$ with $d < n$
satisfies $\sigma(n) = n + d + \ell n$, where $\sigma(n)$ is the sum of the divisors of $n$. Then
$18$ is $[1,1]$-near-perfect, and for every odd prime $p$ and all natural numbers $a$ and
$\ell \ge 1$, if $2p^a$ is $[1,\ell]$-near-perfect then $2p^a = 18$.

The divisor for $18$ is $d = 3$. This is part 1 of Theorem 14 of the source.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 14.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.isKLNearPerfect_one_two_mul_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#is-klnear-perfect-one-two-mul-prime-pow).

## A divisibility condition for near-perfect numbers $2p^a$

Let $p$ be an odd prime, let
$a$, $k$, $\ell$ and $d$ be natural numbers with $k > 1$ and $\ell \ge 1$, and write
$\sigma_k(m) = \sum_{e \mid m} e^k$. If $d$ is a proper divisor of $2p^a$ ($d \mid 2p^a$ and
$d < 2p^a$) with $\sigma_k(2p^a) = (2p^a)^k + d^k + \ell \cdot 2p^a$, then $p^2 \mid 1 + 2^k$,
and $a$ is even if and only if $d$ is odd.

This is part 2 of Theorem 14 of the source.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 14.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.klNearPerfectWith_two_mul_prime_pow_imp` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#kl-near-perfect-with-two-mul-prime-pow-i).

## No near $F$-perfect number of the form $2^a p^b$ with $b$ even

For every prime $p$ and
all natural numbers $a$ and $b$ with $b$ even, the number $n = 2^a p^b$ is not near $F$-perfect:
there is no divisor $d$ of $n$ with $d < n$ and $\sigma_2(n) = n^2 + d^2 + 3n$, where
$\sigma_2(n)$ is the sum of the squares of the divisors of $n$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 15.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFPerfect_two_pow_mul_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fperfect-two-pow-mul-prime-p).

## No deficient $F_k$-perfect number $p_1^a p_2$ with distinct odd primes

Let $k > 1$ be
a natural number, let $p_1 \ne p_2$ be odd primes and let $a$ be a natural number. Then
$p_1^a p_2$ is not deficient $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 16.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isDeficientFkPerfect_prime_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-deficient-fk-perfect-prime-pow-mu).

## No near $F_k$-perfect number of the form $p_1^a p_2$

Let $k > 1$, let $p_1$ and $p_2$ be
distinct odd primes and let $a$ be a natural number. Then $p_1^a p_2$ is not near $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 17.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFkPerfect_prime_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fk-perfect-prime-pow-mul).

## No deficient $F_k$-perfect number of the form $2p^a$ for $k > 2$

Let $k > 2$, let $p$ be
an odd prime and let $a$ be a natural number. Then $2p^a$ is not deficient $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 18.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isDeficientFkPerfect_two_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-deficient-fk-perfect-two-mul-pow).

## No deficient $F_k$-perfect number $p_1^a p_2^b$ with $a + b$ odd or $a, b$ both odd

Let
$k > 1$ be a natural number, let $p_1 \ne p_2$ be odd primes and let $a, b \ge 1$ be natural
numbers such that $a + b$ is odd or both $a$ and $b$ are odd. Then $n = p_1^a p_2^b$ is not
deficient $F_k$-perfect: there is no divisor $d$ of $n$ with $d < n$ and
$\sigma_k(n) + d^k = n^k + 3n$, where $\sigma_k(n) = \sum_{e \mid n} e^k$.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 19.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isDeficientFkPerfect_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-deficient-fk-perfect-pow-mul-pow).

## No near $F_k$-perfect number $p_1^a p_2^b$ with $a + b$ odd or $a, b$ both odd

Let
$k > 1$, let $p_1 \ne p_2$ be odd primes and let $a, b \ge 1$ be natural numbers such that
$a + b$ is odd or both $a$ and $b$ are odd. Then $p_1^a p_2^b$ is not near $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 20.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFkPerfect_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fk-perfect-pow-mul-pow).

## No product of distinct odd primes is deficient $F_k$-perfect

Let $k > 1$ and let $s$ be a
finite set of odd primes. Then $\prod_{p \in s} p$ is not deficient $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 21.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isDeficientFkPerfect_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-deficient-fk-perfect-prod-primes).

## No product of distinct odd primes is near $F_k$-perfect

Let $k > 1$ and let $s$ be a
finite set of odd primes. Then $\prod_{p \in s} p$ is not near $F_k$-perfect.

## Sources

- Flora Jeba S, Anirban Roy, Pankaj Jyoti Mahanta, and Manjil P. Saikia, "On Near `F_k`-Perfect and Deficient `F_k`-Perfect Numbers", Theorem 22.

Stated but not proved: `MathlibExt.NumberTheory.FkPerfectWanted.not_isNearFkPerfect_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/FkPerfectWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FkPerfectWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-is-near-fk-perfect-prod-primes).

## $2$-near perfect numbers of the form $2^k p$

Let $k \ge 1$, let $p$ be a prime and let
$n = 2^k p$. Suppose $d_1 \ne d_2$ are divisors of $n$ with $\sigma(n) = 2n + d_1 + d_2$, where
$\sigma$ is the sum-of-divisors function (that is, $n$ is $2$-near perfect with omitted divisors
$d_1, d_2$). Then, after possibly swapping $d_1$ and $d_2$, one of the following holds, where
all equations are between integers: (1) $p = 2^k - 1$, $d_1 = 1$ and $d_2 = p$; (2) for some
natural numbers $a, b$, $p = 2^{k+1} - 2^a - 2^b - 1$, $d_1 = 2^a$ and $d_2 = 2^b$; (3) for some
natural numbers $a, b$, $p(1 + 2^b) = 2^{k+1} - 2^a - 1$, $d_1 = 2^a$ and $d_2 = 2^b p$; (4) for
some natural numbers $a, b$, $p(1 + 2^a + 2^b) = 2^{k+1} - 1$, $d_1 = 2^a p$ and $d_2 = 2^b p$.

The paper states only this necessary direction; the four situations are not sufficient as
printed ($k = 3$, $a = b = 1$ gives the prime $p = 11$ in situation 2, but $d_1 = d_2 = 2$).

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Theorem 1.

Stated but not proved: `MetaMathlibExt.two_near_perfect_two_pow_mul_prime_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#two-near-perfect-two-pow-mul-prime-cases).

## $2$-near perfect numbers of the form $2^k p^2$

Let $p$ be a prime, let $k$ be a natural
number and let $n = 2^k p^2$. If $n$ has divisors $d_1 \ne d_2$ with
$\sigma(n) = 2n + d_1 + d_2$, where $\sigma$ is the sum-of-divisors function (that is, $n$ is
$2$-near perfect with omitted divisors $d_1, d_2$), then $n$ is $18$, $36$ or $200$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Theorem 2.

Stated but not proved: `MetaMathlibExt.two_near_perfect_two_pow_mul_prime_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#two-near-perfect-two-pow-mul-prime-sq).

## Square values of the discriminant $2^{2k+2} + 2^{k+2} - 2^{a+2} - 7$

Let $a$ and $k$ be
natural numbers with $1 \le a \le k$. If $2^{2k+2} + 2^{k+2} - 2^{a+2} - 7$ is the square of an
integer, then $k = a = 1$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 2.

Stated but not proved: `MetaMathlibExt.eq_one_of_isSquare_discriminant` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#eq-one-of-is-square-discriminant).

## Divisibility constraints on odd solutions of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p + 1$

**Divisibility constraints on odd solutions of $(2^{k+1} - 1)(p^2 + p + 1) =
2^{k+1} p^2 + 2^b p + 1$.** Let $b$ and $k$ be natural numbers and let $p$ be an odd natural
number such that $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p + 1$. Then, as integers, $p$
divides $2^k - 1$ and $p + 1$ divides $2^b - 2$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 3.

Stated but not proved: `MetaMathlibExt.dvd_of_two_near_perfect_eq_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#dvd-of-two-near-perfect-eq-six).

## No odd solutions of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p + 1$ for $2 \le b \le k - 1$

**No odd solutions of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p + 1$ for
$2 \le b \le k - 1$.** Let $b$ and $k$ be natural numbers with $2 \le b$ and $b + 1 \le k$, and
let $p$ be an odd natural number. Then $(2^{k+1} - 1)(p^2 + p + 1) \ne 2^{k+1} p^2 + 2^b p + 1$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 4.

Stated but not proved: `MetaMathlibExt.not_two_near_perfect_eq_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-two-near-perfect-eq-seven).

## Sum and parity of the omitted divisors of a $2$-near perfect $2^k p^2$

Let $p$ be an odd
prime, let $k$ be a natural number, and let $d_1 \ne d_2$ be divisors of $n = 2^k p^2$ with
$\sigma(n) = 2n + d_1 + d_2$, where $\sigma$ denotes the sum of divisors. Then
$d_1 + d_2 = -p^2 + (2^{k+1} - 1) p + (2^{k+1} - 1)$, and $d_1$ and $d_2$ have opposite parity.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 5.

Stated but not proved: `MetaMathlibExt.omitted_divisors_sum_two_pow_mul_prime_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#omitted-divisors-sum-two-pow-mul-prime-s).

## Odd solutions $p$ of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$ divide $2^k - 1$

**Odd solutions $p$ of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$ divide
$2^k - 1$.** Let $k$ and $b$ be positive natural numbers and let $p$ be an odd natural number
such that $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$. Then $p$ divides $2^k - 1$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 6.

Stated but not proved: `MetaMathlibExt.dvd_of_two_near_perfect_eq_twelve` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#dvd-of-two-near-perfect-eq-twelve).

## Odd solutions $p$ of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$ satisfy $p + 1 \mid 2^b + 2$

**Odd solutions $p$ of $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$ satisfy
$p + 1 \mid 2^b + 2$.** Let $k$ and $b$ be positive natural numbers and let $p$ be an odd natural
number such that $(2^{k+1} - 1)(p^2 + p + 1) = 2^{k+1} p^2 + 2^b p^2 + 1$. Then, as integers,
$p + 1$ divides $2^b + 2$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 7.

Stated but not proved: `MetaMathlibExt.succ_dvd_of_two_near_perfect_eq_twelve` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#succ-dvd-of-two-near-perfect-eq-twelve).

## Strongly $2$-near perfect numbers of the form $2^k p$

Let $p$ be an odd prime, let $k$
be a natural number and let $n = 2^k p$. Suppose that $n$ is strongly $2$-near perfect, that is,
$\sigma(n) = 2n + d + n/d$ for some divisor $d$ of $n$, where $\sigma$ is the sum-of-divisors
function. Then there is a natural number $a \le k$ with $p(1 + 2^{k-a}) = 2^{k+1} - 2^a - 1$,
that is, $p = (2^{k+1} - 2^a - 1)/(1 + 2^{k-a})$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 8.

Stated but not proved: `MetaMathlibExt.strong_two_near_perfect_two_pow_mul_prime_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#strong-two-near-perfect-two-pow-mul-prim).

## Prime solutions of $p(1 + 2^{k-a}) = 2^{k+1} - 2^a - 1$ satisfy $k < 2a$

Let $a \le k$
be natural numbers and let $p$ be a prime with $p(1 + 2^{k-a}) = 2^{k+1} - 2^a - 1$, that is,
$p = (2^{k+1} - 2^a - 1)/(1 + 2^{k-a})$. Then $k < 2a$.

The source also assumes that $n = 2^k p$ is strongly $2$-near perfect, that is, that
$\sigma(n) = 2n + d + n/d$ for some divisor $d$ of $n$, where $\sigma$ is the sum of divisors.
This follows from the equation for $p$ by taking $d = 2^a$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 9.

Stated but not proved: `MetaMathlibExt.lt_two_mul_of_strong_two_near_perfect_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#lt-two-mul-of-strong-two-near-perfect-fo).

## If $b \ge 1$ and $2^b + 1$ divides $3 \cdot 2^a + 1$, then $b = 2$

Let $a$ and $b$ be
natural numbers with $b \ge 1$. If $2^b + 1$ divides $3 \cdot 2^a + 1$, then $b = 2$.

The source prints the lemma with no range for $b$; its proof divides $a$ by $b$, so $b \ge 1$ is
assumed here. The hypothesis is needed: for $b = 0$, $2^0 + 1 = 2$ divides $3 \cdot 2^0 + 1 = 4$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Lemma 10.

Stated but not proved: `MetaMathlibExt.eq_two_of_two_pow_add_one_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#eq-two-of-two-pow-add-one-dvd).

## $2$-near perfect $2^k p^2$ whose omitted divisors are powers of $2$

Let $p$ be an odd
prime, let $k$ be a natural number and let $i \ne j$ be natural numbers with $i \le k$ and
$j \le k$. If $n = 2^k p^2$ satisfies $\sigma(n) = 2n + 2^i + 2^j$, where $\sigma$ is the
sum-of-divisors function (that is, $n$ is $2$-near perfect with omitted divisors $2^i$ and
$2^j$), then $n = 18$ and either $i = 0, j = 1$ or $i = 1, j = 0$, so the omitted divisors are
$1$ and $2$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Proposition 1.

Stated but not proved: `MetaMathlibExt.two_near_perfect_two_pow_mul_prime_sq_case_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#two-near-perfect-two-pow-mul-prime-sq-ca).

## No $2$-near perfect $2^k p^2$ with omitted divisors $2^i$ and $p$ or $p^2$

Let $p$ be an
odd prime, let $k$ and $i$ be natural numbers with $i \le k$, let $m$ be $1$ or $2$, and let
$n = 2^k p^2$. Then $\sigma(n) \ne 2n + 2^i + p^m$, where $\sigma$ is the sum-of-divisors
function; that is, $n$ is not $2$-near perfect with omitted divisors $2^i$ and $p^m$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Proposition 2.

Stated but not proved: `MetaMathlibExt.not_two_near_perfect_two_pow_mul_prime_sq_case_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#not-two-near-perfect-two-pow-mul-prime-s).

## $2$-near perfect $2^k p^2$ with omitted divisors $1$ and $2^b p^2$

Let $p$ be an odd
prime and let $b, k$ be integers with $1 \le b \le k$. If $n = 2^k p^2$ satisfies
$\sigma(n) = 2n + 1 + 2^b p^2$, where $\sigma$ is the sum-of-divisors function (that is, $n$ is
$2$-near perfect with omitted divisors $1$ and $2^b p^2$), then $n = 36$ and $2^b p^2 = 18$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Proposition 3.

Stated but not proved: `MetaMathlibExt.two_near_perfect_two_pow_mul_prime_sq_case_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#two-near-perfect-two-pow-mul-prime-sq-ca-2).

## $2$-near perfect $2^k p^2$ with omitted divisors $p^m$ and $2^b p^j$

Let $p$ be an odd
prime, let each of $m$ and $j$ be $1$ or $2$, and let $b, k$ be integers with $1 \le b \le k$.
If $n = 2^k p^2$ satisfies $\sigma(n) = 2n + p^m + 2^b p^j$, where $\sigma$ is the
sum-of-divisors function (that is, $n$ is $2$-near perfect with omitted divisors $p^m$ and
$2^b p^j$), then $n = 200$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Proposition 4.

Stated but not proved: `MetaMathlibExt.two_near_perfect_two_pow_mul_prime_sq_case_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#two-near-perfect-two-pow-mul-prime-sq-ca-3).

## Classification of prime solutions of $p(1 + 2^{k-a}) = 2^{k+1} - 2^a - 1$

Let $a \le k$
be natural numbers and let $p$ be a prime with $p(1 + 2^{k-a}) = 2^{k+1} - 2^a - 1$, that is,
$p = (2^{k+1} - 2^a - 1)/(1 + 2^{k-a})$. Then $k = a + 2$, $2^k p / 2^a = 4p$,
$5p = 2^{a+3} - 2^a - 1$, and $a \equiv 3 \pmod 4$.

The source states this for $n = 2^k p$ strongly $2$-near perfect, that is, with
$\sigma(n) = 2n + d + n/d$ for some divisor $d$ of $n$, where $\sigma$ is the sum of divisors.
That hypothesis follows from the equation for $p$ by taking $d = 2^a$.

## Sources

- Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery and Joshua Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), Article A61, Proposition 5.

Stated but not proved: `MetaMathlibExt.strong_two_near_perfect_two_pow_mul_prime_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoNearPerfectWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoNearPerfectWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html#strong-two-near-perfect-two-pow-mul-prim-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Near-perfect and deficient-perfect numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/near-perfect-and-deficient-perfect-numbers)
