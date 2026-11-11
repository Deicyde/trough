---
declaration: def
origin: cited
lean: TauCeti.gradedLieHom
statement: formalized
---

# The graded Lie homomorphism of a continuous homomorphism `f : G →* H`

the graded maps
`TauCeti.gradedMap p f hf k` of all degrees, assembled into a homomorphism of graded Lie algebras
`⨁ k, gr_k(G) →ₗ⁅ZMod p⁆ ⨁ k, gr_k(H)`. Its value on homogeneous elements is
`TauCeti.gradedLieHom_of`.

```lean
TauCeti.gradedLieHom.{u, v} (p : ℕ) {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] {H : Type v} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (f : G →* H) (hf : Continuous ⇑f) :
  (DirectSum ℕ fun k => TauCeti.gradedPiece p G k) →ₗ⁅ZMod p⁆
    DirectSum ℕ fun k => TauCeti.gradedPiece p H k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobi identity](the-jacobi-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedLieHom`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.html#TauCeti.gradedLieHom).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedLieHom`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.html#TauCeti.gradedLieHom)
- [Source of `TauCeti.gradedLieHom` in TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.lean#L178)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
