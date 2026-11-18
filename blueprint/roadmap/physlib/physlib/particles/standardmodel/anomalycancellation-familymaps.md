---
declaration: module
origin: cited
lean: SM.chargesMapOfSpeciesMap, SM.speciesFamilyProj, SM.familyProjection, SM.speciesEmbed, SM.familyEmbedding, SM.speciesFamilyUniversial, SM.familyUniversal
statement: formalized
proof: formalized
---

# Family maps for the Standard Model ACCs

The module `Physlib.Particles.StandardModel.AnomalyCancellation.FamilyMaps`, [Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean): 7 declarations, 7 with a docstring.

> We define the a series of maps between the charges for different numbers of families.

**`SM.chargesMapOfSpeciesMap`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L26).

> Given a map of for a generic species, the corresponding map for charges.

```lean
def chargesMapOfSpeciesMap {n m : ℕ} (f : (SMSpecies n).Charges →ₗ[ℚ] (SMSpecies m).Charges) :
    (SMCharges n).Charges →ₗ[ℚ] (SMCharges m).Charges
```

**`SM.speciesFamilyProj`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L45).

> The projection of the `m`-family charges onto the first `n`-family charges for species.

```lean
def speciesFamilyProj {m n : ℕ} (h : n ≤ m) :
    (SMSpecies m).Charges →ₗ[ℚ] (SMSpecies n).Charges
```

**`SM.familyProjection`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L52).

> The projection of the `m`-family charges onto the first `n`-family charges.

```lean
def familyProjection {m n : ℕ} (h : n ≤ m) : (SMCharges m).Charges →ₗ[ℚ] (SMCharges n).Charges
```

**`SM.speciesEmbed`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L59).

> For species, the embedding of the `m`-family charges onto the `n`-family charges, with all
> other charges zero.

```lean
def speciesEmbed (m n : ℕ) :
    (SMSpecies m).Charges →ₗ[ℚ] (SMSpecies n).Charges
```

**`SM.familyEmbedding`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L83).

> The embedding of the `m`-family charges onto the `n`-family charges, with all
> other charges zero.

```lean
def familyEmbedding (m n : ℕ) : (SMCharges m).Charges →ₗ[ℚ] (SMCharges n).Charges
```

**`SM.speciesFamilyUniversial`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L89).

> For species, the embedding of the `1`-family charges into the `n`-family charges in
> a universal manner.

```lean
def speciesFamilyUniversial (n : ℕ) :
    (SMSpecies 1).Charges →ₗ[ℚ] (SMSpecies n).Charges
```

**`SM.familyUniversal`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean#L97).

> The embedding of the `1`-family charges into the `n`-family charges in
> a universal manner.

```lean
def familyUniversal (n : ℕ) : (SMCharges 1).Charges →ₗ[ℚ] (SMCharges n).Charges
```

## Depends on

- [Anomaly cancellation conditions for the n-family SM.](anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/FamilyMaps.lean)
