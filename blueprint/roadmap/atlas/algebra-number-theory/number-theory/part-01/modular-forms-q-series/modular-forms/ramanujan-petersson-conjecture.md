---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.RamanujanExponent.LocalExponentFamily, MathlibExt.NumberTheory.RamanujanExponent.exponentSet, MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf, MathlibExt.NumberTheory.RamanujanExponent.IsAdmissible, MathlibExt.NumberTheory.RamanujanExponent.GeneralizedRamanujanFor, MathlibExt.NumberTheory.RamanujanExponent.exponent_le_ramanujanExponentOf, MathlibExt.NumberTheory.RamanujanExponent.isAdmissible_ramanujanExponentOf, MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf_le_of_isAdmissible
statement: formalized
proof: formalized
---

# Ramanujan–Petersson conjecture

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html).

## Family of local exponents

A local-exponent family indexed by a type $\iota$ is a function
$m : \iota \to \mathbb{R}$, the local Langlands exponents, with $0 \le m(i) \le 1/2$ for every
$i \in \iota$.

The upper bound $1/2$ is the Jacquet--Shalika range for genuine cuspidal data. The index type is
part of the data, so the exponent of such a family is a construction attached to the family, not
a definition of the fixed Ramanujan exponent $\delta_2$ of $\mathrm{GL}_2$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.LocalExponentFamily`, a structure declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#local-exponent-family).

## Exponent set of a local-exponent family

For a local-exponent family $F$ indexed by a type
$\iota$, with local exponents $m(i)$ for $i \in \iota$, the exponent set of $F$ is the set of real
numbers $\{0\} \cup \{m(i) : i \in \iota\}$.

The adjoined $0$ makes the supremum of this set the correct value when $\iota$ is empty and in the
tempered case, where every local exponent is $0$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.exponentSet`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#exponent-set).

## Ramanujan exponent of a local-exponent family

The Ramanujan exponent of a local-exponent
family $F$ with local exponents $m(i)$, $i \in \iota$, is the supremum of the set
$\{0\} \cup \{m(i) : i \in \iota\}$. It is the supremum of the local exponents when $\iota$ is
nonempty, and $0$ when $\iota$ is empty.

For the eventual genuine family of cuspidal local components of $\mathrm{GL}_2$ this will be the
Ramanujan exponent $\delta_2$; for other families it is only the supremum of the given
exponents.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#ramanujan-exponent-of).

## Admissibility of an exponent for a local-exponent family

A local-exponent family $F$ is
admissible at a real number $\delta$ (Hypothesis $H_2(\delta)$ for $F$) when every local exponent
$m_i$ of $F$ ($i \in \iota$) is at most $\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.IsAdmissible`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#is-admissible).

## Generalized Ramanujan conjecture for a family

A local-exponent family $F$ satisfies the
Generalized Ramanujan conclusion when every local exponent $m_i$ of $F$ ($i \in \iota$) is zero.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.GeneralizedRamanujanFor`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#generalized-ramanujan-for).

## Local exponents are bounded by the Ramanujan exponent

For every local-exponent family $F$
and every index $i$, the local exponent $m_i$ of $F$ at $i$ is at most the Ramanujan exponent of
$F$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.exponent_le_ramanujanExponentOf`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#exponent-le-ramanujan-exponent-of).

## The Ramanujan exponent is admissible

For every local-exponent family $F$, $F$ is admissible
at its Ramanujan exponent: every local exponent of $F$ is at most the Ramanujan exponent of $F$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.isAdmissible_ramanujanExponentOf`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#is-admissible-ramanujan-exponent-of).

## Admissible exponents bound the Ramanujan exponent

Let $F$ be a local-exponent family and
let $\delta \ge 0$ be a real number. If $\delta$ is admissible for $F$, that is, every local
exponent of $F$ is at most $\delta$, then the Ramanujan exponent of $F$ is at most $\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf_le_of_isAdmissible`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#ramanujan-exponent-of-le-of-is-admissibl).

## Admissibility is a bound by the Ramanujan exponent

For every local-exponent family $F$ and
every real $\delta \ge 0$, $F$ is admissible at $\delta$ if and only if the Ramanujan exponent of
$F$ is at most $\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.isAdmissible_iff_ramanujanExponentOf_le`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#is-admissible-iff-ramanujan-exponent-of).

## The Ramanujan exponent vanishes exactly in the tempered case

For every local-exponent
family $F$, the Ramanujan exponent of $F$ is $0$ if and only if $F$ satisfies the generalized
Ramanujan conclusion, that is, every local exponent of $F$ is $0$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf_eq_zero_iff`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#ramanujan-exponent-of-eq-zero-iff).

## Admissible exponents of a local-exponent family

For a local-exponent family $F$ with
local exponents $m_i$ ($i \in \iota$), the set of admissible exponents of $F$ is the set of real
numbers $\delta \ge 0$ such that $F$ is admissible at $\delta$, that is, $m_i \le \delta$ for
every index $i$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.admissibleExponents`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#admissible-exponents).

## The Ramanujan exponent is the infimum of the admissible exponents

For every
local-exponent family $F$, the Ramanujan exponent of $F$ equals the infimum of the admissible
exponents of $F$, that is, of the set of real numbers $\delta \ge 0$ such that every local
exponent of $F$ is at most $\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf_eq_sInf_admissibleExponents`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#ramanujan-exponent-of-eq-s-inf-admissibl).

## Satake pairs with a given local exponent

For real numbers $N$ and $t$, a pair
$(\alpha, \beta)$ of complex numbers is in arithmetic Satake normalization with local exponent $t$
at residue cardinality $N$ when $|\alpha\beta| = 1$, $|\alpha| = N^t$ and $|\beta| = N^{-t}$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.IsSatakePair`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#is-satake-pair).

## Hecke bound from a Satake pair

Let $N \ge 1$ and $t, \delta$ be real numbers with
$0 \le t \le \delta$. If complex numbers $\alpha, \beta$ form a Satake pair with local exponent
$t$ at residue cardinality $N$, then $|\alpha + \beta| \le 2 N^\delta$.

The catalogue also records the sharper expression $N^\delta + N^{-\delta}$; the bound proved here
is its displayed consequence $2N^\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.hecke_norm_le_two_mul_rpow_of_isSatakePair`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#hecke-norm-le-two-mul-rpow-of-is-satake).

## Hecke bound from a Satake pair at a finite place

Let $K$ be a number field, $v$ a finite
place of $K$ with residue norm $N(v)$, and $t, \delta$ real numbers with $0 \le t \le \delta$. If
complex numbers $\alpha, \beta$ form a Satake pair with local exponent $t$ at residue cardinality
$N(v)$, then $|\alpha + \beta| \le 2 N(v)^\delta$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.hecke_norm_le_two_mul_residueNorm_rpow_of_isSatakePair`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#hecke-norm-le-two-mul-residue-norm-rpow).

## Exceptional Selberg eigenvalue witnesses

The type of pairs $(\Gamma, \lambda)$ where
$\Gamma$ is a congruence subgroup of $\mathrm{SL}_2(\mathbb{Z})$ and $\lambda$ is a real
eigenvalue of the hyperbolic Laplacian on $L^2(\Gamma \backslash \mathbb{H})$ with
$0 < \lambda < 1/4$.

Morally, these pairs index archimedean local components over $\mathbb{Q}$; their
identification with genuine cuspidal automorphic local components is a modelling assumption.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.SelbergWitness`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#selberg-witness).

## Selberg gap of an exceptional eigenvalue

For an exceptional-eigenvalue witness, a
congruence subgroup $\Gamma$ of $\mathrm{SL}_2(\mathbb{Z})$ with a Laplace eigenvalue
$\lambda \in (0, 1/4)$, the Selberg gap is $\sqrt{1/4 - \lambda}$: the archimedean local exponent
$\theta$ forced by $\lambda$, written as $\lambda = 1/4 - \theta^2$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.selbergGap`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#selberg-gap).

## Selberg family of archimedean exponents

The Selberg family is the local-exponent family
indexed by the exceptional-eigenvalue witnesses, the pairs $(\Gamma, \lambda)$ of a congruence
subgroup $\Gamma$ of $\mathrm{SL}_2(\mathbb{Z})$ and a Laplace eigenvalue $\lambda \in (0, 1/4)$
of $\Gamma$, whose local exponent at $(\Gamma, \lambda)$ is $\sqrt{1/4 - \lambda}$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.selbergFamily`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#selberg-family).

## Families dominating the Selberg exceptional spectrum

A local-exponent family $F$ with
local exponents $m_i$ ($i \in \iota$) dominates the Selberg archimedean slice when, for every
congruence subgroup $\Gamma$ of $\mathrm{SL}_2(\mathbb{Z})$ and every eigenvalue $\lambda$ of the
hyperbolic Laplacian on $L^2(\Gamma \backslash \mathbb{H})$ with $0 < \lambda < 1/4$, there is an
index $i$ with $m_i = \sqrt{1/4 - \lambda}$.

This is the precise anchor needed for the comparison with Selberg's constant; it is a hypothesis
on a proposed genuine family, not a definition of one.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.DominatesSelberg`, a definition declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#dominates-selberg).

## Exceptional eigenvalues bound Selberg-dominating exponents from below

Let $F$ be a
local-exponent family that dominates the Selberg archimedean slice. If $\Gamma$ is a congruence
subgroup of $\mathrm{SL}_2(\mathbb{Z})$ and $\lambda$ is a real eigenvalue of the hyperbolic
Laplacian on $L^2(\Gamma \backslash \mathbb{H})$ with $0 < \lambda < 1/4$, then
$\sqrt{1/4 - \lambda}$ is at most the Ramanujan exponent of $F$.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.sqrt_le_ramanujanExponentOf_of_dominatesSelberg`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#sqrt-le-ramanujan-exponent-of-of-dominat).

## Selberg's constant is at most every dominating family's exponent

Let $F$ be a
local-exponent family that dominates the Selberg archimedean slice, that is, for every
congruence subgroup $\Gamma$ of $\mathrm{SL}_2(\mathbb{Z})$ and every Laplace eigenvalue
$\lambda \in (0, 1/4)$ of $\Gamma$, the gap $\sqrt{1/4 - \lambda}$ is one of the local exponents
of $F$. Then Selberg's constant is at most the Ramanujan exponent of $F$.

For the genuine cuspidal family this is the archimedean comparison of Selberg's constant with the
Ramanujan exponent $\delta_2$; it is not an equality of constants.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.selbergConstant_le_of_dominatesSelberg`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#selberg-constant-le-of-dominates-selberg).

## The Selberg family's exponent is Selberg's constant

The Ramanujan exponent of the
canonical Selberg family of archimedean exponents is exactly Selberg's congruence spectral-gap
constant.

This identifies the currently anchored archimedean slice; it does not identify that slice with
the full Ramanujan exponent.

Formalized by `MathlibExt.NumberTheory.RamanujanExponent.ramanujanExponentOf_selbergFamily`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ModularForms/RamanujanExponent.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html#ramanujan-exponent-of-selberg-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan–Petersson conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/ramanujan-petersson-conjecture)
