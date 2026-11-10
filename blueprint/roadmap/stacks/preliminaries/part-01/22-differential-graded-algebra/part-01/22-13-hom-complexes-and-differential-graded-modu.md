---
declaration: section
origin: cited
lean: CochainComplex.endomorphismDGA, DifferentialGradedAlgebra.leftActionEquivHom, DifferentialGraded.rightTensorHomEquiv, DifferentialGraded.rightTensorHomEquiv_apply, DifferentialGraded.exists_rightTensorHomEquiv, DifferentialGradedModule.existsUnique_isSignedAction, DifferentialGradedModule.exists_rightModule_isSignedAction, DifferentialGraded.leftTensorHomEquiv
statement: formalized
proof: formalized
---

# 22.13 Hom complexes and differential graded modules

Section 22.13 of the Stacks Project, [Tag 0FQ2](https://stacks.math.columbia.edu/tag/0FQ2). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FQ3, a lemma

[Tag 0FQ3](https://stacks.math.columbia.edu/tag/0FQ3) in the Stacks Project.

**`CochainComplex.endomorphismDGA`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Basic.lean#L55). The attribute's comment: “endomorphism algebra”.

> The endomorphism differential graded algebra of a cochain complex of `R`-modules, with its
> canonical identification of homogeneous pieces with cochains.

```lean
noncomputable def endomorphismDGA (M : CochainComplex (ModuleCat.{u} R) ℤ) :
    EndomorphismDGA M
```

**`DifferentialGradedAlgebra.leftActionEquivHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/Basic.lean#L87). The attribute's comment: “left module structures and algebra homomorphisms”.

> Left differential graded actions of `A` on a cochain complex `M` of `R`-modules correspond
> canonically to homomorphisms of differential graded algebras from `A` into the endomorphism
> differential graded algebra of `M`. The specification identifies the image of each homogeneous
> element with its action as a cochain.

```lean
noncomputable def leftActionEquivHom (A : DifferentialGradedAlgebra R)
    (M : CochainComplex (ModuleCat.{u} R) ℤ) :
    { e : A.LeftAction M ≃ A.Hom (endomorphismDGA M).algebra //
      ∀ (L : A.LeftAction M) (n : ℤ) (a : A.grading n),
        (endomorphismDGA M).cochainEquiv n
          ⟨(e L).toAlgebraHom a, (e L).map_grading n a a.property⟩ = L.action n a }
```

## Tag 0FQ4, a lemma

[Tag 0FQ4](https://stacks.math.columbia.edu/tag/0FQ4) in the Stacks Project.

**`DifferentialGraded.rightTensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L619). The attribute's comment: “the identification”.

> For a right differential graded `A`-module `M'`, a left differential graded `A`-module `M` and
> a complex `N` of `R`-modules, homomorphisms of right differential graded `A`-modules
> `M' → Hom(M, N)` are the maps of complexes of `R`-modules `M' ⊗_A M → N`.

```lean
noncomputable def rightTensorHomEquiv :
    DifferentialGradedModule.Hom M' P ≃ (tensorComplex M' M ⟶ N)
```

**`DifferentialGraded.rightTensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L625). The attribute's comment: “the identification on pure tensors”.

> `rightTensorHomEquiv` sends `g` to the map of complexes taking `x ⊗ y` to `(g x)(y)`.

```lean
theorem rightTensorHomEquiv_apply (g : DifferentialGradedModule.Hom M' P)
    (p q n : ℤ) (h : p + q = n) (x : M'.grading p) (y : M.grading q) :
    ((rightTensorHomEquiv M' M N P iso hact g).f n).hom ((tensorTmul M' M).map p q n h x y) =
      (((iso.hom.f p) ⟨g.toFun x, g.map_grading p x x.property⟩).v q n (by omega)).hom y
```

**`DifferentialGraded.exists_rightTensorHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L643). The attribute's comment: “existence of the identification”.

> There is a right differential graded `A`-module `P` with underlying complex `Hom(M, N)` such
> that homomorphisms `M' → P` are in bijection with maps of complexes `M' ⊗_A M → N`.

```lean
theorem exists_rightTensorHomEquiv :
    ∃ (P : DifferentialGradedModule.{u, v, u} A)
      (_ : P.toCochainComplex ≅ HomComplexR R (LeftModule.toCochainComplex A M) N),
      Nonempty (DifferentialGradedModule.Hom M' P ≃ (tensorComplex M' M ⟶ N))
```

## Tag 0FQ5, a lemma

[Tag 0FQ5](https://stacks.math.columbia.edu/tag/0FQ5) in the Stacks Project.

**`DifferentialGradedModule.existsUnique_isSignedAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/RightModuleHom.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/RightModuleHom.lean#L402). The attribute's comment: “module to homomorphism”.

> A right differential graded `A`-module whose underlying complex is identified with `M`
> determines a unique homomorphism of differential graded algebras from `A` into the graded opposite
> of the endomorphism algebra of `M`, namely the one satisfying the signed-action equation.

```lean
theorem existsUnique_isSignedAction (A : DifferentialGradedAlgebra R)
    (M : CochainComplex (ModuleCat.{u} R) ℤ) (L : DifferentialGradedModule A)
    (i : L.toCochainComplex ≅ M) :
    ∃! τ : A.Hom (oppEndAlgebra M), IsSignedAction A M L i τ
```

**`DifferentialGradedModule.exists_rightModule_isSignedAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/RightModuleHom.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/RightModuleHom.lean#L491). The attribute's comment: “homomorphism to module”.

> Every homomorphism of differential graded algebras from `A` into the graded opposite of the
> endomorphism algebra of `M` arises from a right differential graded `A`-module whose underlying
> complex is `M`, with the action given by the signed-action equation.

```lean
theorem exists_rightModule_isSignedAction (A : DifferentialGradedAlgebra R)
    (M : CochainComplex (ModuleCat.{u} R) ℤ) (τ : A.Hom (oppEndAlgebra M)) :
    ∃ (L : DifferentialGradedModule A) (i : L.toCochainComplex ≅ M), IsSignedAction A M L i τ
```

## Tag 0FQ6, a lemma

[Tag 0FQ6](https://stacks.math.columbia.edu/tag/0FQ6) in the Stacks Project.

**`DifferentialGraded.leftTensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 1229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L1229). The attribute's comment: “the identification”.

> For a right differential graded `A`-module `M`, a left differential graded `A`-module `M'` and
> a complex `N` of `R`-modules, homomorphisms of left differential graded `A`-modules
> `M' → Hom(M, N)` are the maps of complexes of `R`-modules `M ⊗_A M' → N`.

```lean
noncomputable def leftTensorHomEquiv :
    LeftModule.Hom M' H ≃ (tensorComplex M M' ⟶ N)
```

**`DifferentialGraded.leftTensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 1236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L1236). The attribute's comment: “the identification on pure tensors”.

> `leftTensorHomEquiv` sends `g` to the map of complexes taking `x ⊗ y` to
> `(-1)^{pq} (g y)(x)`.

```lean
theorem leftTensorHomEquiv_apply (g : LeftModule.Hom M' H)
    (p q n : ℤ) (h : p + q = n) (x : M.grading p) (y : M'.grading q) :
    ((leftTensorHomEquiv M M' N H iso hact g).f n).hom ((tensorTmul M M').map p q n h x y) =
      ((p * q).negOnePow : ℤ) •
        (((iso.hom.f q) ⟨g.toFun y, g.map_grading q y y.property⟩).v p n (by omega)).hom x
```

**`DifferentialGraded.exists_leftTensorHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean, line 1255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/TensorHomAdjunction.lean#L1255). The attribute's comment: “existence of the identification”.

> There is a left differential graded `A`-module `H` with underlying complex `Hom(M, N)` such
> that homomorphisms `M' → H` are in bijection with maps of complexes `M ⊗_A M' → N`.

```lean
theorem exists_leftTensorHomEquiv :
    ∃ (H : LeftModule A)
      (_ : LeftModule.toCochainComplex A H ≅ HomComplexR R M.toCochainComplex N),
      Nonempty (LeftModule.Hom M' H ≃ (tensorComplex M M' ⟶ N))
```

## Tag 0FQ7, a remark

[Tag 0FQ7](https://stacks.math.columbia.edu/tag/0FQ7) in the Stacks Project.

**`DifferentialGraded.LeftModule.exists_homEvaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomEvaluation.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomEvaluation.lean#L788). The attribute's comment: “the LEFT-handed remark: `M` is a LEFT differential graded `A`-module (called `L` here), `Hom(M, N)` is a RIGHT one (`rightHom`), `Hom(Hom(M, N), N)` is a LEFT one (`doubleHom`), and `ev` is a map of LEFT differential graded `A`-modules — its type is `DifferentialGraded.LeftModule.Hom L doubleHom`, whose `A`-linearity the third conjunct spells out. The modules are asserted to exist rather than named, having no canonical presentation, so each comes with an isomorphism of its underlying complex with the relevant Hom complex and with the formula for its action; the last conjunct identifies `ev` on underlying complexes with `CochainComplex.HomComplex.evaluationToDoubleHom`, which is 0FNM.”.

> **Stacks 0FQ7.** Let `A` be a differential graded `R`-algebra, `L` a left differential graded
> `A`-module and `N` a complex of `R`-modules. Then there are a right differential graded
> `A`-module `rightHom` with underlying complex `Hom^•(L, N)`, acting by precomposition with the
> left action of `L`; a left differential graded `A`-module `doubleHom` with underlying complex
> `Hom^•(Hom^•(L, N), N)`, acting by signed precomposition with the right action of `rightHom`; and
> an evaluation map
>
> `ev : L ⟶ doubleHom`
>
> in the category of left differential graded `A`-modules, so in particular `ev (a • x) = a • ev x`
> for every `a ∈ A`; on underlying complexes of `R`-modules `ev` is the evaluation map of
> Tag 0FNM, read through the two identifications.

```lean
theorem exists_homEvaluation (A : DifferentialGradedAlgebra.{u, v} R)
    (L : DifferentialGraded.LeftModule A) (N : CochainComplex (ModuleCat.{u} R) ℤ) :
    ∃ (rightHom : DifferentialGradedModule A)
      (rightHomIso : rightHom.toCochainComplex ≅ HomComplexR R (toCochainComplex A L) N)
      (doubleHom : DifferentialGraded.LeftModule A)
      (doubleHomIso : toCochainComplex A doubleHom ≅ HomComplexR R rightHom.toCochainComplex N)
      (ev : DifferentialGraded.LeftModule.Hom L doubleHom),
      (∀ (p q : ℤ) (a : A.grading p) (f : rightHom.grading q),
        (rightHomIso.hom.f (q + p))
            (⟨MulOpposite.op (a : A.A) • (f : rightHom.M),
              rightHom.smul_mem q p (f : rightHom.M) (a : A.A) f.property a.property⟩ :
              rightHom.grading (q + p)) =
          ((leftAction A L (toCochainComplex A L) (Iso.refl _)).action p a).comp
            ((rightHomIso.hom.f q) f) (by omega)) ∧
      (∀ (p q r : ℤ) (a : A.grading p) (g : doubleHom.grading r) (f : rightHom.grading q),
        HEq
          ((((doubleHomIso.hom.f (p + r))
              (⟨(a : A.A) • (g : doubleHom.M),
                doubleHom.smul_mem p r (a : A.A) (g : doubleHom.M) a.property g.property⟩ :
                doubleHom.grading (p + r))).v q (q + (p + r)) (by omega)).hom f)
          ((p * (q + r)).negOnePow •
            (((doubleHomIso.hom.f r) g).v (q + p) (q + p + r) (by omega)).hom
              (⟨MulOpposite.op (a : A.A) • (f : rightHom.M),
                rightHom.smul_mem q p (f : rightHom.M) (a : A.A) f.property a.property⟩ :
                rightHom.grading (q + p)))) ∧
      (∀ (a : A.A) (x : L.M), ev.toFun (a • x) = a • ev.toFun x) ∧
      (∀ (n : ℤ) (x : L.grading n),
        (doubleHomIso.hom.f n)
            (⟨ev.toFun x, ev.map_grading n x x.property⟩ : doubleHom.grading n) =
          ((CochainComplex.HomComplex.evaluationToDoubleHom (toCochainComplex A L) N ≫
              Stacks.HomComplex.TensorHomMap.precomp R rightHom.toCochainComplex
                (HomComplexR R (toCochainComplex A L) N) N rightHomIso.hom).f n) x)
```

## Tag 0FQ8, a remark

[Tag 0FQ8](https://stacks.math.columbia.edu/tag/0FQ8) in the Stacks Project.

**`DifferentialGradedModule.nonempty_homEvaluationData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomEvaluation.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomEvaluation.lean#L542). The attribute's comment: “the RIGHT-handed remark: `M` is a RIGHT differential graded `A`-module, `Hom(M, N)` is a LEFT one (`leftHom`), `Hom(Hom(M, N), N)` is a RIGHT one (`doubleHom`), and `ev` is a map of RIGHT differential graded `A`-modules — its type is `DifferentialGradedModule.Hom M doubleHom`. The data are asserted to exist rather than named, the Hom modules having no canonical presentation; `evaluation_apply` pins `ev` to 0FNM.”.

> **Stacks 0FQ8.** For a right differential graded `A`-module `M` and a complex `N` of
> `R`-modules, the Hom complex `Hom^•(M, N)` carries a left differential graded `A`-module structure,
> its Hom complex into `N` carries a right one, and the canonical evaluation map of Tag 0FNM is a
> homomorphism of right differential graded `A`-modules.

```lean
theorem nonempty_homEvaluationData (A : DifferentialGradedAlgebra.{u, v} R)
    (M : DifferentialGradedModule A) (N : CochainComplex (ModuleCat.{u} R) ℤ) :
    Nonempty (HomEvaluationData A M N)
```

## Tag 0FQ9, a remark

[Tag 0FQ9](https://stacks.math.columbia.edu/tag/0FQ9) in the Stacks Project.

**`DifferentialGradedAlgebra.LeftAction.shiftHomCochain_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomComplexShift.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomComplexShift.lean#L171). The attribute's comment: “left modules”.

> **Stacks 0FQ9**, left modules. If `M` is a left differential graded `A`-module then the
> identification `Hom^•(M, N)[a - b] ≅ Hom^•(M[b], N[a])` of Tag 0FNN is a map of right differential
> graded `A`-modules: both actions are precomposition, on the source with the given action — shifting
> a right module introduces no sign — and on the target with the Koszul-signed shifted action
> `DifferentialGradedAlgebra.LeftAction.shift`. Remark 22.26.9 is the case `a = 0`, `b = k`.

```lean
theorem LeftAction.shiftHomCochain_comp (act : A.LeftAction M) (a b p q : ℤ) (α : A.grading p)
    (z : Cochain M N q) :
    shiftHomCochain M N a b (p + q) ((act.action p α).comp z rfl) =
      ((act.shift b).action p α).comp (shiftHomCochain M N a b q z) (by omega)
```

**`DifferentialGradedAlgebra.RightAction.shiftHomCochain_homAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomComplexShift.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Endomorphism/HomComplexShift.lean#L184). The attribute's comment: “right modules”.

> **Stacks 0FQ9**, right modules. If `M` is a right differential graded `A`-module then the
> identification `Hom^•(M, N)[a - b] ≅ Hom^•(M[b], N[a])` of Tag 0FNN is a map of left differential
> graded `A`-modules: the target carries the left action induced by the shifted right action on
> `M[b]`, and the source carries the left action induced on `Hom^•(M, N)`, multiplied by the Koszul
> factor `(-1)^(p (a - b))` of the shift by `a - b`. Remark 22.26.9 is the case `a = 0`, `b = k`,
> where that factor is `(-1)^(p k)`.

```lean
theorem RightAction.shiftHomCochain_homAction (t : A.RightAction M) (a b p q : ℤ)
    (α : A.grading p) (z : Cochain M N q) :
    shiftHomCochain M N a b (p + q)
        ((p * (a - b)).negOnePow • (t.homLeftAction N).homAction p q (p + q) (by omega) α z) =
      ((t.shift b).homLeftAction (N⟦a⟧)).homAction p (q + (b - a)) (p + q + (b - a)) (by omega) α
        (shiftHomCochain M N a b q z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.13, Tag 0FQ2](https://stacks.math.columbia.edu/tag/0FQ2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
