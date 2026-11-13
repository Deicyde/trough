---
declaration: section
origin: cited
lean: CochainComplex.IsProjectiveResolution, Stacks.ProjectiveResolution.CohomologyVanishing.cohomology_vanishes_of_isProjectiveResolution, Stacks.ProjectiveResolution.CohomologyVanishing.exists_boundedAbove_quasiIso_of_cohomologyVanishes, ProjectiveResolutionLemma.statement3, ProjectiveResolutionLemma.statement2, ProjectiveResolutionLemma.statement1, projective_into_acyclic_is_zero, bijective_postcomp_quotient_map
statement: formalized
proof: formalized
---

# 13.19 Projective resolutions

Section 13.19 of the Stacks Project, [Tag 0643](https://stacks.math.columbia.edu/tag/0643). 11 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0644, a definition

[Tag 0644](https://stacks.math.columbia.edu/tag/0644) in the Stacks Project.

**`CochainComplex.IsProjectiveResolution`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/Defs/ProjectiveResolution.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/Defs/ProjectiveResolution.lean#L112). The attribute's comment: “The case of a complex; for an object it is `ProjectiveResolution`.”. References: SGA 4½ Etat 0 (3.1.8), “projective case”.

> A morphism of cochain complexes `α : P ⟶ K` in an abelian category is a
> *projective resolution* of `K` if `P` is bounded above, all the terms of `P` are
> projective objects, and `α` is a quasi-isomorphism.

```lean
public class IsProjectiveResolution {P K : CochainComplex C ℤ} (α : P ⟶ K) : Prop
    extends QuasiIso α
```

## Tag 0645, a lemma

[Tag 0645](https://stacks.math.columbia.edu/tag/0645) in the Stacks Project.

**`Stacks.ProjectiveResolution.CohomologyVanishing.cohomology_vanishes_of_isProjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean#L125). The attribute's comment: “(1)”.

> **Stacks Tag 0645, Lemma 13.19.2, part (1).**  If `K^•` has a projective
> resolution, then `H^n(K^•) = 0` for `n ≫ 0`.

```lean
theorem cohomology_vanishes_of_isProjectiveResolution
    (K : CochainComplex A ℤ) (h : IsProjectiveResolution K) :
    CohomologyVanishesForLargeN K
```

**`Stacks.ProjectiveResolution.CohomologyVanishing.exists_boundedAbove_quasiIso_of_cohomologyVanishes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean#L147). The attribute's comment: “(2)”.

> **Stacks Tag 0645, Lemma 13.19.2, part (2).**  If `H^n(K^•) = 0` for
> `n ≫ 0`, then there exists a quasi-isomorphism `L^• → K^•` with `L^•` bounded
> above.

```lean
theorem exists_boundedAbove_quasiIso_of_cohomologyVanishes
    (K : CochainComplex A ℤ) (h : CohomologyVanishesForLargeN K) :
    ∃ (L : CochainComplex A ℤ) (f : L ⟶ K), IsBoundedAboveComplex L ∧ QuasiIso f
```

## Tag 0646, a lemma

[Tag 0646](https://stacks.math.columbia.edu/tag/0646) in the Stacks Project.

**`ProjectiveResolutionLemma.statement3`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/BoundedAbove.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/BoundedAbove.lean#L280). The attribute's comment: “(3)”. References: SGA 4½ Etat 0 (3.1.9), “Part 1, special case”; SGA 4½ Etat 0 (3.2.3), “partial”; SGA 4½ Etat 0 (4.2.3.1), “Corollary 1”.

> **Statement 3.**
> Assume `A` has enough projectives. Let `K^•` be a complex with `K^n = 0` for
> `n > a`. Then there exists a projective resolution `α : P^• → K^•` (Definition 4)
> bounded above by `a` such that, additionally, each component `α^n : P^n → K^n` is
> an epimorphism.

```lean
alias statement3
```

**`ProjectiveResolutionLemma.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/BoundedAbove.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/BoundedAbove.lean#L342). The attribute's comment: “(2)”. References: SGA 4½ Etat 0 (3.2.3), “partial”; SGA 4½ Etat 0 (4.2.3.1), “Corollary 1”.

> **Statement 2.**
> Assume `A` has enough projectives. Let `K^•` be a complex with `H^n(K^•) = 0`
> for all `n ≫ 0`. Then `K^•` has a projective resolution in the sense of
> Definition 4, i.e. there exists an upper bound `N` and a projective resolution
> of `K^•` bounded above by `N`.

```lean
theorem statement2 [EnoughProjectives C] (K : CochainComplex C ℤ)
    (hK : ∃ M : ℤ, ∀ n : ℤ, M ≤ n → IsZero (K.homology n)) :
    ∃ N : ℤ, Nonempty (ProjectiveResolutionComplex K N)
```

**`ProjectiveResolutionLemma.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/EpiResData.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/EpiResData.lean#L140). The attribute's comment: “(1)”. References: SGA 2 VIII (1.4), “special case”; SGA 4½ Etat 0 (3.1.9), “Part 1, special case”; SGA 4½ Etat 0 (3.2.3), “partial”.

> **Statement 1.**
> If `A` has enough projectives, then every object `A` of `A` has a projective
> resolution in the sense of Definition 3: there is a complex `P^•` of projectives
> with `P^n = 0` for `n > 0` and a quasi-isomorphism `P^• → A[0]`. Viewing the
> resolution as a projective resolution (Definition 4) of the complex `A[0]` with
> upper bound `0` captures exactly conditions (1)–(4) of Definition 3.

```lean
theorem statement1 [EnoughProjectives C] (A : C) :
    Nonempty (ProjectiveResolutionComplex (single₀ A) 0)
```

## Tag 0647, a lemma

[Tag 0647](https://stacks.math.columbia.edu/tag/0647) in the Stacks Project.

**`projective_into_acyclic_is_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean#L309). References: SGA 6 I (4.1), “special case”; SGA 6 II (1.1), “c)”; SGA 6 II (1.2), “1.2 d), special case”.

> Let `K` be an acyclic complex and `P` a bounded above complex of projective objects. Then
> every morphism of complexes `f : P ⟶ K` is homotopic to zero.

```lean
theorem projective_into_acyclic_is_zero
    {C : Type*} [CategoryTheory.Category C] [CategoryTheory.Abelian C]
    (P K : CochainComplex C ℤ)
    (n : ℤ) (hP : P.IsStrictlyLE n)
    (hProj : ∀ i : ℤ, CategoryTheory.Projective (P.X i))
    (hK : HomologicalComplex.Acyclic K)
    (f : P ⟶ K) : Nonempty (Homotopy f 0)
```

## Tag 0648, a remark

[Tag 0648](https://stacks.math.columbia.edu/tag/0648) in the Stacks Project.

**`bijective_postcomp_quotient_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L247).

> **Remark [Stacks 0648]** for a K-projective complex, the dual of [Stacks 05TF]. If `P` is a
> K-projective cochain complex and `α : L ⟶ K` is a quasi-isomorphism, then postcomposition with
> the image of `α` in the homotopy category is a bijection
> `Hom_{K(A)}(P, L) → Hom_{K(A)}(P, K)`.
>
> Its surjectivity is the first assertion of [Stacks 0649] and its injectivity is
> [Stacks 064A].

```lean
lemma bijective_postcomp_quotient_map {A : Type u} [Category.{v} A] [Abelian A]
    {P K L : CochainComplex A ℤ} [P.IsKProjective] (α : L ⟶ K) [QuasiIso α] :
    Function.Bijective (fun β : (HomotopyCategory.quotient A (.up ℤ)).obj P ⟶
        (HomotopyCategory.quotient A (.up ℤ)).obj L ↦
      β ≫ (HomotopyCategory.quotient A (.up ℤ)).map α)
```

## Tag 0649, a lemma

[Tag 0649](https://stacks.math.columbia.edu/tag/0649) in the Stacks Project.

**`CochainComplex.IsKProjective.exists_lift_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L274).

> **Stacks 0649.** Let `A` be an abelian category, let `α : L ⟶ K` be a quasi-isomorphism of
> cochain complexes in `A` and let `P` be a K-projective cochain complex — for instance one which
> is bounded above and consists of projective objects, by
> `CochainComplex.isKProjective_of_projective`. Then, given `γ : P ⟶ K`:
> (1) there is a `β : P ⟶ L` with `β ≫ α` homotopic to `γ`, and
> (2) if the terms of `P` are projective and `α` is epimorphic in every degree, there is a
> `β : P ⟶ L` with `β ≫ α = γ`.

```lean
public theorem CochainComplex.IsKProjective.exists_lift_of_quasiIso {A : Type u} [Category.{v} A]
    [Abelian A] {P K L : CochainComplex A ℤ} [P.IsKProjective] (α : L ⟶ K) [QuasiIso α]
    (γ : P ⟶ K) :
    (∃ β : P ⟶ L, Nonempty (Homotopy (β ≫ α) γ)) ∧
      ((∀ n : ℤ, Projective (P.X n)) → (∀ n : ℤ, Epi (α.f n)) → ∃ β : P ⟶ L, β ≫ α = γ)
```

## Tag 064A, a lemma

[Tag 064A](https://stacks.math.columbia.edu/tag/064A) in the Stacks Project.

**`CochainComplex.IsKProjective.nonempty_homotopy_of_comp_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L290).

> **Stacks 064A.** Let `A` be an abelian category, let `α : L ⟶ K` be a quasi-isomorphism of
> cochain complexes in `A` and let `P` be a K-projective cochain complex — for instance one which
> is bounded above and consists of projective objects, by
> `CochainComplex.isKProjective_of_projective`. Then two morphisms `β₁, β₂ : P ⟶ L` whose
> composites with `α` are homotopic are themselves homotopic; in particular a lift of a given
> `γ : P ⟶ K` through `α` up to homotopy is unique up to homotopy.

```lean
public theorem CochainComplex.IsKProjective.nonempty_homotopy_of_comp_quasiIso {A : Type u}
    [Category.{v} A] [Abelian A] {P K L : CochainComplex A ℤ} [P.IsKProjective] (α : L ⟶ K)
    [QuasiIso α] {β₁ β₂ : P ⟶ L} (h : Homotopy (β₁ ≫ α) (β₂ ≫ α)) :
    Nonempty (Homotopy β₁ β₂)
```

## Tag 064B, a lemma

[Tag 064B](https://stacks.math.columbia.edu/tag/064B) in the Stacks Project.

**`CochainComplex.isKProjective_iff_Qh_map_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L324).

> **Stacks 064B.** Let `A` be an abelian category and let `P` be a cochain complex in `A`. Then
> `P` is K-projective — which a bounded above complex of projective objects is, by
> `CochainComplex.isKProjective_of_projective` — if and only if for every object `L` of the homotopy
> category `K(A)` the localization functor `Qh : K(A) ⥤ D(A)` induces a bijection
> `Mor_{K(A)}(P, L) → Mor_{D(A)}(P, L)`. The Stacks lemma is the forward implication.

```lean
public theorem CochainComplex.isKProjective_iff_Qh_map_bijective {A : Type u} [Category.{v} A]
    [Abelian A] [HasDerivedCategory.{w} A] (P : CochainComplex A ℤ) :
    P.IsKProjective ↔ ∀ L : HomotopyCategory A (ComplexShape.up ℤ),
      Function.Bijective (DerivedCategory.Qh.map :
        ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj P ⟶ L) → _)
```

## Tag 064C, a lemma

[Tag 064C](https://stacks.math.columbia.edu/tag/064C) in the Stacks Project.

**`CochainComplex.exists_shortExact_isProjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L682).

> Let `C` be an abelian category with enough projectives, let
> `S : 0 ⟶ S.X₁ ⟶ S.X₂ ⟶ S.X₃ ⟶ 0` be a short exact sequence of cochain complexes
> of `C` with `S.X₁` bounded above, and let `π : P ⟶ S.X₃` be a projective
> resolution. Then there is a short exact sequence of complexes
> `0 ⟶ P₁ ⟶ P₂ ⟶ P ⟶ 0` mapping to `S`, with `π` as its third component, whose
> first two components `π₁ : P₁ ⟶ S.X₁` and `π₂ : P₂ ⟶ S.X₂` are projective
> resolutions as well.

```lean
public theorem exists_shortExact_isProjectiveResolution
    [EnoughProjectives C] (S : ShortComplex (CochainComplex C ℤ)) (hS : S.ShortExact)
    (n : ℤ) [S.X₁.IsStrictlyLE n] {P : CochainComplex C ℤ} (π : P ⟶ S.X₃)
    [IsProjectiveResolution π] :
    ∃ (P₁ P₂ : CochainComplex C ℤ) (i : P₁ ⟶ P₂) (p : P₂ ⟶ P) (hip : i ≫ p = 0)
      (π₁ : P₁ ⟶ S.X₁) (π₂ : P₂ ⟶ S.X₂),
      (ShortComplex.mk i p hip).ShortExact ∧ IsProjectiveResolution π₁ ∧
        IsProjectiveResolution π₂ ∧ i ≫ π₂ = π₁ ≫ S.f ∧ p ≫ π = π₂ ≫ S.g
```

## Tag 064D, a lemma

[Tag 064D](https://stacks.math.columbia.edu/tag/064D) in the Stacks Project.

**`CochainComplex.IsKProjective.hom_eq_zero_of_isStrictlyGE_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/KProjective.lean#L423).

> **Stacks 064D.** Let `A` be an abelian category, let `P` be a K-projective cochain complex of
> `A` with `P^i = 0` for `i < n` — for instance a bounded complex of projective objects with that
> property, by `CochainComplex.isKProjective_of_projective` — and let `K` be a cochain complex with
> `H^i(K) = 0` for `i > m`, where `m < n`. Then `Mor_{K(A)}(P, K) = Mor_{D(A)}(P, K) = 0`: every
> morphism from `P` to `K` in the homotopy category, and every morphism from `P` to `K` in the
> derived category, is zero.

```lean
public theorem CochainComplex.IsKProjective.hom_eq_zero_of_isStrictlyGE_of_isLE {A : Type u}
    [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A] (P K : CochainComplex A ℤ)
    [P.IsKProjective] (n : ℤ) [P.IsStrictlyGE n] (m : ℤ) (hmn : m < n) [K.IsLE m] :
    (∀ f : (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj P ⟶
      (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K, f = 0) ∧
      (∀ f : DerivedCategory.Q.obj P ⟶ DerivedCategory.Q.obj K, f = 0)
```

## Tag 064E, a lemma

[Tag 064E](https://stacks.math.columbia.edu/tag/064E) in the Stacks Project.

**`exists_lift_homotopy_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/Resolution/ProjectiveResolution/HomotopyLift.lean#L592). References: SGA 6 II (1.1), “c), special case”.

> Stacks Tag 064E. Let `β : P^• → L^•` and `α : E^• → L^•` be maps of cochain
> complexes in an abelian category `A`, and `n : ℤ`. Assume `P^•` is a bounded
> complex of projectives with `P^i = 0` for `i < n`, and that `H^i(α)` is an
> isomorphism for `i > n` and an epimorphism for `i = n`. Then there is a chain map
> `γ : P^• → E^•` with `α ∘ γ` homotopic to `β`.

```lean
theorem exists_lift_homotopy_of_projective (P E L : CochainComplex A ℤ)
    (β : P ⟶ L) (α : E ⟶ L) (n : ℤ)
    (hProj : ∀ i, Projective (P.X i))
    (hBddAbove : ∃ b : ℤ, ∀ i, b < i → IsZero (P.X i))
    (hBelow : ∀ i, i < n → IsZero (P.X i))
    (hIso : ∀ i, n < i → IsIso (HomologicalComplex.homologyMap α i))
    (hEpi : Epi (HomologicalComplex.homologyMap α n)) :
    ∃ γ : P ⟶ E, Nonempty (Homotopy (γ ≫ α) β)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.19, Tag 0643](https://stacks.math.columbia.edu/tag/0643)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
