---
declaration: section
origin: cited
lean: AlgebraicGeometry.geometricGenus, AlgebraicGeometry.geometricGenus_eq_sum_components, AlgebraicGeometry.geometricGenus_reduction_birational_normalization, AlgebraicGeometry.genus_le_of_isAffineHom_of_isZero, AlgebraicGeometry.genus_le_of_isFinite_of_isClosedImmersion_over_dense_open, AlgebraicGeometry.genus_le_and_isIso_of_isProper_of_isBirational, AlgebraicGeometry.geometricGenus_le_finSepDegree_mul_genus_toSpecΓ, AlgebraicGeometry.geometricGenus_le_genus_of_irreducible
statement: formalized
proof: formalized
---

# 53.18 Genus versus geometric genus

Section 53.18 of the Stacks Project, [Tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CE0, the section

[Tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0) in the Stacks Project.

**`AlgebraicGeometry.geometricGenus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Geometric.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/Geometric.lean#L83). The attribute's comment: “definition of the geometric genus g\_geom(X/k)”.

> The geometric genus `g_geom(X/k)` of a proper scheme `X` over a field `k`: the sum, over the
> irreducible components of dimension one of the base change of `X` to an algebraic closure of
> `k`, of the genus of the normalization of that component with its reduced structure.
>
> This is the invariant introduced in the preamble of the source's section on genus versus
> geometric genus.

```lean
public def geometricGenus (k : Type u) [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k))
    [IsProper g] : ℕ
```

## Tag 0CE1, a lemma

[Tag 0CE1](https://stacks.math.columbia.edu/tag/0CE1) in the Stacks Project.

**`AlgebraicGeometry.geometricGenus_eq_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricComponents.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricComponents.lean#L348).

> Let `k` be a field and let `X` be a proper scheme of dimension at most one over `k`. The
> geometric genus of `X` over `k` is the sum of the geometric genera of
> the irreducible components of `X` of dimension one, each taken with its reduced closed subscheme
> structure; components of dimension zero contribute nothing.

```lean
public theorem geometricGenus_eq_sum_components {k : Type u} [Field k]
    {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (hX : topologicalKrullDim X ≤ 1) :
    letI : IsNoetherian X :=
      { toIsLocallyNoetherian := LocallyOfFiniteType.isLocallyNoetherian g
        toCompactSpace := QuasiCompact.compactSpace_of_compactSpace g }
    letI : Finite (irreducibleComponents X) :=
      (finite_irreducibleComponents_of_isNoetherian (X := X)).to_subtype
    letI : Fintype (irreducibleComponents X) := Fintype.ofFinite _
    geometricGenus k g =
      ∑ C : irreducibleComponents X,
        if topologicalKrullDim (irreducibleComponentIdeal C).subscheme = 1 then
          geometricGenus k ((irreducibleComponentIdeal C).subschemeι ≫ g)
        else 0
```

## Tag 0CE2, a lemma

[Tag 0CE2](https://stacks.math.columbia.edu/tag/0CE2) in the Stacks Project.

**`AlgebraicGeometry.geometricGenus_reduction_birational_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusBirational.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusBirational.lean#L215).

> Let `k` be a field and let `X` be a proper scheme of dimension at most one over `k`.  Then
>
> 1. the reduction `X_red` has the same geometric genus as `X`;
> 2. the source of a birational proper morphism `X' ⟶ X` has the same geometric genus as `X`; and
> 3. the normalization `X^ν` has the same geometric genus as `X`.

```lean
public theorem geometricGenus_reduction_birational_normalization {k : Type u} [Field k]
    {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (hX : topologicalKrullDim (X : Type u) ≤ 1) :
    letI : IsProper (normalizationOverField k g ≫ g) :=
      isProper_normalizationOverField_comp k g
    geometricGenus k (X.reductionι ≫ g) = geometricGenus k g ∧
      (∀ (X' : Scheme.{u}) (f : X' ⟶ X) [IsProper f], IsBirational f →
        geometricGenus k (f ≫ g) = geometricGenus k g) ∧
      geometricGenus k (normalizationOverField k g ≫ g) = geometricGenus k g
```

## Tag 0CE3, a lemma

[Tag 0CE3](https://stacks.math.columbia.edu/tag/0CE3) in the Stacks Project.

**`AlgebraicGeometry.genus_le_of_isAffineHom_of_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GenusGoesDown.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GenusGoesDown.lean#L282). The attribute's comment: “with the two cohomology vanishings and the finiteness of H¹(X,𝒪\_X) as hypotheses”.

> **[Stacks, Tag 0CE3] with its three cohomological inputs as hypotheses.** Let `f : Y ⟶ X` be
> an affine morphism of schemes over a field `k`, and let `φ : 𝒪_X ⟶ f_*𝒪_Y` be the canonical
> comparison map. If `H¹(X, coker φ) = 0`, if `H²(X, ker φ) = 0` and if `H¹(X, 𝒪_X)` is finite
> dimensional over `k`, then the genus of `Y` is at most the genus of `X`, that is
> `dim_k H¹(Y, 𝒪_Y) ≤ dim_k H¹(X, 𝒪_X)`.
>
> The three hypotheses replace the properness of `X` over `k`, the bound on its dimension and the
> hypothesis that `f` is a closed immersion over a dense open, which the source uses only to
> produce them; see the implementation notes of this file.

```lean
theorem genus_le_of_isAffineHom_of_isZero (f : Y ⟶ X) [IsAffineHom f]
    (hcoker : IsZero (cohomologyOverField k g (cokernel (structureSheafToPushforward f)) 1))
    (hker : IsZero (cohomologyOverField k g (kernel (structureSheafToPushforward f)) 2))
    (hfin : FiniteDimensional k (cohomologyOverField k g (structureSheafModule X) 1)) :
    genus (f ≫ g) ≤ genus g
```

**`AlgebraicGeometry.genus_le_of_isFinite_of_isClosedImmersion_over_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GenusGoesDownUnconditional.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GenusGoesDownUnconditional.lean#L222).

> **[Stacks, Tag 0CE3].** Let `k` be a field, let `g : X ⟶ Spec k` be proper with
> `dim X ≤ 1`, and let `f : Y ⟶ X` be finite and a closed immersion over a dense open `U ⊆ X`.
> Then the genus of `Y` is at most the genus of `X`, that is
> `dim_k H¹(Y, 𝒪_Y) ≤ dim_k H¹(X, 𝒪_X)`.
>
> This is `AlgebraicGeometry.genus_le_of_isAffineHom_of_isZero` with its three cohomological
> hypotheses discharged; see the module docstring.

```lean
theorem genus_le_of_isFinite_of_isClosedImmersion_over_dense_open
    (k : Type u) [Field k] {X Y : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (f : Y ⟶ X) [IsFinite f] (hdim : topologicalKrullDim (X : Type u) ≤ 1)
    (U : X.Opens) (hdense : Dense (U : Set X))
    (hclosed : IsClosedImmersion (pullback.snd f U.ι)) :
    genus (f ≫ g) ≤ genus g
```

## Tag 0CE4, a lemma

[Tag 0CE4](https://stacks.math.columbia.edu/tag/0CE4) in the Stacks Project.

**`AlgebraicGeometry.genus_le_and_isIso_of_isProper_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BirationalGenus.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/BirationalGenus.lean#L239).

> Let `k` be a field and let `X` be a proper scheme of dimension at most one over `k`. If
> `f : X' ⟶ X` is a birational proper morphism, then
>
>   `dim_k H¹(X, 𝒪_X) ≥ dim_k H¹(X', 𝒪_{X'})`,
>
> and if moreover `X` is reduced, `H⁰(X, 𝒪_X) ⟶ H⁰(X', 𝒪_{X'})` is surjective and equality holds,
> then `X' = X`.
>
> Here `dim_k H¹` is `AlgebraicGeometry.genus` of the structure morphism, and `X' = X` means that
> `f` is an isomorphism of schemes.

```lean
theorem genus_le_and_isIso_of_isProper_of_isBirational [IsProper g] (f : X' ⟶ X) [IsProper f]
    (hf : IsBirational f) (hX : topologicalKrullDim (X : Type u) ≤ 1) :
    genus (f ≫ g) ≤ genus g ∧
      (IsReduced X → Function.Surjective f.appTop → genus (f ≫ g) = genus g → IsIso f)
```

## Tag 0CE5, a lemma

[Tag 0CE5](https://stacks.math.columbia.edu/tag/0CE5) in the Stacks Project.

**`AlgebraicGeometry.geometricGenus_le_finSepDegree_mul_genus_toSpecΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusIrreducible.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusIrreducible.lean#L233). The attribute's comment: “κ = k, geometrically integral of dim 1, 0CE3's vanishings and H¹ finite”.

> Let `k` be a field and let `X` be a proper integral scheme over `k` whose global regular
> functions are exactly `k` and whose base change to an algebraic closure of `k` is irreducible,
> reduced and of dimension one.  Writing `κ = Γ(X, ⊤)`, the geometric genus of `X` over `k` is at
> most `[κ : k]_s · dim_κ H¹(X, 𝒪_X)`.

```lean
public theorem geometricGenus_le_finSepDegree_mul_genus_toSpecΓ
    (k : Type u) [Field k] {X : Scheme.{u}} [IsIntegral X] (g : X ⟶ Spec (.of k)) [IsProper g]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ g.appTop)]
    (hirr : IrreducibleSpace (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))))
    (hred : IsReduced (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))))
    (hdim : topologicalKrullDim (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))) = 1)
    (hcoker : IsZero (cohomologyOverField (AlgebraicClosure k)
      (pullback.snd g (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))
      (cokernel (structureSheafToPushforward (normalizationOverField (AlgebraicClosure k)
        (pullback.snd g
          (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))))) 1))
    (hker : IsZero (cohomologyOverField (AlgebraicClosure k)
      (pullback.snd g (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))
      (kernel (structureSheafToPushforward (normalizationOverField (AlgebraicClosure k)
        (pullback.snd g
          (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))))) 2))
    (hfin : FiniteDimensional (AlgebraicClosure k) (cohomologyOverField (AlgebraicClosure k)
      (pullback.snd g (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))
      (structureSheafModule (pullback (C := Scheme.{u}) g
        (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k)))))) 1)) :
    letI : Field Γ(X, ⊤) := (isField_of_universallyClosed k g).toField
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ g.appTop).hom.toAlgebra
    geometricGenus k g ≤ Field.finSepDegree k Γ(X, ⊤) * genus X.toSpecΓ
```

**`AlgebraicGeometry.geometricGenus_le_genus_of_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusIrreducibleUnconditional.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusIrreducibleUnconditional.lean#L73). The attribute's comment: “κ = k, geometrically irreducible of dimension one”.

> Let `k` be a field and `g : X ⟶ Spec k` proper. If the base change `X_{k̄}` of `X` to an
> algebraic closure `k̄` of `k` is irreducible, reduced and of dimension one, then
> `g_geom(X/k) ≤ g(X)`.

```lean
theorem geometricGenus_le_genus_of_irreducible
    (k : Type u) [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (hirr : IrreducibleSpace (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))))
    (hred : IsReduced (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))))
    (hdim : topologicalKrullDim (pullback (C := Scheme.{u}) g
      (Spec.map (CommRingCat.ofHom (algebraMap k (AlgebraicClosure k))))) = 1) :
    geometricGenus k g ≤ genus g
```

**`AlgebraicGeometry.geometricGenus_le_genus_of_dim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusLeGenusUnconditional.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/GeometricGenusLeGenusUnconditional.lean#L139). The attribute's comment: “the per-fibre bound, over an algebraically closed field”.

> **The per-fibre bound of [Stacks, Tag 0CE5].**  Over an algebraically closed field `K`, the
> geometric genus of a proper scheme of dimension at most one is at most its genus.  No hypothesis
> is made on the irreducible components: the scheme may be reducible and non-reduced.

```lean
public theorem geometricGenus_le_genus_of_dim_le_one (K : Type u) [Field K] [IsAlgClosed K]
    {Z : Scheme.{u}} (q : Z ⟶ Spec (.of K)) [IsProper q]
    (hdim : topologicalKrullDim (Z : Type u) ≤ 1) :
    geometricGenus K q ≤ genus q
```

**`AlgebraicGeometry.geometricGenus_le_finSepDegree_mul_genus_toSpecΓ_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/SeparableDegreeFibreSum.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GenusCurve/SeparableDegreeFibreSum.lean#L132).

> **Stacks Project, Tag 0CE5.**  Let `C` be a proper curve over a field `k` and let
> `κ = Γ(C, ⊤)` be its field of global regular functions.  Then the geometric genus of `C` over `k`
> is at most `[κ : k]_s · dim_κ H¹(C, 𝒪_C)`.
>
> The sum over the `k`-embeddings `κ → k̄` is
> `AlgebraicGeometry.geometricGenus_eq_finsum_geometricGenus_pullback_snd_toSpecΓ`, and each of its
> terms is bounded by the genus of the corresponding fibre by
> `AlgebraicGeometry.geometricGenus_le_genus_of_dim_le_one`, the fibre being a proper scheme of
> dimension one over the algebraically closed field `k̄`.

```lean
public theorem geometricGenus_le_finSepDegree_mul_genus_toSpecΓ_of_isCurve
    (k : Type u) [Field k] {C : Scheme.{u}} (f : C ⟶ Spec (.of k)) [IsCurve k f] [IsProper f] :
    letI : Field Γ(C, ⊤) := (isField_of_universallyClosed k f).toField
    letI : Algebra k Γ(C, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    letI : IsProper C.toSpecΓ := isProper_toSpecΓ f
    geometricGenus k f ≤ Field.finSepDegree k Γ(C, ⊤) * genus C.toSpecΓ
```

## Tag 0CE6, a lemma

[Tag 0CE6](https://stacks.math.columbia.edu/tag/0CE6) in the Stacks Project.

**`AlgebraicGeometry.finrank_picardTorsion_le_genus_add_geometricGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionRankConnectedComponents.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Picard/TorsionRankConnectedComponents.lean#L203).

> **Stacks Project, Tag 0CE6.**  Let `k` be a field, let `X` be a proper scheme of dimension at
> most one over `k` and let `ℓ` be a prime invertible in `k`.  Then the `ℓ`-torsion of `Pic(X)` is
> finite-dimensional
> over `F_ℓ` and
>
> `dim_{F_ℓ} Pic(X)[ℓ] ≤ dim_k H¹(X, 𝒪_X) + g_geom(X/k)`.
>
> The proof is the source's: extend the ground field to an algebraic closure and pass to the
> reduction (`AlgebraicGeometry.picardTorsion_bound_of_reducedBaseChange`, which is Tag 0CC5, Tag
> 02KH, Tag 0CE2 (1) and Tag 0CE3), then decompose into connected components
> (`AlgebraicGeometry.picardTorsion_bound_of_connectedComponents`) and apply Tag 0C20 to the
> one-dimensional ones, the zero-dimensional ones having trivial Picard group.

```lean
theorem finrank_picardTorsion_le_genus_add_geometricGenus (k : Type u) [Field k]
    {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) (ℓ : ℕ) [Fact ℓ.Prime] (hℓ : IsUnit (ℓ : k)) :
    FiniteDimensional (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) ∧
      Module.finrank (ZMod ℓ) (AddSubgroup.torsionBy (ofScheme X) (ℓ : ℤ)) ≤
        genus g + geometricGenus k g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.18, Tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
