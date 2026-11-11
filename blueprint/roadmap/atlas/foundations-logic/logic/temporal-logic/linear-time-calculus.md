---
declaration: section
origin: cited
lean: Cslib.Modal.LinearMuCalculus.LinearMuFormula, Cslib.Modal.LinearMuCalculus.LinearMuFormula.neg, Cslib.Modal.LinearMuCalculus.LinearMuFormula.neg_neg, Cslib.Modal.LinearMuCalculus.LinearMuFormula.ClosedAt, Cslib.Modal.LinearMuCalculus.LinearMuFormula.Closed, Cslib.Modal.LinearMuCalculus.LinearMuFormula.depth, Cslib.Modal.LinearMuCalculus.extendEnv, Cslib.Modal.LinearMuCalculus.sat
statement: formalized
proof: formalized
---

# Linear-time μ-calculus

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html).

## Formulas of the linear-time μ-calculus

Formulas of the linear-time μ-calculus over atoms `Atom`, with de Bruijn
variables for the fixed-point binders.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula`, an inductive type declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-formula).

## Dual negation of linear μ-calculus formulas

Meta-level negation, swapping each connective with its dual.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula.neg`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#neg).

## Negation of linear μ-calculus formulas is an involution

Negation is an involution.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula.neg_neg`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#neg-neg).

## Closedness of a μ-calculus formula at a binder depth

`φ` is closed at depth `d` when every free variable is below `d`
(de Bruijn): `var n` needs `n < d`, and binders increase the depth.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula.ClosedAt`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#closed-at).

## Closed linear μ-calculus formula

A formula with no free variables.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula.Closed`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#closed).

## Depth of a linear μ-calculus formula

The depth of a formula: the length of its longest root-to-leaf path, counting
each connective once.

Formalized by `Cslib.Modal.LinearMuCalculus.LinearMuFormula.depth`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#depth).

## Extending an environment under a binder

Extend an environment under a binder (de Bruijn).

Formalized by `Cslib.Modal.LinearMuCalculus.extendEnv`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#extend-env).

## Satisfaction of linear μ-calculus formulas

Satisfaction of a linear μ-calculus formula at a position of the word
`val`. `μ X. φ` is the least pre-fixed point of `S ↦ ⟦φ⟧[X ↦ S]`, stated
directly as an infimum over pre-fixed points; `ν X. φ` is the greatest
post-fixed point, stated as a supremum over post-fixed points.

Formalized by `Cslib.Modal.LinearMuCalculus.sat`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat).

## Satisfaction is monotone in the environment

Satisfaction is monotone in the environment.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_mono_env`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-mono-env).

## Satisfaction is monotone in the bound variable

Monotonicity in the bound variable's denotation.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_mono_extend`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-mono-extend).

## Least fixed point is a pre-fixed point

The least fixed point is a pre-fixed point.

Formalized by `Cslib.Modal.LinearMuCalculus.mu_pre_fixed`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#mu-pre-fixed).

## Least fixed point is a fixed point: lower inclusion

The least fixed point is a fixed point (the lower half).

Formalized by `Cslib.Modal.LinearMuCalculus.mu_le_fixed`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#mu-le-fixed).

## The μ unfolding

`μ X. φ ≡ φ[μ X. φ / X]`.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_mu_unfold`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-mu-unfold).

## Greatest fixed point is a post-fixed point

The greatest fixed point is a post-fixed point (the upper half).

Formalized by `Cslib.Modal.LinearMuCalculus.nu_post_fixed`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#nu-post-fixed).

## Greatest fixed point is a fixed point: upper inclusion

The greatest fixed point is a fixed point (the upper half).

Formalized by `Cslib.Modal.LinearMuCalculus.nu_le_post_fixed`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#nu-le-post-fixed).

## The ν unfolding

`ν X. φ ≡ φ[ν X. φ / X]`.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_nu_unfold`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-nu-unfold).

## Park induction

To show `μ X. φ ≤ P`, it suffices that `P` is a
pre-fixed point.

Formalized by `Cslib.Modal.LinearMuCalculus.mu_induction`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#mu-induction).

## Coinduction

Every post-fixed point is below `ν X. φ`.

Formalized by `Cslib.Modal.LinearMuCalculus.nu_coinduction`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#nu-coinduction).

## The μ operator as a monotone operator on predicates

The μ operator as a monotone operator on predicates.

Formalized by `Cslib.Modal.LinearMuCalculus.muOp`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#mu-op).

## μ-formulas denote least fixed points

The μ fixed point is Mathlib's least fixed point of the operator.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_mu_eq_lfp`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-mu-eq-lfp).

## ν-formulas denote greatest fixed points

The ν fixed point is Mathlib's greatest fixed point of the operator.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_nu_eq_gfp`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-nu-eq-gfp).

## Closed formulas do not depend on the environment

A closed formula does not depend on the environment: environments
agreeing below the depth give the same denotation.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_closed_env`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-closed-env).

## Complementing an environment commutes with extension

Complementing an environment commutes with extending it.

Formalized by `Cslib.Modal.LinearMuCalculus.extendEnv_compl`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#extend-env-compl).

## Double complement of a predicate

Complementing a predicate twice returns it.

Formalized by `Cslib.Modal.LinearMuCalculus.compl_compl`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#compl-compl).

## Duality

`⟦¬φ⟧ = (⟦φ⟧)ᶜ` when the environment is complemented.

Formalized by `Cslib.Modal.LinearMuCalculus.sat_neg`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#sat-neg).

## Eventually operator in the linear μ-calculus

`F p`: `p` holds at some future position.

Formalized by `Cslib.Modal.LinearMuCalculus.F`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#f).

## Always operator in the linear μ-calculus

`G p`: `p` holds at every future position.

Formalized by `Cslib.Modal.LinearMuCalculus.G`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#g).

## The linear μ-calculus `F` is eventuality

**The linear μ-calculus `F` is eventuality.**

Formalized by `Cslib.Modal.LinearMuCalculus.F_iff`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#f-iff).

## The linear μ-calculus `G` is universality over the future

**The linear μ-calculus `G` is universality over the future.**

Formalized by `Cslib.Modal.LinearMuCalculus.G_iff`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#g-iff).

## Cantor-pairing code of linear μ-calculus formulas

An injective encoding of linear μ-calculus formulas over `ℕ` atoms as
natural numbers, via the Cantor pairing function `Nat.pair`. This is a Nat
code only, not a complexity input encoding: repeated pairing squares the
code at every unary connective, so the binary length of the code of
`next^d (atom 0)` doubles at each `next` and is exponential in `d`.
Complexity statements use `linearMuTokens` / `linearMuDecodeList` instead.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuCode`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-code).

## Injectivity of the linear μ-calculus code

The encoding is injective.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuCode_injective`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-code-injective).

## Fuelled decoding of linear μ-calculus codes

Fuelled decoding of a `linearMuCode` number back to a formula. The fuel bounds
the recursion depth; `linearMuDecode` supplies fuel `c + 1`, which exceeds every
formula's depth (see `linearDepth_le_code`).

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecodeFuel`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 789](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L789). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode-fuel).

## Decoding linear μ-calculus codes

Decode a `linearMuCode` number back to the formula it encodes.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecode`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode).

## Formula depth is bounded by its code

A formula's depth is at most its code: pairing dominates each component
(`Nat.add_le_pair`).

Formalized by `Cslib.Modal.LinearMuCalculus.linearDepth_le_code`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 821](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L821). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-depth-le-code).

## Fuelled decoding inverts encoding

Decoding inverts encoding, with enough fuel.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecodeFuel_linearMuCode`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 876](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L876). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode-fuel-linear-mu-code).

## Decoding inverts the linear μ-calculus encoding

Decoding inverts encoding.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecode_linearMuCode`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 945](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L945). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode-linear-mu-code).

## Token-list encoding of linear μ-calculus formulas

A polynomial-size token-list encoding of linear μ-calculus formulas over
`ℕ` atoms, used for the complexity statements in `WantedExt`. Each connective
contributes one tag token (`Nat.pair` of a small tag with `0`), and each atom
or variable contributes one token `Nat.pair tag value`, whose binary size is
`O(log value)`. The canonical bitstring encoding of a `List ℕ` delimits each
token, so the bitstring for a formula has length linear in the number of
connectives plus the total binary size of its atoms: `next^d (atom 0)` is
encoded by exactly `d + 1` tokens, unlike its Cantor-paired `linearMuCode`,
whose binary length is exponential in `d`.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuTokens`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 958](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L958). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-tokens).

## Fuelled parser for linear μ-calculus token lists

Fuelled parsing of a `linearMuTokens` token list back to a formula,
returning the formula and the unconsumed suffix. The fuel bounds the
recursion depth; `linearMuDecodeList` supplies fuel `l.length + 1`, which
exceeds the token length of every formula encoded in `l`.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuParseFuel`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 974](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L974). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-parse-fuel).

## Decoding a linear μ-calculus token list to a formula

Decode a `linearMuTokens` token list back to the formula it encodes,
rejecting trailing tokens.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecodeList`, a definition declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 1016](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L1016). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode-list).

## Fuelled parsing inverts linear μ-calculus token encoding

Parsing inverts token encoding, with enough fuel.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuParseFuel_tokens`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 1022](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L1022). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-parse-fuel-tokens).

## Token-list decoding inverts linear μ-calculus token encoding

Decoding inverts token encoding.

Formalized by `Cslib.Modal.LinearMuCalculus.linearMuDecodeList_tokens`, a theorem declared in [CSLibExt/Logics/Modal/LinearMuCalculus.lean, line 1105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/LinearMuCalculus.lean#L1105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html#linear-mu-decode-list-tokens).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear-time μ-calculus](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-time-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/temporal-logic/linear-time-calculus)
