---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.ExpressionNoise.intrinsicNoiseSq, MathlibExt.Biology.Dynamics.ExpressionNoise.extrinsicNoiseSq, MathlibExt.Biology.Dynamics.ExpressionNoise.totalNoiseSq, MathlibExt.Biology.Dynamics.ExpressionNoise.totalNoiseSq_eq_add, MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair, MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.integral_eq, MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.covariance_eq_variance_condExp, MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.integral_sub_sq_div_two_eq
statement: formalized
proof: formalized
---

# Intrinsic and extrinsic gene expression noise

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html).

## Intrinsic noise strength

Two-reporter intrinsic noise strength `η_int² = ⟨(X - Y)²⟩ / (2 ⟨X⟩⟨Y⟩)`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.intrinsicNoiseSq`, a definition declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#intrinsic-noise-sq).

## Extrinsic noise strength

Two-reporter extrinsic noise strength `η_ext² = (⟨X Y⟩ - ⟨X⟩⟨Y⟩) / (⟨X⟩⟨Y⟩)`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.extrinsicNoiseSq`, a definition declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#extrinsic-noise-sq).

## Total noise strength

Two-reporter total noise strength `η_tot² = (⟨X² + Y²⟩ / 2 - ⟨X⟩⟨Y⟩) / (⟨X⟩⟨Y⟩)`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.totalNoiseSq`, a definition declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#total-noise-sq).

## Two-reporter decomposition

**Two-reporter decomposition** (Swain et al. 2002; Elowitz et al. 2002): for any
square-integrable reporters, `η_tot² = η_int² + η_ext²`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.totalNoiseSq_eq_add`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#total-noise-sq-eq-add).

## Identical reporter pair

Two reporters of the same gene given the extrinsic σ-algebra `m`: equal conditional means,
equal conditional second moments, and conditionally uncorrelated. Conditional independence with
identical conditional laws given `m` implies these three conditions.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair`, a structure declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#is-identical-reporter-pair).

## Identical reporters have equal means

Identical reporters have the same mean.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.integral_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#integral-eq).

## Covariance of identical reporters equals extrinsic variance

For identical reporters the covariance is the extrinsic variance:
`Cov(X, Y) = Var(E[X | m])`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.covariance_eq_variance_condExp`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#covariance-eq-variance-cond-exp).

## Half mean squared reporter difference equals intrinsic variance

For identical reporters half the mean squared difference is the intrinsic variance:
`⟨(X - Y)²⟩ / 2 = ⟨Var(X | m)⟩`.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.integral_sub_sq_div_two_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#integral-sub-sq-div-two-eq).

## Two-reporter formula for extrinsic noise

The two-reporter extrinsic noise is `Var(E[X | m]) / ⟨X⟩²` (Swain et al. Eq. 8).

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.extrinsicNoiseSq_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#extrinsic-noise-sq-eq).

## Two-reporter formula for intrinsic noise

The two-reporter intrinsic noise is `⟨Var(X | m)⟩ / ⟨X⟩²` (Swain et al. Eq. 8).

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.intrinsicNoiseSq_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#intrinsic-noise-sq-eq).

## Total noise splits into intrinsic and extrinsic parts

The two-reporter total noise is `Var(X) / ⟨X⟩²`, and it splits into the intrinsic and
extrinsic parts by the law of total variance.

Formalized by `MathlibExt.Biology.Dynamics.ExpressionNoise.IsIdenticalReporterPair.totalNoiseSq_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/ExpressionNoise.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/ExpressionNoise.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html#total-noise-sq-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intrinsic and extrinsic gene expression noise](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/systems-biology/intrinsic-and-extrinsic-gene-expression-noise)
