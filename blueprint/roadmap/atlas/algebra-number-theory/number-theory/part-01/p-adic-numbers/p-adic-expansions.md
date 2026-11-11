---
declaration: section
origin: cited
lean: PadicInt.padicDigit, PadicInt.padicDigit_lt, PadicInt.padicExpansion, PadicInt.padicExpansion_val, PadicInt.padicDigit_mul_pow, PadicInt.appr_succ_eq, PadicInt.appr_succ_eq_val, PadicInt.appr_eq_sum_padicDigit
statement: formalized
proof: formalized
---

# p-adic expansions

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html).

## Digits of a p-adic integer

Let $p$ be a prime and $a \in \mathbb{Z}_p$, and for each
$n \ge 0$ let $a_n$ be the unique natural number with $a_n < p^n$ and
$a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. The $n$-th $p$-adic digit of $a$ is the natural number
$(a_{n+1} - a_n)/p^n$.

Since $a_n \le a_{n+1}$ and $p^n$ divides $a_{n+1} - a_n$, this quotient is exact.

Formalized by `PadicInt.padicDigit`, a definition declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-digit).

## p-adic digits are less than p

Let $p$ be a prime and $a \in \mathbb{Z}_p$. For every
$n \ge 0$, the $n$-th $p$-adic digit of $a$ is strictly less than $p$.

Formalized by `PadicInt.padicDigit_lt`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-digit-lt).

## p-adic expansion

Let $p$ be a prime and $a \in \mathbb{Z}_p$. The $p$-adic expansion of
$a$ is the sequence whose $n$-th term is the $n$-th $p$-adic digit of $a$, viewed as an element of
$\{0, 1, \dots, p - 1\}$.

Formalized by `PadicInt.padicExpansion`, a definition declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-expansion).

## Terms of the p-adic expansion are the digits

Let $p$ be a prime and $a \in \mathbb{Z}_p$.
For every $n \ge 0$, the $n$-th term of the $p$-adic expansion of $a$, read as a natural number,
is the $n$-th $p$-adic digit of $a$.

Formalized by `PadicInt.padicExpansion_val`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-expansion-val).

## p-adic digits measure the gaps between approximations

Let $p$ be a prime and
$a \in \mathbb{Z}_p$, and for each $n \ge 0$ let $a_n$ be the unique natural number with
$a_n < p^n$ and $a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. For every $n \ge 0$, the $n$-th $p$-adic
digit $d_n$ of $a$ satisfies $d_n p^n = a_{n+1} - a_n$.

Here $a_n \le a_{n+1}$, so the difference is an honest natural number.

Formalized by `PadicInt.padicDigit_mul_pow`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-digit-mul-pow).

## One-step reconstruction from p-adic digits

Let $p$ be a prime and $a \in \mathbb{Z}_p$,
and for each $n \ge 0$ let $a_n$ be the unique natural number with $a_n < p^n$ and
$a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. For every $n \ge 0$, the $n$-th $p$-adic
digit $d_n$ of $a$ satisfies $a_{n+1} = a_n + d_n p^n$.

Formalized by `PadicInt.appr_succ_eq`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#appr-succ-eq).

## One-step reconstruction from the p-adic expansion

Let $p$ be a prime and
$a \in \mathbb{Z}_p$, and for each $n \ge 0$ let $a_n$ be the unique natural number with
$a_n < p^n$ and $a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. For every $n \ge 0$,
$a_{n+1} = a_n + e_n p^n$, where $e_n$ is the $n$-th term of the $p$-adic expansion of $a$, read as
a natural number.

Formalized by `PadicInt.appr_succ_eq_val`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#appr-succ-eq-val).

## Approximations as sums of p-adic digits

Let $p$ be a prime and $a \in \mathbb{Z}_p$, and
for each $n \ge 0$ let $a_n$ be the unique natural number with $a_n < p^n$ and
$a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. For every $n \ge 0$,
$a_n = \sum_{k=0}^{n-1} d_k p^k$, where $d_k$ is the $k$-th $p$-adic digit of $a$.

Formalized by `PadicInt.appr_eq_sum_padicDigit`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#appr-eq-sum-padic-digit).

## Approximations as truncations of the p-adic expansion

Let $p$ be a prime and
$a \in \mathbb{Z}_p$, and for each $n \ge 0$ let $a_n$ be the unique natural number with
$a_n < p^n$ and $a \equiv a_n \pmod{p^n \mathbb{Z}_p}$. For every $n \ge 0$,
$a_n = \sum_{k=0}^{n-1} e_k p^k$, where $e_k$ is the $k$-th term of the $p$-adic expansion of $a$,
read as a natural number.

Formalized by `PadicInt.appr_eq_sum_expansion_val`, a theorem declared in [MathlibExt/NumberTheory/Padics/Digits.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Digits.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#appr-eq-sum-expansion-val).

## $p$-adic digits determine a $p$-adic integer

Let $p$ be a prime. If two $p$-adic
integers $a, a' \in \mathbb{Z}_p$ have the same $n$-th $p$-adic digit for every $n \ge 0$, then
$a = a'$.

Formalized by `PadicInt.eq_of_padicDigit_eq`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#eq-of-padic-digit-eq).

## Existence of a $p$-adic integer with prescribed digits

Let $p$ be a prime. For every
sequence $(b_n)_{n \ge 0}$ of natural numbers with $b_n < p$ for all $n$, there is a $p$-adic
integer $a \in \mathbb{Z}_p$ whose $n$-th $p$-adic digit is $b_n$ for every $n \ge 0$.

The witness is the $p$-adic limit of the partial sums $\sum_{k=0}^{n-1} b_k p^k$, which are its
approximations modulo $p^n$.

Formalized by `PadicInt.exists_padicDigit_eq`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#exists-padic-digit-eq).

## Existence and uniqueness of $p$-adic integers with prescribed digits

Let $p$ be a prime.
For every sequence $(b_n)_{n \ge 0}$ of natural numbers with $b_n < p$ for all $n$, there is
exactly one $p$-adic integer $a \in \mathbb{Z}_p$ whose $n$-th $p$-adic digit is $b_n$ for every
$n \ge 0$.

## Sources

- ATLAS `NumberTheoryI`, Proposition 8.17.

Formalized by `PadicInt.existsUnique_padicDigit_eq`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#exists-unique-padic-digit-eq).

## The $p$-adic expansion map is injective

Let $p$ be a prime. If two $p$-adic integers
$a, a' \in \mathbb{Z}_p$ have the same $p$-adic expansion, then $a = a'$.

Formalized by `PadicInt.padicExpansion_injective`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-expansion-injective).

## The $p$-adic expansion map is surjective

Let $p$ be a prime. Every sequence
$(b_n)_{n \ge 0}$ with values in $\{0, 1, \dots, p - 1\}$ is the $p$-adic expansion of some
$p$-adic integer $a \in \mathbb{Z}_p$.

Formalized by `PadicInt.padicExpansion_surjective`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-expansion-surjective).

## The $p$-adic expansion map is bijective

Let $p$ be a prime. The map sending a $p$-adic
integer $a \in \mathbb{Z}_p$ to its $p$-adic expansion is a bijection from $\mathbb{Z}_p$ onto
the set of all sequences $(b_n)_{n \ge 0}$ with values in $\{0, 1, \dots, p - 1\}$.

## Sources

- ATLAS `NumberTheoryI`, Proposition 8.17.

Formalized by `PadicInt.padicExpansion_bijective`, a theorem declared in [MathlibExt/NumberTheory/Padics/Expansion.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/Expansion.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html#padic-expansion-bijective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: p-adic expansions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/p-adic-expansions)
