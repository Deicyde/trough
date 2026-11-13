---
declaration: section
origin: cited
lean: Real.log_one_sub_le_neg, Real.neg_add_sq_le_log_one_sub, Real.log_one_sub_bounds, Real.exp_neg_le_one_sub_add_sq, Real.pow_le_natCeil_mul_exp, Real.exists_nat_pow_le_mul_exp, Real.exists_nat_pow_le_mul_two_rpow
statement: formalized
proof: formalized
---

# Elementary bounds for exponentials and logarithms

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html).

## Linear upper bound for $\log(1 - x)$

For every real number $x$ with $1 - x > 0$,
$\log(1 - x) \le -x$.

Formalized by `Real.log_one_sub_le_neg`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#log-one-sub-le-neg).

## Quadratic lower bound for $\log(1 - x)$

For every real number $x$ with $0 < x < 1/2$,
$-x - x^2 \le \log(1 - x)$.

Formalized by `Real.neg_add_sq_le_log_one_sub`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#neg-add-sq-le-log-one-sub).

## Two-sided bound for $\log(1 - x)$

For every real number $x$ with $0 < x < 1/2$,
$-x - x^2 \le \log(1 - x) \le -x$.

Formalized by `Real.log_one_sub_bounds`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#log-one-sub-bounds).

## Quadratic upper bound for $e^{-x}$

For every real number $x \ge 0$,
$e^{-x} \le 1 - x + x^2$.

Formalized by `Real.exp_neg_le_one_sub_add_sq`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Log/Inequalities.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#exp-neg-le-one-sub-add-sq).

## Explicit exponential bound on a fixed power

An explicit natural multiple of a positive-rate exponential bounds a fixed power.

Formalized by `Real.pow_le_natCeil_mul_exp`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#pow-le-nat-ceil-mul-exp).

## Existence of a constant bounding a power by an exponential

A single natural constant bounds a fixed power by a positive-rate exponential.

Formalized by `Real.exists_nat_pow_le_mul_exp`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#exists-nat-pow-le-mul-exp).

## Polynomial bounded by a base-two exponential

The source estimate: a natural-input polynomial is bounded by a base-two exponential.

Formalized by `Real.exists_nat_pow_le_mul_two_rpow`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/PolynomialExponentialBound.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html#exists-nat-pow-le-mul-two-rpow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elementary bounds for exponentials and logarithms](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/inequalities/elementary-bounds-for-exponentials-and-logarithm)
