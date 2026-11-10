---
declaration: section
origin: cited
lean: Deformation.CompleteLocalAlgCat.formallyHomotopic_refl, Deformation.CompleteLocalAlgCat.formallyHomotopic_symm, Deformation.CompleteLocalAlgCat.formallyHomotopic_trans, Deformation.CompleteLocalAlgCat.formallyHomotopic_equivalence, Deformation.formallyHomotopic_comp, Deformation.formallyHomotopic_of_isVersal, Deformation.Ideal.map_eq_of_formallyHomotopic_of_mem_minimalPrimes
statement: formalized
proof: formalized
---

# 90.28 Uniqueness of versal rings

Section 90.28 of the Stacks Project, [Tag 0DQA](https://stacks.math.columbia.edu/tag/0DQA). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DQB, a lemma

[Tag 0DQB](https://stacks.math.columbia.edu/tag/0DQB) in the Stacks Project.

**`Deformation.CompleteLocalAlgCat.formallyHomotopic_refl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L765). The attribute's comment: “reflexivity”.

> **Stacks Project, Tag 0DQB.** Every morphism of complete local `Λ`-algebras is formally
> homotopic to itself: take the homotopy in no variables.

```lean
theorem formallyHomotopic_refl (f : R ⟶ S) : FormallyHomotopic f f
```

**`Deformation.CompleteLocalAlgCat.formallyHomotopic_symm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L802). The attribute's comment: “symmetry”.

> **Stacks Project, Tag 0DQB.** Formal homotopy is symmetric: substituting the homotopy into
> itself gives an automorphism of the power series ring exchanging the two specializations.

```lean
theorem formallyHomotopic_symm {f g : R ⟶ S}
    (h : FormallyHomotopic f g) : FormallyHomotopic g f
```

**`Deformation.CompleteLocalAlgCat.formallyHomotopic_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 864](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L864). The attribute's comment: “transitivity”.

> **Stacks Project, Tag 0DQB.** Formal homotopy is transitive: concatenating the variables
> of two homotopies and substituting the first into the second gives a homotopy between the
> outer two morphisms.

```lean
theorem formallyHomotopic_trans {f g h : R ⟶ S}
    (hfg : FormallyHomotopic f g) (hgh : FormallyHomotopic g h) :
    FormallyHomotopic f h
```

**`Deformation.CompleteLocalAlgCat.formallyHomotopic_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 1062](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L1062).

> **Stacks Project, Tag 0DQB.** Formal homotopy is an equivalence relation on each set of
> morphisms of `\widehat{\mathcal C}_Λ`.

```lean
theorem formallyHomotopic_equivalence :
    Equivalence (α := R ⟶ S) FormallyHomotopic
```

## Tag 0DQC, a lemma

[Tag 0DQC](https://stacks.math.columbia.edu/tag/0DQC) in the Stacks Project.

**`Deformation.formallyHomotopic_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L358).

> Postcomposing two formally homotopic maps with the same morphism preserves their
> formal homotopy.

```lean
theorem formallyHomotopic_comp
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {R S S' : CompleteLocalAlgCat.{u, v, w} Λ k}
    {f₁ f₂ : R ⟶ S} (hf : FormallyHomotopic f₁ f₂) (g : S ⟶ S') :
    FormallyHomotopic (f₁ ≫ g) (f₂ ≫ g)
```

## Tag 0DQD, a lemma

[Tag 0DQD](https://stacks.math.columbia.edu/tag/0DQD) in the Stacks Project.

**`Deformation.formallyHomotopic_of_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing/Uniqueness.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing/Uniqueness.lean#L694).

> **Stacks Project, Tag 0DQD.**  Let `ℱ` be a deformation category over `𝒞_Λ` whose tangent
> space and infinitesimal automorphisms are finite-dimensional over `k`.  Let `ξ` be a versal
> formal object lying over `R`, and let `η` be a formal object lying over `S`.  Then any two maps
> `f, g : R → S` with `f_*ξ ≅ η ≅ g_*ξ` are formally homotopic.

```lean
theorem formallyHomotopic_of_isVersal
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v v₃ w, w} Λ k)
    (hp : IsDeformationCategory.{u, max v v₃, w} p)
    (_hT : FiniteDimensional k
      ↥(tangentModuleAt.{u, max v v₃, w} (BasedCategory.ofFunctor p) hp
        (FGModuleCat.of k (ULift.{max v v₃} k))))
    (hInf : ∀ (x : F) (P : ChosenPushforwardsAt p x),
      p.obj x = residueFieldObject.{u, max v v₃, w} Λ k →
      FiniteDimensional k
        ↥((infinitesimalAutomorphismLinearLift.{u, max v v₃, w} P hp.satisfiesRS).functor.obj
          (FGModuleCat.of k (ULift.{max v v₃} k))))
    (ξ η : FormalObject p) (hξ : IsVersal hp.predeformation.cofibered ξ)
    (f g : ξ.base ⟶ η.base)
    (hf : ∃ a : ξ ⟶ η, a.base = f) (hg : ∃ a : ξ ⟶ η, a.base = g) :
    CompleteLocalAlgCat.FormallyHomotopic f g
```

## Tag 0DQE, a lemma

[Tag 0DQE](https://stacks.math.columbia.edu/tag/0DQE) in the Stacks Project.

**`Deformation.Ideal.map_eq_of_formallyHomotopic_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalRing.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalRing.lean#L327).

> Formally homotopic morphisms of Noetherian complete local algebras extend a minimal
> prime of the source to the same ideal of the target.

```lean
theorem map_eq_of_formallyHomotopic_of_mem_minimalPrimes
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f₁ f₂ : R ⟶ S)
    (hf : FormallyHomotopic f₁ f₂) (p : Ideal R) (hp : p ∈ minimalPrimes R) :
    p.map f₁.hom.toRingHom = p.map f₂.hom.toRingHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.28, Tag 0DQA](https://stacks.math.columbia.edu/tag/0DQA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
