---
declaration: section
origin: cited
lean: Stacks.Module.FinitenessViaHomColimit.finite_iff_comparisonMap_injective, Module.IsRelation, Module.exists_linearEquiv_directLimit_finitePresentation, Module.exists_linearEquiv_directLimit_finitePresentation_max, finitePresentation_iff_comparisonMap_bijective
statement: formalized
proof: formalized
---

# 10.11 Characterizing finite and finitely presented modules

Section 10.11 of the Stacks Project, [Tag 0G8M](https://stacks.math.columbia.edu/tag/0G8M). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G8N, a lemma

[Tag 0G8N](https://stacks.math.columbia.edu/tag/0G8N) in the Stacks Project.

**`Stacks.Module.FinitenessViaHomColimit.finite_iff_comparisonMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Finiteness/HomColimit.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Finiteness/HomColimit.lean#L362). References: EGA IV (8.5.2.1), “Forward implication”.

> **Stacks Tag 0G8N.** An `R`-module `N` is finite (finitely generated) if and
> only if for every filtered colimit `M = colim_i M_i` of `R`-modules the canonical
> comparison map `Θ_N : colim_i Hom_R(N, M_i) → Hom_R(N, M)` is injective.

```lean
theorem finite_iff_comparisonMap_injective (N : ModuleCat.{w} R) :
    Module.Finite R N ↔ InjectiveForAllFilteredColimits R N
```

## Tag 07N8, a definition

[Tag 07N8](https://stacks.math.columbia.edu/tag/07N8) in the Stacks Project.

**`Module.IsRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean#L215).

> `IsRelation f x` says that the coefficients `f` give a relation among the elements
> `x` of an `R`-module, i.e. `∑ i, f i • x i = 0`.

```lean
def IsRelation {R : Type*} [Semiring R] {M : Type*} [AddCommMonoid M] [Module R M]
    {ι : Type*} [Fintype ι] (f : ι → R) (x : ι → M) : Prop
```

## Tag 00HA, a lemma

[Tag 00HA](https://stacks.math.columbia.edu/tag/00HA) in the Stacks Project.

**`Module.exists_linearEquiv_directLimit_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean#L162).

> Every `R`-module `M` is the colimit of a directed system of finitely
> presented `R`-modules in the universe of `M`, provided `R` is small in that universe.

```lean
theorem Module.exists_linearEquiv_directLimit_finitePresentation
    (R : Type u) [Ring R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] :
    ∃ (ι : Type v) (_ : Preorder ι) (_ : IsDirectedOrder ι) (_ : Nonempty ι)
      (_ : DecidableEq ι)
      (G : ι → Type v) (_ : (i : ι) → AddCommGroup (G i))
      (_ : (i : ι) → Module R (G i))
      (f : (i j : ι) → i ≤ j → (G i →ₗ[R] G j))
      (_ : DirectedSystem G (fun i j h => f i j h)),
      -- each module in the system is finitely presented
      (∀ i, Module.FinitePresentation R (G i)) ∧
      -- and M is isomorphic to the colimit of the system
      Nonempty (M ≃ₗ[R] Module.DirectLimit G f)
```

**`Module.exists_linearEquiv_directLimit_finitePresentation_max`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/FinitePresentation/Colimit.lean#L195). The attribute's comment: “no smallness assumption on the ring”.

> Every module is a directed colimit of finitely presented modules in the maximum of the
> universes of the ring and the module.

```lean
theorem Module.exists_linearEquiv_directLimit_finitePresentation_max
    (R : Type u) [Ring R] (M : Type v) [AddCommGroup M] [Module R M] :
    ∃ (ι : Type (max u v)) (_ : Preorder ι) (_ : IsDirectedOrder ι) (_ : Nonempty ι)
      (_ : DecidableEq ι)
      (G : ι → Type (max u v)) (_ : (i : ι) → AddCommGroup (G i))
      (_ : (i : ι) → Module R (G i))
      (f : (i j : ι) → i ≤ j → (G i →ₗ[R] G j))
      (_ : DirectedSystem G (fun i j h => f i j h)),
      (∀ i, Module.FinitePresentation R (G i)) ∧
      Nonempty (M ≃ₗ[R] Module.DirectLimit G f)
```

## Tag 0G8P, a lemma

[Tag 0G8P](https://stacks.math.columbia.edu/tag/0G8P) in the Stacks Project.

**`finitePresentation_iff_comparisonMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Finiteness/HomColimit.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Finiteness/HomColimit.lean#L692). References: EGA IV (8.5.2), “(i), special case”; EGA IV (8.5.2.1), “more general”; SGA 3 VIIB (0.3.5), “(3), special case”.

> **Stacks Tag 0G8P.** An `R`-module `N` is finitely presented if and only if for
> every directed (filtered) system of `R`-modules the canonical comparison map
> `Φ : colim_i Hom_R(N, M_i) → Hom_R(N, colim_i M_i)` is bijective.
>
> We quantify over index types `ι` and module families `G` in the universe `u` of `R` and `N`.
> The forward direction holds for directed systems in any universe. The converse uses the system
> of finitely generated submodules of `N`, which lives in the universe of `N`, and the system of
> quotients `(Fin n →₀ R) ⧸ S Q`, which lives in the universe of `R`.

```lean
theorem finitePresentation_iff_comparisonMap_bijective
    (R : Type u) [CommRing R] (N : Type u) [AddCommGroup N] [Module R N] :
    Module.FinitePresentation R N ↔
      ∀ {ι : Type u} [Preorder ι] [DecidableEq ι] [IsDirectedOrder ι] [Nonempty ι]
        (G : ι → Type u) [(i : ι) → AddCommGroup (G i)] [(i : ι) → Module R (G i)]
        (f : (i j : ι) → i ≤ j → G i →ₗ[R] G j)
        [DirectedSystem G (fun i j h => f i j h)],
        Function.Bijective (homColimComparison (R := R) (N := N) (ι := ι) G f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.11, Tag 0G8M](https://stacks.math.columbia.edu/tag/0G8M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
