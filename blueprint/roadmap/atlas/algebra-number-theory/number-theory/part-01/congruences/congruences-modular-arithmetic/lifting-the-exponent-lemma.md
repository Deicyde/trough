---
declaration: section
origin: cited
lean: MetaMathlibExt.padicValInt_pow_sub_pow, MetaMathlibExt.pow_pow_modEq_one_of_modEq_one, MetaMathlibExt.prime_power_lifting_modEq_one
statement: formalized
proof: formalized
---

# Lifting the exponent lemma

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma/index.html).

## Lifting the exponent for odd primes

Let $p$ be an odd prime, let $a \ne b$ be integers
such that $p$ divides $a - b$ but does not divide $ab$, and let $n \ge 1$ be a natural number.
Then

$$v_p(a^n - b^n) = v_p(n) + v_p(a - b),$$

where $v_p$ denotes the $p$-adic valuation.

Formalized by `MetaMathlibExt.padicValInt_pow_sub_pow`, a theorem declared in [MathlibExt/NumberTheory/ClassicalLte.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ClassicalLte.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma/index.html#padic-val-int-pow-sub-pow).

## Lifting a congruence to one along powers of the modulus

Let $p$, $n$ and $a$ be natural
numbers. If $a \equiv 1 \pmod p$, then $a^{p^n} \equiv 1 \pmod{p^{n+1}}$.

The modulus $p$ need not be prime.

Formalized by `MetaMathlibExt.pow_pow_modEq_one_of_modEq_one`, a theorem declared in [MathlibExt/NumberTheory/PrimePowerLifting.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimePowerLifting.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma/index.html#pow-pow-mod-eq-one-of-mod-eq-one).

## Prime-power lifting of a congruence to one

Let $p$ be a prime and let $n$ and $a$ be
positive integers. If $a \equiv 1 \pmod p$, then $a^{p^n} \equiv 1 \pmod{p^{n+1}}$.

## Sources

- Hacène Belbachir and Celia Salhi, "The Generalized Bi-Periodic Fibonacci Sequence Modulo m," Journal of Integer Sequences 24 (2021), Article 21.9.4, Theorem, lines 340–341, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Salhi/salhi4.tex>. It follows from `pow_pow_modEq_one_of_modEq_one`; the hypotheses `hp`, `hn` and `ha` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.prime_power_lifting_modEq_one`, a theorem declared in [MathlibExt/NumberTheory/PrimePowerLifting.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimePowerLifting.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma/index.html#prime-power-lifting-mod-eq-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lifting the exponent lemma](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/lifting-the-exponent-lemma)
