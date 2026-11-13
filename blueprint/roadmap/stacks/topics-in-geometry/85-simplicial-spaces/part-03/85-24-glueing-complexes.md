---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.LocallyGiven, AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_cartesian_summandIdentification, AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_solution, AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_solution_localSerre, AlgebraicGeometry.RingedSite.CoveringGlueing.existsUnique_glueing
statement: formalized
proof: formalized
---

# 85.24 Glueing complexes

Section 85.24 of the Stacks Project, [Tag 0DC8](https://stacks.math.columbia.edu/tag/0DC8). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DC9, a situation

[Tag 0DC9](https://stacks.math.columbia.edu/tag/0DC9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.LocallyGiven`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenDerived.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenDerived.lean#L209).

> Derived objects given locally on a category mapping to a ringed site, with isomorphisms on
> restriction satisfying the cocycle condition: a category `B` with a functor `u : B ⥤ 𝒞`, an object
> `E_U` of `D(𝒪_{u(U)})` for every object `U` of `B`, and an isomorphism
> `ρ_a : E_U|_{𝒞/u(V)} ⟶ E_V` for every arrow `a : V ⟶ U` of `B`, such that
> `ρ_{a ∘ b} = ρ_b ∘ ρ_a|_{𝒞/u(W)}` for composable arrows `b : W ⟶ V` and `a : V ⟶ U`.

```lean
structure LocallyGiven.{uM, u, v, w, uB, vB} (X : RingedSite.{u, v, w})
```

## Tag 0DCA, a lemma

[Tag 0DCA](https://stacks.math.columbia.edu/tag/0DCA) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_cartesian_summandIdentification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenGlueing.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenGlueing.lean#L113).

> **Stacks 0DCA.** In Situation 0DC9, assume the negative self-exts of every `E_U` in
> `D(O_{u(U)})` vanish. Let `L` be a simplicial object of `SR(B)`, let `K = u(L)` and let
> `((C/K)_total, O)` be the ringed site of Remark 0D9W, with `O = a⁻¹O_C`. Then
>
> * there is a cartesian object `E` of `D(O)` whose restriction to `D(O_{C/u(U_{n,i})})` is
>   `E_{U_{n,i}}` compatibly with the isomorphisms `ρ_a` (a
>   `AlgebraicGeometry.RingedSite.LocallyGiven.SummandIdentification`), and
> * such an `E` is unique up to unique isomorphism: for two of them, `(E, σ)` and `(E', σ')`,
>   there is exactly one isomorphism `E ≅ E'` carrying `σ` to `σ'`.

```lean
theorem exists_unique_cartesian_summandIdentification
    (hneg : ∀ (U : G.B) (t : ℤ), 0 < t →
      ∀ g : (shiftFunctor (LocalDerivedCategory.{0} X (G.u.obj U)) t).obj (G.obj U) ⟶ G.obj U,
        g = 0) :
    (∃ E : DerivedCategory ((situation X.J (G.image L)).totalRingedTopos
        (structureSheaf X (G.image L))).Modules,
      (situation X.J (G.image L)).IsCartesianDerivedModule (structureSheaf X (G.image L)) E ∧
        Nonempty (G.SummandIdentification L E)) ∧
    ∀ (E E' : DerivedCategory ((situation X.J (G.image L)).totalRingedTopos
        (structureSheaf X (G.image L))).Modules),
      (situation X.J (G.image L)).IsCartesianDerivedModule (structureSheaf X (G.image L)) E →
      (situation X.J (G.image L)).IsCartesianDerivedModule (structureSheaf X (G.image L)) E' →
      ∀ (σ : G.SummandIdentification L E) (σ' : G.SummandIdentification L E'),
        ∃! ε : E ≅ E', ∀ (n : SimplexCategory) (i : (L.obj (op n)).I),
          (G.summandDerivedRestriction L n i).map
              (((situation X.J (G.image L)).derivedComponentModuleRestriction
                (structureSheaf X (G.image L)) n).map ε.hom) ≫ (σ'.iso n i).hom =
            (σ.iso n i).hom
```

## Tag 0DCB, a lemma

[Tag 0DCB](https://stacks.math.columbia.edu/tag/0DCB) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_solution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenBBDGlueing.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenBBDGlueing.lean#L593).

> **Stacks 0DCB (BBD glueing lemma).** In Situation 0DC9 — a ringed site `(C, O_C)`, a category
> `B` with a functor `u : B ⥤ C`, objects `E_U` of `D(O_{u(U)})` and isomorphisms
> `ρ_a : E_U|_{C/u(V)} ⟶ E_V` satisfying the cocycle condition — assume
>
> 1. `C` has equalizers and fibre products;
> 2. there is a morphism of sites `f : C ⟶ D` given by a continuous functor `u : D ⥤ C` (here
>    `f`, with `IsMorphismOfSites`), such that `D` has equalizers and fibre products and `u`
>    commutes with them, `B` is a full subcategory of `D` (a fully faithful `i : B ⥤ D`) with
>    `u : B ⥤ C` the restriction of `u` (`i ⋙ f = G.u`), and every object of `D` has a covering
>    whose members are objects of `B`;
> 3. for all `U` in `B` all negative self-exts of `E_U` in `D(O_{u(U)})` are zero, that is,
>    every map `E_U[t] ⟶ E_U` with `t > 0` vanishes;
> 4. there exists `t ∈ ℤ` with `H^i(E_U) = 0` for `i < t` and all `U`.
>
> Then there exists a solution `(E, ρ_U)`, and it is unique up to unique isomorphism: between two
> solutions there is exactly one isomorphism compatible with their identifications `ρ_U`.

```lean
theorem exists_unique_solution {X : RingedSite.{u, u, u}} [HasEqualizers X.C] [HasPullbacks X.C]
    (G : LocallyGiven.{0, u, u, u, u, u} X)
    {D : Type u} [SmallCategory D] [HasEqualizers D] [HasPullbacks D] (P : Pretopology D)
    (f : D ⥤ X.C) [IsMorphismOfSites.{u} f P.toGrothendieck X.J]
    [PreservesLimitsOfShape WalkingParallelPair f] [PreservesLimitsOfShape WalkingCospan f]
    (i : G.B ⥤ D) [i.Full] [i.Faithful] (hi : i ⋙ f = G.u)
    (hcover : ∀ V : D, ∃ (ι : Type u) (U : ι → G.B) (g : ∀ k, i.obj (U k) ⟶ V),
      Presieve.ofArrows (fun k ↦ i.obj (U k)) g ∈ P V)
    (hneg : ∀ (U : G.B) (t : ℤ), 0 < t →
      ∀ g : (shiftFunctor (LocalDerivedCategory.{0} X (G.u.obj U)) t).obj (G.obj U) ⟶ G.obj U,
        g = 0)
    (hbound : ∃ t : ℤ, ∀ (U : G.B) (q : ℤ), q < t → IsZero
      ((DerivedCategory.homologyFunctor (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over (G.u.obj U))) q).obj (G.obj U))) :
    Nonempty G.Solution ∧
      ∀ S S' : G.Solution, ∃! e : S.obj ≅ S'.obj, Solution.IsCompatibleIso G e
```

## Tag 0DCC, a lemma

[Tag 0DCC](https://stacks.math.columbia.edu/tag/0DCC) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.LocallyGiven.exists_unique_solution_localSerre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenUnboundedBBDGlueing.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/LocallyGivenUnboundedBBDGlueing.lean#L125).

> The unbounded BBD glueing lemma. In Situation 0DC9 — a ringed site `(C, O_C)`, a category
> `B` with a functor `u : B ⥤ C`, objects `E_U` of `D(O_{u(U)})` and isomorphisms
> `ρ_a : E_U|_{C/u(V)} ⟶ E_V` satisfying the cocycle condition — assume
>
> 1. `C` has equalizers and fibre products;
> 2. there is a morphism of sites `f : C ⟶ D` given by a continuous functor `u : D ⥤ C` (here
>    `f`, with `IsMorphismOfSites`), such that `D` has equalizers and fibre products and `u`
>    commutes with them, `B` is a full subcategory of `D` (a fully faithful `i : B ⥤ D`) with
>    `u : B ⥤ C` the restriction of `u` (`i ⋙ f = G.u`), and every object of `D` has a covering
>    whose members are objects of `B`;
> 3. all negative self-exts of `E_U` in `D(O_{u(U)})` are zero, that is, every map
>    `E_U[t] ⟶ E_U` with `t > 0` vanishes;
> 4. there are weak Serre subcategories `A_U ⊂ Mod(O_U)` for all objects `U` of `C` satisfying
>    conditions 0DC2, 0DC3 and 0DC4 (`T : LocalSerreFamily X`);
> 5. `E_U ∈ D_{A_U}(O_U)`: every cohomology module of `E_U` lies in `A_{u(U)}`.
>
> Then there exists a solution `(E, ρ_U)`, and it is unique up to unique isomorphism: between two
> solutions there is exactly one isomorphism compatible with their identifications `ρ_U`.

```lean
theorem exists_unique_solution_localSerre {X : RingedSite.{u, u, u}} [HasEqualizers X.C]
    [HasPullbacks X.C] (G : LocallyGiven.{0, u, u, u, u, u} X)
    {D : Type u} [SmallCategory D] [HasEqualizers D] [HasPullbacks D] (P : Pretopology D)
    (f : D ⥤ X.C) [IsMorphismOfSites.{u} f P.toGrothendieck X.J]
    [PreservesLimitsOfShape WalkingParallelPair f] [PreservesLimitsOfShape WalkingCospan f]
    (i : G.B ⥤ D) [i.Full] [i.Faithful] (hi : i ⋙ f = G.u)
    (hcover : ∀ V : D, ∃ (ι : Type u) (U : ι → G.B) (g : ∀ k, i.obj (U k) ⟶ V),
      Presieve.ofArrows (fun k ↦ i.obj (U k)) g ∈ P V)
    (hneg : ∀ (U : G.B) (t : ℤ), 0 < t →
      ∀ g : (shiftFunctor (LocalDerivedCategory.{0} X (G.u.obj U)) t).obj (G.obj U) ⟶ G.obj U,
        g = 0)
    (T : LocalSerreFamily.{u} X)
    (hA : ∀ (U : G.B) (q : ℤ), T.A (G.u.obj U)
      ((DerivedCategory.homologyFunctor (SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over (G.u.obj U))) q).obj (G.obj U))) :
    Nonempty G.Solution ∧
      ∀ S S' : G.Solution, ∃! e : S.obj ≅ S'.obj, Solution.IsCompatibleIso G e
```

## Tag 0GMG, a lemma

[Tag 0GMG](https://stacks.math.columbia.edu/tag/0GMG) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.CoveringGlueing.existsUnique_glueing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CoveringGlueing/Glueing.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/CoveringGlueing/Glueing.lean#L315).

> Let `(C, O_C)` be a ringed site with fibre products and `{U_i ⟶ X}_{i ∈ I}` a covering in
> `C`. For `i ∈ I` let `E_i` be an object of `D(O_{U_i})` and for `i, j ∈ I` let
> `ρ_{ij} : E_i|_{C/U_{ij}} ⟶ E_j|_{C/U_{ij}}` be an isomorphism in `D(O_{U_{ij}})`, where
> `U_{ij} = U_i ×_X U_j`. Assume
>
> 1. the `ρ_{ij}` satisfy the cocycle condition on `U_i ×_X U_j ×_X U_k` for all `i, j, k ∈ I`,
> 2. `SheafExt^p_{O_{U_i}}(E_i, E_i) = 0` for all `p < 0` and `i ∈ I` (stated as the vanishing of
>    the negative self-exts of `E_i|_{C/V}` for every object `V` over `U_i`), and
> 3. there exists a `t ∈ ℤ` such that `H^p(E_i) = 0` for `p < t` and all `i ∈ I`.
>
> Then there exists a pair `(E, ρ_i)`, with `E` an object of `D(O_X)` and `ρ_i : E|_{U_i} ⟶ E_i`
> isomorphisms in `D(O_{U_i})` compatible with the `ρ_{ij}`, and it is unique: two such pairs are
> isomorphic by exactly one isomorphism compatible with the `ρ_i`.

```lean
theorem existsUnique_glueing {X : RingedSite.{u, u, u}} [hX : HasPullbacks X.C] {X₀ : X.C}
    {ι : Type u} {U : ι → X.C} (f : ∀ i, U i ⟶ X₀) (E : ∀ i, LocalDerivedCategory.{0} X (U i))
    (ρ : ∀ i j, (derivedOverMap.{0} X (pullback.fst (f i) (f j))).obj (E i) ≅
      (derivedOverMap.{0} X (pullback.snd (f i) (f j))).obj (E j))
    (hf : Sieve.generate (Presieve.ofArrows U f) ∈ X.J X₀)
    (hρ : IsCocycle f ρ)
    (hExt : ∀ (i : ι) {V : X.C} (a : V ⟶ U i) (n : ℤ), n < 0 →
      Subsingleton (DerivedCategory.Ext ((derivedOverMap.{0} X a).obj (E i))
        ((derivedOverMap.{0} X a).obj (E i)) n))
    (hBound : ∃ t : ℤ, ∀ (i : ι) (n : ℤ), n < t →
      IsZero ((DerivedCategory.homologyFunctor _ n).obj (E i))) :
    Nonempty (Glueing f E ρ) ∧
      ∀ A B : Glueing f E ρ, ∃! e : A.obj ≅ B.obj, ∀ i : ι,
        (derivedOverMap.{0} X (f i)).map e.hom ≫ (B.iso i).hom = (A.iso i).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.24, Tag 0DC8](https://stacks.math.columbia.edu/tag/0DC8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
