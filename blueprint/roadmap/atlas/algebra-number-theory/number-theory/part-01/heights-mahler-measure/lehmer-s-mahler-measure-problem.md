---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure, MathlibExt.NumberTheory.LehmerConstant.one_le_intMahlerMeasure, MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_C, MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_one, MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_two, MathlibExt.NumberTheory.LehmerConstant.mahlerMeasuresAboveOne, MathlibExt.NumberTheory.LehmerConstant.lehmerConstant, MathlibExt.NumberTheory.LehmerConstant.lehmerConstant_le_intMahlerMeasure
statement: formalized
---

# Lehmer's Mahler measure problem

18 results, 15 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html).

## Mahler measure of an integer polynomial

The Mahler measure of $f \in \mathbb{Z}[X]$
is the Mahler measure of its image in $\mathbb{C}[X]$. It equals
$|a| \prod_i \max(1, |\alpha_i|)$, where $a$ is the leading coefficient of $f$ and the
$\alpha_i$ are the complex roots of $f$ counted with multiplicity.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#int-mahler-measure).

## Nonzero integer polynomials have Mahler measure at least one

If
$f \in \mathbb{Z}[X]$ is a nonzero polynomial, then its Mahler measure satisfies $M(f) \ge 1$.

Indeed, $M(f) = |a| \prod_i \max(1, |\alpha_i|)$, where the leading coefficient $a$ of $f$ is a
nonzero integer and the $\alpha_i$ are the complex roots of $f$ counted with multiplicity, so
every factor is at least $1$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.one_le_intMahlerMeasure`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#one-le-int-mahler-measure).

## Mahler measure of a monic linear integer polynomial

For every integer $a$, the
Mahler measure of the integer polynomial $X - a$ is $\max(1, |a|)$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_C`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#int-mahler-measure-x-sub-c).

## Mahler measure of $X - 1$

The integer polynomial $X - 1$ has Mahler measure $1$.

Since $1$ is not strictly larger than $1$, this value is excluded from the set whose
infimum is Lehmer's constant.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_one`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#int-mahler-measure-x-sub-one).

## Mahler measure of $X - 2$

The integer polynomial $X - 2$ has Mahler measure $2$.

Since $2 > 1$, this value lies in the set whose infimum is Lehmer's constant.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_X_sub_two`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#int-mahler-measure-x-sub-two).

## Mahler measures above one

This is the set of real numbers of the form $M(f)$, where
$f \in \mathbb{Z}[X]$ is an integer polynomial whose Mahler measure $M(f)$ is strictly larger
than $1$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.mahlerMeasuresAboveOne`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#mahler-measures-above-one).

## Lehmer's constant

Writing $M(f)$ for the Mahler measure of an integer polynomial $f$,
Lehmer's constant is
$C_{40a} = \inf \{M(f) : f \in \mathbb{Z}[X],\ M(f) > 1\}$,
the infimum of the Mahler measures of integer polynomials that are strictly larger than $1$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.lehmerConstant`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-constant).

## Lehmer's constant bounds every Mahler measure above $1$

For every integer polynomial
$f$ whose Mahler measure is strictly larger than $1$, Lehmer's constant is at most the Mahler
measure of $f$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.lehmerConstant_le_intMahlerMeasure`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-constant-le-int-mahler-measure).

## Lehmer's constant is at least one

Lehmer's constant $L$, the infimum of the Mahler
measures strictly larger than $1$ of polynomials in $\mathbb{Z}[X]$, satisfies $1 \le L$.

This is the lower bound recorded in the catalogue for the constant $C_{40a}$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.one_le_lehmerConstant`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#one-le-lehmer-constant).

## Lehmer's constant is at most $2$

Lehmer's constant $C_{40a}$ satisfies
$C_{40a} \le 2$.

The witness is the integer polynomial $X - 2$, whose Mahler measure is $2$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.lehmerConstant_le_two`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-constant-le-two).

## Lehmer's question

The proposition that there are integer polynomials with
Mahler measure arbitrarily close to $1$ from above: for every real $\varepsilon > 0$ there is a
polynomial $f \in \mathbb{Z}[X]$ whose Mahler measure $M(f)$ satisfies $1 < M(f) < 1 + \varepsilon$.

Lehmer asked in 1933 whether this proposition holds.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.LehmerQuestion`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-question).

## Lehmer's question in terms of Lehmer's constant

Lehmer's constant equals $1$ if and
only if Lehmer's question has a positive answer, that is, for every $\varepsilon > 0$ there is
an integer polynomial whose Mahler measure lies strictly between $1$ and $1 + \varepsilon$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.lehmerConstant_eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-constant-eq-one-iff).

## Lehmer's polynomial

Lehmer's polynomial is the integer polynomial
$X^{10} + X^9 - X^7 - X^6 - X^5 - X^4 - X^3 + X + 1$.

Lehmer found it in 1933. Its Mahler measure $1.176280\ldots$ is still the smallest known
Mahler measure larger than $1$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.lehmerPolynomial`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer-polynomial).

## Smyth's polynomial

Smyth's polynomial is $X^3 - X - 1 \in \mathbb{Z}[X]$.

Its Mahler measure is the plastic number $\theta_0 = 1.324717\ldots$, the real root of
$X^3 - X - 1$. Smyth proved in 1971 that every polynomial $f \in \mathbb{Z}[X]$ with
$f(0) \neq 0$ that is nonreciprocal (reversing its coefficients gives neither $f$ nor $-f$)
has Mahler measure at least $\theta_0$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.smythPolynomial`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#smyth-polynomial).

## Reciprocal polynomial

An integer polynomial $f$ is reciprocal when reversing its
coefficients gives $f$ or $-f$, that is, when $X^d f(1/X) = f$ or $X^d f(1/X) = -f$, where $d$
is the degree of $f$, taken to be $0$ when $f = 0$.

Formalized by `MathlibExt.NumberTheory.LehmerConstant.IsReciprocal`, a definition declared in [MathlibExt/NumberTheory/Height/LehmerConstant.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/LehmerConstant.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#is-reciprocal).

## Mahler measure of Lehmer's polynomial

The Mahler measure of Lehmer's polynomial is at most
$1176281/1000000 = 1.176281$.

## Sources

- Lehmer (1933), the Mahler measure of Lehmer's polynomial is `1.176280818...`, hence at most `1.176281`. No root-location computation for the degree-ten example is formalized here.

Stated but not proved: `MathlibExt.NumberTheory.LehmerConstant.intMahlerMeasure_lehmerPolynomial_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/LehmerConstantWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Height/LehmerConstantWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#int-mahler-measure-lehmer-polynomial-le).

## Lehmer's upper bound for Lehmer's constant

Lehmer's constant is at most
$1176281/1000000 = 1.176281$.

## Sources

- Lehmer (1933), catalogue upper bound `C₄₀ₐ ≤ 1.176280...` from the Mahler measure of Lehmer's polynomial, rounded up at the sixth decimal place.

Stated but not proved: `MathlibExt.NumberTheory.LehmerConstant.lehmer1933UpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/LehmerConstantWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Height/LehmerConstantWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#lehmer1933-upper-bound-wanted).

## Smyth's theorem for nonreciprocal polynomials

Let $f \in \mathbb{Z}[X]$ be an integer
polynomial that is not reciprocal and whose constant term $f(0)$ is nonzero. Then the Mahler
measure of $f$ is at least the Mahler measure of Smyth's polynomial $X^3 - X - 1$.

## Sources

- Smyth (1971), as quoted in the catalogue: a nonreciprocal integer polynomial with nonzero constant term has Mahler measure at least that of `X^3 - X - 1` (the plastic number `1.324717...`).

Stated but not proved: `MathlibExt.NumberTheory.LehmerConstant.smyth1971Nonreciprocal_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/LehmerConstantWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Height/LehmerConstantWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html#smyth1971-nonreciprocal-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lehmer's Mahler measure problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/heights-mahler-measure/lehmer-s-mahler-measure-problem)
