---
declaration: module
origin: cited
lean: LorentzGroup.genBoostAux₁, LorentzGroup.genBoostAux₂, LorentzGroup.genBoostAux₂_self, LorentzGroup.genBoostAux₁_apply_basis, LorentzGroup.genBoostAux₂_apply_basis, LorentzGroup.genBoostAux₁_basis_minkowskiProduct, LorentzGroup.genBoostAux₁_toMatrix_apply, LorentzGroup.genBoostAux₂_basis_minkowskiProduct
statement: formalized
proof: formalized
---

# Generalized Boosts

The module `Physlib.Relativity.LorentzGroup.Boosts.Generalized`, [Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean): 31 declarations, 5 with a docstring.

> This module defines a generalization of the traditional boosts.
> They are define given two velocities `u` and `v`, as an input an take
> the velocity `u` to the velocity `v`.
>
> We show that these generalised boosts are Lorentz transformations,
> and furthermore sit in the restricted Lorentz group.
>
> A boost is the special case of a generalised boost when `u = basis 0`.

## References

> * The main argument follows: Guillem Cobos, The Lorentz Group, 2015:
>   https://diposit.ub.edu/dspace/bitstream/2445/68763/2/memoria.pdf. [ref: cobos\_2015\_lorentz\_group]

## Auxiliary Linear Maps

**`LorentzGroup.genBoostAux₁`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L45).

> An auxiliary linear map used in the definition of a generalised boost.

```lean
def genBoostAux₁ (u v : Velocity d) : Vector d →ₗ[ℝ] Vector d
```

**`LorentzGroup.genBoostAux₂`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L56).

> An auxiliary linear map used in the definition of a generalised boost.

```lean
def genBoostAux₂ (u v : Velocity d) : Vector d →ₗ[ℝ] Vector d
```

**`LorentzGroup.genBoostAux₂_self`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L70).

```lean
lemma genBoostAux₂_self (u : Velocity d) : genBoostAux₂ u u = - genBoostAux₁ u u
```

**`LorentzGroup.genBoostAux₁_apply_basis`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L79).

```lean
lemma genBoostAux₁_apply_basis (u v : Velocity d) (μ : Fin 1 ⊕ Fin d) :
    (genBoostAux₁ u v) (Vector.basis μ) = (2 * η μ μ * u.1 μ) • v
```

**`LorentzGroup.genBoostAux₂_apply_basis`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L84).

```lean
lemma genBoostAux₂_apply_basis (u v : Velocity d) (μ : Fin 1 ⊕ Fin d) :
    (genBoostAux₂ u v) (Vector.basis μ) =
    - (η μ μ * (u.1 μ + v.1 μ) / (1 + ⟪u.1, v.1⟫ₘ)) • (u.1 + v.1)
```

**`LorentzGroup.genBoostAux₁_basis_minkowskiProduct`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L90).

```lean
lemma genBoostAux₁_basis_minkowskiProduct (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    ⟪genBoostAux₁ u v (Vector.basis μ), genBoostAux₁ u v (Vector.basis ν)⟫ₘ =
    4 * η μ μ * η ν ν * u.1 μ * u.1 ν
```

**`LorentzGroup.genBoostAux₁_toMatrix_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L96).

```lean
lemma genBoostAux₁_toMatrix_apply (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    (LinearMap.toMatrix Vector.basis Vector.basis (genBoostAux₁ u v)) μ ν =
    η ν ν * (2 * u.1 ν * v.1 μ)
```

**`LorentzGroup.genBoostAux₂_basis_minkowskiProduct`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L103).

```lean
lemma genBoostAux₂_basis_minkowskiProduct (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    ⟪genBoostAux₂ u v (Vector.basis μ), genBoostAux₂ u v (Vector.basis ν)⟫ₘ =
    2 * η μ μ * η ν ν * (u.1 μ + v.1 μ) * (u.1 ν + v.1 ν)
    * (1 + ⟪u, v.1⟫ₘ)⁻¹
```

**`LorentzGroup.genBoostAux₁_basis_genBoostAux₂_minkowskiProduct`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L123).

```lean
lemma genBoostAux₁_basis_genBoostAux₂_minkowskiProduct (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    ⟪genBoostAux₁ u v (Vector.basis μ), genBoostAux₂ u v (Vector.basis ν)⟫ₘ =
    - 2 * η μ μ * η ν ν * u.1 μ * (u.1 ν + v.1 ν)
```

**`LorentzGroup.genBoostAux₂_toMatrix_apply`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L140).

```lean
lemma genBoostAux₂_toMatrix_apply (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    (LinearMap.toMatrix Vector.basis Vector.basis (genBoostAux₂ u v)) μ ν =
      η ν ν * (- (u.1 μ + v.1 μ) * (u.1 ν + v.1 ν)
      / (1 + ⟪u.1, v.1⟫ₘ))
```

**`LorentzGroup.genBoostAux₁_add_genBoostAux₂_minkowskiProduct`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L151).

```lean
lemma genBoostAux₁_add_genBoostAux₂_minkowskiProduct (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    ⟪genBoostAux₁ u v (Vector.basis μ) + genBoostAux₂ u v (Vector.basis μ),
    genBoostAux₁ u v (Vector.basis ν) + genBoostAux₂ u v (Vector.basis ν)⟫ₘ =
    2 * η μ μ * η ν ν * (- u.1 μ * (u.1 ν + v.1 ν)
      - u.1 ν * (u.1 μ + v.1 μ)
      + (u.1 μ + v.1 μ) * (u.1 ν + v.1 ν) * (1 + ⟪u, v.1⟫ₘ)⁻¹ +
      2 * u.1 μ * u.1 ν)
```

**`LorentzGroup.basis_minkowskiProduct_genBoostAux₁_add_genBoostAux₂`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L166).

```lean
lemma basis_minkowskiProduct_genBoostAux₁_add_genBoostAux₂ (u v : Velocity d)
    (μ ν : Fin 1 ⊕ Fin d) :
    ⟪Vector.basis μ, genBoostAux₁ u v (Vector.basis ν) + genBoostAux₂ u v (Vector.basis ν)⟫ₘ =
    η μ μ * η ν ν * (2 * u.1 ν * v.1 μ
    - (u.1 μ + v.1 μ) * (u.1 ν + v.1 ν) * (1 + ⟪u.1, v.1⟫ₘ)⁻¹)
```

## Generalized Boosts

**`LorentzGroup.generalizedBoost`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L189).

> An generalised boost. This is a Lorentz transformation which takes the Lorentz velocity `u`
> to `v`.

```lean
def generalizedBoost (u v : Velocity d) : LorentzGroup d
```

**`LorentzGroup.generalizedBoost_apply`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L218).

```lean
lemma generalizedBoost_apply (u v : Velocity d) (x : Vector d) :
    generalizedBoost u v • x = x + genBoostAux₁ u v x + genBoostAux₂ u v x
```

**`LorentzGroup.generalizedBoost_apply_mul_one_plus_contr`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L228).

```lean
lemma generalizedBoost_apply_mul_one_plus_contr (u v : Velocity d) (x : Vector d) :
    (1 + ⟪u, v.1⟫ₘ) • generalizedBoost u v • x = (1 + ⟪u, v.1⟫ₘ) • x +
    (2 * ⟪x, u⟫ₘ * (1 + ⟪u, v.1⟫ₘ)) • v - ⟪x, u + v⟫ₘ • (u + v)
```

**`LorentzGroup.generalizedBoost_apply_expand`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L250).

```lean
lemma generalizedBoost_apply_expand (u v : Velocity d) (x : Vector d) :
    generalizedBoost u v • x = x + (2 * ⟪x, u⟫ₘ) • v.1 -
      (⟪x, u + v⟫ₘ / (1 + ⟪u, v.1⟫ₘ)) • (u.1 + v.1)
```

**`LorentzGroup.generalizedBoost_apply_fst`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L259).

```lean
lemma generalizedBoost_apply_fst (u v : Velocity d) :
    generalizedBoost u v • u.1 = v.1
```

**`LorentzGroup.generalizedBoost_apply_snd`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L267).

```lean
lemma generalizedBoost_apply_snd (u v : Velocity d) :
    generalizedBoost u v • v.1 = (2 * ⟪u, v.1⟫ₘ) • ↑v - ↑u
```

**`LorentzGroup.generalizedBoost_self`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L279).

> This lemma states that for a given four-velocity `u`, the general boost
> transformation `genBoost u u` is equal to the identity linear map `LinearMap.id`.

```lean
lemma generalizedBoost_self (u : Velocity d) :
    generalizedBoost u u = 1
```

**`LorentzGroup.genearlizedBoost_apply_basis`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L284).

```lean
lemma genearlizedBoost_apply_basis (u v : Velocity d) (μ : Fin 1 ⊕ Fin d) :
    generalizedBoost u v • (Vector.basis μ) =
    Vector.basis μ + (2 * η μ μ * u.1 μ) • v - (η μ μ * (u.1 μ + v.1 μ)
      / (1 + ⟪u.1, v.1⟫ₘ)) • (u.1 + v.1)
```

**`LorentzGroup.generalizedBoost_apply_eq_minkowskiProduct`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L291).

```lean
lemma generalizedBoost_apply_eq_minkowskiProduct (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    (generalizedBoost u v).1 μ ν = η μ μ * (⟪Vector.basis μ, Vector.basis ν⟫ₘ + 2 *
    ⟪Vector.basis ν, u⟫ₘ * ⟪Vector.basis μ, v.1⟫ₘ
    - ⟪Vector.basis μ, u + v⟫ₘ * ⟪Vector.basis ν, u + v⟫ₘ / (1 + ⟪u.1, v⟫ₘ))
```

**`LorentzGroup.generalizedBoost_apply_eq_toCoord`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L315).

```lean
lemma generalizedBoost_apply_eq_toCoord (u v : Velocity d) (μ ν : Fin 1 ⊕ Fin d) :
    (generalizedBoost u v).1 μ ν = ((1 : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) μ ν +
    2 * η ν ν * u.1 ν * v.1 μ
    - η ν ν * (u.1 μ + v.1 μ) * (u.1 ν + v.1 ν) / (1 + ⟪u.1, v⟫ₘ))
```

**`LorentzGroup.generalizedBoost_continuous_snd`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L330).

```lean
lemma generalizedBoost_continuous_snd (u : Velocity d) : Continuous (generalizedBoost u)
```

**`LorentzGroup.generalizedBoost_continuous_fst`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L339).

```lean
lemma generalizedBoost_continuous_fst (u : Velocity d) : Continuous (generalizedBoost · u)
```

**`LorentzGroup.id_joined_generalizedBoost`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L347).

```lean
lemma id_joined_generalizedBoost (u v : Velocity d) : Joined 1 (generalizedBoost u v)
```

**`LorentzGroup.generalizedBoost_in_connected_component_of_id`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L353).

```lean
lemma generalizedBoost_in_connected_component_of_id (u v : Velocity d) :
    generalizedBoost u v ∈ connectedComponent 1
```

**`LorentzGroup.generalizedBoost_isProper`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L357).

```lean
lemma generalizedBoost_isProper (u v : Velocity d) : IsProper (generalizedBoost u v)
```

**`LorentzGroup.generalizedBoost_isOrthochronous`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L361).

```lean
lemma generalizedBoost_isOrthochronous (u v : Velocity d) :
    IsOrthochronous (generalizedBoost u v)
```

**`LorentzGroup.generalizedBoost_mem_restricted`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L366).

```lean
lemma generalizedBoost_mem_restricted (u v : Velocity d) :
    generalizedBoost u v ∈ LorentzGroup.restricted d
```

**`LorentzGroup.generalizedBoost_inv`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L373).

```lean
lemma generalizedBoost_inv (u v : Velocity d) :
    (generalizedBoost u v)⁻¹ = generalizedBoost v u
```

**`LorentzGroup.generalizedBoost_timeComponent_eq`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean#L386).

> The time component of a generalised boost.

```lean
lemma generalizedBoost_timeComponent_eq (u v : Velocity d) :
    (generalizedBoost u v).1 (Sum.inl 0) (Sum.inl 0) = 1 +
    ‖u.1.timeComponent • v.1.spatialPart -
      v.1.timeComponent • u.1.spatialPart‖ ^ 2 / (1 + ⟪u.1, v.1⟫ₘ)
```

## Depends on

- [The Restricted Lorentz Group](restricted-basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Generalized.lean)
