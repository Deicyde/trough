# Outline

The proof of the criterion has four parts, one per chapter.

Chapter [Class numbers of the cyclotomic CM field](../../class-numbers-of-the-cyclotomic-cm-field/README.md) proves that extension of ideals induces an *injective* map $\mathrm{Cl}(\mathcal O_{K^+}) \to \mathrm{Cl}(\mathcal O_K)$ ([Theorem class-group-map-injective](../../class-numbers-of-the-cyclotomic-cm-field/the-relative-class-number/thm-class-group-map-injective.md)). Consequently $h^+ \mid h$, and the relative class number $h^- = h/h^+$ is a genuine natural number with $h = h^+ h^-$.

Chapter [The minus class-number criterion](../../the-minus-class-number-criterion/README.md) establishes the analytic formula

$$
h^- = 2p \prod_{\chi \text{ odd}} \Bigl(-\tfrac12 B_{1,\chi^{-1}}\Bigr)
$$

([Theorem hminus-formula](../../the-minus-class-number-criterion/the-relative-class-number-formula/thm-hminus-formula.md)), then reduces it modulo $p$: indexing the odd characters by powers of the Teichmüller character and applying the congruence $B_{1,\omega^j} \equiv B_{j+1}/(j+1) \pmod p$ converts the product into a product of classical divided Bernoulli numbers, giving

$$
p \mid h^- \iff
\exists k,\ 1 \le k,\ 2k \le p-3,\ p \mid \operatorname{num}(B_{2k})
$$

([Theorem hminus-bernoulli-final](../../the-minus-class-number-criterion/from-h-to-bernoulli-numerators/thm-hminus-bernoulli-final.md)).

Chapter [Cyclotomic units and Kummer logarithms](../../cyclotomic-units-and-kummer-logarithms/README.md) treats the plus side. The real cyclotomic units form a subgroup $C^+$ of $(\mathcal O_{K^+})^\times$, and the determinant of the *Kummer logarithm matrix* — a matrix of $p$-adic logarithms of the cyclotomic-unit generators — factors as a product of Bernoulli numbers times a nonzero Vandermonde determinant ([Theorem kummer-log-det-bernoulli](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-bernoulli.md)). If no Bernoulli numerator in Kummer's range is divisible by $p$, the determinant is nonzero and $C^+$ is $p$-saturated in the full unit group, whence $p \nmid [(\mathcal O_{K^+})^\times : C^+]$ ([Theorem kummer-log-det-saturation](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-saturation.md) and [Theorem not-dvd-index-of-pSaturated](../../cyclotomic-units-and-kummer-logarithms/exact-p-saturation/thm-not-dvd-index-of-psaturated.md)). Sinnott's prime-conductor index theorem (sinnott1978) identifies the $p$-divisibility of this index with that of $h^+$ ([Theorem sinnott-index-pprimary](../../cyclotomic-units-and-kummer-logarithms/the-prime-conductor-index-theorem/thm-sinnott-index-pprimary.md)).

Chapter [Final assembly](../../final-assembly/README.md) assembles the criterion. The plus-side results yield the implication $p \mid h^+ \Rightarrow p \mid h^-$ ([Theorem hplus-to-hminus-units](../../final-assembly/the-implication-from-h-to-h/thm-hplus-to-hminus-units.md)); together with $h = h^+h^-$ this reduces $p \mid h$ to $p \mid h^-$, and the minus criterion finishes the proof ([Theorem kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md)).

Chapter [Infinitely many irregular primes](../../infinitely-many-irregular-primes/README.md) contains the application to the infinitude of irregular primes, following Carlitz (carlitz1954): a finite set $S$ of primes is escaped by manufacturing an even index $M$, divisible by $q - 1$ for every prime $q \in S$, with $|B_M/M| > 1$; any prime in the numerator of $B_M/M$ is then irregular and lies outside $S$. The key arithmetic input is the unrestricted Kummer congruence $B_m/m \equiv B_n/n \pmod p$ for even $m \equiv n \not\equiv 0 \pmod{p-1}$, proved by the elementary Voronoi route ([Theorem kummer-congruence-full](../../infinitely-many-irregular-primes/the-unrestricted-kummer-congruence/thm-kummer-congruence-full.md)).
