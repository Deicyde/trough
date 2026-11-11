---
declaration: section
origin: cited
lean: Ideal.mem_inertia_of_forall_smul_sub_pow_mem, AlgHom.IsArithFrobAt.pow_apply_sub_pow_mem, IsArithFrobAt.pow_smul_sub_pow_mem, IsArithFrobAt.comap, IsArithFrobAt.pow_eq_of_forall_smul_sub_pow_mem_of_inertia_eq_bot, IsArithFrobAt.eq_comap_of_forall_smul_sub_pow_mem_of_inertia_eq_bot, Ideal.natCard_quotient_under_eq_pow_inertiaDeg, IsArithFrobAt.tower_eq_of_inertia_eq_bot
statement: formalized
proof: formalized
---

# Arithmetic Frobenius in towers and restrictions

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html).

## Ideal

## Elements with the same powered congruence differ by inertia

Two elements satisfying the same powered congruence differ by an
element of the inertia subgroup of `Q`.

Formalized by `Ideal.mem_inertia_of_forall_smul_sub_pow_mem`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#mem-inertia-of-forall-smul-sub-pow-mem).

## Powers of a Frobenius map satisfy the powered congruence

Powers of an arithmetic Frobenius map satisfy the powered congruence:
if `φ x - x ^ q ∈ Q` for all `x`, then `(φ ^ f) x - x ^ q ^ f ∈ Q`.

Formalized by `AlgHom.IsArithFrobAt.pow_apply_sub_pow_mem`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#pow-apply-sub-pow-mem).

## Powers of a Frobenius element satisfy the powered congruence

Powers of an arithmetic Frobenius element satisfy the powered
congruence: if `σ • x - x ^ q ∈ Q` for all `x`, with
`q = Nat.card (R ⧸ Q.under R)`, then
`(σ ^ f) • x - x ^ q ^ f ∈ Q`.

Formalized by `IsArithFrobAt.pow_smul_sub_pow_mem`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#pow-smul-sub-pow-mem).

## Restriction of a Frobenius element along a compatible pair

A Frobenius congruence restricts along a compatible pair: if
`ι : C →ₐ[R] B` and `ρ : G →* H` satisfy `ι (ρ g • c) = g • ι c`, and `σ`
is a Frobenius at `Q`, then `ρ σ` is a Frobenius at `Q.comap ι`.

Formalized by `IsArithFrobAt.comap`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#comap).

## Uniqueness of Frobenius powers with trivial inertia

If `σ` is a Frobenius at `Q` and `τ` satisfies the powered congruence
with exponent `q ^ f`, then `σ ^ f = τ` when the inertia subgroup of `Q` is
trivial. This is a uniqueness helper for an already supplied powered
congruence. The actual tower theorem below derives that congruence from the
Frobenius premise over the intermediate ring and its residue cardinality.

Formalized by `IsArithFrobAt.pow_eq_of_forall_smul_sub_pow_mem_of_inertia_eq_bot`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#pow-eq-of-forall-smul-sub-pow-mem-of-ine).

## Restriction of Frobenius equals Frobenius with trivial inertia

If `σ` is a Frobenius at `Q` and `τ` satisfies the Frobenius congruence
at `Q.comap ι`, then `ρ σ = τ` when the inertia subgroup of `Q.comap ι` is
trivial. This is the equality form of the restriction statement of
Proposition 7.22 under its unramified hypothesis.

Formalized by `IsArithFrobAt.eq_comap_of_forall_smul_sub_pow_mem_of_inertia_eq_bot`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#eq-comap-of-forall-smul-sub-pow-mem-of-i).

## Intermediate residue cardinality as a power of the base residue cardinality

In a finite ring tower `R → T → B`, the intermediate prime residue quotient
has cardinality equal to the base residue cardinality raised to its canonical
inertia degree. The cardinality theorem is Mathlib's `cardQuot_pow_inertiaDeg`.

Formalized by `Ideal.natCard_quotient_under_eq_pow_inertiaDeg`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#nat-card-quotient-under-eq-pow-inertia-d).

## Frobenius in a tower is a power of the base Frobenius

In a finite ring tower `R → T → B`, the Frobenius over `T`, embedded into
an action over `R`, equals the Frobenius over `R` raised to the intermediate
residue degree when the inertia subgroup is trivial. Only `H` must fix `T`.

Formalized by `IsArithFrobAt.tower_eq_of_inertia_eq_bot`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#tower-eq-of-inertia-eq-bot).

## Frobenius tower equality for algebra automorphisms

For algebra automorphisms in a finite ring tower, the inclusion of the
intermediate Frobenius is the canonical `AlgEquiv.restrictScalars`.

Formalized by `IsArithFrobAt.tower_eq_of_inertia_eq_bot_algEquiv`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#tower-eq-of-inertia-eq-bot-alg-equiv).

## Frobenius tower equality for an intermediate field

The tower equality for the source's intermediate field `E ⊂ L`.
Here `K` is the fraction field of the base ring `R`, `T` is the integral
closure of `R` in `E`, and `B` is its integral closure in `L`. In the
number-field application these are the three rings of integers. The
intermediate action is `E.fixingSubgroup`; the whole `Gal(L/K)` need not fix `T`.

Formalized by `IsArithFrobAt.tower_eq_of_inertia_eq_bot_fixingSubgroup`, a theorem declared in [MathlibExt/RingTheory/Frobenius/TowerRestriction.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Frobenius/TowerRestriction.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html#tower-eq-of-inertia-eq-bot-fixing-subgro).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic Frobenius in towers and restrictions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/frobenius-elements/arithmetic-frobenius-in-towers-and-restrictions)
