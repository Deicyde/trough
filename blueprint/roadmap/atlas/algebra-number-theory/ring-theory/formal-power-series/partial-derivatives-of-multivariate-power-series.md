---
declaration: section
origin: cited
lean: MvPowerSeries.iteratedPDeriv, MvPowerSeries.iteratedPDeriv_append, MvPowerSeries.pderiv_pderiv, MvPowerSeries.pderiv_iteratedPDeriv, Multiset.toFinsupp_coe_list_eq_sum, MvPowerSeries.factorial_smul_coeff_iteratedPDeriv, MvPowerSeries.factorial_smul_coeff_eq_constantCoeff_iteratedPDeriv, MvPowerSeries.factorial_smul_coeff_iteratedPDeriv_rat
statement: formalized
proof: formalized
---

# Partial derivatives of multivariate power series

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html).

## Iterated partial derivative of a multivariate power series

Partial derivatives in list order, with the first entry applied first, as a linear map.

Formalized by `MvPowerSeries.iteratedPDeriv`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#iterated-pderiv).

## Iterated partial derivatives along concatenated lists compose

Concatenating lists composes the second iterated derivative after the first.

Formalized by `MvPowerSeries.iteratedPDeriv_append`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#iterated-pderiv-append).

## Formal partial derivatives commute

Two formal partial derivatives commute.

Formalized by `MvPowerSeries.pderiv_pderiv`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#pderiv-pderiv).

## A partial derivative commutes with iterated partial derivatives

A partial derivative commutes with any list of partial derivatives.

Formalized by `MvPowerSeries.pderiv_iteratedPDeriv`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#pderiv-iterated-pderiv).

## Variable multiplicities of a list as a sum of singleton multi-indices

List variable multiplicities equal the sum of singleton multi-indices.

Formalized by `Multiset.toFinsupp_coe_list_eq_sum`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#to-finsupp-coe-list-eq-sum).

## Factorial-weighted coefficient of an iterated partial derivative

The factorial-weighted coefficient after iterated differentiation. No factorial is
cancelled, so this identity also holds in positive characteristic.

Formalized by `MvPowerSeries.factorial_smul_coeff_iteratedPDeriv`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#factorial-smul-coeff-iterated-pderiv).

## Factorial times a coefficient is a constant term of an iterated derivative

A monomial's factorial times its coefficient is the constant coefficient of the
corresponding iterated partial derivative.

Formalized by `MvPowerSeries.factorial_smul_coeff_eq_constantCoeff_iteratedPDeriv`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#factorial-smul-coeff-eq-constant-coeff-i).

## Rational factorial-weighted coefficient of an iterated derivative

The source rational-factorial scalar equation, obtained by casting the natural
factorial product and its scalar action.

Formalized by `MvPowerSeries.factorial_smul_coeff_iteratedPDeriv_rat`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#factorial-smul-coeff-iterated-pderiv-rat).

## Rational factorial coefficient as a constant term of an iterated derivative

The source rational-factorial constant coefficient equation.

Formalized by `MvPowerSeries.factorial_smul_coeff_eq_constantCoeff_iteratedPDeriv_rat`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/IteratedPDeriv.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#factorial-smul-coeff-eq-constant-coeff-i-2).

## Formal linear form in multivariate power series

The formal linear form with variable coefficient family `b : σ → R`.

Its coefficient at `d` is the sum of `b i` over the support of `d` when `d`
has total degree one, and zero otherwise.

Formalized by `MvPowerSeries.linearForm`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#linear-form).

## Coefficient formula for a formal linear form

The coefficient formula defining a formal linear form.

Formalized by `MvPowerSeries.coeff_linearForm`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#coeff-linear-form).

## Coefficient of a single variable in a formal linear form

The coefficient of variable `i` is the prescribed coefficient `b i`.

Formalized by `MvPowerSeries.coeff_linearForm_single`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#coeff-linear-form-single).

## A formal linear form has zero constant coefficient

A formal linear form has zero constant coefficient.

Formalized by `MvPowerSeries.constantCoeff_linearForm`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#constant-coeff-linear-form).

## Partial derivative of a formal linear form

The partial derivative of a formal linear form is its corresponding
constant coefficient.

Formalized by `MvPowerSeries.pderiv_linearForm`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#pderiv-linear-form).

## Coefficient ring maps commute with formal linear forms

Mapping the coefficient ring commutes with forming a formal linear form.

Formalized by `MvPowerSeries.map_linearForm`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/LinearForm.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html#map-linear-form).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial derivatives of multivariate power series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series/partial-derivatives-of-multivariate-power-series)
