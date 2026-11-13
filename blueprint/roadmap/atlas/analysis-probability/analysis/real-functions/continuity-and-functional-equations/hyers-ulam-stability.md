---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.approx, MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.norm_nsmul_eq, MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_addMonoidHom_of_additive_defect, MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.eq_of_forall_norm_sub_le, MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_addMonoidHom_of_jensen_defect, MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_continuousLinearMap_of_additive_defect_of_continuousAt
statement: formalized
proof: formalized
---

# Hyers–Ulam stability

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html).

## Dyadic approximants in Hyers' proof

The dyadic approximants `2 ^ (-n) • f (2 ^ n • x)` used in Hyers' proof.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.approx`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#approx).

## Norm of a natural-number multiple

Norm of a natural-number multiple in a real normed space.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.norm_nsmul_eq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#norm-nsmul-eq).

## Hyers' theorem (Hyers–Ulam stability of the Cauchy equation)

If
`f : E → F` between real normed spaces, with `F` complete, satisfies
`‖f (x + y) - f x - f y‖ ≤ δ` for all `x, y`, then there is an additive map
`A : E →+ F` with `‖f x - A x‖ ≤ δ` for all `x`. The bound `δ` is sharp:
for `f x = x + c` on `ℝ` the defect is `‖c‖` and the best additive
approximant is the identity, at distance exactly `‖c‖`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_addMonoidHom_of_additive_defect`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#exists-add-monoid-hom-of-additive-defect).

## Uniqueness in Hyers' theorem

Two additive maps both within `δ` of
the same `f` are equal: their difference is additive, hence `n`-homogeneous,
while staying bounded by `2 * δ`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.eq_of_forall_norm_sub_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#eq-of-forall-norm-sub-le).

## Hyers–Ulam stability of Jensen's functional equation

If the midpoint
(Jensen) defect `‖f ((1/2) • (x + y)) - (1/2) • (f x + f y)‖` is `≤ δ` for
all `x, y`, then `f` is within `4 * δ` of an additive map plus the constant
`f 0`. The factor `4` comes from doubling the two Jensen estimates at
`(x + y, 0)` and `(x, y)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_addMonoidHom_of_jensen_defect`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#exists-add-monoid-hom-of-jensen-defect).

## Continuous Hyers–Ulam stability

If `f` is continuous at `0` (in
particular if `f` itself is continuous), the additive approximant from
Hyers' theorem is continuous, hence a continuous real-linear map. The proof:
continuity of `f` at `0` bounds `f` on a small ball, so the approximant is
bounded on that ball, and an additive map bounded on a ball is continuous
at `0` by the dyadic scaling argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HyersUlam.exists_continuousLinearMap_of_additive_defect_of_continuousAt`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/HyersUlam.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html#exists-continuous-linear-map-of-additive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyers–Ulam stability](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/hyers-ulam-stability)
