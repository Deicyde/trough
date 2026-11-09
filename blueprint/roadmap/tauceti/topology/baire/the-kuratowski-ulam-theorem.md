---
declaration: theorem
origin: cited
lean: BaireMeasurableSet.eventually_eventually_left_iff_mem_residual, BaireMeasurableSet.eventually_eventually_right_iff_mem_residual, BaireMeasurableSet.eventually_isMeagre_curry_left_iff_isMeagre, BaireMeasurableSet.eventually_isMeagre_curry_right_iff_isMeagre
statement: formalized
proof: formalized
---

# The Kuratowski–Ulam theorem

If `Y` is second countable, a set `s` with the Baire property
in `X × Y` is comeagre if and only if comeagrely many sections `(x, ·) ⁻¹' s` are comeagre, that
is, if and only if it belongs to the curried residual filter `(residual X).curry (residual Y)`.

```lean
BaireMeasurableSet.eventually_eventually_left_iff_mem_residual.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology Y]
  {s : Set (X × Y)} (hs : BaireMeasurableSet s) :
  (∀ᶠ (x : X) in residual X, ∀ᶠ (y : Y) in residual Y, (x, y) ∈ s) ↔ s ∈ residual (X × Y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [One half of the Kuratowski–Ulam theorem](one-half-of-the-kuratowski-ulam-theorem.md)

## Lean

Formalized in Tau Ceti as [`BaireMeasurableSet.eventually_eventually_left_iff_mem_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#BaireMeasurableSet.eventually_eventually_left_iff_mem_residual).

## Other forms

**The Kuratowski–Ulam theorem, right-hand form.** Formalized in Tau Ceti as [`BaireMeasurableSet.eventually_eventually_right_iff_mem_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#BaireMeasurableSet.eventually_eventually_right_iff_mem_residual).

```lean
BaireMeasurableSet.eventually_eventually_right_iff_mem_residual.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology X]
  {s : Set (X × Y)} (hs : BaireMeasurableSet s) :
  (∀ᶠ (y : Y) in residual Y, ∀ᶠ (x : X) in residual X, (x, y) ∈ s) ↔ s ∈ residual (X × Y)
```

**The Kuratowski–Ulam theorem, meagre form.** Formalized in Tau Ceti as [`BaireMeasurableSet.eventually_isMeagre_curry_left_iff_isMeagre`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#BaireMeasurableSet.eventually_isMeagre_curry_left_iff_isMeagre).

```lean
BaireMeasurableSet.eventually_isMeagre_curry_left_iff_isMeagre.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology Y]
  {s : Set (X × Y)} (hs : BaireMeasurableSet s) :
  (∀ᶠ (x : X) in residual X, IsMeagre ((fun x_1 => (x, x_1)) ⁻¹' s)) ↔ IsMeagre s
```

**The Kuratowski–Ulam theorem, right-hand meagre form.** Formalized in Tau Ceti as [`BaireMeasurableSet.eventually_isMeagre_curry_right_iff_isMeagre`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#BaireMeasurableSet.eventually_isMeagre_curry_right_iff_isMeagre).

```lean
BaireMeasurableSet.eventually_isMeagre_curry_right_iff_isMeagre.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology X]
  {s : Set (X × Y)} (hs : BaireMeasurableSet s) :
  (∀ᶠ (y : Y) in residual Y, IsMeagre ((fun x => (x, y)) ⁻¹' s)) ↔ IsMeagre s
```

## Sources

- [Tau Ceti documentation: `BaireMeasurableSet.eventually_eventually_left_iff_mem_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#BaireMeasurableSet.eventually_eventually_left_iff_mem_residual)
- [Source of `BaireMeasurableSet.eventually_eventually_left_iff_mem_residual` in TauCeti/Topology/Baire/KuratowskiUlam.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Baire/KuratowskiUlam.lean#L195)
