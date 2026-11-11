---
declaration: section
origin: cited
lean: ProbabilityTheory.uStatistic, ProbabilityTheory.hoeffdingProj, ProbabilityTheory.integral_uStatistic, ProbabilityTheory.variance_uStatistic
statement: formalized
proof: formalized
---

# U-statistics

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html).

## U-statistic

The U-statistic with kernel `h` of degree `m` on a sample `x` of size `n`: the average of
`h (x ∘ f)` over the `n.descFactorial m` injective maps `f : Fin m ↪ Fin n`. For `m > n` there
are no such maps and the value is `0` (Lean's `a / 0 = 0`).

Formalized by `ProbabilityTheory.uStatistic`, a definition declared in [MathlibExt/Probability/Statistics/UStatistic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/UStatistic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html#u-statistic).

## Hoeffding projection of a kernel

Hoeffding's `c`-th projection of a kernel `h` of degree `m` under `μ`:
`h_c(y) = E h(y₁, …, y_c, X_{c+1}, …, X_m)` with `X_{c+1}, …, X_m` i.i.d. `μ`.

Formalized by `ProbabilityTheory.hoeffdingProj`, a definition declared in [MathlibExt/Probability/Statistics/UStatistic.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/UStatistic.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html#hoeffding-proj).

## Unbiasedness

For an i.i.d. sample of size `n ≥ m` and an integrable kernel, the
U-statistic has mean `E h(X₁, …, X_m)`.

Formalized by `ProbabilityTheory.integral_uStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/UStatistic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/UStatistic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html#integral-u-statistic).

## Hoeffding's variance formula

**Hoeffding's variance formula** (1948, §5): for an i.i.d. sample of size `n ≥ m`
and a symmetric square-integrable kernel `h` of degree `m`,
`Var U = C(n, m)⁻¹ ∑_{c=1}^{m} C(m, c) C(n - m, m - c) Var h_c`.

Formalized by `ProbabilityTheory.variance_uStatistic`, a theorem declared in [MathlibExt/Probability/Statistics/UStatistic.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/UStatistic.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html#variance-u-statistic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: U-statistics](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/u-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/nonparametric-survival/u-statistics)
