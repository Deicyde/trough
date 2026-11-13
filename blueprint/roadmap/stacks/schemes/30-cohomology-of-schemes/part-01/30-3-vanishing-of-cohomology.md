---
declaration: section
origin: cited
lean: Stacks.SerreCriterion.isAffine_of_forall_isZero_H1_ideal, Stacks.SerreCriterion.isAffine_of_forall_isZero_H1_finiteType_ideal, AlgebraicGeometry.Scheme.Modules.isAmple_of_forall_isZero_h1_quasicoherentIdeal, Stacks.ProjectionFormula.isAmple_of_hasEventuallyVanishingH1, Stacks.AffineFromVanishing.isAffineHom_of_forall_isZero_rightDerived_ideal
statement: formalized
proof: formalized
---

# 30.3 Vanishing of cohomology

Section 30.3 of the Stacks Project, [Tag 01XE](https://stacks.math.columbia.edu/tag/01XE). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01XF, a lemma

[Tag 01XF](https://stacks.math.columbia.edu/tag/01XF) in the Stacks Project.

**`Stacks.SerreCriterion.isAffine_of_forall_isZero_H1_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SerreAffinenessCriterion/VanishingCriterion.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SerreAffinenessCriterion/VanishingCriterion.lean#L59). References: EGA II (5.2.1), “(d')⇒(a)”; EGA IV (1.7.17), “(d') => affine”; EGA III (1.4.7), “(ii), special case”.

> **Serre's criterion for affineness.** A quasi-compact scheme on which the first cohomology
> of every quasi-coherent sheaf of ideals vanishes is affine.

```lean
theorem isAffine_of_forall_isZero_H1_ideal (X : Scheme.{u}) [CompactSpace X]
    (hH₁ : ∀ I : Subobject (SheafOfModules.unit X.ringCatSheaf),
      (Subobject.underlying.obj I).IsQuasicoherent →
        IsZero (((SheafOfModules.evaluation X.ringCatSheaf (op ⊤)).rightDerived 1).obj
          (Subobject.underlying.obj I))) :
    IsAffine X
```

## Tag 01XG, a lemma

[Tag 01XG](https://stacks.math.columbia.edu/tag/01XG) in the Stacks Project.

**`Stacks.SerreCriterion.isAffine_of_forall_isZero_H1_finiteType_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SerreAffinenessCriterion/FiniteTypeIdeals.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SerreAffinenessCriterion/FiniteTypeIdeals.lean#L92). References: EGA II (5.2.1), “(d')⇒(a), quasi-sep”; EGA III (1.4.7), “(ii), special case”.

> **Serre's criterion for affineness, finite type form.** Vanishing of the first cohomology on
> the finite type quasi-coherent sheaves of ideals suffices for affineness of a quasi-compact,
> quasi-separated scheme.

```lean
theorem isAffine_of_forall_isZero_H1_finiteType_ideal (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X]
    (hH₁ : ∀ I : Subobject (SheafOfModules.unit X.ringCatSheaf),
      (Subobject.underlying.obj I).IsQuasicoherent →
        (Subobject.underlying.obj I).IsFiniteType →
          IsZero (((SheafOfModules.evaluation X.ringCatSheaf (op ⊤)).rightDerived 1).obj
            (Subobject.underlying.obj I))) :
    IsAffine X
```

## Tag 0B5P, a lemma

[Tag 0B5P](https://stacks.math.columbia.edu/tag/0B5P) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isAmple_of_forall_isZero_h1_quasicoherentIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/QuasicoherentIdeal.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/QuasicoherentIdeal.lean#L204). References: EGA III (2.6.1), “c) => a), absolute”.

> **[Stacks, Tag 0B5P].** Let `X` be a quasi-compact scheme and `𝓛` an invertible
> `𝒪_X`-module. If every quasi-coherent submodule `𝒥 ⊆ 𝒪_X` admits an `n ≥ 1` with
> `H¹(X, 𝒥 ⊗ 𝓛^{⊗ n}) = 0`, then `𝓛` is ample.
>
> The hypothesis is clause (2) of the tag: a quasi-coherent sheaf of ideals is a quasi-coherent
> `𝒪_X`-module with a monomorphism into `𝒪_X`. It is specialised at the ideal sheaf of a closed
> immersion, which is such a submodule — quasi-coherent by
> `Stacks.Conormal.isQuasicoherent_idealSheaf` and included in `𝒪_X` by `kernel.ι` — and the
> criterion `isAmple_of_forall_exists_isZero_h1_idealSheaf` then concludes.

```lean
public theorem isAmple_of_forall_isZero_h1_quasicoherentIdeal {X : Scheme.{u}} [CompactSpace X]
    (L : X.Modules)
    [hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (hvan : ∀ (J : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
      (ι : J ⟶ SheafOfModules.unit (structureSheafRing X.toRingedSpace)), Mono ι →
      J.IsQuasicoherent → ∃ n : ℕ, 1 ≤ n ∧
        IsZero (((moduleGlobalSections X).rightDerived 1).obj
          ((((Stacks.SheafOfModules.Tensor.sheafTensor
              ⟨((X.toRingedSpace)).presheaf, ((X.toRingedSpace)).IsSheaf⟩).obj (J)).obj
            ((tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (n : ℤ))))))) :
    IsAmple X L
```

**`Stacks.ProjectionFormula.isAmple_of_hasEventuallyVanishingH1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectionFormulaInvertible/AmpleCriterion.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectionFormulaInvertible/AmpleCriterion.lean#L90). References: EGA III (2.6.1), “c) => a), absolute”.

> Let `X` be a quasi-compact scheme and `L` an invertible `𝒪_X`-module. If for every
> quasi-coherent sheaf of ideals `I ⊆ 𝒪_X` there is an `n ≥ 1` with `H¹(X, I ⊗ L^{⊗ n}) = 0`, then
> `L` is ample.
>
> Here `CompactSpace X` is "`X` is quasi-compact", `Stacks.Ample.IsInvertibleModule X L` is "`L` is
> an invertible `𝒪_X`-module", and `Stacks.AmpleCohomologicalCriterion.HasEventuallyVanishingH1 X L`
> is the vanishing hypothesis.

```lean
theorem isAmple_of_hasEventuallyVanishingH1 (X : Scheme.{u}) [CompactSpace X] (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (h : Stacks.AmpleCohomologicalCriterion.HasEventuallyVanishingH1 X L) :
    Stacks.Ample.IsAmple X L
```

## Tag 0F83, a lemma

[Tag 0F83](https://stacks.math.columbia.edu/tag/0F83) in the Stacks Project.

**`Stacks.AffineFromVanishing.isAffineHom_of_forall_isZero_rightDerived_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/AffineFromVanishing.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/AffineFromVanishing.lean#L165). References: EGA II (5.2.2), “c ⇒ a, c' ⇒ a”.

> **Stacks Project, Tag 0F83.** A quasi-compact morphism between quasi-separated schemes is
> affine as soon as the first higher direct image of every quasi-coherent sheaf of ideals on the
> source vanishes.

```lean
theorem isAffineHom_of_forall_isZero_rightDerived_ideal
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f]
    [QuasiSeparatedSpace X] [QuasiSeparatedSpace Y]
    (hR₁ : ∀ I : Subobject (SheafOfModules.unit X.ringCatSheaf),
      (Subobject.underlying.obj I).IsQuasicoherent →
        IsZero (((Scheme.Modules.pushforward f).rightDerived 1).obj
          (Subobject.underlying.obj I))) :
    IsAffineHom f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.3, Tag 01XE](https://stacks.math.columbia.edu/tag/01XE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
