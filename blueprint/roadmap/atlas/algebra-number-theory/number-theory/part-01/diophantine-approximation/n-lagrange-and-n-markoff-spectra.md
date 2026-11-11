---
declaration: section
origin: cited
lean: MetaMathlibExt.nLagrangeApproximability, MetaMathlibExt.nLagrangeApproximability_one, MetaMathlibExt.nMarkoffApproximability, MetaMathlibExt.nMarkoffApproximability_comm, MetaMathlibExt.nLagrangeSpectrum, MetaMathlibExt.mem_nLagrangeSpectrum, MetaMathlibExt.nMarkoffSpectrum, MetaMathlibExt.mem_nMarkoffSpectrum
statement: formalized
---

# n-Lagrange and n-Markoff spectra

24 results, 8 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html).

## $n$-Lagrange approximability

For a natural number $n$ and a real number $\xi$, the
$n$-Lagrange approximability of $\xi$ is the element of the extended reals

$$\lambda_n(\xi) = \limsup_{s/t \to \xi} \frac{\gcd(t, n)}{t^2 \, |s/t - \xi|},$$

where the limsup is over rational numbers $s/t \ne \xi$, written in lowest terms with $t > 0$,
tending to $\xi$. For $n = 1$ this is the classical Lagrange approximability $\lambda(\xi)$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (3).

Formalized by `MetaMathlibExt.nLagrangeApproximability`, a definition declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-lagrange-approximability).

## The $1$-Lagrange approximability is the classical one

For every real number $\xi$, the
$1$-Lagrange approximability of $\xi$ is

$$\lambda_1(\xi) = \limsup_{s/t \to \xi} \frac{1}{t^2 \, |s/t - \xi|},$$

taken in the extended reals, where the limsup is over rational numbers $s/t \ne \xi$, written in
lowest terms with $t > 0$, tending to $\xi$. That is, the factor $\gcd(t, 1)$ in the definition
equals $1$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equations (1) and (3).

Formalized by `MetaMathlibExt.nLagrangeApproximability_one`, a theorem declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-lagrange-approximability-one).

## $n$-Markoff approximability

For a natural number $n$ and real numbers $\xi$ and $\xi'$, the
$n$-Markoff approximability is the supremum in the extended reals

$$\mu_n(\xi, \xi') = \sup_{(s,t) \ne 0} \frac{\gcd(t, n)\,|\xi - \xi'|}{|s - t\xi|\,|s - t\xi'|}$$

over all pairs of integers $(s, t) \ne (0, 0)$. A term whose denominator is $0$, which happens only
when $\xi$ or $\xi'$ is rational, counts as $0$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (4).

Formalized by `MetaMathlibExt.nMarkoffApproximability`, a definition declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-markoff-approximability).

## Symmetry of the $n$-Markoff approximability

For every natural number $n$ and all real
numbers $\xi$ and $\xi'$, the $n$-Markoff approximability satisfies
$\mu_n(\xi, \xi') = \mu_n(\xi', \xi)$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (4).

Formalized by `MetaMathlibExt.nMarkoffApproximability_comm`, a theorem declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-markoff-approximability-comm).

## $n$-Lagrange spectrum

For a natural number $n$, the $n$-Lagrange spectrum $L_n$ is the set
of real numbers $\alpha$ such that $\lambda_n(\xi) = \alpha$ for some irrational real number
$\xi$, where $\lambda_n$ is the $n$-Lagrange approximability; only finite values of $\lambda_n$
count. For $n = 1$ this is the classical Lagrange spectrum $L$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (3).

Formalized by `MetaMathlibExt.nLagrangeSpectrum`, a definition declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-lagrange-spectrum).

## Membership in the $n$-Lagrange spectrum

For every natural number $n$ and real number
$\alpha$, $\alpha$ lies in the $n$-Lagrange spectrum $L_n$ if and only if $\alpha = \lambda_n(\xi)$
for some irrational real number $\xi$, where $\lambda_n$ is the $n$-Lagrange approximability.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (3).

Formalized by `MetaMathlibExt.mem_nLagrangeSpectrum`, a theorem declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#mem-n-lagrange-spectrum).

## The $n$-Markoff spectrum

For a natural number $n$ and irrational numbers $\xi \ne \xi'$,
the $n$-Markoff approximability $\mu_n(\xi, \xi')$ is the extended real number
$\sup_{(s, t) \in \mathbb{Z}^2 \setminus \{0\}}
\gcd(t, n) \, |\xi - \xi'| / (|s - t\xi| \, |s - t\xi'|)$. The $n$-Markoff spectrum $M_n$ is the
set of real numbers $\alpha$ such that $\mu_n(\xi, \xi') = \alpha$ for some irrational numbers
$\xi \ne \xi'$. For $n = 1$ this is the classical Markoff spectrum $M$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (4).

Formalized by `MetaMathlibExt.nMarkoffSpectrum`, a definition declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-markoff-spectrum).

## Membership in the $n$-Markoff spectrum

For every natural number $n$ and real number
$\alpha$, $\alpha$ lies in the $n$-Markoff spectrum $M_n$ if and only if $\alpha = \mu_n(\xi, \xi')$
for some distinct irrational real numbers $\xi$ and $\xi'$, where $\mu_n$ is the $n$-Markoff
approximability.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Introduction, equation (4).

Formalized by `MetaMathlibExt.mem_nMarkoffSpectrum`, a theorem declared in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#mem-n-markoff-spectrum).

## Convergents and the Lagrange approximability

Let $\xi$ be an irrational real number,
with complete quotients $\xi_0 = \xi$ and $\xi_{k+1} = 1/\{\xi_k\}$, where $\{x\}$ is the
fractional part of $x$, and digits $a_k = \lfloor \xi_k \rfloor$, so that
$\xi = [a_0; a_1, a_2, \dots]$. For $k \ge 1$ let
$c_k = a_k + [0; a_{k-1}, \dots, a_1] + \{\xi_k\}$, where the middle term is $0$ when $k = 1$.
Then for every $k \ge 1$ the convergent $p/q = [a_0; a_1, \dots, a_{k-1}]$, written in lowest terms
with $q > 0$, satisfies $(-1)^k / (q^2 (p/q - \xi)) = c_k$. Moreover, the $1$-Lagrange
approximability $\lambda_1(\xi)$ equals $\limsup_{k \to \infty} c_k$, taken in the extended reals.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 4, parts (a) and (c), quoted from Cusick and Flahive, Appendix 1.

Stated but not proved: `MetaMathlibExt.convergent_quality_and_lagrange_limsup` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#convergent-quality-and-lagrange-limsup).

## Real numbers with a common continued fraction prefix are close

Let $\xi$ and $\xi'$ be
real numbers with continued fraction expansions $[a_0; a_1, a_2, \dots]$ and
$[a_0'; a_1', a_2', \dots]$, computed by $\xi_0 = \xi$, $a_i = \lfloor \xi_i \rfloor$ and
$\xi_{i+1} = 1/(\xi_i - a_i)$, stopping when $\xi_i = a_i$ (so an expansion is finite exactly when
the number is rational). Let $k \ge 0$ be an integer, and suppose that $a_0 = a_0'$ and that for
each $1 \le i \le k$ either both expansions have a digit of index $i$ and $a_i = a_i'$, or neither
has one. Then $|\xi - \xi'| \le 2^{1-k}$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Lemma 5, quoted from Cusick and Flahive, Lemma 1.

Stated but not proved: `MetaMathlibExt.abs_sub_le_of_contFrac_prefix_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#abs-sub-le-of-cont-frac-prefix-eq).

## The $n$-approximabilities as maxima over divisors

Let $n \ge 1$, let $\lambda_n$ and
$\mu_n$ be the $n$-Lagrange and $n$-Markoff approximabilities, and let $\xi \ne \xi'$ be irrational
real numbers. Then $\lambda_n(\xi) = \max_{g \mid n} \lambda_1(g\xi)$ and
$\mu_n(\xi, \xi') = \max_{g \mid n} \mu_1(g\xi, g\xi')$, where $g$ runs over the positive divisors
of $n$ and the maxima are taken in the extended reals.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 6.

Stated but not proved: `MetaMathlibExt.nApproximability_eq_sup_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-approximability-eq-sup-divisors).

## Divisibility inclusions of the $n$-Lagrange and $n$-Markoff spectra

Let $m$ and $n$
be natural numbers with $m \ge 1$, $n \ge 1$ and $m \mid n$, and write $L_k$ and $M_k$ for the
$k$-Lagrange and $k$-Markoff spectra. Then $L_n \subseteq L_m$ and $M_n \subseteq M_m$; in
particular $L_n \subseteq L_1$ and $M_n \subseteq M_1$, where $L_1$ and $M_1$ are the
classical Lagrange and Markoff spectra.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Corollary 7, equations (8) and (9).

Stated but not proved: `MetaMathlibExt.nSpectrum_subset_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-spectrum-subset-of-dvd).

## The $n$-Lagrange spectrum lies in the $n$-Markoff spectrum, with attained suprema

Let
$n \ge 1$, let $L_n$ and $M_n$ be the $n$-Lagrange and $n$-Markoff spectra, and let $\mu_n$ be the
$n$-Markoff approximability. Then $L_n \subseteq M_n$. Moreover, for every $\alpha \in L_n$ there
are distinct irrational real numbers $\xi$ and $\xi'$ with $\mu_n(\xi, \xi') = \alpha$ at which the
supremum defining $\mu_n(\xi, \xi')$ is attained: some pair of integers $(s, t) \ne (0, 0)$
satisfies

$$\frac{\gcd(t, n)\,|\xi - \xi'|}{|s - t\xi|\,|s - t\xi'|} = \alpha.$$

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 9.

Stated but not proved: `MetaMathlibExt.nLagrangeSpectrum_subset_nMarkoffSpectrum_attained` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-lagrange-spectrum-subset-n-markoff-spe).

## Attained suprema in the $n$-Markoff spectrum

Let $n \ge 1$, let $M_n$ be the $n$-Markoff
spectrum, and let $\mu_n$ be the $n$-Markoff approximability. For every $\alpha \in M_n$ there are
distinct irrational real numbers $\xi$ and $\xi'$ with $\mu_n(\xi, \xi') = \alpha$ at which the
supremum defining $\mu_n(\xi, \xi')$ is attained: some pair of integers $(s, t) \ne (0, 0)$
satisfies

$$\frac{\gcd(t, n)\,|\xi - \xi'|}{|s - t\xi|\,|s - t\xi'|} = \alpha.$$

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 10.

Stated but not proved: `MetaMathlibExt.nMarkoffSpectrum_attained` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-markoff-spectrum-attained).

## The $n$-Markoff spectrum is closed

For every integer $n \ge 1$, the $n$-Markoff spectrum
$M_n$ is a closed subset of $\mathbb{R}$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 11.

Stated but not proved: `MetaMathlibExt.isClosed_nMarkoffSpectrum` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#is-closed-n-markoff-spectrum).

## Common minimum of the $n$-Lagrange and $n$-Markoff spectra

For every integer $n \ge 1$
there is a real number $\alpha$ that is the least element both of the $n$-Lagrange spectrum $L_n$
and of the $n$-Markoff spectrum $M_n$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 12.

Stated but not proved: `MetaMathlibExt.exists_isLeast_nLagrangeSpectrum_nMarkoffSpectrum` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#exists-is-least-n-lagrange-spectrum-n-ma).

## Scaled classical spectra lie in the $n$-spectra

Let $n \ge 1$ be a natural number and
write $L_k$ and $M_k$ for the $k$-Lagrange and $k$-Markoff spectra, so that $L_1$ and $M_1$
are the classical Lagrange and Markoff spectra. Then $n\alpha \in L_n$ for every
$\alpha \in L_1$ and $n\alpha \in M_n$ for every $\alpha \in M_1$; that is,
$n L_1 \subseteq L_n$ and $n M_1 \subseteq M_n$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 13.

Stated but not proved: `MetaMathlibExt.smul_spectrum_subset_nSpectrum` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#smul-spectrum-subset-n-spectrum).

## Hall's ray in the $n$-Lagrange spectrum

Let $L_1$ be the classical Lagrange spectrum and
let $F$ (Freĭman's constant) be the infimum of the real numbers $c$ with
$[c, \infty) \subseteq L_1$. Then for every integer $n \ge 1$,
$[nF, \infty) \subseteq L_n \subseteq M_n$, where $L_n$ is the $n$-Lagrange spectrum and
$M_n$ is the $n$-Markoff spectrum.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 14.

Stated but not proved: `MetaMathlibExt.hall_ray_nLagrangeSpectrum` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#hall-ray-n-lagrange-spectrum).

## The $n$-Lagrange spectrum is closed

For every integer $n \ge 1$, the $n$-Lagrange spectrum
$L_n$ is a closed subset of $\mathbb{R}$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 19.

Stated but not proved: `MetaMathlibExt.isClosed_nLagrangeSpectrum` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#is-closed-n-lagrange-spectrum).

## The $n$-Lagrange spectrum is the closure of its quadratic-irrational values

Let $n \ge 1$,
let $\lambda_n$ be the $n$-Lagrange approximability, and let $P_n$ be the set of real numbers
$\alpha$ such that $\alpha = \lambda_n(\xi)$ for some quadratic irrational $\xi$, that is, an
irrational real number with $a\xi^2 + b\xi + c = 0$ for some integers $a \ne 0$, $b$, $c$. Then
the $n$-Lagrange spectrum $L_n$ is the closure of $P_n$ in $\mathbb{R}$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 20.

Stated but not proved: `MetaMathlibExt.nLagrangeSpectrum_eq_closure_quadratic` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#n-lagrange-spectrum-eq-closure-quadratic).

## Isolated minimum of the $p$-Lagrange spectrum for primes below 2000

For every prime
$p < 2000$, the $p$-Lagrange spectrum $L_p$ has a least element $\alpha$ with the following
properties: $\alpha$ is an isolated point of $L_p$, that is, there is $\varepsilon > 0$ such that
every $\beta \in L_p$ with $|\beta - \alpha| < \varepsilon$ equals $\alpha$; $\alpha$ is
irrational; and $\alpha = \sqrt{r}$ for some rational number $r$.

This is Conjecture 1 of the source for primes below 2000.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Theorem 2, with Conjecture 1.

Stated but not proved: `MetaMathlibExt.min_nLagrangeSpectrum_isolated_sqrt_rat_of_prime_lt_2000` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#min-n-lagrange-spectrum-isolated-sqrt-ra).

## The prime $67$ and continued fraction digits $1$ and $2$

For an irrational real
number $\xi$, define its complete quotients by $\xi_0 = \xi$ and $\xi_{k+1} = 1/\{\xi_k\}$,
where $\{\cdot\}$ denotes the fractional part, and its continued fraction digits by
$a_k = \lfloor \xi_k \rfloor$. Let $p < 2000$ be a prime. Then there is no irrational $\xi$
such that the digits of both $\xi$ and $p\xi$ eventually all lie in $\{1, 2\}$ if and only
if $p = 67$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Theorem 3.

Stated but not proved: `MetaMathlibExt.no_eventually_one_two_contFrac_pair_iff_eq_67` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#no-eventually-one-two-cont-frac-pair-iff).

## Markoff points in the $p$-Lagrange spectrum

Let $x \le y \le z$ be positive integers with
$x^2 + y^2 + z^2 = 3xyz$ (a sorted Markoff triple), let $\lambda_z = \sqrt{9 - 4/z^2}$, let
$D = 9z^2 - 4$ if $z$ is odd and $D = (9z^2 - 4)/4$ if $z$ is even, and let $p$ be a prime.
Call $p$ a principal norm if $|u^2 + Duv + \frac{D^2 - D}{4} v^2| = p$ for some integers $u, v$,
that is, if some element $u + v \frac{D + \sqrt{D}}{2}$ of the quadratic order $\mathcal{O}_D$ has
norm $\pm p$. Then: (a) if $p$ is a principal norm, then $\lambda_z$ lies in the $p$-Lagrange
spectrum $L_p$; (b) if $\lambda_z \in L_p$ and, for every sorted Markoff triple
$(x', y', z') \ne (x, y, z)$ with $z' \le z$, the rational number $(9z^2 - 4)/(9z'^2 - 4)$ is not
a square in $\mathbb{Q}$, then $p$ is a principal norm.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Proposition 26; the printed `λ_p ∈ L_p` is read as `λ_z ∈ L_p`, as in the proof.

Stated but not proved: `MetaMathlibExt.markoff_point_mem_nLagrangeSpectrum_iff_principal_norm` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#markoff-point-mem-n-lagrange-spectrum-if).

## Congruence conditions for Markoff points in the $p$-Lagrange spectrum

Let $p$ be a prime
and let $L_p$ be the $p$-Lagrange spectrum. Then: (a) $\sqrt{5} \in L_p$ if and only if
$p \equiv 0, \pm 1 \pmod 5$; (b) $2\sqrt{2} \in L_p$ if and only if $p \equiv 2, \pm 1 \pmod 8$;
(c) $\sqrt{221}/5 \in L_p$ if and only if $p$ is a square modulo $13$ and modulo $17$;
(d) $\sqrt{1517}/13 \in L_p$ if and only if $p$ is a square modulo $37$ and modulo $41$;
(e) $\sqrt{7565}/29 \in L_p$ if and only if $p$ is a square modulo $5$, modulo $17$ and modulo
$89$. Here $p$ is a square modulo $m$ when $p \equiv a^2 \pmod m$ for some integer $a$; this
includes the case $p \equiv 0 \pmod m$.

Part (f) of the source, for $10\sqrt{26}/17$, is omitted: as printed it fails at $p = 17$.

## Sources

- Brandon Dong, Soren Dupont, Evan M. O'Dorney and W. Theo Waitkus, *Raney Transducers and the Lowest Point of the n-Lagrange Spectrum*, INTEGERS 25 (2025), Article A47, Corollary 27.

Stated but not proved: `MetaMathlibExt.markoff_points_mem_nLagrangeSpectrum_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NLagrangeSpectrumWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html#markoff-points-mem-n-lagrange-spectrum-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: n-Lagrange and n-Markoff spectra](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/n-lagrange-and-n-markoff-spectra)
