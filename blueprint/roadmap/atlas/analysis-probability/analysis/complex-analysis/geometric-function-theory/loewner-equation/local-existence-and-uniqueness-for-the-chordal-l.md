---
declaration: section
origin: cited
lean: StatMech.SLE.picard_exists_ball, StatMech.SLE.picard_exists_ball_family_lipschitz, StatMech.SLE.loewner_local_existence, StatMech.SLE.loewner_local_existsUnique
statement: formalized
proof: formalized
---

# Local existence and uniqueness for the chordal Loewner equation

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html).

## Picard–Lindelöf theorem with solutions confined to a ball

Picard–Lindelöf with the solution confined to `closedBall x₀ a`: a strengthening of Mathlib's
`IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt₀` by the bound
`α t ∈ closedBall x₀ a` for all `t`.

Formalized by `StatMech.SLE.picard_exists_ball`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html#picard-exists-ball).

## Lipschitz Picard–Lindelöf flow confined to a ball

Picard–Lindelöf local flow, Lipschitz in the initial point, with every trajectory in
`closedBall x₀ a`: a strengthening of Mathlib's
`IsPicardLindelof.exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith` by the ball
bound.

Formalized by `StatMech.SLE.picard_exists_ball_family_lipschitz`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html#picard-exists-ball-family-lipschitz).

## Local existence for the chordal Loewner equation

For continuous `W` and `Im z > 0` there
are `ε > 0` and `g` with `g 0 = z`, `ġ(t) = 2 / (g(t) - W_t)` on `[0, ε]` (one-sided derivatives
at the endpoints), and `g(t) ∈ ℍ` on `[0, ε]` (Lawler 2005, Chapter 4).

Formalized by `StatMech.SLE.loewner_local_existence`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html#loewner-local-existence).

## Local existence and uniqueness for the chordal Loewner equation

Local existence and uniqueness for the chordal Loewner equation: the solution from
`loewner_local_existence` is the unique continuous solution on `[0, ε]` with right derivatives on
`[0, ε)` that stays in `ℍ`.

Formalized by `StatMech.SLE.loewner_local_existsUnique`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerExistence.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html#loewner-local-exists-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local existence and uniqueness for the chordal Loewner equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/local-existence-and-uniqueness-for-the-chordal-l)
