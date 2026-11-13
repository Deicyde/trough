---
declaration: section
origin: cited
lean: MetaMathlibExt.rogersRamanujanContFracReal, MetaMathlibExt.rogersRamanujanContFracReal_zero, MetaMathlibExt.rogersRamanujan_golden_ratio_theta_relation, MetaMathlibExt.rogersRamanujan_theta_coeff_eta_quotient
statement: formalized
---

# Rogers–Ramanujan continued fraction

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html).

## The real Rogers–Ramanujan continued fraction

For a real number $x$,

$$
R(x) = x^{1/5} \prod_{n \ge 0}
\frac{(1 - x^{5n+1})(1 - x^{5n+4})}{(1 - x^{5n+2})(1 - x^{5n+3})},
$$

where $x^{1/5}$ is the real power function (the nonnegative fifth root for $x \ge 0$, and
$|x|^{1/5} \cos(\pi/5)$ for $x < 0$), a factor whose denominator is $0$ is read as $0$, and the
infinite product is taken to be $1$ when it does not converge unconditionally. For $0 \le x < 1$
this is the product formula
$R(x) = x^{1/5} (x; x^5)_\infty (x^4; x^5)_\infty / ((x^2; x^5)_\infty (x^3; x^5)_\infty)$ of the
Rogers–Ramanujan continued fraction, where $(c; q)_\infty = \prod_{m \ge 0} (1 - c q^m)$.

## Sources

- S. E. Gladun and M. P. Chaudhary, *Connecting Ramanujan's Theta Functions, the Rogers-Ramanujan Continued Fraction, and the Golden Ratio*, INTEGERS 25 (2025), Article A43, Section 1 (the Rogers-Ramanujan continued fraction formula).

Formalized by `MetaMathlibExt.rogersRamanujanContFracReal`, a definition declared in [WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html#rogers-ramanujan-cont-frac-real).

## The Rogers–Ramanujan continued fraction vanishes at zero

The real Rogers–Ramanujan
continued fraction $R$ satisfies $R(0) = 0$.

## Sources

- S. E. Gladun and M. P. Chaudhary, *Connecting Ramanujan's Theta Functions, the Rogers-Ramanujan Continued Fraction, and the Golden Ratio*, INTEGERS 25 (2025), Article A43, Section 1 (the Rogers-Ramanujan continued fraction formula).

Formalized by `MetaMathlibExt.rogersRamanujanContFracReal_zero`, a theorem declared in [WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html#rogers-ramanujan-cont-frac-real-zero).

## Golden-ratio relation for the Rogers–Ramanujan continued fraction

Let $t > 0$, and put
$q = e^{-\pi t}$ and $q' = e^{-\pi/t}$. Let $\psi(x) = \sum_{n \ge 0} x^{n(n+1)/2}$ and
$E(x) = (x; x)_\infty = \prod_{n \ge 1} (1 - x^n)$, and set
$\tau(q) = \psi(q) - 5q^3 \psi(q^{25})$, $\rho(q) = \psi(q)^2 - 5q\,\psi(q^5)^2$ and

$$
g(0) = \frac{16\psi(q)^5 - \tau(q)\bigl(\tau(q)^4 + 5\tau(q)^2\rho(q) +
5\rho(q)^2\bigr)}{5\psi(q^5)}.
$$

Let $\Phi = (\sqrt{5} + 1)/2$, let $R$ be the real Rogers–Ramanujan continued fraction, and put
$U = \bigl(R(q)\,R(q'^{4/5})\bigr)^{5/2}$ and $V = \bigl(R(q)/R(q'^{4/5})\bigr)^{5/2}$. Then

$$
\Bigl(\sqrt{\Phi} - \frac{1}{\sqrt{\Phi}}\Bigr)\Bigl(U + \frac{1}{U}\Bigr) +
\Bigl(\sqrt{\Phi} + \frac{1}{\sqrt{\Phi}}\Bigr)\Bigl(V - \frac{1}{V}\Bigr) =
\frac{g(0)}{\sqrt{q}\,\bigl(E(q)\,E(q^5)\bigr)^2}.
$$

This is Theorem 1 of the source on the imaginary axis $z = it$, where $q = e^{\pi i z}$ and
$q' = e^{\pi i z'}$ with $z z' = -1$.

## Sources

- S. E. Gladun and M. P. Chaudhary, *Connecting Ramanujan's Theta Functions, the Rogers-Ramanujan Continued Fraction, and the Golden Ratio*, INTEGERS 25 (2025), Article A43, Theorem 1, Equation (3).

Stated but not proved: `MetaMathlibExt.rogersRamanujan_golden_ratio_theta_relation` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html#rogers-ramanujan-golden-ratio-theta-rela).

## Eta-quotient form of the Gladun–Chaudhary theta coefficient

In the ring of integer
power series in $q$, let $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$ be the triangular theta series
and $E_k = (q^k; q^k)_\infty$ the Euler products, and set $\tau(q) = \psi(q) - 5q^3\psi(q^{25})$
and $\rho(q) = \psi(q)^2 - 5q\,\psi(q^5)^2$. Then

$$
\bigl(16\psi(q)^5 - \tau(q)\bigl(\tau(q)^4 + 5\tau(q)^2\rho(q) + 5\rho(q)^2\bigr)\bigr)E_5E_{25} =
5\psi(q^5)\bigl(E_5^6 + 20q\,E_1^4E_{25}^2 + 110q^2E_1^3E_{25}^3 + 350q^3E_1^2E_{25}^4 +
600q^4E_1E_{25}^5 + 625q^5E_{25}^6\bigr).
$$

This is Theorem 2 of the source, which writes
$g(0) = \bigl(16\psi(q)^5 - \tau(q)(\tau(q)^4 + 5\tau(q)^2\rho(q) + 5\rho(q)^2)\bigr)/(5\psi(q^5))$
as $E_5^5/E_{25} + 20q\,E_1^4E_{25}/E_5 + 110q^2E_1^3E_{25}^2/E_5 + 350q^3E_1^2E_{25}^3/E_5 +
600q^4E_1E_{25}^4/E_5 + 625q^5E_{25}^5/E_5$, multiplied through by $5\psi(q^5)E_5E_{25}$.

## Sources

- S. E. Gladun and M. P. Chaudhary, *Connecting Ramanujan's Theta Functions, the Rogers-Ramanujan Continued Fraction, and the Golden Ratio*, INTEGERS 25 (2025), Article A43, Theorem 2.

Stated but not proved: `MetaMathlibExt.rogersRamanujan_theta_coeff_eta_quotient` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersRamanujanGoldenRatioWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html#rogers-ramanujan-theta-coeff-eta-quotien).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rogers–Ramanujan continued fraction](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-continued-fraction)
