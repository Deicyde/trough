---
declaration: section
origin: cited
lean: Stacks.EnriquesSeveriZariski.forall_le_eq_zero_sections_twist, Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_globalSectionsOverField_twist, Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_zero_twist, Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_globalSectionsOverField_twistedGradedModuleTwist, Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_zero_twistedGradedModuleTwist, Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_one_twistedGradedModuleTwist, Stacks.AmpleSectionConnected.connectedSpace_zeroScheme_of_isAmple
statement: formalized
proof: formalized
---

# 33.48 Enriques-Severi-Zariski

Section 33.48 of the Stacks Project, [Tag 0FVD](https://stacks.math.columbia.edu/tag/0FVD). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FD7, a lemma

[Tag 0FD7](https://stacks.math.columbia.edu/tag/0FD7) in the Stacks Project.

**`Stacks.EnriquesSeveriZariski.forall_le_eq_zero_sections_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean#L407). The attribute's comment: “the vanishing stated on the global sections themselves”.

> **[Stacks, Tag 0FD7], on global sections.** Let `k` be a field, let `X` be a proper scheme
> over `k`, let `ℒ` be an ample invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module. If
> `Ass(ℱ)` contains no closed points then `Γ(X, ℱ ⊗ ℒ^{⊗ n}) = 0` for all `n ≪ 0`.

```lean
theorem forall_le_eq_zero_sections_twist (k : Type u) [Field k] (f : X ⟶ Spec (.of k))
    [IsProper f] (hL : Stacks.Ample.IsAmple X L) (F : X.Modules) [F.IsCoherent]
    (hAss : ∀ x : X, IsClosed ({x} : Set X) → x ∉ Stacks.Divisors.associatedPoints F) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n ≤ n₀ → ∀ t : Γ(twist L F n, ⊤), t = 0
```

**`Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_globalSectionsOverField_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean#L432).

> **[Stacks, Tag 0FD7].** Let `k` be a field, let `X` be a proper scheme over `k`, let `ℒ` be
> an ample invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module. If `Ass(ℱ)` contains no
> closed points then
>
> `Γ(X, ℱ ⊗_{𝒪_X} ℒ^{⊗ n}) = 0`
>
> for all `n ≪ 0`, as an assertion about the `k`-vector space of global sections.

```lean
theorem exists_forall_le_isZero_globalSectionsOverField_twist (k : Type u) [Field k]
    (f : X ⟶ Spec (.of k)) [IsProper f] (hL : Stacks.Ample.IsAmple X L) (F : X.Modules)
    [F.IsCoherent]
    (hAss : ∀ x : X, IsClosed ({x} : Set X) → x ∉ Stacks.Divisors.associatedPoints F) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n ≤ n₀ → IsZero (globalSectionsOverField k f (twist L F n))
```

**`Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_zero_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean#L447). The attribute's comment: “the vanishing stated on degree-zero cohomology”.

> **[Stacks, Tag 0FD7], in degree-zero cohomology.** The same vanishing read through the
> derived functor computing `H⁰`, which is the form the twisted-cohomology consumers of 0FD7 ask
> for.

```lean
theorem exists_forall_le_isZero_cohomologyOverField_zero_twist (k : Type u) [Field k]
    (f : X ⟶ Spec (.of k)) [IsProper f] (hL : Stacks.Ample.IsAmple X L) (F : X.Modules)
    [F.IsCoherent]
    (hAss : ∀ x : X, IsClosed ({x} : Set X) → x ∉ Stacks.Divisors.associatedPoints F) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n ≤ n₀ → IsZero (cohomologyOverField k f (twist L F n) 0)
```

**`Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_globalSectionsOverField_twistedGradedModuleTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean#L477). The attribute's comment: “the vanishing at the twisted-graded-module spelling of the twist”.

> **[Stacks, Tag 0FD7] at the twisted-graded-module spelling of the twist**, which is the
> spelling the graded twisted-cohomology machinery is typed against.

```lean
theorem exists_forall_le_isZero_globalSectionsOverField_twistedGradedModuleTwist (k : Type u)
    [Field k] (f : X ⟶ Spec (.of k)) [IsProper f] (hL : Stacks.Ample.IsAmple X L)
    (F : X.Modules) [F.IsCoherent]
    (hAss : ∀ x : X, IsClosed ({x} : Set X) → x ∉ Stacks.Divisors.associatedPoints F) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n ≤ n₀ →
      IsZero (globalSectionsOverField k f
        (Stacks.Cohomology.TwistedGradedModule.twist X L F n))
```

**`Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_zero_twistedGradedModuleTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/Basic.lean#L490). The attribute's comment: “the vanishing at the twisted-graded-module spelling, in degree-zero cohomology”.

> **[Stacks, Tag 0FD7] at the twisted-graded-module spelling, in degree-zero cohomology.**

```lean
theorem exists_forall_le_isZero_cohomologyOverField_zero_twistedGradedModuleTwist (k : Type u)
    [Field k] (f : X ⟶ Spec (.of k)) [IsProper f] (hL : Stacks.Ample.IsAmple X L)
    (F : X.Modules) [F.IsCoherent]
    (hAss : ∀ x : X, IsClosed ({x} : Set X) → x ∉ Stacks.Divisors.associatedPoints F) :
    ∃ n₀ : ℤ, ∀ n : ℤ, n ≤ n₀ →
      IsZero (cohomologyOverField k f
        (Stacks.Cohomology.TwistedGradedModule.twist X L F n) 0)
```

## Tag 0FD8, a lemma

[Tag 0FD8](https://stacks.math.columbia.edu/tag/0FD8) in the Stacks Project.

**`Stacks.EnriquesSeveriZariski.exists_forall_le_isZero_cohomologyOverField_one_twistedGradedModuleTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/H1Vanishing.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EnriquesSeveriZariski/H1Vanishing.lean#L194).

> **[Stacks, Tag 0FD8].**  Let `k` be a field, let `X` be a scheme proper over `k`, let `ℒ` be
> an ample invertible `𝒪_X`-module and let `ℱ` be a coherent `𝒪_X`-module.  If the stalk of `ℱ` has
> depth at least two at every closed point of `X`, then
>
> `H¹(X, ℱ ⊗_{𝒪_X} ℒ^{⊗ m}) = 0`
>
> for all `m ≪ 0`.

```lean
theorem exists_forall_le_isZero_cohomologyOverField_one_twistedGradedModuleTwist (k : Type u)
    [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L) (F : X.Modules)
    [F.IsCoherent]
    (hdepth : ∀ x : X, IsClosed ({x} : Set X) → (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ m₀ : ℤ, ∀ m : ℤ, m ≤ m₀ →
      IsZero (AlgebraicGeometry.cohomologyOverField k f
        (Stacks.Cohomology.TwistedGradedModule.twist X L F m) 1)
```

## Tag 0FD9, a lemma

[Tag 0FD9](https://stacks.math.columbia.edu/tag/0FD9) in the Stacks Project.

**`Stacks.AmpleSectionConnected.connectedSpace_zeroScheme_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleSectionConnected/Connected.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AmpleSectionConnected/Connected.lean#L88).

> **[Stacks, Tag 0FD9].** Let `k` be a field, let `X` be a proper scheme over `k`, let `ℒ` be
> an ample invertible `𝒪_X`-module and let `s ∈ Γ(X, ℒ)`. If `s` is a regular section
> ([Stacks, Tag 01WY]), if `depth(𝒪_{X,x}) ≥ 2` for every closed point `x ∈ X`, and if `X` is
> connected, then the zero scheme `Z(s)` is connected.

```lean
theorem connectedSpace_zeroScheme_of_isAmple (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f]
    (L : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [inst : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) (s : L.sections)
    (hs : Mono (L.unitHomEquiv.symm s))
    (hdepth : ∀ x : X, IsClosed ({x} : Set X) → (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
      (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x))
    [ConnectedSpace X] :
    ConnectedSpace (zeroScheme X L (s.eval (op ⊤))).subscheme
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.48, Tag 0FVD](https://stacks.math.columbia.edu/tag/0FVD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
