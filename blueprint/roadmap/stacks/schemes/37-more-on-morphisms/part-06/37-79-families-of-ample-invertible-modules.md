---
declaration: section
origin: cited
lean: Stacks.AmpleFamilyRelativeAmple.exists_isAmpleFamily, Stacks.AmpleFamilyRelativeAmple.exists_isAmpleFamily_of_isAffineHom_or_isQuasiAffineHom
statement: formalized
proof: formalized
---

# 37.79 Families of ample invertible modules

Section 37.79 of the Stacks Project, [Tag 0GTN](https://stacks.math.columbia.edu/tag/0GTN). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GTP, a lemma

[Tag 0GTP](https://stacks.math.columbia.edu/tag/0GTP) in the Stacks Project.

**`Stacks.AmpleFamilyRelativeAmple.exists_isAmpleFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFamilyRelativeAmple/Basic.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFamilyRelativeAmple/Basic.lean#L365).

> **Stacks Tag 0GTP.** Let `f : X ⟶ Y` be a morphism of schemes. If `Y` has an ample family of
> invertible modules and there is an invertible `𝒪_X`-module ample relative to `f`, then `X` has an
> ample family of invertible modules.

```lean
theorem exists_isAmpleFamily {X Y : Scheme.{u}} (f : X ⟶ Y) {I : Type v} (N : I → Y.Modules)
    (hN : Y.IsAmpleFamily N)
    (hL : ∃ (L : X.Modules) (_ : IsInvertibleModule X L),
      Stacks.RelativeAmple.IsRelativelyAmple f L) :
    ∃ (J : Type v) (M : J → X.Modules), X.IsAmpleFamily M
```

## Tag 0GTQ, a lemma

[Tag 0GTQ](https://stacks.math.columbia.edu/tag/0GTQ) in the Stacks Project.

**`Stacks.AmpleFamilyRelativeAmple.exists_isAmpleFamily_of_isAffineHom_or_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFamilyRelativeAmple/QuasiAffine.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFamilyRelativeAmple/QuasiAffine.lean#L61).

> **Stacks 0GTQ.** Let `f : X ⟶ Y` be an affine or quasi-affine morphism of schemes. If `Y` has
> an ample family of invertible modules, then so does `X`.

```lean
theorem exists_isAmpleFamily_of_isAffineHom_or_isQuasiAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsAffineHom f ∨ IsQuasiAffineHom f) {I : Type v} (N : I → Y.Modules)
    (hN : Y.IsAmpleFamily N) :
    ∃ (J : Type v) (M : J → X.Modules), X.IsAmpleFamily M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.79, Tag 0GTN](https://stacks.math.columbia.edu/tag/0GTN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
