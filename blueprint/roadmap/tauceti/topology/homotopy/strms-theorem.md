---
declaration: def
origin: cited
lean: TauCeti.NDRPair.ofRetraction
statement: formalized
---

# Strøm's theorem

A retraction `r` of the cylinder `I × X` onto `{0} × X ∪ I × A`, for a
closed subset `A`, gives NDR data for `A`: the deformation is the second coordinate of `r`, and
the control function is `x ↦ ⨆ t, t - (r (t, x)).1`, the largest amount by which `r` lowers a
point of the cylinder over `x`.

```lean
TauCeti.NDRPair.ofRetraction.{u} {X : Type u} [TopologicalSpace X] {A : Set X}
  {r : C(↑unitInterval × X, ↑unitInterval × X)}
  (hr : ∀ (p : ↑unitInterval × X), r p ∈ TauCeti.cylinderExtensionDomain A)
  (hr' : ∀ p ∈ TauCeti.cylinderExtensionDomain A, r p = p) (hA : IsClosed A) : TauCeti.NDRPair A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NDRPair.ofRetraction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Extension/NDRPair.html#TauCeti.NDRPair.ofRetraction).

## Sources

- [Tau Ceti documentation: `TauCeti.NDRPair.ofRetraction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Extension/NDRPair.html#TauCeti.NDRPair.ofRetraction)
- [Source of `TauCeti.NDRPair.ofRetraction` in TauCeti/Topology/Homotopy/Extension/NDRPair.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/Extension/NDRPair.lean#L315)
