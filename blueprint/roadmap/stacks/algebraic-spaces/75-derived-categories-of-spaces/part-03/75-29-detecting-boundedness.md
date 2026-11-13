---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.eventually_subsingleton_hom_iff_truncGE_of_isPerfect, AlgebraicGeometry.Space.eventually_subsingleton_hom_iff_truncLE_of_isPerfect, AlgebraicGeometry.Space.tfae_isLE_of_isPerfect_generator, AlgebraicGeometry.Space.tfae_isGE_of_isPerfect_generator
statement: formalized
proof: formalized
---

# 75.29 Detecting Boundedness

Section 75.29 of the Stacks Project, [Tag 0GFE](https://stacks.math.columbia.edu/tag/0GFE). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GFF, a lemma

[Tag 0GFF](https://stacks.math.columbia.edu/tag/0GFF) in the Stacks Project.

**`AlgebraicGeometry.Space.eventually_subsingleton_hom_iff_truncGE_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DetectingBoundednessTruncGE.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DetectingBoundednessTruncGE.lean#L162).

> **[Stacks, Tag 0GFF].**  Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`, let `P` be a perfect object of `D(𝒪_X)`, let `E` be an object of
> `D_QCoh(𝒪_X)` and let `a` be an integer.  Then
>
> 1. `Hom_{D(𝒪_X)}(P⟦-i⟧, E) = 0` for `i ≫ 0`
>
> if and only if
>
> 2. `Hom_{D(𝒪_X)}(P⟦-i⟧, τ_{≥a}E) = 0` for `i ≫ 0`,
>
> where `τ_{≥a}` is the canonical truncation of `D(𝒪_X)` and vanishing of a Hom-group is
> subsingletonness of the morphism type, the derived category being additive.
>
> Both implications are the truncation triangle
> `τ_{≤a-1}E ⟶ E ⟶ τ_{≥a}E ⟶ (τ_{≤a-1}E)⟦1⟧`: a morphism `P⟦-i⟧ ⟶ E` which dies in `τ_{≥a}E`
> factors through `τ_{≤a-1}E`, and a morphism `P⟦-i⟧ ⟶ τ_{≥a}E` which dies in `(τ_{≤a-1}E)⟦1⟧`
> factors through `E`.  So each direction needs only that `τ_{≤a-1}E` and `(τ_{≤a-1}E)⟦1⟧` receive
> no nonzero morphism from `P⟦-i⟧` for `i` large; both lie in `D_QCoh(𝒪_X)` and are bounded above,
> by `a - 1` and `a - 2`, and
> `AlgebraicGeometry.Space.exists_threshold_subsingleton_hom_negShift_of_isPerfect` kills both from
> `i ≥ a - 1 + c` on, with `c` the threshold that perfectness of `P` supplies through
> [Stacks, Tag 09MB].

```lean
theorem eventually_subsingleton_hom_iff_truncGE_of_isPerfect
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    [HasDerivedCategory.{w} (Modules.{u, u} B S hS X hX)]
    (P E : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hP : (smallEtaleRingedSite B S hS X hX).IsPerfect P)
    (hE : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) j).obj
      E).IsQuasicoherentOnSite)
    (a : ℤ) :
    (∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (P⟦-i⟧ ⟶ E)) ↔
      ∃ N : ℤ, ∀ i : ℤ, N ≤ i →
        Subsingleton (P⟦-i⟧ ⟶ (DerivedCategory.TStructure.t.truncGE a).obj E)
```

## Tag 0GFG, a lemma

[Tag 0GFG](https://stacks.math.columbia.edu/tag/0GFG) in the Stacks Project.

**`AlgebraicGeometry.Space.eventually_subsingleton_hom_iff_truncLE_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DetectingBoundednessTruncLE.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DetectingBoundednessTruncLE.lean#L111).

> **[Stacks, Tag 0GFG].** Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`, let `P` be a perfect object of `D(𝒪_X)`, let `E` be an object of
> `D_QCoh(𝒪_X)` and let `a` be an integer. Then
>
> 1. `Hom_{D(𝒪_X)}(P⟦-i⟧, E) = 0` for `i ≪ 0`, and
> 2. `Hom_{D(𝒪_X)}(P⟦-i⟧, τ_{≤a}E) = 0` for `i ≪ 0`
>
> are equivalent.
>
> A perfect object on a quasi-compact algebraic space is bounded above
> (`AlgebraicGeometry.Space.exists_isLE_of_isPerfect`), and for a `P` bounded above the equivalence
> is t-structure orthogonality against the truncation triangle
> `τ_{≤a}E ⟶ E ⟶ τ_{≥a+1}E ⟶`, which is
> `Stacks.DerivedTruncation.eventually_subsingleton_hom_iff_truncLE`. Quasi-separatedness of `X` and
> quasi-coherence of the cohomology sheaves of `E` are hypotheses of the source that this argument
> does not read.

```lean
theorem eventually_subsingleton_hom_iff_truncLE_of_isPerfect
    (hqc : IsQuasiCompactSpace B S hS X)
    (_hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (P : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hP : (smallEtaleRingedSite B S hS X hX).IsPerfect P)
    (E : DerivedCategory (Modules.{u, u} B S hS X hX))
    (_hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj
      E).IsQuasicoherentOnSite)
    (a : ℤ) :
    (∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (P⟦-i⟧ ⟶ E)) ↔
      ∃ N : ℤ, ∀ i : ℤ, i ≤ N →
        Subsingleton (P⟦-i⟧ ⟶ (DerivedCategory.TStructure.t.truncLE a).obj E)
```

## Tag 0GFH, a proposition

[Tag 0GFH](https://stacks.math.columbia.edu/tag/0GFH) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_isLE_of_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BoundedAboveCriterion.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BoundedAboveCriterion.lean#L115).

> **Stacks 0GFH.** Let `X` be a quasi-compact and quasi-separated algebraic space, `G` a perfect
> object of `D(𝒪_X)` which generates `D_QCoh(𝒪_X)`, and `E` an object of `D_QCoh(𝒪_X)`. The
> following are equivalent:
> 1. `E ∈ D⁻_QCoh(𝒪_X)`;
> 2. `Hom(G[-i], E) = 0` for `i ≫ 0`;
> 3. `Ext^i_X(G, E) = 0` for `i ≫ 0`;
> 4. `RHom_X(G, E)` is bounded above;
> 5. `H^i(X, G^∨ ⊗^L E) = 0` for `i ≫ 0`;
> 6. `RΓ(X, G^∨ ⊗^L E)` is bounded above;
> 7. for every perfect `P`: (2), (3), (4) hold with `P` in place of `G`, `H^i(X, P ⊗^L E) = 0` for
>    `i ≫ 0`, and `RΓ(X, P ⊗^L E)` is bounded above.

```lean
theorem tfae_isLE_of_isPerfect_generator (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (G : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hG : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect G)
    (hgen : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      (∀ n : ℤ, Subsingleton (G⟦n⟧ ⟶ E.obj)) → IsZero E.obj)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    List.TFAE [
      ∃ a : ℤ, E.obj.IsLE a,
      ∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (G⟦-i⟧ ⟶ E.obj),
      ∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (G ⟶ E.obj⟦i⟧),
      ∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
        (((smallEtaleDerivedSheafHom B S hS X).obj (op G)).obj E.obj)).IsLE a,
      ∃ N : ℤ, ∀ i : ℤ, N ≤ i → IsZero ((DerivedCategory.homologyFunctor
        (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2)) i).obj
          ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
            (((smallEtaleDerivedTensor B S hS X).obj
              (smallEtaleDerivedDual B S hS X G)).obj E.obj))),
      ∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
          (((smallEtaleDerivedTensor B S hS X).obj
            (smallEtaleDerivedDual B S hS X G)).obj E.obj)).IsLE a,
      ∀ P : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
        (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P →
          (∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (P⟦-i⟧ ⟶ E.obj)) ∧
          (∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (P ⟶ E.obj⟦i⟧)) ∧
          (∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
            (((smallEtaleDerivedSheafHom B S hS X).obj (op P)).obj E.obj)).IsLE a) ∧
          (∃ N : ℤ, ∀ i : ℤ, N ≤ i → IsZero ((DerivedCategory.homologyFunctor
            (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2)) i).obj
              ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
                (((smallEtaleDerivedTensor B S hS X).obj P).obj E.obj)))) ∧
          (∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
              (((smallEtaleDerivedTensor B S hS X).obj P).obj E.obj)).IsLE a)]
```

## Tag 0GFI, a proposition

[Tag 0GFI](https://stacks.math.columbia.edu/tag/0GFI) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_isGE_of_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BoundedBelowCriterion.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BoundedBelowCriterion.lean#L133).

> **Stacks 0GFI.** Let `X` be a quasi-compact and quasi-separated algebraic space, `G` a perfect
> object of `D(𝒪_X)` which generates `D_QCoh(𝒪_X)`, and `E` an object of `D_QCoh(𝒪_X)`. The
> following are equivalent:
> 1. `E ∈ D⁺_QCoh(𝒪_X)`;
> 2. `Hom(G[-i], E) = 0` for `i ≪ 0`;
> 3. `Ext^i_X(G, E) = 0` for `i ≪ 0`;
> 4. `RHom_X(G, E)` is bounded below;
> 5. `H^i(X, G^∨ ⊗^L E) = 0` for `i ≪ 0`;
> 6. `RΓ(X, G^∨ ⊗^L E)` is bounded below;
> 7. for every perfect `P`: (2), (3), (4) hold with `P` in place of `G`, `H^i(X, P ⊗^L E) = 0` for
>    `i ≪ 0`, and `RΓ(X, P ⊗^L E)` is bounded below.

```lean
theorem tfae_isGE_of_isPerfect_generator (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (G : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hG : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect G)
    (hgen : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      (∀ n : ℤ, Subsingleton (G⟦n⟧ ⟶ E.obj)) → IsZero E.obj)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    List.TFAE [
      ∃ a : ℤ, E.obj.IsGE a,
      ∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (G⟦-i⟧ ⟶ E.obj),
      ∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (G ⟶ E.obj⟦i⟧),
      ∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
        (((smallEtaleDerivedSheafHom B S hS X).obj (op G)).obj E.obj)).IsGE a,
      ∃ N : ℤ, ∀ i : ℤ, i ≤ N → IsZero ((DerivedCategory.homologyFunctor
        (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2)) i).obj
          ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
            (((smallEtaleDerivedTensor B S hS X).obj
              (smallEtaleDerivedDual B S hS X G)).obj E.obj))),
      ∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
          (((smallEtaleDerivedTensor B S hS X).obj
            (smallEtaleDerivedDual B S hS X G)).obj E.obj)).IsGE a,
      ∀ P : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
        (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P →
          (∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (P⟦-i⟧ ⟶ E.obj)) ∧
          (∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (P ⟶ E.obj⟦i⟧)) ∧
          (∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
            (((smallEtaleDerivedSheafHom B S hS X).obj (op P)).obj E.obj)).IsGE a) ∧
          (∃ N : ℤ, ∀ i : ℤ, i ≤ N → IsZero ((DerivedCategory.homologyFunctor
            (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2)) i).obj
              ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
                (((smallEtaleDerivedTensor B S hS X).obj P).obj E.obj)))) ∧
          (∃ a : ℤ, ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).obj
              (((smallEtaleDerivedTensor B S hS X).obj P).obj E.obj)).IsGE a)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.29, Tag 0GFE](https://stacks.math.columbia.edu/tag/0GFE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
