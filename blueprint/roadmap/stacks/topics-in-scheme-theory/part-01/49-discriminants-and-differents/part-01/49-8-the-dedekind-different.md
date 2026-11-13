---
declaration: section
origin: cited
lean: Stacks.Discriminant.one_mem_complementaryModule_iff, Stacks.Discriminant.dedekindDifferent_eq_map_ideal, Stacks.Discriminant.trace_algebraMap_mem_range_of_flat, Stacks.Discriminant.trace_algebraMap_mem_range_of_isNormalRing, Stacks.Discriminant.complementaryModuleEquivDualizingModuleWithFormula, Stacks.Discriminant.complementaryModuleEquivDualizingModule_one_eq_traceElement, Stacks.Discriminant.mem_dedekindDifferentIdeal_iff_smul_mem_span_traceElement, Stacks.Discriminant.dedekindDifferent_eq_image_setOf_smul_mem_span_traceElement
statement: formalized
proof: formalized
---

# 49.8 The Dedekind different

Section 49.8 of the Stacks Project, [Tag 0BW0](https://stacks.math.columbia.edu/tag/0BW0). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BW1, a lemma

[Tag 0BW1](https://stacks.math.columbia.edu/tag/0BW1) in the Stacks Project.

**`Stacks.Discriminant.one_mem_complementaryModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean#L50). The attribute's comment: “trace\_iff\_one\_mem”.

> One lies in the Dedekind complementary module exactly when the generic-fibre trace of every
> element of `B` belongs to the canonical image of `A` in its total quotient ring.

```lean
theorem one_mem_complementaryModule_iff (setup : DedekindDifferentSetup A B) :
    letI : Algebra (FractionRing A) (B ⊗[A] FractionRing A) :=
      Algebra.TensorProduct.rightAlgebra
    (1 : B ⊗[A] FractionRing A) ∈ setup.complementaryModule ↔
      ∀ b : B, setup.trace (algebraMap B (B ⊗[A] FractionRing A) b) ∈
        Set.range (algebraMap A (FractionRing A))
```

**`Stacks.Discriminant.dedekindDifferent_eq_map_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean#L66). The attribute's comment: “one\_mem\_different\_ideal”.

> If one lies in the complementary module, the Dedekind different is the
> image of an ideal of `B`.

```lean
theorem dedekindDifferent_eq_map_ideal
    (setup : DedekindDifferentSetup A B)
    (h_one : (1 : B ⊗[A] FractionRing A) ∈ setup.complementaryModule) :
    setup.dedekindDifferent =
      Submodule.map (Algebra.linearMap B (B ⊗[A] FractionRing A))
        (dedekindDifferentIdeal setup : Submodule B B)
```

**`Stacks.Discriminant.trace_algebraMap_mem_range_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTrace.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTrace.lean#L138). The attribute's comment: “flat\_trace”.

> **Stacks Project, Tag 0BW1 (flat trace).** In the setup for the Dedekind
> different, if `B` is flat over `A`, then the generic-fibre trace of every
> element of `B` belongs to the canonical image of `A` in its total quotient
> ring.

```lean
theorem trace_algebraMap_mem_range_of_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (setup : DedekindDifferentSetup A B) [Module.Flat A B]
    (b : B) :
    letI : Algebra (FractionRing A) (B ⊗[A] FractionRing A) :=
      Algebra.TensorProduct.rightAlgebra
    setup.trace (algebraMap B (B ⊗[A] FractionRing A) b) ∈
      Set.range (algebraMap A (FractionRing A))
```

**`Stacks.Discriminant.trace_algebraMap_mem_range_of_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/NormalTrace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/NormalTrace.lean#L100). The attribute's comment: “normal\_trace”.

> In the setup for the Dedekind different, if `A` is a normal ring, then the generic-fibre
> trace of every element of `B` belongs to the canonical image of `A` in its total quotient
> ring.

```lean
theorem trace_algebraMap_mem_range_of_isNormalRing
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (setup : DedekindDifferentSetup A B) (hA : IsNormalRing A) (b : B) :
    letI : Algebra (FractionRing A) (B ⊗[A] FractionRing A) :=
      Algebra.TensorProduct.rightAlgebra
    setup.trace (algebraMap B (B ⊗[A] FractionRing A) b) ∈
      Set.range (algebraMap A (FractionRing A))
```

## Tag 0BW2, a lemma

[Tag 0BW2](https://stacks.math.columbia.edu/tag/0BW2) in the Stacks Project.

**`Stacks.Discriminant.complementaryModuleEquivDualizingModuleWithFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/ComplementaryModule.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/ComplementaryModule.lean#L61).

> **Stacks Project, Tag 0BW2.** The trace pairing canonically identifies the Dedekind
> complementary module with the relative dualizing module `Hom_A(B, A)` of a finite map, together
> with the formula characterizing it: the image of `x` is the functional `b ↦ Tr(bx)`.

```lean
def complementaryModuleEquivDualizingModuleWithFormula
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (setup : DedekindDifferentSetup A B) :
    { e : setup.complementaryModule ≃ₗ[B] Module.Dual A B //
      ∀ (x : setup.complementaryModule) (b : B),
        algebraMap A (FractionRing A) (e x b) =
          setup.trace
            (algebraMap B (B ⊗[A] FractionRing A) b *
              (x : B ⊗[A] FractionRing A)) }
```

## Tag 0BW3, a lemma

[Tag 0BW3](https://stacks.math.columbia.edu/tag/0BW3) in the Stacks Project.

**`Stacks.Discriminant.complementaryModuleEquivDualizingModule_one_eq_traceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean#L80). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0BW3, part (1).** If the Dedekind different of a flat algebra `A → B`
> is defined, the canonical isomorphism `L_{B/A} → ω_{B/A}` (Tag 0BW2, followed by the canonical
> identification `Hom_A(B, A) ≅ ω_{B/A}` for a finite-open factorization `F`) sends `1` to the trace
> element `τ_{B/A}` of Tag 0BT6.

```lean
theorem complementaryModuleEquivDualizingModule_one_eq_traceElement :
    letI : IsNoetherianRing A := setup.isNoetherianRing
    letI : Module.Finite A B := setup.finite
    letI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
    ∀ (F : FiniteOpenFactorization.{u, v, w} A B) (τ : dualizingModule F),
      IsTraceElement.{u, v, w, u, max u v, max u v} F τ →
        dualizingModuleEquiv (selfFactorization A B) F
            (selfFactorizationDualEquiv.symm
              (complementaryModuleEquivDualizingModule setup
                ⟨1, one_mem_complementaryModule_of_flat setup⟩)) = τ
```

**`Stacks.Discriminant.mem_dedekindDifferentIdeal_iff_smul_mem_span_traceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean#L107). The attribute's comment: “part (2), membership form”.

> **Stacks Project, Tag 0BW3, part (2), membership form.** If the Dedekind different of a flat
> algebra `A → B` is defined, an element `b ∈ B` lies in the Dedekind different exactly when
> `b ω_{B/A} ⊆ B τ_{B/A}`.

```lean
theorem mem_dedekindDifferentIdeal_iff_smul_mem_span_traceElement :
    letI : IsNoetherianRing A := setup.isNoetherianRing
    letI : Module.Finite A B := setup.finite
    letI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
    ∀ (F : FiniteOpenFactorization.{u, v, w} A B) (τ : dualizingModule F),
      IsTraceElement.{u, v, w, u, max u v, max u v} F τ → ∀ b : B,
        b ∈ dedekindDifferentIdeal setup ↔
          ∀ x : dualizingModule F, b • x ∈ Submodule.span B {τ}
```

**`Stacks.Discriminant.dedekindDifferent_eq_image_setOf_smul_mem_span_traceElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTraceElement.lean#L141). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0BW3, part (2).** If the Dedekind different of a flat algebra `A → B`
> is defined, then `𝔇_{B/A} = {b ∈ B | b ω_{B/A} ⊆ B τ_{B/A}}`, as a subset of the generic fibre
> `L = B ⊗_A Q(A)` in which the Dedekind different is defined.

```lean
theorem dedekindDifferent_eq_image_setOf_smul_mem_span_traceElement :
    letI : IsNoetherianRing A := setup.isNoetherianRing
    letI : Module.Finite A B := setup.finite
    letI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
    ∀ (F : FiniteOpenFactorization.{u, v, w} A B) (τ : dualizingModule F),
      IsTraceElement.{u, v, w, u, max u v, max u v} F τ →
        (setup.dedekindDifferent : Set (B ⊗[A] FractionRing A)) =
          algebraMap B (B ⊗[A] FractionRing A) ''
            {b | ∀ x : dualizingModule F, b • x ∈ Submodule.span B {τ}}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.8, Tag 0BW0](https://stacks.math.columbia.edu/tag/0BW0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
