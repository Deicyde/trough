---
declaration: section
origin: cited
lean: IsCyclotomicExtension.Rat.isField_quotient_span_natCast_iff_orderOf_eq, IsCyclotomicExtension.Rat.isUnramifiedIn_of_not_dvd, IsCyclotomicExtension.Rat.isUnramifiedIn_divMaxPow, IsCyclotomicExtension.Rat.eq_bot_of_isUnramifiedIn_prime_pow
statement: formalized
proof: formalized
---

# Ramification and inertia in cyclotomic fields

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html).

## Inert primes in prime cyclotomic fields

Let $\ell$ and $p$ be distinct prime numbers,
and let $K$ be a number field that is an $\ell$-th cyclotomic extension of $\mathbb{Q}$, with
ring of integers $\mathcal{O}_K$. Then the quotient ring $\mathcal{O}_K / p\mathcal{O}_K$ is a
field (that is, $p$ is inert in $K$) if and only if the multiplicative order of $p$ modulo
$\ell$ is $\ell - 1$.

Formalized by `IsCyclotomicExtension.Rat.isField_quotient_span_natCast_iff_orderOf_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Cyclotomic/InertPrime.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Cyclotomic/InertPrime.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html#is-field-quotient-span-nat-cast-iff-orde).

## Cyclotomic fields are unramified at primes not dividing $m$

Let $m \ge 1$ and let $p$ be
a prime number with $p \nmid m$. If $K$ is a number field that is an $m$-th cyclotomic extension
of $\mathbb{Q}$ (that is, $K = \mathbb{Q}(\zeta_m)$ for a primitive $m$-th root of unity
$\zeta_m$), then $p$ is unramified in $K$: every prime ideal of the ring of integers
$\mathcal{O}_K$ lying over $p\mathbb{Z}$ is unramified over $\mathbb{Z}$.

Formalized by `IsCyclotomicExtension.Rat.isUnramifiedIn_of_not_dvd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html#is-unramified-in-of-not-dvd).

## The $p$-free part of $m$ gives a cyclotomic field unramified at $p$

Let $m \ge 1$, let
$p$ be a prime number, and let $m'$ be $m$ divided by the largest power of $p$ dividing it, so
that $m = p^a m'$ for some $a \ge 0$ with $p \nmid m'$. Then $p$ is unramified in the $m'$-th
cyclotomic field $\mathbb{Q}(\zeta_{m'})$, where $\zeta_{m'}$ is a primitive $m'$-th root of
unity: every prime ideal of its ring of integers lying over $p\mathbb{Z}$ is unramified over
$\mathbb{Z}$.

Formalized by `IsCyclotomicExtension.Rat.isUnramifiedIn_divMaxPow`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html#is-unramified-in-div-max-pow).

## Subfields of a $p$-power cyclotomic field unramified at $p$ are trivial

Let $p$ be a
prime number, $e \ge 0$ an integer and $L$ a number field. Let $E_1$ and $F$ be subfields of $L$
such that $E_1$ is a $p^e$-th cyclotomic extension of $\mathbb{Q}$ and $F \subseteq E_1$. If $p$
is unramified in $F$, that is, every prime ideal of the ring of integers $\mathcal{O}_F$ lying
over $p\mathbb{Z}$ is unramified over $\mathbb{Z}$, then $F = \mathbb{Q}$.

## Sources

- the prime-power vanishing step of the N390 maximality argument (`cyclotomic_ppow_unramified_le_bot` in the primary source), which takes $e$ to be the exponent of $p$ in a positive integer $m$ and $L = \mathbb{Q}(\zeta_m)$ for a primitive $m$-th root of unity $\zeta_m$; here $e$ and $L$ are arbitrary.

Formalized by `IsCyclotomicExtension.Rat.eq_bot_of_isUnramifiedIn_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Cyclotomic/Unramified.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html#eq-bot-of-is-unramified-in-prime-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramification and inertia in cyclotomic fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/ramification-and-inertia-in-cyclotomic-fields)
