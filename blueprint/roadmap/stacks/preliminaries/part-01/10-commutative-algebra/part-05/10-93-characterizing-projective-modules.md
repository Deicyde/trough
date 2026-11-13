---
declaration: section
origin: cited
lean: Module.Flat.projective_of_isMittagLeffler_of_countablyGenerated, Module.projective_iff_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span, Module.projective_of_forall_rTensor_injective_of_exists_sSupIndep_countable_span, Module.projective_of_forall_rTensor_injective_mvPowerSeries_of_exists_sSupIndep_countable_span
statement: formalized
proof: formalized
---

# 10.93 Characterizing projective modules

Section 10.93 of the Stacks Project, [Tag 059V](https://stacks.math.columbia.edu/tag/059V). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 059X, a lemma

[Tag 059X](https://stacks.math.columbia.edu/tag/059X) in the Stacks Project.

**`Module.Flat.projective_of_isMittagLeffler_of_countablyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Projective.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Projective.lean#L439). The attribute's comment: “Mittag-Leffler is `IsMittagLeffler` (059F) and countable generation is `Module.CountablyGenerated` (from Tag 0GVD), both cited by name; the companion statements write them out inline, `isMittagLeffler_def_iff` identifying the two forms. Test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> **Stacks 059X.** A flat, Mittag-Leffler, countably generated module over a commutative ring is
> projective. The Mittag-Leffler condition is `IsMittagLeffler` (Definition 059F), with its finitely
> presented modules and test modules taken in the universe of `M`; countable generation is
> `Module.CountablyGenerated`, the existence of a countable spanning set.

```lean
public theorem Module.Flat.projective_of_isMittagLeffler_of_countablyGenerated
    (R : Type u) [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M]
    [Module.Flat R M] (hML : IsMittagLeffler.{u, v, v, v, v} R M)
    (hcg : Module.CountablyGenerated R M) :
    Module.Projective R M
```

## Tag 059Z, a theorem

[Tag 059Z](https://stacks.math.columbia.edu/tag/059Z) in the Stacks Project.

**`Module.projective_iff_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/ProjectiveCharacterization.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/ProjectiveCharacterization.lean#L233). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N, 059P, 059R, 05CQ, 05D6 and 059X; the direct sum decomposition internally, as an independent set of submodules of `M` with supremum `⊤`, as in 058W and 058Y, with countable generation as a countable spanning set, as in 0590. Test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> Let `R` be a commutative ring and `M` an `R`-module. Then `M` is projective if and only if (1)
> `M` is flat, (2) `M` is Mittag-Leffler, and (3) `M` is a direct sum of countably generated
> `R`-modules. Being Mittag-Leffler is spelled out in the intrinsic form 059E (1): every map
> `f : P → M` from a finitely presented module dominates and is dominated by a map `g : P → Q` into a
> finitely presented module, domination meaning `Ker(f ⊗ id_T) = Ker(g ⊗ id_T)` for every `R`-module
> `T`. Being a direct sum of countably generated modules is spelled internally, as in 058W and 058Y:
> an independent set of submodules of `M` with supremum `⊤`, each spanned by a countable set.

```lean
public theorem Module.projective_iff_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span
    (R : Type u) [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M] :
    Module.Projective R M ↔
      Module.Flat R M ∧
        (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
            (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
              (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
                [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)) ∧
        (∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
          ∀ N ∈ S, ∃ t : Set M, t.Countable ∧ Submodule.span R t = N)
```

## Tag 05A0, a lemma

[Tag 05A0](https://stacks.math.columbia.edu/tag/05A0) in the Stacks Project.

**`Module.projective_of_forall_rTensor_injective_of_exists_sSupIndep_countable_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean#L390). The attribute's comment: “Universal injectivity of `f` is injectivity of `f ⊗ id_T` for every `T`, as in 058K (1) and 059N; Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059N, 059X and 059Z; the direct sum decomposition internally, as an independent set of submodules of `M` with supremum `⊤`, as in 058W and 058Y, with countable generation as a countable spanning set, as in 0590. Test data in the universe of `M` and `N`, whence `Small.{v} R`. See the module docstring.”.

> Let `f : M → N` be a universally injective map of `R`-modules, that is, one for which
> `f ⊗ id_T` is injective for every `R`-module `T`. Suppose `M` is a direct sum of countably
> generated `R`-modules and suppose `N` is flat and Mittag-Leffler. Then `M` is projective. Being a
> direct sum of countably generated modules is spelled internally, as in 058W and 058Y: an
> independent set of submodules of `M` with supremum `⊤`, each spanned by a countable set. Being
> Mittag-Leffler is spelled out in the intrinsic form 059E (1): every map `g : P → N` from a finitely
> presented module dominates and is dominated by a map `h : P → Q` into a finitely presented module,
> domination meaning `Ker(g ⊗ id_T) = Ker(h ⊗ id_T)` for every `R`-module `T`.

```lean
public theorem Module.projective_of_forall_rTensor_injective_of_exists_sSupIndep_countable_span
    (R : Type u) [CommRing R] [Small.{v} R] (M : Type v) [AddCommGroup M] [Module R M]
    (N : Type v) [AddCommGroup N] [Module R N] [Module.Flat R N] (f : M →ₗ[R] N)
    (hf : ∀ (T : Type v) [AddCommGroup T] [Module R T], Function.Injective (f.rTensor T))
    (hM : ∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ K ∈ S, ∃ t : Set M, t.Countable ∧ Submodule.span R t = K)
    (hML : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (g : P →ₗ[R] N), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (h : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (g.rTensor T) = LinearMap.ker (h.rTensor T)) :
    Module.Projective R M
```

## Tag 05A1, a lemma

[Tag 05A1](https://stacks.math.columbia.edu/tag/05A1) in the Stacks Project.

**`Module.projective_of_forall_rTensor_injective_mvPowerSeries_of_exists_sSupIndep_countable_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/CountablyGenerated.lean#L549). The attribute's comment: “`R[[t_1, …, t_n]]` is `MvPowerSeries (Fin n) R` with its coefficientwise `R`-module structure, as in 059T; universal injectivity of `f` is injectivity of `f ⊗ id_T` for every `T`, as in 058K (1), 059N and 05A0; the direct sum decomposition internally, as an independent set of submodules of `M` with supremum `⊤` each spanned by a countable set, as in 058W, 058Y and 05A0. `n` and `f` are parameters rather than existentially bound, the conclusion mentioning neither, and no positivity of `n` is assumed, as none is in the source. See the module docstring.”.

> Let `R` be a Noetherian ring and let `M` be an `R`-module. Suppose `M` is a direct sum of
> countably generated `R`-modules, and suppose there is a universally injective map
> `f : M → R[[t_1, …, t_n]]` for some `n`, that is, one for which `f ⊗ id_T` is injective for every
> `R`-module `T`. Then `M` is projective. Being a direct sum of countably generated modules is
> spelled internally, as in 058W, 058Y and 05A0: an independent set of submodules of `M` with
> supremum `⊤`, each spanned by a countable set.

```lean
public theorem
    Module.projective_of_forall_rTensor_injective_mvPowerSeries_of_exists_sSupIndep_countable_span
    (R : Type u) [CommRing R] [IsNoetherianRing R] (M : Type u) [AddCommGroup M] [Module R M]
    (n : ℕ) (f : M →ₗ[R] MvPowerSeries (Fin n) R)
    (hf : ∀ (T : Type u) [AddCommGroup T] [Module R T], Function.Injective (f.rTensor T))
    (hM : ∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ K ∈ S, ∃ t : Set M, t.Countable ∧ Submodule.span R t = K) :
    Module.Projective R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.93, Tag 059V](https://stacks.math.columbia.edu/tag/059V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
