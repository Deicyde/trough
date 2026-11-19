---
declaration: lemma
origin: cited
lean: ProbabilityTheory.SimpleProcess.integral_add_left, ProbabilityTheory.SimpleProcess.integral_smul_left, ProbabilityTheory.SimpleProcess.integral_add_right, ProbabilityTheory.SimpleProcess.integral_smul_right, ProbabilityTheory.SimpleProcess.integral_sub_left, ProbabilityTheory.SimpleProcess.integral_sub_right, ProbabilityTheory.SimpleProcess.integral_zero_left, ProbabilityTheory.SimpleProcess.integral_const_right
statement: formalized
proof: formalized
---

# elemStochIntegral_linear

The elementary stochastic integrals $\bullet_B$, $\bullet_L$ and $\bullet_{\mathbb{R}}$ are linear in both arguments.

## Depends on

- [Elementary stochastic integral](def-elemstochintegralbilin.md)
- [elemStochIntegralLinear](def-elemstochintegrallinear.md)
- [addCommGroup_simpleProcess](../simple-processes-and-elementary-predictable-sets/lem-addcommgroup-simpleprocess.md)
- [module_simpleProcess](../simple-processes-and-elementary-predictable-sets/lem-module-simpleprocess.md)

## Proof

(In Lean, this is split into several lemmas about each argument and add/sub/smul.)

Immediate from the definition.

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess.integral_add_left`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_add_left), [`ProbabilityTheory.SimpleProcess.integral_smul_left`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_smul_left), [`ProbabilityTheory.SimpleProcess.integral_add_right`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_add_right), [`ProbabilityTheory.SimpleProcess.integral_smul_right`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_smul_right), [`ProbabilityTheory.SimpleProcess.integral_sub_left`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_sub_left), [`ProbabilityTheory.SimpleProcess.integral_sub_right`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_sub_right), [`ProbabilityTheory.SimpleProcess.integral_zero_left`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_zero_left), [`ProbabilityTheory.SimpleProcess.integral_const_right`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess.integral_const_right).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 416](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L416)
