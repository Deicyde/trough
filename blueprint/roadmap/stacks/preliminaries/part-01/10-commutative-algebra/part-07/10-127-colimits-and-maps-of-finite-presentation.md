---
declaration: section
origin: cited
lean: CommRingCat.isFiltered_costructuredArrow_and_isDenseAt_finitePresentation, Algebra.exists_directedSystem_finitePresentation_lift_bijective, CommRingCat.finitePresentation_tfae_colimit_hom, CommRingCat.ind_under_iff_exists_factorization, Stacks.FinitePresentation.ColimitDescent.statement_two, Stacks.FinitePresentation.ColimitDescent.statement_three, Stacks.FinitePresentation.ColimitDescent.statement_four, Stacks.FinitePresentation.ColimitDescent.statement_one
statement: formalized
proof: formalized
---

# 10.127 Colimits and maps of finite presentation

Section 10.127 of the Stacks Project, [Tag 00QL](https://stacks.math.columbia.edu/tag/00QL). 17 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BUF, a lemma

[Tag 0BUF](https://stacks.math.columbia.edu/tag/0BUF) in the Stacks Project.

**`CommRingCat.isFiltered_costructuredArrow_and_isDenseAt_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ColimitPresentation/Canonical.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ColimitPresentation/Canonical.lean#L407). The attribute's comment: “The category `𝓘` is `CostructuredArrow P.ι A` for `P` the property of being of finite presentation over `R`, and "the colimit of the `A'` is `A`" is `P.ι.isDenseAt A`, which pins the colimit cocone to the tautological one. No smallness device is needed. See the module docstring.”. References: EGA IV (1.9.3.1), “more general”.

> Let `R → A` be a ring map and let `𝓘 = CostructuredArrow P.ι A` be the category of
> `R`-algebra maps `A' → A` with `A'` of finite presentation over `R`. Then `𝓘` is filtered,
> and `A` is the colimit of the `A'` over `𝓘`, via the tautological cocone whose leg at
> `A' → A` is that map (which is what `Functor.isDenseAt` asserts).

```lean
public theorem isFiltered_costructuredArrow_and_isDenseAt_finitePresentation
    {R : CommRingCat.{u}} (A : Under R) :
    IsFiltered (CostructuredArrow
        (ObjectProperty.ι fun B : Under R ↦ B.hom.hom.FinitePresentation) A) ∧
      (ObjectProperty.ι fun B : Under R ↦ B.hom.hom.FinitePresentation).isDenseAt A
```

## Tag 00QN, a lemma

[Tag 00QN](https://stacks.math.columbia.edu/tag/00QN) in the Stacks Project.

**`Algebra.exists_directedSystem_finitePresentation_lift_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/FinitePresentation.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/FinitePresentation.lean#L406). The attribute's comment: “Both sentences. The second is the implication `Algebra.FiniteType R A → ∀ i j h, Function.Surjective (f i j h)` inside the same existential, which is equivalent to stating it separately; `A = colim G l` is bijectivity of `DirectLimit.Algebra.lift`, which pins the comparison map. See the module docstring.”.

> **Every algebra is a direct limit of algebras of finite presentation.** For a ring map
> `R → A` there is a directed system `G` of `R`-algebras of finite presentation, indexed by a
> directed partially ordered set `Λ`, together with a compatible family of `R`-algebra maps
> `g l : G l →ₐ[R] A` whose induced map `colim_l G l → A` is bijective. If `A` is of finite type
> over `R`, the system can moreover be chosen with all transition maps surjective.

```lean
public theorem Algebra.exists_directedSystem_finitePresentation_lift_bijective
    (R : Type u) [CommRing R] (A : Type v) [CommRing A] [Algebra R A] :
    ∃ (Λ : Type (max u v)) (_ : PartialOrder Λ) (_ : Nonempty Λ) (_ : IsDirectedOrder Λ)
      (G : Λ → Type (max u v)) (_ : ∀ l, CommRing (G l)) (_ : ∀ l, Algebra R (G l))
      (f : ∀ i j, i ≤ j → G i →ₐ[R] G j) (_ : DirectedSystem G fun i j h ↦ ⇑(f i j h))
      (g : ∀ l, G l →ₐ[R] A) (hg : ∀ i j h x, g j (f i j h x) = g i x),
      (∀ l, Algebra.FinitePresentation R (G l)) ∧
      (Algebra.FiniteType R A → ∀ i j (h : i ≤ j), Function.Surjective (f i j h)) ∧
      Function.Bijective (DirectLimit.Algebra.lift G f A g hg)
```

## Tag 00QO, a lemma

[Tag 00QO](https://stacks.math.columbia.edu/tag/00QO) in the Stacks Project.

**`CommRingCat.finitePresentation_tfae_colimit_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/FinitePresentation.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/FinitePresentation.lean#L313). The attribute's comment: “A directed system of `R`-algebras is a functor `Λ ⥤ Under R` out of a nonempty directed preordered set, `colim_λ A_λ` is the vertex of any colimit cocone `c`, and the map `colim_λ Homᵣ(S, A_λ) → Homᵣ(S, colim_λ A_λ)` is `colimit.desc` of `coyoneda.obj (op S)` applied to `c`.”.

> **Algebras of finite presentation are the compact algebras.** For an `R`-algebra `S`, the
> following are equivalent: the ring map `R → S` is of finite presentation; for every directed
> system `A_λ` of `R`-algebras the canonical map `colim_λ Homᵣ(S, A_λ) → Homᵣ(S, colim_λ A_λ)` is
> bijective; for every directed system `A_λ` of `R`-algebras that map is surjective.
>
> A directed system of `R`-algebras is a functor `A : Λ ⥤ Under R` out of a nonempty directed
> preordered set `Λ`, `colim_λ A_λ` is the vertex of any colimit cocone `c` on it, and the
> canonical map is `colimit.desc` of the image of `c` under the hom functor `Homᵣ(S, -)`.

```lean
public theorem finitePresentation_tfae_colimit_hom {R : CommRingCat.{u}} (S : Under R) :
    List.TFAE
      [ S.hom.hom.FinitePresentation,
        ∀ (Λ : Type u) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
          (A : Λ ⥤ Under R) (c : Cocone A), IsColimit c →
            Function.Bijective
              (colimit.desc (A ⋙ CategoryTheory.coyoneda.obj (Opposite.op S))
                ((CategoryTheory.coyoneda.obj (Opposite.op S)).mapCocone c)),
        ∀ (Λ : Type u) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
          (A : Λ ⥤ Under R) (c : Cocone A), IsColimit c →
            Function.Surjective
              (colimit.desc (A ⋙ CategoryTheory.coyoneda.obj (Opposite.op S))
                ((CategoryTheory.coyoneda.obj (Opposite.op S)).mapCocone c)) ]
```

## Tag 07C3, a lemma

[Tag 07C3](https://stacks.math.columbia.edu/tag/07C3) in the Stacks Project.

**`CommRingCat.ind_under_iff_exists_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/FinitePresentation.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/FinitePresentation.lean#L562). The attribute's comment: “The family `𝓔` is an `E : ObjectProperty (Under R)` on the category `Under R` of `R`-algebras, and "`Λ` is a filtered colimit of members of `𝓔`" is Mathlib's `ObjectProperty.ind.{u} E Λ`. `E` is not assumed small; the source's set-theoretic hypothesis is only a smallness device. See the module docstring.”.

> **Criterion for being a filtered colimit of algebras of a given family.** Let `R → Λ` be a
> ring map and let `E` be a family of `R`-algebras of finite presentation over `R`. Then `Λ` is a
> filtered colimit of members of `E` if and only if every `R`-algebra map `A → Λ` with `A` of
> finite presentation over `R` factors as `A → B → Λ` with `B` in `E`.

```lean
public theorem ind_under_iff_exists_factorization {R : CommRingCat.{u}} (Λ : Under R)
    {E : ObjectProperty (Under R)} (hE : E ≤ fun B : Under R ↦ B.hom.hom.FinitePresentation) :
    ObjectProperty.ind.{u} E Λ ↔
      ∀ A : Under R, A.hom.hom.FinitePresentation → ∀ f : A ⟶ Λ,
        ∃ (B : Under R) (g : A ⟶ B) (h : B ⟶ Λ), g ≫ h = f ∧ E B
```

## Tag 05LI, a lemma

[Tag 05LI](https://stacks.math.columbia.edu/tag/05LI) in the Stacks Project.

**`Stacks.FinitePresentation.ColimitDescent.statement_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/ColimitRing.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/ColimitRing.lean#L590). The attribute's comment: “(2)”.

> **Statement (2).** If `N` is a finite `A`-module and `u : M → N` has
> surjective base change to `R`, then its base change to some `R_i` is surjective.

```lean
theorem statement_two
    (htrans : TransitionSystem φ) (hcocone : IsCoconeAlg φ ψ)
    (hcolimN : IsModuleColimit φ ψ N)
    (hN : Module.Finite A N)
    (u : M →ₗ[A] N)
    (h : Function.Surjective (LinearMap.baseChange S u)) :
    ∃ i : ι, Function.Surjective (LinearMap.baseChange (R i) u)
```

**`Stacks.FinitePresentation.ColimitDescent.statement_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/LinearMapDescent.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/LinearMapDescent.lean#L113). The attribute's comment: “(3)”.

> **Statement (3).** If `N` is a finitely presented `A`-module and
> `v : N ⊗_A R → M ⊗_A R` is an `R`-module map, then there is some `i` and an
> `R_i`-module map `v_i : N ⊗_A R_i → M ⊗_A R_i` whose base change along
> `ψ i : R_i → S` (i.e. composition with the canonical identification maps)
> recovers `v`.  Concretely, `v` composed with the canonical map for `N` equals
> the canonical map for `M` composed with `v_i`.

```lean
theorem statement_three
    (htrans : TransitionSystem φ) (hcocone : IsCoconeAlg φ ψ)
    (hcolimM : IsModuleColimit φ ψ M)
    (hN : Module.FinitePresentation A N)
    (v : S ⊗[A] N →ₗ[S] S ⊗[A] M) :
    ∃ (i : ι) (vi : (R i) ⊗[A] N →ₗ[R i] (R i) ⊗[A] M),
      (v.restrictScalars A) ∘ₗ (canonMod ψ N i)
        = (canonMod ψ M i) ∘ₗ (vi.restrictScalars A)
```

**`Stacks.FinitePresentation.ColimitDescent.statement_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/LinearMapDescent.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/LinearMapDescent.lean#L300). The attribute's comment: “(4)”.

> **Statement (4).** If `M` is finite, `N` is finitely presented, and
> `u : M → N` has base change to `R` an isomorphism, then its base change to some
> `R_i` is an isomorphism.

```lean
theorem statement_four
    (htrans : TransitionSystem φ) (hcocone : IsCoconeAlg φ ψ)
    (hcolimM : IsModuleColimit φ ψ M) (hcolimN : IsModuleColimit φ ψ N)
    (hM : Module.Finite A M) (hN : Module.FinitePresentation A N)
    (u : M →ₗ[A] N)
    (h : Function.Bijective (LinearMap.baseChange S u)) :
    ∃ i : ι, Function.Bijective (LinearMap.baseChange (R i) u)
```

**`Stacks.FinitePresentation.ColimitDescent.statement_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/ModuleColimit.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/ModuleColimit.lean#L231). The attribute's comment: “(1)”.

> **Statement (1).** If `M` is a finite `A`-module and `u, u' : M → N` are
> `A`-module maps whose base changes to `R` agree, then their base changes to some
> `R_i` already agree.

```lean
theorem statement_one
    (hcolimN : IsModuleColimit φ ψ N)
    (hM : Module.Finite A M)
    (u u' : M →ₗ[A] N)
    (h : LinearMap.baseChange S u = LinearMap.baseChange S u') :
    ∃ i : ι, LinearMap.baseChange (R i) u = LinearMap.baseChange (R i) u'
```

## Tag 05N7, a lemma

[Tag 05N7](https://stacks.math.columbia.edu/tag/05N7) in the Stacks Project.

**`Module.exists_finitePresentation_and_baseChange_eq_of_lift_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/DirectLimit/FinitePresentation.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/DirectLimit/FinitePresentation.lean#L295). The attribute's comment: “The colimit is a `DirectedSystem` of `A`-algebras whose comparison map `colim_j S j → R` is bijective, as in 00QN; items (2) and (3) are stated over an arbitrary base ring `A` and with the finiteness hypotheses of 05LI (3) and (1), of which they are instances, the source's form being `A = R_λ` and the system restricted to `μ ≥ λ`; `φ = φ_μ ⊗ 1_R` is the commuting square with the canonical maps `LinearMap.rTensor M (algebraMap (S j) R)`. See the module docstring.”. References: EGA IV (8.5.3), “affine case”.

> Let `A` be a ring, let `S` be a directed system of `A`-algebras over a nonempty directed
> preorder `J` with transition maps `f i j : S i →ₐ[A] S j`, and let `R` be an `A`-algebra
> receiving compatible maps `algebraMap (S j) R` which exhibit it as the colimit `colim_j S j`.
> Then the category of finitely presented `R`-modules is the colimit of the categories of finitely
> presented `S j`-modules:
>
> 1. every finitely presented `R`-module `M` is isomorphic to the base change `R ⊗[S j] M_j` of a
>    finitely presented `S j`-module, for some `j`;
> 2. for `A`-modules `M`, `N` with `M` finitely presented, every `R`-linear map
>    `R ⊗[A] M → R ⊗[A] N` is the base change of an `S j`-linear map `S j ⊗[A] M → S j ⊗[A] N`
>    for some `j`, in the sense that the square with the canonical maps
>    `S j ⊗[A] M → R ⊗[A] M` commutes;
> 3. for `A`-modules `M`, `N` with `M` finite, two `A`-linear maps `u, u' : M → N` with
>    `u ⊗ 1_R = u' ⊗ 1_R` satisfy `u ⊗ 1_{S j} = u' ⊗ 1_{S j}` for some `j`.

```lean
public theorem exists_finitePresentation_and_baseChange_eq_of_lift_bijective
    {J : Type w} [Preorder J] [Nonempty J] [IsDirectedOrder J] {A : Type u} [CommRing A]
    {S : J → Type v} [∀ j, CommRing (S j)] [∀ j, Algebra A (S j)]
    (f : ∀ i j, i ≤ j → S i →ₐ[A] S j) [DirectedSystem S fun i j h ↦ ⇑(f i j h)]
    {R : Type v} [CommRing R] [Algebra A R] [∀ j, Algebra (S j) R]
    [∀ j, IsScalarTower A (S j) R]
    (hf : ∀ i j (h : i ≤ j) (x : S i), algebraMap (S j) R (f i j h x) = algebraMap (S i) R x)
    (hR : Function.Bijective (DirectLimit.Algebra.lift S f R
      (fun j ↦ IsScalarTower.toAlgHom A (S j) R) hf)) :
    (∀ (M : Type t) [AddCommGroup M] [Module R M] [Module.FinitePresentation R M],
        ∃ (j : J) (Mj : Type v) (_ : AddCommGroup Mj) (_ : Module (S j) Mj),
          Module.FinitePresentation (S j) Mj ∧ Nonempty (R ⊗[S j] Mj ≃ₗ[R] M)) ∧
    (∀ (M : Type t) [AddCommGroup M] [Module A M] [Module.FinitePresentation A M]
        (N : Type t') [AddCommGroup N] [Module A N] (φ : R ⊗[A] M →ₗ[R] R ⊗[A] N),
        ∃ (j : J) (φj : S j ⊗[A] M →ₗ[S j] S j ⊗[A] N), ∀ x : S j ⊗[A] M,
          φ (LinearMap.rTensor M (IsScalarTower.toAlgHom A (S j) R).toLinearMap x) =
            LinearMap.rTensor N (IsScalarTower.toAlgHom A (S j) R).toLinearMap (φj x)) ∧
    (∀ (M : Type t) [AddCommGroup M] [Module A M] [Module.Finite A M]
        (N : Type t') [AddCommGroup N] [Module A N] (u u' : M →ₗ[A] N),
        u.baseChange R = u'.baseChange R →
          ∃ j : J, u.baseChange (S j) = u'.baseChange (S j))
```

## Tag 05N8, a lemma

[Tag 05N8](https://stacks.math.columbia.edu/tag/05N8) in the Stacks Project.

**`Algebra.TensorProduct.exists_of_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/Hom.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/Hom.lean#L758). The attribute's comment: “The four items are the four conjuncts, each carrying only its own finiteness hypothesis. `B ⊗_A R` is `R ⊗[A] B` and `u ⊗ 1` is `Algebra.TensorProduct.lTensor`; `R = colim_i R_i` is bijectivity of `DirectLimit.Algebra.lift`, as in `00QN`; item (3)'s `v = v_i ⊗ 1` is the commuting square with the comparison maps `rTensor _ (g i)`. See the module docstring.”.

> **Stacks 05N8.** Let `A` be a ring, let `B`, `C` be `A`-algebras, and let `R` be the colimit
> of a directed system `G` of `A`-algebras with transition maps `f` and structure maps
> `g i : G i →ₐ[A] R`.
>
> 1. If `B` is of finite type over `A` and `u, u' : B →ₐ[A] C` satisfy `u ⊗ 1 = u' ⊗ 1` over `R`,
>    then `u ⊗ 1 = u' ⊗ 1` over `G i` for some `i`.
> 2. If `C` is of finite type over `A` and `u ⊗ 1` is surjective over `R`, then `u ⊗ 1` is
>    surjective over `G i` for some `i`.
> 3. If `C` is of finite presentation over `A`, then every `R`-algebra map
>    `v : R ⊗[A] C →ₐ[R] R ⊗[A] B` is the base change of a `G i`-algebra map
>    `vᵢ : G i ⊗[A] C →ₐ[G i] G i ⊗[A] B` for some `i`.
> 4. If `B` is of finite type and `C` of finite presentation over `A` and `u ⊗ 1` is bijective over
>    `R`, then `u ⊗ 1` is bijective over `G i` for some `i`.

```lean
public theorem exists_of_directLimit {A : Type u} [CommRing A]
    {B : Type v} [CommRing B] [Algebra A B] {C : Type w} [CommRing C] [Algebra A C]
    {ι : Type t} [Preorder ι] [Nonempty ι] [IsDirectedOrder ι]
    {G : ι → Type s} [∀ i, CommRing (G i)] [∀ i, Algebra A (G i)]
    (f : ∀ i j, i ≤ j → G i →ₐ[A] G j) [DirectedSystem G fun i j h ↦ ⇑(f i j h)]
    {R : Type r} [CommRing R] [Algebra A R] (g : ∀ i, G i →ₐ[A] R)
    (hg : ∀ i j h x, g j (f i j h x) = g i x)
    (hR : Function.Bijective (DirectLimit.Algebra.lift G f R g hg)) :
    (Algebra.FiniteType A B → ∀ u u' : B →ₐ[A] C,
        lTensor (S := R) R u = lTensor (S := R) R u' →
        ∃ i, lTensor (S := G i) (G i) u = lTensor (S := G i) (G i) u') ∧
    (Algebra.FiniteType A C → ∀ u : B →ₐ[A] C,
        Function.Surjective (lTensor (S := R) R u) →
        ∃ i, Function.Surjective (lTensor (S := G i) (G i) u)) ∧
    (Algebra.FinitePresentation A C → ∀ v : R ⊗[A] C →ₐ[R] R ⊗[A] B,
        ∃ (i : ι) (vᵢ : G i ⊗[A] C →ₐ[G i] G i ⊗[A] B),
          (v.restrictScalars A).comp (rTensor C (g i)) =
            (rTensor B (g i)).comp (vᵢ.restrictScalars A)) ∧
    (Algebra.FiniteType A B → Algebra.FinitePresentation A C → ∀ u : B →ₐ[A] C,
        Function.Bijective (lTensor (S := R) R u) →
        ∃ i, Function.Bijective (lTensor (S := G i) (G i) u))
```

## Tag 05N9, a lemma

[Tag 05N9](https://stacks.math.columbia.edu/tag/05N9) in the Stacks Project.

**`CommRingCat.exists_isPushout_and_exists_eq_comp_and_exists_comp_eq_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ColimitPresentation/FinitePresentation.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ColimitPresentation/FinitePresentation.lean#L863). The attribute's comment: “The colimit is a colimit cocone in `CommRingCat` over a filtered category, an algebra is a ring map, and `A ≅ A_λ ⊗_{R_λ} R` is `IsPushout`, so no tensor product is constructed. Items (2) and (3) are transposed along that pushout, which is Mathlib's spelling and drops the source's finite presentation of `B_λ`; item (3) needs `A_λ` of finite type only. See the module docstring.”.

> **Stacks 05N9.** Let `R = colim_λ R_λ` be a filtered colimit of rings, given by a filtered
> diagram `F` with colimit cocone `c`.
>
> 1. Every finitely presented `R`-algebra `A` is the base change of a finitely presented
>    `R_λ`-algebra `A'`, in the sense that the square `R_λ → A'`, `R_λ → R`, `A' → A`, `R → A` is
>    a pushout.
> 2. If `A'` is of finite presentation over `R_λ` and `B` is the base change to `R` of an
>    `R_λ`-algebra `B'`, then every `R_λ`-algebra map `ρ : A' → B` factors as `ρ = σ ≫ t` through
>    the base change `Bₖ` of `B'` to some `R_μ` with `μ ≥ λ`, by an `R_λ`-algebra map `σ` and the
>    canonical map `t : Bₖ → B`. Transposed along the pushout of item 1, this says that every
>    `R`-algebra map `A' ⊗_{R_λ} R → B' ⊗_{R_λ} R` is the base change of an `R_μ`-algebra map
>    `A' ⊗_{R_λ} R_μ → B' ⊗_{R_λ} R_μ`.
> 3. If `A'` is of finite type over `R_λ` and `φ, ψ : A' → B'` are `R_λ`-algebra maps whose base
>    changes to `R` agree, then their base changes to `R_μ` agree for some `μ ≥ λ`.

```lean
public theorem exists_isPushout_and_exists_eq_comp_and_exists_comp_eq_of_isColimit
    {J : Type v} [Category.{w} J] [IsFiltered J] {F : J ⥤ CommRingCat.{u}} {c : Cocone F}
    (hc : IsColimit c) [PreservesColimit F (forget CommRingCat.{u})] :
    (∀ (A : CommRingCat.{u}) (f : c.pt ⟶ A), f.hom.FinitePresentation →
        ∃ (j : J) (A' : CommRingCat.{u}) (f' : F.obj j ⟶ A') (a : A' ⟶ A),
          f'.hom.FinitePresentation ∧ IsPushout f' (c.ι.app j) a f) ∧
    (∀ (j : J) (A' B' B : CommRingCat.{u}) (f' : F.obj j ⟶ A') (g' : F.obj j ⟶ B')
        (g : c.pt ⟶ B) (b : B' ⟶ B), f'.hom.FinitePresentation →
        IsPushout g' (c.ι.app j) b g →
        ∀ ρ : A' ⟶ B, f' ≫ ρ = c.ι.app j ≫ g →
          ∃ (k : J) (h : j ⟶ k) (Bₖ : CommRingCat.{u}) (gₖ : F.obj k ⟶ Bₖ) (bₖ : B' ⟶ Bₖ)
              (t : Bₖ ⟶ B) (σ : A' ⟶ Bₖ), IsPushout g' (F.map h) bₖ gₖ ∧ bₖ ≫ t = b ∧
            gₖ ≫ t = c.ι.app k ≫ g ∧ f' ≫ σ = F.map h ≫ gₖ ∧ ρ = σ ≫ t) ∧
    (∀ (j : J) (A' B' B : CommRingCat.{u}) (f' : F.obj j ⟶ A') (g' : F.obj j ⟶ B')
        (g : c.pt ⟶ B) (b : B' ⟶ B), f'.hom.FiniteType → IsPushout g' (c.ι.app j) b g →
        ∀ φ ψ : A' ⟶ B', f' ≫ φ = g' → f' ≫ ψ = g' → φ ≫ b = ψ ≫ b →
          ∃ (k : J) (h : j ⟶ k) (Bₖ : CommRingCat.{u}) (gₖ : F.obj k ⟶ Bₖ) (bₖ : B' ⟶ Bₖ),
            IsPushout g' (F.map h) bₖ gₖ ∧ φ ≫ bₖ = ψ ≫ bₖ)
```

## Tag 00QT, a lemma

[Tag 00QT](https://stacks.math.columbia.edu/tag/00QT) in the Stacks Project.

**`exists_essFiniteType_directedSystem_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Colimit.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/EssentialFiniteness/Colimit.lean#L450).

> A local homomorphism `φ : R → S` of local rings is the colimit, over a directed
> set `Λ`, of a system of local homomorphisms `ψ_λ : R_λ → S_λ` of local rings
> such that each `R_λ` is essentially of finite type over `ℤ` and each `S_λ` is
> essentially of finite type over `R_λ` (via `ψ_λ`).
>
> The data is bundled in the existential as:
> * `Λ` with a `Preorder`, `Nonempty` and `IsDirectedOrder` instance — the
>   directed set;
> * `Rl`, `Sl` — the families of local rings, with their `CommRing` and
>   `IsLocalRing` structure;
> * `rf`, `sf` — the transition maps, forming directed systems (`dsR`, `dsS`);
> * `ψ` — the family of local homomorphisms (`instLH`), commuting with the
>   transition maps (`hψ`).
>
> Condition (1) is encoded by the existence of ring isomorphisms
> `eR : colim R_λ ≃+* R` and `eS : colim S_λ ≃+* S` identifying the colimit map
> `Ring.DirectLimit.map ψ hψ` with `φ`, i.e. `φ ∘ eR = eS ∘ (colim ψ)`.

```lean
theorem exists_essFiniteType_directedSystem_colimit
    (R S : Type u) [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    (φ : R →+* S) [IsLocalHom φ] :
    ∃ (Λ : Type u) (instP : Preorder Λ),
    ∃ (_ : Nonempty Λ) (_ : @IsDirectedOrder Λ instP.toLE)
      (Rl : Λ → Type u) (Sl : Λ → Type u)
      (_ : ∀ i, CommRing (Rl i)) (_ : ∀ i, CommRing (Sl i))
      (rf : ∀ i j, i ≤ j → (Rl i →+* Rl j))
      (sf : ∀ i j, i ≤ j → (Sl i →+* Sl j))
      (_ : ∀ i, @IsLocalRing (Rl i) _)
      (_ : ∀ i, @IsLocalRing (Sl i) _)
      (ψ : ∀ i, Rl i →+* Sl i)
      (_ : ∀ i, IsLocalHom (ψ i))
      -- `rf`, `sf` form directed systems of rings
      (_ : @DirectedSystem Λ instP Rl (fun i j h => ⇑(rf i j h)))
      (_ : @DirectedSystem Λ instP Sl (fun i j h => ⇑(sf i j h)))
      -- the squares commute: `ψ` is a morphism of directed systems
      (hψ : ∀ i j (h : i ≤ j), (ψ j).comp (rf i j h) = (sf i j h).comp (ψ i)),
      -- (1) the colimit of the system `R_λ → S_λ` is equal to `φ : R → S`
      (∃ (eR : Ring.DirectLimit Rl (fun i j h => ⇑(rf i j h)) ≃+* R)
         (eS : Ring.DirectLimit Sl (fun i j h => ⇑(sf i j h)) ≃+* S),
         φ.comp eR.toRingHom = eS.toRingHom.comp (Ring.DirectLimit.map ψ hψ)) ∧
      -- (2) each `R_λ` is essentially of finite type over `ℤ`
      (∀ i, (Int.castRingHom (Rl i)).EssFiniteType) ∧
      -- (3) each `S_λ` is essentially of finite type over `R_λ` (via `ψ_λ`)
      (∀ i, (ψ i).EssFiniteType)
```

## Tag 00QU, a lemma

[Tag 00QU](https://stacks.math.columbia.edu/tag/00QU) in the Stacks Project.

**`exists_colimit_presentation_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Colimit.lean, line 1374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/EssentialFiniteness/Colimit.lean#L1374).

> Let `φ : R → S` be a local homomorphism of local rings
> which is essentially of finite type.  Then `φ` is a filtered colimit of a system
> of local homomorphisms `φ_λ : R_λ → S_λ` of local rings, where each `R_λ` is
> essentially of finite type over `ℤ`, each `S_λ` is essentially of finite type
> over `R_λ`, and for `λ ≤ μ` the map `S_λ ⊗_{R_λ} R_μ → S_μ` realizes `S_μ` as a
> localization of a quotient of `S_λ ⊗_{R_λ} R_μ`.

```lean
theorem exists_colimit_presentation_of_essFiniteType
    (R S : Type) [CommRing R] [CommRing S] [Algebra R S]
    [IsLocalRing R] [IsLocalRing S] (hφ : IsLocalHom (algebraMap R S))
    (hft : Algebra.EssFiniteType R S) :
    ∃ (Λ : Type) (_ : PartialOrder Λ) (_ : IsDirected Λ (· ≤ ·)) (_ : Nonempty Λ)
      (Rf Sf : Λ ⥤ CommRingCat) (φsys : Rf ⟶ Sf),
      -- each `R_λ`, `S_λ` is a local ring
      (∀ i, IsLocalRing (Rf.obj i)) ∧ (∀ i, IsLocalRing (Sf.obj i)) ∧
      -- each `φ_λ` is a local homomorphism
      (∀ i, IsLocalHom (φsys.app i).hom) ∧
      -- each transition map is a local homomorphism
      (∀ (i j : Λ) (h : i ≤ j), IsLocalHom (Rf.map h.hom).hom) ∧
      (∀ (i j : Λ) (h : i ≤ j), IsLocalHom (Sf.map h.hom).hom) ∧
      -- (1) the colimit of the system is `φ : R → S` (up to canonical isomorphism)
      (∃ (iR : colimit Rf ≅ CommRingCat.of R) (iS : colimit Sf ≅ CommRingCat.of S),
        iR.inv ≫ colimMap φsys ≫ iS.hom = CommRingCat.ofHom (algebraMap R S)) ∧
      -- (2) each `R_λ` is essentially of finite type over `ℤ`
      (∀ i, Algebra.EssFiniteType ℤ (Rf.obj i)) ∧
      -- (3) each `S_λ` is essentially of finite type over `R_λ`
      (∀ i, letI : Algebra (Rf.obj i) (Sf.obj i) := (φsys.app i).hom.toAlgebra
        Algebra.EssFiniteType (Rf.obj i) (Sf.obj i)) ∧
      -- (4) for `i ≤ j`, `S_j` is the localization of a quotient of `S_i ⊗_{R_i} R_j`
      (∀ (i j : Λ) (h : i ≤ j), Stacks.EssentialFiniteness.LocalColimit.LocalizationOfQuotient φsys
        h)
```

## Tag 00QV, a lemma

[Tag 00QV](https://stacks.math.columbia.edu/tag/00QV) in the Stacks Project.

**`Stacks.EssentialFiniteness.ColimitPresentation.main_theorem_00qv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/ColimitFinitePresentation/BaseChangeLocalization.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/EssentialFiniteness/ColimitFinitePresentation/BaseChangeLocalization.lean#L599).

> **Stacks Project, Tag 00QV (Lemma 10.127.11).**
>
> Let `φ : R → S` be a local homomorphism of local rings. If `S` is essentially of finite
> presentation over `R` (via `φ`), then `φ` is a filtered colimit of a directed system of local
> homomorphisms `ψ_λ : R_λ → S_λ` between local rings, with local transition maps, such that:
> (1) the colimit of the system is `φ`; (2) each `R_λ` is essentially of finite type over `ℤ`;
> (3) each `ψ_λ` is essentially of finite type; (4) for `λ ≤ μ`, the canonical base-change map
> `S_λ ⊗_{R_λ} R_μ → S_μ` exhibits `S_μ` as a localization of `S_λ ⊗_{R_λ} R_μ` at a prime.

```lean
theorem main_theorem_00qv
    (R S : Type u) [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    (φ : R →+* S) (hφ : IsLocalHom φ)
    (hfp : φ.EssFinitePresentation) :
    ∃ (Λ : Type u) (_ : Preorder Λ) (_ : Nonempty Λ) (_ : IsDirected Λ (· ≤ ·))
      (Robj : Λ → Type u) (Sobj : Λ → Type u)
      (_ : ∀ i, CommRing (Robj i)) (_ : ∀ i, CommRing (Sobj i))
      (_ : ∀ i, IsLocalRing (Robj i)) (_ : ∀ i, IsLocalRing (Sobj i))
      (fR : ∀ i j, i ≤ j → Robj i →+* Robj j)
      (fS : ∀ i j, i ≤ j → Sobj i →+* Sobj j)
      (ψ : ∀ i, Robj i →+* Sobj i)
      (comm : ∀ i j (hij : i ≤ j), (ψ j).comp (fR i j hij) = (fS i j hij).comp (ψ i)),
      -- the transition maps form directed systems of rings
      (DirectedSystem Robj (fun i j h => (fR i j h : Robj i → Robj j))) ∧
      (DirectedSystem Sobj (fun i j h => (fS i j h : Sobj i → Sobj j))) ∧
      -- all transition maps and all `ψ_λ` are local homomorphisms
      (∀ i j (hij : i ≤ j), IsLocalHom (fR i j hij)) ∧
      (∀ i j (hij : i ≤ j), IsLocalHom (fS i j hij)) ∧
      (∀ i, IsLocalHom (ψ i)) ∧
      -- (1) the colimit of the system `R_λ → S_λ` recovers `φ : R → S`
      (∃ (eR : Ring.DirectLimit Robj (fun i j h => (fR i j h : Robj i → Robj j)) ≃+* R)
         (eS : Ring.DirectLimit Sobj (fun i j h => (fS i j h : Sobj i → Sobj j)) ≃+* S),
         φ.comp eR.toRingHom = eS.toRingHom.comp (Ring.DirectLimit.map ψ comm)) ∧
      -- (2) each `R_λ` is essentially of finite type over `ℤ`
      (∀ i, Algebra.EssFiniteType ℤ (Robj i)) ∧
      -- (3) each fiber map `ψ_λ` is essentially of finite type
      (∀ i, (ψ i).EssFiniteType) ∧
      -- (4) each transition map is a localization at a prime after base change
      (∀ i j (hij : i ≤ j),
        IsLocalizationAtPrimeOfBaseChange fR fS ψ comm i j hij)
```

## Tag 00QX, a lemma

[Tag 00QX](https://stacks.math.columbia.edu/tag/00QX) in the Stacks Project.

**`RingHom.EssentiallyOfFinitePresentation.exists_isColimit_essFiniteType_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/ColimitSystem.lean, line 1365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/ColimitSystem.lean#L1365). The attribute's comment: “The system is a pair of functors `A B : Λ ⥤ CommRingCat` with a natural transformation `φ : A ⟶ B`, and a functor `N : Λ ⥤ AddCommGrpCat` with `B.obj i`-module structures compatible with the transition maps; `S_λ ⊗_{R_λ} R_μ` is the pushout in `CommRingCat` and (6) is `IsBaseChange`. Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate; (2) and (3) are Mathlib's `EssFiniteType` (Definition 00QM (1)). The conclusion also asserts that each structure map `ρ_λ : A.obj i → R` is local, which is the source's "system of local homomorphisms of local rings" read as a system in the category of local rings; it is realized by the construction of 00QU and is not implied by (1)–(6). See the module docstring.”.

> **Stacks 00QX.** Let `R → S` be a local homomorphism of local rings which is
> essentially of finite presentation and let `M` be a finitely presented `S`-module. Then
> there are a nonempty directed set `Λ`, a system `φ : A ⟶ B` of local homomorphisms
> `A.obj i → B.obj i` of local rings, and `B.obj i`-modules `N.obj i`, such that (1) the
> colimits of `A`, `B` and `N` are `R`, `S` and `M`, compatibly with `algebraMap R S` and
> with the `S`-action on `M`; (2) each `A.obj i` is essentially of finite type over `ℤ`;
> (3) each `A.obj i → B.obj i` is essentially of finite type; (4) each `N.obj i` is a
> finite `B.obj i`-module; (5) for `i ≤ j` the ring `B.obj j` is a localization of
> `B.obj i ⊗_{A.obj i} A.obj j` at a prime ideal; (6) for `i ≤ j` the transition map
> `N.obj i → N.obj j` exhibits `N.obj j` as the base change of `N.obj i` along
> `B.obj i → B.obj j`. Moreover each structure map `A.obj i → R` of the colimit cocone is
> a local homomorphism, so that each transition map `A.obj i → A.obj j` is local too and
> each `𝔪_{A.obj i}` is the contraction of the maximal ideal of `R`.

```lean
public theorem RingHom.EssentiallyOfFinitePresentation.exists_isColimit_essFiniteType_module
    {R S M : Type u} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)]
    [AddCommGroup M] [Module S M] [Module.FinitePresentation S M]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) :
    ∃ (Λ : Type u) (_ : Preorder Λ) (_ : Nonempty Λ) (_ : IsDirected Λ (· ≤ ·))
      (A B : Λ ⥤ CommRingCat.{u}) (φ : A ⟶ B) (N : Λ ⥤ AddCommGrpCat.{u})
      (_ : ∀ i, Module (B.obj i) (N.obj i))
      (hsmul : ∀ ⦃i j : Λ⦄ (h : i ⟶ j) (b : B.obj i) (m : N.obj i),
        N.map h (b • m) = B.map h b • N.map h m)
      (ρ : A ⟶ (Functor.const Λ).obj (CommRingCat.of R))
      (σ : B ⟶ (Functor.const Λ).obj (CommRingCat.of S))
      (ν : N ⟶ (Functor.const Λ).obj (AddCommGrpCat.of M))
      (_ : IsColimit (Cocone.mk (CommRingCat.of R) ρ))
      (_ : IsColimit (Cocone.mk (CommRingCat.of S) σ))
      (_ : IsColimit (Cocone.mk (AddCommGrpCat.of M) ν)),
      (∀ i, φ.app i ≫ σ.app i = ρ.app i ≫ CommRingCat.ofHom (algebraMap R S)) ∧
      (∀ (i : Λ) (b : B.obj i) (m : N.obj i),
        (ν.app i (b • m) : M) = HSMul.hSMul (α := S) (β := M) (σ.app i b) (ν.app i m)) ∧
      (∀ i, IsLocalRing (A.obj i)) ∧ (∀ i, IsLocalRing (B.obj i)) ∧
      (∀ i, IsLocalHom (φ.app i).hom) ∧
      (∀ i, IsLocalHom (ρ.app i).hom) ∧
      (∀ i, Algebra.EssFiniteType ℤ (A.obj i)) ∧
      (∀ i, (φ.app i).hom.EssFiniteType) ∧
      (∀ i, Module.Finite (B.obj i) (N.obj i)) ∧
      (∀ ⦃i j : Λ⦄ (h : i ⟶ j),
        letI := (pushout.desc (B.map h) (φ.app j) (φ.naturality h).symm).hom.toAlgebra
        ∃ (q : Ideal ↑(pushout (φ.app i) (A.map h))) (_ : q.IsPrime),
          IsLocalization q.primeCompl ↑(B.obj j)) ∧
      (∀ ⦃i j : Λ⦄ (h : i ⟶ j),
        letI : Algebra ↑(B.obj i) ↑(B.obj j) := (B.map h).hom.toAlgebra
        letI : Module ↑(B.obj i) ↑(N.obj j) := Module.compHom _ (B.map h).hom
        letI : IsScalarTower ↑(B.obj i) ↑(B.obj j) ↑(N.obj j) :=
          .of_algebraMap_smul fun _ _ => rfl
        IsBaseChange ↑(B.obj j)
          (⟨(N.map h).hom.toAddHom, hsmul h⟩ :
            ↑(N.obj i) →ₗ[↑(B.obj i)] ↑(N.obj j)))
```

## Tag 00QY, a lemma

[Tag 00QY](https://stacks.math.columbia.edu/tag/00QY) in the Stacks Project.

**`CommRingCat.exists_colimitPresentation_arrow_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ColimitPresentation/FiniteType.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ColimitPresentation/FiniteType.lean#L406). The attribute's comment: “A ring map is an object of `Arrow CommRingCat`, and the source's item (1) is the bundled `Limits.ColimitPresentation Λ X` (diagram, cocone, colimiting), colimits in an arrow category being computed entrywise. The index is the source's nonempty directed poset; Mathlib's `ObjectProperty.ind` form follows from this one. See the module docstring.”.

> **A ring map is a directed colimit of finite type ring maps between `ℤ`-algebras of finite
> type.** Given a ring map `X : R ⟶ S`, there are a nonempty directed poset `Λ` and a diagram of
> ring maps `R_λ ⟶ S_λ` over `Λ`, together with a colimit cocone exhibiting `R ⟶ S` as its
> colimit, such that each `R_λ` is of finite type over `ℤ` and each `R_λ ⟶ S_λ` is of finite
> type.

```lean
public theorem exists_colimitPresentation_arrow_finiteType (X : Arrow CommRingCat.{u}) :
    ∃ (Λ : Type u) (_ : PartialOrder Λ) (_ : IsDirected Λ (· ≤ ·)) (_ : Nonempty Λ)
      (pres : ColimitPresentation Λ X), ∀ i : Λ,
        Algebra.FiniteType ℤ (pres.diag.obj i).left ∧ (pres.diag.obj i).hom.hom.FiniteType
```

## Tag 0BTG, a lemma

[Tag 0BTG](https://stacks.math.columbia.edu/tag/0BTG) in the Stacks Project.

**`integral_isColimit_directed_finite_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Colimit.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/Colimit.lean#L641).

> If `S` is integral over `R`, then the algebra map `R → S` is a filtered colimit of a
> directed system of module-finite ring maps `f_λ : R_λ → S_λ` whose bases `R_λ` are of
> finite type over `ℤ`.

```lean
theorem integral_isColimit_directed_finite_of_finiteType
    (R S : Type) [CommRing R] [CommRing S] [Algebra R S] [Algebra.IsIntegral R S] :
    ∃ D : DirectedRingMapSystem,
      -- (1) Colimit: the colimit of the system equals the structural map `R → S`.
      D.IsColimitEqual (algebraMap R S) ∧
      -- (2) Finite type base: each `R_λ` is of finite type over `Z`.
      (∀ a : D.Λ, Algebra.FiniteType ℤ (D.FR.obj a)) ∧
      -- (3) Module-finite: each `f_λ : R_λ → S_λ` is finite.
      (∀ a : D.Λ, RingHom.Finite (D.f.app a).hom)
```

## Tag 00QZ, a lemma

[Tag 00QZ](https://stacks.math.columbia.edu/tag/00QZ) in the Stacks Project.

**`exists_ringHomDirectedSystem_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FiniteType/Colimit.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FiniteType/Colimit.lean#L430).

> Let `φ : R → S` be a ring map with `S` of finite
> type over `R`.  Then there exist a directed set `(Λ, ≤)` and a system of ring maps
> `φ_λ : R_λ → S_λ` over `Λ` such that:
>
> 1. the colimit of the system recovers `φ : R → S` (there are ring isomorphisms
>    `α : colim R_λ ≅ R`, `β : colim S_λ ≅ S` with `β ∘ (colim φ_λ) = φ ∘ α`);
> 2. each `R_λ` is of finite type over `ℤ`;
> 3. each `φ_λ : R_λ → S_λ` is of finite type;
> 4. for each `λ ≤ μ`, the base-change map `θ_{λμ} : S_λ ⊗_{R_λ} R_μ → S_μ` is
>    surjective.

```lean
theorem exists_ringHomDirectedSystem_of_finiteType
    (R S : Type u) [CommRing R] [CommRing S] (φ : R →+* S)
    (hft : φ.FiniteType) :
    ∃ (Λ : Type u) (_ : Preorder Λ) (_ : IsDirected Λ (· ≤ ·)) (_ : Nonempty Λ)
      (sys : RingHomDirectedSystem Λ),
      -- (1) the colimit recovers `φ : R → S`
      (∃ (α : sys.colimR ≃+* R) (β : sys.colimS ≃+* S),
        (β : sys.colimS →+* S).comp sys.colimφ = φ.comp (α : sys.colimR →+* R)) ∧
      -- (2) each `R_λ` is of finite type over `ℤ`
      (∀ l, (algebraMap ℤ (sys.R l)).FiniteType) ∧
      -- (3) each `φ_λ` is of finite type
      (∀ l, (sys.φ l).FiniteType) ∧
      -- (4) each base-change map `θ_{λμ}` is surjective
      (∀ ⦃i j : Λ⦄ (h : i ≤ j), Function.Surjective (sys.baseChangeMap h))
```

## Tag 00R0, a lemma

[Tag 00R0](https://stacks.math.columbia.edu/tag/00R0) in the Stacks Project.

**`exists_ringMapSystem_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/Colimit.lean, line 961](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/Colimit.lean#L961).

> Let `f : R →+* S` be a ring map with `S` of finite presentation over `R`. Then
> there is a directed index set `Λ` and a system of ring maps `R_λ → S_λ`
> (packaged as `𝓟 : RingMapSystem Λ`) such that:
>
> 1. there are ring isomorphisms `eR : colim R_λ ≃+* R` and `eS : colim S_λ ≃+* S`
>    intertwining the colimit map `colim ψ` with the given map `f`
>    (`f ∘ eR = eS ∘ colim ψ`);
> 2. each `R_λ` is of finite type over `ℤ`;
> 3. each `ψ_λ : R_λ →+* S_λ` is of finite type;
> 4. for each `λ ≤ μ` the base change map `S_λ ⊗_{R_λ} R_μ →+* S_μ` is bijective
>    (an isomorphism of rings).

```lean
theorem exists_ringMapSystem_of_finitePresentation {R S : Type u} [CommRing R] [CommRing S] (f : R
  →+* S)
    (hf : f.FinitePresentation) :
    ∃ (Λ : Type u) (_ : PartialOrder Λ) (_ : Nonempty Λ) (_ : IsDirected Λ (· ≤ ·))
      (𝓟 : RingMapSystem.{u, u} Λ)
      (eR : 𝓟.source.colimit ≃+* R) (eS : 𝓟.target.colimit ≃+* S),
      -- (1) Colimit: the square commutes (`f ∘ eR = eS ∘ colim ψ`).
      (∀ x, f (eR x) = eS (𝓟.colimitMap x)) ∧
      -- (2) Finite type base: each `R_λ` is of finite type over `ℤ`.
      (∀ i, Algebra.FiniteType ℤ (𝓟.source.R i)) ∧
      -- (3) Finite type fibers: each `ψ_λ` is of finite type.
      (∀ i, (𝓟.ψ i).FiniteType) ∧
      -- (4) Cartesian transitions: the base change maps are isomorphisms.
      (∀ ⦃i j : Λ⦄ (hij : i ≤ j), Function.Bijective (𝓟.baseChange hij))
```

## Tag 00R1, a lemma

[Tag 00R1](https://stacks.math.columbia.edu/tag/00R1) in the Stacks Project.

**`Algebra.exists_subring_finiteType_int_isPushout_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/SubringDescent.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ModuleDescent/SubringDescent.lean#L390). The attribute's comment: “Stated as a descent along a single subring `R₀ ⊆ R` of finite type over `ℤ` rather than as a directed system: the six clauses of the source are recovered by taking for `Λ` the subrings of `R` of finite type over `ℤ` containing `R₀` and base changing `S₀` and `M₀` along `R₀ → R_λ`, and conversely the source's system gives such an `R₀` as the image of any `R_λ` in `R`. See the module docstring.”.

> **A finitely presented algebra with a finitely presented module descends to a subring of
> finite type over `ℤ`.** Let `R → S` be of finite presentation and let `M` be a finitely
> presented `S`-module. Then there are a subring `R₀ ⊆ R` of finite type over `ℤ`, an `R₀`-algebra
> `S₀` of finite type and a finite `S₀`-module `M₀`, together with an algebra map `S₀ → S` and an
> `S₀`-linear map `f : M₀ → M`, presenting `S` as `R ⊗_{R₀} S₀` and `M` as `S ⊗_{S₀} M₀`.

```lean
public theorem Algebra.exists_subring_finiteType_int_isPushout_isBaseChange
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S]
    (M : Type v) [AddCommGroup M] [Module S M] [Module.FinitePresentation S M] :
    ∃ (R₀ : Subring R) (S₀ M₀ : Type u) (_ : CommRing S₀) (_ : Algebra R₀ S₀)
      (_ : Algebra S₀ S) (_ : IsScalarTower R₀ S₀ S) (_ : AddCommGroup M₀)
      (_ : Module S₀ M₀) (_ : Module S₀ M) (_ : IsScalarTower S₀ S M) (f : M₀ →ₗ[S₀] M),
      Algebra.FiniteType ℤ R₀ ∧ Algebra.FiniteType R₀ S₀ ∧ Module.Finite S₀ M₀ ∧
        Algebra.IsPushout R₀ R S₀ S ∧ IsBaseChange S f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.127, Tag 00QL](https://stacks.math.columbia.edu/tag/00QL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
