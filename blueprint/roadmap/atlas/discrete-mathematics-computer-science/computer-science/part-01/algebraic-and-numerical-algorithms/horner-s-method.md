---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.hornerEval, Cslib.Algorithms.Lean.TimeM.hornerEval_time, Cslib.Algorithms.Lean.TimeM.hornerEval_ret_eq_sum, Cslib.Algorithms.Lean.TimeM.hornerEval_ret_eq_eval, Cslib.Algorithms.Lean.TimeM.hornerEval_empty, Cslib.Algorithms.Lean.TimeM.hornerEval_singleton, Cslib.Algorithms.Lean.TimeM.hornerEval_zero
statement: formalized
proof: formalized
---

# Horner's method

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html).

## Horner evaluation with operation count

Let $R$ be a commutative semiring, let
$x \in R$, and let $a_0, \dots, a_{n-1} \in R$ be coefficients listed in ascending order of
degree. Horner evaluation starts with the accumulator $v = 0$ and, for $i = n-1, \dots, 0$
in turn, replaces $v$ by $a_i + x v$, charging two operations (one multiplication and one
addition) for each step. It returns the final accumulator together with the total number of
operations charged, a natural number.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval`, a definition declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval).

## Horner evaluation uses $2n$ operations

For every commutative semiring $R$, every
$x \in R$ and all coefficients $a_0, \dots, a_{n-1} \in R$, Horner evaluation of
$a_0, \dots, a_{n-1}$ at $x$ charges exactly $2n$ operations, one multiplication and one
addition per coefficient.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-time).

## Horner evaluation computes the coefficient sum

For every commutative semiring $R$,
every $x \in R$ and all coefficients $a_0, \dots, a_{n-1} \in R$, the value returned by Horner
evaluation of $a_0, \dots, a_{n-1}$ at $x$ is $\sum_{i=0}^{n-1} a_i x^i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_ret_eq_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-ret-eq-sum).

## Horner evaluation is polynomial evaluation

For every commutative semiring $R$,
every $x \in R$ and all coefficients $a_0, \dots, a_{n-1} \in R$, the value returned by Horner
evaluation of $a_0, \dots, a_{n-1}$ at $x$ equals $p(x)$, where
$p = a_0 + a_1 X + \dots + a_{n-1} X^{n-1} \in R[X]$ is the polynomial with these
coefficients.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_ret_eq_eval`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-ret-eq-eval).

## Horner evaluation of the empty coefficient list

For every commutative semiring $R$
and every $x \in R$, Horner evaluation at $x$ with no coefficients ($n = 0$) returns $0$
and charges $0$ operations.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-empty).

## Horner evaluation of a constant polynomial

For every commutative semiring $R$,
every $x \in R$ and every single coefficient $a_0 \in R$ ($n = 1$), Horner evaluation of
$a_0$ at $x$ returns $a_0$ and charges $2$ operations.

The two operations are the multiplication $x \cdot 0$ and the addition $a_0 + x \cdot 0$,
which are executed because the accumulator starts at zero.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-singleton).

## Horner evaluation at zero

For every commutative semiring $R$ and all coefficients
$a_0, \dots, a_n \in R$ (at least one coefficient), the value returned by Horner evaluation
of $a_0, \dots, a_n$ at $x = 0$ is $a_0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hornerEval_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Numerical/Horner.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Numerical/Horner.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html#horner-eval-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Horner's method](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/horner-s-method)
