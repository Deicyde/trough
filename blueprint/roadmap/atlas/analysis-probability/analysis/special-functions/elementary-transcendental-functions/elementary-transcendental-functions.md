---
declaration: section
origin: cited
lean: Real.eq_zero_of_sum_mul_exp_eq_zero, MetaMathlibExt.exists_parametrization_of_rpow_eq_rpow, Real.sigmoid_log_sub_log
statement: formalized
proof: formalized
---

# Exponential, logarithmic and related functions: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/index.html).

Exponential, logarithmic and trigonometric-type functions and their relatives: exponential integral E1 and Ein, logarithmic integral, Lambert W, logistic function, x^y = y^x, exponential sums, Mittag-Leffler expansion of 1/(e^u − 1), modified Bessel functions, Dickman–de Bruijn function, Bell-polynomial functions.

## Exponential sums have full column rank

If `∑_{u ∈ S} c_u exp(-a u)` vanishes at
`|S|` distinct points `a ∈ P` (the rates `u ∈ S` are distinct as elements of a `Finset`), every
coefficient is zero. Equivalently, the matrix `(exp(-a u))_{a ∈ P, u ∈ S}` has full column
rank when `|P| ≥ |S|`.

Formalized by `Real.eq_zero_of_sum_mul_exp_eq_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSumZeros.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSumZeros.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/index.html#eq-zero-of-sum-mul-exp-eq-zero).

## Parametrization of the solutions of $x^y = y^x$ with $0 < y < x$

Let $x$ and $y$ be real
numbers with $0 < y < x$ and $x^y = y^x$. Then there is a real number $t > 0$ such that
$y = (1 + 1/t)^t$ and $x = (1 + 1/t)^{t+1}$.

## Sources

- Hirotaka Kobayashi, Kota Saito, and Wataru Takeda, "Transcendence of Values of the Iterated Exponential Function at Algebraic Points," Journal of Integer Sequences 26 (2023), Article 23.3.3, Lemma, lines 604–612, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Takeda/tak6.tex>.

Formalized by `MetaMathlibExt.exists_parametrization_of_rpow_eq_rpow`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/RealPowerParametrization.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/RealPowerParametrization.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/index.html#exists-parametrization-of-rpow-eq-rpow).

## The logistic function of the log odds

For real numbers $a > 0$ and $b > 0$, the logistic
function $\sigma(z) = 1 / (1 + e^{-z})$ satisfies $\sigma(\log a - \log b) = a / (a + b)$.

Formalized by `Real.sigmoid_log_sub_log`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/SigmoidLogOdds.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/SigmoidLogOdds.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/index.html#sigmoid-log-sub-log).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential, logarithmic and related functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions)
