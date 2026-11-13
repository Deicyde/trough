---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.meanValue, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.meanValue_of_norm_eq_one, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.centered, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance_of_norm_eq_one, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance_smul, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.inner_self_of_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.inner_right_of_isSelfAdjoint
statement: formalized
proof: formalized
---

# Robertson–Schrödinger uncertainty relation

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html).

## Normalized expectation value of an observable

The normalized real expectation is Mathlib's canonical Rayleigh quotient.
For a nonzero state and self-adjoint observable it is the physical expectation.
At zero this total definition is zero; zero is not a physical state.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.meanValue`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#mean-value).

## Normalized expectation on a unit vector

On a unit vector, normalized expectation equals the original quadratic mean.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.meanValue_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#mean-value-of-norm-eq-one).

## Centered state vector of an observable

The centered vector subtracts the normalized real expectation times the state.
Its squared norm divided by the squared state norm is `variance`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.centered`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#centered).

## Normalized variance of an observable

Normalized variance is the centered squared norm divided by the squared state norm.
For a nonzero state and self-adjoint observable it is the physical variance.
The totalized value at zero is zero. Off the unit sphere this corrects the raw
quadratic quantities; agreement with the original formulas is asserted only for unit states.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#variance).

## Normalized variance on the unit sphere

On the unit sphere, normalized variance is the centered squared norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance_of_norm_eq_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#variance-of-norm-eq-one).

## Normalized variance is invariant under nonzero scaling

Nonzero scalar multiplication does not change normalized variance.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance_smul`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#variance-smul).

## Expectation inner product of a self-adjoint operator

For a self-adjoint operator, the expectation inner product is the normalized
mean multiplied by the squared state norm. The norm factor is required off the unit sphere.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.inner_self_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#inner-self-of-is-self-adjoint).

## Flipped expectation inner product of a self-adjoint operator

The flipped expectation has the same necessary squared-state-norm factor.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.inner_right_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#inner-right-of-is-self-adjoint).

## Inner product of two centered vectors

The inner product of two centered vectors, for self-adjoint
operators at a unit vector: the uncentered inner product minus the
product of the mean values.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.inner_centered`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#inner-centered).

## Commutator expectation as the skew part of the centered inner product

The commutator expectation is the skew part of the inner product of
the centered vectors.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.commutator_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#commutator-inner).

## Commutator expectation of self-adjoint operators is purely imaginary

The commutator expectation of two self-adjoint operators is purely
imaginary: its real part vanishes.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.commutator_inner_re`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#commutator-inner-re).

## Squared norm of the commutator expectation

The squared norm of the commutator expectation is four times the
squared imaginary part of the centered inner product.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.norm_sq_commutator_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#norm-sq-commutator-inner).

## Norm of the commutator expectation

The commutator expectation has norm twice the absolute imaginary
part of the centered inner product.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.norm_commutator_inner_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#norm-commutator-inner-eq).

## Robertson–Schrödinger uncertainty principle

The **Robertson–Schrödinger uncertainty principle**: the product of
the variances is at least the squared covariance plus a quarter of the
squared norm of the commutator expectation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.schrodinger`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#schrodinger).

## Robertson's uncertainty principle

The product of the variances
is at least a quarter of the squared norm of the commutator
expectation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.robertson`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#robertson).

## Commutator of commuting operators vanishes

The commutator of commuting operators vanishes.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.commutator_eq_zero_of_commute`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#commutator-eq-zero-of-commute).

## Variance as second moment minus squared mean

The variance is the second moment minus the squared mean.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RobertsonUncertainty.variance_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/RobertsonUncertainty.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html#variance-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Robertson–Schrödinger uncertainty relation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators/robertson-schr-dinger-uncertainty-relation)
