---
declaration: module
origin: cited
lean: SMRHN.chargesMapOfSpeciesMap, SMRHN.chargesMapOfSpeciesMap_toSpecies, SMRHN.speciesFamilyProj, SMRHN.familyProjection, SMRHN.speciesEmbed, SMRHN.familyEmbedding, SMRHN.speciesFamilyUniversial, SMRHN.familyUniversal
statement: formalized
proof: formalized
---

# Family maps for the Standard Model for RHN ACCs

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.FamilyMaps`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean): 22 declarations, 7 with a docstring.

> We define the a series of maps between the charges for different numbers of families.

**`SMRHN.chargesMapOfSpeciesMap`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L25).

> Given a map of for a generic species, the corresponding map for charges.

```lean
def chargesMapOfSpeciesMap {n m : ℕ} (f : (SMνSpecies n).Charges →ₗ[ℚ] (SMνSpecies m).Charges) :
    (SMνCharges n).Charges →ₗ[ℚ] (SMνCharges m).Charges
```

**`SMRHN.chargesMapOfSpeciesMap_toSpecies`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L39).

```lean
lemma chargesMapOfSpeciesMap_toSpecies {n m : ℕ}
    (f : (SMνSpecies n).Charges →ₗ[ℚ] (SMνSpecies m).Charges)
    (S : (SMνCharges n).Charges) (j : Fin 6) :
    toSpecies j (chargesMapOfSpeciesMap f S) = (LinearMap.comp f (toSpecies j)) S
```

**`SMRHN.speciesFamilyProj`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L47).

> The projection of the `m`-family charges onto the first `n`-family charges for species.

```lean
def speciesFamilyProj {m n : ℕ} (h : n ≤ m) :
    (SMνSpecies m).Charges →ₗ[ℚ] (SMνSpecies n).Charges
```

**`SMRHN.familyProjection`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L54).

> The projection of the `m`-family charges onto the first `n`-family charges.

```lean
def familyProjection {m n : ℕ} (h : n ≤ m) : (SMνCharges m).Charges →ₗ[ℚ] (SMνCharges n).Charges
```

**`SMRHN.speciesEmbed`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L61).

> For species, the embedding of the `m`-family charges onto the `n`-family charges, with all
> other charges zero.

```lean
def speciesEmbed (m n : ℕ) :
    (SMνSpecies m).Charges →ₗ[ℚ] (SMνSpecies n).Charges
```

**`SMRHN.familyEmbedding`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L86).

> The embedding of the `m`-family charges onto the `n`-family charges, with all
> other charges zero.

```lean
def familyEmbedding (m n : ℕ) : (SMνCharges m).Charges →ₗ[ℚ] (SMνCharges n).Charges
```

**`SMRHN.speciesFamilyUniversial`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L92).

> For species, the embedding of the `1`-family charges into the `n`-family charges in
> a universal manner.

```lean
def speciesFamilyUniversial (n : ℕ) :
    (SMνSpecies 1).Charges →ₗ[ℚ] (SMνSpecies n).Charges
```

**`SMRHN.familyUniversal`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L100).

> The embedding of the `1`-family charges into the `n`-family charges in
> a universal manner.

```lean
def familyUniversal (n : ℕ) : (SMνCharges 1).Charges →ₗ[ℚ] (SMνCharges n).Charges
```

**`SMRHN.toSpecies_familyUniversal`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L103).

```lean
lemma toSpecies_familyUniversal {n : ℕ} (j : Fin 6) (S : (SMνCharges 1).Charges)
    (i : Fin n) : toSpecies j (familyUniversal n S) i = toSpecies j S ⟨0, by simp⟩
```

**`SMRHN.sum_familyUniversal`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L109).

```lean
lemma sum_familyUniversal {n : ℕ} (m : ℕ) (S : (SMνCharges 1).Charges) (j : Fin 6) :
    ∑ i, ((fun a => a ^ m) ∘ toSpecies j (familyUniversal n S)) i =
    n * (toSpecies j S ⟨0, by simp⟩) ^ m
```

**`SMRHN.sum_familyUniversal_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L122).

```lean
lemma sum_familyUniversal_one {n : ℕ} (S : (SMνCharges 1).Charges) (j : Fin 6) :
    ∑ i, toSpecies j (familyUniversal n S) i = n * (toSpecies j S ⟨0, by simp⟩)
```

**`SMRHN.sum_familyUniversal_two`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L127).

```lean
lemma sum_familyUniversal_two {n : ℕ} (S : (SMνCharges 1).Charges)
    (T : (SMνCharges n).Charges) (j : Fin 6) :
    ∑ i, (toSpecies j (familyUniversal n S) i * toSpecies j T i) =
    (toSpecies j S ⟨0, by simp⟩) * ∑ i, toSpecies j T i
```

**`SMRHN.sum_familyUniversal_three`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L138).

```lean
lemma sum_familyUniversal_three {n : ℕ} (S : (SMνCharges 1).Charges)
    (T L : (SMνCharges n).Charges) (j : Fin 6) :
    ∑ i, (toSpecies j (familyUniversal n S) i * toSpecies j T i * toSpecies j L i) =
    (toSpecies j S ⟨0, by simp⟩) * ∑ i, toSpecies j T i * toSpecies j L i
```

**`SMRHN.familyUniversal_accGrav`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L154).

```lean
lemma familyUniversal_accGrav (S : (SMνCharges 1).Charges) :
    accGrav (familyUniversal n S) = n * (accGrav S)
```

**`SMRHN.familyUniversal_accSU2`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L163).

```lean
lemma familyUniversal_accSU2 (S : (SMνCharges 1).Charges) :
    accSU2 (familyUniversal n S) = n * (accSU2 S)
```

**`SMRHN.familyUniversal_accSU3`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L171).

```lean
lemma familyUniversal_accSU3 (S : (SMνCharges 1).Charges) :
    accSU3 (familyUniversal n S) = n * (accSU3 S)
```

**`SMRHN.familyUniversal_accYY`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L179).

```lean
lemma familyUniversal_accYY (S : (SMνCharges 1).Charges) :
    accYY (familyUniversal n S) = n * (accYY S)
```

**`SMRHN.familyUniversal_quadBiLin`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L186).

```lean
lemma familyUniversal_quadBiLin (S : (SMνCharges 1).Charges) (T : (SMνCharges n).Charges) :
    quadBiLin (familyUniversal n S) T =
    S (0 : Fin 6) * ∑ i, Q T i - 2 * S (1 : Fin 6) * ∑ i, U T i + S (2 : Fin 6) *∑ i, D T i -
    S (3 : Fin 6) * ∑ i, L T i + S (4 : Fin 6) * ∑ i, E T i
```

**`SMRHN.familyUniversal_accQuad`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L196).

```lean
lemma familyUniversal_accQuad (S : (SMνCharges 1).Charges) :
    accQuad (familyUniversal n S) = n * (accQuad S)
```

**`SMRHN.familyUniversal_cubeTriLin`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L206).

```lean
lemma familyUniversal_cubeTriLin (S : (SMνCharges 1).Charges) (T R : (SMνCharges n).Charges) :
    cubeTriLin (familyUniversal n S) T R = 6 * S (0 : Fin 6) * ∑ i, (Q T i * Q R i) +
      3 * S (1 : Fin 6) * ∑ i, (U T i * U R i) + 3 * S (2 : Fin 6) * ∑ i, (D T i * D R i)
      + 2 * S (3 : Fin 6) * ∑ i, (L T i * L R i) +
      S (4 : Fin 6) * ∑ i, (E T i * E R i) + S (5 : Fin 6) * ∑ i, (N T i * N R i)
```

**`SMRHN.familyUniversal_cubeTriLin'`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L217).

```lean
lemma familyUniversal_cubeTriLin' (S T : (SMνCharges 1).Charges) (R : (SMνCharges n).Charges) :
    cubeTriLin (familyUniversal n S) (familyUniversal n T) R =
      6 * S (0 : Fin 6) * T (0 : Fin 6) * ∑ i, Q R i +
      3 * S (1 : Fin 6) * T (1 : Fin 6) * ∑ i, U R i
      + 3 * S (2 : Fin 6) * T (2 : Fin 6) * ∑ i, D R i +
      2 * S (3 : Fin 6) * T (3 : Fin 6) * ∑ i, L R i +
      S (4 : Fin 6) * T (4 : Fin 6) * ∑ i, E R i + S (5 : Fin 6) * T (5 : Fin 6) * ∑ i, N R i
```

**`SMRHN.familyUniversal_accCube`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean#L230).

```lean
lemma familyUniversal_accCube (S : (SMνCharges 1).Charges) :
    accCube (familyUniversal n S) = n * (accCube S)
```

## Depends on

- [Anomaly cancellation conditions for the Standard Model with right-handed neutrinos](rhn-anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/FamilyMaps.lean)
