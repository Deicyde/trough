---
declaration: section
origin: cited
lean: ModuleCat.exists_countable_directedOn_isColimit_whisker, Module.exists_end_factorization_finitePresentation_of_countable_span_of_mittagLeffler
statement: formalized
proof: formalized
---

# 10.92 Countably generated Mittag-Leffler modules

Section 10.92 of the Stacks Project, [Tag 05D1](https://stacks.math.columbia.edu/tag/05D1). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 059W, a lemma

[Tag 059W](https://stacks.math.columbia.edu/tag/059W) in the Stacks Project.

**`ModuleCat.exists_countable_directedOn_isColimit_whisker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/DirectLimit/Countable.lean, line 564](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/DirectLimit/Countable.lean#L564). The attribute's comment: “Mittag-Leffler as 059E (3); finite presentation of the members is unused”.

> **Stacks 059W.** Let `R` be a ring, `w`-small relative to the universe of the modules below,
> let `F : J ⥤ ModuleCat R` be a directed system of `R`-modules over a nonempty directed preorder
> `J`, and let `c` be a colimit cocone on `F`, so that `M = c.pt` is `colim_{i ∈ J} M i`. Assume that
> for every `i` there is a `j ≥ i` such that the transition map `M i → M j` factors through
> `M i → M k` for every `k ≥ i` — condition (3) of Stacks 059E, which for a system of finitely
> presented modules says exactly that `M` is Mittag-Leffler — and that `M` is spanned by a countable
> set. Then there is a nonempty countable directed subset `J' ⊆ J` such that `M`, with the canonical
> maps `M i → M` for `i ∈ J'`, is a colimit of the restricted system: `M = colim_{i ∈ J'} M i`.

```lean
public theorem ModuleCat.exists_countable_directedOn_isColimit_whisker
    {R : Type u} [Ring R] [Small.{w} R] {J : Type v} [Preorder J] [IsDirectedOrder J] [Nonempty J]
    {F : J ⥤ ModuleCat.{w} R}
    (hfac : ∀ i : J, ∃ (j : J) (u : i ⟶ j), ∀ (k : J) (v : i ⟶ k),
      ∃ h : F.obj k ⟶ F.obj j, F.map u = F.map v ≫ h)
    {c : Cocone F} (hc : IsColimit c)
    (hcg : ∃ t : Set c.pt, t.Countable ∧ Submodule.span R t = ⊤) :
    ∃ s : Set J, s.Nonempty ∧ s.Countable ∧ DirectedOn (· ≤ ·) s ∧
      Nonempty (IsColimit (c.whisker (Set.mono_coe s).functor))
```

## Tag 05D2, a lemma

[Tag 05D2](https://stacks.math.columbia.edu/tag/05D2) in the Stacks Project.

**`Module.exists_end_factorization_finitePresentation_of_countable_span_of_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Endomorphism.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Endomorphism.lean#L607). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N, 059P, 059R, 05CQ, 059X and 05D6; countable generation as a countable spanning set, as in 0590. Test data in the universe of `M`, whence `Small.{v} R`; the source's `P` keeps its own universe. Factoring through a finitely presented module is the equation `α = v ∘ₗ u`, as in `Module.Flat.exists_factorization_of_finitePresentation`. See the module docstring.”.

> Let `R` be a commutative ring and let `M` be an `R`-module which is countably generated — it
> admits a countable spanning set — and Mittag-Leffler, the latter in the intrinsic form 059E (1):
> every map `f : P → M` from a finitely presented module dominates and is dominated by a map
> `g : P → Q` into a finitely presented module, domination meaning `Ker (f ⊗ id_T) = Ker (g ⊗ id_T)`
> for every `R`-module `T`. Then for every `R`-module map `f : P → M` with `P` finitely generated
> there is an endomorphism `α : M → M` such that (1) `α` factors through a finitely presented
> `R`-module, that is `α = v ∘ₗ u` for some `u : M → Q` and `v : Q → M` with `Q` finitely presented,
> and (2) `α ∘ f = f`.

```lean
public theorem Module.exists_end_factorization_finitePresentation_of_countable_span_of_mittagLeffler
    (R : Type u) [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M]
    (hcg : ∃ s : Set M, s.Countable ∧ Submodule.span R s = ⊤)
    (hML : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T))
    {P : Type w} [AddCommGroup P] [Module R P] [Module.Finite R P] (f : P →ₗ[R] M) :
    ∃ α : M →ₗ[R] M,
      (∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q) (_ : Module.FinitePresentation R Q)
        (u : M →ₗ[R] Q) (v : Q →ₗ[R] M), α = v ∘ₗ u) ∧ α ∘ₗ f = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.92, Tag 05D1](https://stacks.math.columbia.edu/tag/05D1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
