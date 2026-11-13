---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsQuasiExcellentScheme, AlgebraicGeometry.IsExcellentScheme, AlgebraicGeometry.isQuasiExcellentScheme_iff_exists_isGScheme_isJ2, AlgebraicGeometry.IsQuasiExcellentScheme.isNagataScheme, AlgebraicGeometry.isExcellentScheme_iff_exists_isQuasiExcellentScheme_isUniversallyCatenary, AlgebraicGeometry.IsQuasiExcellentScheme.restrict, AlgebraicGeometry.isQuasiExcellentScheme_tfae, AlgebraicGeometry.IsExcellentScheme.restrict
statement: formalized
proof: formalized
---

# 29.20 Excellent schemes

Section 29.20 of the Stacks Project, [Tag 0HA6](https://stacks.math.columbia.edu/tag/0HA6). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HA7, a definition

[Tag 0HA7](https://stacks.math.columbia.edu/tag/0HA7) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiExcellentScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L63). The attribute's comment: “quasi-excellent”.

> A scheme is **quasi-excellent** if every point has an affine open neighbourhood whose ring of
> sections is quasi-excellent.

```lean
def IsQuasiExcellentScheme (X : Scheme.{u}) : Prop
```

**`AlgebraicGeometry.IsExcellentScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L69). The attribute's comment: “excellent”.

> A scheme is **excellent** if every point has an affine open neighbourhood whose ring of
> sections is excellent.

```lean
def IsExcellentScheme (X : Scheme.{u}) : Prop
```

## Tag 0HA8, a lemma

[Tag 0HA8](https://stacks.math.columbia.edu/tag/0HA8) in the Stacks Project.

**`AlgebraicGeometry.isQuasiExcellentScheme_iff_exists_isGScheme_isJ2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L126).

> A scheme is quasi-excellent if and only if it is a G-scheme and J-2. Here the J-2 condition
> refers to the local Noetherianity which the G-scheme condition provides.

```lean
theorem isQuasiExcellentScheme_iff_exists_isGScheme_isJ2 :
    IsQuasiExcellentScheme X ↔
      ∃ h : IsGScheme X, letI := h.isLocallyNoetherian; Scheme.IsJ2 X
```

## Tag 0HA9, a lemma

[Tag 0HA9](https://stacks.math.columbia.edu/tag/0HA9) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiExcellentScheme.isNagataScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L138).

> A quasi-excellent scheme is Nagata.

```lean
theorem IsQuasiExcellentScheme.isNagataScheme (h : IsQuasiExcellentScheme X) :
    IsNagataScheme X
```

## Tag 0HAA, a lemma

[Tag 0HAA](https://stacks.math.columbia.edu/tag/0HAA) in the Stacks Project.

**`AlgebraicGeometry.isExcellentScheme_iff_exists_isQuasiExcellentScheme_isUniversallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L162).

> A scheme is excellent if and only if it is quasi-excellent and universally catenary. Here
> universal catenarity refers to the local Noetherianity which quasi-excellence provides.

```lean
theorem isExcellentScheme_iff_exists_isQuasiExcellentScheme_isUniversallyCatenary :
    IsExcellentScheme X ↔
      ∃ h : IsQuasiExcellentScheme X,
        letI := h.isLocallyNoetherian; Scheme.IsUniversallyCatenary X
```

## Tag 0HAB, a lemma

[Tag 0HAB](https://stacks.math.columbia.edu/tag/0HAB) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiExcellentScheme.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L178). The attribute's comment: “open subschemes, quasi-excellent case”.

> Every open subscheme of a quasi-excellent scheme is quasi-excellent.

```lean
theorem IsQuasiExcellentScheme.restrict (h : IsQuasiExcellentScheme X) (U : X.Opens) :
    IsQuasiExcellentScheme U.toScheme
```

**`AlgebraicGeometry.isQuasiExcellentScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L188). The attribute's comment: “equivalent conditions, quasi-excellent case”.

> A scheme is quasi-excellent if and only if the ring of sections on every affine open is
> quasi-excellent, if and only if it is quasi-excellent on the members of one affine open covering,
> if and only if the scheme has an open covering by quasi-excellent open subschemes.

```lean
theorem isQuasiExcellentScheme_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsQuasiExcellentScheme X,
      ∀ U : X.affineOpens, IsQuasiExcellent Γ(X, U),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsQuasiExcellent Γ(X, U i),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsQuasiExcellentScheme (U i).toScheme]
```

**`AlgebraicGeometry.IsExcellentScheme.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L216). The attribute's comment: “open subschemes, excellent case”.

> Every open subscheme of an excellent scheme is excellent.

```lean
theorem IsExcellentScheme.restrict (h : IsExcellentScheme X) (U : X.Opens) :
    IsExcellentScheme U.toScheme
```

**`AlgebraicGeometry.isExcellentScheme_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExcellentCriteria.lean#L226). The attribute's comment: “equivalent conditions, excellent case”.

> A scheme is excellent if and only if the ring of sections on every affine open is excellent,
> if and only if it is excellent on the members of one affine open covering, if and only if the
> scheme has an open covering by excellent open subschemes.

```lean
theorem isExcellentScheme_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsExcellentScheme X,
      ∀ U : X.affineOpens, IsExcellent Γ(X, U),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).val) = ⊤ ∧ ∀ i, IsExcellent Γ(X, U i),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧ ∀ i, IsExcellentScheme (U i).toScheme]
```

## Tag 0HAC, a lemma

[Tag 0HAC](https://stacks.math.columbia.edu/tag/0HAC) in the Stacks Project.

**`AlgebraicGeometry.isQuasiExcellentScheme_and_isExcellentScheme_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L94).

> **Stacks 0HAC.** A scheme locally of finite type over a quasi-excellent scheme is
> quasi-excellent, and a scheme locally of finite type over an excellent scheme is excellent.

```lean
theorem isQuasiExcellentScheme_and_isExcellentScheme_of_locallyOfFiniteType {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] :
    (IsQuasiExcellentScheme S → IsQuasiExcellentScheme X) ∧
      (IsExcellentScheme S → IsExcellentScheme X)
```

## Tag 0HAD, a lemma

[Tag 0HAD](https://stacks.math.columbia.edu/tag/0HAD) in the Stacks Project.

**`AlgebraicGeometry.isExcellentScheme_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L127). The attribute's comment: “clause (1): over a field”.

> **Stacks 0HAD, clause (1).** A scheme locally of finite type over a field is excellent.

```lean
theorem isExcellentScheme_of_locallyOfFiniteType_over_field (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    IsExcellentScheme X
```

**`AlgebraicGeometry.isExcellentScheme_of_locallyOfFiniteType_over_completeLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L136). The attribute's comment: “clause (2): over a Noetherian complete local ring”.

> **Stacks 0HAD, clause (2).** A scheme locally of finite type over a Noetherian complete local
> ring is excellent.

```lean
theorem isExcellentScheme_of_locallyOfFiniteType_over_completeLocalRing (R : Type u)
    [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] :
    IsExcellentScheme X
```

**`AlgebraicGeometry.isExcellentScheme_of_locallyOfFiniteType_over_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L155). The attribute's comment: “clause (3): over the integers”.

> **Stacks 0HAD, clause (3).** A scheme locally of finite type over the integers is excellent.
> The base is `Spec (ULift ℤ)`, the terminal scheme of the ambient universe, so this is the
> statement for a scheme in an arbitrary universe.

```lean
theorem isExcellentScheme_of_locallyOfFiniteType_over_int {X : Scheme.{u}}
    (f : X ⟶ Spec (.of (ULift.{u} ℤ))) [LocallyOfFiniteType f] :
    IsExcellentScheme X
```

**`AlgebraicGeometry.isExcellentScheme_of_locallyOfFiniteType_over_dedekindDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Excellent.lean#L163). The attribute's comment: “clause (4): over a Dedekind ring of characteristic zero”.

> **Stacks 0HAD, clause (4).** A scheme locally of finite type over a Dedekind ring of
> characteristic zero is excellent.

```lean
theorem isExcellentScheme_of_locallyOfFiniteType_over_dedekindDomain (R : Type u) [CommRing R]
    [IsDedekindDomain R] [CharZero R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFiniteType f] :
    IsExcellentScheme X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.20, Tag 0HA6](https://stacks.math.columbia.edu/tag/0HA6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
