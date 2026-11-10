---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.IsFlat, Stacks.SheafOfModules.flat_stalk_of_isFlat, AlgebraicGeometry.SheafOfModules.isFlat_iff_stalk_flat, AlgebraicGeometry.SheafOfModules.IsFlatAt, Stacks.SheafOfModules.modulePullback_isFlat, Stacks.SheafOfModules.FlatColimits.isFlat_colimit, Stacks.SheafOfModules.FlatColimits.isFlat_coproduct, AlgebraicGeometry.SheafOfModules.isFlat_jShriek_unit
statement: formalized
proof: formalized
---

# 17.17 Flat modules

Section 17.17 of the Stacks Project, [Tag 05NC](https://stacks.math.columbia.edu/tag/05NC). 11 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05ND, a definition

[Tag 05ND](https://stacks.math.columbia.edu/tag/05ND) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean#L285). The attribute's comment: “the definition: F is flat when G ↦ G ⊗_{O_X} F is exact”. References: SGA 4 V (1.1), “commutative case”.

> A sheaf of modules is flat when tensoring on the right with it is an exact
> endofunctor on sheaves of modules.
>
> This is part (3) of tag 03ER for the native tensor bifunctor, and part (4) just below
> is stated in terms of it. `Stacks.SheafOfModules.IsFlat` uses the same native tensor
> functor.

```lean
abbrev IsFlat {O : Sheaf J CommRingCat.{w}}
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}]
    [HasWeakSheafify J AddCommGrpCat.{z}]
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) : Prop
```

## Tag 05NE, a lemma

[Tag 05NE](https://stacks.math.columbia.edu/tag/05NE) in the Stacks Project.

**`Stacks.SheafOfModules.flat_stalk_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorDeterminantInvertible.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorDeterminantInvertible.lean#L625). The attribute's comment: “flat implies stalkwise flat, for a ringed space, in the `structureSheafRing` spelling”.

> **Tag 05NE, in the spellings the determinant development uses.** A flat sheaf of modules on
> a ringed space has flat stalks, for the module structure
> `Stacks.SheafOfModules.stalkModule`.
>
> The content is `AlgebraicGeometry.SheafOfModules.isFlat_iff_stalk_flat`; what this adds is that
> the index `structureSheafRing Y` of the determinant development is
> `Stacks.SheafOfModules.Tensor.ringSheaf Y.sheaf`, and that
> `Stacks.SheafOfModules.stalkModule` is the module structure that theorem's statement supplies
> by `inferInstanceAs`. Both hold by `rfl`, but the universe arguments of
> `AlgebraicGeometry.SheafOfModules.IsFlat` are not determined by `F` alone, so they are written
> out; this is the spelling Tag 08BL uses as well.

```lean
theorem flat_stalk_of_isFlat {Y : RingedSpace.{u, u}}
    (F : _root_.SheafOfModules.{u} (structureSheafRing Y))
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := Y.sheaf) F)
    (x : Y) :
    @Module.Flat _ _ _ _ (Stacks.SheafOfModules.stalkModule F x)
```

**`AlgebraicGeometry.SheafOfModules.isFlat_iff_stalk_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Flat/Stalk.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Flat/Stalk.lean#L78).

> A module sheaf on a ringed space is flat precisely when each of its
> stalks is flat over the corresponding stalk of the structure sheaf.

```lean
public theorem isFlat_iff_stalk_flat {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u})
    (F : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} O)) :
    IsFlat F ↔
      ∀ x : X,
        letI : Module (TopCat.Presheaf.stalk (C := CommRingCat.{u}) (X := X) O.obj x)
          (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) (X := X) F.val.presheaf x) :=
          inferInstanceAs (Module (TopCat.Presheaf.stalk (C := CommRingCat.{u}) (X := X) O.obj x)
          (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) (X := X)
              ((id F.val : _root_.PresheafOfModules.{u}
                (O.obj ⋙ forget₂ CommRingCat.{u} RingCat.{u})).presheaf) x))
        Module.Flat (TopCat.Presheaf.stalk (C := CommRingCat.{u}) (X := X) O.obj x)
          (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) (X := X) F.val.presheaf x)
```

## Tag 05NF, a definition

[Tag 05NF](https://stacks.math.columbia.edu/tag/05NF) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.IsFlatAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Flat/AtPoint.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Flat/AtPoint.lean#L42).

> An `𝒪_X`-module `F` on a ringed space `X` is *flat at* `x : X` if its stalk `F_x` is a flat
> `𝒪_{X,x}`-module.

```lean
noncomputable def IsFlatAt {X : RingedSpace.{u}}
    (F : _root_.SheafOfModules.{u} ((sheafCompose (Opens.grothendieckTopology X)
      (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf))
    (x : X) : Prop
```

## Tag 0H97, a lemma

[Tag 0H97](https://stacks.math.columbia.edu/tag/0H97) in the Stacks Project.

**`Stacks.SheafOfModules.modulePullback_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/FlatPullback.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/FlatPullback.lean#L47). References: SGA 4 V (1.7.1), “ringed spaces”.

> Pullback along a morphism of ringed spaces preserves flat sheaves of modules.

```lean
theorem modulePullback_isFlat {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : _root_.SheafOfModules.{u} (structureSheafRing Y))
    (hG : AlgebraicGeometry.SheafOfModules.IsFlat
      (J := Opens.grothendieckTopology Y.carrier) (O := Y.sheaf) G) :
    AlgebraicGeometry.SheafOfModules.IsFlat
      (J := Opens.grothendieckTopology X.carrier) (O := X.sheaf)
      ((modulePullback f).obj G)
```

## Tag 05NG, a lemma

[Tag 05NG](https://stacks.math.columbia.edu/tag/05NG) in the Stacks Project.

**`Stacks.SheafOfModules.FlatColimits.isFlat_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean#L225). The attribute's comment: “filtered_colimits_flat”.

> **Stacks Project, Tag 03EU part (2), filtered colimits.** A filtered colimit of flat
> sheaves of modules is flat.

```lean
theorem isFlat_colimit {O : Sheaf J CommRingCat.{w}}
    {I : Type z} [Category.{z} I] [IsFiltered I]
    (F : I ⥤ _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∀ i, IsFlat (F.obj i)) :
    IsFlat (colimit F)
```

**`Stacks.SheafOfModules.FlatColimits.isFlat_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatColimits.lean#L241). The attribute's comment: “direct_sums_flat”.

> **Stacks Project, Tag 03EU part (2), direct sums.** An arbitrary direct sum of flat sheaves
> of modules is flat. An arbitrary coproduct is the filtered colimit of its finite subcoproducts,
> so this follows from the finite case `isFlat_coproduct_finite` and the filtered-colimit case
> `isFlat_colimit`.

```lean
theorem isFlat_coproduct {O : Sheaf J CommRingCat.{w}} {ι : Type z}
    (F : ι → _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hF : ∀ i, IsFlat (F i)) :
    IsFlat (∐ F)
```

## Tag 05NH, a lemma

[Tag 05NH](https://stacks.math.columbia.edu/tag/05NH) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.isFlat_jShriek_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ExtensionByZero/Flat.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ExtensionByZero/Flat.lean#L169).

> **Stacks 05NH.** The extension by zero of the structure sheaf of an open subset of a ringed
> space is a flat sheaf of modules.

```lean
theorem isFlat_jShriek_unit {X : TopCat.{u}} (U : Opens X)
    (O : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}) :
    IsFlat.{u, u, u, u} (O := O)
      ((ExtensionByZeroModules.jShriek U (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} O)).obj
        (_root_.SheafOfModules.unit
          (ExtensionByZeroModules.resRing U
            (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} O))))
```

## Tag 05NI, a lemma

[Tag 05NI](https://stacks.math.columbia.edu/tag/05NI) in the Stacks Project.

**`Stacks.SheafOfModules.exists_epi_from_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ExtensionByZero/Flat.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ExtensionByZero/Flat.lean#L222). The attribute's comment: “part (2)”.

> **Stacks 05NI, part (2).** Every sheaf of modules on a ringed space is a quotient of a flat
> sheaf of modules: the explicit cover of part (1) is a direct sum of extensions by zero of
> structure sheaves, each flat by Stacks 05NH, and a direct sum of flat sheaves is flat.

```lean
theorem exists_epi_from_flat {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u})
    (F : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} O)) :
    ∃ (P : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} O))
        (f : P ⟶ F),
      IsFlat.{u, u, u, u} (O := O) P ∧ Epi f
```

**`Stacks.SheafOfModules.exists_epi_from_coproduct_jShriek_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/FlatCover.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorAndDuals/FlatCover.lean#L66). The attribute's comment: “part (1)”.

> **Stacks 05NI, part (1).** Every sheaf of modules is a quotient of a coproduct of extensions
> by zero of structure sheaves on open subspaces.

```lean
theorem exists_epi_from_coproduct_jShriek_unit :
    ∃ (I : Type u) (U : I → Opens X),
      ∃ f : (∐ fun i : I =>
        (ExtensionByZeroModules.jShriek (U i) O).obj
          (_root_.SheafOfModules.unit (ExtensionByZeroModules.resRing (U i) O))) ⟶ F,
        Epi f
```

## Tag 05NJ, a lemma

[Tag 05NJ](https://stacks.math.columbia.edu/tag/05NJ) in the Stacks Project.

**`Stacks.SheafOfModules.FlatCover.sheafTensorRight_shortExact_of_isFlat_X₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCoverTensorExactness.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatCoverTensorExactness.lean#L385). The attribute's comment: “ringed spaces, as the special case of a general site”.

> **Stacks Project, Tag 03EX, sheaf case.** If the final term of a short exact sequence of
> sheaves of modules is flat, tensoring the sequence with any sheaf of modules gives a short exact
> sequence.
>
> This is `shortExact_map_sheafTensorFlipObj` with the composite-is-zero witness carried
> explicitly, so that the statement does not mention the zero-morphism-preservation instance of
> the tensor functor.
>
> Taking the site to be the site of opens of a topological space and `O` its structure sheaf,
> this is **Stacks Tag 05NJ**: a short exact sequence `0 → ℱ'' → ℱ' → ℱ → 0` of `𝒪_X`-modules on
> a ringed space with `ℱ` flat stays short exact after `- ⊗_{𝒪_X} 𝒢`.

```lean
theorem sheafTensorRight_shortExact_of_isFlat_X₃
    (O : Sheaf J CommRingCat.{w})
    (S : ShortComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O)))
    (G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf O))
    (hS : S.ShortExact)
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := O) S.X₃) :
    ∃ h : ((Stacks.SheafOfModules.Tensor.sheafTensor O).flip.obj G).map S.f ≫
        ((Stacks.SheafOfModules.Tensor.sheafTensor O).flip.obj G).map S.g = 0,
      (ShortComplex.mk (((Stacks.SheafOfModules.Tensor.sheafTensor O).flip.obj G).map S.f)
        (((Stacks.SheafOfModules.Tensor.sheafTensor O).flip.obj G).map S.g) h).ShortExact
```

## Tag 05NK, a lemma

[Tag 05NK](https://stacks.math.columbia.edu/tag/05NK) in the Stacks Project.

**`Stacks.SheafOfModules.FlatShortExact.isFlat_middle_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatShortExactSequence.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatShortExactSequence.lean#L737). The attribute's comment: “(1)”. References: SGA 1 IV (1.1), “(ii) M' flat => M flat”.

> **Statement 1** (Stacks Tag 05NK, extension of flat modules is flat).  Given a short
> exact sequence `0 → F₂ → F₁ → F₀ → 0` of sheaves of `O_X`-modules (encoded as a short
> complex `S` in the abelian category `SheafOfModules (structureSheafRing X)` together with the
> hypothesis `S.ShortExact`), if `S.X₁ = F₂` and `S.X₃ = F₀` are flat then the middle term
> `S.X₂ = F₁` is flat.
>
> PROOF.  By `isFlat_iff_stalkModule_flat` it suffices to show, for each `x`, that
> the canonical stalk module `(S.X₂)_x` is flat.  By `stalkShortExact` we have a
> short exact sequence of `O_{X,x}`-modules `0 → (S.X₁)_x → (S.X₂)_x → (S.X₃)_x → 0`.
> By hypotheses `h₂, h₀` (via `isFlat_iff_stalkModule_flat`) the outer modules are
> flat, so `Module.Flat.of_shortExact_extension` gives flatness of the middle.

```lean
theorem isFlat_middle_of_shortExact
    (S : ShortComplex (SheafOfModules (structureSheafRing X)))
    (hS : S.ShortExact) (h₂ : IsFlat S.X₁) (h₀ : IsFlat S.X₃) :
    IsFlat S.X₂
```

**`Stacks.SheafOfModules.FlatShortExact.isFlat_sub_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatShortExactSequence.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatShortExactSequence.lean#L764). The attribute's comment: “(2)”. References: SGA 1 IV (1.1), “(ii) M flat => M' flat”; SGA 4 XVII (4.1.1), “(i), ringed space”.

> **Statement 2** (Stacks Tag 05NK, kernel of an epimorphism of flat modules is flat).
> Given a short exact sequence `0 → F₂ → F₁ → F₀ → 0` of sheaves of `O_X`-modules (encoded as
> a short complex `S` with `S.ShortExact`), if `S.X₂ = F₁` and `S.X₃ = F₀` are flat then the
> left term `S.X₁ = F₂` is flat.
>
> PROOF.  By `isFlat_iff_stalkModule_flat` it suffices to show `(S.X₁)_x` is flat for
> each `x`.  By `stalkShortExact` we have the short exact sequence of stalk modules
> `0 → (S.X₁)_x → (S.X₂)_x → (S.X₃)_x → 0`; by `h₁, h₀` the modules `(S.X₂)_x` and
> `(S.X₃)_x` are flat, so `Module.Flat.of_shortExact_kernel` gives flatness of
> `(S.X₁)_x`.

```lean
theorem isFlat_sub_of_shortExact
    (S : ShortComplex (SheafOfModules (structureSheafRing X)))
    (hS : S.ShortExact) (h₁ : IsFlat S.X₂) (h₀ : IsFlat S.X₃) :
    IsFlat S.X₁
```

## Tag 05NL, a lemma

[Tag 05NL](https://stacks.math.columbia.edu/tag/05NL) in the Stacks Project.

**`Stacks.SheafOfModules.FlatResolution.acyclic_map_sheafTensorRight_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatResolution/TensorExactness.lean#L140). The attribute's comment: “ringed spaces, as the special case of a general site”. References: EGA IV (2.1.10), “Absolute case f = id”.

> **Stacks 03EZ, sheaf case.** An exact `ℕ`-indexed complex of sheaves of modules all of
> whose terms are flat stays exact after tensoring with an arbitrary sheaf of modules.
>
> This is also **Stacks 05NL**, the same statement for a ringed space: a ringed space is the
> ringed site of its lattice of opens, its `O_X`-modules are the sheaves of modules over the
> structure ring sheaf of that site, and the tensor product is `sheafTensorRight`.  The
> site-level statement is recorded against the ringed-space tag for the same reason that the
> site-level flatness of Stacks 03ER(3) is recorded against Stacks 05ND in
> `StacksFrontier/CategoryTheory/Sites/Modules/Flat.lean`.

```lean
theorem acyclic_map_sheafTensorRight_of_isFlat
    (K : ChainComplex
      (_root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℕ)
    (hK : K.Acyclic)
    (hflat : ∀ i, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (K.X i))
    (G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) :
    ((Functor.mapHomologicalComplex
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} R).flip.obj G)
      (ComplexShape.down ℕ)).obj K).Acyclic
```

## Tag 08BK, a lemma

[Tag 08BK](https://stacks.math.columbia.edu/tag/08BK) in the Stacks Project.

**`Stacks.FlatEquationalCriterion.exists_local_factorization_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquationalCriterion.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatEquationalCriterion.lean#L259).

> **Stacks Project Tag 08BK (Modules, Lemma 17.17.11).**
>
> Let `(X, O_X)` be a ringed space and `F` a flat `O_X`-module. Let `U ⊆ X` be open, `n ∈ ℕ`,
> `f₁, …, fₙ ∈ O_X(U)` and `s₁, …, sₙ ∈ F(U)` such that the diagram
> `O_U → O_U^{⊕n} → F|_U` is a complex, i.e. `∑ᵢ fᵢ • sᵢ = 0` in `F(U)`.
>
> Then for every `x ∈ U` there exist an open neighbourhood `V ⊆ U` of `x`, an integer `m`,
> sections `t₁, …, t_m ∈ F(V)` and scalars `a_{ji} ∈ O_X(V)` such that:
>   - (Factorization)  `sᵢ|_V = ∑ⱼ a_{ji} • t_j`   for every `i`;
>   - (Annihilation)   `∑ᵢ a_{ji} • fᵢ|_V = 0`      for every `j`.

```lean
theorem exists_local_factorization_of_isFlat {X : AlgebraicGeometry.RingedSpace.{u}}
  (M : OXModule X) (hM : M.IsFlat)
    (U : Opens X) (n : ℕ) (f : Fin n → OSections X U) (s : Fin n → M.sheaf.obj (op U))
    (hcomplex : ∑ i, f i • s i = 0)
    (x : X) (hx : x ∈ U) :
    ∃ (V : Opens X) (_ : x ∈ V) (iVU : V ≤ U) (m : ℕ)
      (t : Fin m → M.sheaf.obj (op V)) (a : Fin m → Fin n → OSections X V),
      (∀ i, M.res iVU (s i) = ∑ j, a j i • t j) ∧
      (∀ j, ∑ i, a j i • Ores X iVU (f i) = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.17, Tag 05NC](https://stacks.math.columbia.edu/tag/05NC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
