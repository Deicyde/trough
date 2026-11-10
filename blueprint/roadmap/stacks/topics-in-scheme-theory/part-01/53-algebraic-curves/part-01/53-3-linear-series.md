---
declaration: section
origin: cited
lean: AlgebraicGeometry.LinearSeries, Stacks.LinearSeriesMorphism.exists_hom_over_and_hom_pullback_twistingSheafAtUniverse_of_isRegular, AlgebraicGeometry.linearSeries_nonempty_of_le, Stacks.LinearSeriesMorphism.degreeOver_le_or_constant_of_isRegular, AlgebraicGeometry.linearSeries_dimension_le_degree_and_genus_eq_zero, Stacks.Divisors.LinearlyEquivalent, Stacks.Divisors.completeLinearSystem, Stacks.LinearSystemScheme.completeLinearSystem_eq_closedPoints_abelMapFibre
statement: formalized
proof: formalized
---

# 53.3 Linear series

Section 53.3 of the Stacks Project, [Tag 0CCM](https://stacks.math.columbia.edu/tag/0CCM). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CCN, a definition

[Tag 0CCN](https://stacks.math.columbia.edu/tag/0CCN) in the Stacks Project.

**`AlgebraicGeometry.LinearSeries`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean#L82).

> A linear series of degree `d` and dimension `r` on a proper scheme of dimension at most one
> over a field: an invertible sheaf of degree `d` together with an `(r + 1)`-dimensional space of
> global sections.

```lean
structure LinearSeries (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (hdim : topologicalKrullDim X ≤ 1) (d r : ℕ)
```

## Tag 0CCP, a lemma

[Tag 0CCP](https://stacks.math.columbia.edu/tag/0CCP) in the Stacks Project.

**`Stacks.LinearSeriesMorphism.exists_hom_over_and_hom_pullback_twistingSheafAtUniverse_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSeriesMorphism.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSeriesMorphism.lean#L309).

> **Stacks Project, Tag 0CCP.** Let `k` be a field, `X` a nonsingular proper curve over `k` and
> `(ℒ, V)` a `𝔤^r_d` on `X`. Then there are a morphism `φ : X ⟶ ℙ^r_k` of varieties over `k` — a
> morphism lying over the structure morphism of `X` — and a map `α : φ ^* 𝒪(1) ⟶ ℒ` carrying
> `φ ^* T_0, …, φ ^* T_r` to a basis of `V`.
>
> Nonsingularity enters as integrality of `X` together with `hreg`; the properness and the
> dimension bound are carried by `AlgebraicGeometry.LinearSeries`. The basis is the one supplied by
> `nonempty_basis`, and the conclusion asserts that the `α`-images of the pulled-back coordinates
> are the sections underlying it, which is the source's "are sent to a basis of `V`".

```lean
theorem exists_hom_over_and_hom_pullback_twistingSheafAtUniverse_of_isRegular [IsIntegral X]
    (hreg : IsRegular X) (E : LinearSeries k f hdim d r) :
    ∃ (b : Module.Basis (Fin (r + 1)) k E.V) (p : X ⟶ projectiveSpaceOver r (Spec (.of k))),
      p ≫ (projectiveSpaceOver r (Spec (.of k)) ↘ Spec (.of k)) = f ∧
      ∃ α : (Scheme.Modules.pullback
          (p ≫ projectiveSpaceOver.toIntegralAtUniverse r (Spec (.of k)))).obj
            (twistingSheafAtUniverse.{u} r) ⟶ E.L,
        ∀ i, α.app ⊤ (pullbackCoordSection.{u}
          (p ≫ projectiveSpaceOver.toIntegralAtUniverse r (Spec (.of k))) i) =
          seriesSections E b i
```

## Tag 0CCQ, a lemma

[Tag 0CCQ](https://stacks.math.columbia.edu/tag/0CCQ) in the Stacks Project.

**`AlgebraicGeometry.linearSeries_nonempty_of_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean#L98).

> A linear series of degree `d` and dimension `r` yields one of degree `d` and dimension `s` for
> every `s ≤ r`.

```lean
lemma linearSeries_nonempty_of_le
    {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X ≤ 1) (d r s : ℕ)
    (h : Nonempty (LinearSeries k f hdim d r)) (hs : s ≤ r) :
    Nonempty (LinearSeries k f hdim d s)
```

## Tag 0CCR, a lemma

[Tag 0CCR](https://stacks.math.columbia.edu/tag/0CCR) in the Stacks Project.

**`Stacks.LinearSeriesMorphism.degreeOver_le_or_constant_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PencilDegree.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/PencilDegree.lean#L534). The attribute's comment: “the whole tag. `the morphism of Lemma 53.3.2` is rendered by the property that characterizes it: the data of Tag 0CCP exists for `(ℒ, V)`, and every datum of that shape satisfies the alternative. `factors through a closed point` is rendered as constancy of the morphism with closed image, nothing being asked of the residue field of that point, and `H⁰(X, 𝒪_X) ≠ k` as `1 < Module.rank k H⁰(X, 𝒪_X)`”.

> **Stacks Project, Tag 0CCR.** Let `k` be a field, `X` a nonsingular proper curve over `k`,
> and `(ℒ, V)` a `𝔤¹_d` on `X`. Then the morphism `φ : X ⟶ 𝐏¹_k` of [Stacks, Tag 0CCP] either
>
> 1. is nonconstant and has degree `≤ d`, or
> 2. factors through a closed point of `𝐏¹_k`, and in this case `H⁰(X, 𝒪_X) ≠ k`.
>
> The whole tag is this one statement. **"The morphism of Lemma 53.3.2" is rendered by its
> characterizing property.** [Stacks, Tag 0CCP] asserts the existence of a basis `b` of `V`, a
> morphism `p : X ⟶ 𝐏¹_k` over `k`, and a map `α : p ^* 𝒪(1) ⟶ ℒ` carrying the pulled-back
> coordinates `p ^* T₀, p ^* T₁` to the sections underlying `b`; it does not single one out, so
> there is no term `φ (ℒ, V)` to name. The definite article is therefore read as the conjunction of
> two assertions: the first is that such a triple `(b, p, α)` **exists** — which is
> `Stacks.LinearSeriesMorphism.exists_hom_over_and_hom_pullback_twistingSheafAtUniverse_of_isRegular`
> — and the second that **every** such triple satisfies the alternative, which is
> `Stacks.LinearSeriesMorphism.degreeOver_le_or_constant` with its arguments universally
> quantified. The second assertion is what makes this a statement about `φ` itself: it holds of
> every morphism Tag 0CCP's property characterizes, so it is independent of any choice, and it is
> strictly stronger than the assertion that *some* morphism to `𝐏¹_k` over `k` satisfies the
> alternative. The two alternatives are mutually exclusive, by
> `Stacks.LinearSeriesMorphism.not_constant_of_not_exists_eq`.
>
> Hypotheses: `k` is a field; `X` is a proper curve over `k` (`[IsProper f]`, `[IsCurve k f]`) and
> nonsingular (`hreg : IsRegular X`, integrality being already part of `IsCurve`); and
> `E : LinearSeries k f hdim d 1` is a `𝔤¹_d`, the degree-`d` dimension-one linear series of
> [Stacks, Tag 0CCN]. Nothing else is assumed.
>
> Readings: the degree of `φ` is `AlgebraicGeometry.degreeOver`, the degree of the extension of
> function fields ([Stacks, Tag 02NY]); `H⁰(X, 𝒪_X) ≠ k` is `1 < Module.rank k H⁰(X, 𝒪_X)`, which
> by `Stacks.LinearSeriesMorphism.not_nonempty_linearEquiv_of_one_lt_rank` rules out every
> `k`-linear isomorphism `H⁰(X, 𝒪_X) ≃ₗ[k] k`; and "factors through a closed point" is constancy
> of `φ` together with closedness of its image point. **The closed point is not required to be
> `k`-rational**, which is the point of Tongmu He's comment on the tag: over a `k` that is not
> algebraically closed the morphism attached to two `k`-linearly independent sections can land on
> a closed point whose residue field properly extends `k`, and alternative (2) asserts of `y` only
> `IsClosed {y}`. See the module documentation for all of these.

```lean
theorem degreeOver_le_or_constant_of_isRegular (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] [IsCurve k f] (hreg : IsRegular X)
    {hdim : topologicalKrullDim X ≤ 1} {d : ℕ} (E : LinearSeries k f hdim d 1) :
    (∃ (b : Module.Basis (Fin 2) k E.V) (p : X ⟶ projectiveSpaceOver 1 (Spec (.of k))),
        p ≫ (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)) = f ∧
        ∃ α : (Scheme.Modules.pullback
            (p ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k)))).obj
              (twistingSheafAtUniverse.{u} 1) ⟶ E.L,
          ∀ i, α.app ⊤ (pullbackCoordSection.{u}
            (p ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k))) i) =
            seriesSections E b i) ∧
      ∀ (b : Module.Basis (Fin 2) k E.V) (p : X ⟶ projectiveSpaceOver 1 (Spec (.of k)))
        (hp : p ≫ (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)) = f)
        (α : (Scheme.Modules.pullback
            (p ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k)))).obj
              (twistingSheafAtUniverse.{u} 1) ⟶ E.L),
        (∀ i, α.app ⊤ (pullbackCoordSection.{u}
          (p ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k))) i) =
          seriesSections E b i) →
        (∃ _hnc : ¬ ∃ y : projectiveSpaceOver 1 (Spec (.of k)), ∀ x : X, p.base x = y,
            @degreeOver X (projectiveSpaceOver 1 (Spec (.of k))) p inferInstance inferInstance
              (locallyOfFiniteType_of_isCurve_comp k f
                (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)) p hp)
              (isDominant_of_not_constant k f
                (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)) p _hnc) ≤ d) ∨
          ((∃ y : projectiveSpaceOver 1 (Spec (.of k)),
                IsClosed ({y} : Set (projectiveSpaceOver 1 (Spec (.of k)))) ∧
                ∀ x : X, p.base x = y) ∧
            1 < Module.rank k
              (cohomologyOverField k f (SheafOfModules.unit X.ringCatSheaf) 0))
```

## Tag 0CCS, a lemma

[Tag 0CCS](https://stacks.math.columbia.edu/tag/0CCS) in the Stacks Project.

**`AlgebraicGeometry.linearSeries_dimension_le_degree_and_genus_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSeries.lean#L810). The attribute's comment: “both assertions, under the source's own hypotheses. Tag 02O6 at the structure sheaf, Tag 0B5T clause (4) and the ampleness of `ℒ` that the latter consumes are all proved here. `0 < d` is assumed for the equality clause because the source's statement is false at `r = d = 0`, by `AlgebraicGeometry.exists_counterexample_to_displayed_statement_of_tag_0CCS_at_zero`”.

> Let `X` be a proper curve over a field `k` with `H⁰(X, 𝒪_X) = k`, spelled as invertibility of
> the canonical map from `k`. If `X` has a `𝔤^r_d`, then `r ≤ d`, and if moreover `0 < d` and
> `r = d`, then the genus of `X` is zero.

```lean
theorem linearSeries_dimension_le_degree_and_genus_eq_zero {k : Type u} [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    {hdim : topologicalKrullDim X ≤ 1} {d r : ℕ} (series : LinearSeries k f hdim d r) :
    r ≤ d ∧ (0 < d → r = d → genus f = 0)
```

## Tag 0CCT, a remark

[Tag 0CCT](https://stacks.math.columbia.edu/tag/0CCT) in the Stacks Project.

**`Stacks.Divisors.LinearlyEquivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ClassicalLinearSystem.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ClassicalLinearSystem.lean#L77). The attribute's comment: “the classical definition of linear equivalence: 𝒪\_X(D) ≅ 𝒪\_X(D')”.

> **Stacks Project, Tag 0CCT.** Two effective Cartier divisors `D, D' ⊆ X` are *linearly
> equivalent* when `𝒪_X(D) ≅ 𝒪_X(D')` as `𝒪_X`-modules.

```lean
def LinearlyEquivalent (D D' : X.IdealSheafData) : Prop
```

**`Stacks.Divisors.completeLinearSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ClassicalLinearSystem.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ClassicalLinearSystem.lean#L126). The attribute's comment: “the complete linear system |D|: the effective Cartier divisors linearly equivalent to D”.

> **Stacks Project, Tag 0CCT.** The *complete linear system*, or *complete linear series*,
> `|D|` of an effective Cartier divisor `D ⊆ X`: the set of effective Cartier divisors `E ⊆ X`
> which are linearly equivalent to `D`.

```lean
def completeLinearSystem (D : X.IdealSheafData) : Set X.IdealSheafData
```

**`Stacks.LinearSystemScheme.completeLinearSystem_eq_closedPoints_abelMapFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/AbelMapFibre.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/AbelMapFibre.lean#L287). The attribute's comment: “|D| is the set of closed points of the fibre of gamma\_d : Hilb^d -> Pic over the point of O\_X(D); this gives |D| a natural scheme structure”.

> **Stacks Project, Tag 0CCT.** Let `X` be a smooth projective curve over an algebraically
> closed field `k` and `D ⊆ X` an effective Cartier divisor of degree `d`. The fibre
> `Hilb^d_{X/k} ×_{Pic_{X/k}} Spec k` of the Abel map `γ_d : Hilb^d_{X/k} → Pic_{X/k}`,
> `Z ↦ [𝒪(Z)]` (`AlgebraicGeometry.RigidifiedPicard.familyClass`), over the point `[𝒪_X(D)]` is
> represented by `𝐏(H⁰(X, 𝒪_X(D))^∨)`: its `T`-points are naturally the `k`-morphisms
> `T ⟶ 𝐏(H⁰(X, 𝒪_X(D))^∨)`. The closed points of this scheme are exactly the members of `|D|`, a
> closed point corresponding to the image in `X` of the family over `Spec k` it classifies; the
> closed point cut out by evaluation at a nonzero `s ∈ H⁰(X, 𝒪_X(D))` corresponds to the zero
> scheme `Z(s)`. This is the scheme structure on `|D|`.

```lean
theorem completeLinearSystem_eq_closedPoints_abelMapFibre {d : ℕ}
    (hd : invertibleCurveDegree k (B.inclusion.map g)
      (topologicalKrullDim_le_one k (B.inclusion.map g))
      (Stacks.Divisors.modulesInvertibleSheaf D) = d) :
    ∃ e : ∀ T : BigFppfOver B (Spec (.of k)) hk,
        ((BigFppfOver.toOver B (Spec (.of k)) hk).obj T ⟶
          (linearSystemScheme k (B.inclusion.map g) D).asOver (Spec (.of k))) ≃
          abelMapFibre B hX k g D d T,
      (∀ (T T' : BigFppfOver B (Spec (.of k)) hk) (h : T' ⟶ T)
          (p : (BigFppfOver.toOver B (Spec (.of k)) hk).obj T ⟶
            (linearSystemScheme k (B.inclusion.map g) D).asOver (Spec (.of k))),
        (e T' ((BigFppfOver.toOver B (Spec (.of k)) hk).map h ≫ p)).1.ideal =
          (e T p).1.ideal.comap (Stacks.Hilbert.familyBaseChangeMap
            (curveOver (B.inclusion.map g)) ((BigFppfOver.toOver B (Spec (.of k)) hk).map h))) ∧
      ∃ c : closedPoints (linearSystemScheme k (B.inclusion.map g) D) ≃
          Stacks.Divisors.completeLinearSystem D,
        (∀ x : closedPoints (linearSystemScheme k (B.inclusion.map g) D),
          (c x : (B.inclusion.obj (B.obj hX)).IdealSheafData) =
            (e (terminalTest B hk) (Over.homMk (@pointOfClosedPoint _ _ _ _
              (projectiveSpaceOfModuleToSpec k (dualSections k (B.inclusion.map g) D))
              (locallyOfFiniteType_linearSystemScheme k (B.inclusion.map g) D) x.1 x.2)
              (@pointOfClosedPoint_comp _ _ _ _ _
                (locallyOfFiniteType_linearSystemScheme k (B.inclusion.map g) D) x.1
                x.2))).1.ideal.comap
              (baseChangeTerminalIso B hX hk g).inv) ∧
        ∀ (s : cohomologyOverField k (B.inclusion.map g)
            (Stacks.Divisors.modulesInvertibleSheaf D) 0) (hs : s ≠ 0),
          (c ⟨ProjectiveSpaceOfModule.linearFunctionalPoint k _ (Module.Dual.eval k _ s)
              (eval_ne_zero k (B.inclusion.map g) D hs),
            ProjectiveSpaceOfModule.linearFunctionalPoint_isClosed k _ _
              (eval_ne_zero k (B.inclusion.map g) D hs)⟩ :
              (B.inclusion.obj (B.obj hX)).IdealSheafData) =
            zeroScheme _ (Stacks.Divisors.modulesInvertibleSheaf D)
              (sectionOf k (B.inclusion.map g) (Stacks.Divisors.modulesInvertibleSheaf D) s)
```

**`Stacks.LinearSystemScheme.isLinearSystem_iff_exists_eq_iSup_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearEquations/Basic.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearEquations/Basic.lean#L183). The attribute's comment: “a linear system on X is a closed subvariety L of |D| which can be cut out by linear equations, the ideal sheaf of L being generated by linear forms”.

> **Stacks Project, Tag 0CCT.** A closed subscheme `L ⊆ |D|` is a linear system exactly when it
> is a closed subvariety cut out by linear equations: `L` is integral, and its ideal sheaf is
> generated by the global sections of `𝒪(1)` given by the elements of a subspace
> `E ⊆ W = H⁰(X, 𝒪_X(D))^∨` of linear forms on `|D| = 𝐏(W)`, that is
> `L = ⨆_{e ∈ E} Z(e)`.

```lean
theorem isLinearSystem_iff_exists_eq_iSup_zeroScheme
    (L : (linearSystemScheme k f D).IdealSheafData) :
    haveI := isInvertible_twistingSheaf_projectiveSpaceOfModule k (dualSections k f D)
      ((1 : ℕ) : ℤ)
    IsLinearSystem k f D L ↔
      (∃ E : Submodule k (dualSections k f D),
        L = ⨆ e : E, AlgebraicGeometry.zeroScheme (linearSystemScheme k f D)
          (twistingSheafModule (fun n => SymPow.symmetricPower n k (dualSections k f D))
            ((1 : ℕ) : ℤ))
          (degreeSection (fun n => SymPow.symmetricPower n k (dualSections k f D)) 1
            ⟨SymmetricAlgebra.ι k (dualSections k f D) e,
              ProjectiveSpaceOfModule.ι_mem_symmetricPower_one k (dualSections k f D)
                (e : dualSections k f D)⟩)) ∧
        IsIntegral L.subscheme
```

**`Stacks.LinearSystemScheme.IsLinearSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean#L210). The attribute's comment: “a linear system on X is a closed subvariety L of |D| which can be cut out by linear equations”.

> A *linear system* (or *linear series*) on `X` is a closed subvariety `L ⊆ |D|` which can be
> cut out by linear equations: `L` is the closed subscheme `V₊(E)` of a space `E` of linear forms
> on `|D| = 𝐏(H⁰(X, 𝒪_X(D))^∨)`, and it is integral.

```lean
structure IsLinearSystem (L : (linearSystemScheme k f D).IdealSheafData) : Prop
```

**`Stacks.LinearSystemScheme.IsLinearSystem.exists_eq_projectiveSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean#L278). The attribute's comment: “if L has dimension r, then L = P(V^dual) where V is a linear subspace of H^0(X, O\_X(D)) of dimension r + 1”.

> If a linear system `L ⊆ |D|` has dimension `r`, then `L = 𝐏(V^∨)` for a linear subspace
> `V ⊆ H⁰(X, 𝒪_X(D))` of dimension `r + 1`: `L` is the image of the closed immersion
> `𝐏(V^∨) ⟶ 𝐏(H⁰(X, 𝒪_X(D))^∨)` induced by `V ⊆ H⁰(X, 𝒪_X(D))`, and it is isomorphic to
> `𝐏(V^∨)` through that immersion. The subspace `V` is determined by `L`.

```lean
theorem IsLinearSystem.exists_eq_projectiveSpace {L : (linearSystemScheme k f D).IdealSheafData}
    (hL : IsLinearSystem k f D L) {r : ℕ} (hr : topologicalKrullDim L.subscheme = r) :
    ∃ (V : Submodule k (cohomologyOverField k f (Stacks.Divisors.modulesInvertibleSheaf D) 0))
      (_ : Module.finrank k V = r + 1),
      L = (subspaceImmersion k f D V).ker ∧
        (∀ V' : Submodule k
            (cohomologyOverField k f (Stacks.Divisors.modulesInvertibleSheaf D) 0),
          L = (subspaceImmersion k f D V').ker → V' = V) ∧
        ∃ φ : L.subscheme ≅ projectiveSpaceOfModule k (Module.Dual k V),
          φ.inv ≫ L.subschemeι = subspaceImmersion k f D V
```

**`Stacks.LinearSystemScheme.IsLinearSystem.linearSeries`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/LinearSubsystem.lean#L319). The attribute's comment: “the classical linear series L in |D| corresponds to the linear series (O\_X(D), V)”.

> The linear series `(𝒪_X(D), V)` of [Stacks, Tag 0CCN] corresponding to a linear system
> `L ⊆ |D|` of dimension `r`, with `L = 𝐏(V^∨)` as in
> `Stacks.LinearSystemScheme.IsLinearSystem.exists_eq_projectiveSpace`.

```lean
def IsLinearSystem.linearSeries {L : (linearSystemScheme k f D).IdealSheafData}
    (hL : IsLinearSystem k f D L) {r : ℕ} (hr : topologicalKrullDim L.subscheme = r) {d : ℕ}
    (hd : invertibleCurveDegree k f (topologicalKrullDim_le_one k f)
      (Stacks.Divisors.modulesInvertibleSheaf D) = d) :
    LinearSeries k f (topologicalKrullDim_le_one k f) d r
```

**`Stacks.LinearSystemScheme.completeLinearSystem_iso_projectiveSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/Statement.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/Statement.lean#L217). The attribute's comment: “|D| is isomorphic to P^m\_k with m + 1 = h^0(O\_X(D)); canonically |D| = P(H^0(X, O\_X(D))^dual)”.

> Let `X` be a smooth projective curve over an algebraically closed field `k`, `D ⊆ X` an
> effective Cartier divisor of degree `d`, and `m` the integer with `m + 1 = h⁰(𝒪_X(D))`. The scheme
> `|D| = 𝐏(H⁰(X, 𝒪_X(D))^∨)` representing the fibre of the Abel map over the point of `𝒪_X(D)` is
> isomorphic over `k` to `ℙ^m_k`; equivalently, that fibre is represented by `ℙ^m_k` — a natural
> bijection between its `T`-points and the `k`-morphisms `T ⟶ ℙ^m_k`. Canonically, the fibre is
> represented by `𝐏(H⁰(X, 𝒪_X(D))^∨)` itself, through the bijection sending the closed point cut out
> by evaluation at a nonzero `s ∈ H⁰(X, 𝒪_X(D))` to the family whose image in `X` is the zero scheme
> `Z(s)`.

```lean
theorem completeLinearSystem_iso_projectiveSpace {d m : ℕ}
    (hd : invertibleCurveDegree k f (topologicalKrullDim_le_one k f)
      (Stacks.Divisors.modulesInvertibleSheaf D) = d)
    (hm : Module.finrank k
      (cohomologyOverField k f (Stacks.Divisors.modulesInvertibleSheaf D) 0) = m + 1) :
    Nonempty ((linearSystemScheme k f D).asOver (Spec (.of k)) ≅
      (projectiveSpaceOverRing m (.of k)).asOver (Spec (.of k))) ∧
    (∃ e : ∀ T : Over (Spec (.of k)),
        (T ⟶ (projectiveSpaceOverRing m (.of k)).asOver (Spec (.of k))) ≃ abelFibre f D d T,
      ∀ (T T' : Over (Spec (.of k))) (h : T' ⟶ T)
          (g : T ⟶ (projectiveSpaceOverRing m (.of k)).asOver (Spec (.of k))),
        (e T' (h ≫ g)).1.ideal = (e T g).1.ideal.comap (familyBaseChangeMap (curveOver f) h)) ∧
    ∃ e : ∀ T : Over (Spec (.of k)),
        (T ⟶ (linearSystemScheme k f D).asOver (Spec (.of k))) ≃ abelFibre f D d T,
      (∀ (T T' : Over (Spec (.of k))) (h : T' ⟶ T)
          (g : T ⟶ (linearSystemScheme k f D).asOver (Spec (.of k))),
        (e T' (h ≫ g)).1.ideal = (e T g).1.ideal.comap (familyBaseChangeMap (curveOver f) h)) ∧
      ∀ (s : cohomologyOverField k f (Stacks.Divisors.modulesInvertibleSheaf D) 0) (hs : s ≠ 0),
        (e (fieldPoint k) (sectionPoint k f D hs)).1.ideal.comap
            (inv (pullback.fst f (𝟙 (Spec (.of k))))) =
          zeroScheme X (Stacks.Divisors.modulesInvertibleSheaf D)
            (sectionOf k f (Stacks.Divisors.modulesInvertibleSheaf D) s)
```

**`Stacks.Divisors.linearlyEquivalent_iff_weilDivisorClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/WeilDivisorClass.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LinearSystemScheme/WeilDivisorClass.lean#L147). The attribute's comment: “D and D' are linearly equivalent iff their Weil divisors have the same class in Cl(X)”.

> **Stacks Project, Tag 0CCT.** Let `X` be a smooth projective curve over an algebraically
> closed field `k`. Two effective Cartier divisors `D, D' ⊆ X` are linearly equivalent exactly
> when the Weil divisors `[D]` and `[D']` associated to them define the same element of the Weil
> divisor class group `Cl(X)`.

```lean
theorem linearlyEquivalent_iff_weilDivisorClass_eq (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [IsProjectiveVariety k f] [Smooth f]
    (D D' : X.IdealSheafData) [hD : IsEffectiveCartierDivisor D]
    [hD' : IsEffectiveCartierDivisor D'] :
    haveI : IsNoetherian X := isNoetherian_of_isVariety k f
    haveI : IsIntegral X := (inferInstance : IsVariety k f).toIsIntegral
    LinearlyEquivalent D D' ↔
      (effectiveCartierWeilDivisor D hD : weilDivisorClassGroup X) =
        (effectiveCartierWeilDivisor D' hD' : weilDivisorClassGroup X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.3, Tag 0CCM](https://stacks.math.columbia.edu/tag/0CCM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
