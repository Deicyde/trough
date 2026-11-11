---
declaration: theorem
origin: cited
lean: TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod
statement: formalized
proof: formalized
---

# Strøm's product theorem

if closed subsets `A ⊆ X` and `B ⊆ Y` have the homotopy
extension property, then so does `A × Y ∪ X × B ⊆ X × Y`.

```lean
TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] {A : Set X} {B : Set Y}
  (hA : TauCeti.HasHomotopyExtensionProperty A) (hA' : IsClosed A)
  (hB : TauCeti.HasHomotopyExtensionProperty B) (hB' : IsClosed B) :
  TauCeti.HasHomotopyExtensionProperty (A ×ˢ Set.univ ∪ Set.univ ×ˢ B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Strøm's theorem](strms-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Extension/Prod.html#TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod).

## Sources

- [Tau Ceti documentation: `TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Extension/Prod.html#TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod)
- [Source of `TauCeti.HasHomotopyExtensionProperty.prod_univ_union_univ_prod` in TauCeti/Topology/Homotopy/Extension/Prod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Homotopy/Extension/Prod.lean#L56)
