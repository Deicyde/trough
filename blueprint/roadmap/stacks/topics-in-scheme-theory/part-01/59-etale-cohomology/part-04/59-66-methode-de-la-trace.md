---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.mono_etaleModuleCohomology_map_unit_of_finiteEtale, Stacks.EtaleCohomology.isZero_etaleModuleCohomology_of_finiteEtale, AlgebraicGeometry.moduleTrace_app_eq_sum_of_cover, AlgebraicGeometry.eq_moduleTrace_app_of_sum, AlgebraicGeometry.unit_comp_moduleTrace_eq_nsmul, AlgebraicGeometry.abelianTrace, AlgebraicGeometry.moduleTrace, Stacks.EtaleCohomology.exists_primeToEll_finiteEtale_constantFiltration_unconditional
statement: formalized
proof: formalized
---

# 59.66 Méthode de la trace

Section 59.66 of the Stacks Project, [Tag 03SH](https://stacks.math.columbia.edu/tag/03SH). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03SH, the section

[Tag 03SH](https://stacks.math.columbia.edu/tag/03SH) in the Stacks Project.

**`Stacks.EtaleCohomology.mono_etaleModuleCohomology_map_unit_of_finiteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceCohomology.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceCohomology.lean#L78). The attribute's comment: “the méthode de la trace: H^n(X, F) → H^n(Y, f⁻¹F) is injective when multiplication by the degree is an isomorphism of F”. References: SGA 5 IIIB (3.2), “partial”.

> **Stacks 03SH, the méthode de la trace.** For `f : T ⟶ S` finite étale of degree `d` and a
> sheaf of `Λ`-modules `F` on which multiplication by `d` is an isomorphism, the map
> `H^n(S, F) ⟶ H^n(T, f⁻¹ F)` — induced by the restriction `F ⟶ f_* f⁻¹ F`, followed by the
> identification `H^n(S, f_* f⁻¹ F) = H^n(T, f⁻¹ F)` — is injective: the restriction has a left
> inverse, the trace divided by `d`.

```lean
theorem mono_etaleModuleCohomology_map_unit_of_finiteEtale [IsIso (d • 𝟙 F)] (n : ℕ) :
    Mono (((etaleModuleGlobalSections.{u, r} Λ S).rightDerived n).map
        ((etaleModuleInverseImageAdj.{u, r} Λ f).unit.app F) ≫
      (etaleModuleCohomologyDirectImageIsoOfIsIntegralHom Λ f n
        ((etaleModuleInverseImage.{u, r} Λ f).obj F)).hom)
```

**`Stacks.EtaleCohomology.isZero_etaleModuleCohomology_of_finiteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceCohomology.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceCohomology.lean#L96). The attribute's comment: “if H^q(Y, f⁻¹F) = 0 then H^q(X, F) = 0, when multiplication by the degree is an isomorphism of F”.

> **Stacks 03SH, the vanishing consequence of the méthode de la trace.** For `f : T ⟶ S` finite
> étale of degree `d` and a sheaf of `Λ`-modules `F` on which multiplication by `d` is an
> isomorphism, `H^q(T, f⁻¹ F) = 0` implies `H^q(S, F) = 0`.

```lean
theorem isZero_etaleModuleCohomology_of_finiteEtale [IsIso (d • 𝟙 F)] (q : ℕ)
    (h : IsZero (((etaleModuleGlobalSections.{u, r} Λ T).rightDerived q).obj
      ((etaleModuleInverseImage.{u, r} Λ f).obj F))) :
    IsZero (((etaleModuleGlobalSections.{u, r} Λ S).rightDerived q).obj F)
```

**`AlgebraicGeometry.moduleTrace_app_eq_sum_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean#L142). The attribute's comment: “if Y is a disjoint union of copies of the base, the trace is the sum map, for sheaves of Λ-modules”.

> **Stacks 03SH, the trace on a split cover is the sum map.** If over the étale object `Q` of
> `T` the morphism `f` is described by the pairwise disjoint morphisms `φ i : Q ⟶ T'` whose graphs
> cover `Q ×_T T'`, so that `(f_* f^{-1} ℱ)(Q) = ℱ(Q ×_T T') = ⨁ᵢ ℱ(Q)`, then the trace sends a
> section to the sum of its restrictions to the sheets `φ i`, each read on `Q`.

```lean
theorem moduleTrace_app_eq_sum_of_cover
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (ModuleCat.{max (u + 1) v} Λ))
    (Q : SmallEtale B T.1 T.property) {ι : Type u} [Fintype ι]
    (φ : ι → (Q ⟶ SmallEtale.ofEtaleHom B f))
    (hcov : ∀ z : ((smallEtaleBaseChange B (SmallEtale.ofEtaleHom B f).obj.hom).obj Q).obj.left.1,
      ∃ i, z ∈ Set.range (B.inclusion.map
        (smallEtaleLiftGraph B T.1 T.property (SmallEtale.ofEtaleHom B f) Q (φ i)).hom.left))
    (hd : Pairwise (fun i j => smallEtaleArrowsDisjoint B T.1 T.property
      (SmallEtale.ofEtaleHom B f) Q (φ i) (φ j)))
    (s : F.obj.obj (op ((smallEtalePostcompose B T.1 T.property (SmallEtale.ofEtaleHom B f)).obj
      ((smallEtaleBaseChange B (SmallEtale.ofEtaleHom B f).obj.hom).obj Q)))) :
    ((moduleTrace B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).app F).hom.app (op Q) s =
      ∑ i, F.obj.map (smallEtaleLiftPostIso B T.1 T.property (SmallEtale.ofEtaleHom B f) Q
        (φ i)).inv.op
        (((moduleRestriction B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).obj F).obj.map
          (smallEtaleLiftGraph B T.1 T.property (SmallEtale.ofEtaleHom B f) Q (φ i)).op s)
```

**`AlgebraicGeometry.eq_moduleTrace_app_of_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean#L210). The attribute's comment: “the trace is characterized by being the sum map étale locally on the base, for sheaves of Λ-modules”.

> **Stacks 03SH, the trace is characterized by the sum formula.** A morphism
> `τ : f_* f^{-1} ℱ ⟶ ℱ` which, over every étale neighbourhood `Q` on which `f` is a disjoint union
> of copies of `Q` (pairwise disjoint sheets `φ i : Q ⟶ T'` whose graphs cover `Q ×_T T'`), sends a
> section to the sum of its restrictions to the sheets is the trace: such neighbourhoods cover `T`
> (Stacks 04HN), and two morphisms of sheaves agreeing on a covering agree.

```lean
theorem eq_moduleTrace_app_of_sum
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (ModuleCat.{max (u + 1) v} Λ))
    (τ : (B.smallPushforward f (ModuleCat.{max (u + 1) v} Λ)).obj
      ((moduleRestriction B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).obj F) ⟶ F)
    (hτ : ∀ (Q : SmallEtale B T.1 T.property) {ι : Type u} [Fintype ι]
      (φ : ι → (Q ⟶ SmallEtale.ofEtaleHom B f)),
      (∀ z : ((smallEtaleBaseChange B (SmallEtale.ofEtaleHom B f).obj.hom).obj Q).obj.left.1,
        ∃ i, z ∈ Set.range (B.inclusion.map
          (smallEtaleLiftGraph B T.1 T.property (SmallEtale.ofEtaleHom B f) Q (φ i)).hom.left)) →
      Pairwise (fun i j => smallEtaleArrowsDisjoint B T.1 T.property
        (SmallEtale.ofEtaleHom B f) Q (φ i) (φ j)) →
      ∀ s : F.obj.obj (op ((smallEtalePostcompose B T.1 T.property (SmallEtale.ofEtaleHom B f)).obj
        ((smallEtaleBaseChange B (SmallEtale.ofEtaleHom B f).obj.hom).obj Q))),
      τ.hom.app (op Q) s =
        ∑ i, F.obj.map (smallEtaleLiftPostIso B T.1 T.property (SmallEtale.ofEtaleHom B f) Q
          (φ i)).inv.op
          (((moduleRestriction B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).obj F).obj.map
            (smallEtaleLiftGraph B T.1 T.property (SmallEtale.ofEtaleHom B f) Q (φ i)).op s)) :
    τ = (moduleTrace B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).app F
```

**`AlgebraicGeometry.unit_comp_moduleTrace_eq_nsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/ModuleTraceDegree.lean#L257). The attribute's comment: “restriction followed by the trace is multiplication by the degree, for sheaves of Λ-modules”. References: SGA 4 XVII (6.2.3), “Var 4 (normalization)”; SGA 4 XVIII (2.9), “Var 4 (I)”.

> **Stacks 03SH, the trace of a finite étale morphism of degree `d` on sheaves of modules.**
> For `f` finite étale and finite locally free of rank `d`, the restriction map `ℱ ⟶ f_* f^{-1} ℱ`
> (the unit of `f^{-1} ⊣ f_*`) followed by the trace `f_* f^{-1} ℱ ⟶ ℱ` of Definition 03SE is
> multiplication by `d`.

```lean
theorem unit_comp_moduleTrace_eq_nsmul (d : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank (B.inclusion.map f) d]
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (ModuleCat.{max (u + 1) v} Λ)) :
    (smallEtalePostcomposePushforwardAdjunction B f
        (ModuleCat.{max (u + 1) v} Λ)).unit.app F ≫
        (moduleTrace B T.1 T.property (SmallEtale.ofEtaleHom B f) Λ).app F = d • 𝟙 F
```

## Tag 03SE, a definition

[Tag 03SE](https://stacks.math.columbia.edu/tag/03SE) in the Stacks Project.

**`AlgebraicGeometry.abelianTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Trace.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Trace.lean#L114). The attribute's comment: “abelian sheaves”.

> **Stacks 03SE.** The trace map of the finite étale morphism `U ⟶ X` on abelian étale
> sheaves: the counit `j_!j^{-1} ⟶ id` of the extension-by-zero adjunction, read as a map
> `j_*j^{-1} ⟶ id` through the comparison isomorphism `j_! ≅ j_*` of Stacks 03S7.

```lean
public def abelianTrace :
    let := smallEtaleBaseChange_isContinuous B U.obj.hom
    abelianRestriction B X hX U ⋙
        (smallEtaleBaseChange B U.obj.hom).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B X hX)
          (SmallEtale.topology B U.obj.left.1 U.obj.left.property) ⟶
      𝟭 (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.moduleTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Trace.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZeroBaseChange/Trace.lean#L216). The attribute's comment: “sheaves of modules”.

> **Stacks 03SE.** The trace map of the finite étale morphism `U ⟶ X` on étale sheaves of
> `Λ`-modules, constructed exactly as in the abelian case.

```lean
public def moduleTrace :
    let := smallEtaleBaseChange_isContinuous B U.obj.hom
    moduleRestriction B X hX U Λ ⋙
        (smallEtaleBaseChange B U.obj.hom).sheafPushforwardContinuous
          (ModuleCat.{max (u + 1) v} Λ)
          (SmallEtale.topology B X hX)
          (SmallEtale.topology B U.obj.left.1 U.obj.left.property) ⟶
      𝟭 (Sheaf (SmallEtale.topology B X hX) (ModuleCat.{max (u + 1) v} Λ))
```

## Tag 0A3R, a lemma

[Tag 0A3R](https://stacks.math.columbia.edu/tag/0A3R) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_primeToEll_finiteEtale_constantFiltration_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PrimeToEllCover.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PrimeToEllCover.lean#L806).

> **Stacks Project, Tag 0A3R.** Let `S` be a connected scheme, let `ℓ` be a prime number and
> let `F` be a finite type locally constant sheaf of `F_ℓ`-vector spaces on `S_étale`. Then there
> is a finite étale morphism `f : T → S` of degree prime to `ℓ` such that `f⁻¹F` has a finite
> filtration whose successive quotients are the constant sheaf `Z/ℓZ_T`.
>
> The filtration is a chain of subobjects of `f⁻¹F` running from the zero subobject to the whole
> sheaf, each step having the constant sheaf as its quotient. The local constancy of `F` enters
> through the dictionary of Tag 0DV5 (3), which is
> `Stacks.EtaleCohomology.nonempty_fundamentalGroupFGModuleDictionary`.
>
> The dictionary is read at a geometric point, which the statement does not mention: a connected
> space is nonempty, and `AlgebraicGeometry.GeometricPoint.ofPoint` puts a geometric point of `S`
> above any of its points, so one is produced inside the proof rather than assumed. `NeZero ℓ`,
> which the dictionary needs for the finiteness of `F_ℓ[K]`, comes from the primality of `ℓ`
> likewise.

```lean
theorem exists_primeToEll_finiteEtale_constantFiltration_unconditional {ℓ : ℕ} (hℓ : ℓ.Prime)
    {S : Scheme.{u}} [ConnectedSpace S]
    (F : Sheaf (smallEtaleTopology S) (ModuleCat.{max (u + 1) v} (ZMod ℓ)))
    (_hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant (ZMod ℓ) (smallEtaleTopology S) F) :
    ∃ (T : Scheme.{u}) (f : T ⟶ S) (d : ℕ), IsFinite f ∧ Etale f ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d ∧ ¬ ℓ ∣ d ∧
      ∃ X : RelSeries (ConstantRankOneStep ℓ ((smallEtalePullbackZMod ℓ f).obj F)),
        IsZero (Subobject.underlying.obj X.head) ∧ IsIso X.last.arrow
```

**`Stacks.EtaleCohomology.exists_primeToEll_finiteEtale_relSeries_constantRankOneStep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PrimeToEllFiltration.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PrimeToEllFiltration.lean#L389).

> **Stacks Project, Tag 0A3R.** Let `S` be a connected scheme, `ℓ` a prime number and `F` a
> finite type locally constant sheaf of `F_ℓ`-vector spaces on `S_étale`. Then there is a finite
> étale morphism `f : T → S` of degree prime to `ℓ` such that `f⁻¹F` has a finite filtration
> whose successive quotients are isomorphic to `Z/ℓZ_T`.
>
> The filtration is a chain of subobjects of `f⁻¹F` running from the zero subobject to the whole
> sheaf, each step having the constant sheaf `Z/ℓZ_T` as its quotient.

```lean
theorem exists_primeToEll_finiteEtale_relSeries_constantRankOneStep {ℓ : ℕ} (hℓ : ℓ.Prime)
    {S : Scheme.{u}} [ConnectedSpace S]
    (F : Sheaf S.smallEtaleTopology (ModuleCat.{u + 1} (ZMod ℓ)))
    (hF : IsFiniteTypeLocallyConstant (ZMod ℓ) S.smallEtaleTopology F) :
    ∃ (T : Scheme.{u}) (f : T ⟶ S) (d : ℕ), IsFinite f ∧ Etale f ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d ∧ ¬ ℓ ∣ d ∧
      ∃ X : RelSeries (ConstantRankOneStep.{0} ℓ ((smallEtalePullbackZMod.{0} ℓ f).obj F)),
        IsZero (Subobject.underlying.obj X.head) ∧ IsIso X.last.arrow
```

## Tag 0GIZ, a lemma

[Tag 0GIZ](https://stacks.math.columbia.edu/tag/0GIZ) in the Stacks Project.

**`Module.exists_relSeries_trivial_action_subquotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PGroupFiltration.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/PGroupFiltration.lean#L384). References: SGA 5 I (App.1.3.1), “trivial action quotients”.

> A module over the group ring of a finite `ℓ`-group, annihilated by a power of `ℓ`,
> has a finite filtration by group-ring submodules with trivial group action on every successive
> quotient.

```lean
theorem Module.exists_relSeries_trivial_action_subquotient
    (Λ H M : Type*) [CommRing Λ] [Group H] [Finite H]
    (ℓ n : ℕ) (hℓ : ℓ.Prime) (hH : IsPGroup ℓ H)
    [AddCommGroup M] [Module (MonoidAlgebra Λ H) M]
    (hM : ∀ x : M, (ℓ ^ n) • x = 0) :
    ∃ X : RelSeries {p : Submodule (MonoidAlgebra Λ H) M ×
        Submodule (MonoidAlgebra Λ H) M |
      p.1 ≤ p.2 ∧ ∀ (g : H) (x : p.2),
        MonoidAlgebra.single g (1 : Λ) • (x : M) - x ∈ p.1},
      X.head = ⊥ ∧ X.last = ⊤
```

## Tag 0GJ0, a lemma

[Tag 0GJ0](https://stacks.math.columbia.edu/tag/0GJ0) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_primeToEll_finiteEtale_finiteModuleFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/ConstantModuleFiltration.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/ConstantModuleFiltration.lean#L563). The attribute's comment: “granted hypothesis D, the Stacks 0GIY dictionary in finite-module form”.

> **Stacks Project, Tag 0GJ0.** Let `S` be an irreducible, geometrically unibranch scheme, let
> `ℓ` be a prime number, let `n ≥ 1`, let `Λ` be a Noetherian ring and let `F` be a finite type
> locally constant sheaf of `Λ`-modules on `S_étale` annihilated by `ℓ ^ n`. Then there is a finite
> étale morphism `f : T → S` of degree prime to `ℓ` such that `f⁻¹F` has a finite filtration whose
> successive quotients are of the form `M_T` for finite `Λ`-modules `M`.
>
> The filtration is a chain of subobjects of `f⁻¹F` running from the zero subobject to the whole
> sheaf, each step having the constant sheaf of a finite `Λ`-module as its quotient.
>
> The irreducibility and geometric unibranchness of `S` and the local constancy of `F` are the
> hypotheses under which the dictionary `D` of Stacks Tag 0GIY is available. The annihilation of `F`
> by `ℓ ^ n` is stated twice: on the sections of `F`, as `_hann`, because the source states it there,
> and on the module the dictionary attaches to `F`, as the field `D.annihilated`, because that is the
> form Tag 0GIZ consumes. Transporting the first to the second is part of Tag 0GIY and so is part of
> what `D` carries; nothing here derives one from the other.

```lean
theorem exists_primeToEll_finiteEtale_finiteModuleFiltration {ℓ n : ℕ} (hℓ : ℓ.Prime)
    (_hn : 1 ≤ n) {Λ : Type v} [CommRing Λ] [IsNoetherianRing Λ]
    {S : Scheme.{u}} [IrreducibleSpace S] (_hS : IsGeometricallyUnibranch S)
    (s : GeometricPoint S)
    (F : Sheaf (smallEtaleTopology S) (ModuleCat.{max (u + 1) v} Λ))
    (_hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant Λ (smallEtaleTopology S) F)
    (_hann : ∀ (U : S.Etale) (x : F.obj.obj (Opposite.op U)), (ℓ ^ n) • x = 0)
    (D : FiniteModuleMonodromyDictionary Λ ℓ n s F) :
    ∃ (T : Scheme.{u}) (f : T ⟶ S) (d : ℕ), IsFinite f ∧ Etale f ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d ∧ ¬ ℓ ∣ d ∧
      ∃ X : RelSeries (ConstantFiniteModuleStep Λ
          ((smallEtalePullbackModuleCat Λ f).obj F)),
        IsZero (Subobject.underlying.obj X.head) ∧ IsIso X.last.arrow
```

**`Stacks.EtaleCohomology.exists_primeToEll_finiteEtale_finiteModuleFiltration_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/ConstantModuleFiltrationUnconditional.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/ConstantModuleFiltrationUnconditional.lean#L234).

> **Stacks Project, Tag 0GJ0.** Let `S` be an irreducible, geometrically unibranch scheme, let
> `ℓ` be a prime number, let `n ≥ 1`, let `Λ` be a Noetherian ring and let `F` be a finite type
> locally constant sheaf of `Λ`-modules on `S_étale` annihilated by `ℓ ^ n`. Then there is a finite
> étale morphism `f : T → S` of degree prime to `ℓ` such that `f⁻¹F` has a finite filtration whose
> successive quotients are of the form `M_T` for finite `Λ`-modules `M`.
>
> The filtration is a chain of subobjects of `f⁻¹F` running from the zero subobject to the whole
> sheaf, each step having the constant sheaf of a finite `Λ`-module as its quotient. The degree of
> `f` is the rank of the finite locally free morphism `f` (Tag 02KA).

```lean
theorem exists_primeToEll_finiteEtale_finiteModuleFiltration_general {ℓ n : ℕ} (hℓ : ℓ.Prime)
    (_hn : 1 ≤ n) {Λ : Type v} [CommRing Λ] [IsNoetherianRing Λ]
    {S : Scheme.{u}} [IrreducibleSpace S] (hS : IsGeometricallyUnibranch S)
    (s : GeometricPoint S)
    (F : Sheaf (smallEtaleTopology S) (ModuleCat.{max (u + 1) v} Λ))
    (hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant Λ (smallEtaleTopology S) F)
    (hann : ∀ (U : S.Etale) (x : F.obj.obj (Opposite.op U)), (ℓ ^ n) • x = 0) :
    ∃ (T : Scheme.{u}) (f : T ⟶ S) (d : ℕ), IsFinite f ∧ Etale f ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d ∧ ¬ ℓ ∣ d ∧
      ∃ X : RelSeries (ConstantFiniteModuleStep Λ
          ((smallEtalePullbackModuleCat Λ f).obj F)),
        IsZero (Subobject.underlying.obj X.head) ∧ IsIso X.last.arrow
```

**`Stacks.EtaleCohomology.exists_finiteEtale_primeToEll_constantModuleFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/UnibranchConstantModuleFiltration.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/MethodeDeLa/UnibranchConstantModuleFiltration.lean#L275). The attribute's comment: “the filtration after a finite étale cover of degree prime to ℓ, for S irreducible and geometrically unibranch”.

> **Stacks, Tag 0GJ0.** Let `S` be an irreducible, geometrically unibranch scheme, let `ℓ` be a
> prime number and `n ≥ 1`, let `Λ` be a Noetherian ring and let `F` be a finite type, locally
> constant sheaf of `Λ`-modules on `S_étale` annihilated by `ℓ ^ n`. Then there is a finite étale
> morphism `f : T ⟶ S` of degree `d` prime to `ℓ` such that `f⁻¹ F` has a finite filtration whose
> successive quotients are of the form `M̲_T` for finite `Λ`-modules `M`.
>
> The filtration is a chain of subobjects of `f⁻¹ F` from the zero subobject to the whole sheaf,
> each step having the constant sheaf of a finite `Λ`-module as its quotient. The degree is the
> rank `d` of `f` as a finite locally free morphism.
>
> **The unibranch hypothesis of the source is necessary**: it cannot be dropped even for `S`
> irreducible (a fortiori it cannot be replaced by connectedness). Let
> `S` be the nodal cubic over an algebraically closed field `k`: it is irreducible but not
> geometrically unibranch at the node, and its étale fundamental group is `ℤ̂`. It is `ℙ¹_k` with
> `0` and `∞` glued, and the infinite chain of copies of `ℙ¹_k`, the `i`-th glued at `∞` to
> the `(i+1)`-st at `0`, is an étale covering `S̃ ⟶ S` with deck group `ℤ`. Let
> `Λ = 𝔽_ℓ[t, t⁻¹]`, a Noetherian domain annihilated by `ℓ`, and let `F = S̃ ×^ℤ Λ` be the sheaf of
> `Λ`-modules obtained by letting the generator of `ℤ` act on `Λ` by multiplication by `t`. It is
> locally constant (constant on `S̃`), of finite type (stalks `Λ`) and annihilated by `ℓ`. For
> every finite étale `f : T ⟶ S` and every connected component `T₀` of `T` (a cycle of `m ≥ 1`
> copies of `ℙ¹_k`), the pullback of `S̃` to `T₀` is the `ℤ`-cover with monodromy `m`, so
> `Γ(T₀, f⁻¹ F) = {v ∈ Λ | t ^ m v = v} = 0`, `t ^ m - 1` being a nonzero divisor. A constant
> subsheaf `M̲_{T₀}` of `f⁻¹ F|_{T₀}` therefore has `M ⊆ Γ(T₀, M̲) = 0`; by induction along a
> filtration with constant successive quotients every term restricted to `T₀` is `0`, while
> `f⁻¹ F|_{T₀}` has stalks `Λ ≠ 0`. So the conclusion fails for every finite étale `f`.

```lean
theorem exists_finiteEtale_primeToEll_constantModuleFiltration {ℓ n : ℕ} (hℓ : ℓ.Prime)
    (_hn : 1 ≤ n) {Λ : Type r} [CommRing Λ] [IsNoetherianRing Λ]
    {S : Scheme.{u}} [IrreducibleSpace S] (hS : IsGeometricallyUnibranch S)
    (F : EtaleModules.{u, r} Λ S)
    (hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant Λ S.smallEtaleTopology F)
    (hann : ∀ (U : S.Etale) (y : F.obj.obj (op U)), (ℓ ^ n) • y = 0) :
    ∃ (T : Scheme.{u}) (f : T ⟶ S) (d : ℕ), IsFinite f ∧ Etale f ∧
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d ∧ ¬ ℓ ∣ d ∧
      ∃ X : RelSeries (ConstantFiniteModuleStep Λ ((etaleModuleInverseImage.{u, r} Λ f).obj F)),
        IsZero (Subobject.underlying.obj X.head) ∧ IsIso X.last.arrow
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.66, Tag 03SH](https://stacks.math.columbia.edu/tag/03SH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
