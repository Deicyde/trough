---
declaration: theorem
origin: cited
lean: TauCeti.curry_le_residual, TauCeti.eventually_eventually_left_of_mem_residual, TauCeti.eventually_eventually_right_of_mem_residual
statement: formalized
proof: formalized
---

# One half of the Kuratowski–Ulam theorem

If `Y` is second countable, every comeagre subset
of `X × Y` has comeagre sections `(x, ·) ⁻¹' s` over a comeagre set of `x`.

```lean
TauCeti.curry_le_residual.{u_1, u_2} {X : Type u_1} {Y : Type u_2} [TopologicalSpace X]
  [TopologicalSpace Y] [SecondCountableTopology Y] :
  (residual X).curry (residual Y) ≤ residual (X × Y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.curry_le_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#TauCeti.curry_le_residual).

## Other forms

**One half of the Kuratowski–Ulam theorem.** Formalized in Tau Ceti as [`TauCeti.eventually_eventually_left_of_mem_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#TauCeti.eventually_eventually_left_of_mem_residual).

```lean
TauCeti.eventually_eventually_left_of_mem_residual.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology Y] {s : Set (X × Y)}
  (hs : s ∈ residual (X × Y)) : ∀ᶠ (x : X) in residual X, ∀ᶠ (y : Y) in residual Y, (x, y) ∈ s
```

**One half of the Kuratowski–Ulam theorem.** Formalized in Tau Ceti as [`TauCeti.eventually_eventually_right_of_mem_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#TauCeti.eventually_eventually_right_of_mem_residual).

```lean
TauCeti.eventually_eventually_right_of_mem_residual.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [TopologicalSpace Y] [SecondCountableTopology X] {s : Set (X × Y)}
  (hs : s ∈ residual (X × Y)) : ∀ᶠ (y : Y) in residual Y, ∀ᶠ (x : X) in residual X, (x, y) ∈ s
```

## Sources

- [Tau Ceti documentation: `TauCeti.curry_le_residual`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/KuratowskiUlam.html#TauCeti.curry_le_residual)
- [Source of `TauCeti.curry_le_residual` in TauCeti/Topology/Baire/KuratowskiUlam.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Baire/KuratowskiUlam.lean#L101)
