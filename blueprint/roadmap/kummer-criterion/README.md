# Kummer's criterion

The blueprint of Kummer's criterion, read at commit [b96b2cde](https://github.com/riccardobrasca/KummerCriterion/tree/b96b2cde81e799bfe8364b6dd469abafd9a26bdf) (2026-11-03): one article for each of its 93 nodes whose Lean declarations it names and marks formalized, or in Mathlib. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

This document gives a proof of **Kummer's criterion**:

$$
p \text{ is regular}
\quad\Longleftrightarrow\quad
\forall k,\ 1 \le k,\ 2k \le p - 3,\quad
p \nmid \operatorname{num}(B_{2k})
$$

for every odd prime $p$.

The proof has four steps. First, for a prime cyclotomic CM field $K$ and its maximal real subfield $K^+$, extension of ideals gives an injective class-group map

$$
\mathrm{Cl}(\mathcal O_{K^+}) \longrightarrow \mathrm{Cl}(\mathcal O_K).
$$

This proves $h^+ \mid h$ and allows the relative class number

$$
h^- := h/h^+
$$

to be used as an actual natural number.

Second, the relative class-number formula is reduced to a $p$-adic congruence and then to the Bernoulli numerator criterion:

$$
p \mid h^- \quad\Longleftrightarrow\quad
\exists k,\ 1 \le k,\ 2k \le p-3,\quad
p \mid \operatorname{num}(B_{2k}).
$$

Third, the real cyclotomic units form a subgroup $C^+$ of the full unit group of $K^+$. The Kummer logarithm matrix proves that Bernoulli numerator non-divisibility forces $C^+$ to be $p$-saturated, hence

$$
p \nmid [\mathcal O_{K^+}^{\times}:C^+].
$$

The prime-conductor cyclotomic-unit index theorem identifies the odd-primary part of this index with $h^+$.

Finally, these ingredients show that $p \mid h$ is equivalent to divisibility of one Bernoulli numerator in Kummer's range. The definition of regular prime then gives the stated criterion.

The Lean declaration corresponding to the final theorem is `KummerCriterion`.

As an application of the criterion, a final chapter proves Carlitz's theorem that there are infinitely many irregular primes, via the unrestricted Kummer congruence for divided Bernoulli numbers.

2

- [Introduction](introduction/README.md)
- [Class numbers of the cyclotomic CM field](class-numbers-of-the-cyclotomic-cm-field/README.md)
- [The minus class-number criterion](the-minus-class-number-criterion/README.md)
- [Cyclotomic units and Kummer logarithms](cyclotomic-units-and-kummer-logarithms/README.md)
- [Final assembly](final-assembly/README.md)
- [Infinitely many irregular primes](infinitely-many-irregular-primes/README.md)
