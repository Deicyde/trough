---
declaration: section
origin: cited
lean: Stacks.Divisors.relativeAssassin, AlgebraicGeometry.mem_relativeAssassin_of_mem_relativeAssassin_sections, AlgebraicGeometry.mem_relativeAssassin_sections_iff_of_locallyNoetherian_fibers, AlgebraicGeometry.mem_relativeAssassin_pullback_iff, AlgebraicGeometry.relativeAssassin_pullback_subset_preimage, AlgebraicGeometry.preimage_relativeAssassin_eq_pullback_of_locallyQuasiFinite, AlgebraicGeometry.preimage_relativeAssassin_eq_pullback_of_isAlgebraic_residueField
statement: formalized
proof: formalized
---

# 31.7 Relative assassin

Section 31.7 of the Stacks Project, [Tag 05AS](https://stacks.math.columbia.edu/tag/05AS). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05AT, a definition

[Tag 05AT](https://stacks.math.columbia.edu/tag/05AT) in the Stacks Project.

**`Stacks.Divisors.relativeAssassin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociated.lean#L176).

> **Stacks Project, Tag 05AT.** The *relative assassin* `Ass_{X/S}(F)` of an `𝒪_X`-module
> along `f : X ⟶ S` is the union over the points of `S` of the images in `X` of the associated
> points of the restriction of `F` to the scheme-theoretic fibre.

```lean
noncomputable def relativeAssassin (f : X ⟶ S) (F : X.Modules) : Set X
```

## Tag 0CU5, a lemma

[Tag 0CU5](https://stacks.math.columbia.edu/tag/0CU5) in the Stacks Project.

**`AlgebraicGeometry.mem_relativeAssassin_of_mem_relativeAssassin_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/AffineOpen.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/AffineOpen.lean#L568). The attribute's comment: “forward implication”.

> **Stacks Project, Tag 0CU5.** A relative associated prime of the sections on an affine open
> gives a relative associated point of the sheaf.

```lean
public theorem mem_relativeAssassin_of_mem_relativeAssassin_sections
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) [F.IsQuasicoherent]
    (U : X.Opens) (V : S.Opens) (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (hUV : U ≤ f ⁻¹ᵁ V) {x : X} (hx : x ∈ U) :
    letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
    letI : Module Γ(S, V) Γ(F, U) :=
      Module.compHom Γ(F, U) (f.appLE V U hUV).hom
    letI : IsScalarTower Γ(S, V) Γ(X, U) Γ(F, U) :=
      IsScalarTower.of_compHom Γ(S, V) Γ(X, U) Γ(F, U)
    (hU.primeIdealOf ⟨x, hx⟩) ∈
      Module.relativeAssassin Γ(S, V) Γ(X, U) Γ(F, U) →
      x ∈ Stacks.Divisors.relativeAssassin f F
```

**`AlgebraicGeometry.mem_relativeAssassin_sections_iff_of_locallyNoetherian_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/AffineOpen.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/AffineOpen.lean#L605). The attribute's comment: “locally Noetherian equivalence”.

> **Stacks Project, Tag 0CU5.** With locally Noetherian fibres, the relative associated
> primes of affine sections are exactly the relative associated points of the sheaf.

```lean
public theorem mem_relativeAssassin_sections_iff_of_locallyNoetherian_fibers
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) [F.IsQuasicoherent]
    (U : X.Opens) (V : S.Opens) (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (hUV : U ≤ f ⁻¹ᵁ V) (hf : ∀ s : S, IsLocallyNoetherian (f.fiber s))
    {x : X} (hx : x ∈ U) :
    letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
    letI : Module Γ(S, V) Γ(F, U) :=
      Module.compHom Γ(F, U) (f.appLE V U hUV).hom
    letI : IsScalarTower Γ(S, V) Γ(X, U) Γ(F, U) :=
      IsScalarTower.of_compHom Γ(S, V) Γ(X, U) Γ(F, U)
    (hU.primeIdealOf ⟨x, hx⟩) ∈
      Module.relativeAssassin Γ(S, V) Γ(X, U) Γ(F, U) ↔
      x ∈ Stacks.Divisors.relativeAssassin f F
```

## Tag 05DC, a lemma

[Tag 05DC](https://stacks.math.columbia.edu/tag/05DC) in the Stacks Project.

**`AlgebraicGeometry.mem_relativeAssassin_pullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismAssociatedPoints/BaseChange.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismAssociatedPoints/BaseChange.lean#L552).

> **Stacks Project, Tag 05DC.** Under arbitrary base change, a point is in
> the relative assassin of the pulled-back quasi-coherent module exactly when
> its image is in the original relative assassin and its residue-field tensor
> product point is generic in an irreducible component.

```lean
theorem mem_relativeAssassin_pullback_iff
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (F : X.Modules)
    [F.IsQuasicoherent] [LocallyOfFiniteType f]
    (x' : pullback (C := Scheme.{u}) f g) :
    x' ∈ Stacks.Divisors.relativeAssassin (pullback.snd (C := Scheme.{u}) f g)
        ((Scheme.Modules.pullback (pullback.fst (C := Scheme.{u}) f g)).obj F) ↔
      (pullback.fst (C := Scheme.{u}) f g x' ∈ Stacks.Divisors.relativeAssassin f F ∧
        ∃ Z ∈ irreducibleComponents
            (Spec (Scheme.Pullback.Triplet.ofPoint x').tensor),
          IsGenericPoint (Scheme.Pullback.SpecOfPoint x') Z)
```

## Tag 05KL, a remark

[Tag 05KL](https://stacks.math.columbia.edu/tag/05KL) in the Stacks Project.

**`AlgebraicGeometry.relativeAssassin_pullback_subset_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean#L194). The attribute's comment: “unconditional containment”.

> **Stacks Project, Tag 05KL.** After arbitrary base change, the relative assassin of the
> pulled-back module is contained in the inverse image of the original relative assassin.

```lean
public theorem relativeAssassin_pullback_subset_preimage
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (F : X.Modules)
    [F.IsQuasicoherent] [LocallyOfFiniteType f] :
    Stacks.Divisors.relativeAssassin (pullback.snd (C := Scheme.{u}) f g)
        ((Scheme.Modules.pullback (pullback.fst (C := Scheme.{u}) f g)).obj F) ⊆
      (pullback.fst (C := Scheme.{u}) f g) ⁻¹'
        Stacks.Divisors.relativeAssassin f F
```

**`AlgebraicGeometry.preimage_relativeAssassin_eq_pullback_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean#L206). The attribute's comment: “equality for locally quasi-finite base change”.

> **Stacks Project, Tag 05KL.** A locally quasi-finite base change pulls the relative
> assassin back exactly.

```lean
public theorem preimage_relativeAssassin_eq_pullback_of_locallyQuasiFinite
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (F : X.Modules)
    [F.IsQuasicoherent] [LocallyOfFiniteType f]
    [LocallyOfFiniteType g] [LocallyQuasiFinite g] :
    (pullback.fst (C := Scheme.{u}) f g) ⁻¹' Stacks.Divisors.relativeAssassin f F =
      Stacks.Divisors.relativeAssassin (pullback.snd (C := Scheme.{u}) f g)
        ((Scheme.Modules.pullback (pullback.fst (C := Scheme.{u}) f g)).obj F)
```

**`AlgebraicGeometry.preimage_relativeAssassin_eq_pullback_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassinTwo/BaseChange.lean#L225). The attribute's comment: “equality for algebraic residue-field extensions”.

> **Stacks Project, Tag 05KL.** If every residue-field extension induced by the base-change
> morphism is algebraic, then it pulls the relative assassin back exactly.

```lean
public theorem preimage_relativeAssassin_eq_pullback_of_isAlgebraic_residueField
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (F : X.Modules)
    [F.IsQuasicoherent] [LocallyOfFiniteType f]
    (hg : ∀ s' : S',
      letI := (g.residueFieldMap s').hom.toAlgebra
      Algebra.IsAlgebraic (S.residueField (g s')) (S'.residueField s')) :
    (pullback.fst (C := Scheme.{u}) f g) ⁻¹' Stacks.Divisors.relativeAssassin f F =
      Stacks.Divisors.relativeAssassin (pullback.snd (C := Scheme.{u}) f g)
        ((Scheme.Modules.pullback (pullback.fst (C := Scheme.{u}) f g)).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.7, Tag 05AS](https://stacks.math.columbia.edu/tag/05AS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
