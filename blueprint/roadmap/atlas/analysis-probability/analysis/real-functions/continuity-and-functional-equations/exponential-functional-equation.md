---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_eq_exp_mul_of_continuous_add_mul, MathlibExt.Analysis.SpecialFunctions.ContinuousMultiplicativeFunctionalEqExpWanted.exists_eq_exp_mul_of_map_add_eq_mul
statement: formalized
---

# Exponential functional equation

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/exponential-functional-equation/index.html).

## Continuous solutions of the exponential functional equation

If a continuous function
$f : \mathbb{R} \to \mathbb{C}$ satisfies $f(0) = 1$ and $f(r + s) = f(r) f(s)$ for all real $r$
and $s$, then there is a complex number $L$ such that $f(r) = e^{rL}$ for every real $r$.

Formalized by `MetaMathlibExt.exists_eq_exp_mul_of_continuous_add_mul`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpOfContinuousAddMul.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ExpOfContinuousAddMul.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/exponential-functional-equation/index.html#exists-eq-exp-mul-of-continuous-add-mul).

## Continuous nonzero solutions of $f(x)f(y) = f(x+y)$ are exponentials

Let
$f : \mathbb{R} \to \mathbb{R}$ be a continuous function that is not identically zero and
satisfies $f(x)f(y) = f(x+y)$ for all real $x$ and $y$. Then there is a real constant $c$ such
that $f(x) = e^{cx}$ for every real $x$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_32`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.ContinuousMultiplicativeFunctionalEqExpWanted.exists_eq_exp_mul_of_map_add_eq_mul` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/ContinuousMultiplicativeFunctionalEqExpWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecialFunctions/ContinuousMultiplicativeFunctionalEqExpWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/exponential-functional-equation/index.html#exists-eq-exp-mul-of-map-add-eq-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential functional equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/exponential-functional-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/exponential-functional-equation)
