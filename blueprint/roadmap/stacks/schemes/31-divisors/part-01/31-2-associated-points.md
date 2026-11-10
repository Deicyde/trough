---
declaration: section
origin: cited
lean: Stacks.Divisors.IsAssociatedPoint, Stacks.Divisors.associatedPoints, Stacks.Divisors.schemeAssociatedPoints, AlgebraicGeometry.isAssociatedPoint_of_isAssociatedPrime_sections, AlgebraicGeometry.isAssociatedPrime_sections_of_isAssociatedPoint_of_fg, AlgebraicGeometry.isAssociatedPrime_sections_iff_isAssociatedPoint_of_isLocallyNoetherian, AlgebraicGeometry.associatedPoints_subset_support, AlgebraicGeometry.associatedPoints_subset_of_mono
statement: formalized
proof: formalized
---

# 31.2 Associated points

Section 31.2 of the Stacks Project, [Tag 02OI](https://stacks.math.columbia.edu/tag/02OI). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02OJ, a definition

[Tag 02OJ](https://stacks.math.columbia.edu/tag/02OJ) in the Stacks Project.

**`Stacks.Divisors.IsAssociatedPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean#L57). The attribute's comment: “part (1)”.

> A point `x` is *associated* to an `𝒪_X`-module `F` when the maximal ideal of the local ring
> `𝒪_{X, x}` is an associated prime of the stalk `F_x`.

```lean
abbrev IsAssociatedPoint (F : X.Modules) (x : X) : Prop
```

**`Stacks.Divisors.associatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean#L64). The attribute's comment: “part (2)”.

> The set `Ass(F)` of points associated to an `𝒪_X`-module `F`.

```lean
abbrev associatedPoints (F : X.Modules) : Set X
```

**`Stacks.Divisors.schemeAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints.lean#L76). The attribute's comment: “part (3)”.

> The associated points `Ass(X)` of a scheme `X` are the associated points of its structure
> sheaf.

```lean
abbrev schemeAssociatedPoints (X : Scheme.{u}) : Set X
```

## Tag 02OK, a lemma

[Tag 02OK](https://stacks.math.columbia.edu/tag/02OK) in the Stacks Project.

**`AlgebraicGeometry.isAssociatedPoint_of_isAssociatedPrime_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean#L121). The attribute's comment: “part (1)”.

> **Stacks 02OK, part (1).** An associated prime of the sections of a quasi-coherent sheaf on
> an affine open gives an associated point of the sheaf.

```lean
theorem isAssociatedPoint_of_isAssociatedPrime_sections {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] (U : X.Opens) (hU : IsAffineOpen U) {x : X} (hx : x ∈ U)
    (h : IsAssociatedPrimeStacks Γ(X, U) Γ(F, U) (hU.primeIdealOf ⟨x, hx⟩).asIdeal) :
    Stacks.Divisors.IsAssociatedPoint F x
```

**`AlgebraicGeometry.isAssociatedPrime_sections_of_isAssociatedPoint_of_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean#L163). The attribute's comment: “part (2)”.

> **Stacks 02OK, part (2).** If the prime corresponding to an associated point is finitely
> generated, then it is associated to the module of sections on the affine open.

```lean
theorem isAssociatedPrime_sections_of_isAssociatedPoint_of_fg {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] (U : X.Opens) (hU : IsAffineOpen U) {x : X} (hx : x ∈ U)
    (hfg : (hU.primeIdealOf ⟨x, hx⟩).asIdeal.FG) (h : Stacks.Divisors.IsAssociatedPoint F x) :
    IsAssociatedPrimeStacks Γ(X, U) Γ(F, U) (hU.primeIdealOf ⟨x, hx⟩).asIdeal
```

**`AlgebraicGeometry.isAssociatedPrime_sections_iff_isAssociatedPoint_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/AffineComparison.lean#L184). The attribute's comment: “locally Noetherian case”. References: EGA IV (3.1.2), “more general”.

> **Stacks 02OK, locally Noetherian case.** On a locally Noetherian scheme, the prime
> corresponding to a point of an affine open is associated to the module of sections exactly when
> the point is associated to the sheaf.

```lean
theorem isAssociatedPrime_sections_iff_isAssociatedPoint_of_isLocallyNoetherian
    {X : Scheme.{u}} [IsLocallyNoetherian X] (F : X.Modules) [F.IsQuasicoherent] (U : X.Opens)
    (hU : IsAffineOpen U) {x : X} (hx : x ∈ U) :
    IsAssociatedPrimeStacks Γ(X, U) Γ(F, U) (hU.primeIdealOf ⟨x, hx⟩).asIdeal ↔
      Stacks.Divisors.IsAssociatedPoint F x
```

## Tag 05AD, a lemma

[Tag 05AD](https://stacks.math.columbia.edu/tag/05AD) in the Stacks Project.

**`AlgebraicGeometry.associatedPoints_subset_support`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean#L54).

> **Stacks Project, Tag 05AD.** Every associated point of a sheaf of modules lies in its
> support.

```lean
lemma associatedPoints_subset_support {X : Scheme.{u}} (F : X.Modules) :
    Stacks.Divisors.associatedPoints F ⊆ SheafOfModules.supp F
```

## Tag 05AE, a lemma

[Tag 05AE](https://stacks.math.columbia.edu/tag/05AE) in the Stacks Project.

**`AlgebraicGeometry.associatedPoints_subset_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean#L82). The attribute's comment: “associated\_points\_subsheaf\_subset”.

> **Stacks Project, Tag 05AE.** The associated points of a subsheaf are associated points of
> the ambient sheaf.

```lean
theorem associatedPoints_subset_of_mono {X : Scheme.{u}} {F₁ F₂ : X.Modules} (f : F₁ ⟶ F₂)
    [Mono f] :
    Stacks.Divisors.associatedPoints F₁ ⊆ Stacks.Divisors.associatedPoints F₂
```

**`AlgebraicGeometry.associatedPoints_subset_union_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Basic.lean#L135). The attribute's comment: “associated\_points\_middle\_subset\_union”.

> **Stacks Project, Tag 05AE.** The associated points of the middle term of a short exact
> sequence lie in the union of those of its outer terms.

```lean
theorem associatedPoints_subset_union_of_shortExact {X : Scheme.{u}}
    (S : ShortComplex X.Modules) (hS : S.ShortExact) :
    Stacks.Divisors.associatedPoints S.X₂ ⊆
      Stacks.Divisors.associatedPoints S.X₁ ∪ Stacks.Divisors.associatedPoints S.X₃
```

## Tag 05AF, a lemma

[Tag 05AF](https://stacks.math.columbia.edu/tag/05AF) in the Stacks Project.

**`AlgebraicGeometry.associatedPoints_inter_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Finite.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Finite.lean#L70).

> **Stacks Project, Tag 05AF.** A coherent module on a locally Noetherian scheme has only
> finitely many associated points in a quasi-compact open subset.

```lean
theorem associatedPoints_inter_finite {X : Scheme.{u}} [IsLocallyNoetherian X] (F : X.Modules)
    [F.IsCoherent] (U : X.Opens) (hU : IsCompact (U : Set X)) :
    (Stacks.Divisors.associatedPoints F ∩ (U : Set X)).Finite
```

## Tag 05AG, a lemma

[Tag 05AG](https://stacks.math.columbia.edu/tag/05AG) in the Stacks Project.

**`AlgebraicGeometry.isZero_iff_associatedPoints_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Vanishing.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Vanishing.lean#L95).

> A quasi-coherent module on a locally Noetherian scheme is zero if and only if its set of
> associated points is empty.

```lean
theorem isZero_iff_associatedPoints_eq_empty (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsQuasicoherent] :
    IsZero F ↔ Stacks.Divisors.associatedPoints F = ∅
```

## Tag 05AI, an example

[Tag 05AI](https://stacks.math.columbia.edu/tag/05AI) in the Stacks Project.

**`AlgebraicGeometry.maximalIdeal_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean#L94). The attribute's comment: “locally nilpotent maximal ideal”.

> **Stacks 05AI.** The maximal ideal of the square-zero-variable quotient is locally
> nilpotent.

```lean
theorem maximalIdeal_locallyNilpotent (k : Type u) [Field k] :
    (IsLocalRing.maximalIdeal (S k)).LocallyNilpotent
```

**`AlgebraicGeometry.no_maximalIdeal_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean#L101). The attribute's comment: “no maximal-ideal annihilator”.

> **Stacks 05AI.** No element of the quotient has its maximal ideal as annihilator.

```lean
theorem no_maximalIdeal_annihilator (k : Type u) [Field k] (s : S k) :
    annElem s ≠ IsLocalRing.maximalIdeal (S k)
```

**`AlgebraicGeometry.spectrum_associatedPoints_eq_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean#L113). The attribute's comment: “no associated points”.

> **Stacks 05AI.** The spectrum of the square-zero-variable quotient has no associated
> points.

```lean
theorem spectrum_associatedPoints_eq_empty (k : Type u) [Field k] :
    Stacks.Divisors.schemeAssociatedPoints (Spec (.of (S k))) = ∅
```

**`Stacks.SquareZero.isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SquareZeroQuotient.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/SquareZeroQuotient.lean#L96). The attribute's comment: “local ring”.

> **Stacks 05AI.** The quotient by the squares of countably many variables is local.

```lean
theorem isLocalRing (k : Type u) [Field k] : IsLocalRing (S k)
```

Declarations registered for the tag:

- [`assExact_S_eq_empty`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean#L518), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Counterexample.lean#L108) (StacksFrontier): “no associated primes”.

## Tag 0B3L, a lemma

[Tag 0B3L](https://stacks.math.columbia.edu/tag/0B3L) in the Stacks Project.

**`AlgebraicGeometry.restriction_injective_of_associatedPoints_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Restriction.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Restriction.lean#L202).

> **Stacks Project, Tag 0B3L.** Restriction of sections of a quasi-coherent sheaf on a locally
> Noetherian scheme to an open subset containing all associated points is injective.

```lean
theorem restriction_injective_of_associatedPoints_subset (X : Scheme.{u})
    [IsLocallyNoetherian X] (F : X.Modules) [F.IsQuasicoherent] (U : X.Opens)
    (hU : Stacks.Divisors.associatedPoints F ⊆ (U : Set X)) :
    Function.Injective (F.presheaf.map (homOfLE (show U ≤ (⊤ : X.Opens) from le_top)).op)
```

## Tag 05AH, a lemma

[Tag 05AH](https://stacks.math.columbia.edu/tag/05AH) in the Stacks Project.

**`AlgebraicGeometry.mem_associatedPoints_of_mem_supp_of_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean#L133). The attribute's comment: “minimal point of the support”.

> **Stacks Project, Tag 05AH.** A point of the support of a quasi-coherent module on a locally
> Noetherian scheme which is not a specialization of another point of the support is associated to
> the module.

```lean
theorem mem_associatedPoints_of_mem_supp_of_specialization (X : Scheme.{u})
    [IsLocallyNoetherian X] (F : X.Modules) [F.IsQuasicoherent] (x : X)
    (hx : x ∈ SheafOfModules.supp F)
    (hmin : ∀ y : X, y ∈ SheafOfModules.supp F → y ⤳ x → y = x) :
    x ∈ Stacks.Divisors.associatedPoints F
```

**`AlgebraicGeometry.mem_schemeAssociatedPoints_of_isGenericPoint_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/MinimalSupport.lean#L155). The attribute's comment: “generic points of irreducible components”.

> **Stacks Project, Tag 05AH.** Every generic point of an irreducible component of a locally
> Noetherian scheme is an associated point of the scheme.

```lean
theorem mem_schemeAssociatedPoints_of_isGenericPoint_irreducibleComponent (X : Scheme.{u})
    [IsLocallyNoetherian X] {Z : Set X} (hZ : Z ∈ irreducibleComponents X) {x : X}
    (hx : IsGenericPoint x Z) :
    x ∈ Stacks.Divisors.schemeAssociatedPoints X
```

## Tag 0AVL, a lemma

[Tag 0AVL](https://stacks.math.columbia.edu/tag/0AVL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AssociatedPointsMono.mono_of_stalk_injective_on_associatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AssociatedPointsMono/Basic.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AssociatedPointsMono/Basic.lean#L267).

> **Stacks Project, Tag 0AVL.** A morphism of quasi-coherent modules on a locally
> Noetherian scheme is a monomorphism if it is injective on the stalk at every associated
> point of its source.

```lean
theorem mono_of_stalk_injective_on_associatedPoints
    {X : Scheme.{u}} [IsLocallyNoetherian X] {F G : X.Modules}
    [F.IsQuasicoherent] [G.IsQuasicoherent] (f : F ⟶ G)
    (hf : ∀ x : X,
      Function.Injective
        ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
          ((PresheafOfModules.toPresheaf X.ringCatSheaf.obj).map f.val)).hom ∨
        x ∉ associatedPoints F) :
    Mono f
```

## Tag 0AVM, a lemma

[Tag 0AVM](https://stacks.math.columbia.edu/tag/0AVM) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_stalk_isIso_or_depth_two_and_not_associated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Depth.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Depth.lean#L384).

> **Stacks Project, Tag 0AVM.** A map from a coherent sheaf to a quasi-coherent sheaf is an
> isomorphism if, at every point, it is an isomorphism on stalks, or the source stalk has depth at
> least two and the point is not associated to the target.
>
> The clause on associated points is what settles the degenerate case, and it cannot be dropped:
> Tag 00LI sets `depth_I(M) = ∞` when `IM = M`, hence `⊤` for `M = 0`
> (`Module.depth_eq_top_of_subsingleton`), so for `F = 0` and `G` nonzero the alternative
> `depth(F_x) ≥ 2` holds at every point on its own while `0 ⟶ G` is not an isomorphism. See
> `AlgebraicGeometry.isIso_of_stalk_isIso_or_depth_two_and_not_associated_of_isTorsionFree`, which
> is the integral, torsion-free case of Tag 0AVS, and the counterexample recorded alongside it.

```lean
theorem isIso_of_stalk_isIso_or_depth_two_and_not_associated {X : Scheme.{u}}
    [IsLocallyNoetherian X] {F G : X.Modules} [F.IsQuasicoherent] [G.IsQuasicoherent]
    [F.IsCoherent] (f : F ⟶ G)
    (hf : ∀ x : X,
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) F.val x
      IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf X.ringCatSheaf.obj).map f.val)) ∨
      ((2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) ∧
        x ∉ Stacks.Divisors.associatedPoints G)) :
    IsIso f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.2, Tag 02OI](https://stacks.math.columbia.edu/tag/02OI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
