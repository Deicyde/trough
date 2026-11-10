---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finiteEtale_model, AlgebraicGeometry.exists_finiteEtale_hom_model, AlgebraicGeometry.eventually_eq_of_finiteEtaleBaseChange_eq, AlgebraicGeometry.etaleFundamentalGroup_homeomorph_compatibleFamilies, AlgebraicGeometry.connectedSpace_pullback_specMap_algebraMap_perfectClosure, AlgebraicGeometry.connectedSpace_and_etaleFundamentalGroupMap_perfectClosure, AlgebraicGeometry.connectedSpace_of_connectedSpace_pullback_specMap_algebraMap, AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_isAlgClosed
statement: formalized
proof: formalized
---

# 58.14 Geometric and arithmetic fundamental groups

Section 58.14 of the Stacks Project, [Tag 0BTU](https://stacks.math.columbia.edu/tag/0BTU). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BTV, a lemma

[Tag 0BTV](https://stacks.math.columbia.edu/tag/0BTV) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean#L233). The attribute's comment: “equivalence of categories: every finite étale cover of the limit comes from a stage”.

> **Every finite étale cover of the limit comes from a stage.** A scheme finite étale over the
> limit of a cofiltered inverse system of quasi-compact and quasi-separated schemes with affine
> transition morphisms is isomorphic, as a cover of the limit, to the base change of a scheme finite
> étale over one of the stages.

```lean
theorem exists_finiteEtale_model (hc : IsLimit c) (Y : FiniteEtaleOver c.pt) :
    ∃ (j : I) (B : FiniteEtaleOver (D.obj j)),
      Nonempty (Y ≅ (finiteEtaleBaseChange (c.π.app j)).obj B)
```

**`AlgebraicGeometry.exists_finiteEtale_hom_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean#L314). The attribute's comment: “equivalence of categories: every morphism over the limit comes from a stage”.

> **Every morphism of finite étale covers over the limit comes from a stage.** A morphism between
> the base changes to the limit of two finite étale covers of a stage is, after transport along the
> comparison isomorphism `AlgebraicGeometry.finiteEtaleLimitCompIso`, the base change of a morphism
> of the base changes of those covers to some later stage.

```lean
theorem exists_finiteEtale_hom_model (hc : IsLimit c) (i : I) (A B : FiniteEtaleOver (D.obj i))
    (ψ : (finiteEtaleBaseChange (c.π.app i)).obj A ⟶
      (finiteEtaleBaseChange (c.π.app i)).obj B) :
    ∃ (j : I) (e : j ⟶ i)
      (χ : (finiteEtaleBaseChange (D.map e)).obj A ⟶ (finiteEtaleBaseChange (D.map e)).obj B),
      ψ = (finiteEtaleLimitCompIso D c e).hom.app A
        ≫ (finiteEtaleBaseChange (c.π.app j)).map χ
        ≫ (finiteEtaleLimitCompIso D c e).inv.app B
```

**`AlgebraicGeometry.eventually_eq_of_finiteEtaleBaseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleOverLimit.lean#L365). The attribute's comment: “equivalence of categories: morphisms agreeing over the limit agree at a later stage”.

> **Morphisms of finite étale covers agreeing over the limit agree at a later stage.** Two
> morphisms of finite étale covers of a stage whose base changes along the projection of the cone
> agree are already equal after base change to some later stage.

```lean
theorem eventually_eq_of_finiteEtaleBaseChange_eq (hc : IsLimit c) (i : I)
    (A B : FiniteEtaleOver (D.obj i)) (f g : A ⟶ B)
    (h : (finiteEtaleBaseChange (c.π.app i)).map f
      = (finiteEtaleBaseChange (c.π.app i)).map g) :
    ∃ (j : I) (e : j ⟶ i),
      (finiteEtaleBaseChange (D.map e)).map f = (finiteEtaleBaseChange (D.map e)).map g
```

**`AlgebraicGeometry.etaleFundamentalGroup_homeomorph_compatibleFamilies`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FundamentalGroupOfLimit.lean, line 866](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FundamentalGroupOfLimit.lean#L866). The attribute's comment: “π₁(X, x̄) = lim π₁(Xᵢ, x̄) for a connected cofinal tail”.

> **Stacks Project, Tag 0BTV, second conclusion: `π₁(X, x̄) = lim π₁(Xᵢ, x̄)`.** Let `D` be a
> cofiltered inverse system of quasi-compact and quasi-separated schemes with affine transition
> morphisms, let `c` be a limit cone on it, so that `c.pt` is `X = lim Xᵢ`, and suppose that the
> schemes of the cofinal tail `Over i₀` are connected. Then for a geometric point `x` of `X` the
> scheme `X` is connected, the compatible families of elements of the fundamental groups of the
> stages of the tail form a topological group, and the canonical map is an isomorphism of
> topological groups onto it: every coordinate of the isomorphism is the homomorphism induced by
> the corresponding projection of the cone.

```lean
theorem etaleFundamentalGroup_homeomorph_compatibleFamilies {I : Type u} [Category.{u} I]
    [IsCofiltered I] (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (e : i ⟶ j), IsAffineHom (D.map e)]
    [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i₀ : I) [hconn : ∀ j : Over i₀, ConnectedSpace (D.obj j.left)]
    (x : GeometricPoint c.pt) :
    ∃ hX : ConnectedSpace c.pt,
      letI : ConnectedSpace c.pt := hX
      ∃ hGroup : Group
          {σ : ∀ j : Over i₀, EtaleFundamentalGroup (D.obj j.left) (x.map (c.π.app j.left)) //
            CompatibleFundamentalGroupFamily D c i₀ x σ},
        letI := hGroup
        ∃ hTopGroup : IsTopologicalGroup
            {σ : ∀ j : Over i₀, EtaleFundamentalGroup (D.obj j.left) (x.map (c.π.app j.left)) //
              CompatibleFundamentalGroupFamily D c i₀ x σ},
          letI := hTopGroup
          ∃ e : EtaleFundamentalGroup c.pt x ≃ₜ*
              {σ : ∀ j : Over i₀, EtaleFundamentalGroup (D.obj j.left) (x.map (c.π.app j.left)) //
                CompatibleFundamentalGroupFamily D c i₀ x σ},
            ∀ (σ : EtaleFundamentalGroup c.pt x) (j : Over i₀),
              (e σ).1 j = @etaleFundamentalGroupMap _ _ hX (hconn j) (c.π.app j.left) x σ
```

## Tag 0BTW, a lemma

[Tag 0BTW](https://stacks.math.columbia.edu/tag/0BTW) in the Stacks Project.

**`AlgebraicGeometry.connectedSpace_pullback_specMap_algebraMap_perfectClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PerfectionBaseChange.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PerfectionBaseChange.lean#L68). The attribute's comment: “the assertion that `X_{k^{perf}}` is connected; the asserted isomorphism `π₁(X_{k^{perf}}) → π₁(X)` is not proved here”.

> **The connectedness half of Stacks Project, Tag 0BTW.** For a field `k` with perfection
> `kperf` and a connected scheme `X` over `k`, the base change `X_{kperf}` is connected.
>
> The perfection is purely inseparable over `k`, so this is
> `AlgebraicGeometry.connectedSpace_pullback_specMap_algebraMap`.

```lean
theorem connectedSpace_pullback_specMap_algebraMap_perfectClosure (k kperf : Type u) [Field k]
    [Field kperf] [Algebra k kperf] (p : ℕ) [ExpChar k p] [ExpChar kperf p]
    [PerfectRing kperf p] [IsPerfectClosure (algebraMap k kperf) p] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [ConnectedSpace ↥X] :
    ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kperf))))
```

**`AlgebraicGeometry.connectedSpace_and_etaleFundamentalGroupMap_perfectClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PerfectionFundamentalGroup.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PerfectionFundamentalGroup.lean#L57). The attribute's comment: “both assertions: `X_{k^{perf}}` is connected, and the canonical map `π₁(X_{k^{perf}}) → π₁(X)` is an isomorphism of topological groups”.

> **Stacks Project, Tag 0BTW.** Let `k` be a field with perfection `kperf` and let `X` be a
> connected scheme over `k`. Then `X_{kperf} = X ×_{Spec k} Spec kperf` is connected, and for every
> geometric point `x` of `X_{kperf}` the map `π₁(X_{kperf}, x) → π₁(X, x)` induced by the
> projection is an isomorphism of topological groups.

```lean
theorem connectedSpace_and_etaleFundamentalGroupMap_perfectClosure (k kperf : Type u) [Field k]
    [Field kperf] [Algebra k kperf] (p : ℕ) [ExpChar k p] [ExpChar kperf p]
    [PerfectRing kperf p] [IsPerfectClosure (algebraMap k kperf) p] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [ConnectedSpace ↥X] :
    ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kperf)))) ∧
      ∀ x : GeometricPoint (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kperf)))),
        haveI := connectedSpace_pullback_specMap_algebraMap_perfectClosure k kperf p f
        ∃ e : EtaleFundamentalGroup _ x ≃ₜ*
            EtaleFundamentalGroup X (x.map (pullback.fst f _)),
          ∀ σ, e σ = etaleFundamentalGroupMap (pullback.fst f _) x σ
```

## Tag 0BTX, a lemma

[Tag 0BTX](https://stacks.math.columbia.edu/tag/0BTX) in the Stacks Project.

**`AlgebraicGeometry.connectedSpace_of_connectedSpace_pullback_specMap_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean#L76). The attribute's comment: “connectedness of `X`, implicit in the statement since `π₁(X)` appears in it”.

> If the base change of a scheme `X` over `k` to a field extension `Ω` is connected, then so is
> `X`.

```lean
theorem connectedSpace_of_connectedSpace_pullback_specMap_algebraMap
    (k Ω : Type u) [Field k] [Field Ω] [Algebra k Ω] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k Ω))))] :
    ConnectedSpace ↥X
```

**`AlgebraicGeometry.etaleFundamentalGroupMap_comp_eq_one_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean#L171). The attribute's comment: “triviality of the composite `π₁(X_k̄) → π₁(X) → π₁(Spec k)`”. References: SGA 1 XIII (4.0), “vu = 1”.

> For a field `k` with an
> algebraically closed extension `Ω`, a scheme `X` over `k` whose base change `X_Ω` is connected,
> and a geometric point `x` of `X_Ω`, the composite
>
> ```
> π₁(X_Ω, x) ⟶ π₁(X, x) ⟶ π₁(Spec k, x)
> ```
>
> is the trivial homomorphism.

```lean
theorem etaleFundamentalGroupMap_comp_eq_one_isAlgClosed
    (k Ω : Type u) [Field k] [Field Ω] [Algebra k Ω] [IsAlgClosed Ω]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k Ω))))]
    (x : GeometricPoint (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k Ω))))) :
    letI : ConnectedSpace ↥X := connectedSpace_of_connectedSpace_pullback_specMap_algebraMap k Ω f
    (etaleFundamentalGroupMap f
          (x.map (pullback.fst f
            (Spec.map (CommRingCat.ofHom (algebraMap k Ω)))))).toMonoidHom.comp
        (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k Ω)))) x).toMonoidHom = 1
```

**`AlgebraicGeometry.surjective_etaleFundamentalGroupMap_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/AlgebraicClosureBaseChange.lean#L315). The attribute's comment: “surjectivity of `π₁(X) → π₁(Spec k)`”. References: SGA 7 I (5.2), “surjectivity of π₁(X_η”.

> For a field `k` with an algebraically closed
> extension `Ω`, a scheme `X` over `k` whose base change `X_Ω` is connected, and a geometric point
> `x` of `X`, the induced homomorphism
>
> ```
> π₁(X, x) ⟶ π₁(Spec k, x)
> ```
>
> is surjective.

```lean
theorem surjective_etaleFundamentalGroupMap_isAlgClosed
    (k Ω : Type u) [Field k] [Field Ω] [Algebra k Ω] [IsAlgClosed Ω]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k Ω))))]
    (x : GeometricPoint X) :
    letI : ConnectedSpace ↥X := connectedSpace_of_connectedSpace_pullback_specMap_algebraMap k Ω f
    Function.Surjective (etaleFundamentalGroupMap f x)
```

**`AlgebraicGeometry.shortExact_etaleFundamentalGroupMap_isAlgClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GeometricArithmeticExactSequence.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GeometricArithmeticExactSequence.lean#L388). The attribute's comment: “the full short exact sequence: injectivity, exactness in the middle, surjectivity”. References: SGA 1 IX (6.1), “special case”; SGA 1 XIII (4.4), “special case”; SGA 7 I (5.2), “more general”.

> **Stacks Project, Tag 0BTX.** Let `k` be a field with algebraic closure `k̄`, and `X` a
> quasi-compact and quasi-separated scheme over `k` whose base change `X_{k̄}` is connected. Then
> `X` is connected
> (`AlgebraicGeometry.connectedSpace_of_connectedSpace_pullback_specMap_algebraMap`), and for a
> geometric point `x` of `X_{k̄}` the sequence of continuous homomorphisms of étale fundamental
> groups
>
> ```
> 1 → π₁(X_{k̄}, x) → π₁(X, x) → π₁(Spec k, x) → 1
> ```
>
> induced by the projection `X_{k̄} ⟶ X` and the structure morphism `X ⟶ Spec k` is exact. The
> first map is injective, its image is the kernel of the second, and the second is surjective. The
> three groups are profinite (`AlgebraicGeometry.isProfiniteTop_etaleFundamentalGroup`).
>
> The proof is described in the module docstring.

```lean
theorem shortExact_etaleFundamentalGroupMap_isAlgClosure (k kbar : Type u) [Field k]
    [Field kbar] [Algebra k kbar] [IsAlgClosure k kbar] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [CompactSpace X] [QuasiSeparatedSpace X]
    [ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))]
    (x : GeometricPoint (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) :
    letI : ConnectedSpace ↥X :=
      connectedSpace_of_connectedSpace_pullback_specMap_algebraMap k kbar f
    Function.Injective (etaleFundamentalGroupMap
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x) ∧
      (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x).toMonoidHom.range =
        (etaleFundamentalGroupMap f (x.map (pullback.fst f
          (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))))).toMonoidHom.ker ∧
      Function.Surjective (etaleFundamentalGroupMap f
        (x.map (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))))
```

**`AlgebraicGeometry.topologicalShortExact_etaleFundamentalGroupMap_isAlgClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GeometricFundamentalExactSequence.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GeometricFundamentalExactSequence.lean#L404). References: SGA 1 XIII (4.0), “vu = 1”; SGA 1 XIII (4.4), “special case”.

> **Stacks Project, Tag 0BTX.** Let `k` be a field with algebraic closure `k̄` and let `X` be a
> quasi-compact and quasi-separated scheme over `k` whose base change `X_k̄` is connected. Then `X`
> is connected (`AlgebraicGeometry.connectedSpace_of_connectedSpace_pullback_specMap_algebraMap`)
> and, for a geometric point `x` of `X_k̄`,
>
> ```
> 1 → π₁(X_k̄, x) → π₁(X, x) → π₁(Spec k, x) → 1
> ```
>
> is a short exact sequence of profinite topological groups: the first map is injective and a
> closed embedding, its image is the kernel of the second, and the second is surjective and a
> quotient map. Both maps are the continuous homomorphisms induced by the projection
> `X_k̄ ⟶ X` and the structure morphism `X ⟶ Spec k`; the three groups carry their profinite
> topologies (`AlgebraicGeometry.etaleFundamentalGroupCompactSpace` and its companions).

```lean
theorem topologicalShortExact_etaleFundamentalGroupMap_isAlgClosure (k kbar : Type u) [Field k]
    [Field kbar] [Algebra k kbar] [IsAlgClosure k kbar] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [CompactSpace X] [QuasiSeparatedSpace X]
    [ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))]
    (x : GeometricPoint (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) :
    letI : ConnectedSpace ↥X :=
      connectedSpace_of_connectedSpace_pullback_specMap_algebraMap k kbar f
    Function.Injective (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x) ∧
      Topology.IsClosedEmbedding (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x) ∧
      (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x).toMonoidHom.range =
        (etaleFundamentalGroupMap f
          (x.map (pullback.fst f
            (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))))).toMonoidHom.ker ∧
      Function.Surjective (etaleFundamentalGroupMap f
          (x.map (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))))) ∧
      Topology.IsQuotientMap (etaleFundamentalGroupMap f
          (x.map (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.14, Tag 0BTU](https://stacks.math.columbia.edu/tag/0BTU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
