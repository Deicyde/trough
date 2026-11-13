---
declaration: section
origin: cited
lean: CuspForm.norm, CuspForm.coe_norm_eq_coe_modularFormNorm, CuspForm.norm_eq_zero_iff, CongruenceSubgroup.Gamma0_two_index_eq_three, ModularForm.S2_Gamma0_one_eq_zero, ModularForm.S2_Gamma0_2_eq_zero, ModularForm.exists_mul_eq_mul_norm_of_forall_slash_mul_eq
statement: formalized
proof: formalized
---

# Weight-two cusp forms on Γ₀(2)

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html).

## Norm of a cusp form

The product norm of a cusp form: for `𝒢` of finite relative index in `ℋ`,
the product of the `ℋ / 𝒢`-translates of `f`, viewed as a cusp form on the
larger group `ℋ` at weight `k * [ℋ : 𝒢]`. This lifts Mathlib's
`ModularForm.norm` to cusp forms; the only new work is checking vanishing
at the cusps, which follows because each translate is a cusp form.

Formalized by `CuspForm.norm`, a definition declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#norm).

## Cusp form norm agrees with the modular form norm

The coercion of the norm of a cusp form is the norm of its coercion as a
modular form.

Formalized by `CuspForm.coe_norm_eq_coe_modularFormNorm`, a lemma declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#coe-norm-eq-coe-modular-form-norm).

## Norm of a cusp form vanishes only for the zero form

The norm of a cusp form vanishes if and only if the form itself vanishes:
the norm is a product of translates, and a translate of a nonzero form is
nonzero.

Formalized by `CuspForm.norm_eq_zero_iff`, a lemma declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#norm-eq-zero-iff).

## Γ₀(2) has index 3 in SL(2, ℤ)

The index of `Γ₀(2)` in `SL(2, ℤ)` is 3: the cosets are classified by
the first column mod 2, and there are three nonzero vectors in `(ZMod 2)²`.

Formalized by `CongruenceSubgroup.Gamma0_two_index_eq_three`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#gamma0-two-index-eq-three).

## No nonzero weight-two cusp forms of level one

Every weight-two cusp form on `Γ₀(1)` is zero: `Γ₀(1)` is the full
modular group, and the dimension formula gives rank zero below weight 12.

Formalized by `ModularForm.S2_Gamma0_one_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#s2-gamma0-one-eq-zero).

## No nonzero weight-two cusp forms on Γ₀(2)

Every weight-two cusp form on `Γ₀(2)` is zero. Take the norm of `f`
to `Γ₀(1)`: it has weight `2 * [Γ₀(1) : Γ₀(2)] = 6`, hence vanishes by the
level-one dimension formula, and the norm vanishes only when `f` does.

Formalized by `ModularForm.S2_Gamma0_2_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/CuspFormGamma0Two.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#s2-gamma0-2-eq-zero).

## Norm trick for modular forms

The norm trick: two modular forms satisfying a commutation relation under
the slash action of `ℋ` give rise to a modular form `Φ` of level `ℋ` with
`Φ * G = F * norm ℋ G`.

Formalized by `ModularForm.exists_mul_eq_mul_norm_of_forall_slash_mul_eq`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/NormTrick.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/NormTrick.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html#exists-mul-eq-mul-norm-of-forall-slash-m).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weight-two cusp forms on Γ₀(2)](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/weight-two-cusp-forms-on-2)
