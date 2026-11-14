---
declaration: module
origin: cited
lean: MSSMCharges, MSSMSpecies, MSSMCharges.sum_MSSMSpecies_numberCharges_eq_expand, MSSMCharges.toSMPlusH, MSSMCharges.splitSMPlusH, MSSMCharges.toSplitSMPlusH, MSSMCharges.toSpeciesMaps', MSSMCharges.toSpecies
statement: formalized
proof: formalized
---

# The MSSM with 3 families and RHNs

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.Basic`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean): 50 declarations, 37 with a docstring.

> We define the system of ACCs for the MSSM with 3 families and RHNs.
> We define the system of charges for 1-species. We prove some basic lemmas about them.

**`MSSMCharges`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L24).

> The vector space of charges corresponding to the MSSM fermions.

```lean
def MSSMCharges : ACCSystemCharges
```

**`MSSMSpecies`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L28).

> The vector spaces of charges of one species of fermions in the MSSM.

```lean
def MSSMSpecies : ACCSystemCharges
```

**`MSSMCharges.sum_MSSMSpecies_numberCharges_eq_expand`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L32).

```lean
lemma sum_MSSMSpecies_numberCharges_eq_expand [AddCommMonoid M]
    (f : Fin MSSMSpecies.numberCharges → M) :
    ∑ i, f i = f ⟨0, by simp⟩ + f ⟨1, by simp⟩ + f ⟨2, by simp⟩
```

**`MSSMCharges.toSMPlusH`**, a def, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L40).

> An equivalence between `MSSMCharges.charges` and the space of maps
> `(Fin 18 ⊕ Fin 2 → ℚ)`. The first 18 factors corresponds to the SM fermions, while the last two
> are the higgsions.

```lean
def toSMPlusH : MSSMCharges.Charges ≃ (Fin 18 ⊕ Fin 2 → ℚ)
```

**`MSSMCharges.splitSMPlusH`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L45).

> An equivalence between `Fin 18 ⊕ Fin 2 → ℚ` and `(Fin 18 → ℚ) × (Fin 2 → ℚ)`.

```lean
def splitSMPlusH : (Fin 18 ⊕ Fin 2 → ℚ) ≃ (Fin 18 → ℚ) × (Fin 2 → ℚ)
```

**`MSSMCharges.toSplitSMPlusH`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L54).

> An equivalence between `MSSMCharges.charges` and `(Fin 18 → ℚ) × (Fin 2 → ℚ)`. This
> splits the charges up into the SM and the additional ones for the MSSM.

```lean
def toSplitSMPlusH : MSSMCharges.Charges ≃ (Fin 18 → ℚ) × (Fin 2 → ℚ)
```

**`MSSMCharges.toSpeciesMaps'`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L59).

> An equivalence between `(Fin 18 → ℚ)` and `(Fin 6 → Fin 3 → ℚ)`.

```lean
def toSpeciesMaps' : (Fin 18 → ℚ) ≃ (Fin 6 → Fin 3 → ℚ)
```

**`MSSMCharges.toSpecies`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L67).

> An equivalence between `MSSMCharges.charges` and `(Fin 6 → Fin 3 → ℚ) × (Fin 2 → ℚ))`.
> This splits charges up into the SM and additional fermions, and further splits the SM into
> species.

```lean
def toSpecies : MSSMCharges.Charges ≃ (Fin 6 → Fin 3 → ℚ) × (Fin 2 → ℚ)
```

**`MSSMCharges.toSMSpecies`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L73).

> For a given `i ∈ Fin 6` the projection of `MSSMCharges.charges` down to the
> corresponding SM species of charges.

```lean
def toSMSpecies (i : Fin 6) : MSSMCharges.Charges →ₗ[ℚ] MSSMSpecies.Charges
```

**`MSSMCharges.toSMSpecies_toSpecies_inv`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L78).

```lean
lemma toSMSpecies_toSpecies_inv (i : Fin 6) (f : (Fin 6 → Fin 3 → ℚ) × (Fin 2 → ℚ)) :
    (toSMSpecies i) (toSpecies.symm f) = f.1 i
```

**`MSSMCharges.Q`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L83).

> The `Q` charges as a map `Fin 3 → ℚ`.

```lean
abbrev Q
```

**`MSSMCharges.U`**, an abbrev, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L85).

> The `U` charges as a map `Fin 3 → ℚ`.

```lean
abbrev U
```

**`MSSMCharges.D`**, an abbrev, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L87).

> The `D` charges as a map `Fin 3 → ℚ`.

```lean
abbrev D
```

**`MSSMCharges.L`**, an abbrev, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L89).

> The `L` charges as a map `Fin 3 → ℚ`.

```lean
abbrev L
```

**`MSSMCharges.E`**, an abbrev, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L91).

> The `E` charges as a map `Fin 3 → ℚ`.

```lean
abbrev E
```

**`MSSMCharges.N`**, an abbrev, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L93).

> The `N` charges as a map `Fin 3 → ℚ`.

```lean
abbrev N
```

**`MSSMCharges.Hd`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L97).

> The charge `Hd`.

```lean
def Hd : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMCharges.Hu`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L104).

> The charge `Hu`.

```lean
def Hu : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMCharges.charges_eq_toSpecies_eq`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L109).

```lean
lemma charges_eq_toSpecies_eq (S T : MSSMCharges.Charges) :
    S = T ↔ (∀ i, toSMSpecies i S = toSMSpecies i T) ∧ Hd S = Hd T ∧ Hu S = Hu T
```

**`MSSMCharges.Hd_toSpecies_inv`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L114).

```lean
lemma Hd_toSpecies_inv (f : (Fin 6 → Fin 3 → ℚ) × (Fin 2 → ℚ)) :
    Hd (toSpecies.symm f) = f.2 0
```

**`MSSMCharges.Hu_toSpecies_inv`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L118).

```lean
lemma Hu_toSpecies_inv (f : (Fin 6 → Fin 3 → ℚ) × (Fin 2 → ℚ)) :
    Hu (toSpecies.symm f) = f.2 1
```

**`MSSMACCs.accGrav`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L130).

> The gravitational anomaly equation.

```lean
def accGrav : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMACCs.accGrav_ext`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L144).

> Extensionality lemma for `accGrav`.

```lean
lemma accGrav_ext {S T : MSSMCharges.Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSMSpecies j) S i = ∑ i, (toSMSpecies j) T i)
    (hd : Hd S = Hd T) (hu : Hu S = Hu T) :
    accGrav S = accGrav T
```

**`MSSMACCs.accSU2`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L153).

> The anomaly cancellation condition for SU(2) anomaly.

```lean
def accSU2 : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMACCs.accSU2_ext`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L166).

> Extensionality lemma for `accSU2`.

```lean
lemma accSU2_ext {S T : MSSMCharges.Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSMSpecies j) S i = ∑ i, (toSMSpecies j) T i)
    (hd : Hd S = Hd T) (hu : Hu S = Hu T) :
    accSU2 S = accSU2 T
```

**`MSSMACCs.accSU3`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L175).

> The anomaly cancellation condition for SU(3) anomaly.

```lean
def accSU3 : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMACCs.accSU3_ext`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L188).

> Extensionality lemma for `accSU3`.

```lean
lemma accSU3_ext {S T : MSSMCharges.Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSMSpecies j) S i = ∑ i, (toSMSpecies j) T i) :
    accSU3 S = accSU3 T
```

**`MSSMACCs.accYY`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L196).

> The ACC for `Y²`.

```lean
def accYY : MSSMCharges.Charges →ₗ[ℚ] ℚ
```

**`MSSMACCs.accYY_ext`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L210).

> Extensionality lemma for `accGrav`.

```lean
lemma accYY_ext {S T : MSSMCharges.Charges}
    (hj : ∀ (j : Fin 6), ∑ i, (toSMSpecies j) S i = ∑ i, (toSMSpecies j) T i)
    (hd : Hd S = Hd T) (hu : Hu S = Hu T) :
    accYY S = accYY T
```

**`MSSMACCs.quadBiLin`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L220).

> The symmetric bilinear function used to define the quadratic ACC.

```lean
def quadBiLin : BiLinearSymm MSSMCharges.Charges
```

**`MSSMACCs.accQuad`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L265).

> The quadratic ACC.

```lean
def accQuad : HomogeneousQuadratic MSSMCharges.Charges
```

**`MSSMACCs.accQuad_ext`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L269).

> Extensionality lemma for `accQuad`.

```lean
lemma accQuad_ext {S T : (MSSMCharges).Charges}
    (h : ∀ j, ∑ i, ((fun a => a^2) ∘ toSMSpecies j S) i =
    ∑ i, ((fun a => a^2) ∘ toSMSpecies j T) i)
    (hd : Hd S = Hd T) (hu : Hu S = Hu T) :
    accQuad S = accQuad T
```

**`MSSMACCs.cubeTriLinToFun`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L279).

> The function underlying the symmetric trilinear form used to define the cubic ACC.

```lean
def cubeTriLinToFun
    (S : MSSMCharges.Charges × MSSMCharges.Charges × MSSMCharges.Charges) : ℚ
```

**`MSSMACCs.cubeTriLinToFun_map_smul₁`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L290).

```lean
lemma cubeTriLinToFun_map_smul₁ (a : ℚ) (S T R : MSSMCharges.Charges) :
    cubeTriLinToFun (a • S, T, R) = a * cubeTriLinToFun (S, T, R)
```

**`MSSMACCs.cubeTriLinToFun_map_add₁`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L297).

```lean
lemma cubeTriLinToFun_map_add₁ (S T R L : MSSMCharges.Charges) :
    cubeTriLinToFun (S + T, R, L) = cubeTriLinToFun (S, R, L) + cubeTriLinToFun (T, R, L)
```

**`MSSMACCs.cubeTriLinToFun_swap1`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L303).

```lean
lemma cubeTriLinToFun_swap1 (S T R : MSSMCharges.Charges) :
    cubeTriLinToFun (S, T, R) = cubeTriLinToFun (T, S, R)
```

**`MSSMACCs.cubeTriLinToFun_swap2`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L308).

```lean
lemma cubeTriLinToFun_swap2 (S T R : MSSMCharges.Charges) :
    cubeTriLinToFun (S, T, R) = cubeTriLinToFun (S, R, T)
```

**`MSSMACCs.cubeTriLin`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L315).

> The symmetric trilinear form used to define the cubic ACC.

```lean
def cubeTriLin : TriLinearSymm MSSMCharges.Charges
```

**`MSSMACCs.accCube`**, a def, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L324).

> The cubic ACC.

```lean
def accCube : HomogeneousCubic MSSMCharges.Charges
```

**`MSSMACCs.accCube_ext`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L328).

> Extensionality lemma for `accCube`.

```lean
lemma accCube_ext {S T : MSSMCharges.Charges}
    (h : ∀ j, ∑ i, ((fun a => a^3) ∘ toSMSpecies j S) i =
    ∑ i, ((fun a => a^3) ∘ toSMSpecies j T) i)
    (hd : Hd S = Hd T) (hu : Hu S = Hu T) :
    accCube S = accCube T
```

**`MSSMACC`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L344).

> The ACCSystem for the MSSM without RHN.

```lean
def MSSMACC : ACCSystem
```

**`MSSMACC.cubicACC_apply`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L362).

```lean
lemma cubicACC_apply (S : MSSMACC.Charges) : MSSMACC.cubicACC S = cubeTriLin.toCubic S
```

**`MSSMACC.quadSol`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L364).

```lean
lemma quadSol (S : MSSMACC.QuadSols) : accQuad S.val = 0
```

**`MSSMACC.AnomalyFreeMk`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L368).

> A solution from a charge satisfying the ACCs.

```lean
def AnomalyFreeMk (S : MSSMACC.Charges) (hg : accGrav S = 0)
    (hsu2 : accSU2 S = 0) (hsu3 : accSU3 S = 0) (hyy : accYY S = 0)
    (hquad : accQuad S = 0) (hcube : accCube S = 0) : MSSMACC.Sols
```

**`MSSMACC.AnomalyFreeMk_val`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L382).

```lean
lemma AnomalyFreeMk_val (S : MSSMACC.Charges) (hg : accGrav S = 0)
    (hsu2 : accSU2 S = 0) (hsu3 : accSU3 S = 0) (hyy : accYY S = 0)
    (hquad : accQuad S = 0) (hcube : accCube S = 0) :
    (AnomalyFreeMk S hg hsu2 hsu3 hyy hquad hcube).val = S
```

**`MSSMACC.AnomalyFreeQuadMk'`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L390).

> A `QuadSol` from a `LinSol` satisfying the quadratic ACC.

```lean
def AnomalyFreeQuadMk' (S : MSSMACC.LinSols) (hquad : accQuad S.val = 0) :
    MSSMACC.QuadSols
```

**`MSSMACC.AnomalyFreeMk'`**, a def, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L399).

> A `Sol` from a `LinSol` satisfying the quadratic and cubic ACCs.

```lean
def AnomalyFreeMk' (S : MSSMACC.LinSols) (hquad : accQuad S.val = 0)
    (hcube : accCube S.val = 0) : MSSMACC.Sols
```

**`MSSMACC.AnomalyFreeMk''`**, a def, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L408).

> A `Sol` from a `QuadSol` satisfying the cubic ACCs.

```lean
def AnomalyFreeMk'' (S : MSSMACC.QuadSols) (hcube : accCube S.val = 0) : MSSMACC.Sols
```

**`MSSMACC.AnomalyFreeMk''_val`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L411).

```lean
lemma AnomalyFreeMk''_val (S : MSSMACC.QuadSols)
    (hcube : accCube S.val = 0) :
    (AnomalyFreeMk'' S hcube).val = S.val
```

**`MSSMACC.dot`**, a def, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean#L419).

> The dot product on the vector space of charges.

```lean
def dot : BiLinearSymm MSSMCharges.Charges
```

## Depends on

- [Anomaly cancellation conditions](../../../qft/anomalycancellation/basic.md)

## Proof depends on

- [Anomaly cancellation conditions for the n-family SM.](../../standardmodel/anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Basic.lean)
