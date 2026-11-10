---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.hodgeDuality, AlgebraicGeometry.deRhamComplex_d_zero_app_top_eq_zero, AlgebraicGeometry.TopDegreeDifferential.rightDerived_map_deRham_d_eq_zero_of_isProper_of_smooth, AlgebraicGeometry.Scheme.Hom.deRhamPoincareDuality
statement: formalized
proof: formalized
---

# 50.20 Poincaré duality

Section 50.20 of the Stacks Project, [Tag 0FW3](https://stacks.math.columbia.edu/tag/0FW3). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FW4, a lemma

[Tag 0FW4](https://stacks.math.columbia.edu/tag/0FW4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.hodgeDuality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/HodgeDuality.lean, line 922](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/HodgeDuality.lean#L922). The attribute's comment: “for X nonempty smooth proper over a field k, equidimensional of dimension d: there is t : H^d(X, Omega^d) -> k, unique up to precomposition with multiplication by a unit of H^0(X, O_X), such that every pairing H^q(X, Omega^p) x H^{d-q}(X, Omega^{d-p}) -> k, (xi, xi') |-> t(xi cup xi') is perfect”.

> **[Stacks, Tag 0FW4].** Let `k` be a field and `X` a nonempty smooth proper scheme over `k`,
> equidimensional of dimension `d`. There is a `k`-linear map `t : Hᵈ(X, Ω^d_{X/k}) ⟶ k` such
> that for all `p, q` the pairing `H^q(X, Ω^p_{X/k}) × H^{d-q}(X, Ω^{d-p}_{X/k}) ⟶ k`,
> `(ξ, ξ') ↦ t(ξ ∪ ξ')` is perfect, and `t` is unique up to precomposing with multiplication by a
> unit of `H⁰(X, 𝒪_X)`: a linear map `t'` has the same property if and only if
> `t' = t ∘ (u · -)` for a unit `u` of `H⁰(X, 𝒪_X)`, and that unit is unique. The map `t` is the
> trace read through `ω_X ≅ Ω^d_{X/k}` ([Stacks, Tag 0FVV], part (7)).

```lean
theorem hodgeDuality [Smooth f] [Nonempty X] (d : ℕ)
    (hequi : TopologicalSpace.Equidimensional X) (hd : topologicalKrullDim X = d) :
    ∃ t : sheafCohomology f (relativeDifferentialForms f d) d →ₗ[k] k,
      (∀ p q : ℤ, (hodgePairing f d t p q).IsPerfPair) ∧
      ∀ t' : sheafCohomology f (relativeDifferentialForms f d) d →ₗ[k] k,
        (∀ p q : ℤ, (hodgePairing f d t' p q).IsPerfPair) ↔
          ∃! u : (Γ(X, ⊤))ˣ, t' = t ∘ₗ cohomologySMul f (relativeDifferentialForms f d) d u
```

## Tag 0FW5, a lemma

[Tag 0FW5](https://stacks.math.columbia.edu/tag/0FW5) in the Stacks Project.

**`AlgebraicGeometry.deRhamComplex_d_zero_app_top_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/BottomDifferential.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/BottomDifferential.lean#L102).

> **The degree-zero de Rham differential of a smooth proper scheme over a field vanishes on
> global sections.**

```lean
theorem deRhamComplex_d_zero_app_top_eq_zero (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [Smooth f] [IsProper f]
    (B : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier)
      (SheafOfModules.moduleOfDifferentials.{u, u, u} (inverseImageStructureMap f)))
    (D : SheafOfModules.DeRhamDifferential B) :
    ((SheafOfModules.deRhamComplex B D).d 0 1).val.app (op ⊤) = 0
```

## Tag 0FW6, a lemma

[Tag 0FW6](https://stacks.math.columbia.edu/tag/0FW6) in the Stacks Project.

**`AlgebraicGeometry.TopDegreeDifferential.rightDerived_map_deRham_d_eq_zero_of_isProper_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/TopDifferentialSpreadOut.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/TopDifferentialSpreadOut.lean#L298). The attribute's comment: “for X smooth proper over a field k, equidimensional of dimension d, the map d : H^d(X, Omega^{d-1}_{X/k}) -> H^d(X, Omega^d_{X/k}) is zero”.

> **[Stacks, Tag 0FW6].** Let `k` be a field and `X` a smooth proper scheme over `k`,
> equidimensional of dimension `d`. Then the map `d : Hᵈ(X, Ω^{d-1}_{X/k}) ⟶ Hᵈ(X, Ω^d_{X/k})`
> induced by the de Rham differential is zero. The dualizing module of a smooth proper scheme over
> a field is its sheaf of top forms by [Stacks, Tag 0FVV], part (7).

```lean
theorem rightDerived_map_deRham_d_eq_zero_of_isProper_of_smooth {k : Type u} [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] [Smooth f]
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ)
    (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) :
    ((sectionsFunctor X.carrier ⊤).rightDerived d).map
      ((SheafOfModules.toSheaf _).map (f.deRhamComplex.d (d - 1) d)) = 0
```

## Tag 0FW7, a proposition

[Tag 0FW7](https://stacks.math.columbia.edu/tag/0FW7) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamPoincareDuality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/DeRhamPoincareDuality.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PoincareDuality/DeRhamPoincareDuality.lean#L697). The attribute's comment: “for X nonempty smooth proper over a field k, equidimensional of dimension d: there is t : H^{2d}_dR(X/k) -> k, unique up to precomposition with multiplication by a unit of H^0(X, O_X), such that for all i the pairing H^i_dR(X/k) x H^{2d-i}_dR(X/k) -> k, (xi, xi') |-> t(xi cup xi') is perfect”.

> **Poincaré duality for de Rham cohomology ([Stacks, Tag 0FW7]).** Let `k` be a field and
> `X` a nonempty smooth proper scheme over `k`, equidimensional of dimension `d`. There is a
> `k`-linear map `t : H^{2d}_{dR}(X/k) ⟶ k` such that for every `i` the pairing
> `Hⁱ_{dR}(X/k) × H^{2d-i}_{dR}(X/k) ⟶ k`, `(ξ, ξ') ↦ t(ξ ∪ ξ')` is perfect, and `t` is unique up
> to precomposing with multiplication by a unit of `H⁰(X, 𝒪_X)`: a linear map `t'` has the same
> property if and only if `t' = t(ξ ∪ -)` for the class `ξ ∈ H⁰_{dR}(X/k)` of a unit `u` of
> `H⁰(X, 𝒪_X)` — `H⁰_{dR}(X/k) = H⁰(X, 𝒪_X)` through `Ω^•_{X/k} ⟶ 𝒪_X[0]`
> (`bijective_deRhamCohomologyZeroToSections`) — and that unit is unique.
>
> The cup product is that of Section 0FM3 (`AlgebraicGeometry.Scheme.Hom.deRhamCup`, see
> `deRhamCupBilinear_apply`), defined for `X` with affine diagonal; a scheme proper over a field
> is separated, so it has affine diagonal.

```lean
theorem deRhamPoincareDuality [IsProper f] [Smooth f] [Nonempty X] (d : ℕ)
    (hequi : TopologicalSpace.Equidimensional X) (hdim : topologicalKrullDim X = d) :
    letI := AlgebraicGeometry.DeRhamTypeComplex.isAffineHom_diagonal_of_isProper f
    ∃ t : deRhamCohomologyOverField f ((d : ℤ) + d) →ₗ[k] k,
      (∀ i : ℤ, ((deRhamCupBilinear f i ((d : ℤ) + d - i) ((d : ℤ) + d) (by ring)).compr₂
        t).IsPerfPair) ∧
      ∀ t' : deRhamCohomologyOverField f ((d : ℤ) + d) →ₗ[k] k,
        (∀ i : ℤ, ((deRhamCupBilinear f i ((d : ℤ) + d - i) ((d : ℤ) + d) (by ring)).compr₂
          t').IsPerfPair) ↔
          ∃! u : (Γ(X, ⊤))ˣ, ∃ ξ : deRhamCohomologyOverField f 0,
            deRhamCohomologyZeroToSections f ξ = u ∧
              t' = t ∘ₗ deRhamCupBilinear f 0 ((d : ℤ) + d) ((d : ℤ) + d) (zero_add _) ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.20, Tag 0FW3](https://stacks.math.columbia.edu/tag/0FW3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
