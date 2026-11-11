---
declaration: section
origin: cited
lean: MvPowerSeries.coefficientOperator, MvPowerSeries.coeff_coefficientOperator, MvPowerSeries.add_one_le_order_coefficientOperator, MvPowerSeries.add_le_order_iterate_coefficientOperator, MvPowerSeries.coeff_iterate_coefficientOperator_eq_zero, MvPowerSeries.coeff_coefficientOperator_eq_sum, MvPowerSeries.pderiv_compLeft, MvPowerSeries.pderiv_coefficientOperator
statement: formalized
proof: formalized
---

# Exponentials of coefficient operators

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html).

## Coefficient operator on multivariate power series

The operator `∑ i, X i * O i`, defined by finite coefficient sums.

Formalized by `MvPowerSeries.coefficientOperator`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coefficient-operator).

## Coefficient formula for a coefficient operator

The coefficient of the formal operator is a sum over the exponent support.

Formalized by `MvPowerSeries.coeff_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-coefficient-operator).

## Coefficient operators raise the order by one

A coefficient operator raises every natural lower bound on order by one.

Formalized by `MvPowerSeries.add_one_le_order_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#add-one-le-order-coefficient-operator).

## Iterated coefficient operators raise the order

Iteration raises every natural lower bound on order by the number of steps.

Formalized by `MvPowerSeries.add_le_order_iterate_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#add-le-order-iterate-coefficient-operato).

## Low-degree coefficients of an iterated coefficient operator vanish

The `n`th iterate has no coefficient in total degree less than `n`.

Formalized by `MvPowerSeries.coeff_iterate_coefficientOperator_eq_zero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-iterate-coefficient-operator-eq-ze).

## Coefficient of a coefficient operator over any finite superset

At any exponent, sum over any finite set containing its support.

Formalized by `MvPowerSeries.coeff_coefficientOperator_eq_sum`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-coefficient-operator-eq-sum).

## Partial derivatives commute with coefficient lifting

Partial differentiation commutes with canonical coefficient lifting.

Formalized by `MvPowerSeries.pderiv_compLeft`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-comp-left).

## Partial derivative of a coefficient operator

The operator derivative is the operator of the derivative plus the lifted `O i`.

Formalized by `MvPowerSeries.pderiv_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-coefficient-operator).

## Lifted coefficient maps commute with the coefficient operator

Lifted coefficient maps commute with the operator under the source pairwise premise.

Formalized by `MvPowerSeries.compLeft_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#comp-left-coefficient-operator).

## Product rule for coefficient operators

A family of coefficient derivations gives the source product rule, without commutation.

Formalized by `MvPowerSeries.coefficientOperator_mul`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/CoefficientOperator.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coefficient-operator-mul).

## Partial sums of the exponential of a coefficient operator

The first `N` operator iterates, `∑ n < N, 𝒪ⁿ / n!`, acting on the full input series.

Formalized by `MvPowerSeries.expOperatorPartial`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-partial).

## Partial operator exponential as a sum of function iterates

The finite exponential sum agrees with the source's function-iterate formula.

Formalized by `MvPowerSeries.expOperatorPartial_apply`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-partial-apply).

## Formal exponential of a coefficient operator

The formal exponential: coefficient `d` uses operator iterates `n ≤ d.degree`.

Formalized by `MvPowerSeries.expOperator`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator).

## Defining coefficient formula of the operator exponential

The defining iteration bound is exactly the source constructor's bound.

Formalized by `MvPowerSeries.coeff_expOperator_def`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-exp-operator-def).

## Coefficients of the operator exponential via partial sums

For `d.degree < N`, the first `N` operator iterates determine coefficient `d`.

Formalized by `MvPowerSeries.coeff_expOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-exp-operator).

## The operator exponential preserves the constant coefficient

The formal exponential preserves every constant coefficient, including nonzero ones.

Formalized by `MvPowerSeries.constantCoeff_expOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#constant-coeff-exp-operator).

## Operator exponential when the square of the operator vanishes

If the second operator iterate vanishes on `f`, its exponential is `f + 𝒪 f`.

Formalized by `MvPowerSeries.expOperator_of_sq_zero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-of-sq-zero).

## The operator exponential fixes series annihilated by the operator

The exponential fixes an input annihilated by the coefficient operator.

Formalized by `MvPowerSeries.expOperator_of_zero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-of-zero).

## Exponential of the zero coefficient-operator family is the identity

The exponential of the zero coefficient-map family is the identity linear map.

Formalized by `MvPowerSeries.expOperator_zero_family`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponential.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-zero-family).

## Lifted coefficient maps commute with coefficient-operator iterates

A lifted coefficient map commutes with every coefficient-operator iterate when the
coefficient maps commute pairwise.

Formalized by `MvPowerSeries.compLeft_iterate_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#comp-left-iterate-coefficient-operator).

## Partial derivative of a coefficient-operator iterate

The partial derivative of the `(n + 1)`st coefficient-operator iterate is the
iterate of the partial derivative plus `(n + 1)` copies of the lifted coefficient map.

Formalized by `MvPowerSeries.pderiv_iterate_coefficientOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-iterate-coefficient-operator).

## Partial derivative of partial sums of the operator exponential

The partial derivative of the first `N + 1` exponential terms is the corresponding
partial sum on the derivative plus the first `N` terms on the lifted coefficient map.

Formalized by `MvPowerSeries.pderiv_expOperatorPartial`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-exp-operator-partial).

## Partial derivative of a coefficient-operator exponential

The partial derivative of a formal coefficient-operator exponential is the exponential
of the input derivative plus the exponential of the lifted coefficient map.

Formalized by `MvPowerSeries.pderiv_expOperator`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-exp-operator).

## Gradient law for the exponential of commuting coefficient derivations

The exponential gradient law specialized to a pairwise commuting family of coefficient
derivations, using their canonical rational linear maps.

Formalized by `MvPowerSeries.pderiv_expOperator_derivation`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialDerivative.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#pderiv-exp-operator-derivation).

## The exponential of coefficient derivations is multiplicative

The formal exponential of a family of coefficient derivations preserves products.
No pairwise commutation or finiteness hypothesis on the family is needed.

Formalized by `MvPowerSeries.expOperator_mul`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-mul).

## The exponential of coefficient derivations preserves one

The formal exponential of a family of coefficient derivations preserves one.

Formalized by `MvPowerSeries.expOperator_one`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-one).

## Exponential of coefficient derivations as a ring endomorphism

The formal exponential of coefficient derivations as a ring endomorphism.

Formalized by `MvPowerSeries.expOperatorHom`, a definition declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-hom).

## Evaluation of the operator-exponential ring homomorphism

Applying the operator-exponential ring homomorphism is the existing formal operator
exponential.

Formalized by `MvPowerSeries.expOperatorHom_apply`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-hom-apply).

## Operator exponential coefficients depend only on lower-degree inputs

A coefficient of the operator exponential depends only on input coefficients of no
greater total degree.

Formalized by `MvPowerSeries.coeff_expOperator_congr`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#coeff-exp-operator-congr).

## The operator exponential commutes with the formal exponential

The operator exponential commutes with the lawful ordinary formal exponential.

Formalized by `MvPowerSeries.expOperator_expOfConstantCoeffZero`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/OperatorExponentialHom.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html#exp-operator-exp-of-constant-coeff-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponentials of coefficient operators](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series/exponentials-of-coefficient-operators)
