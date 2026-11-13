---
declaration: section
origin: cited
lean: StatMech.Probability.cro2_integral_exp_mul, StatMech.Probability.cro2_integral_exp_le, StatMech.Probability.cro2_integral_one_sub_pow, StatMech.Probability.cro2_integral_lhs, StatMech.Probability.cro2_integral_rhs_le, StatMech.Probability.cro2_master_sub, StatMech.Probability.cro2_rhoOptimise
statement: formalized
proof: formalized
---

# The KKL inequality on the uniform cube with constant 2

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html).

## Integral of $e^{cx}$ over an interval

`∫_a^b exp (c x) dx = (exp (c b) - exp (c a)) / c` for `c ≠ 0`.

Formalized by `StatMech.Probability.cro2_integral_exp_mul`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-integral-exp-mul).

## Bound on the integral of $e^{-tu/2}$ over $(0, 1)$

`∫₀¹ exp (-(t/2) u) du ≤ 2 / t` for `t > 0`.

Formalized by `StatMech.Probability.cro2_integral_exp_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-integral-exp-le).

## Integral of $(1 - u)^n$ over $(0, 1)$

`∫₀¹ (1 - u)^n du = 1 / (n + 1)`.

Formalized by `StatMech.Probability.cro2_integral_one_sub_pow`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-integral-one-sub-pow).

## Integral of damped total-influence weights over the noise parameter

Integrating the damped total-influence weights over the noise parameter: `∫₀¹ ∑_S 4 |S|
 (1-u)^{|S|-1} c_S du = 4 ∑_{S ≠ ∅} c_S`.

Formalized by `StatMech.Probability.cro2_integral_lhs`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-integral-lhs).

## Bound on the integral of $\delta^{u/(2-u)}$ over $(0, 1)$

`∫₀¹ δ^{u/(2-u)} du ≤ 2 / log (1/δ)` for `0 < δ < 1`.

Formalized by `StatMech.Probability.cro2_integral_rhs_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-integral-rhs-le).

## Capped estimate rewritten in the variable $u = 1 - \rho^2$

The capped estimate in the variable `u = 1 - ρ²`: `∑_S 4 |S| (1-u)^{|S|-1} f̂(S)² ≤ δ^{u/(2-u)}
 ∑_S 4 |S| f̂(S)²`.

Formalized by `StatMech.Probability.cro2_master_sub`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-master-sub).

## KKL inequality

**KKL inequality** for the uniform measure, Fourier form with constant `2` (after J. Kahn, G.
 Kalai, N. Linial, *The influence of variables on Boolean functions*, FOCS 1988; this proof
 follows D. Falik, A. Samorodnitsky, *Edge-isoperimetric inequalities and influences*, 2007): `2
 · ∑_{S ≠ ∅} f̂(S)² · log (1 / maxₑ Infₑ) ≤ ∑_S 4 |S| f̂(S)²` for every Boolean function.

Formalized by `StatMech.Probability.cro2_rhoOptimise`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLUniform.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html#cro2-rho-optimise).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The KKL inequality on the uniform cube with constant 2](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-on-the-uniform-cube-with-cons)
