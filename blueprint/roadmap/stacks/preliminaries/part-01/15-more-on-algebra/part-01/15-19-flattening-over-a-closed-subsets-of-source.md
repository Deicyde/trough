---
declaration: section
origin: cited
lean: Module.FlatteningSituation, Module.IsFlatAtPrimesOver, Module.IsFlatAtPrimesOver.baseChange, Module.IsFlatAtPrimesOver.of_baseChange, Module.exists_isFlatAtPrimesOver_of_isColimit, Module.flat_localizedModule_atPrime_of_flat_quotient_pow
statement: formalized
proof: formalized
---

# 15.19 Flattening over a closed subsets of source and base

Section 15.19 of the Stacks Project, [Tag 05LN](https://stacks.math.columbia.edu/tag/05LN). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05LP, a situation

[Tag 05LP](https://stacks.math.columbia.edu/tag/05LP) in the Stacks Project.

**`Module.FlatteningSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L71).

> **Stacks Tag 05LP.** The fixed data for flattening over closed subsets of source and base:
> a ring map `R → S`, an ideal `J ⊆ S`, and an `S`-module `M`.

```lean
structure Module.FlatteningSituation
```

## Tag 05LQ, an equation

[Tag 05LQ](https://stacks.math.columbia.edu/tag/05LQ) in the Stacks Project.

**`Module.IsFlatAtPrimesOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L96).

> **Stacks Tag 05LQ.** Condition (15.19.1): the base change of `M` along `R → R'` is flat over
> `R'` at every prime of `S ⊗[R] R'` containing the extensions of both `I'` and `J`. The module
> denoted `M ⊗_R R'` in the source is represented by the canonically equivalent extension of
> scalars `(S ⊗[R] R') ⊗[S] M`.

```lean
def Module.IsFlatAtPrimesOver {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    [Algebra R S] (J : Ideal S) {M : Type w} [AddCommGroup M] [Module R M]
    [Module S M] [IsScalarTower R S M] (R' : Type x) [CommRing R'] [Algebra R R']
    (I' : Ideal R') : Prop
```

## Tag 05LR, a lemma

[Tag 05LR](https://stacks.math.columbia.edu/tag/05LR) in the Stacks Project.

**`Module.IsFlatAtPrimesOver.baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L182).

> **Stacks Tag 05LR.** Flatness at all primes over the extensions of `I'` and `J` is preserved
> by a further base change `R' → R''` and by replacing the extension of `I'` with a larger
> ideal `I''`.

```lean
lemma Module.IsFlatAtPrimesOver.baseChange
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    (J : Ideal S) {M : Type w} [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M]
    (R' : Type x) [CommRing R'] [Algebra R R']
    (R'' : Type y) [CommRing R''] [Algebra R R''] [Algebra R' R'']
    [IsScalarTower R R' R'']
    (I' : Ideal R') (I'' : Ideal R'')
    (hI : Ideal.map (algebraMap R' R'') I' ≤ I'')
    (hflat : Module.IsFlatAtPrimesOver (R := R) (S := S) J (M := M) R' I') :
    Module.IsFlatAtPrimesOver (R := R) (S := S) J (M := M) R'' I''
```

## Tag 05LS, a lemma

[Tag 05LS](https://stacks.math.columbia.edu/tag/05LS) in the Stacks Project.

**`Module.IsFlatAtPrimesOver.of_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L411).

> **Stacks Tag 05LS.** Flatness along the closed subsets determined by `I'` and `J` descends
> from `R''` to `R'` when `V(I'') → V(I')` is surjective and the localizations of `R''` at primes
> containing `I''` are flat over `R'`.

```lean
lemma Module.IsFlatAtPrimesOver.of_baseChange
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    (J : Ideal S) {M : Type w} [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M]
    {R' : Type x} {R'' : Type y} [CommRing R'] [CommRing R'']
    [Algebra R R'] [Algebra R R''] [Algebra R' R''] [IsScalarTower R R' R'']
    (I' : Ideal R') (I'' : Ideal R'')
    (_hI : Ideal.map (algebraMap R' R'') I' ≤ I'')
    (hsurj : ∀ (p' : Ideal R'), p'.IsPrime → I' ≤ p' →
      ∃ p'' : Ideal R'', p''.IsPrime ∧ I'' ≤ p'' ∧
        Ideal.comap (algebraMap R' R'') p'' = p')
    (hflat : ∀ (p'' : Ideal R'') [p''.IsPrime], I'' ≤ p'' →
      Module.Flat R' (Localization p''.primeCompl))
    (h : Module.IsFlatAtPrimesOver (R := R) (M := M) J R'' I'') :
    Module.IsFlatAtPrimesOver (R := R) (M := M) J R' I'
```

## Tag 05LT, a lemma

[Tag 05LT](https://stacks.math.columbia.edu/tag/05LT) in the Stacks Project.

**`Module.exists_isFlatAtPrimesOver_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 1047](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L1047).

> **Stacks Tag 05LT.** Let `R → S` be essentially of finite presentation, let `J ⊆ S` be an
> ideal and let `M` be a finitely presented `S`-module. Let `F` be a filtered system of
> `R`-algebras whose colimit cocone `c` is preserved by the forgetful functor to types, and let
> `I lambda ⊆ F.obj lambda` be a compatible family of ideals. If the flatness condition
> `Module.IsFlatAtPrimesOver` holds over the colimit `c.pt` and the supremum of the images of the
> `I lambda`, then it already holds at some stage `lambda`.
>
> Preservation of the colimit by the forgetful functor expresses the source's directed colimit of
> rings elementwise: every element and every finite equation in `c.pt` comes from a stage. It is
> required explicitly because the index universes and the ring universe are independent.

```lean
theorem Module.exists_isFlatAtPrimesOver_of_isColimit
    {R : Type u} {S : Type v} {M : Type w} [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FinitePresentation S M] (J : Ideal S)
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation)
    {Lambda : Type y} [Category.{z} Lambda] [IsFiltered Lambda]
    (F : Lambda ⥤ CommAlgCat.{x} R) [PreservesColimit F (forget (CommAlgCat.{x} R))]
    (c : Cocone F) (hc : IsColimit c)
    (I : (lambda : Lambda) → Ideal (F.obj lambda))
    (hI : ∀ {lambda mu : Lambda} (f : lambda ⟶ mu),
      Ideal.map (F.map f).hom.toRingHom (I lambda) ≤ I mu)
    (hflat : Module.IsFlatAtPrimesOver (R := R) (S := S) (M := M) J (c.pt : Type x)
      (⨆ lambda, Ideal.map (c.ι.app lambda).hom.toRingHom (I lambda))) :
    ∃ lambda, Module.IsFlatAtPrimesOver (R := R) (S := S) (M := M) J
      (F.obj lambda) (I lambda)
```

## Tag 05LU, a lemma

[Tag 05LU](https://stacks.math.columbia.edu/tag/05LU) in the Stacks Project.

**`Module.flat_localizedModule_atPrime_of_flat_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Stratification.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Stratification.lean#L562).

> **Stacks Tag 05LU.** Let `R → S` be a map of Noetherian rings, let `J ⊆ S` and `I ⊆ R` be
> ideals, and let `M` be a finite `S`-module. If, at every prime `q` containing `J + IS`, the
> localization `(M / IⁿM)_q` is flat over `R / Iⁿ` for every `n ≥ 1`, then `M_q` is flat over `R`
> at every such prime.

```lean
theorem Module.flat_localizedModule_atPrime_of_flat_quotient_pow
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S]
    {M : Type w} [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Finite S M] (J : Ideal S) (I : Ideal R)
    (hflat : ∀ (n : ℕ) (q : Ideal S) (_ : q.IsPrime),
      J + I.map (algebraMap R S) ≤ q →
        let K := (I ^ (n + 1)).map (algebraMap R S) • (⊤ : Submodule S M)
        let Q := M ⧸ K
        let hQ : Module.IsTorsionBySet R Q ((I ^ (n + 1) : Ideal R) : Set R) := by
          intro z r
          induction z using Quotient.inductionOn' with
          | _ m =>
            change (Submodule.Quotient.mk ((r : R) • m) : M ⧸ K) = 0
            exact (Submodule.Quotient.mk_eq_zero K).mpr
              (show (r : R) • m ∈ K by
                rw [← IsScalarTower.algebraMap_smul S (r : R) m]
                exact Submodule.smul_mem_smul
                  (Ideal.mem_map_of_mem (algebraMap R S) r.2) Submodule.mem_top)
        let N := LocalizedModule q.primeCompl Q
        let hN : Module.IsTorsionBySet R N ((I ^ (n + 1) : Ideal R) : Set R) := by
          intro z r
          obtain ⟨⟨z, s⟩, rfl⟩ := IsLocalizedModule.mk'_surjective q.primeCompl
            (LocalizedModule.mkLinearMap q.primeCompl Q) z
          change (r : R) • IsLocalizedModule.mk'
            (LocalizedModule.mkLinearMap q.primeCompl Q) z s = 0
          rw [← IsLocalizedModule.mk'_smul, hQ]
          exact IsLocalizedModule.mk'_zero _ _
        letI := hN.module
        Module.Flat (R ⧸ I ^ (n + 1)) N) :
    ∀ (q : Ideal S) (_ : q.IsPrime), J + I.map (algebraMap R S) ≤ q →
      Module.Flat R (LocalizedModule q.primeCompl M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.19, Tag 05LN](https://stacks.math.columbia.edu/tag/05LN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
