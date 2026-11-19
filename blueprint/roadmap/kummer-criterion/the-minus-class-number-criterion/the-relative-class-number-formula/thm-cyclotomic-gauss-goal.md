---
declaration: theorem
origin: cited
lean: KummerCriterion.cyclotomicHGaussGoal_holds
statement: formalized
proof: formalized
---

# cyclotomic-gauss-goal

The explicit Gauss-product evaluation of [Theorem raw-gauss-product](thm-raw-gauss-product.md) satisfies the packaged Gauss hypothesis required by the relative class-number assembly theorem ([Theorem hminus-formula-from-inputs](thm-hminus-formula-from-inputs.md)).

## Depends on

- [raw-gauss-product](thm-raw-gauss-product.md)

## Proof

Purely formal: the assembly theorem consumes the Gauss product in a normalised shape (with the analytic constants of the odd $L$-value formula distributed over the product), and this normalisation is a finite algebraic rewriting of [Theorem raw-gauss-product](thm-raw-gauss-product.md).

## Lean

Formalized as [`KummerCriterion.cyclotomicHGaussGoal_holds`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.cyclotomicHGaussGoal_holds).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 170](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L170)
