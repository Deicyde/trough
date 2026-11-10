---
declaration: section
origin: cited
lean: Deformation.Artin.exists_nonEffectiveSystem_quotientStack_trivialAction
statement: formalized
proof: formalized
---

# 110.75 An algebraic stack not satisfying strong formal effectiveness

Section 110.75 of the Stacks Project, [Tag 0CXW](https://stacks.math.columbia.edu/tag/0CXW). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CXX, a lemma

[Tag 0CXX](https://stacks.math.columbia.edu/tag/0CXX) in the Stacks Project.

**`Deformation.Artin.exists_nonEffectiveSystem_quotientStack_trivialAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystem.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/NonEffectiveSystem.lean#L335). The attribute's comment: “RESTRICTED: Tag 0AFB (lifting an object along a thickening) is the hypothesis h0AFB, Tags 0AF9 and 0AFA (finite order of the class over the limit) are h0AF9, the non-torsion rational point of the abelian variety with Tag 0AEN is ξ₀ with hnontorsion, and the class of a torsor is the data H, cls, hcls; the site realization is U, cU, e, eL, he, heL, hchart”.

> **Stacks Project, Tag 0CXX.** Let `k` be an algebraically closed field which is not the
> algebraic closure of a finite field, let `A` be an abelian variety over `k` and let
> `𝒳 = [Spec(k)/A]`. There is an inverse system of `k`-algebras whose transition maps are
> surjective with locally nilpotent kernels — the thickenings of the triangle of three affine
> lines — and a system of objects of `𝒳` over the spectra of its levels, which is not effective
> in the sense of Tag 0CXT.
>
> The mathematical inputs the library does not have are hypotheses: `h0AFB` is the lifting of an
> object along a nilpotent thickening of the triangle, the method of Tag 0AFB; `h0AF9` is the
> finiteness of the order of the class of every object over the limit, Tag 0AF9 together with
> Tag 0AFA; `ξ₀` together with `hnontorsion` is the object over the reduced triangle whose class
> has infinite order, which the source builds from a non-torsion rational point of `A` and
> Tag 0AEN; `H`, `cls` and `hcls` are the first cohomology class of an object of `𝒳`, that is,
> the description of the fibre categories of a classifying stack as groupoids of torsors; and
> `U`, `cU`, `e`, `eL`, `he`, `heL`, `hchart` realize the spectra of the levels of the inverse
> system and of its limit as objects of the chosen big fppf site. Non-effectivity is nowhere
> assumed, and the system of objects is constructed rather than supposed.

```lean
public theorem exists_nonEffectiveSystem_quotientStack_trivialAction
    [IsAlgClosed k]
    (_hkinf : ∀ F : Subfield k, Finite F → ¬ Algebra.IsAlgebraic F k)
    (U : ℕ ⥤ fppfOverField k C hk) (cU : Cocone U)
    (cR : Cone (triangleThickenings k)) (hcR : IsLimit cR)
    (e : ∀ n : ℕ, (schemeOverField k C hk).obj (U.obj n) ≅
      Spec (.of ((triangleThickenings k).obj (.op n))))
    (eL : (schemeOverField k C hk).obj cU.pt ≅ Spec (.of cR.pt))
    (he : ∀ {i j : ℕ} (g : i ⟶ j), (schemeOverField k C hk).map (U.map g) ≫ (e j).hom =
      (e i).hom ≫ Scheme.Spec.map
        (CommRingCat.ofHom ((triangleThickenings k).map g.op).hom.toRingHom).op)
    (heL : ∀ n : ℕ, (schemeOverField k C hk).map (cU.ι.app n) ≫ eL.hom =
      (e n).hom ≫ Scheme.Spec.map
        (CommRingCat.ofHom (cR.π.app (.op n)).hom.toRingHom).op)
    (hchart : eL.inv ≫ C.inclusion.map cU.pt.hom =
      Scheme.Spec.map (CommRingCat.ofHom (algebraMap k cR.pt)).op)
    (H : (fppfOverField k C hk)ᵒᵖ ⥤ AddCommGrpCat.{u})
    (cls : (x : (Stack.quotientStack Q.groupoid).obj) →
      H.obj (.op ((Stack.quotientStack Q.groupoid).p.obj x)))
    (hcls : ∀ {x y : (Stack.quotientStack Q.groupoid).obj} (φ : x ⟶ y),
      cls x = H.map ((Stack.quotientStack Q.groupoid).p.map φ).op (cls y))
    (ξ₀ : (Stack.quotientStack Q.groupoid).obj)
    (hξ₀ : (Stack.quotientStack Q.groupoid).p.obj ξ₀ ≅ U.obj 0)
    (hnontorsion : ¬ IsOfFinAddOrder (cls ξ₀))
    (h0AF9 : ∀ x : (Stack.quotientStack Q.groupoid).obj,
      (Stack.quotientStack Q.groupoid).p.obj x = cU.pt → IsOfFinAddOrder (cls x))
    (h0AFB : ∀ (n : ℕ) (x : (Stack.quotientStack Q.groupoid).obj)
      (a : (Stack.quotientStack Q.groupoid).p.obj x ≅ U.obj n),
      ∃ (y : (Stack.quotientStack Q.groupoid).obj)
        (b : (Stack.quotientStack Q.groupoid).p.obj y ≅ U.obj (n + 1))
        (φ : x ⟶ y), (Stack.quotientStack Q.groupoid).p.map φ ≫ b.hom =
          a.hom ≫ U.map (homOfLE (Nat.le_succ n))) :
    ∃ (R : ℕᵒᵖ ⥤ CommAlgCat.{u} k) (cS : Cone R)
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
        (f n).hom ≫ Scheme.Spec.map (CommRingCat.ofHom (cS.π.app (.op n)).hom.toRingHom).op) ∧
      (fL.inv ≫ C.inclusion.map c.pt.hom =
        Scheme.Spec.map (CommRingCat.ofHom (algebraMap k cS.pt)).op) ∧
      ¬ IsEffectiveSystem (Stack.quotientStack Q.groupoid).p ξ c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.75, Tag 0CXW](https://stacks.math.columbia.edu/tag/0CXW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
