---
declaration: section
origin: cited
lean: MetaMathlibExt.oddPart, MetaMathlibExt.oddPart_eq, MetaMathlibExt.oddRangeProduct, MetaMathlibExt.oddRangeProduct_eq, MetaMathlibExt.oddProductBlock, MetaMathlibExt.oddProductBlock_eq, MetaMathlibExt.unstableBits, MetaMathlibExt.unstableBits_eq
statement: formalized
---

# 2-adic odd part of factorials of powers of two

45 results, 26 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html).

## Odd part

For a natural number $n \ge 1$, the odd part $\operatorname{od}(n)$ is
$n / 2^{\nu_2(n)}$, where $2^{\nu_2(n)}$ is the largest power of $2$ dividing $n$; it is the odd
factor of $n$ left after removing that power of $2$. For $n = 0$ the definition gives
$\operatorname{od}(0) = 0$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of od.

Formalized by `MetaMathlibExt.oddPart`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part).

## Odd part as a quotient by a power of two

For every natural number $n$,
$\mathrm{od}(n) = n / 2^{\nu_2(n)}$, where $\mathrm{od}(n)$ is the odd part of $n$ and
$\nu_2(n)$ is the exponent of $2$ in the prime factorization of $n$, with $\nu_2(0) = 0$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of od.

Formalized by `MetaMathlibExt.oddPart_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part-eq).

## Odd-range product

For natural numbers $l$ and $m$, the odd-range product
$\operatorname{odpr}(l, m)$ is the product of the odd natural numbers $j$ with $l \le j \le m$;
it equals $1$ when there are none.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of odpr.

Formalized by `MetaMathlibExt.oddRangeProduct`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-range-product).

## Odd-range product as a filtered product

For all natural numbers $l$ and $m$, the odd-range
product $\operatorname{odpr}(l, m)$ equals the product $\prod j$ over the odd natural numbers $j$ in
the closed interval $[l, m]$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of odpr.

Formalized by `MetaMathlibExt.oddRangeProduct_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-range-product-eq).

## Odd product block

For a natural number $m$, the odd product block $h(m)$ is the product of
the odd integers $j$ with $2^{m-1}+1 \le j \le 2^m-1$. In particular $h(0) = h(1) = 1$, as empty
products.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of h.

Formalized by `MetaMathlibExt.oddProductBlock`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-product-block).

## Odd product block as an odd-range product

For every natural number $m$, the odd product block
$h(m)$ equals $\operatorname{odpr}(2^{m-1}+1, 2^m-1)$, the product of the odd integers $j$ with
$2^{m-1}+1 \le j \le 2^m-1$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of h.

Formalized by `MetaMathlibExt.oddProductBlock_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-product-block-eq).

## Unstable bits

Write $\operatorname{od}(n)$ for the odd part of a natural number $n$. For
natural numbers $e$ and $d$, the unstable bits $\operatorname{uns}(e,d)$ are the natural number
$\lfloor \operatorname{od}((2^e)!) / 2^{e+1} \rfloor \bmod 2^d$, whose binary digits are the $d$
bits of $\operatorname{od}((2^e)!)$ at positions $e+1, \dots, e+d$ (position $0$ being the least
significant bit).

The paper assumes $e > d$ only when stating Theorem 1, so the definition itself is total.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of uns.

Formalized by `MetaMathlibExt.unstableBits`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#unstable-bits).

## Formula for the unstable bits

Write $\operatorname{od}(n)$ for the odd part of a natural
number $n$. For all natural numbers $e$ and $d$, the unstable bits are
$\operatorname{uns}(e,d) = \lfloor \operatorname{od}((2^e)!) / 2^{e+1} \rfloor \bmod 2^d$.

The binary digits of this number, least significant first, are the paper's first $d$ unstable
bits of $\operatorname{od}((2^e)!)$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of uns.

Formalized by `MetaMathlibExt.unstableBits_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#unstable-bits-eq).

## Stable bits of the odd part of a factorial

For natural numbers $s$ and $d$, let
$\operatorname{stab}(s, d)$ be the number whose binary digits are the digits of
$\operatorname{od}((2^{s+d-1})!)$ in positions $s, \dots, s + d - 1$ (position $0$ being the
units digit), where $\operatorname{od}(m)$ is the odd part of $m$ and $s + d - 1$ is truncated
subtraction. That is,

$$\operatorname{stab}(s, d) = \lfloor \operatorname{od}((2^{s+d-1})!) / 2^s \rfloor \bmod 2^d.$$

For $s = e + 1$ this is the source's $\operatorname{stab}(e + 1, d)$, the digits in positions
$e + 1, \dots, e + d$ of $\operatorname{od}((2^{e+d})!)$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of stab.

Formalized by `MetaMathlibExt.stableBits`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#stable-bits).

## Formula for the stable bits

Write $\operatorname{od}(n)$ for the odd part of a natural
number $n$. For all natural numbers $s$ and $d$, the stable bits are
$\operatorname{stab}(s, d) = \lfloor \operatorname{od}((2^{s+d-1})!) / 2^s \rfloor \bmod 2^d$,
where $s + d - 1$ is read as $0$ when $s = d = 0$.

For $s = e + 1$ the factorial is that of $2^{e+d}$, the shift is by $e + 1$ binary digits and the
modulus is $2^d$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of stab.

Formalized by `MetaMathlibExt.stableBits_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#stable-bits-eq).

## The unstable bits for $e = 4$ and $d = 2$

The unstable bits $\operatorname{uns}(4,2)$ equal
$3$; that is, $\lfloor \operatorname{od}(16!) / 2^5 \rfloor \bmod 2^2 = 3$, where
$\operatorname{od}(16!)$ is the odd part of $16!$.

This small case stands in for the paper's worked example $\operatorname{uns}(17,7) = 74$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Worked example after Theorem 1.

Formalized by `MetaMathlibExt.unstableBits_four_two`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#unstable-bits-four-two).

## The stable bits $\operatorname{stab}(5, 2)$ vanish

Writing $\operatorname{od}(m)$ for the odd
part of $m$, the binary digits of $\operatorname{od}(64!)$ in positions $5$ and $6$ (the units
digit being position $0$) are both $0$; that is,
$\operatorname{stab}(5, 2) = \lfloor \operatorname{od}(64!) / 2^5 \rfloor \bmod 4 = 0$.

This small instance checks the same factorial, shift and remainder convention as the source's
larger worked example $\operatorname{stab}(18, 7) = 55$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Worked example after Theorem 1.

Formalized by `MetaMathlibExt.stableBits_five_two`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#stable-bits-five-two).

## Dyadic upper half interval

For a natural number $e$, $I_e$ is the finite set of natural
numbers $i$ with $2^{e-1} < i \le 2^e$, where $e - 1$ is truncated subtraction, so that $I_0$ is
empty.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of I_e.

Formalized by `MetaMathlibExt.dyadicUpperHalf`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#dyadic-upper-half).

## Membership in the dyadic upper half

For natural numbers $e$ and $i$, $i$ belongs to the
dyadic upper half $I_e$ if and only if $2^{e-1} < i$ and $i \le 2^e$, where $e - 1$ is truncated
subtraction.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of I_e.

Formalized by `MetaMathlibExt.mem_dyadicUpperHalf`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#mem-dyadic-upper-half).

## Odd numbers below a power of two

For a natural number $e$, $S_e$ is the finite set of odd
natural numbers $i$ with $1 \le i < 2^e$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of S_e.

Formalized by `MetaMathlibExt.oddBelowTwoPow`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-below-two-pow).

## Membership in the odd numbers below $2^e$

For natural numbers $e$ and $i$, $i$ belongs to the
set $S_e$ of odd positive integers below $2^e$ if and only if $1 \le i$, $i < 2^e$ and $i$ is odd.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of S_e.

Formalized by `MetaMathlibExt.mem_oddSet`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#mem-odd-set).

## Integer multiset of a finite set of naturals

For a finite set $s$ of natural numbers, its
integer multiset is the multiset of integers obtained by sending each element $n \in s$ to $n$
viewed as an integer, so each element of $s$ occurs exactly once.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Convention for finite multisets.

Formalized by `MetaMathlibExt.integerMultiset`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#integer-multiset).

## Cardinality of the integer multiset

For every finite set $s$ of natural numbers, the integer
multiset of $s$ has the same number of elements, counted with multiplicity, as $s$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Convention for finite multisets.

Formalized by `MetaMathlibExt.integerMultiset_card`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#integer-multiset-card).

## Reversed elementary symmetric functions

Let $R$ be a commutative semiring, let $S$ be a
finite multiset of elements of $R$ with $n$ elements counted with multiplicity, and let $i$ be a
natural number. The reversed elementary symmetric function $\hat\sigma_i(S)$ is
$\sigma_{n-i}(S)$, the elementary symmetric function of degree $n - i$ in the elements of $S$.
Here $n - i$ is truncated subtraction, so $\hat\sigma_i(S) = \sigma_0(S) = 1$ whenever $i \ge n$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of σ̂_i.

Formalized by `MetaMathlibExt.reverseESymm`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#reverse-esymm).

## Unfolding the reversed elementary symmetric function

For every commutative semiring $R$,
natural number $i$ and finite multiset $S$ of elements of $R$ with $n$ elements counted with
multiplicity, the reversed elementary symmetric function satisfies
$\hat\sigma_i(S) = \sigma_{n-i}(S)$, the elementary symmetric function of $S$ of degree $n - i$,
where $n - i$ is truncated subtraction.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of σ̂_i.

Formalized by `MetaMathlibExt.reverseESymm_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#reverse-esymm-eq).

## Odd double factorial below a power of two

For a natural number $e$, $(2^e-1)!!$ is the
product of the odd natural numbers in the closed interval $[1, 2^e-1]$. The parameter is the
exponent $e$, not the odd endpoint $2^e-1$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of (2^e-1)!!.

Formalized by `MetaMathlibExt.oddDoubleFactorial`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-double-factorial).

## Odd double factorial below a power of two as an odd-range product

For every natural number
$e$, $(2^e-1)!!$ equals the product of the odd natural numbers in the closed interval
$[1, 2^e-1]$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition of (2^e-1)!!.

Formalized by `MetaMathlibExt.oddDoubleFactorial_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-double-factorial-eq).

## Numbers below $2^e$ congruent to $1$ modulo $8$

For a natural number $e$, this is the
finite set of natural numbers $n$ with $n < 2^e$ and $n \equiv 1 \pmod 8$.

For $e \ge 3$ its elements are $1, 9, \dots, 2^e - 7$, the sequence displayed in Lemma 21 of
the source.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 21 notation.

Formalized by `MetaMathlibExt.oneModEightBelowTwoPow`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#one-mod-eight-below-two-pow).

## Membership in the residues one modulo eight below a power of two

For all natural numbers $e$
and $n$, $n$ lies in the set of natural numbers below $2^e$ that are congruent to $1$ modulo $8$
if and only if $n < 2^e$ and $n \equiv 1 \pmod 8$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 21 notation.

Formalized by `MetaMathlibExt.mem_oneModEight`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#mem-one-mod-eight).

## Four copies of the residues $1 \bmod 8$ below $2^e$

For a natural number $e$, this is the
multiset of integers containing exactly four copies of each natural number $n < 2^e$ with
$n \equiv 1 \pmod 8$, that is, of each of $1, 9, \dots, 2^e - 7$ when $e \ge 3$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 21.

Formalized by `MetaMathlibExt.fourCopiesOneModEightBelowTwoPow`, a definition declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#four-copies-one-mod-eight-below-two-pow).

## Four copies as a multiset scalar multiple

For every natural number $e$, the multiset of four
copies of the residues $1 \bmod 8$ below $2^e$ equals $4 \cdot M$, the sum of four copies of $M$,
where $M$ is the integer multiset of the set of natural numbers $n < 2^e$ with $n \equiv 1 \pmod 8$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 21.

Formalized by `MetaMathlibExt.fourCopiesOneModEight_eq`, a theorem declared in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#four-copies-one-mod-eight-eq).

## A 2-adic constant relating unstable and stable bits

Write
$\mathrm{od}(n)$ for the odd part of a natural number $n$, and for natural numbers $d$ and $e$ let
$\mathrm{uns}(e, d) = \lfloor \mathrm{od}((2^e)!) / 2^{e+1} \rfloor \bmod 2^d$ and
$\mathrm{stab}(e + 1, d) = \lfloor \mathrm{od}((2^{e+d})!) / 2^{e+1} \rfloor \bmod 2^d$. There is a
2-adic integer $K$ such that for all natural numbers $d < e$, $2^d$ divides
$\mathrm{uns}(e, d) + K - \mathrm{stab}(e + 1, d)$ in $\mathbb{Z}_2$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_twoAdic_unstable_add_eq_stable` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#exists-two-adic-unstable-add-eq-stable).

## Odd part of a dyadic factorial as a product of odd blocks

For every natural number
$e \ge 1$,

$$\mathrm{od}((2^e)!) = \prod_{m=2}^{e} h(m)^{e+1-m},$$

where $\mathrm{od}(n)$ is the odd part of $n$ and $h(m)$ is the product of the odd numbers from
$2^{m-1}+1$ to $2^m-1$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Proposition 3.

Stated but not proved: `MetaMathlibExt.oddPart_factorial_eq_prod_h` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part-factorial-eq-prod-h).

## Initial-segment congruence for the odd product block

For natural numbers $l$ and $u$ write
$\operatorname{odpr}(l, u)$ for the product of the odd integers $j$ with $l \le j \le u$, and let
$h(m) = \operatorname{odpr}(2^{m-1}+1, 2^m-1)$. Let $m \ge 4$ and $B$ be natural numbers with
$m - 1 \le B \le 3m - 7$, and put $d = \lfloor (B + 4 - m)/2 \rfloor$, that is,
$d = 2 + \lfloor (B - m)/2 \rfloor$ (so $d = 1$ when $B = m - 1$). Then

$$
h(m) \equiv \operatorname{odpr}\bigl(2^{m-1}+1,\ 2^{m-1}+2^d-1\bigr)^{2^{m-1-d}} \pmod{2^B}.
$$

The paper prints the hypotheses $2 \le m - 1 \le B \le 3m - 7$, which also allow $(m, B) = (3, 2)$.
There $d = 1$, $h(3) = 35$ and the right-hand side is $5^2 = 25$, but $35 - 25 = 10$ is not
divisible by $4$. Requiring $m \ge 4$ removes exactly that case and keeps every other printed case.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Theorem 4.

Stated but not proved: `MetaMathlibExt.oddProductBlock_congr_initial_segment` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-product-block-congr-initial-segment).

## Odd parts biject the upper dyadic half onto the odd numbers below a power of two

For every natural number $e \ge 1$, the map sending each natural number to its odd part restricts
to a bijection from $I_e = \{i \in \mathbb{N} : 2^{e-1} < i \le 2^e\}$ onto the set $S_e$ of odd
natural numbers $i$ with $1 \le i < 2^e$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 5.

Stated but not proved: `MetaMathlibExt.oddPart_bijOn_upperHalf_oddSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part-bij-on-upper-half-odd-set).

## Product of the odd numbers below $2^e$

For every natural number $e \ge 3$, the product of the
odd integers $i$ with $1 \le i < 2^e$ is congruent to $2^e + 1$ modulo $2^{e+1}$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 6.

Stated but not proved: `MetaMathlibExt.oddSet_product_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-set-product-congr).

## Odd parts of consecutive dyadic factorials agree modulo a power of two

For every natural
number $e \ge 3$, $\mathrm{od}((2^{e-1})!) \equiv \mathrm{od}((2^e)!) \pmod{2^e}$, where
$\mathrm{od}(n)$ denotes the odd part of $n$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Corollary 7.

Stated but not proved: `MetaMathlibExt.oddPart_factorial_congr_previous` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part-factorial-congr-previous).

## A 2-adic limit of the odd parts of $(2^e)!$

There is a 2-adic integer $z \in \mathbb{Z}_2$
such that $z \equiv \operatorname{od}((2^{e-1})!) \pmod{2^e}$ in $\mathbb{Z}_2$ for every natural
number $e \ge 1$, where $\operatorname{od}(n)$ is the odd part of $n$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Corollary 8.

Stated but not proved: `MetaMathlibExt.exists_twoAdic_oddPart_factorial_limit` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#exists-two-adic-odd-part-factorial-limit).

## Shifting the odd numbers below $2^e$ by $2^e$

For every natural number $e \ge 2$, let $S_e$ be
the set of odd integers $i$ with $1 \le i < 2^e$. Then

$$
\prod_{i \in S_e} i \equiv \prod_{i \in S_e} (2^e + i) \pmod{2^{2e}}.
$$

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Proposition 9.

Stated but not proved: `MetaMathlibExt.oddSet_product_congr_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-set-product-congr-shift).

## Congruence of normalized odd double factorials

For every natural number $e \ge 3$, writing
$(2^k-1)!!$ for the product of the odd numbers from $1$ to $2^k-1$, the integer $2^e$ divides
$(2^e-1)!! - 1$, the integer $2^{e+1}$ divides $(2^{e+1}-1)!! - 1$, and

$$\frac{(2^e-1)!! - 1}{2^e} \equiv \frac{(2^{e+1}-1)!! - 1}{2^{e+1}} \pmod{2^{e-1}}.$$

The source states this for $e \ge 2$, but at $e = 2$ the first quotient is not an integer:
$(2^2-1)!! - 1 = 2$ is not divisible by $4$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Corollary 10.

Stated but not proved: `MetaMathlibExt.oddDoubleFactorial_normalized_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-double-factorial-normalized-congr).

## A 2-adic limit of normalized odd double factorials

Write $(2^e - 1)!!$ for the product of
the odd natural numbers from $1$ to $2^e - 1$. There is a 2-adic integer $w$ such that for every
natural number $e \ge 3$, $2^{e-1}$ divides $w - \lfloor ((2^e - 1)!! - 1) / 2^e \rfloor$ in
$\mathbb{Z}_2$.

For $e \ge 3$ the division is exact. The paper writes $e \ge 2$, but at $e = 2$ the quotient
$(3 - 1)/4$ is not an integer.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Definition after Corollary 10.

Stated but not proved: `MetaMathlibExt.exists_twoAdic_oddDoubleFactorial_limit` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#exists-two-adic-odd-double-factorial-lim).

## Normalized difference of odd parts of dyadic factorials

Write $\mathrm{od}(n)$ for the odd
part of $n$, $(2^e-1)!!$ for the product of the odd numbers from $1$ to $2^e-1$, and
$\lfloor x \rfloor$ for the floor of $x$; congruences are taken in the $2$-adic integers
$\mathbb{Z}_2$. Let $z, w \in \mathbb{Z}_2$ satisfy $z \equiv \mathrm{od}((2^{e-1})!) \pmod{2^e}$
for every $e \ge 1$ and $w \equiv \lfloor ((2^e-1)!! - 1)/2^e \rfloor \pmod{2^{e-1}}$ for every
$e \ge 3$. Then for every $e \ge 3$,

$$\lfloor (\mathrm{od}((2^e)!) - \mathrm{od}((2^{e-1})!))/2^e \rfloor \equiv zw \pmod{2^{e-1}}.$$

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Theorem 12.

Stated but not proved: `MetaMathlibExt.oddPart_factorial_difference_congr_product` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-part-factorial-difference-congr-prod).

## The unstable translation constant equals $-zw$

Write $\operatorname{od}(n)$ for the odd part
of a natural number $n$, $(2^e-1)!!$ for the product of the odd numbers from $1$ to $2^e-1$,
$\operatorname{uns}(e,d) = \lfloor \operatorname{od}((2^e)!)/2^{e+1} \rfloor \bmod 2^d$ and
$\operatorname{stab}(e+1,d) = \lfloor \operatorname{od}((2^{e+d})!)/2^{e+1} \rfloor \bmod 2^d$.
Let $K$, $z$ and $w$ be $2$-adic integers such that, with congruences in $\mathbb{Z}_2$,
$\operatorname{uns}(e,d) + K \equiv \operatorname{stab}(e+1,d) \pmod{2^d}$ for all natural
numbers $d < e$, $z \equiv \operatorname{od}((2^{e-1})!) \pmod{2^e}$ for all $e \ge 1$, and
$w \equiv \lfloor ((2^e-1)!! - 1)/2^e \rfloor \pmod{2^{e-1}}$ for all $e \ge 3$. Then $K = -zw$.

The three hypotheses are the defining properties of $K$ (Theorem 1), $z$ (Corollary 8) and $w$
(the definition after Corollary 10).

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Theorem 14.

Stated but not proved: `MetaMathlibExt.unstable_translation_eq_neg_product` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#unstable-translation-eq-neg-product).

## Shifting the odd numbers below $2^e$ by a multiple of $2^e$

For every integer $A$ and every
natural number $e \ge 2$, let $S_e$ be the set of odd integers $i$ with $1 \le i < 2^e$. Then

$$
\prod_{i \in S_e} (A \cdot 2^e + i) \equiv \prod_{i \in S_e} i \pmod{2^{3e-1}}.
$$

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Theorem 16.

Stated but not proved: `MetaMathlibExt.oddSet_product_linear_shift_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-set-product-linear-shift-congr).

## Powers of shifted products over the odd numbers below $2^e$

For all integers $A$ and $B$ and
all natural numbers $j$ and $e$ with $e \ge 2$, let $S_e$ be the set of odd integers $i$ with
$1 \le i < 2^e$. Then

$$
\prod_{i \in S_e} (A \cdot 2^e + i)^{2^j} \equiv \prod_{i \in S_e} (B \cdot 2^e + i)^{2^j}
\pmod{2^{3e-1+j}}.
$$

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Corollary 17.

Stated but not proved: `MetaMathlibExt.oddSet_product_power_shift_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#odd-set-product-power-shift-congr).

## $\hat\sigma_1$ of the odd numbers below $2^e$

Let $e \ge 2$ and let $S_e$ be the set of odd
natural numbers $i$ with $1 \le i < 2^e$, regarded as a multiset of integers with $n$ elements,
and write $\sigma_k$ for the elementary symmetric function of degree $k$. Then the reversed
elementary symmetric function $\hat\sigma_1(S_e) = \sigma_{n-1}(S_e)$ satisfies
$\hat\sigma_1(S_e) \equiv 2^{2e-2} \pmod{2^{2e-1}}$ in $\mathbb{Z}$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 18.

Stated but not proved: `MetaMathlibExt.reverseESymm_one_oddSet_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#reverse-esymm-one-odd-set-congr).

## $\hat\sigma_2$ of the odd numbers below $2^e$

Let $e \ge 2$ and let $S_e$ be the set of odd
natural numbers $i$ with $1 \le i < 2^e$, regarded as a multiset of integers with $n$ elements,
and write $\sigma_k$ for the elementary symmetric function of degree $k$. Then the reversed
elementary symmetric function $\hat\sigma_2(S_e) = \sigma_{n-2}(S_e)$ satisfies
$\hat\sigma_2(S_e) \equiv 2^{e-2} \pmod{2^{e-1}}$ in $\mathbb{Z}$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 19.

Stated but not proved: `MetaMathlibExt.reverseESymm_two_oddSet_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#reverse-esymm-two-odd-set-congr).

## Each residue $1 \bmod 8$ has four odd square roots modulo $2^e$

Let $e \ge 3$ and let $S_e$
be the set of odd natural numbers $i$ with $1 \le i < 2^e$. For every natural number $v < 2^e$
with $v \equiv 1 \pmod 8$, exactly four elements $i \in S_e$ satisfy $i^2 \bmod 2^e = v$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 20.

Stated but not proved: `MetaMathlibExt.square_mod_twoPower_fiber_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#square-mod-two-power-fiber-card).

## $\hat\sigma_1$ of four copies of the numbers $1 \bmod 8$ below $2^e$

Let $e \ge 3$ and let
$M_e$ be the multiset of integers containing each natural number $n < 2^e$ with
$n \equiv 1 \pmod 8$ (that is, $1, 9, \dots, 2^e - 7$) exactly four times, let $N$ be the
number of elements of $M_e$ counted with multiplicity, and write $\sigma_k$ for the elementary
symmetric function of degree $k$. Then the reversed elementary symmetric function
$\hat\sigma_1(M_e) = \sigma_{N-1}(M_e)$ satisfies $\hat\sigma_1(M_e) \equiv 2^{e-1} \pmod{2^e}$
in $\mathbb{Z}$.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Lemma 21.

Stated but not proved: `MetaMathlibExt.reverseESymm_fourCopies_oneModEight_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#reverse-esymm-four-copies-one-mod-eight).

## Squared products of the odd residues omitting one factor

Let $e \ge 1$ and let
$S_e$ be the set of odd positive integers below $2^e$. Then, as integers,

$$\sum_{i \in S_e} \Bigl(\prod_{j \in S_e \setminus \{i\}} j\Bigr)^2 \equiv 2^{e-1} \pmod{2^e}.$$

Each squared product equals the paper's $((2^e-1)!!)^2/i^2$; the product form avoids an exact
division for every summand.

## Sources

- Donald M. Davis, *Some 2-adic Integers Related to the Odd Part of 2^e!*, Journal of Integer Sequences 29 (2026), Article 26.3.1, Proposition 22.

Stated but not proved: `MetaMathlibExt.sum_square_erased_oddSet_product_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddPartFactorialTwoAdicWanted.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html#sum-square-erased-odd-set-product-congr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-adic odd part of factorials of powers of two](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/p-adic-numbers/2-adic-odd-part-of-factorials-of-powers-of-two)
