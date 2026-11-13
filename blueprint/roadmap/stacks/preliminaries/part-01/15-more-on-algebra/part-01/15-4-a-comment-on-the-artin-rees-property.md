---
declaration: section
origin: cited
lean: artinRees_stability, associatedGraded_coker_equiv_of_congr, artinRees_baseChange
statement: formalized
proof: formalized
---

# 15.4 A comment on the Artin-Rees property

Section 15.4 of the Stacks Project, [Tag 07VD](https://stacks.math.columbia.edu/tag/07VD). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07VE, a lemma

[Tag 07VE](https://stacks.math.columbia.edu/tag/07VE) in the Stacks Project.

**`artinRees_stability`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ArtinRees/Constant.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ArtinRees/Constant.lean#L233).

> **Stacks 07VE**.
> Let `A` be Noetherian and `I ⊆ rad(A)`. Let `L --f--> M --g--> N` and `L --f'--> M --g'--> N` be
> two complexes of `A`-modules with `M` finite, and `c ≥ 0` such that `c` works for `f` and `g` in
> the Artin-Rees lemma, the first complex is exact, `f' ≡ f (mod I^{c+1})` and
> `g' ≡ g (mod I^{c+1})`. Then `c` works for `g'` in the Artin-Rees lemma and the second complex
> is exact.

```lean
theorem artinRees_stability {A : Type*} [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (hI : I ≤ (⊥ : Ideal A).jacobson) {L M N : Type*} [AddCommGroup L] [AddCommGroup M]
    [AddCommGroup N] [Module A L] [Module A M] [Module A N] [Module.Finite A M]
    (f f' : L →ₗ[A] M) (g g' : M →ₗ[A] N) (c : ℕ) (hS'c : g'.comp f' = 0)
    (hf : IsArtinReesConstant I f c) (hg : IsArtinReesConstant I g c)
    (hexact : LinearMap.ker g = LinearMap.range f)
    (hff' : CongruentModPow I f f' (c + 1)) (hgg' : CongruentModPow I g g' (c + 1)) :
    IsArtinReesConstant I g' c ∧ LinearMap.ker g' = LinearMap.range f'
```

## Tag 07VF, a lemma

[Tag 07VF](https://stacks.math.columbia.edu/tag/07VF) in the Stacks Project.

**`associatedGraded_coker_equiv_of_congr`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ArtinRees/AssociatedGraded.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ArtinRees/AssociatedGraded.lean#L233).

> **Stacks 07VF.** With the hypotheses of `artinRees_stability`, the cokernels of the two
> nearby maps `g` and `g'` have isomorphic associated graded modules over the associated graded
> ring of `I`.

```lean
public noncomputable def associatedGraded_coker_equiv_of_congr
    {A : Type u} [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (hI : I ≤ (⊥ : Ideal A).jacobson)
    {L : Type v} {M : Type w} {N : Type x}
    [AddCommGroup L] [AddCommGroup M] [AddCommGroup N]
    [Module A L] [Module A M] [Module A N]
    [Module.Finite A L] [Module.Finite A M] [Module.Finite A N]
    (f : L →ₗ[A] M) (g : M →ₗ[A] N) (f' : L →ₗ[A] M) (g' : M →ₗ[A] N)
    (c : ℕ)
    (hS'c : g'.comp f' = 0)
    (hf : IsArtinReesConstant I f c) (hg : IsArtinReesConstant I g c)
    (hexact : LinearMap.ker g = LinearMap.range f)
    (hff' : CongruentModPow I f f' (c + 1)) (hgg' : CongruentModPow I g g' (c + 1)) :
    AssociatedGraded.GradedLinearEquiv I
      (N ⧸ LinearMap.range g) (N ⧸ LinearMap.range g')
```

## Tag 07VG, a lemma

[Tag 07VG](https://stacks.math.columbia.edu/tag/07VG) in the Stacks Project.

**`artinRees_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ArtinRees/Constant.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ArtinRees/Constant.lean#L283).

> **Stacks 07VG**.
> Let `A → B` be a flat ring homomorphism, `I ⊆ A` an ideal, and `f : M → N` a map of `A`-modules.
> If `c` works for `f` in the Artin-Rees lemma with respect to `I`, then `c` works for the base
> change `B ⊗[A] M → B ⊗[A] N` with respect to the ideal `IB`.

```lean
theorem artinRees_baseChange {A : Type*} (B : Type*) [CommRing A] [CommRing B]
    [Algebra A B] [Module.Flat A B] (I : Ideal A) {M N : Type*} [AddCommGroup M]
    [AddCommGroup N] [Module A M] [Module A N] (f : M →ₗ[A] N) (c : ℕ)
    (hf : IsArtinReesConstant I f c) :
    IsArtinReesConstant (Ideal.map (algebraMap A B) I) (LinearMap.baseChange B f) c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.4, Tag 07VD](https://stacks.math.columbia.edu/tag/07VD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
