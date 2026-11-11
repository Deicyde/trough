---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.add_deriv_mul_sub_le_of_convexOn, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.peierls_inequality, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_inequality, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.peierls_exp, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_sq, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.eigenvalues_nonneg_of_forall_nonneg_inner, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.eigenvalues_pos_of_forall_pos_inner, MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_entropy_tangent
statement: formalized
proof: formalized
---

# Peierls and Klein inequalities

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html).

## Convex differentiable functions lie above their tangent lines

The first-order (tangent-line) characterization of a convex
differentiable function: the graph lies above every tangent line.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.add_deriv_mul_sub_le_of_convexOn`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#add-deriv-mul-sub-le-of-convex-on).

## Peierls' inequality

The diagonal of a self-adjoint operator in
any orthonormal basis is majorized by its eigenvalues, as measured by
any convex function.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.peierls_inequality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#peierls-inequality).

## Klein's inequality

**Klein's inequality** (sum form): for a convex function `f`
differentiable at the eigenvalues of `S`, the tangent-line sum at the
eigenvalues of `S` evaluated on the diagonal of `T` is at most the sum
of `f` over the eigenvalues of `T`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_inequality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#klein-inequality).

## Peierls' inequality for the exponential

Peierls' inequality for the exponential function.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.peierls_exp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#peierls-exp).

## Klein's inequality for the square function

Klein's inequality for `f x = x ^ 2`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#klein-sq).

## Eigenvalues of a positive semidefinite operator are nonnegative

Eigenvalues of a positive semidefinite symmetric operator are
nonnegative: an eigenvalue is the Rayleigh quotient at a unit
eigenvector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.eigenvalues_nonneg_of_forall_nonneg_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#eigenvalues-nonneg-of-forall-nonneg-inne).

## Eigenvalues of a positive definite operator are positive

Eigenvalues of a positive definite symmetric operator are positive.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.eigenvalues_pos_of_forall_pos_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#eigenvalues-pos-of-forall-pos-inner).

## Entropy tangent bound in an arbitrary orthonormal basis

The entropy tangent bound in an arbitrary orthonormal basis. Its diagonal entries
need not align with the eigenvalues of `S`; `klein_entropy` supplies the aligned
quantum-relative-entropy form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_entropy_tangent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#klein-entropy-tangent).

## Klein's entropy inequality

Klein's entropy inequality in the eigenbasis of `S`. The eigenvalue at index `i`
is paired with its eigenvector, so this is the quantum-relative-entropy form up to
the trace terms. In particular, its tangent correction vanishes when `T = S`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.PeierlsKlein.klein_entropy`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/PeierlsKlein.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html#klein-entropy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Peierls and Klein inequalities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/peierls-and-klein-inequalities)
