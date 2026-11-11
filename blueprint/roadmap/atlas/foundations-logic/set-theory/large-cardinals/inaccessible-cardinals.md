---
declaration: section
origin: cited
lean: MetaMathlibExt.IsWeaklyInaccessible, MetaMathlibExt.inaccessibleBelow, MetaMathlibExt.IsInaccessibleFixedPoint, Cardinal.IsInaccessible.beth_lt, MetaMathlibExt.Cardinal.IsInaccessible.aleph_lt, MetaMathlibExt.mk_inaccessibleBelow_le, MetaMathlibExt.exists_regular_between, MetaMathlibExt.IsWeaklyInaccessible.isInaccessible_of_gch
statement: formalized
proof: formalized
---

# Inaccessible cardinals

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html).

## Weakly inaccessible cardinal

A cardinal κ is *weakly inaccessible* if it is an uncountable, regular limit cardinal.

Formalized by `MetaMathlibExt.IsWeaklyInaccessible`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#weakly-inaccessible-cardinal).

## Set of inaccessible cardinals below a cardinal

InAccBelow κ is the set of all inaccessible cardinals below κ.

Formalized by `MetaMathlibExt.inaccessibleBelow`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#set-of-inaccessible-cardinals-below-a-ca).

## Inaccessible fixed point

A cardinal κ is an *inaccessible fixed point* if κ is inaccessible and the inaccessibles below κ
have order type κ (i.e. κ is the κ-th inaccessible).

Formalized by `MetaMathlibExt.IsInaccessibleFixedPoint`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#inaccessible-fixed-point).

## The beth hierarchy stays below an inaccessible cardinal

Below an inaccessible `κ`, the beth hierarchy stays below `κ`: `κ` is a beth
fixed point (`IsInaccessible.beth_ord`) and `beth` is strictly monotone.

## Sources

- Below an inaccessible κ, each ℶ_o with o < κ.ord lies below κ.

Formalized by `Cardinal.IsInaccessible.beth_lt`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#the-beth-hierarchy-stays-below-an-inacce).

## The aleph hierarchy stays below an inaccessible cardinal

Below an inaccessible `κ`, the aleph hierarchy stays below `κ`: same argument
via `IsInaccessible.aleph_ord`.

## Sources

- Below an inaccessible κ, each ℵ_o with o < κ.ord lies below κ.

Formalized by `MetaMathlibExt.Cardinal.IsInaccessible.aleph_lt`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#the-aleph-hierarchy-stays-below-an-inacc).

## At most $\kappa$ inaccessible cardinals lie below $\kappa$

There are at most `κ` inaccessibles below `κ`: the set injects into
`↥(Set.Iio κ.ord)`, which has size `lift κ`.  The `≤` half of the counting needed
for the Mahlo-implies-fixed-point benchmark item.

The `lift` is forced: the carrier lives in `Type (u+1)`, the same phenomenon as
the `lift` in `IsInaccessibleFixedPoint`.

## Sources

- There are at most κ inaccessible cardinals below κ.

Formalized by `MetaMathlibExt.mk_inaccessibleBelow_le`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#at-most-kappa-inaccessible-cardinals-lie).

## Regular cardinals are unbounded below an uncountable limit cardinal

Regular cardinals are unbounded below an uncountable limit cardinal `κ` (in
particular a weakly inaccessible one): above any `a < κ` sits
`succ (max a ℵ₀)`, regular by `isRegular_succ` and below `κ` since `κ` is a
limit.

## Sources

- Regular cardinals are unbounded below any uncountable limit cardinal.

Formalized by `MetaMathlibExt.exists_regular_between`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#regular-cardinals-are-unbounded-below-an).

## Under GCH, weakly inaccessible cardinals are inaccessible

Under (local) GCH, weakly inaccessible implies strongly inaccessible: for
infinite `μ < κ`, `2 ^ μ = succ μ < κ` by the limit property, and the finite
case is `power_lt_aleph0`.

`GCH` is spelled inline and localized below `κ`, following the
`singularCardinalsHypothesis_of_gch` precedent (Mathlib has no `GCH` identifier);
the `ℵ₀ ≤ μ` restriction is load-bearing for the same reason as there.

## Sources

- Under GCH below κ, a weakly inaccessible κ is inaccessible.

Formalized by `MetaMathlibExt.IsWeaklyInaccessible.isInaccessible_of_gch`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#under-gch-weakly-inaccessible-cardinals).

## Strong limit cardinals are closed under exponentiation

A strong limit `κ` is closed under cardinal exponentiation: `x ^ y ≤ 2 ^ (x * y)`
(via `cantor` and `power_mul`), and `x * y < κ` by `mul_lt_of_lt`.  No
infiniteness hypothesis is needed — it is automatic by `IsStrongLimit.aleph0_le`.

## Sources

- Below a strong limit κ, x < κ and y < κ imply x ^ y < κ.

Formalized by `Cardinal.IsStrongLimit.power_lt`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#strong-limit-cardinals-are-closed-under).

## Existence of an inaccessible with no inaccessibles below it

If any inaccessible exists, some inaccessible has no inaccessibles below it:
minimize over the initial ordinals of inaccessible cardinals
(`WellFounded.has_min`), and any member of `inaccessibleBelow` would give a
smaller one.

In particular the least inaccessible — if one exists — is neither Mahlo (see
`exists_isInaccessible_not_isMahlo` in `Mahlo.lean`) nor an inaccessible fixed
point (`not_isInaccessibleFixedPoint_of_inaccessibleBelow_eq_empty` above).

## Sources

- If any inaccessible cardinal exists, some inaccessible has no inaccessibles below it.

Formalized by `MetaMathlibExt.exists_isInaccessible_inaccessibleBelow_eq_empty`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#existence-of-an-inaccessible-with-no-ina).

## Weak power below a strong limit cardinal equals the cardinal

For `2 ≤ x < κ` with `κ` a strong limit, `x ^< κ = κ`: every smaller power is
below `κ` (`IsStrongLimit.power_lt`), while every `y < κ` sits below
`2 ^ y ≤ x ^< κ`.  No infiniteness hypothesis is needed — it is automatic by
`IsStrongLimit.aleph0_le`.

## Sources

- For 2 ≤ x < κ with κ a strong limit, x ^< κ = κ.

Formalized by `MetaMathlibExt.Cardinal.IsStrongLimit.powerlt_eq_self`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#weak-power-below-a-strong-limit-cardinal).

## Strong limits are unbounded below an inaccessible cardinal

Strong limits are unbounded below an inaccessible `κ`: above any `a < κ` sits
`ℶ_{a.ord + ω}`, a strong limit by `isStrongLimit_beth` since `a.ord + ω` is a
limit ordinal (`isSuccLimit_add`), and below `κ` since
`(a.ord + ω).card = a.ord.card + ℵ₀ < κ` (`add_lt_of_lt`).

## Sources

- Above any a < κ with κ inaccessible sits a strong limit cardinal below κ.

Formalized by `MetaMathlibExt.Cardinal.IsInaccessible.exists_isStrongLimit_between`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#strong-limits-are-unbounded-below-an-ina).

## Set of regular cardinals below a cardinal

The **regular cardinals below `κ`**, carried as initial ordinals — parallel to
`inaccessibleBelow`, and definitionally the stationary set in `IsWeaklyMahlo`.
Spelled with Mathlib's `Ordinal.IsInitial`.

## Sources

- regularBelow κ is the set of initial ordinals below κ whose cardinals are regular.

Formalized by `MetaMathlibExt.regularBelow`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#set-of-regular-cardinals-below-a-cardina).

## A regular beth fixed point is uncountable

A regular beth fixed point is uncountable: regularity gives `ℵ₀ ≤ κ`, and
`κ = ℵ₀` fails the fixed-point equation since `ℶ_ω > ℶ_0 = ℵ₀`.

## Sources

- A regular beth fixed point is uncountable.

Formalized by `MetaMathlibExt.aleph0_lt_of_isRegular_beth_ord`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#a-regular-beth-fixed-point-is-uncountabl).

## A regular beth fixed point is inaccessible

Converse to `IsInaccessible.beth_ord`: a regular beth fixed point is
inaccessible.  Uncountability is derived, not assumed
(`aleph0_lt_of_isRegular_beth_ord`); for `x < κ`,
`2 ^ x ≤ 2 ^ ℶ_{x.ord} = ℶ_{succ x.ord} < κ`, using that `κ.ord` is a limit
ordinal.

Regularity is genuinely needed — the first beth fixed point is singular — so
this does not promote a bare fixed point.

## Sources

- A regular beth fixed point is inaccessible.

Formalized by `MetaMathlibExt.Cardinal.IsInaccessible.of_isRegular_beth_ord`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#a-regular-beth-fixed-point-is-inaccessib).

## Inaccessible cardinals are the regular beth fixed points

`κ` is inaccessible iff it is regular and a beth fixed point (uncountability
is automatic by `aleph0_lt_of_isRegular_beth_ord`): this packages
`of_isRegular_beth_ord` with Mathlib's `IsInaccessible.beth_ord`.

## Sources

- κ is inaccessible if and only if κ is regular and a beth fixed point.

Formalized by `MetaMathlibExt.Cardinal.isInaccessible_iff_isRegular_beth_ord`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#inaccessible-cardinals-are-the-regular-b).

## Exactly $\kappa$ inaccessibles lie below an inaccessible fixed point

The fixed-point equation forces `#(inaccessibleBelow κ) = lift κ`
(`card_type`): the companion to the upper bound `mk_inaccessibleBelow_le`.

## Sources

- Below an inaccessible fixed point κ there are exactly κ inaccessible cardinals.

Formalized by `MetaMathlibExt.IsInaccessibleFixedPoint.mk_inaccessibleBelow`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#exactly-kappa-inaccessibles-lie-below-an).

## Inaccessibles are unbounded below an inaccessible fixed point

Inaccessibles below an inaccessible fixed point are unbounded: if they were
bounded by `a`, the set would inject into `Iic a.val`, hence have size at most
`lift (a.val + 1).card < lift κ` — contradicting `mk_inaccessibleBelow`.

## Sources

- Inaccessibles below an inaccessible fixed point are unbounded.

Formalized by `MetaMathlibExt.IsInaccessibleFixedPoint.exists_gt`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#inaccessibles-are-unbounded-below-an-ina).

## Limit cardinals are unbounded below a weakly inaccessible cardinal

Limit cardinals are unbounded below a weakly inaccessible `κ`: the sup of
the `ω`-chain `μ 0 = succ (max a ℵ₀)`, `μ (n+1) = succ (μ n)` stays below `κ`
(`sum_lt_of_isRegular`), exceeds `a`, and is a limit since every `x < σ`
lies below some `μ n` (`exists_lt_of_lt_ciSup`).

## Sources

- Above any a < κ with κ weakly inaccessible sits a limit cardinal below κ.

Formalized by `MetaMathlibExt.IsWeaklyInaccessible.exists_isSuccLimit_between`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#limit-cardinals-are-unbounded-below-a-we).

## Supremum of a bounded set of initial ordinals is initial

The sup of a bounded set of initial ordinals is initial: if
`σ.card.ord < σ` then some member exceeds `σ.card.ord`, trapping it strictly
between itself and its own initial ordinal.

## Sources

- The supremum of a bounded set of initial ordinals is initial.

Formalized by `MetaMathlibExt.sSup_initial_of_forall_initial`, a theorem declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Inaccessible.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html#supremum-of-a-bounded-set-of-initial-ord).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inaccessible cardinals](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/inaccessible-cardinals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/large-cardinals/inaccessible-cardinals)
