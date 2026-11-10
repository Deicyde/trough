---
declaration: section
origin: cited
lean: Stacks.Discriminant.one_mem_complementaryModule_iff, Stacks.Discriminant.dedekindDifferent_eq_map_ideal, Stacks.Discriminant.trace_algebraMap_mem_range_of_flat, Stacks.Discriminant.trace_algebraMap_mem_range_of_isNormalRing, Stacks.Discriminant.complementaryModuleEquivDualizingModuleWithFormula, Stacks.Discriminant.complementaryModuleEquivDualizingModule_one_apply, Stacks.Discriminant.mem_dedekindDifferent_iff_smul_dual_le_trace
statement: formalized
proof: formalized
---

# 49.8 The Dedekind different

Section 49.8 of the Stacks Project, [Tag 0BW0](https://stacks.math.columbia.edu/tag/0BW0). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BW1, a lemma

[Tag 0BW1](https://stacks.math.columbia.edu/tag/0BW1) in the Stacks Project.

**`Stacks.Discriminant.one_mem_complementaryModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean#L50). The attribute's comment: “trace\_iff\_one\_mem”.

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

**`Stacks.Discriminant.dedekindDifferent_eq_map_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/DifferentIdeal.lean#L66). The attribute's comment: “one\_mem\_different\_ideal”.

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

**`Stacks.Discriminant.trace_algebraMap_mem_range_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTrace.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatTrace.lean#L141). The attribute's comment: “flat\_trace”.

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

**`Stacks.Discriminant.trace_algebraMap_mem_range_of_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/NormalTrace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/NormalTrace.lean#L100). The attribute's comment: “normal\_trace”.

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

**`Stacks.Discriminant.complementaryModuleEquivDualizingModuleWithFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/ComplementaryModule.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/ComplementaryModule.lean#L61).

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

**`Stacks.Discriminant.complementaryModuleEquivDualizingModule_one_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatCase.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatCase.lean#L66). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0BW3, part (1).** Under the canonical trace-pairing identification of
> the complementary module with the relative dualizing module, `1` becomes the trace
> functional.

```lean
theorem complementaryModuleEquivDualizingModule_one_apply (b : B) :
    algebraMap A (FractionRing A)
      (complementaryModuleEquivDualizingModule setup
        ⟨1, one_mem_complementaryModule_of_flat setup⟩ b) =
      setup.trace (algebraMap B (B ⊗[A] FractionRing A) b)
```

**`Stacks.Discriminant.mem_dedekindDifferent_iff_smul_dual_le_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatCase.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/DedekindDifferent/FlatCase.lean#L78). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0BW3, part (2).** An element of `B` lies in the Dedekind different
> exactly when multiplication by it carries the whole relative dualizing module into the `B`-line
> generated by the trace functional.

```lean
theorem mem_dedekindDifferent_iff_smul_dual_le_trace (b : B) :
    algebraMap B (B ⊗[A] FractionRing A) b ∈ setup.dedekindDifferent ↔
      ∀ f : Module.Dual A B,
        b • f ∈ Submodule.span B
          { complementaryModuleEquivDualizingModule setup
              ⟨1, one_mem_complementaryModule_of_flat setup⟩ }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.8, Tag 0BW0](https://stacks.math.columbia.edu/tag/0BW0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
