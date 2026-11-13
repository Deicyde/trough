---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isAmple_of_fieldExtension, AlgebraicGeometry.isQuasiAffine_of_fieldExtension, AlgebraicGeometry.isQuasiAffine_of_isQuasiAffine_baseChange, AlgebraicGeometry.isQuasiProjective_of_fieldExtension, AlgebraicGeometry.isProper_of_fieldExtension, AlgebraicGeometry.isProjective_of_fieldExtension
statement: formalized
proof: formalized
---

# 33.15 Change of fields and ample invertible sheaves

Section 33.15 of the Stacks Project, [Tag 0BDB](https://stacks.math.columbia.edu/tag/0BDB). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BDC, a lemma

[Tag 0BDC](https://stacks.math.columbia.edu/tag/0BDC) in the Stacks Project.

**`AlgebraicGeometry.exists_isAmple_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Unconditional.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Unconditional.lean#L91).

> Let `k` be a field and `X` a scheme over `k`. If there exists an ample invertible sheaf on
> `X_K` for some field extension `K/k`, then `X` has an ample invertible sheaf.

```lean
public theorem exists_isAmple_of_fieldExtension
    (h : ∃ L : (pullback (Spec.map (CommRingCat.ofHom (algebraMap k K))) f).Modules,
        ∃ _ : AlgebraicGeometry.SheafOfModules.IsInvertible
          (pullback (Spec.map (CommRingCat.ofHom (algebraMap k K))) f).toRingedSpace.presheaf
          (structureSheafRing
            (pullback (Spec.map (CommRingCat.ofHom (algebraMap k K))) f).toRingedSpace).property L,
          Scheme.Modules.IsAmple
            (pullback (Spec.map (CommRingCat.ofHom (algebraMap k K))) f) L) :
    ∃ M : X.Modules, ∃ _ : AlgebraicGeometry.SheafOfModules.IsInvertible
        X.toRingedSpace.presheaf (structureSheafRing X.toRingedSpace).property M,
      Scheme.Modules.IsAmple X M
```

## Tag 0BDD, a lemma

[Tag 0BDD](https://stacks.math.columbia.edu/tag/0BDD) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffine_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/QuasiAffine.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/QuasiAffine.lean#L123).

> Let `k` be a field and `X` a scheme over `k`. If `X_K` is quasi-affine for some field
> extension `K/k`, then `X` is quasi-affine.

```lean
public theorem isQuasiAffine_of_fieldExtension
    (h : Scheme.IsQuasiAffine
      (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    Scheme.IsQuasiAffine X
```

**`AlgebraicGeometry.isQuasiAffine_of_isQuasiAffine_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiAffine.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/QuasiAffine.lean#L49).

> **Stacks Project, Tag 0BDD.** Quasi-affineness descends along an extension of the base
> field: if the base change of `X` to `K` is quasi-affine, then so is `X`.

```lean
theorem isQuasiAffine_of_isQuasiAffine_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    (h : Scheme.IsQuasiAffine
      (pullback f (Spec.map (ofHom (algebraMap k K))))) :
    Scheme.IsQuasiAffine X
```

## Tag 0BDE, a lemma

[Tag 0BDE](https://stacks.math.columbia.edu/tag/0BDE) in the Stacks Project.

**`AlgebraicGeometry.isQuasiProjective_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Unconditional.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Unconditional.lean#L114). References: EGA IV (9.1.5), “quasi-projective case”; EGA II (6.6.5), “quasi-proj. descent”.

> Let `k` be a field and `X` a scheme over `k`. If `X_K` is quasi-projective over `K` for some
> field extension `K/k`, then `X` is quasi-projective over `k`.

```lean
public theorem isQuasiProjective_of_fieldExtension
    (h : IsQuasiProjective (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    IsQuasiProjective f
```

## Tag 0BDF, a lemma

[Tag 0BDF](https://stacks.math.columbia.edu/tag/0BDF) in the Stacks Project.

**`AlgebraicGeometry.isProper_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Proper.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Proper.lean#L96).

> **[Stacks Project, Tag 0BDF].** Let `k` be a field and `X` a scheme over `k`. If `X_K` is
> proper over `K` for some field extension `K/k`, then `X` is proper over `k`.
>
> The field extension is faithfully flat, so `Spec(K) → Spec(k)` is a surjective flat quasi-compact
> morphism and the statement is the descent of properness along one; that descent is
> [Stacks Project, Tag 02L1], of which the source says this lemma is a special case.

```lean
public theorem isProper_of_fieldExtension
    (h : IsProper (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    IsProper f
```

## Tag 0BDG, a lemma

[Tag 0BDG](https://stacks.math.columbia.edu/tag/0BDG) in the Stacks Project.

**`AlgebraicGeometry.isProjective_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Projective.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FieldExtensionDescent/Projective.lean#L161).

> **[Stacks Project, Tag 0BDG].** Let `k` be a field and `X` a scheme over `k`. If `X_K` is
> projective over `K` for some field extension `K/k`, then `X` is projective over `k`.
>
> This is the source proof verbatim: projectivity over a field is quasi-projectivity together with
> properness, and each of those descends along an arbitrary field extension by
> [Stacks Project, Tag 0BDE] and [Stacks Project, Tag 0BDF]. The identification of projectivity
> with the conjunction is clause (1) of [Stacks Project, Tag 0BCL], applied at the two affine bases
> `Spec K` and `Spec k`, where it is
> `AlgebraicGeometry.isProjective_iff_isQuasiProjective_and_isProper_of_isAffine`.

```lean
public theorem isProjective_of_fieldExtension
    (h : IsProjective (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))))) :
    IsProjective f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.15, Tag 0BDB](https://stacks.math.columbia.edu/tag/0BDB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
