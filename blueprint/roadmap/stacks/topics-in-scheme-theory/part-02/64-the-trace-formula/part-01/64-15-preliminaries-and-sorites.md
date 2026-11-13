---
declaration: section
origin: cited
lean: Stacks.Trace.epsilon_comp_mk, Stacks.Trace.groupTrace, Stacks.Trace.projectiveModuleTrace_restrictScalars_groupAlgebra, Stacks.Trace.inducedAdditiveCommutatorQuotientModule, Stacks.Trace.diagonalAction_module_finite, Stacks.Trace.diagonalAction_module_projective, Stacks.Trace.groupTrace_diagonalTensorEndomorphism, Stacks.Trace.trace_eq_card_centralizer_nsmul_groupTrace
statement: formalized
proof: formalized
---

# 64.15 Preliminaries and sorites

Section 64.15 of the Stacks Project, [Tag 03U4](https://stacks.math.columbia.edu/tag/03U4). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03U5, a lemma

[Tag 03U5](https://stacks.math.columbia.edu/tag/03U5) in the Stacks Project.

**`Stacks.Trace.epsilon_comp_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/GroupTrace.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/GroupTrace.lean#L119). References: SGA 4½ Rapport (5.5), “ε factorization”.

> The chosen coefficient-of-the-identity map factors the map on the group ring.

```lean
theorem epsilon_comp_mk (R : Type u) (G : Type v) [Ring R] [Group G] :
    (epsilon R G).comp (additiveCommutatorQuotientMk R[G]) =
      coeffOneToAdditiveCommutatorQuotient R G
```

## Tag 03U6, a definition

[Tag 03U6](https://stacks.math.columbia.edu/tag/03U6) in the Stacks Project.

**`Stacks.Trace.groupTrace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/GroupTrace.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/GroupTrace.lean#L143). References: SGA 4½ Rapport (5.5), “tr\_Λ^H definition”.

> The group trace of an endomorphism of a finite projective group-ring module.

```lean
noncomputable abbrev groupTrace (R : Type u) (G : Type v) [Ring R] [Group G]
    (P : Type w) [AddCommGroup P] [Module R[G] P] [Module.Finite R[G] P]
    [Module.Projective R[G] P] (f : Module.End R[G] P) :
    AdditiveCommutatorQuotient R
```

## Tag 03U7, a lemma

[Tag 03U7](https://stacks.math.columbia.edu/tag/03U7) in the Stacks Project.

**`Stacks.Trace.projectiveModuleTrace_restrictScalars_groupAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/RestrictScalars.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/RestrictScalars.lean#L200). References: SGA 4½ Rapport (5.6); SGA 5 IIIB (5.10.11), “A = K = R”; SGA 5 IIIB (5.13), “(1), special case”; SGA 5 IIIB (6.7), “special case”.

> **Stacks Project, Tag 03U7.** The coefficient-ring trace of an endomorphism of a finite
> projective module over the group algebra of a finite group is the order of the group times its
> group trace.

```lean
theorem projectiveModuleTrace_restrictScalars_groupAlgebra
    (R : Type u) (G : Type v) (P : Type w) [Ring R] [Group G] [Finite G]
    [AddCommGroup P] [Module R[G] P]
    [Module.Finite R[G] P] [Module.Projective R[G] P]
    (f : Module.End R[G] P) :
    letI : Module R P := Module.compHom P
      (MonoidAlgebra.singleOneRingHom (R := R) (M := G))
    letI : Module.Finite R P := finite_restrictScalars_groupAlgebra R G P
    letI : Module.Projective R P := projective_restrictScalars_groupAlgebra R G P
    let fR : Module.End R P :=
      { f with
        map_smul' := by
          intro r p
          exact f.map_smul (MonoidAlgebra.singleOneRingHom (R := R) (M := G) r) p }
    projectiveModuleTrace R P fR =
      (Nat.card G) • groupTrace R G P f
```

## Tag 03U8, a lemma

[Tag 03U8](https://stacks.math.columbia.edu/tag/03U8) in the Stacks Project.

**`Stacks.Trace.inducedAdditiveCommutatorQuotientModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/QuotientModule.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/QuotientModule.lean#L67).

> A central map `A → Λ` induces an `A`-module structure on the
> additive commutator quotient of `Λ`.

```lean
noncomputable def inducedAdditiveCommutatorQuotientModule
    (A Λ : Type*) [CommRing A] [Ring Λ] [Algebra A Λ] :
    InducedAdditiveCommutatorQuotientModule A Λ
```

## Tag 03U9, a lemma

[Tag 03U9](https://stacks.math.columbia.edu/tag/03U9) in the Stacks Project.

**`Stacks.Trace.diagonalAction_module_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/DiagonalAction.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/DiagonalAction.lean#L403). The attribute's comment: “finiteness”.

> A tensor product with diagonal action is finite over the
> group algebra when both input modules are finite over their respective rings.

```lean
lemma diagonalAction_module_finite
    {A : Type uA} {Λ : Type uΛ} {G : Type uG} {P : Type uP} {M : Type uM}
    [CommRing A] [Ring Λ] [Algebra A Λ] [Group G]
    [AddCommGroup P] [Module A P]
    [AddCommGroup M] [Module A M] [Module Λ M] [IsScalarTower A Λ M]
    (ρ : _root_.Representation A G P) (σ : _root_.Representation Λ G M)
    [Module.Finite A[G] (Representation.asModuleNC ρ)] [Module.Finite Λ M] :
    Module.Finite Λ[G] (Representation.asModuleNC (Representation.tprodAlgebra ρ σ))
```

**`Stacks.Trace.diagonalAction_module_projective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Preliminaries/DiagonalAction.lean, line 960](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Preliminaries/DiagonalAction.lean#L960). The attribute's comment: “projectivity”. References: SGA 4½ Rapport (5.7), “more general”; SGA 4½ Rapport (5.9), “P⊗M projective”.

> A tensor product with diagonal action is projective over the group algebra when the first
> input is projective over its group algebra and the second is projective over the coefficient
> ring.

```lean
lemma diagonalAction_module_projective
    {A : Type uA} {Λ : Type uΛ} {G : Type uG} {P : Type uP} {M : Type uM}
    [CommRing A] [Ring Λ] [Algebra A Λ] [Group G]
    [AddCommGroup P] [Module A P]
    [AddCommGroup M] [Module A M] [Module Λ M] [IsScalarTower A Λ M]
    (ρ : _root_.Representation A G P) (σ : _root_.Representation Λ G M)
    [Module.Projective A[G] (Representation.asModuleNC ρ)] [Module.Projective Λ M] :
    Module.Projective Λ[G]
      (Representation.asModuleNC (Representation.tprodAlgebra ρ σ))
```

## Tag 03UA, a lemma

[Tag 03UA](https://stacks.math.columbia.edu/tag/03UA) in the Stacks Project.

**`Stacks.Trace.groupTrace_diagonalTensorEndomorphism`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Multiplicativity.lean, line 541](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Multiplicativity.lean#L541). References: SGA 4½ Rapport (5.8); SGA 5 IIIB (5.12), “special case”; SGA 6 I (8.6), “Punctual (affine) case”.

> The group trace is multiplicative for the diagonal tensor product action.

```lean
lemma groupTrace_diagonalTensorEndomorphism
    {A : Type uA} {Λ : Type uΛ} {G : Type uG} {P : Type uP} {M : Type uM}
    [CommRing A] [Ring Λ] [Algebra A Λ] [Group G]
    [AddCommGroup P] [Module A P]
    [AddCommGroup M] [Module A M] [Module Λ M] [IsScalarTower A Λ M]
    (ρ : _root_.Representation A G P) (σ : _root_.Representation Λ G M)
    [Module.Finite A[G] (asModuleNC ρ)] [Module.Projective A[G] (asModuleNC ρ)]
    [Module.Finite Λ M] [Module.Projective Λ M]
    (u : Module.End A[G] (asModuleNC ρ))
    (v : Module.End Λ[G] (asModuleNC σ)) :
    diagonalTensorGroupTrace ρ σ u v =
      commutativeAdditiveCommutatorQuotientEval A
          (groupTrace A G (asModuleNC ρ) u) •
      projectiveModuleTrace Λ M
          (groupAlgebraEnd_restrictScalars σ v)
```

## Tag 03UB, a lemma

[Tag 03UB](https://stacks.math.columbia.edu/tag/03UB) in the Stacks Project.

**`Stacks.Trace.trace_eq_card_centralizer_nsmul_groupTrace`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Centralizer.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Centralizer.lean#L331). References: SGA 4½ Rapport (5.9), “(5.9.1)”.

> The ordinary trace is the centralizer order times the centralizer trace.

```lean
lemma trace_eq_card_centralizer_nsmul_groupTrace (i : G →* Γ)
    [Module.Finite Λ[G] (restrictedModule Λ P i)]
    [Module.Projective Λ[G] (restrictedModule Λ P i)]
    (γ : Γ) :
    letI : Module.Finite Λ (coefficientModule Λ Γ P) :=
      finite_over_coefficients (P := P) i
    letI : Module.Projective Λ (coefficientModule Λ Γ P) :=
      projective_over_coefficients (P := P) i
    projectiveModuleTrace Λ (coefficientModule Λ Γ P)
      (coefficientEndomorphism (P := P) γ).val =
      Nat.card (centralizer i γ) • centralizerTrace (P := P) i γ
```

## Tag 03UC, a lemma

[Tag 03UC](https://stacks.math.columbia.edu/tag/03UC) in the Stacks Project.

**`Stacks.Trace.MonoidExtensionByNat.diagonalTensorCentralizerTrace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/CentralizerMultiplicativity.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/CentralizerMultiplicativity.lean#L79). References: SGA 4½ Rapport (5.9), “(5.9.2)”; SGA 5 IIIB (5.12), “special case”; SGA 6 I (8.6), “Punctual (affine) case”.

> The centralizer trace is multiplicative for the diagonal action on a tensor product.

```lean
theorem MonoidExtensionByNat.diagonalTensorCentralizerTrace_eq
    {A : Type uA} {Λ : Type uΛ} {G : Type uG} {Γ : Type uΓ} {P : Type uP} {M : Type uM}
    [CommRing A] [Ring Λ] [Algebra A Λ] [Group G] [Finite G] [Monoid Γ]
    [AddCommGroup P] [Module A P]
    [AddCommGroup M] [Module A M] [Module Λ M] [IsScalarTower A Λ M]
    (E : MonoidExtensionByNat G Γ)
    (ρ : _root_.Representation A Γ P) (σ : _root_.Representation Λ Γ M)
    [Module.Finite A[G] (asModuleNC (restrictedRepresentation E ρ))]
    [Module.Projective A[G] (asModuleNC (restrictedRepresentation E ρ))]
    [Module.Finite Λ M] [Module.Projective Λ M]
    (γ : Γ) :
    E.diagonalTensorCentralizerTrace ρ σ γ =
      commutativeAdditiveCommutatorQuotientEval A (E.centralizerTrace ρ γ) •
        projectiveModuleTrace Λ M (σ γ)
```

## Tag 03UD, a lemma

[Tag 03UD](https://stacks.math.columbia.edu/tag/03UD) in the Stacks Project.

**`Stacks.Trace.coinvariantRepresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean#L157). The attribute's comment: “the action on coinvariants”. References: SGA 4½ Rapport (5.10), “action of G^+ on P\_H”.

> The canonical action of the quotient monoid `ℕ` on the coinvariants.  Its
> specification records compatibility with every lift in `Γ`.

```lean
noncomputable def coinvariantRepresentation (E : MonoidExtensionByNat G Γ)
    [AddCommGroup P] [Module Λ P] (ρ : _root_.Representation Λ Γ P) :
    { σ : _root_.Representation Λ (Multiplicative ℕ)
        (coinvariants (restrictedRepresentation E ρ)) //
      ∀ (γ : Γ) (p : P),
        σ (E.degree γ) (coinvariantsMk (restrictedRepresentation E ρ) p) =
          coinvariantsMk (restrictedRepresentation E ρ) (ρ γ p) }
```

**`Stacks.Trace.coinvariants_module_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean#L471). The attribute's comment: “finiteness of the coinvariants”.

> The coinvariants of a finite `Λ[G]`-projective representation are finite
> over `Λ`.

```lean
lemma coinvariants_module_finite
    [AddCommGroup P] [Module Λ P] (σ : _root_.Representation Λ G P)
    [Module.Finite Λ[G] (Representation.asModuleNC
      σ)] :
    Module.Finite Λ (coinvariants σ)
```

**`Stacks.Trace.coinvariants_module_projective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean#L535). The attribute's comment: “projectivity of the coinvariants”. References: SGA 4½ Rapport (5.10), “P\_H projective over Λ”.

> The coinvariants of a finite `Λ[G]`-projective representation are
> projective over `Λ`.

```lean
lemma coinvariants_module_projective
    [AddCommGroup P] [Module Λ P] (σ : _root_.Representation Λ G P)
    [Module.Projective Λ[G] (Representation.asModuleNC
      σ)] :
    Module.Projective Λ (coinvariants σ)
```

**`Stacks.Trace.trace_degreeOne_on_coinvariants`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean, line 927](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/Coinvariants.lean#L927). The attribute's comment: “the trace identity”. References: SGA 4½ Rapport (5.11).

> The trace of degree one on the coinvariants is the sum of the centralizer
> traces over the `G`-conjugacy classes of degree-one elements.

```lean
lemma trace_degreeOne_on_coinvariants [Finite G] (E : MonoidExtensionByNat G Γ)
    [AddCommGroup P] [Module Λ P] (ρ : _root_.Representation Λ Γ P)
    [Module.Finite Λ[G] (Representation.asModuleNC
      (restrictedRepresentation E ρ))]
    [Module.Projective Λ[G] (Representation.asModuleNC
      (restrictedRepresentation E ρ))]
    (S : Finset Γ) (hS : IsConjugacyClassRepresentatives E (.ofAdd 1) S) :
    letI := coinvariants_module_finite (restrictedRepresentation E ρ)
    letI := coinvariants_module_projective (restrictedRepresentation E ρ)
    projectiveModuleTrace Λ (coinvariants (restrictedRepresentation E ρ))
        ((coinvariantRepresentation E ρ).val (.ofAdd 1)) =
      ∑ γ ∈ S, MonoidExtensionByNat.centralizerTrace E ρ γ
```

## Tag 03UE, a remark

[Tag 03UE](https://stacks.math.columbia.edu/tag/03UE) in the Stacks Project.

**`Stacks.Trace.isZero_groupHomology_trivial_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean#L55). The attribute's comment: “the vanishing of the homology of `G` in positive degrees”.

> The homology of a finite group with coefficients in the trivial module given by a field
> in which the order of the group is invertible vanishes in positive degrees.

```lean
theorem isZero_groupHomology_trivial_succ (Λ : Type u) (G : Type u) [Field Λ] [Group G]
    [Finite G] [NeZero (Nat.card G : Λ)] (n : ℕ) :
    Limits.IsZero (groupHomology (Rep.trivial Λ G Λ) (n + 1))
```

**`Stacks.Trace.sum_inv_card_centralizer_degreeOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean#L68). The attribute's comment: “the trivial trace formula”.

> The reciprocals of the orders of the centralizers of the degree-one elements of the
> extension monoid, summed over their `G`-conjugacy classes, add up to `1` in any field in which
> the order of `G` is invertible.

```lean
theorem sum_inv_card_centralizer_degreeOne {Λ : Type u} {G : Type v} {Γ : Type w} [Field Λ]
    [Group G] [Finite G] [Monoid Γ] [NeZero (Nat.card G : Λ)] (E : MonoidExtensionByNat G Γ)
    (S : Finset Γ) (hS : IsConjugacyClassRepresentatives E (.ofAdd 1) S) :
    ∑ γ ∈ S, (Nat.card (centralizer E.inclusion γ) : Λ)⁻¹ = 1
```

Declarations registered for the tag:

- [`groupHomology.H0IsoOfIsTrivial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=groupHomology.H0IsoOfIsTrivial#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Trace/Sorites/TrivialTraceFormula.lean#L62) (StacksFrontier): “the homology in degree zero”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.15, Tag 03U4](https://stacks.math.columbia.edu/tag/03U4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
