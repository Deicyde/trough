---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv
statement: formalized
proof: formalized
---

# Lang's equation on the weight torus of the Geck carrier

Over a ring of characteristic `p`
whose units are divisible, for instance an algebraically closed field, if `φ` is a character map
of an endomorphism `F` with `φ ^ n = p ^ r • 1` for some `r > 0`, then every point of the weight
torus is `T u * (F (T u))⁻¹` for some `u`.

```lean
TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv.{v} (t : TauCeti.DynkinType)
  (ht : t.Valid) {K : Type v} [CommRing K] [RootableBy Kˣ ℕ] (p : ℕ) [CharP K p]
  {F : ↥(t.geckPoints ht K) →* ↥(t.geckPoints ht K)} {φ : Module.End ℤ (Fin t.rank → ℤ)}
  (hF : TauCeti.IsCharacterMap (t.geckWeightTorusPoints ht K) F φ) {n r : ℕ} (hr : 0 < r)
  (hφ : φ ^ n = p ^ r • 1) (s : Fin t.rank → Kˣ) :
  ∃ u,
    (t.geckWeightTorusPoints ht K) s =
      (t.geckWeightTorusPoints ht K) u * (F ((t.geckWeightTorusPoints ht K) u))⁻¹
```

## Depends on

- [`φ` is a character map of `F` on the torus `T`](is-a-character-map-of-f-on-the-torus-t.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/GeckLattice/CharacterMap.html#TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/GeckLattice/CharacterMap.html#TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv)
- [Source of `TauCeti.DynkinType.exists_geckWeightTorusPoints_eq_mul_inv` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/GeckLattice/CharacterMap.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/GeckLattice/CharacterMap.lean#L80)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
