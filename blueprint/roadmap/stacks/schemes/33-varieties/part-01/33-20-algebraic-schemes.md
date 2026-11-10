---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocallyOfFiniteType, AlgebraicGeometry.QuasiCompact, AlgebraicGeometry.exists_iso_coproduct_spec_local_artinian_of_dimension_zero, AlgebraicGeometry.isAffine_of_finiteType_of_dimension_zero, AlgebraicGeometry.isFinite_of_finiteType_of_dimension_zero, AlgebraicGeometry.isCatenarySpace_of_locallyOfFiniteType_over_field, AlgebraicGeometry.topologicalKrullDimAt_eq_krullDimOfRing_stalk, AlgebraicGeometry.topologicalKrullDimAt_eq_iSup_irreducibleComponents
statement: formalized
proof: formalized
---

# 33.20 Algebraic schemes

Section 33.20 of the Stacks Project, [Tag 06LF](https://stacks.math.columbia.edu/tag/06LF). 5 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06LG, a definition

[Tag 06LG](https://stacks.math.columbia.edu/tag/06LG) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L92) (StacksFrontier): “locally algebraic k-scheme, and the local half of algebraic k-scheme”. References: EGA I (6.3.1), “partial”; EGA I (6.6.2); EGA IV (1.3.2); SGA 3 VIB (1.3); SGA 4 Vbis (5.2.0), “partial”.
- [`AlgebraicGeometry.QuasiCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L103) (StacksFrontier): “the quasi-compact half of algebraic k-scheme”. References: EGA 0 (9.1.1), “special case”; EGA I (6.6.1); EGA IV (1.1.1); SGA 1 XIII (1.5); SGA 4 Vbis (4.2.0), “partial”; SGA 6 II (3.0); SGA 7 VII (1.3.8), “partial”.

## Tag 06LH, a lemma

[Tag 06LH](https://stacks.math.columbia.edu/tag/06LH) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_coproduct_spec_local_artinian_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean#L70). The attribute's comment: “locally algebraic case”.

> A zero-dimensional scheme locally of finite type over a field is, over that field, a
> coproduct of spectra of finite-dimensional local Artinian algebras.

```lean
theorem exists_iso_coproduct_spec_local_artinian_of_dimension_zero
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (hdim : topologicalKrullDim X = 0) :
    ∃ (I : Type u) (A : I → Type u)
      (_ : ∀ i, CommRing (A i))
      (_ : ∀ i, Algebra k (A i))
      (_ : ∀ i, IsLocalRing (A i))
      (_ : ∀ i, IsArtinianRing (A i))
      (_ : ∀ i, Module.Finite k (A i))
      (e : X ≅ ∐ fun i ↦ Spec (.of (A i))),
      e.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (A i)))) = f
```

**`AlgebraicGeometry.isAffine_of_finiteType_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean#L116). The attribute's comment: “affineness in the algebraic case”.

> A zero-dimensional scheme of finite type over a field is affine.

```lean
theorem isAffine_of_finiteType_of_dimension_zero
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim X = 0) : IsAffine X
```

**`AlgebraicGeometry.isFinite_of_finiteType_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Zero.lean#L125). The attribute's comment: “finiteness in the algebraic case”.

> The structure morphism of a zero-dimensional scheme of finite type over a field is finite.

```lean
theorem isFinite_of_finiteType_of_dimension_zero
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim X = 0) : IsFinite f
```

## Tag 0A21, a lemma

[Tag 0A21](https://stacks.math.columbia.edu/tag/0A21) in the Stacks Project.

**`AlgebraicGeometry.isCatenarySpace_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Catenary.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Catenary.lean#L81). The attribute's comment: “catenary”.

> The underlying topological space of a scheme locally of finite type over a field is
> catenary.

```lean
theorem isCatenarySpace_of_locallyOfFiniteType_over_field
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] :
    IrreducibleClosedsCodim.IsCatenarySpace X
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_krullDimOfRing_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ClosedPoint.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ClosedPoint.lean#L43). The attribute's comment: “dimension_at_closed_point”.

> At a closed point of a scheme locally of finite type over a field, the local dimension of
> the scheme equals the Krull dimension of its local ring.

```lean
theorem topologicalKrullDimAt_eq_krullDimOfRing_stalk
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X) (hx : IsClosed ({x} : Set X)) :
    topologicalKrullDimAt X x = ringKrullDim (X.presheaf.stalk x)
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_iSup_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Components.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Components.lean#L181). The attribute's comment: “local_dimension_components”.

> For a scheme locally of finite type over a field, the local dimension at a point is the
> largest dimension of an irreducible component containing that point.

```lean
theorem topologicalKrullDimAt_eq_iSup_irreducibleComponents
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X) :
    topologicalKrullDimAt X x =
      ⨆ Z ∈ {Z ∈ irreducibleComponents X | x ∈ Z}, topologicalKrullDim Z
```

**`AlgebraicGeometry.exists_mem_irreducibleComponents_topologicalKrullDim_eq_topologicalKrullDimAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Components.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Components.lean#L190). The attribute's comment: “local_dimension_components”. References: EGA IV (10.6.3), “sup_i dim(Y_i)”.

> The maximum dimension among the irreducible components through a point is attained.

```lean
theorem exists_mem_irreducibleComponents_topologicalKrullDim_eq_topologicalKrullDimAt
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X) :
    ∃ Z ∈ irreducibleComponents X,
      x ∈ Z ∧ topologicalKrullDim Z = topologicalKrullDimAt X x
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_trdeg_add_krullDim_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Formula.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Formula.lean#L99). The attribute's comment: “dimension_formula”. References: EGA IV (13.3.4), “special case”; EGA IV (17.15.8); EGA IV (5.2.3); SGA 1 II (5.8), “partial”; SGA 1 II (5.9), “n = trdeg_k κ(x) + p”.

> **Stacks Project, Tag 0A21.** The dimension at a point of a scheme locally of finite type
> over a field is the transcendence degree of its residue field plus the dimension of its local
> ring.

```lean
theorem topologicalKrullDimAt_eq_trdeg_add_krullDim_stalk
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (x : X) :
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    topologicalKrullDimAt X x =
      (Cardinal.toENat (Algebra.trdeg k (X.residueField x)) : WithBot ℕ∞) +
        ringKrullDim (X.presheaf.stalk x)
```

**`AlgebraicGeometry.trdeg_residueField_eq_add_one_of_isImmediateSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ImmediateSpecialization.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ImmediateSpecialization.lean#L57). The attribute's comment: “immediate_specialization_trdeg”.

> **Stacks Project, Tag 0A21.** For an immediate specialization in a scheme locally of finite
> type over a field, the transcendence degree of the residue field at the more general point is
> one greater than that at the more special point.

```lean
theorem trdeg_residueField_eq_add_one_of_isImmediateSpecialization
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] {x x' : X} (h : IsImmediateSpecialization x x') :
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    letI : Algebra k (X.residueField x') :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x').hom.toAlgebra
    Algebra.trdeg k (X.residueField x) = Algebra.trdeg k (X.residueField x') + 1
```

**`AlgebraicGeometry.krullDimOfRing_stalk_eq_add_one_of_isImmediateSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ImmediateSpecialization.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ImmediateSpecialization.lean#L222). The attribute's comment: “immediate_specialization_local_ring”.

> For an irreducible or equidimensional scheme locally of finite type over a field, local-ring
> dimension increases by one under an immediate specialization.

```lean
theorem krullDimOfRing_stalk_eq_add_one_of_isImmediateSpecialization
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x x' : X) (hxx' : IsImmediateSpecialization x x')
    (hX : IrreducibleSpace X ∨ TopologicalSpace.Equidimensional X) :
    ringKrullDim (X.presheaf.stalk x') =
      ringKrullDim (X.presheaf.stalk x) + 1
```

**`AlgebraicGeometry.exists_maximalChain_extending`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/MaximalChain.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/MaximalChain.lean#L121). The attribute's comment: “extend_irreducible_chain”.

> Any finite chain of irreducible closed subsets of an irreducible locally algebraic scheme
> over a field extends to a maximal chain.

```lean
lemma exists_maximalChain_extending
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [IrreducibleSpace X]
    (p : LTSeries (IrreducibleCloseds X)) :
    ∃ q : RelSeries {(Y, Z) : IrreducibleCloseds X × IrreducibleCloseds X | Y ⋖ Z},
      IsMin q.head ∧ IsMax q.last ∧ Set.range p ⊆ Set.range q
```

**`AlgebraicGeometry.maximalChain_length_eq_topologicalKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/MaximalChain.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/MaximalChain.lean#L255). The attribute's comment: “maximal_chain_length”.

> Every maximal chain of irreducible closed subsets of an irreducible locally algebraic
> scheme over a field has length equal to the dimension of the scheme.

```lean
theorem maximalChain_length_eq_topologicalKrullDim
    (k : Type u) [Field k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] [IrreducibleSpace X]
    (s : RelSeries {p : IrreducibleCloseds X × IrreducibleCloseds X | p.1 ⋖ p.2})
    (hmin : IsMin s.head) (hmax : IsMax s.last) :
    (s.length : WithBot ℕ∞) = topologicalKrullDim X
```

**`AlgebraicGeometry.topologicalKrullDim_eq_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/NonemptyOpen.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/NonemptyOpen.lean#L129). The attribute's comment: “dimension_nonempty_open”. References: SGA 3 VIB (1.5), “more general”.

> A nonempty open subset of an irreducible scheme locally of finite type over a field has the
> same Krull dimension as the whole scheme.

```lean
theorem topologicalKrullDim_eq_of_isOpen
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [IrreducibleSpace X] (U : Set X) (hU : IsOpen U)
    (hne : U.Nonempty) :
    topologicalKrullDim X = topologicalKrullDim U
```

**`AlgebraicGeometry.topologicalKrullDim_eq_topologicalKrullDimAt_of_irreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/NonemptyOpen.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/NonemptyOpen.lean#L170). The attribute's comment: “dimension_at_point_irreducible”.

> The dimension of an irreducible scheme locally of finite type over a field equals its
> dimension at every point.

```lean
theorem topologicalKrullDim_eq_topologicalKrullDimAt_of_irreducible
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [IrreducibleSpace X] (x : X) :
    topologicalKrullDim X = topologicalKrullDimAt X x
```

**`AlgebraicGeometry.topologicalKrullDimAt_le_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean#L56). The attribute's comment: “specialization_local_dimension”.

> Local Krull dimension cannot decrease along a specialization.

```lean
theorem topologicalKrullDimAt_le_of_specialization {X : Type*} [TopologicalSpace X] {x x' : X}
    (h : x ⤳ x') :
    topologicalKrullDimAt X x ≤ topologicalKrullDimAt X x'
```

**`AlgebraicGeometry.krullDimOfRing_stalk_lt_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean#L65). The attribute's comment: “specialization_stalk_dimension”.

> A nontrivial specialization on a scheme locally of finite type over a field strictly
> increases the Krull dimension of the local ring.

```lean
theorem krullDimOfRing_stalk_lt_of_specialization
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    {x x' : X} (hxx' : x ⤳ x') (hne : x ≠ x') :
    ringKrullDim (X.presheaf.stalk x) < ringKrullDim (X.presheaf.stalk x')
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_iInf_closedSpecializations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Specialization.lean#L126). The attribute's comment: “local_dimension_closed_specializations”.

> For a scheme locally of finite type over a field, its local dimension at a point is the
> minimum of the dimensions of the local rings at the closed specializations of that point.

```lean
theorem topologicalKrullDimAt_eq_iInf_closedSpecializations
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x : X) :
    topologicalKrullDimAt X x =
      ⨅ (x' : {x' : X // x ⤳ x' ∧ IsClosed ({x'} : Set X)}),
        ringKrullDim (X.presheaf.stalk x')
```

**`AlgebraicGeometry.length_eq_trdeg_sub_of_maximalSpecializationChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/SpecializationChain.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/SpecializationChain.lean#L100). The attribute's comment: “specialization_chain_length”.

> The length of a maximal chain of nontrivial specializations on a scheme locally of finite
> type over a field is the drop in transcendence degree of the residue fields at its endpoints.

```lean
theorem length_eq_trdeg_sub_of_maximalSpecializationChain
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] (x x' : X) (_hxx' : x ⤳ x') (_hne : x ≠ x')
    (c : RelSeries {p : X × X | p.1 ⤳ p.2 ∧ p.1 ≠ p.2})
    (hc : IsMaximalSpecializationChain c) (hhead : c.head = x) (hlast : c.last = x') :
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    letI : Algebra k (X.residueField x') :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x').hom.toAlgebra
    c.length = Cardinal.toNat (Algebra.trdeg k (X.residueField x)) -
      Cardinal.toNat (Algebra.trdeg k (X.residueField x'))
```

**`AlgebraicGeometry.trdeg_residueField_lt_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/SpecializationTrdeg.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/SpecializationTrdeg.lean#L51). The attribute's comment: “specialization_trdeg”.

> On a scheme locally of finite type over a field, residue-field transcendence degree strictly
> decreases along a nontrivial specialization.

```lean
theorem trdeg_residueField_lt_of_specialization
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    {x x' : X} (hxx' : x ⤳ x') (hne : x ≠ x') :
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    letI : Algebra k (X.residueField x') :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x').hom.toAlgebra
    Algebra.trdeg k (X.residueField x') < Algebra.trdeg k (X.residueField x)
```

**`AlgebraicGeometry.topologicalKrullDim_eq_trdeg_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Trdeg.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Trdeg.lean#L100). The attribute's comment: “irreducible_dimension_trdeg”. References: EGA IV (4.1.1), “special case”; EGA IV (5.2.1).

> **Stacks Project, Tag 0A21.** The dimension of an irreducible scheme locally of finite type
> over a field equals the transcendence degree of its residue field at a generic point.

```lean
theorem topologicalKrullDim_eq_trdeg_residueField
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IrreducibleSpace X] [LocallyOfFiniteType f] (x : X)
    (hx : IsGenericPoint x Set.univ) :
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    topologicalKrullDim X =
      (Cardinal.toENat (Algebra.trdeg k (X.residueField x)) : WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDim_eq_iSup_trdeg_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Trdeg.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/Trdeg.lean#L202). The attribute's comment: “dimension_sup_trdeg”. References: EGA IV (4.1.1); EGA IV (5.2.1), “more general”; EGA IV (5.2.2).

> **Stacks Project, Tag 0A21.** The dimension of a scheme locally of finite type over a field
> is the supremum of the transcendence degrees of the residue fields at the generic points of its
> irreducible components.

```lean
theorem topologicalKrullDim_eq_iSup_trdeg_residueField
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] :
    topologicalKrullDim X =
      ⨆ x : genericPoints X,
        letI : Algebra k (X.residueField x.1) :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x.1).hom.toAlgebra
        (Cardinal.toENat (Algebra.trdeg k (X.residueField x.1)) : WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDimAt_eq_add_ringKrullDim_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Correspondences/GraphCodimension.lean#L107). The attribute's comment: “local dimension, point closure and local ring”. References: EGA IV (10.6.3), “special case”.

> **Stacks 0A21.** On a scheme locally of finite type over a field the dimension at a point is
> the dimension of the closure of that point plus the dimension of the local ring there. Both
> summands are read off the dimension formula of Stacks 0A21 at the same point.

```lean
theorem topologicalKrullDimAt_eq_add_ringKrullDim_stalk (k : Type u) [Field k] {T : Scheme.{u}}
    (q : T ⟶ Spec (.of k)) [LocallyOfFiniteType q] (t : T) :
    topologicalKrullDimAt T t =
      topologicalKrullDim (closure ({t} : Set T)) + ringKrullDim (T.presheaf.stalk t)
```

## Tag 0B2L, a lemma

[Tag 0B2L](https://stacks.math.columbia.edu/tag/0B2L) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFiniteType_fiberToSpecResidueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Fibre.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Fibre.lean#L66). The attribute's comment: “locally_algebraic_fibre”.

> A fibre of a morphism between locally algebraic schemes is locally algebraic over the
> residue field of the corresponding point.

```lean
public theorem locallyOfFiniteType_fiberToSpecResidueField
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (y : Y) :
    LocallyOfFiniteType (f.fiberToSpecResidueField y)
```

**`AlgebraicGeometry.topologicalKrullDim_le_fiber_add_imageClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean#L325). The attribute's comment: “part (2a): dim_x(X_{f(x)}) ≥ d”. References: EGA IV (10.6.1), “(iii), special case”.

> **Lower bound for the fibre dimension.** For a morphism `f : X ⟶ Y` of schemes locally of
> finite type over a field with `X` irreducible, the local dimension of every fibre of `f` is at
> least the dimension of `X` minus the dimension of the reduced closure of the image of `f`. The
> bound is stated additively, since `WithBot ℕ∞` has no subtraction.

```lean
public theorem topologicalKrullDim_le_fiber_add_imageClosure
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY] [IrreducibleSpace X]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (x : X) :
    topologicalKrullDim X ≤
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) +
        topologicalKrullDim
        (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure (Set.range (fun x : X => f x)))).subscheme
```

**`AlgebraicGeometry.isOpen_and_dense_setOf_topologicalKrullDimAt_fiber_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean#L404). The attribute's comment: “part (2b): {x | dim_x(X_{f(x)}) = d} is dense open”.

> **The fibre dimension is generically the expected one.** For a morphism `f : X ⟶ Y` of schemes
> locally of finite type over a field with `X` irreducible, the set of points at which the local
> fibre dimension attains the value `d = dim X - dim Z` is a dense open subset of `X`. Here `Z` is
> the reduced closure of the image of `f`, and `d` is the difference of the two dimensions taken in
> `ℕ`, since `WithBot ℕ∞` has no subtraction.

```lean
public theorem isOpen_and_dense_setOf_topologicalKrullDimAt_fiber_eq
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY] [IrreducibleSpace X]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (d : ℕ)
    (hd : d = ((topologicalKrullDim X).unbotD 0).toNat -
      ((topologicalKrullDim
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure (Set.range (fun x : X => f x)))).subscheme).unbotD 0).toNat) :
    IsOpen {x : X | topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞)} ∧
      Dense {x : X |
        topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞)}
```

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_add_one_le_of_one_le_ringKrullDim_imageClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean#L571). The attribute's comment: “part (2c): dim_x(X_{f(x)}) ≤ d + dim O_{Z,f(x)} - 1”.

> **Upper bound for the fibre dimension over a point of higher codimension.** For a morphism
> `f : X ⟶ Y` of schemes locally of finite type over a field with `X` irreducible, if the local ring
> of the reduced closure `Z` of the image of `f` at `f x` has dimension at least one, then
>
> `dim_x(X_{f(x)}) ≤ d + dim 𝒪_{Z, f(x)} - 1`,
>
> where `d = dim X - dim Z`. Since `WithBot ℕ∞` has no subtraction, the bound is stated by adding
> one to the left-hand side, as in Tag 0B2K. The point of `Z` over `f x` is given by `z`.

```lean
public theorem topologicalKrullDimAt_fiber_add_one_le_of_one_le_ringKrullDim_imageClosure
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY] [IrreducibleSpace X]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (d : ℕ)
    (hd : d = ((topologicalKrullDim X).unbotD 0).toNat -
      ((topologicalKrullDim
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure (Set.range (fun x : X => f x)))).subscheme).unbotD 0).toNat)
    (x : X)
    (z : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure (Set.range (fun x : X => f x)))).subscheme)
    (hz : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure (Set.range (fun x : X => f x)))).subschemeι z = f x)
    (h1 : 1 ≤ ringKrullDim
      ((Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure (Set.range (fun x : X => f x)))).subscheme.presheaf.stalk z)) :
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) + 1 ≤
      (d : WithBot ℕ∞) + ringKrullDim
        ((Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure (Set.range (fun x : X => f x)))).subscheme.presheaf.stalk z)
```

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_ringKrullDim_imageClosure_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean#L621). The attribute's comment: “part (2d): dim O_{Z,f(x)} = 1 implies dim_x(X_{f(x)}) = d”.

> **The fibre dimension over a point of codimension one.** For a morphism `f : X ⟶ Y` of schemes
> locally of finite type over a field with `X` irreducible, if the local ring of the reduced closure
> `Z` of the image of `f` at `f x` has dimension exactly one, then `dim_x(X_{f(x)}) = d`, where
> `d = dim X - dim Z`. The point of `Z` over `f x` is given by `z`.

```lean
public theorem topologicalKrullDimAt_fiber_eq_of_ringKrullDim_imageClosure_eq_one
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY] [IrreducibleSpace X]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (d : ℕ)
    (hd : d = ((topologicalKrullDim X).unbotD 0).toNat -
      ((topologicalKrullDim
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure (Set.range (fun x : X => f x)))).subscheme).unbotD 0).toNat)
    (x : X)
    (z : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure (Set.range (fun x : X => f x)))).subscheme)
    (hz : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure (Set.range (fun x : X => f x)))).subschemeι z = f x)
    (h1 : ringKrullDim
      ((Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure (Set.range (fun x : X => f x)))).subscheme.presheaf.stalk z) = 1) :
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDimAt_le_fiber_add_topologicalKrullDimAt_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/FibreDimension.lean#L686). The attribute's comment: “part (3): dim_x(X_y) ≥ dim_x(X) - dim_y(Y)”.

> **Local lower bound for the fibre dimension.** For a morphism `f : X ⟶ Y` of schemes locally of
> finite type over a field and any point `x` of `X` with image `y = f x`,
>
> `dim_x(X_y) ≥ dim_x(X) - dim_y(Y)`.
>
> The source is not assumed irreducible: the bound is obtained by applying part (2a) to each
> irreducible component of `X` through `x`, carrying the reduced induced structure. As elsewhere,
> the statement is additive because `WithBot ℕ∞` has no subtraction.

```lean
public theorem topologicalKrullDimAt_le_fiber_add_topologicalKrullDimAt_target
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType pX] [LocallyOfFiniteType pY]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (x : X) :
    topologicalKrullDimAt X x ≤
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) + topologicalKrullDimAt Y (f x)
```

## Tag 0B2M, a lemma

[Tag 0B2M](https://stacks.math.columbia.edu/tag/0B2M) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Product.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Product.lean#L112). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0B2M, part (1).** Let `X` and `Y` be locally algebraic schemes over a
> field `k`. At a point `z` of the product `X ×_{Spec k} Y`, the local dimension of the product is
> the sum of the local dimensions of `X` and of `Y` at the two images of `z`.

```lean
theorem topologicalKrullDimAt_pullback (k : Type u) [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [LocallyOfFiniteType g] (z : ↑(pullback f g)) :
    topologicalKrullDimAt ↑(pullback f g) z =
      topologicalKrullDimAt X ((pullback.fst f g) z) +
        topologicalKrullDimAt Y ((pullback.snd f g) z)
```

**`AlgebraicGeometry.topologicalKrullDim_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Product.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/Product.lean#L131). The attribute's comment: “part (2)”. References: EGA IV (4.1.5).

> **Stacks Project, Tag 0B2M, part (2).** Let `X` and `Y` be locally algebraic schemes over a
> field `k`. The dimension of the product `X ×_{Spec k} Y` is the sum of the dimensions of `X` and
> of `Y`.

```lean
theorem topologicalKrullDim_pullback (k : Type u) [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [LocallyOfFiniteType g] :
    topologicalKrullDim ↑(pullback f g) = topologicalKrullDim X + topologicalKrullDim Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.20, Tag 06LF](https://stacks.math.columbia.edu/tag/06LF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
