---
declaration: def
origin: cited
lean: Module.Grassmannian.schemeSchubertLocus
statement: formalized
---

# Module.Grassmannian.schemeSchubertLocus

The ideal sheaf of the **Schubert rank locus** of zero-based pivot positions
`p : Fin r → Fin n` relative to the flag `F_j = b.flag j` of a basis `b` of `M`: the
rank-condition subscheme of `G(k, M)` over which `F_{p i + 1}` maps to the universal quotient with
rank at most `p i - i`, for every `i`. Over a field and for strictly increasing `p`, its points are
the `N` with `dim (N ⊓ F_{p i + 1}) ≥ i + 1` for all `i`
(`Module.Grassmannian.schemeSchubertLocus_le_ker_toSchemeHom_iff_of_field`).

```lean
Module.Grassmannian.schemeSchubertLocus.{u} {R : Type u} [CommRing R] {M : Type u} [AddCommGroup M]
  [_root_.Module R M] (k : ℕ) {n r : ℕ} (b : Module.Basis (Fin n) R M) (p : Fin r → Fin n) :
  (Module.Grassmannian.scheme R M k).IdealSheafData
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Grassmannian.schemeSchubertLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Grassmannian/RankLocus.html#Module.Grassmannian.schemeSchubertLocus).

## Sources

- [Tau Ceti documentation: `Module.Grassmannian.schemeSchubertLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Grassmannian/RankLocus.html#Module.Grassmannian.schemeSchubertLocus)
- [Source of `Module.Grassmannian.schemeSchubertLocus` in TauCeti/AlgebraicGeometry/Grassmannian/RankLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Grassmannian/RankLocus.lean#L176)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
