---
declaration: section
origin: cited
lean: MetaMathlibExt.IsFortunateNumber, MathlibExt.NumberTheory.PrimeCounting.GandhiNthPrimeFormulaWanted.gandhi_nthPrimeFormula, MetaMathlibExt.generalizedFermatNumber
statement: formalized
proof: formalized
---

# Special classes of primes: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/index.html).

Fermat, Mersenne, Sophie Germain, Wieferich, Cullen and other named prime families, Fermat numbers, Sierpiński–Riesel numbers, prime-producing formulas.

## Fortunate numbers

Write $q\#$ for the primorial of a natural number $q$, the product of
all primes $p \le q$. For natural numbers $q$ and $m$, $m$ is the Fortunate number of $q$ when
$q$ is prime, $m > 1$, $q\# + m$ is prime, and $q\# + k$ is not prime for any $k$ with
$1 < k < m$.

## Sources

- Antonín Čejchan, Michal Křížek, and Lawrence Somer, *On Remarkable Properties of Primes Near Factorials and Primorials*, Journal of Integer Sequences 25 (2022), Article 22.1.4.

Formalized by `MetaMathlibExt.IsFortunateNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FortunateNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FortunateNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/index.html#is-fortunate-number).

## Gandhi's formula for the $n$th prime

For $i \ge 1$ let $p_i$ be the $i$th prime, so that
$p_1 = 2$, and for $n \ge 1$ let $P_{n-1} = p_1 p_2 \cdots p_{n-1}$, the empty product $1$ when
$n = 1$. Let $\mu$ be the Möbius function. Then for every $n \ge 1$,

$$p_n = \left\lfloor 1 - \log_2 \left( -\frac{1}{2} + \sum_{d \mid P_{n-1}} \frac{\mu(d)}{2^d - 1}
\right) \right\rfloor.$$

## Sources

- J. M. Gandhi, "Formulae for the nth prime," Proc. Washington State University Conference on Number Theory (1971), 96--107. The displayed formula and indexing follow the secondary source Eric S. Rowland, "A Natural Prime-Generating Recurrence," Journal of Integer Sequences 11 (2008), Article 08.2.8, lines 90--103 of the official TeX, https://cs.uwaterloo.ca/journals/JIS/VOL11/Rowland/rowland21.tex, where `f(n)` is the `n`th prime `pₙ` and `Pₙ = p₁ p₂ ⋯ pₙ`.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.GandhiNthPrimeFormulaWanted.gandhi_nthPrimeFormula`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/GandhiNthPrimeFormula.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/GandhiNthPrimeFormula.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/index.html#gandhi-nth-prime-formula).

## Generalized Fermat number

For an even natural number $b$ and a positive integer $n$,
the generalized Fermat number is $F_n(b) = b^{2^n} + 1$ (also written $F_{b,n}$).

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL15/Castillo/castillo2.tex> and <https://cs.uwaterloo.ca/journals/JIS/VOL24/Witno/witno8.tex>.

Formalized by `MetaMathlibExt.generalizedFermatNumber`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFermatNumber.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFermatNumber.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/index.html#generalized-fermat-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Special classes of primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/special-primes)
