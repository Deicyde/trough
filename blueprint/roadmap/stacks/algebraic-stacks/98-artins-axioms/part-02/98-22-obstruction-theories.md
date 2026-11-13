---
declaration: section
origin: cited
lean: Deformation.Artin.ObstructionTheory, Deformation.Artin.isOpenVersality_of_obstructionTheory, Deformation.Artin.SectionsSheaf.exists_obstructionTheory, Deformation.Artin.KeyExample.objEquivTuple, Deformation.Artin.KeyExample.exists_isHomotopyEquiv_nl_canonical, Deformation.Artin.KeyExample.exists_basis_nl_cotangentSpace, Deformation.Artin.KeyExample.Situation.Lift.obsHom, Deformation.Artin.KeyExample.Situation.Lift.obsHom_mk
statement: formalized
proof: formalized
---

# 98.22 Obstruction theories

Section 98.22 of the Stacks Project, [Tag 07YF](https://stacks.math.columbia.edu/tag/07YF). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07YG, a definition

[Tag 07YG](https://stacks.math.columbia.edu/tag/07YG) in the Stacks Project.

**`Deformation.Artin.ObstructionTheory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/Theory.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/Theory.lean#L232).

> An obstruction theory for a category fibred in groupoids over the big fppf site of `S`: a
> linear functor of obstruction modules at every object over the spectrum of an `S`-algebra
> mapping into an affine open, functorial in the triple `(x, A, M)`, together with an obstruction
> element for every deformation situation whose vanishing is equivalent to the existence of a
> lift.

```lean
public structure ObstructionTheory (hp : p.IsFiberedInGroupoids)
```

## Tag 0CYF, a lemma

[Tag 0CYF](https://stacks.math.columbia.edu/tag/0CYF) in the Stacks Project.

**`Deformation.Artin.isOpenVersality_of_obstructionTheory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessObstruction.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/OpennessObstruction.lean#L90).

> Let `S` be a locally Noetherian scheme and let `𝒳` be a category fibred in
> groupoids over the big fppf site of `S`. Assume
>
> 1. the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces,
> 2. `𝒳` has (RS*),
> 3. `𝒳` is limit preserving,
> 4. there exists an obstruction theory `O`,
> 5. for an object `x` of `𝒳` over `Spec A` and `A`-modules `Mₙ`, `n ≥ 1`,
>    (a) `T_x(∏ Mₙ) = ∏ T_x(Mₙ)`, and
>    (b) `𝒪_x(∏ Mₙ) ⟶ ∏ 𝒪_x(Mₙ)` is injective.
>
> Then `𝒳` satisfies openness of versality: if `x` over a scheme `U` locally of finite type over
> `S` is versal at a finite type point `u₀`, it is versal at every finite type point of an open
> neighbourhood of `u₀`.

```lean
theorem isOpenVersality_of_obstructionTheory [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (AlgebraicGeometry.BigFppfOver B S hS))
    (h1 : AlgebraicGeometry.Stack.HasRepresentableDiagonal B S hS 𝒳)
    (h2 : SatisfiesRSStar B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (h3 : IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳)
    (O : ObstructionTheory B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids)
    (h5a : TangentPreservesCountableProducts B S hS 𝒳.val.p 𝒳.isFiberedInGroupoids h2)
    (h5b : O.InjectiveOnCountableProducts) :
    ∀ (U : Over S), LocallyOfFiniteType U.hom →
      ∀ (x : 𝒳.val.obj) (hx : (𝒳.val.p ⋙ Over.post B.inclusion).obj x = U) (u₀ : U.left),
        IsFiniteTypePoint u₀ →
        IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u₀ x hx →
        ∃ W : U.left.Opens, u₀ ∈ W.1 ∧
          ∀ u ∈ W.1, IsFiniteTypePoint u →
            IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u x hx
```

## Tag 07YH, an example

[Tag 07YH](https://stacks.math.columbia.edu/tag/07YH) in the Stacks Project.

**`Deformation.Artin.SectionsSheaf.exists_obstructionTheory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionTheory.lean, line 787](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/SectionsObstructionTheory.lean#L787).

> **Stacks 07YH.** Let `S = Spec Λ` with `Λ` Noetherian, `W → S` a morphism of schemes and `𝓕` a
> quasi-coherent `𝒪_W`-module flat over `S`. The category fibred in groupoids `𝒳` attached to
> `F : T/S ↦ H⁰(W_T, 𝓕_T)` has an obstruction theory (Stacks 07YG) whose obstruction modules at an
> object `x` over `Spec A` are `𝒪_x(M) = H¹(W_A, 𝓕_A ⊗_A M)` (`affineObstruction`, i.e.
> `obstructionFunctor`, as a functor of `M`), and whose obstruction element at a deformation
> situation `(x, A' → A)` is the image of `x` under the boundary map
> `H⁰(W_A, 𝓕_A) → H¹(W_A, 𝓕_A ⊗_A I)` of `0 → 𝓕_A ⊗_A I → 𝓕_{A'} → 𝓕_A → 0`.

```lean
theorem exists_obstructionTheory [IsNoetherianRing Λ]
    (hF : AlgebraicGeometry.IsFlatOver g.toLRSHom.toShHom F) :
    ∃ θ : ObstructionTheory B (Spec (.of Λ)) hS (sectionsFibredCategory g F B hS)
        (Functor.IsFiberedInSets.isFiberedInGroupoids _),
      ∃ e : ∀ P, (θ.obstruction P).functor ≅ (affineObstruction g F P).functor,
        ∀ P t, (e P).hom.app t.kernelObj (θ.obs P t) = sectionsObstructionClass B hS g F hF P t
```

## Tag 07YI, an example

[Tag 07YI](https://stacks.math.columbia.edu/tag/07YI) in the Stacks Project.

**`Deformation.Artin.KeyExample.objEquivTuple`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L197). The attribute's comment: “x corresponds to a tuple (a\_1, …, a\_n) killing J”.

> An object `x` of `𝒳 = (Sch/Spec R)_{fppf}` over `Spec A`, that is a
> `Λ`-algebra map `R → A` with `R = Λ[x_1, …, x_n]/J`, is the same datum as a tuple
> `(a_1, …, a_n)` of elements of `A` with `f(a_1, …, a_n) = 0` in `A` for every `f ∈ J`.

```lean
noncomputable def objEquivTuple :
    ((MvPolynomial (Fin n) Λ ⧸ J) →ₐ[Λ] A) ≃
      {a : Fin n → A // ∀ f ∈ J, MvPolynomial.aeval a f = 0}
```

**`Deformation.Artin.KeyExample.exists_isHomotopyEquiv_nl_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L228). The attribute's comment: “NL\_\{R/Λ} is canonically homotopy equivalent to J/J² → ⊕ R dx\_i”. References: SGA 6 0 (4.3), “partial”; SGA 6 0 (4.4), “special case”.

> The naive cotangent complex `NL_{R/Λ}` is canonically homotopy equivalent to the two-term
> complex `J/J² → ⊕_{i = 1, …, n} R dx_i` attached to the presentation `Λ[x_1, …, x_n] → R`:
> there is a morphism of presentations onto the canonical presentation, and the induced chain map
> is a homotopy equivalence. This is Stacks 00S1(4) read at the presentation of the key example;
> `presentation_ker` identifies the conormal module of `presentation J` with `J/J²`.

```lean
theorem exists_isHomotopyEquiv_nl_canonical :
    ∃ φ : P.Hom (NaiveCotangent.canonicalGenerators Λ R),
      NaiveCotangent.IsHomotopyEquiv
        (NaiveCotangent.nlMap P (NaiveCotangent.canonicalGenerators Λ R) φ)
```

**`Deformation.Artin.KeyExample.exists_basis_nl_cotangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L241). The attribute's comment: “the degree-0 term is the free module ⊕\_\{i = 1, …, n} R dx\_i”.

> The degree-`0` term of the two-term complex of the key example is the free `R`-module
> `⊕_{i = 1, …, n} R dx_i` on the classes `dx_i` of the variables.

```lean
theorem exists_basis_nl_cotangentSpace :
    ∃ b : Module.Basis (Fin n) R (NaiveCotangent.NL P).X₀,
      ∀ i, b i = 1 ⊗ₜ[P.toExtension.Ring]
        (KaehlerDifferential.D Λ P.toExtension.Ring) (MvPolynomial.X i)
```

**`Deformation.Artin.KeyExample.Situation.Lift.obsHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L409). The attribute's comment: “the map J/J² → I, f ↦ f(a'\_1, …, a'\_n)”.

> **The obstruction map**: the `R`-linear map `J/J² → I` sending the class
> of `f ∈ J` to `f(a'_1, …, a'_n)`, where `a'_i` are the chosen lifts. It is the map induced
> on conormal modules by the morphism of extensions `Lift.hom`; its target is `I/I²`, which is
> `I` because `I² = 0` (see `Situation.cotangentEquivKernel`).

```lean
noncomputable def Lift.obsHom (l : t.Lift) :
    P.toExtension.Cotangent →ₗ[R] t.ext.Cotangent
```

**`Deformation.Artin.KeyExample.Situation.Lift.obsHom_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L416). The attribute's comment: “o\_x(A') is represented by the map f ↦ f(a'\_1, …, a'\_n)”.

> **The obstruction map sends the class of `f ∈ J` to `f(a'_1, …, a'_n) ∈ I`**, through the
> identification `I/I² = I` of `Situation.cotangentEquivKernel`.

```lean
theorem Lift.obsHom_mk (l : t.Lift) (f : P.ker) :
    l.obsHom (Algebra.Extension.Cotangent.mk f) =
      t.cotangentEquivKernel
        ⟨MvPolynomial.aeval l.val (f : MvPolynomial (Fin n) Λ), l.aeval_mem_kernel f⟩
```

**`Deformation.Artin.KeyExample.obstructionModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L473). The attribute's comment: “the obstruction module Hom\_R(J/J², M)/Hom\_R(R^\{⊕n}, M)”.

> **The obstruction module**,
> `𝒪_x(M) = Hom_R(J/J², M)/Hom_R(R^{⊕n}, M)`: the `R`-linear maps out of the conormal module
> `J/J²` of the presentation, modulo those that factor through the differential
> `J/J² → ⊕_i R dx_i` of the naive cotangent complex. The quotient is taken by the range of
> precomposition with that differential; since `⊕_i R dx_i` is free on the `dx_i`, the
> submodule divided out is the image of `Hom_R(R^{⊕n}, M)`.

```lean
abbrev obstructionModule (P : Algebra.Generators Λ R (Fin n)) (M : Type v) [AddCommGroup M]
    [Module R M]
```

**`Deformation.Artin.KeyExample.obstructionModuleAddEquivExtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L490). The attribute's comment: “Hom\_R(J/J², M)/Hom\_R(R^\{⊕n}, M) = Ext¹\_R(NL\_\{R/Λ}, M)”.

> The obstruction module `Hom_R(J/J², M)/Hom_R(R^{⊕n}, M)` is
> `Ext¹_R(NL_{R/Λ}, M)`: the comparison of Stacks 0GPU,
> `NaiveCotangent.extOne_naiveCotangentComplex_addEquiv_cokernel`, read at the presentation of
> the key example.

```lean
noncomputable def obstructionModuleAddEquivExtOne
    (P : Algebra.Generators Λ R (Fin n)) (M : Type v) [AddCommGroup M] [Module R M]
```

**`Deformation.Artin.KeyExample.Situation.obsClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L501). The attribute's comment: “the obstruction element o\_x(A')”.

> **The obstruction element `o_x(A')`**: the class in the obstruction module
> of the map `J/J² → I`, `f ↦ f(a'_1, …, a'_n)`.

```lean
noncomputable def obsClass (l : t.Lift) : obstructionModule P t.ext.Cotangent
```

**`Deformation.Artin.KeyExample.Situation.obsClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L509). The attribute's comment: “o\_x(A') is independent of the choice of lifts”.

> **`o_x(A')` does not depend on the choice of the lifts `a'_i`.** Two
> families of lifts induce morphisms of extensions whose maps on conormal modules differ by
> precomposition with the differential of the naive cotangent complex, so their classes in
> `Hom_R(J/J², I)/Hom_R(R^{⊕n}, I)` agree.

```lean
theorem obsClass_eq (l l' : t.Lift) : obsClass l = obsClass l'
```

**`Deformation.Artin.KeyExample.Situation.obsClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L605). The attribute's comment: “o\_x(A') = 0 if and only if Lift(x, A') is nonempty”.

> **`o_x(A') = 0` if and only if `x` lifts.** This is condition (iii) of
> Stacks 07YG for the key example.

```lean
theorem obsClass_eq_zero_iff (l : t.Lift) : obsClass l = 0 ↔ HasLift t
```

**`Deformation.Artin.KeyExample.Situation.coe_cotangentEquivKernel_symm_obsHom_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExample.lean#L629). The attribute's comment: “a morphism of deformation situations carries o\_x(A') to o\_y(B')”.

> **Functoriality of the obstruction element.** For a morphism of deformation
> situations `(x, A' → A) → (y, B' → B)` the obstruction map of `x` is carried to the
> obstruction map of `y` by the map `I → I₂` induced on kernels by `A' → B'`, so `o_x(A')`
> maps to `o_y(B')`.

```lean
theorem coe_cotangentEquivKernel_symm_obsHom_pushforward {t₂ : Situation P}
    (ι : t.thick →ₐ[Λ] t₂.thick) (κ : t.base →ₐ[Λ] t₂.base)
    (hcomm : t₂.proj.comp ι = κ.comp t.proj) (hobj : κ.comp t.obj = t₂.obj) (l : t.Lift)
    (f : P.ker) :
    ((t₂.cotangentEquivKernel.symm
          ((l.pushforward ι κ hcomm hobj).obsHom
            (Algebra.Extension.Cotangent.mk f))).1 : t₂.thick) =
      ι (((t.cotangentEquivKernel.symm
        (l.obsHom (Algebra.Extension.Cotangent.mk f))).1 : t.thick))
```

**`Deformation.Artin.KeyExample.baseChangedObstructionModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean#L184). The attribute's comment: “the obstruction module computed from NL\_\{R/Λ} ⊗\_R A”.

> **The obstruction module of Stacks 07YI computed after base change**, the cokernel
> `Hom_A(A ⊗_R J/J², M)/Hom_A(A ⊗_R R^{⊕n}, M)` of the dual of the differential of
> `NL_{R/Λ} ⊗_R A`.

```lean
abbrev baseChangedObstructionModule
```

**`Deformation.Artin.KeyExample.obstructionModuleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean#L195). The attribute's comment: “Hom\_R(J/J², M)/Hom\_R(R^\{⊕n}, M) = Hom\_A(A ⊗ J/J², M)/Hom\_A(A ⊗ R^\{⊕n}, M)”.

> **Stacks 07YI.** The obstruction module `Hom_R(J/J², M)/Hom_R(R^{⊕n}, M)` of the key
> example agrees with the obstruction module computed from `NL_{R/Λ} ⊗_R A`: the tensor-hom
> adjunction carries one cokernel presentation onto the other.

```lean
def obstructionModuleBaseChange :
    obstructionModule P M ≃+ baseChangedObstructionModule P A M
```

**`Deformation.Artin.KeyExample.extOneNaiveCotangentBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleBaseChange.lean#L212). The attribute's comment: “Ext¹\_R(NL\_\{R/Λ}, I) = Ext¹\_A(NL\_\{R/Λ} ⊗\_R A, I)”.

> **Stacks 07YI: `Ext¹_R(NL_{R/Λ}, M) = Ext¹_A(NL_{R/Λ} ⊗_R A, M)`.** The first extension
> group of the naive cotangent complex of `R` over `Λ` with coefficients in an `A`-module `M` is
> the first extension group over `A` of the base change `NL_{R/Λ} ⊗_R A`. Both complexes are
> realized as the mapping cone of their differential, so that the conormal module lies in degree
> `-1`.

```lean
def extOneNaiveCotangentBaseChange :
    DerivedCategory.Ext
        (DerivedCategory.Q.obj (HomologicalComplex.homotopyCofiber
          (NaiveCotangent.ExtCokernelLinear.singleMap
            (ModuleCat.ofHom P.toExtension.cotangentComplex))))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R M)) 1 ≃+
      DerivedCategory.Ext
        (DerivedCategory.Q.obj (HomologicalComplex.homotopyCofiber
          (NaiveCotangent.ExtCokernelLinear.singleMap
            (ModuleCat.ofHom (P.toExtension.cotangentComplex.baseChange A)))))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) 1
```

**`Deformation.Artin.nlBaseChangeToNaive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean, line 650](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean#L650). The attribute's comment: “the map NL\_\{R/Λ} ⊗\_R A → NL\_\{A/Λ}”.

> **The morphism `NL_{R/Λ} ⊗_R A ⟶ NL_{A/Λ}`** in the derived category of `A`-modules:
> functoriality of the naive cotangent complex for the `Λ`-algebra map `R → A`, with the source
> written as the termwise base change of the two-term complex of the presentation
> `Λ[x_1, …, x_n] → R`.

```lean
def nlBaseChangeToNaive :
    DerivedCategory.Q.obj (double
        (ModuleCat.ofHom (P.toExtension.cotangentComplex.baseChange A))
        upIntRelNegOneZero) ⟶
      derivedNaiveCotangentComplex Λ A
```

**`Deformation.Artin.cotangentComposition_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean#L699). The attribute's comment: “the composite NL\_\{R/Λ} ⊗\_R A → NL\_\{A/Λ} → NL\_\{A/A'} = I[1]”.

> **Stacks 07YI: the invariant description of the obstruction element.** The composite
> `NL_{R/Λ} ⊗_R A ⟶ NL_{A/Λ} ⟶ NL_{A/A'} = I[1]` in the derived category of `A`-modules is the
> class of the conormal functional `compositeObsFunctional`.

```lean
theorem cotangentComposition_eq :
    letI := Stacks.Smooth.kerModule hq hsq
    nlBaseChangeToNaive Λ R A P ≫ cotangentExtensionClass Λ A' A hq hsq =
      DerivedCategory.Q.map (doubleToSingleNegOne
        (ModuleCat.ofHom (P.toExtension.cotangentComplex.baseChange A))
        (ModuleCat.ofHom (compositeObsFunctional Λ R A A' P hq hsq)))
```

**`Deformation.Artin.coe_compositeObsFunctional_one_tmul_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean, line 800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean#L800). The attribute's comment: “the composite is represented by the map f ↦ f(a'\_1, …, a'\_n)”.

> **The conormal functional of the composite, in coordinates**: on `1 ⊗ (class of f)` it is
> `f(a'_1, …, a'_n)`, where `a'_i` are the lifts `canonicalLift i`. This is the map `J/J² → I`
> of Stacks 07YI.

```lean
theorem coe_compositeObsFunctional_one_tmul_mk (f : P.toExtension.ker) :
    letI := Stacks.Smooth.kerModule hq hsq
    ((compositeObsFunctional Λ R A A' P hq hsq
          (1 ⊗ₜ[R] Algebra.Extension.Cotangent.mk f)).1 : A') =
      (MvPolynomial.aeval (canonicalLift Λ R A A' P hq) :
        P.toExtension.Ring →ₐ[Λ] A') f.1
```

**`Deformation.Artin.doubleCokernelExtEquiv_cotangentComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean, line 819](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/KeyExampleCotangentClass.lean#L819). The attribute's comment: “o\_x(A') equals the composite NL\_\{R/Λ} → NL\_\{A/Λ} → NL\_\{A/A'} = I[1]”.

> **Stacks 07YI: the obstruction element is the composite of cotangent complexes.** Under
> the identification of `Hom_{D(A)}(NL_{R/Λ} ⊗_R A, I[1]) = Ext¹_A(NL_{R/Λ} ⊗_R A, I)` with the
> cokernel `Hom_A(A ⊗_R J/J², I)/Hom_A(A ⊗_R R^{⊕n}, I)`, the composite
> `NL_{R/Λ} ⊗_R A ⟶ NL_{A/Λ} ⟶ NL_{A/A'} = I[1]` is the class of the functional whose value on
> `1 ⊗ (class of f)` is `f(a'_1, …, a'_n)`, for the lifts `a'_i = canonicalLift i` of the
> coordinates of `x`. That class is the obstruction element `o_x(A')` of
> `Deformation.Artin.KeyExample.Situation.obsClass`, which by
> `Deformation.Artin.KeyExample.Situation.obsClass_eq` does not depend on the chosen lifts.

```lean
theorem doubleCokernelExtEquiv_cotangentComposition :
    letI := Stacks.Smooth.kerModule hq hsq
    doubleCokernelExtEquiv (P.toExtension.cotangentComplex.baseChange A)
        (RingHom.ker (algebraMap A' A))
        (nlBaseChangeToNaive Λ R A P ≫ cotangentExtensionClass Λ A' A hq hsq) =
      Submodule.Quotient.mk (compositeObsFunctional Λ R A A' P hq hsq)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.22, Tag 07YF](https://stacks.math.columbia.edu/tag/07YF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
