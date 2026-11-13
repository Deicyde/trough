---
declaration: section
origin: cited
lean: Stacks.Picard.continuousSMul_galoisPicardAction, Stacks.Picard.injective_schemePullbackClass_of_globalSectionsIso, Stacks.Picard.bijOn_schemePullbackClass_galoisFixedClasses, Stacks.Picard.bijOn_schemePullbackClass_zsmulTorsion_of_isPurelyInseparable
statement: formalized
proof: formalized
---

# 44.7 Some remarks on Picard groups

Section 44.7 of the Stacks Project, [Tag 0CDS](https://stacks.math.columbia.edu/tag/0CDS). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CDT, a lemma

[Tag 0CDT](https://stacks.math.columbia.edu/tag/0CDT) in the Stacks Project.

**`Stacks.Picard.continuousSMul_galoisPicardAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/FiniteStageContinuity.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/FiniteStageContinuity.lean#L276). The attribute's comment: “continuity of the action of `Gal(k'/k)` on `Pic(X_{k'})`, proved from Tag 0B8W (2) through `exists_finiteSubextension_schemePullbackClass_eq`”.

> **The continuity clause of Stacks Tag 0CDT.** Let `k` be a field, let `X` be a quasi-compact,
> quasi-separated scheme over `k`, and let `K/k` be a Galois extension. The action of `Gal(K/k)`
> on `Pic(X_K)` by pullback along the twists `id_X × Spec(σ)` is continuous for the Krull topology
> on the Galois group and the discrete topology on the Picard group: every class descends to a
> finite subextension `E` (Tag 0B8W (2)), hence is fixed by the open subgroup `Gal(K/E)`.

```lean
theorem continuousSMul_galoisPicardAction (X : Over (Spec (.of k)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    [TopologicalSpace (ofScheme (SchemeOver.baseChange k K X))]
    [DiscreteTopology (ofScheme (SchemeOver.baseChange k K X))] :
    letI := galoisPicardAction k K X
    ContinuousSMul (K ≃ₐ[k] K) (ofScheme (SchemeOver.baseChange k K X))
```

**`Stacks.Picard.injective_schemePullbackClass_of_globalSectionsIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/Injectivity.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/Injectivity.lean#L68). The attribute's comment: “injectivity of `Pic(X) → Pic(X_{k'})`, proved from Tag 0CC5; the full identification is `bijOn_schemePullbackClass_galoisFixedClasses`”.

> **The injectivity half of Stacks Tag 0CDT.** Let `X` be a quasi-compact, quasi-separated
> scheme over a field `k` with `H⁰(X, 𝒪_X) = k`, and let `k'/k` be a field extension. Then the
> pullback map `Pic(X) → Pic(X_{k'})` is injective: `H⁰(X, 𝒪_X)` is then a field, hence
> semi-local, and Tag 0CC5 applies.

```lean
theorem injective_schemePullbackClass_of_globalSectionsIso {k k' : Type u} [Field k] [Field k']
    (φ : k →+* k') {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [CompactSpace X] [QuasiSeparatedSpace X]
    (hf : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)) :
    Function.Injective (schemePullbackClass (pullback.fst f (Spec.map (CommRingCat.ofHom φ))))
```

**`Stacks.Picard.bijOn_schemePullbackClass_galoisFixedClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/PicardGaloisInvariants.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/GaloisDescent/PicardGaloisInvariants.lean#L180). The attribute's comment: “the identification `Pic(X) = Pic(X_{k'})^{Gal(k'/k)}`. The continuity clause of the tag is `Stacks.Picard.continuousSMul_galoisPicardAction`”.

> **Stacks Project, Tag 0CDT.** Let `k` be a field, let `X` be a quasi-compact,
> quasi-separated scheme over `k` with `H⁰(X, 𝒪_X) = k` admitting a `k`-rational point, and let
> `k'/k` be a Galois extension. Then pullback along `X_{k'} ⟶ X` is a bijection of `Pic(X)` onto
> the classes of `Pic(X_{k'})` fixed by `Gal(k'/k)`.

```lean
theorem bijOn_schemePullbackClass_galoisFixedClasses (k k' : Type u) [Field k] [Field k']
    [Algebra k k'] [IsGalois k k'] (X : Over (Spec (.of k)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    (hΓ : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ X.hom.appTop))
    (pt : Spec (.of k) ⟶ X.left) (hpt : pt ≫ X.hom = 𝟙 (Spec (.of k))) :
    Set.BijOn (schemePullbackClass (pullback.fst X.hom
        (Spec.map (CommRingCat.ofHom (algebraMap k k'))))) Set.univ
      (galoisFixedClasses k k' X)
```

## Tag 0CD5, a lemma

[Tag 0CD5](https://stacks.math.columbia.edu/tag/0CD5) in the Stacks Project.

**`Stacks.Picard.bijOn_schemePullbackClass_zsmulTorsion_of_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/TorsionBaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/TorsionBaseChange.lean#L125).

> **Stacks Project, Tag 0CD5.** Let `k` be a field of characteristic `p > 0`, let `X` be a
> quasi-compact and quasi-separated scheme over `k` with `H⁰(X, 𝒪_X) = k`, and let `n` be an
> integer prime to `p`. Then for every purely inseparable extension `k'/k`, pullback along
> `X_{k'} ⟶ X` is a bijection `Pic(X)[n] → Pic(X_{k'})[n]`.
>
> Injectivity is Tag 0CC5. For surjectivity, a class of `Pic(X_{k'})[n]` is pulled back from a
> class of `Pic(X_E)` for a finite subextension `E/k` (Tag 0B8W), which is again `n`-torsion
> because pullback from `X_E` is injective (Tag 0CC5 at the stage), and the finite purely
> inseparable case is
> `Stacks.Picard.bijOn_schemePullbackClass_zsmulTorsion_of_hasExponent`, proved through the
> absolute Frobenius.

```lean
theorem bijOn_schemePullbackClass_zsmulTorsion_of_isPurelyInseparable
    {k k' : Type u} [Field k] [Field k'] [Algebra k k'] [IsPurelyInseparable k k']
    (p : ℕ) [CharP k p] (hp : 0 < p) {n : ℤ} (hn : n.natAbs.Coprime p)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [CompactSpace X] [QuasiSeparatedSpace X]
    (hΓ : IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)) :
    Set.BijOn
      (schemePullbackClass (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k k')))))
      (zsmulTorsion (ofScheme X) n)
      (zsmulTorsion
        (ofScheme (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k k'))))) n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.7, Tag 0CDS](https://stacks.math.columbia.edu/tag/0CDS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
