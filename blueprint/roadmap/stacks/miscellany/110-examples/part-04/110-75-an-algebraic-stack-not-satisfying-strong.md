---
declaration: section
origin: cited
lean: Deformation.Artin.exists_nonEffectiveSystem_quotientStack_abelianVariety, Deformation.Artin.not_forall_exists_nonEffectiveSystem_quotientStack_zero
statement: formalized
proof: formalized
---

# 110.75 An algebraic stack not satisfying strong formal effectiveness

Section 110.75 of the Stacks Project, [Tag 0CXW](https://stacks.math.columbia.edu/tag/0CXW). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CXX, a lemma

[Tag 0CXX](https://stacks.math.columbia.edu/tag/0CXX) in the Stacks Project.

**`Deformation.Artin.exists_nonEffectiveSystem_quotientStack_abelianVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystemAbelian.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystemAbelian.lean#L349). The attribute's comment: “with the condition 1 ≤ dim A, which the source omits: as printed the lemma fails for the zero abelian variety (errata.md, 2026-10-28). The system is the source's construction over the function field k(A), glued along the generic point of A.”.

> **Stacks Project, Tag 0CXX.** Let `k` be an algebraically closed field which is not the
> algebraic closure of a finite field, let `A` be an abelian variety over `k` with `1 ≤ dim A`, and
> let `𝒳 = [Spec(k)/A]` over the big fppf site of `Spec k`. There are an inverse system `R` of
> `k`-algebras with a limit cone `cS`, whose transition maps are surjective with locally nilpotent
> kernels, and a system `ξ` of objects of `𝒳` lying over the spectra of the levels of `R` (through
> the isomorphisms `f`, compatible with the transition maps), together with the cocone `c` of the
> base it maps to, whose vertex is the spectrum of the limit (through `fL`, compatible with the legs
> and with the structure morphism to `Spec k`), such that `ξ` is not effective over `c` in the sense
> of Tag 0CXT.
>
> The condition `1 ≤ dim A` is not in the source, whose statement fails for the zero abelian
> variety (`errata.md`, entry of 2026-10-28). The system is the one of the discussion before the
> lemma, over the function field `K = k(A)`: `R_n = K[x, y] ⧸ (xy(x + y - 1)) ^ (n + 1)` and `ξ_n`
> glued along the generic point of `A`. The hypothesis on `k` is not used; it is the source's.

```lean
theorem exists_nonEffectiveSystem_quotientStack_abelianVariety [IsAlgClosed k]
    (_hkinf : ∀ F : Subfield k, Finite F → ¬ Algebra.IsAlgebraic F k)
    (hdim : 1 ≤ Stacks.Groupoids.abelianVarietyDimension A) :
    ∃ (R : ℕᵒᵖ ⥤ CommAlgCat.{u} k) (cS : Cone R)
      (ξ : ℕ ⥤ (abelianVarietyClassifyingStack 𝒞 hk A).obj)
      (c : Cocone (ξ ⋙ (abelianVarietyClassifyingStack 𝒞 hk A).p))
      (f : ∀ n : ℕ, (schemeOverField k 𝒞 hk).obj
        ((ξ ⋙ (abelianVarietyClassifyingStack 𝒞 hk A).p).obj n) ≅ Spec (.of (R.obj (.op n))))
      (fL : (schemeOverField k 𝒞 hk).obj c.pt ≅ Spec (.of cS.pt)),
      Nonempty (IsLimit cS) ∧
      (∀ {i j : ℕᵒᵖ} (g : i ⟶ j), Function.Surjective (R.map g).hom) ∧
      (∀ {i j : ℕᵒᵖ} (g : i ⟶ j),
        (RingHom.ker (R.map g).hom.toRingHom).LocallyNilpotent) ∧
      (∀ {i j : ℕ} (g : i ⟶ j), (schemeOverField k 𝒞 hk).map
          ((ξ ⋙ (abelianVarietyClassifyingStack 𝒞 hk A).p).map g) ≫ (f j).hom =
        (f i).hom ≫ Scheme.Spec.map (CommRingCat.ofHom (R.map g.op).hom.toRingHom).op) ∧
      (∀ n : ℕ, (schemeOverField k 𝒞 hk).map (c.ι.app n) ≫ fL.hom =
        (f n).hom ≫ Scheme.Spec.map (CommRingCat.ofHom (cS.π.app (.op n)).hom.toRingHom).op) ∧
      (fL.inv ≫ 𝒞.inclusion.map c.pt.hom =
        Scheme.Spec.map (CommRingCat.ofHom (algebraMap k cS.pt)).op) ∧
      ¬ IsEffectiveSystem (abelianVarietyClassifyingStack 𝒞 hk A).p ξ c
```

**`Deformation.Artin.not_forall_exists_nonEffectiveSystem_quotientStack_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystemZero.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystemZero.lean#L162). The attribute's comment: “as printed it is false: the zero abelian variety A = Spec k (an abelian variety by Tag 03RO) gives [Spec(k)/A] = Spec k, over which every system of objects is effective; refuted for k the algebraic closure of Q. The corrected statement needs 1 ≤ dim A”.

> **Tag 0CXX is false as printed.** The source's statement is: for `k` an algebraically closed
> field which is not the algebraic closure of a finite field, `A` an abelian variety over `k` and
> `𝒳 = [Spec(k)/A]`, there are an inverse system of `k`-algebras `Rₙ` with surjective transition
> maps whose kernels are locally nilpotent and a system `(ξₙ)` of objects of `𝒳` over
> `(Spec(Rₙ))` which is not effective in the sense of Tag 0CXT. It fails for the zero abelian
> variety `A = Spec k`, which is an abelian variety by Tag 03RO
> (`AlgebraicGeometry.isAbelianVariety_tensorUnit`): its group algebraic space is the trivial group
> `𝟙_` over `Spec k`, the quotient `[Spec(k)/0]` is the base itself, and every system of objects of
> it is effective (`Deformation.Artin.isEffectiveSystem_quotientStack_zero`).
>
> The statement refuted is the source's, read at `A = 0`, for every field `k` meeting the source's
> hypotheses, every big fppf site containing `Spec k`, and every presentation of the action
> groupoid of the trivial action; the counterexample is `k` the algebraic closure of `ℚ`, a site
> supplied by `AlgebraicGeometry.BigFppfSite.exists_contains`, and the action groupoid of
> `AlgebraicGeometry.Space.actionGroupoidConstruction`. The corrected statement assumes `1 ≤ dim A`
> and is `Deformation.Artin.exists_nonEffectiveSystem_quotientStack_abelianVariety`.

```lean
public theorem not_forall_exists_nonEffectiveSystem_quotientStack_zero :
    ¬ ∀ (k : Type) [Field k] [IsAlgClosed k],
      (∀ F : Subfield k, Finite F → ¬ Algebra.IsAlgebraic F k) →
      ∀ (C : BigFppfSite.{0}) (hk : C.Contains (Spec (CommRingCat.of k)))
        (Q : Space.ActionGroupoidConstruction (fieldAsAlgebraicSpace k C hk)
          (𝟙_ (Over (fieldAsAlgebraicSpace k C hk).obj))
          (𝟙_ (Over (fieldAsAlgebraicSpace k C hk).obj))
          (fieldAsAlgebraicSpace k C hk).property (fieldAsAlgebraicSpace k C hk).property),
      ∃ (R : ℕᵒᵖ ⥤ CommAlgCat.{0} k) (cS : Cone R)
        (ξ : ℕ ⥤ (Stack.quotientStack Q.groupoid).obj)
        (c : Cocone (ξ ⋙ (Stack.quotientStack Q.groupoid).p))
        (f : ∀ n : ℕ, (schemeOverField k C hk).obj
          ((ξ ⋙ (Stack.quotientStack Q.groupoid).p).obj n) ≅ Spec (.of (R.obj (.op n))))
        (fL : (schemeOverField k C hk).obj c.pt ≅ Spec (.of cS.pt)),
        Nonempty (IsLimit cS) ∧
        (∀ {i j : ℕᵒᵖ} (g : i ⟶ j), Function.Surjective (R.map g).hom) ∧
        (∀ {i j : ℕᵒᵖ} (g : i ⟶ j),
          (RingHom.ker (R.map g).hom.toRingHom).LocallyNilpotent) ∧
        (∀ {i j : ℕ} (g : i ⟶ j), (schemeOverField k C hk).map
            ((ξ ⋙ (Stack.quotientStack Q.groupoid).p).map g) ≫ (f j).hom =
          (f i).hom ≫ Scheme.Spec.map (CommRingCat.ofHom (R.map g.op).hom.toRingHom).op) ∧
        (∀ n : ℕ, (schemeOverField k C hk).map (c.ι.app n) ≫ fL.hom =
          (f n).hom ≫
            Scheme.Spec.map (CommRingCat.ofHom (cS.π.app (.op n)).hom.toRingHom).op) ∧
        (fL.inv ≫ C.inclusion.map c.pt.hom =
          Scheme.Spec.map (CommRingCat.ofHom (algebraMap k cS.pt)).op) ∧
        ¬ IsEffectiveSystem (Stack.quotientStack Q.groupoid).p ξ c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.75, Tag 0CXW](https://stacks.math.columbia.edu/tag/0CXW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
