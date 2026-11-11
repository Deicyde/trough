---
declaration: theorem
origin: cited
lean: TauCeti.mayerVietoris_induction
statement: formalized
proof: formalized
---

# Mayer–Vietoris induction

A property of opens in a second-countable locally compact
Hausdorff space holds on every open if it holds on an intersection-stable basis and on the
empty set, is preserved by binary unions when it holds on the intersection, and is preserved
by countable disjoint unions. No hypothesis about increasing unions is required.

```lean
TauCeti.mayerVietoris_induction.{u_1} {X : Type u_1} [TopologicalSpace X] [T2Space X]
  [LocallyCompactSpace X] [SecondCountableTopology X] (P : TopologicalSpace.Opens X → Prop)
  (B : Set (TopologicalSpace.Opens X)) (hB : TopologicalSpace.Opens.IsBasis B)
  (hB_inf : ∀ U ∈ B, ∀ V ∈ B, U ⊓ V ∈ B) (hbot : P ⊥) (hbase : ∀ U ∈ B, P U)
  (hsup : ∀ (U V : TopologicalSpace.Opens X), P U → P V → P (U ⊓ V) → P (U ⊔ V))
  (hdisjoint :
    ∀ (s : ℕ → TopologicalSpace.Opens X),
      (∀ (i j : ℕ), i ≠ j → Disjoint (s i) (s j)) → (∀ (n : ℕ), P (s n)) → P (⨆ n, s n))
  (U : TopologicalSpace.Opens X) : P U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mayerVietoris_induction`](https://taucetiproject.org/docs/TauCeti/Topology/MayerVietoris.html#TauCeti.mayerVietoris_induction).

## Sources

- [Tau Ceti documentation: `TauCeti.mayerVietoris_induction`](https://taucetiproject.org/docs/TauCeti/Topology/MayerVietoris.html#TauCeti.mayerVietoris_induction)
- [Source of `TauCeti.mayerVietoris_induction` in TauCeti/Topology/MayerVietoris.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/MayerVietoris.lean#L101)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
