---
declaration: section
origin: cited
lean: Stacks.Groupoids.IsAbelianVariety, AlgebraicGeometry.IsAbelianVariety, AlgebraicGeometry.isProjective_of_isAbelianVariety, AlgebraicGeometry.isAbelianVariety_pullbackObj, AlgebraicGeometry.smooth_of_isAbelianVariety, Stacks.Groupoids.nonempty_cubeRelation_of_isAbelianVariety, Stacks.Groupoids.nonempty_cubeRelation, Stacks.Groupoids.nonempty_zpowId_pullback_iso
statement: formalized
proof: formalized
---

# 39.9 Abelian varieties

Section 39.9 of the Stacks Project, [Tag 0BF9](https://stacks.math.columbia.edu/tag/0BF9). 11 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03RO, a definition

[Tag 03RO](https://stacks.math.columbia.edu/tag/03RO) in the Stacks Project.

**`Stacks.Groupoids.IsAbelianVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety.lean#L52).

> A group scheme over a field is an abelian variety if its structure morphism makes its
> underlying scheme a proper, geometrically integral variety.

```lean
class IsAbelianVariety (k : Type u) [Field k] (A : Over (Spec (.of k))) [GrpObj A] : Prop
    extends IsProperVariety k A.hom, GeometricallyIntegral A.hom
```

**`AlgebraicGeometry.IsAbelianVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean#L68).

> **Stacks Project, Tag 03RO.** A group scheme over a field is an abelian variety if its
> structure morphism makes its underlying scheme a proper, geometrically integral variety.

```lean
class IsAbelianVariety (k : Type u) [Field k] (A : Over (Spec (.of k)))
    [GrpObj A] : Prop extends IsProperVariety k A.hom, GeometricallyIntegral A.hom
```

## Tag 0BFA, a lemma

[Tag 0BFA](https://stacks.math.columbia.edu/tag/0BFA) in the Stacks Project.

**`AlgebraicGeometry.isProjective_of_isAbelianVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyProjective.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyProjective.lean#L69).

> **Stacks Project, Tag 0BFA.** Let `k` be a field and let `A` be an abelian variety over `k`.
> Then `A` is projective over `k`.
>
> An abelian variety is an algebraic group scheme over `k`, hence quasi-projective over `k` by
> Tag 0BF7, and it is proper over `k`, so Tag 0B45 makes it projective over the affine base
> `Spec k`.

```lean
theorem isProjective_of_isAbelianVariety (k : Type u) [Field k] (A : Over (Spec (.of k)))
    [GrpObj A] [IsAbelianVariety k A] : IsProjective A.hom
```

## Tag 0BFB, a lemma

[Tag 0BFB](https://stacks.math.columbia.edu/tag/0BFB) in the Stacks Project.

**`AlgebraicGeometry.isAbelianVariety_pullbackObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean#L82).

> **Stacks Project, Tag 0BFB.** For a field extension `K/k`, the base change `A_K` of an
> abelian variety `A` over `k` is an abelian variety over `K`.

```lean
instance isAbelianVariety_pullbackObj (A : Over (Spec (.of k))) [GrpObj A]
    [IsAbelianVariety k A] :
    IsAbelianVariety K
      ((Over.pullback (Spec.map (CommRingCat.ofHom (algebraMap k K)))).obj A)
```

## Tag 0BFC, a lemma

[Tag 0BFC](https://stacks.math.columbia.edu/tag/0BFC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.smooth_of_isAbelianVariety`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyEquivalentDefinitions.lean#L218), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyEquivalentDefinitions.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyEquivalentDefinitions.lean#L293) (StacksFrontier).

## Tag 0BFE, a lemma

[Tag 0BFE](https://stacks.math.columbia.edu/tag/0BFE) in the Stacks Project.

**`Stacks.Groupoids.nonempty_cubeRelation_of_isAbelianVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cube/TheoremOfTheCube.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cube/TheoremOfTheCube.lean#L602).

> **Stacks Project, Tag 0BFE.** Let `k` be a field, let `A` be an abelian variety over `k`
> and let `L` be an invertible `𝒪_A`-module. Then
>
> `m₁₂₃^*L ⊗ m₁^*L ⊗ m₂^*L ⊗ m₃^*L ≅ m₁₂^*L ⊗ m₁₃^*L ⊗ m₂₃^*L`
>
> as invertible modules on `A × A × A`, where `m_I` is the sum of the coordinates indexed by
> `I`, written as the product of the corresponding coordinates in the group `A × A × A ⟶ A`. The
> theorem of the cube is `Stacks.Groupoids.hasTheoremOfTheCube`.

```lean
theorem nonempty_cubeRelation_of_isAbelianVariety [IsAbelianVariety k A]
    (L : SheafOfModules.{u} (structureSheafRing A.left.toRingedSpace))
    (hL : Stacks.SheafOfModules.IsInvertible A.left.presheaf A.left.ringCatIsSheaf L) :
    Nonempty
      (Stacks.SheafOfModules.schemeTensor (cubeObj A).left
          (Stacks.SheafOfModules.schemeTensor (cubeObj A).left
            (Stacks.SheafOfModules.schemeTensor (cubeObj A).left
              (pullbackOver (cubeProj₁ A * cubeProj₂ A * cubeProj₃ A) L)
              (pullbackOver (cubeProj₁ A) L))
            (pullbackOver (cubeProj₂ A) L))
          (pullbackOver (cubeProj₃ A) L) ≅
        Stacks.SheafOfModules.schemeTensor (cubeObj A).left
          (Stacks.SheafOfModules.schemeTensor (cubeObj A).left
            (pullbackOver (cubeProj₁ A * cubeProj₂ A) L)
            (pullbackOver (cubeProj₁ A * cubeProj₃ A) L))
          (pullbackOver (cubeProj₂ A * cubeProj₃ A) L))
```

**`Stacks.Groupoids.nonempty_cubeRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/CubeRelation.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/CubeRelation.lean#L468). The attribute's comment: “assuming the theorem of the cube (Tag 0BF4) for the triple self-product of A”.

> Let `A` be an abelian variety over a field `k` satisfying the theorem of the cube
> `HasTheoremOfTheCube A`, and let `L` be an invertible `𝒪_A`-module. Then
>
> `m₁₂₃^*L ⊗ m₁^*L ⊗ m₂^*L ⊗ m₃^*L ≅ m₁₂^*L ⊗ m₁₃^*L ⊗ m₂₃^*L`
>
> as invertible modules on `A × A × A`, where `m_I` is the product of the coordinates indexed by
> `I` in the group `A × A × A ⟶ A`.

```lean
theorem nonempty_cubeRelation [AlgebraicGeometry.IsAbelianVariety k A]
    (hcube : HasTheoremOfTheCube A)
    (L : SheafOfModules.{u} (structureSheafRing A.left.toRingedSpace))
    (hL : Stacks.SheafOfModules.IsInvertible A.left.presheaf A.left.ringCatIsSheaf L) :
    Nonempty
      (schemeTensor (cubeObj A).left
          (schemeTensor (cubeObj A).left
            (schemeTensor (cubeObj A).left
              (pullbackOver (cubeProj₁ A * cubeProj₂ A * cubeProj₃ A) L)
              (pullbackOver (cubeProj₁ A) L))
            (pullbackOver (cubeProj₂ A) L))
          (pullbackOver (cubeProj₃ A) L) ≅
        schemeTensor (cubeObj A).left
          (schemeTensor (cubeObj A).left
            (pullbackOver (cubeProj₁ A * cubeProj₂ A) L)
            (pullbackOver (cubeProj₁ A * cubeProj₃ A) L))
          (pullbackOver (cubeProj₂ A * cubeProj₃ A) L))
```

## Tag 0BFF, a lemma

[Tag 0BFF](https://stacks.math.columbia.edu/tag/0BFF) in the Stacks Project.

**`Stacks.Groupoids.nonempty_zpowId_pullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowPullback.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowPullback.lean#L369). The attribute's comment: “for every integer n, assuming the theorem of the cube (Tag 0BF4) for A”.

> Let `k` be a field, let `A` be an abelian variety over `k` satisfying the theorem of the
> cube for its triple self-product, and let `L` be an invertible `𝒪_A`-module. Then
>
> `[n]^*L ≅ L^{⊗ n(n+1)/2} ⊗ ([-1]^*L)^{⊗ n(n-1)/2}`
>
> for every integer `n`, where `[n] : A → A` is multiplication by `n`, the `n`th power of the
> identity in the group `A ⟶ A` of morphisms into the group object, and `[-1] = ι` is inversion.

```lean
theorem nonempty_zpowId_pullback_iso [AlgebraicGeometry.IsAbelianVariety k A]
    (hcube : HasTheoremOfTheCube A) (n : ℤ) :
    Nonempty (pullbackOver ((𝟙 A : A ⟶ A) ^ n) L ≅
      schemeTensor A.left (schemeTensorPower A.left L hL (n * (n + 1) / 2))
        (schemeTensorPower A.left (pullbackOver (ι : A ⟶ A) L)
          (isInvertible_pullbackOver (ι : A ⟶ A) L hL) (n * (n - 1) / 2)))
```

**`Stacks.Groupoids.nonempty_zpowId_pullback_iso_of_isAbelianVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowPullbackFormula.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowPullbackFormula.lean#L308).

> Let `k` be a field, let `A` be an abelian variety over `k` and let `L` be an invertible
> `𝒪_A`-module. Then for every integer `n`
>
> `[n]^*L ≅ L^{⊗ n(n+1)/2} ⊗ ([-1]^*L)^{⊗ n(n-1)/2}`
>
> where `[n] : A → A` is multiplication by `n`, the `n`th power of the identity in the group
> `A ⟶ A` of morphisms into the group object, and `[-1] = ι` is inversion. Both divisions are
> exact (`Stacks.Groupoids.two_dvd_mul_succ`).

```lean
theorem nonempty_zpowId_pullback_iso_of_isAbelianVariety (n : ℤ) :
    Nonempty (pullbackOver ((𝟙 A : A ⟶ A) ^ n) L ≅
      schemeTensor A.left (schemeTensorPower A.left L hL (n * (n + 1) / 2))
        (schemeTensorPower A.left (pullbackOver (ι : A ⟶ A) L)
          (isInvertible_pullbackOver (ι : A ⟶ A) L hL) (n * (n - 1) / 2)))
```

## Tag 0BFG, a lemma

[Tag 0BFG](https://stacks.math.columbia.edu/tag/0BFG) in the Stacks Project.

**`Stacks.Groupoids.isFiniteLocallyFreeOfRank_zpow_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L61). The attribute's comment: “for n nonzero, the degree n^(2 dim A) read as |n|^(2 dim A): the source's statement fails for n = 0 when dim A >= 1, since [0] factors through the unit point and its fibre over the unit is all of A”.

> Let `k` be a field, let `A` be an abelian variety over `k` and let `[n] = (𝟙 A) ^ n : A ⟶ A`
> be multiplication by a nonzero integer `n` in the group `A ⟶ A`. Then `[n]` is finite locally free
> of degree `|n| ^ (2 * dim A)`.

```lean
theorem isFiniteLocallyFreeOfRank_zpow_id (n : ℤ) (hn : n ≠ 0) :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((𝟙 A : A ⟶ A) ^ n).left
      (n.natAbs ^ (2 * abelianVarietyDimension A))
```

## Tag 0BFH, a lemma

[Tag 0BFH](https://stacks.math.columbia.edu/tag/0BFH) in the Stacks Project.

**`Stacks.Groupoids.etale_zpow_id_iff_isUnit_intCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/ZPowEtaleCriterion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/ZPowEtaleCriterion.lean#L232).

> **Stacks Project, Tag 0BFH.** Let `k` be a field and let `A` be a nonzero abelian variety
> over `k`.  Then `[d] : A → A` is étale if and only if `d` is invertible in `k`.
>
> Nonzeroness is the positivity of the topological Krull dimension, and it is used: it is what
> makes the relative tangent space at the identity nonzero, so that multiplication by `d` on that
> space is injective only for `d` invertible.  If `k` has characteristic `p` and `p` divides `d`
> then the derivative of `[d]` at the identity vanishes, and `[d]` is not étale.

```lean
theorem etale_zpow_id_iff_isUnit_intCast (k : Type u) [Field k] (A : Over (Spec (.of k)))
    [GrpObj A] [AlgebraicGeometry.IsAbelianVariety k A] (hA : 0 < topologicalKrullDim A.left)
    (d : ℤ) :
    Etale (((𝟙 A : A ⟶ A) ^ d).left) ↔ IsUnit ((d : ℤ) : k)
```

## Tag 0C0Y, a lemma

[Tag 0C0Y](https://stacks.math.columbia.edu/tag/0C0Y) in the Stacks Project.

**`Stacks.Groupoids.cardinalMk_fiber_multiplication_by_char_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowCharFibre.lean, line 1574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/ZPowCharFibre.lean#L1574).

> Let `k` be a field of characteristic `p > 0` and `A` an abelian variety of dimension `g` over
> `k`. The fibre of `[p] : A → A` over the identity has at most `p ^ g` distinct points. The fibre is
> the pullback of `[p]` along the identity section, and its points are counted by the cardinality of
> its underlying space.

```lean
theorem cardinalMk_fiber_multiplication_by_char_le {k : Type u} [Field k]
    (A : Over (Spec (.of k))) [GrpObj A] [AlgebraicGeometry.IsAbelianVariety k A] (p : ℕ)
    [CharP k p] (hp : 0 < p) :
    Cardinal.mk
      (pullback (η[A]).left (((𝟙 A : A ⟶ A) ^ (p : ℤ)).left) : Scheme.{u}) ≤
      p ^ abelianVarietyDimension A
```

## Tag 03RP, a proposition

[Tag 03RP](https://stacks.math.columbia.edu/tag/03RP) in the Stacks Project.

**`Stacks.Groupoids.etale_torsion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/Torsion.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/Torsion.lean#L88). The attribute's comment: “part (6), with the zero-dimensional case added”. References: SGA 3 XII (4.4.2), “partial”.

> **Stacks Project, Tag 03RP, part (6).** Let `A` be an abelian variety over a field `k` and
> `n` an integer.  The `n`-torsion group scheme `A[n] = Ker([n] : A → A)` is étale over `k` if and
> only if `n` is invertible in `k`, or `A` is zero-dimensional.
>
> The second alternative is a correction of the source, which omits it: for the zero abelian
> variety `A = Spec k`, every `A[n]` is `Spec k`, hence étale, also when `n = 0` in `k`.  For a
> nonzero abelian variety the statement is the source's.

```lean
theorem etale_torsion_iff (k : Type u) [Field k] (A : Over (Spec (.of k))) [GrpObj A]
    [AlgebraicGeometry.IsAbelianVariety k A] (n : ℤ) :
    Etale (GrpObj.torsion A n).X.hom ↔ topologicalKrullDim A.left = 0 ∨ IsUnit (n : k)
```

**`Stacks.Groupoids.surjective_zpow_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L68). The attribute's comment: “part (3), for every nonzero n”. References: SGA 7 IX (2.2.1), “more general”.

> Multiplication by a nonzero integer `n` on an abelian variety is surjective.

```lean
theorem surjective_zpow_id (n : ℤ) (hn : n ≠ 0) : Surjective ((𝟙 A : A ⟶ A) ^ n).left
```

**`Stacks.Groupoids.exists_pow_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L76). The attribute's comment: “part (4)”. References: SGA 3 VIII (7.11), “special case”.

> If `k` is algebraically closed, the group `A(k)` of rational points of an abelian variety is
> divisible: for every `n ≥ 1`, every rational point is an `n`-th power.

```lean
theorem exists_pow_eq [IsAlgClosed k] (n : ℕ) (hn : n ≠ 0)
    (x : 𝟙_ (Over (Spec (.of k))) ⟶ A) : ∃ y : 𝟙_ (Over (Spec (.of k))) ⟶ A, y ^ n = x
```

**`Stacks.Groupoids.isFiniteLocallyFreeOfRank_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L85). The attribute's comment: “part (5), for every nonzero n”.

> For a nonzero integer `n`, the `n`-torsion group scheme `A[n] = Ker([n] : A → A)` of an
> abelian variety `A` of dimension `g` is finite locally free of degree `|n| ^ 2g` over `k`.

```lean
theorem isFiniteLocallyFreeOfRank_torsion (n : ℤ) (hn : n ≠ 0) :
    Stacks.Morphisms.IsFiniteLocallyFreeOfRank (GrpObj.torsion A n).X.hom
      (n.natAbs ^ (2 * abelianVarietyDimension A))
```

**`Stacks.Groupoids.nonempty_torsionBy_addEquiv_of_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L95). The attribute's comment: “part (7)”.

> Let `A` be an abelian variety of dimension `g` over an algebraically closed field `k`, and `n`
> a natural number invertible in `k`. Then the `n`-torsion `A(k)[n]` of the group of rational points
> is isomorphic to `(ℤ/nℤ) ^ 2g`.

```lean
theorem nonempty_torsionBy_addEquiv_of_isUnit [IsAlgClosed k] (n : ℕ) (hn : IsUnit (n : k)) :
    Nonempty (AddSubgroup.torsionBy (Additive (𝟙_ (Over (Spec (.of k))) ⟶ A)) n ≃+
      (Fin (2 * abelianVarietyDimension A) → ZMod n))
```

**`Stacks.Groupoids.exists_torsionBy_char_pow_addEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/AbelianVariety/TorsionDegree.lean#L111). The attribute's comment: “part (8)”.

> Let `A` be an abelian variety of dimension `g` over an algebraically closed field `k` of
> characteristic `p > 0`. There is an integer `0 ≤ f ≤ g` such that `A(k)[p ^ m] ≅ (ℤ/p^mℤ) ^ f` for
> every `m` (for `m = 0` both sides are trivial).

```lean
theorem exists_torsionBy_char_pow_addEquiv [IsAlgClosed k] (p : ℕ) [CharP k p] (hp : 0 < p) :
    ∃ f ≤ abelianVarietyDimension A, ∀ m : ℕ, Nonempty
      (AddSubgroup.torsionBy (Additive (𝟙_ (Over (Spec (.of k))) ⟶ A)) ((p ^ m : ℕ) : ℤ) ≃+
        (Fin f → ZMod (p ^ m)))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isCommMonObj_of_isProper_of_geometricallyIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isCommMonObj_of_isProper_of_geometricallyIntegral#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVariety.lean#L98) (StacksFrontier): “commutative”. References: SGA 3 VIB (12.3), “special case”.
- [`AlgebraicGeometry.isProjective_of_isAbelianVariety`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyProjective.lean#L69), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyProjective.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyProjective.lean#L78) (StacksFrontier): “projective”.

## Tag 0H2U, a remark

[Tag 0H2U](https://stacks.math.columbia.edu/tag/0H2U) in the Stacks Project.

**`AlgebraicGeometry.isAbelianVariety_iff_of_choices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyEquivalentDefinitions.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/AbelianVarietyEquivalentDefinitions.lean#L265). References: EGA IV (15.6.10), “special case”; SGA 3 VIB (12.3), “more general”; SGA 3 VIB (7.8), “special case”; SGA 3 XV (4.6), “special case”; SGA 7 VIII (4.1), “Proper group schemes”.

> **Stacks Project, Tag 0H2U.** Let `k` be a field and `A` a group scheme over `k`. Pick one
> property from each of the three sets
>
> * projective, proper;
> * geometrically irreducible, irreducible, geometrically connected, connected;
> * smooth, geometrically reduced.
>
> Then `A` is an abelian variety if and only if it has the three chosen properties over `k`; so the
> sixteen choices are sixteen equivalent definitions of an abelian variety. The choice "proper,
> geometrically irreducible, geometrically reduced" recovers Definition 03RO.
>
> Every choice implies the weakest one, "proper, connected, geometrically reduced", which makes `A`
> an abelian variety (`AlgebraicGeometry.isAbelianVariety_of_choices`); conversely an abelian
> variety is projective by Tag 0BFA, smooth by Tag 0BFC and geometrically irreducible, which is the
> strongest choice and implies every other.

```lean
theorem isAbelianVariety_iff_of_choices
    (k : Type u) [Field k] (A : Over (Spec (.of k))) [GrpObj A] :
    ∀ P₁ ∈ [IsProjective A.hom, IsProper A.hom],
    ∀ P₂ ∈ [GeometricallyIrreducible A.hom, IrreducibleSpace A.left,
      GeometricallyConnected A.hom, ConnectedSpace A.left],
    ∀ P₃ ∈ [Smooth A.hom, GeometricallyReduced A.hom],
      (IsAbelianVariety k A ↔ P₁ ∧ P₂ ∧ P₃)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.9, Tag 0BF9](https://stacks.math.columbia.edu/tag/0BF9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
