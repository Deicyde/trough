---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_constructible_partition_finite_etale, AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict, AlgebraicGeometry.exists_finite_affine_stratification_split_reduction, AlgebraicGeometry.exists_surjective_affine_baseChange_thickening_finiteEtale
statement: formalized
proof: formalized
---

# 59.72 Auxiliary lemmas on morphisms

Section 59.72 of the Stacks Project, [Tag 095J](https://stacks.math.columbia.edu/tag/095J). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03S0, a lemma

[Tag 03S0](https://stacks.math.columbia.edu/tag/03S0) in the Stacks Project.

**`AlgebraicGeometry.exists_constructible_partition_finite_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/FiniteEtaleStratification.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/FiniteEtaleStratification.lean#L574).

> Let `f : U ⟶ X` be an étale morphism of quasi-compact and quasi-separated schemes. Then `X`
> has a partition into constructible locally closed subschemes over each of which the base change
> of `f` is finite étale.

```lean
public theorem exists_constructible_partition_finite_etale
    {U X : Scheme.{u}} [CompactSpace U] [QuasiSeparatedSpace U]
    [CompactSpace X] [QuasiSeparatedSpace X] (f : U ⟶ X) [Etale f] :
    ∃ P : Set (Set X), IsTopologicalPartition P ∧
      (∀ S ∈ P, Topology.IsConstructible S) ∧
      (∀ S ∈ P, ∃ (Y : Scheme.{u}) (i : Y ⟶ X),
        IsImmersion i ∧ Set.range i.base = S ∧
          IsFinite (pullback.fst i f) ∧ Etale (pullback.fst i f))
```

## Tag 03S1, a lemma

[Tag 03S1](https://stacks.math.columbia.edu/tag/03S1) in the Stacks Project.

**`AlgebraicGeometry.finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/GenericallyFinite.lean#L513). The attribute's comment: “forward direction over an affine open”.

> **Stacks Project, Tag 02NW, condition (4).** For a quasi-compact and quasi-separated
> morphism locally of finite type, finiteness of the fibre over a generic point of an
> irreducible component is equivalent to finiteness over some affine neighbourhood of the
> point.

```lean
theorem finite_preimage_singleton_iff_exists_affine_open_isFinite_restrict
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiCompact f]
    [QuasiSeparated f] (η : Y) (hη : η ∈ genericPoints Y) :
    (f ⁻¹' {η}).Finite ↔
      ∃ V : Y.affineOpens, (η ∈ V.1) ∧ IsFinite (f ∣_ V.1)
```

## Tag 095K, a lemma

[Tag 095K](https://stacks.math.columbia.edu/tag/095K) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_affine_stratification_split_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChangeDecomposition.lean, line 2088](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChangeDecomposition.lean#L2088). The attribute's comment: “part (2)”.

> A finite locally free cover of each affine stratum splits the reduced pullback into
> finitely many copies of the reduced covering scheme.

```lean
public theorem exists_finite_affine_stratification_split_reduction
    {Y X : Scheme.{u}} (f : Y ⟶ X) [IsAffine Y] [IsAffine X]
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyQuasiFinite f]
    (hfp : FinitePresentation f) :
    ∃ (n : ℕ) (S : Fin n → Scheme.{u}) (s : ∀ i, S i ⟶ X),
      (∀ i, IsAffine (S i) ∧ IsImmersion (s i) ∧
        IsLocallyClosed (Set.range (s i).base) ∧
        Topology.IsConstructible (Set.range (s i).base)) ∧
      (∀ i j, i ≠ j → Disjoint (Set.range (s i).base) (Set.range (s j).base)) ∧
      (⋃ i, Set.range (s i).base) = Set.univ ∧
      ∀ i, ∃ (S' : Scheme.{u}) (g : S' ⟶ S i),
        Surjective g ∧ Stacks.Morphisms.IsFiniteLocallyFree g ∧
        ∃ (m : ℕ)
          (q : (pullback f (g ≫ s i)).nilradical.subscheme ⟶
            S'.nilradical.subscheme)
          (e : (pullback f (g ≫ s i)).nilradical.subscheme ≅
            ∐ (fun _ : Fin m ↦ S'.nilradical.subscheme)),
          q ≫ S'.nilradical.subschemeι =
              (pullback f (g ≫ s i)).nilradical.subschemeι ≫
                pullback.snd f (g ≫ s i) ∧
          e.hom ≫ Sigma.desc (fun _ : Fin m ↦ 𝟙 S'.nilradical.subscheme) = q
```

**`AlgebraicGeometry.exists_surjective_affine_baseChange_thickening_finiteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChangeDecomposition.lean, line 2150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/BaseChangeDecomposition.lean#L2150). The attribute's comment: “part (1)”.

> After a surjective affine base change, the pullback contains a finite étale thickening.

```lean
public theorem exists_surjective_affine_baseChange_thickening_finiteEtale
    {Y X : Scheme.{u}} (f : Y ⟶ X) [IsAffine Y] [IsAffine X]
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyQuasiFinite f]
    (hfp : FinitePresentation f) :
    ∃ (X' : Scheme.{u}) (_ : IsAffine X') (g : X' ⟶ X),
      Surjective g ∧
      ∃ (Z' : Scheme.{u}) (i : Z' ⟶ pullback f g),
        Stacks.Thickenings.IsThickening i ∧
        IsFinite (i ≫ pullback.snd f g) ∧
        Etale (i ≫ pullback.snd f g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.72, Tag 095J](https://stacks.math.columbia.edu/tag/095J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
