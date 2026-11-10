---
declaration: section
origin: cited
lean: AlgebraicGeometry.quasiFiniteAt_of_target_stalk_dimension_le_one, AlgebraicGeometry.exists_isFinite_morphismRestrict_of_ringKrullDim_stalk_le_one, AlgebraicGeometry.exists_isIso_restrict_of_finite_fiber_of_normal, AlgebraicGeometry.mem_maximal_isomorphism_open_of_quasiFiniteAt_of_isNormal, AlgebraicGeometry.mem_maximal_isomorphism_open_of_mem_genericPoints, AlgebraicGeometry.mem_maximal_isomorphism_open_of_isDiscreteValuationRing
statement: formalized
proof: formalized
---

# 33.17 Generically finite morphisms

Section 33.17 of the Stacks Project, [Tag 0AB5](https://stacks.math.columbia.edu/tag/0AB5). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AB6, a lemma

[Tag 0AB6](https://stacks.math.columbia.edu/tag/0AB6) in the Stacks Project.

**`AlgebraicGeometry.quasiFiniteAt_of_target_stalk_dimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiFiniteCodimensionOne.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiFiniteCodimensionOne.lean#L157).

> **Stacks Project, Tag 0AB6.** A locally finite type morphism which is generically
> quasi-finite is quasi-finite above a point with Noetherian local ring of dimension at most
> one. It suffices to impose the generic condition only on components whose generic points
> specialize to the chosen point, or alternatively to assume quasi-finiteness at every generic
> point or on a dense set over a locally Noetherian target.

```lean
theorem quasiFiniteAt_of_target_stalk_dimension_le_one
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] (y : Y)
    (hyNoetherian : IsNoetherianRing (Y.presheaf.stalk y))
    (hyDimension : ringKrullDim (Y.presheaf.stalk y) ≤ 1)
    (hgeneric :
      (∀ η : X, η ∈ genericPoints X →
        letI := (f.residueFieldMap η).hom.toAlgebra
        Algebra.IsAlgebraic (Y.residueField (f η)) (X.residueField η)) ∨
      (∀ η : X, η ∈ genericPoints X → Specializes (f η) y →
        letI := (f.residueFieldMap η).hom.toAlgebra
        Algebra.IsAlgebraic (Y.residueField (f η)) (X.residueField η)) ∨
      (∀ η : X, η ∈ genericPoints X → quasiFiniteAt f η) ∨
      (IsLocallyNoetherian Y ∧ Dense {x : X | quasiFiniteAt f x})) :
    ∀ x : X, f x = y → quasiFiniteAt f x
```

## Tag 0AB7, a lemma

[Tag 0AB7](https://stacks.math.columbia.edu/tag/0AB7) in the Stacks Project.

**`AlgebraicGeometry.exists_isFinite_morphismRestrict_of_ringKrullDim_stalk_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiFiniteCodimensionOne.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiFiniteCodimensionOne.lean#L190).

> **Stacks Project, Tag 0AB7.** A proper morphism which is generically quasi-finite is finite
> over a neighbourhood of a point whose local ring is Noetherian of dimension at most one.

```lean
theorem exists_isFinite_morphismRestrict_of_ringKrullDim_stalk_le_one
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] (y : Y)
    [IsNoetherianRing (Y.presheaf.stalk y)] (hy : ringKrullDim (Y.presheaf.stalk y) ≤ 1)
    (h : (∀ (η : X), η ∈ genericPoints X → letI := (f.residueFieldMap η).hom.toAlgebra
        Algebra.IsAlgebraic (Y.residueField (f η)) (X.residueField η)) ∨
      ((∀ (η : X), η ∈ genericPoints X → Specializes (f η) y →
          letI := (f.residueFieldMap η).hom.toAlgebra
          Algebra.IsAlgebraic (Y.residueField (f η)) (X.residueField η)) ∨
        ((∀ (η : X), η ∈ genericPoints X → quasiFiniteAt f η) ∨
          (IsLocallyNoetherian Y ∧ Dense {x : X | quasiFiniteAt f x})))) :
    ∃ V : Y.Opens, y ∈ V ∧ IsFinite (f ∣_ V)
```

## Tag 0BFP, a lemma

[Tag 0BFP](https://stacks.math.columbia.edu/tag/0BFP) in the Stacks Project.

**`AlgebraicGeometry.exists_isIso_restrict_of_finite_fiber_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocus.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocus.lean#L369). The attribute's comment: “finite_fibre_normal”. References: EGA III (4.4.9), “proper case”.

> **Stacks Project, Tag 0BFP (finite fibre, normal local ring).**
> Let `f : Y ⟶ X` be a proper birational morphism, where `X` is Noetherian and `Y`
> is reduced. The morphism is an isomorphism over a neighbourhood of every point whose fibre
> is finite and whose local ring is a normal domain.

```lean
public theorem exists_isIso_restrict_of_finite_fiber_of_normal
    {X Y : Scheme.{u}} [IsNoetherian X] (f : Y ⟶ X) [IsProper f] [IsReduced Y]
    (hf : IsBirational f) (x : X) (hfinite : (f ⁻¹' {x}).Finite)
    [IsDomain (X.presheaf.stalk x)] [IsIntegrallyClosed (X.presheaf.stalk x)] :
    ∃ U : X.Opens, x ∈ U ∧ IsIso (f ∣_ U)
```

**`AlgebraicGeometry.mem_maximal_isomorphism_open_of_quasiFiniteAt_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocus.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocus.lean#L729). The attribute's comment: “quasi_finite_point_normal”. References: EGA III (4.4.9), “proper case”.

> **Stacks Project, Tag 0BFP (quasi-finite point over a normal point).** The maximal open
> over which a proper birational morphism with reduced source is an isomorphism contains every
> normal point admitting a preimage at which the morphism is quasi-finite.

```lean
public theorem mem_maximal_isomorphism_open_of_quasiFiniteAt_of_isNormal
    {X Y : Scheme.{u}} [IsNoetherian X] (f : Y ⟶ X) [IsProper f] [IsReduced Y]
    (hf : IsBirational f) (U : X.Opens)
    (hU : IsGreatest { V : X.Opens | IsIso (f ∣_ V) } U) (x : X)
    (hnormal : IsNormalRing (X.presheaf.stalk x)) (y : Y) (hy : f y = x)
    (hqf : quasiFiniteAt f y) :
    x ∈ U
```

**`AlgebraicGeometry.mem_maximal_isomorphism_open_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocusCodimensionZero.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocusCodimensionZero.lean#L127). The attribute's comment: “item (1): a point of codimension zero, a generic point of a component”.

> **Stacks Project, Tag 0BFP (codimension zero).**
> Let `f : Y ⟶ X` be a proper birational morphism, where `X` is Noetherian and `Y` is reduced. The
> maximal open over which `f` is an isomorphism contains every point of codimension zero on `X`,
> that is, every generic point of an irreducible component of `X`.

```lean
public theorem mem_maximal_isomorphism_open_of_mem_genericPoints
    {X Y : Scheme.{u}} [IsNoetherian X] (f : Y ⟶ X) [IsProper f] [IsReduced Y]
    (hf : IsBirational f) (U : X.Opens)
    (hU : IsGreatest { V : X.Opens | IsIso (f ∣_ V) } U) (x : X)
    (hx : x ∈ genericPoints X) :
    x ∈ U
```

**`AlgebraicGeometry.mem_maximal_isomorphism_open_of_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocusDVR.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Geometric/BirationalIsomorphismLocusDVR.lean#L101). The attribute's comment: “item (2): a codimension-one point whose local ring is a discrete valuation ring”.

> Let `f : Y ⟶ X` be a proper birational morphism, where `X` is Noetherian and `Y` is reduced.
> The maximal open over which `f` is an isomorphism contains every point whose local ring is a
> discrete valuation ring. Such a point has codimension one on `X`, the dimension of a discrete
> valuation ring being one.

```lean
public theorem mem_maximal_isomorphism_open_of_isDiscreteValuationRing
    {X Y : Scheme.{u}} [IsNoetherian X] (f : Y ⟶ X) [IsProper f] [IsReduced Y]
    (hf : IsBirational f) (U : X.Opens)
    (hU : IsGreatest { V : X.Opens | IsIso (f ∣_ V) } U) (x : X)
    [IsDomain (X.presheaf.stalk x)]
    [IsDiscreteValuationRing (X.presheaf.stalk x)] :
    x ∈ U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.17, Tag 0AB5](https://stacks.math.columbia.edu/tag/0AB5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
