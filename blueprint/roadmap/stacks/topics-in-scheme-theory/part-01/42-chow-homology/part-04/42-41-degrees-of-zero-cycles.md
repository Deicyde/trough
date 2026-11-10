---
declaration: section
origin: cited
lean: Stacks.Chow.chowDegree, Stacks.Chow.chowGroupBaseEquivInt, Stacks.Chow.cycleDegree_eq_sum_finrank, AlgebraicGeometry.curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental, AlgebraicGeometry.intersectionNumber_eq_chowDegree_iteratedFirstChernCap_and_ample
statement: formalized
proof: formalized
---

# 42.41 Degrees of zero cycles

Section 42.41 of the Stacks Project, [Tag 0AZ0](https://stacks.math.columbia.edu/tag/0AZ0). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AZ1, a definition

[Tag 0AZ1](https://stacks.math.columbia.edu/tag/0AZ1) in the Stacks Project.

**`Stacks.Chow.chowDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DegreeHomomorphism.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DegreeHomomorphism.lean#L67). The attribute's comment: “the degree homomorphism”.

> **Stacks Project, Tag 0AZ1.** The degree homomorphism `A_0(X) ⟶ ℤ` on the zeroth Chow group
> of a scheme `X` proper over a one-point base with vanishing dimension function — the spectrum of a
> field.
>
> This is the definition of Stacks 0AZ1 verbatim: proper pushforward `p_* : A_0(X) ⟶ A_0(S)` of
> Stacks 0GU8, which exists by Stacks 02S2
> (`Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper`), composed with the
> identification `A_0(S) = ℤ` of `Stacks.Chow.chowGroupBaseEquivInt`, which sends the fundamental
> cycle of the base to one.

```lean
def chowDegree (s : C.S) : chowGroup C p 0 →+ ℤ
```

**`Stacks.Chow.chowGroupBaseEquivInt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/ZeroCycleDegree.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/ZeroCycleDegree.lean#L213). The attribute's comment: “the identification of the Chow group of the base with the integers”.

> For a one-point base with vanishing dimension function — the spectrum of a field — the
> degree of a zero cycle is an isomorphism `A_0(S) ≅ ℤ`, sending the fundamental cycle to `1`.

```lean
def chowGroupBaseEquivInt (s : C.S) : chowGroup C (𝟙 C.S) 0 ≃+ ℤ
```

## Tag 0AZ2, a lemma

[Tag 0AZ2](https://stacks.math.columbia.edu/tag/0AZ2) in the Stacks Project.

**`Stacks.Chow.cycleDegree_eq_sum_finrank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/ZeroCycleDegreeFormula.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/ZeroCycleDegreeFormula.lean#L170).

> The degree `Stacks.Chow.cycleDegree` of a zero cycle on a scheme proper over a field,
> presented as a finite sum `α = ∑ n_i [Z_i]` over integral closed subschemes of delta-dimension
> zero, is `∑ n_i dim_k Γ(Z_i, 𝒪_{Z_i})`, where `dim_k Γ(Z_i, 𝒪_{Z_i})` is the degree of
> `Z_i → Spec(k)`.

```lean
theorem cycleDegree_eq_sum_finrank [IsProper p] (s : (fieldChowSituation k).S)
    (α : CycleGroup (fieldChowSituation k) p 0) {J : Type*} [Fintype J]
    (W : J → X.IdealSheafData) (hW : ∀ i, IsIntegral (W i).subscheme) (n : J → ℤ)
    (hDim : ∀ i, schemeDeltaDimension (fieldChowSituation k) ((W i).subschemeι ≫ p) = (0 : EInt))
    (hα : α.1 = ∑ i, @Function.locallyFinsuppWithin.single X _ ℤ (Classical.decEq X) _
      (genericPointOf (W i) (hW i)) (n i)) :
    cycleDegree (fieldChowSituation k) p s α =
      ∑ i : J, n i *
        (letI : Algebra k Γ((W i).subscheme, ⊤) :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ ((W i).subschemeι ≫ p).appTop).hom.toAlgebra
        (Module.finrank k Γ((W i).subscheme, ⊤) : ℤ))
```

## Tag 0AZ3, a lemma

[Tag 0AZ3](https://stacks.math.columbia.edu/tag/0AZ3) in the Stacks Project.

**`AlgebraicGeometry.curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochGenuine.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RiemannRochGenuine.lean#L305).

> **Equation [Stacks, Tag 0BRY]**, in the orientation of the source:
> `deg(ℰ) = deg(c₁(ℰ) ∩ [X]_1)` for `ℰ` finite locally free of constant rank on a proper scheme of
> dimension at most one over a field, with `c₁(ℰ) ∩ -` the operation of Stacks 02U5 at the Chern
> classes of Stacks 02U0 and `deg` the degree of Stacks 0AZ1.
>
> Two conventions are fixed here. In rank zero Stacks 02U5 defines no `c₁`; the total Chern class
> of a module of rank zero is `1`, so `c₁ = 0`, and `GenuineChern.firstChernCapOnCycles` is zero
> there by definition. The operation of Stacks 02U5 extends `[W] ↦ i_*(c₁(i^*ℰ) ∩ [W])` over
> cycles through representatives of the classes of Stacks 02U0 (`GenuineChern.chowRep`); the choice
> does not matter here, since `[X]_1` is a finite sum of fundamental cycles of one-dimensional
> components and on each the class is the one of Stacks 02U0
> (`GenuineChern.chernCapOnCycles_integral_cycle`).

```lean
theorem curveDegree_eq_chowDegree_firstChernCapOnCycles_fundamental
    (hdim : topologicalKrullDim X ≤ 1) (E : X.Modules) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] :
    curveDegree k p hdim E r =
      chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) p
        (IsLocalRing.closedPoint k)
        (chowGroupCast (fieldChowSituation k) p (show (1 : ℤ) - 1 = 0 by simp)
          (GenuineChern.firstChernCapOnCycles (fieldChowSituation k) p E r 1
            (cycleAssociatedToClosedSubscheme (fieldChowSituation k) p (𝟙 X) 1)))
```

## Tag 0BFI, a lemma

[Tag 0BFI](https://stacks.math.columbia.edu/tag/0BFI) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_eq_chowDegree_iteratedFirstChernCap_and_ample`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/ChowDegree.lean, line 1155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/ChowDegree.lean#L1155).

> Let `k` be a field, let `X` be a proper scheme over `k` and let `Z ⊆ X` be a closed
> subscheme of dimension `d`. For invertible `𝒪_X`-modules `𝓛_1, …, 𝓛_d`,
>
> `(𝓛_1 ⋯ 𝓛_d · Z) = deg(c₁(𝓛_1) ∩ ⋯ ∩ c₁(𝓛_d) ∩ [Z]_d)`,
>
> and in particular, for an ample invertible `𝒪_X`-module `𝓛`,
>
> `deg_𝓛(Z) = deg(c₁(𝓛)^d ∩ [Z]_d)`.
>
> Here `(𝓛_1 ⋯ 𝓛_d · Z)` is the intersection number of [Stacks, Tag 0BEP], `deg_𝓛(Z)` the degree
> of [Stacks, Tag 0BEW], and `deg` the degree of zero cycles of [Stacks, Tag 0AZ1], for the Chow
> groups over `Spec k` with its zero dimension function.

```lean
theorem intersectionNumber_eq_chowDegree_iteratedFirstChernCap_and_ample {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (dimZ : topologicalKrullDim Z = d) :
    (∀ (L : Fin d → X.Modules) [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)],
      intersectionNumber k f i d dimZ.le L =
        chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) f
          (IsLocalRing.closedPoint k)
          (iteratedFirstChernCap k f L
            (QuotientAddGroup.mk' (rationalEquivalences (fieldChowSituation k) f d)
              (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f i d)))) ∧
    (∀ (L : X.Modules) [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
      (ample : Scheme.Modules.IsAmple X L),
      degreeWithRespectTo k f i d dimZ L ample =
        chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction_eq_zero k) f
          (IsLocalRing.closedPoint k)
          (iteratedFirstChernCap k f (fun _ : Fin d => L)
            (QuotientAddGroup.mk' (rationalEquivalences (fieldChowSituation k) f d)
              (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f i d))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.41, Tag 0AZ0](https://stacks.math.columbia.edu/tag/0AZ0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
