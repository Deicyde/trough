---
declaration: section
origin: cited
lean: CurveDivisor.evalMonoidHom, CurveDivisor.eval, CurveDivisor.eval_eq_prod, CurveDivisor.eval_zero, CurveDivisor.eval_single, CurveDivisor.eval_add, CurveDivisor.eval_zsmul
statement: formalized
proof: formalized
---

# Evaluation of curve divisors

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html).

## Evaluation of divisors as a group homomorphism

For a commutative group $G$ and a
function $f : C \to G$, this is the monoid homomorphism from the group of divisors on $C$,
written multiplicatively, to $G$ that sends a divisor $D$ to the finite product
$\prod_{P \in \operatorname{supp} D} f(P)^{D(P)}$.

Formalized by `CurveDivisor.evalMonoidHom`, a definition declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-monoid-hom).

## Evaluation of a divisor against a function

For a commutative group $G$, a function
$f : C \to G$ and a divisor $D$ on $C$, the evaluation of $D$ against $f$ is the element
$f(D) = \prod_{P \in \operatorname{supp} D} f(P)^{D(P)}$ of $G$.

Formalized by `CurveDivisor.eval`, a definition declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval).

## Evaluation is a product over the support

For a commutative group $G$, every function
$f : C \to G$ and every divisor $D$ on $C$, the evaluation of $D$ against $f$ equals
$\prod_{P \in \operatorname{supp} D} f(P)^{D(P)}$, the product over the points in the support
of $D$.

Formalized by `CurveDivisor.eval_eq_prod`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-eq-prod).

## The zero divisor evaluates to one

For a commutative group $G$ and every function
$f : C \to G$, the evaluation of the zero divisor on $C$ against $f$ is the identity element
$1$ of $G$.

Formalized by `CurveDivisor.eval_zero`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-zero).

## Evaluation of a one-point divisor

For a commutative group $G$, every function
$f : C \to G$, every point $P \in C$ and every integer $n$, the divisor $n \cdot P$, with
coefficient $n$ at $P$ and $0$ elsewhere, evaluates against $f$ to $f(P)^n$.

Formalized by `CurveDivisor.eval_single`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-single).

## Evaluation is multiplicative

For a commutative group $G$, every function
$f : C \to G$ and all divisors $D_1, D_2$ on $C$, writing $f(D)$ for the evaluation of a
divisor $D$ against $f$, we have $f(D_1 + D_2) = f(D_1) \, f(D_2)$.

Formalized by `CurveDivisor.eval_add`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-add).

## Evaluation of an integer multiple

For a commutative group $G$, every function
$f : C \to G$, every integer $n$ and every divisor $D$ on $C$, writing $f(D)$ for the
evaluation of $D$ against $f$, we have $f(nD) = f(D)^n$.

Formalized by `CurveDivisor.eval_zsmul`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/Curve/Evaluation.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html#eval-zsmul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Evaluation of curve divisors](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/evaluation-of-curve-divisors)
