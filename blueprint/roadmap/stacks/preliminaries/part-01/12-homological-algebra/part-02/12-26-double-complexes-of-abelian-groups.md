---
declaration: section
origin: cited
lean: quasiIso_of_isRightResolution, quasiIso_of_goodResolution, HomologicalComplex₂.quasiIso_toProductTotal, quasiIso_productTotalAug
statement: formalized
proof: formalized
---

# 12.26 Double complexes of abelian groups

Section 12.26 of the Stacks Project, [Tag 0E1P](https://stacks.math.columbia.edu/tag/0E1P). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E1Q, a lemma

[Tag 0E1Q](https://stacks.math.columbia.edu/tag/0E1Q) in the Stacks Project.

**`quasiIso_of_isRightResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Grp/TotalComplex.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/Grp/TotalComplex.lean#L550).

> Let `M^•` be a cochain complex of abelian groups and let
> `0 → M^• → A_0^• → A_1^• → …` be an exact complex of complexes of abelian
> groups (encoded as a half-plane double complex with augmentation `f`). Then
> the induced map `g : M^• → Tot(A^{•,•})` is a quasi-isomorphism.

```lean
theorem quasiIso_of_isRightResolution
    (M : CochainComplex AddCommGrpCat ℤ)
    (A : HomologicalComplex₂ AddCommGrpCat 𝕀 𝕀) [A.HasTotal 𝕀]
    (f : M ⟶ A.X 0)
    (hA_vanish : ∀ p : ℤ, p < 0 → IsZero (A.X p))
    (hExact : IsRightResolution M A f)
    (g : M ⟶ A.total 𝕀) (hg : InducedFromColumnZero f g) :
    QuasiIso g
```

## Tag 09IZ, a lemma

[Tag 09IZ](https://stacks.math.columbia.edu/tag/09IZ) in the Stacks Project.

**`quasiIso_of_goodResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Grp/TotalComplex.lean, line 940](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/Grp/TotalComplex.lean#L940).

> A good resolution `A → M` yields a chain map `A.total shZ ⟶ M` whose
> per-degree components agree with `canonicalMapF`, and this chain map is a
> quasi-isomorphism.

```lean
theorem quasiIso_of_goodResolution
    (M : HomologicalComplex Ab shZ)
    (A : HomologicalComplex₂ Ab shZ shZ)
    [A.HasTotal shZ]
    (f : A.X 0 ⟶ M)
    (_h : GoodResolution M A f) :
    ∃ φ : A.total shZ ⟶ M,
      (∀ n : ℤ, φ.f n = canonicalMapF M A f n) ∧ QuasiIso φ
```

## Tag 09J0, a lemma

[Tag 09J0](https://stacks.math.columbia.edu/tag/09J0) in the Stacks Project.

**`HomologicalComplex₂.quasiIso_toProductTotal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/AbelianGroupComplexResolutions.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/AbelianGroupComplexResolutions.lean#L631).

> Let `0 → M^• → A_0^• → A_1^• → ⋯` be an exact complex of complexes of abelian groups such
> that for every `p` the induced complex `0 → Coker(d_M^p) → Coker(d_{A_0}^p) → ⋯` is exact. Then
> the map `M^• → Tot_π(A^{•, •})` induced by `M^• → A_0^•` is a quasi-isomorphism. Here `K` is the
> double complex `A^{p, q} = A_p^q`, `ε` is the map `M^• → A_0^•`, the exact complex of complexes
> is the augmentation of `K` by `ε`, and `Coker(d^p)` is the object of opcycles in degree `p + 1`.

```lean
theorem quasiIso_toProductTotal (ε : M ⟶ K.X 0) (w : ε ≫ K.d 0 1 = 0)
    (hA : (CochainComplex.augment K ε w).Acyclic)
    (hC : ∀ q : ℤ, (((HomologicalComplex.opcyclesFunctor AddCommGrpCat.{u} (ComplexShape.up ℤ)
      q).mapHomologicalComplex (ComplexShape.up ℕ)).obj (CochainComplex.augment K ε w)).Acyclic) :
    QuasiIso (toProductTotal ε w)
```

## Tag 0E1R, a lemma

[Tag 0E1R](https://stacks.math.columbia.edu/tag/0E1R) in the Stacks Project.

**`quasiIso_productTotalAug`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Grp/TotalComplex.lean, line 1289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/Grp/TotalComplex.lean#L1289).

> The natural map from the product total complex of an exact left resolution
> by complexes to `M` is a quasi-isomorphism.

```lean
alias quasiIso_productTotalAug
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.26, Tag 0E1P](https://stacks.math.columbia.edu/tag/0E1P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
