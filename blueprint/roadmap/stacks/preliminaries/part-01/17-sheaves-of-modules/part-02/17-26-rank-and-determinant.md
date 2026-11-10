---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.rankDecomposition, Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge, Stacks.SheafOfModules.TopWedge.isIso_determinantTensorDeterminantHom, Stacks.SheafOfModules.TopWedge.eq_determinantTensorDeterminantHom, Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree, Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantHom, Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIso, Stacks.SheafOfModules.TopWedge.detComparison_wedge
statement: formalized
proof: formalized
---

# 17.26 Rank and determinant

Section 17.26 of the Stacks Project, [Tag 0B37](https://stacks.math.columbia.edu/tag/0B37). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B37, the section

[Tag 0B37](https://stacks.math.columbia.edu/tag/0B37) in the Stacks Project.

**`Stacks.SheafOfModules.rankDecomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RankDecomposition.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RankDecomposition.lean#L186). The attribute's comment: “the locally constant rank and the clopen rank decomposition X = X_0 ⊔ X_1 ⊔ … with E finite locally free of rank i on X_i; the exact category Vect(X) and its K-group, the rank homomorphism K_0(Vect(X)) → Map_cont(X, Z), the invertible sheaf det(E) and the homomorphism det : K_0(Vect(X)) → Pic(X) are not covered”. References: EGA 0 (5.4.1), “partial”.

> **Stacks Project, Tag 0B37: the rank decomposition.** A finite locally free sheaf of modules
> `E` on a ringed space whose structure stalks are all nonzero has locally constant rank, so the
> loci `X_i` where the rank is `i` are open and closed, pairwise disjoint and cover `X`, and `E` is
> finite locally free of rank `i` on `X_i`.

```lean
theorem rankDecomposition :
    IsLocallyConstant (⇑(finiteLocallyFreeRank F hO)) ∧
      (∀ i : ℕ, IsClopen (rankStratum F hO i : Set X)) ∧
      Pairwise (Function.onFun Disjoint fun i : ℕ => (rankStratum F hO i : Set X)) ∧
      (⨆ i : ℕ, rankStratum F hO i) = ⊤ ∧
      ∀ (i : ℕ) (x : X), x ∈ rankStratum F hO i →
        ∃ (V : Opens X) (_ : x ∈ V) (_ : V ≤ rankStratum F hO i) (I : Type u),
          Nonempty (I ≃ Fin i) ∧ Nonempty (_root_.SheafOfModules.free.{u} I ≅ F.over V)
```

## Tag 0B38, a lemma

[Tag 0B38](https://stacks.math.columbia.edu/tag/0B38) in the Stacks Project.

**`Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean#L591). The attribute's comment: “the WEDGE-AND-LIFT FORMULA in the GENERAL case, with no constant-rank hypothesis”.

> **The wedge-and-lift formula for the comparison between determinant summands**, in every
> pair of degrees, read inside `⋀ⁿ⁺ᵐ E` through the inclusion of the degree-`n+m` summand of
> `det(E)`.
>
> This is the wedge-and-lift formula of [Stacks, Tag 0B38] in the general case: a short exact
> sequence of finite locally free sheaves with no constant-rank hypothesis. On the summand
> `det(E')ₙ ⊗ det(E'')ₘ` of `det(E') ⊗ det(E'')` the canonical map of
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantHom` carries the image of
> `(s₁∧⋯∧sₙ) ⊗ (g(l₁)∧⋯∧g(lₘ))` to `f(s₁)∧⋯∧f(sₙ)∧l₁∧⋯∧lₘ`, for **arbitrary** local lifts `lⱼ`.
> This is the formula the source gives for its canonical map, and
> `Stacks.SheafOfModules.TopWedge.eq_determinantTensorDeterminantHom` and
> `Stacks.SheafOfModules.TopWedge.eq_detTensorAnnComparison` say it determines the map.

```lean
theorem detSummandComparison_ι_unit_wedge
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E''] (n m : ℕ)
    (V : (Opens ↥X)ᵒᵖ)
    (w : ToType ((A'.exteriorAnnihilator n).toSheafOfModules.val.obj V))
    (s : Fin n → E'.val.obj V)
    (hw : (A'.exteriorAnnihilator n).ι.val.app V w = wedgeSec A' V n s)
    (z : ToType ((A''.exteriorAnnihilator m).toSheafOfModules.val.obj V))
    (l : Fin m → E.val.obj V)
    (hz : (A''.exteriorAnnihilator m).ι.val.app V z =
      wedgeSec A'' V m fun i => g.val.app V (l i)) :
    (detSummandComparison A' A A'' f g hfg hS n m ≫
          (A.exteriorAnnihilator (n + m)).ι).val.app V
        ((PresheafOfModules.tensorSheafUnit (A'.exteriorAnnihilator n).toSheafOfModules
          (A''.exteriorAnnihilator m).toSheafOfModules).app V (w ⊗ₜ z)) =
      wedgeSec A V (n + m) (Fin.append (fun i => f.val.app V (s i)) l)
```

**`Stacks.SheafOfModules.TopWedge.isIso_determinantTensorDeterminantHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean#L990). The attribute's comment: “the ISOMORPHISM clause in the GENERAL case: the canonical map det(E')⊗det(E'')⟶det(E) of `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantHom` is an isomorphism, for a short exact sequence of finite locally free sheaves with NO constant-rank hypothesis. Here det is the det of 0FJN. The isomorphism itself is `determinantTensorDeterminantIsoOfFiniteLocallyFree`”.

> **Stacks 0B38: the canonical map `det(E') ⊗ det(E'') ⟶ det(E)` is an isomorphism**, for a
> short exact sequence `0 → E' → E → E'' → 0` of sheaves of modules on a ringed space whose outer
> terms are finite locally free of **no particular rank**.

```lean
theorem isIso_determinantTensorDeterminantHom
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E''] :
    IsIso (determinantTensorDeterminantHom A' A A'' f g hfg hS)
```

**`Stacks.SheafOfModules.TopWedge.eq_determinantTensorDeterminantHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean#L1035). The attribute's comment: “uniqueness of the canonical map det(E')⊗det(E'')⟶det(E) in the GENERAL case — a short exact sequence of finite locally free sheaves of modules with no constant-rank hypothesis. Together with `eq_detTensorAnnComparison` and the wedge-and-lift formula `detSummandComparison_ι_unit_wedge` this says the map is determined by the formula the source gives for it”.

> **The canonical map is the only morphism restricting to
> `Stacks.SheafOfModules.TopWedge.detTensorAnnComparison` on every degree-`m` summand of
> `det(E'')`.** Together with `Stacks.SheafOfModules.TopWedge.eq_detTensorAnnComparison` and the
> wedge-and-lift formula `Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge` this
> is the precise sense in which the map of [Stacks, Tag 0B38] is *canonical*.

```lean
theorem eq_determinantTensorDeterminantHom
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E'']
    (ψ : ((Stacks.SheafOfModules.Tensor.sheafTensor Osharp).obj A'.determinant).obj A''.determinant
        ⟶ A.determinant)
    (hψ : ∀ m : ℕ, (Stacks.SheafOfModules.TensorLocalProperties.tensorSheafRight
            (Opens.grothendieckTopology ↥X) Osharp A'.determinant).map
          (Limits.Sigma.ι (fun j : ℕ => (A''.exteriorAnnihilator j).toSheafOfModules) m) ≫ ψ =
        detTensorAnnComparison A' A A'' f g hfg hS m) :
    ψ = determinantTensorDeterminantHom A' A A'' f g hfg hS
```

**`Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean, line 1072](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactIso.lean#L1072). The attribute's comment: “the canonical isomorphism det(E')⊗det(E'')≅det(E) in the GENERAL case, with NO constant-rank hypothesis”. References: SGA 6 X (5.1), “special case”.

> **Stacks 0B38, the general case.** For a short exact sequence `0 → E' → E → E'' → 0` of
> sheaves of `O_X`-modules on a ringed space with `E'` and `E''` **finite locally free of no
> particular rank**, there is a canonical isomorphism
>
> `det(E') ⊗_{O_X} det(E'') ≅ det(E)`
>
> of the determinants of [Stacks, Tag 0FJN] — the annihilator of the degree-one part of the
> exterior algebra.
>
> The underlying map is `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantHom`, which
> `Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge` pins to the wedge-and-lift
> formula the source gives for it, which the uniqueness statements
> `Stacks.SheafOfModules.TopWedge.eq_determinantTensorDeterminantHom` and
> `Stacks.SheafOfModules.TopWedge.eq_detTensorAnnComparison` show that formula determines, and
> which `Stacks.SheafOfModules.TopWedge.isIso_determinantTensorDeterminantHom` shows is an
> isomorphism.
>
> No hypothesis on `E` is needed: the freeness of its stalks is derived from the split stalk
> sequence, so the statement is a strengthening of the one in the source, which assumes all three
> terms finite locally free.

```lean
noncomputable def determinantTensorDeterminantIsoOfFiniteLocallyFree
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E''] :
    ((Stacks.SheafOfModules.Tensor.sheafTensor Osharp).obj A'.determinant).obj A''.determinant ≅
        A.determinant
```

**`Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactSummand.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorShortExactSummand.lean#L713). The attribute's comment: “the canonical MAP det(E')⊗det(E'')⟶det(E) in the GENERAL case, with NO constant-rank hypothesis”.

> **The canonical map `det(E') ⊗ det(E'') ⟶ det(E)` of [Stacks, Tag 0B38], for a short exact
> sequence `0 → E' → E → E'' → 0` of sheaves of modules on a ringed space with `E'` and `E''`
> finite locally free of NO PARTICULAR RANK.**
>
> The determinant of [Stacks, Tag 0FJN] is the coproduct over the degrees of the degreewise
> annihilators of the degree-one part of the exterior algebra, and the tensor product of sheaves of
> modules preserves coproducts in each variable, so a map out of `det(E') ⊗ det(E'')` is the same
> thing as a family of maps `det(E')ₙ ⊗ det(E'')ₘ ⟶ det(E)`. This is the family obtained from
> `Stacks.SheafOfModules.TopWedge.detSummandComparison` followed by the inclusion of the
> degree-`n+m` summand of `det(E)`.
>
> That this map is an isomorphism is
> `Stacks.SheafOfModules.TopWedge.isIso_determinantTensorDeterminantHom`, the isomorphism itself is
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree`, and the
> wedge-and-lift formula pinning it is
> `Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge` — all three in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorAnnihilatorShortExactIso`.

```lean
noncomputable def determinantTensorDeterminantHom [Mono f] [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E''] :
    ((Stacks.SheafOfModules.Tensor.sheafTensor Osharp).obj A'.determinant).obj A''.determinant ⟶
        A.determinant
```

**`Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorDeterminantShortExactIso.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorDeterminantShortExactIso.lean#L93). The attribute's comment: “the canonical isomorphism det(E')⊗det(E'')≅det(E) in DETERMINANT form, for a short exact sequence of finite locally free sheaves of CONSTANT rank”. References: SGA 6 X (5.1), “special case”; SGA 6 X (6.2.7), “special case”.

> **Stacks 0B38 in determinant form, at constant rank.** For a short exact sequence
> `0 → E' → E → E'' → 0` of sheaves of modules on a ringed space, with `E'`, `E''` and `E` finite
> locally free of constant ranks `r'`, `k + 1` and `r' + k + 1`, there is a canonical isomorphism
> `det(E') ⊗ det(E'') ≅ det(E)` of the determinants of [Stacks, Tag 0FJN] — the annihilator of the
> degree-one part of the exterior algebra.
>
> It is the comparison of top exterior powers of
> `Stacks.SheafOfModules.TopWedge.detComparison`, which
> `Stacks.SheafOfModules.TopWedge.isIso_detComparison` shows is an isomorphism, conjugated by the
> identifications `⋀ʳ F ≅ det(F)` of [Stacks, Tag 0B37]. The map is pinned by
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIso_hom` to that top-exterior-power
> comparison, which `Stacks.SheafOfModules.TopWedge.detComparison_wedge` in turn pins to the
> wedge-and-lift formula of the source.
>
> This is the CONSTANT-RANK form of the tag. The general case, where the ranks are only locally
> constant, is carried by
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorAnnihilatorShortExactIso`.

```lean
noncomputable def determinantTensorDeterminantIso
    (A' : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E')
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E)
    (A'' : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E'')
    (f : E' ⟶ E) (g : E ⟶ E'') (hfg : f ≫ g = 0)
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g] (r' k : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E' r']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E'' (k + 1)]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E (r' + (k + 1))] :
    ((Stacks.SheafOfModules.Tensor.sheafTensor Osharp).obj A'.determinant).obj A''.determinant ≅
        A.determinant
```

**`Stacks.SheafOfModules.TopWedge.detComparison_wedge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExact.lean, line 780](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExact.lean#L780). The attribute's comment: “the CONSTANT-RANK form of the canonical map det(E')⊗det(E'')⟶det(E) and of its wedge-and-lift formula”.

> **Stacks 0B38, the wedge-and-lift formula.** The canonical comparison carries the image of
> `(s₁ ∧ ⋯ ∧ s_{r'}) ⊗ (g(l₁) ∧ ⋯ ∧ g(l_{k+1}))` to
> `f(s₁) ∧ ⋯ ∧ f(s_{r'}) ∧ l₁ ∧ ⋯ ∧ l_{k+1}`: the wedge of the images of the sections of `E'` with
> **arbitrary local lifts** `lⱼ` of the sections of `E''`. This equation is the one the source
> gives for its canonical map, and it determines the comparison, since the wedges of local
> sections generate the exterior powers locally.
>
> Here `det` is the top exterior power, which
> `SheafOfModules.TensorExteriorSymmetricAlgebras.determinantIsoExteriorPower` identifies with the
> `det` of [Stacks, Tag 0FJN] at constant rank; what is carried here is `E'` of constant rank `r'`
> and `E''` of constant rank `r'' = k + 1`. The ISOMORPHISM clause of the tag is carried separately
> by `Stacks.SheafOfModules.TopWedge.isIso_detComparison`.
>
> This is the CONSTANT-RANK form of the tag. The general case — a short exact sequence of finite
> locally free sheaves with no constant-rank hypothesis — is carried by
> `Stacks.SheafOfModules.TopWedge.detSummandComparison_ι_unit_wedge` and
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorAnnihilatorShortExactIso`.

```lean
theorem detComparison_wedge [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E' r']
    (V : (Opens ↥X)ᵒᵖ) (s : Fin r' → E'.val.obj V) (l : Fin (k + 1) → E.val.obj V) :
    (detComparison A' A A'' f g hfg hS r' k).val.app V
        ((PresheafOfModules.tensorSheafUnit (A'.exteriorPower r')
            (A''.exteriorPower (k + 1))).app V
          (wedgeSec A' V r' s ⊗ₜ wedgeSec A'' V (k + 1) fun i => g.val.app V (l i))) =
      wedgeSec A V (r' + (k + 1)) (Fin.append (fun i => f.val.app V (s i)) l)
```

**`Stacks.SheafOfModules.TopWedge.eq_detComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExact.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExact.lean#L807). The attribute's comment: “uniqueness of the map satisfying the wedge-and-lift formula, which is the precise sense of CANONICAL here — again in the constant-rank form, with the same carried hypotheses as `detComparison_wedge`; the isomorphism clause is carried by `Stacks.SheafOfModules.TopWedge.isIso_detComparison`, and the general case by `Stacks.SheafOfModules.TopWedge.eq_determinantTensorDeterminantHom`”.

> **The canonical comparison is the only morphism satisfying its defining equation.** The
> morphism `⋀ʳ' E' ⊗ ⋀ᵏ⁺¹(g)` is an epimorphism, so a morphism out of `⋀ʳ' E' ⊗ ⋀ᵏ⁺¹ E''` is
> determined by its composite with it.

```lean
theorem eq_detComparison [Epi g]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E' r']
    (ψ : ((Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, _, u, u} Osharp).obj (A'.exteriorPower
        r')).obj
        (A''.exteriorPower (k + 1)) ⟶
      A.exteriorPower (r' + (k + 1)))
    (hψ : ((Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, _, u, u} Osharp).obj
      (A'.exteriorPower r')).map ((extHom A A'' g).app ((k + 1 : ℕ) : ℤ)) ≫ ψ =
      wedgeHom A' A f r' (k + 1)) :
    ψ = detComparison A' A A'' f g hfg hS r' k
```

**`Stacks.SheafOfModules.TopWedge.isIso_detComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExactIso.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerShortExactIso.lean#L432). The attribute's comment: “the ISOMORPHISM clause, in the constant-rank form”. References: SGA 6 X (5.1), “special case”; SGA 6 X (6.2.7), “(6.2.9), special case”.

> **Stacks 0B38, the isomorphism clause in the constant-rank form.** For a short exact
> sequence `0 → E' → E → E'' → 0` of sheaves of modules on a ringed space with `E'` finite
> locally free of constant rank `r'` and `E''` finite locally free of constant rank `k + 1`, the
> canonical comparison `⋀^{r'} E' ⊗ ⋀^{k+1} E'' ⟶ ⋀^{r'+k+1} E` is an isomorphism.
>
> The canonical map `det(E') ⊗ det(E'') ⟶ det(E)` shown invertible here is
> `Stacks.SheafOfModules.TopWedge.detComparison`. Here `det` is the top exterior power, identified
> with the `det` of [Stacks, Tag 0FJN] at constant rank by
> `SheafOfModules.TensorExteriorSymmetricAlgebras.determinantIsoExteriorPower`; what is carried
> here is `E'` of constant rank `r'` and `E''` of constant rank `r'' = k + 1`.
>
> This is the CONSTANT-RANK form of the tag. The general case — a short exact sequence of finite
> locally free sheaves with no constant-rank hypothesis — is carried by
> `Stacks.SheafOfModules.TopWedge.isIso_determinantTensorDeterminantHom` and
> `Stacks.SheafOfModules.TopWedge.determinantTensorDeterminantIsoOfFiniteLocallyFree` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorAnnihilatorShortExactIso`.

```lean
theorem isIso_detComparison
    (A' : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E')
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E)
    (A'' : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology ↥X) E'')
    (f : E' ⟶ E) (g : E ⟶ E'') (hfg : f ≫ g = 0)
    (hS : (ShortComplex.mk f g hfg).Exact) [Mono f] [Epi g] (r' k : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E' r']
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E'' (k + 1)] :
    IsIso (detComparison A' A A'' f g hfg hS r' k)
```

## Tag 0FJN, a lemma

[Tag 0FJN](https://stacks.math.columbia.edu/tag/0FJN) in the Stacks Project.

**`SheafOfModules.TensorExteriorSymmetricAlgebras.determinant_isInvertible_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DeterminantFinitePresentationFlat.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DeterminantFinitePresentationFlat.lean#L329). The attribute's comment: “flatness and finite presentation of F are its only hypotheses on F, which is what the source assumes, and it carries no hypothesis about det(F)”. References: SGA 3 XV (5.7), “partial”.

> **[Stacks, Tag 0FJN].** The determinant of a flat sheaf of modules of finite presentation on
> a ringed space is an invertible module.
>
> Its hypotheses on `F` are exactly the source's: `F` is flat, in the sense
> `AlgebraicGeometry.SheafOfModules.IsFlat` that the source assumes, and of finite presentation.
> Nothing is assumed about `det(F)`. Three statements stand behind it, each proved in this
> repository: every stalk of `det(F)` is an invertible module
> (`SheafOfModules.TensorExteriorSymmetricAlgebras.determinant_stalk_invertible`, with Tag 05NE
> turning flatness of the sheaf into flatness of the stalks); `det(F)` is of finite presentation
> (`isFinitePresentation_determinant_of_isFlat` above); and invertibility descends from the stalks
> for a sheaf of modules of finite presentation
> (`Stacks.SheafOfModules.stalkwiseInvertibleDescent`).
>
> **This is the whole covering set of Tag 0FJN.** The two other statements of the tag's
> conclusion — `determinant_isInvertible` in
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraDeterminant.lean` and
> `determinant_isInvertible_of_finitePresentationDescent` in
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAnnihilatorStalk.lean` — assume more than
> this one and do not carry the attribute.
>
> The statement lives here rather than beside
> `determinant_stalk_invertible_of_isFlat`, which is where it was while the finite presentation of
> `det(F)` was a hypothesis, because
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorDeterminantInvertible` cannot import the
> file that proves that finite presentation: the closure of
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorPowerShortExact`, which this file needs
> through the two retract conditions, makes `HasCoproduct` unsynthesizable in the coproduct
> section of that file, where a family of sheaves of modules on a space is summed. That is a
> pre-existing incompatibility between those two files and has nothing to do with the determinant;
> it is recorded here because it is the reason for the split.

```lean
theorem determinant_isInvertible_of_isFlat {Y : RingedSpace.{u, u}}
    (G : SheafOfModules.{u} (structureSheafRing Y)) [G.IsFinitePresentation]
    (A : TensorExteriorSymmetricAlgebras (Opens.grothendieckTopology Y.carrier) G)
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := Y.sheaf) G) :
    AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ Y.presheaf
        (forget₂ CommRingCat.{u} RingCat.{u}) Y.IsSheaf) A.determinant
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.26, Tag 0B37](https://stacks.math.columbia.edu/tag/0B37)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
