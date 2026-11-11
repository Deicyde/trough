---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.field, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.output, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.HasPerfectAdaptation, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.HasIntegralFeedback, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.dcGain, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.hasPerfectAdaptation_of_hasIntegralFeedback, MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.field_eq_zero_iff
statement: formalized
proof: formalized
---

# Integral feedback and perfect adaptation

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html).

## Integral Feedback

## Single-input single-output linear time-invariant system

A single-input single-output linear time-invariant system `ẋ = A x + u b`,
`y = c ⬝ x + d u` with state space `n → ℝ`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem`, a structure declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#linear-system).

## Vector field of a linear time-invariant system

The vector field `A x + u b` at state `x` and input `u`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.field`, a definition declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#field).

## Output of a linear time-invariant system

The output `c ⬝ x + d u`, measured from its adapted value.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.output`, a definition declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#output).

## Perfect adaptation

For every constant input `u`, the output vanishes at every
equilibrium.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.HasPerfectAdaptation`, a definition declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-perfect-adaptation).

## Integral feedback

A linear functional `z = k ⬝ x` of the state integrates the output,
`ż = k ⬝ (A x + u b) = y`, for every state and input.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.HasIntegralFeedback`, a definition declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-integral-feedback).

## Steady-state (DC) gain of a linear system

The steady-state (DC) gain `d - c ⬝ A⁻¹ b`; for nonsingular `A` the output at the
equilibrium for input `u` is `dcGain * u`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.dcGain`, a definition declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#dc-gain).

## Integral feedback implies perfect adaptation

Integral feedback implies perfect adaptation.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.hasPerfectAdaptation_of_hasIntegralFeedback`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-perfect-adaptation-of-has-integral-f).

## Unique equilibrium of a nonsingular linear system

For nonsingular `A`, the unique equilibrium for input `u` is `x = -u • A⁻¹ b`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.field_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#field-eq-zero-iff).

## Output at equilibrium equals DC gain times input

For nonsingular `A`, the output at the equilibrium for input `u` is `dcGain * u`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.output_equilibrium`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#output-equilibrium).

## Perfect adaptation iff the DC gain vanishes

For nonsingular `A`, perfect adaptation holds iff the steady-state gain vanishes.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.hasPerfectAdaptation_iff_dcGain_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-perfect-adaptation-iff-dc-gain-eq-ze).

## Integral feedback is necessary

**Integral feedback is necessary** (linear systems with nonsingular `A`): perfect
adaptation holds iff some linear functional of the state integrates the output; one such
functional is `k = c A⁻¹`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.hasIntegralFeedback_iff_hasPerfectAdaptation`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-integral-feedback-iff-has-perfect-ad).

## Integral-feedback functional is the time integral of the output

Along a trajectory `ẋ(t) = A x(t) + u(t) b`, the functional `k ⬝ x(t)` of an
integral-feedback system has derivative `y(t) = c ⬝ x(t) + d u(t)`: it is the time integral of
the output.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.LinearSystem.hasDerivAt_integral`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#has-deriv-at-integral).

## Integral feedback gives robust perfect adaptation

**Integral feedback gives robust perfect adaptation** (nonlinear form). Let `F p` be the
vector field and `y p` the output of a system with parameters `p`, and let `z` be a
differentiable state function with derivative `z' x` satisfying
`z' x (F p x) = y p x` for all `p`, `x` (so `ż = y` along every trajectory, for
every parameter). Then the output vanishes at every equilibrium of every `F p`.

Formalized by `MathlibExt.Biology.Dynamics.IntegralFeedback.output_eq_zero_of_integral_feedback`, a theorem declared in [MathlibExt/Biology/Dynamics/IntegralFeedback.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/IntegralFeedback.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html#output-eq-zero-of-integral-feedback).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral feedback and perfect adaptation](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/systems-biology/integral-feedback-and-perfect-adaptation)
