---
declaration: section
origin: cited
lean: CategoryTheory.IsPullback.of_hasPullback, Stacks.Flatness.exists_etaleNeighborhood_finiteAt, Stacks.Flatness.isFiniteNeighborhoodAt_baseChange, Stacks.Flatness.exists_etaleNeighborhood_finite_opens_of_isolated_fiber_points, AlgebraicGeometry.exists_elementaryEtaleNeighborhood_finite_opens_of_isolated_fiber_points, AlgebraicGeometry.exists_etale_finite_opens_of_isolated_fiber_points, Stacks.Flatness.exists_etaleNeighborhood_decomposition, AlgebraicGeometry.exists_elementaryEtaleNeighborhood_decomposition
statement: formalized
proof: formalized
---

# 37.41 Étale localization of quasi-finite morphisms

Section 37.41 of the Stacks Project, [Tag 04HF](https://stacks.math.columbia.edu/tag/04HF). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02LJ, an equation

[Tag 02LJ](https://stacks.math.columbia.edu/tag/02LJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsPullback.of_hasPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPullback.of_hasPullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L69) (StacksFrontier): “the cartesian square X\_U = U ×\_S X of the basic diagram”.

## Tag 02LK, a lemma

[Tag 02LK](https://stacks.math.columbia.edu/tag/02LK) in the Stacks Project.

**`Stacks.Flatness.exists_etaleNeighborhood_finiteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteNeighborhood.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteNeighborhood.lean#L392). The attribute's comment: “existence”. References: EGA IV (18.12.1).

> A locally finite type morphism becomes finite near a point isolated in its fibre after an
> elementary étale base change.

```lean
theorem exists_etaleNeighborhood_finiteAt {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (x : X) (hx : IsIsolatedPoint (f.asFiber x)) :
    Nonempty (FiniteNeighborhoodAt f x)
```

**`Stacks.Flatness.isFiniteNeighborhoodAt_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteNeighborhood.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteNeighborhood.lean#L578). The attribute's comment: “elementary étale refinement”.

> The pullback of a finite neighbourhood along any further elementary étale neighbourhood is
> again a finite neighbourhood: finite over the new base, with a unique distinguished-fibre point
> having the same residue field as the original point.

```lean
theorem isFiniteNeighborhoodAt_baseChange {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (U : EtaleNeighborhood S (f x))
    (V : (pullback f U.toBase).Opens) (hV : IsFiniteNeighborhoodAt f x U V)
    (U' : EtaleNeighborhood U.scheme U.point) (hU' : U'.IsElementary) :
    IsFiniteNeighborhoodAt f x
      { scheme := U'.scheme
        point := U'.point
        toBase := U'.toBase ≫ U.toBase
        map_point := by simp [U'.map_point, U.map_point] }
      ((pullback.map f (U'.toBase ≫ U.toBase) f U.toBase
        (𝟙 X) U'.toBase (𝟙 S) (by simp) (by simp)) ⁻¹ᵁ V)
```

## Tag 02LL, a lemma

[Tag 02LL](https://stacks.math.columbia.edu/tag/02LL) in the Stacks Project.

**`Stacks.Flatness.exists_etaleNeighborhood_finite_opens_of_isolated_fiber_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/IsolatedPointsDecomposition.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/IsolatedPointsDecomposition.lean#L147).

> **Stacks Project, Tag 02LL.** Several isolated points of one fibre can simultaneously be
> made finite over a single elementary étale neighbourhood of the base point.

```lean
theorem exists_etaleNeighborhood_finite_opens_of_isolated_fiber_points
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (s : S) (n : ℕ) (x : Fin n → X) (hx : ∀ i, f (x i) = s)
    (hx_isolated : ∀ i, IsIsolatedPoint (f.asFiber (x i))) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (V : Fin n → (pullback f U.toBase).Opens)
      (v : ∀ i, V i),
      (∀ i, IsFinite ((V i).ι ≫ pullback.snd f U.toBase)) ∧
      (∀ i, {y : V i | ((V i).ι ≫ pullback.snd f U.toBase) y = U.point} = {v i}) ∧
      (∀ i, ((V i).ι ≫ pullback.fst f U.toBase) (v i) = x i) ∧
      (∀ i, IsIso (((V i).ι ≫ pullback.fst f U.toBase).residueFieldMap (v i)))
```

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_finite_opens_of_isolated_fiber_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/FiniteNeighborhood.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/FiniteNeighborhood.lean#L297).

> **Stacks Project, Tag 02LL.** Several isolated points in one fibre can
> simultaneously be made finite over an elementary étale neighborhood.

```lean
public theorem exists_elementaryEtaleNeighborhood_finite_opens_of_isolated_fiber_points
    (f : X ⟶ S) [LocallyOfFiniteType f] (s : S) (n : ℕ) (x : Fin n → X) (hx : ∀ i, f (x i) = s)
    (hx_isolated : ∀ i, IsIsolatedPoint (f.asFiber (x i))) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (V : Fin n → (pullback f U.toBase).Opens)
      (v : ∀ i, V i),
      (∀ i, IsFinite ((V i).ι ≫ pullback.snd f U.toBase)) ∧
      (∀ i, {y : V i | ((V i).ι ≫ pullback.snd f U.toBase) y = U.point} = {v i}) ∧
      (∀ i, ((V i).ι ≫ pullback.fst f U.toBase) (v i) = x i) ∧
      (∀ i, IsIso (((V i).ι ≫ pullback.fst f U.toBase).residueFieldMap (v i)))
```

## Tag 02LM, a lemma

[Tag 02LM](https://stacks.math.columbia.edu/tag/02LM) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_finite_opens_of_isolated_fiber_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/QuasiFiniteEtaleLocalisation.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/QuasiFiniteEtaleLocalisation.lean#L317). References: EGA IV (18.12.1), “more general”.

> **Stacks Project, Tag 02LM.** Finitely many distinct isolated points of a fibre of a morphism
> locally of finite type have, after a single étale base change, finite open neighbourhoods meeting
> the distinguished fibre in exactly one point, with finite purely inseparable residue extension,
> and these points exhaust the base change of the chosen points.

```lean
theorem exists_etale_finite_opens_of_isolated_fiber_points
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (n : ℕ) (s : S) (x : Fin n → X) (hx : ∀ i, f (x i) = s)
    (hx_injective : Function.Injective x)
    (hx_isolated : ∀ i, IsIsolatedPoint (f.asFiber (x i))) :
    ∃ (U : EtaleNeighborhood S s)
      (m : Fin n → ℕ)
      (V : ∀ i, Fin (m i) → (pullback f U.toBase).Opens)
      (v : ∀ i j, V i j),
      (∀ i j,
        let g := (V i j).ι ≫ pullback.snd f U.toBase
        IsFinite g ∧
          g ⁻¹' {U.point} = {v i j} ∧
          ((V i j).ι ≫ pullback.fst f U.toBase) (v i j) = x i ∧
          ∃ hvu : g (v i j) = U.point,
            RingHom.Finite (((U.scheme.residueFieldCongr hvu).inv ≫
              g.residueFieldMap (v i j)).hom) ∧
            ((U.scheme.residueFieldCongr hvu).inv ≫
              g.residueFieldMap (v i j)).hom.IsPurelyInseparable) ∧
      Function.Injective (fun p : Σ i, Fin (m i) ↦ (V p.1 p.2).ι (v p.1 p.2)) ∧
      (∀ i (y : ↥(pullback f U.toBase)),
        (pullback.snd f U.toBase) y = U.point →
        (pullback.fst f U.toBase) y = x i →
        ∃ j, (V i j).ι (v i j) = y)
```

## Tag 02LN, a lemma

[Tag 02LN](https://stacks.math.columbia.edu/tag/02LN) in the Stacks Project.

**`Stacks.Flatness.exists_etaleNeighborhood_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/IsolatedPointsDecomposition.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/IsolatedPointsDecomposition.lean#L329). References: EGA IV (18.12.1), “separated case”; EGA IV (18.12.3), “more general”.

> **Stacks Project, Tag 02LN.** Finitely many distinct isolated points of a fibre of a
> separated morphism locally of finite type split into separate finite open-and-closed pieces
> after an elementary étale base change.

```lean
theorem exists_etaleNeighborhood_decomposition
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f]
    (s : S) (n : ℕ) (x : Fin n → X) (hx : ∀ i, f (x i) = s)
    (hx_injective : Function.Injective x)
    (hx_isolated : ∀ i, IsOpen {f.asFiber (x i)}) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (P : Option (Fin n) → Scheme.{u})
      (j : ∀ a, P a ⟶ pullback f U.toBase)
      (_ : ∀ a, IsOpenImmersion (j a))
      (_ : ∀ a, IsClosedImmersion (j a))
      (_ : IsIso (Sigma.desc j))
      (v : ∀ i, P (some i))
      (_ : ∀ i, IsFinite (j (some i) ≫ pullback.snd f U.toBase)),
      (∀ i, (j (some i) ≫ pullback.fst f U.toBase) (v i) = x i) ∧
      (∀ i, {y : P (some i) |
          (j (some i) ≫ pullback.snd f U.toBase) y = U.point} = {v i}) ∧
      (∀ i, IsIso ((j (some i) ≫ pullback.fst f U.toBase).residueFieldMap (v i))) ∧
      (∀ y : P none,
        (j none ≫ pullback.snd f U.toBase) y = U.point →
          ∀ i, (j none ≫ pullback.fst f U.toBase) y ≠ x i)
```

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/Decomposition.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/Decomposition.lean#L239). References: EGA IV (18.12.1), “separated case”; EGA IV (18.12.3), “more general”.

> **Stacks Project, Tag 02LN.** Finitely many distinct isolated points of a
> fibre of a separated morphism locally of finite type split into separate finite
> open-and-closed pieces after an elementary étale base change.

```lean
public theorem exists_elementaryEtaleNeighborhood_decomposition
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f]
    (s : S) (n : ℕ) (x : Fin n → X) (hx : ∀ i, f (x i) = s)
    (hx_injective : Function.Injective x)
    (hx_isolated : ∀ i, IsOpen {f.asFiber (x i)}) :
    ∃ (U : EtaleNeighborhood S s) (_ : U.IsElementary)
      (P : Option (Fin n) → Scheme.{u})
      (j : ∀ a, P a ⟶ pullback f U.toBase)
      (_ : ∀ a, IsOpenImmersion (j a))
      (_ : ∀ a, IsClosedImmersion (j a))
      (_ : IsIso (Sigma.desc j))
      (v : ∀ i, P (some i))
      (_ : ∀ i, IsFinite (j (some i) ≫ pullback.snd f U.toBase)),
      (∀ i, (j (some i) ≫ pullback.fst f U.toBase) (v i) = x i) ∧
      (∀ i, {y : P (some i) |
          (j (some i) ≫ pullback.snd f U.toBase) y = U.point} = {v i}) ∧
      (∀ i, IsIso ((j (some i) ≫ pullback.fst f U.toBase).residueFieldMap (v i))) ∧
      (∀ y : P none,
        (j none ≫ pullback.snd f U.toBase) y = U.point →
          ∀ i, (j none ≫ pullback.fst f U.toBase) y ≠ x i)
```

## Tag 02LO, a lemma

[Tag 02LO](https://stacks.math.columbia.edu/tag/02LO) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_purelyInseparable_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/PurelyInseparableDecomposition.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/PurelyInseparableDecomposition.lean#L65). References: EGA IV (18.12.1), “separated case”; EGA IV (18.12.3), “partial”.

> **Stacks Project, Tag 02LO.** Finitely many pairwise distinct isolated points of a fibre of
> a separated morphism locally of finite type split into finite open-and-closed pieces after an
> étale base change.  Each distinguished piece has singleton fibre and purely inseparable
> residue-field extension, and the residual piece contains none of the specified points.

```lean
public theorem exists_etaleNeighborhood_purelyInseparable_decomposition
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f]
    (n : ℕ) (s : S) (x : Fin n → f.fiber s) (hx : Function.Injective x)
    (hxi : ∀ i, IsIsolatedPoint (x i)) :
    ∃ (U : EtaleNeighborhood S s)
      (m : Fin n → ℕ)
      (D : Option (Σ i, Fin (m i)) → (pullback f U.toBase).Opens)
      (v : ∀ i j, D (some ⟨i, j⟩)),
      Set.PairwiseDisjoint Set.univ (fun k ↦ (D k).1) ∧
      (⋃ k, (D k).1) = Set.univ ∧
      (∀ k, IsClopen (D k).1) ∧
      (∀ i j,
        let V := D (some ⟨i, j⟩)
        let g := V.ι ≫ pullback.snd f U.toBase
        IsFinite g ∧
          g ⁻¹' {U.point} = {v i j} ∧
          (V.ι ≫ pullback.fst f U.toBase) (v i j) = f.fiberι s (x i) ∧
          ∃ hvu : g (v i j) = U.point,
            ((U.scheme.residueFieldCongr hvu).inv ≫
              g.residueFieldMap (v i j)).hom.IsPurelyInseparable) ∧
      (∀ w : D none,
        ((D none).ι ≫ pullback.snd f U.toBase) w = U.point →
          ∀ i, ((D none).ι ≫ pullback.fst f U.toBase) w ≠ f.fiberι s (x i))
```

## Tag 02LP, a lemma

[Tag 02LP](https://stacks.math.columbia.edu/tag/02LP) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_isCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/Decomposition.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/EtaleLocalizationQuasiFinite/Decomposition.lean#L461). References: EGA IV (18.12.1), “separated case”; EGA IV (18.12.3).

> **Stacks Project, Tag 02LP.** After an elementary étale base change, the isolated
> part of a fibre of a separated morphism locally of finite type splits off as a finite
> open-and-closed subscheme.  The complementary fibre has no isolated points and is empty
> when the original set-theoretic fibre is finite.

```lean
public theorem exists_elementaryEtaleNeighborhood_isCompl
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f] (s : S)
    (hfinite : {x : f.fiber s | IsIsolatedPoint x}.Finite) :
    ∃ (U : EtaleNeighborhood S s),
      U.IsElementary ∧
      ∃ (W V : (pullback f U.toBase).Opens),
        IsCompl W V ∧
        IsFinite (V.ι ≫ pullback.snd f U.toBase) ∧
        (∀ x : (W.ι ≫ pullback.snd f U.toBase).fiber U.point,
          ¬ IsIsolatedPoint x) ∧
        ((f ⁻¹' {s}).Finite →
          IsEmpty ((W.ι ≫ pullback.snd f U.toBase).fiber U.point))
```

**`AlgebraicGeometry.exists_elementaryEtale_isCompl_not_quasiFiniteAt_of_finite_isolatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/SplitFiniteFibre.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/SplitFiniteFibre.lean#L251). The attribute's comment: “the main assertion: `V ⟶ U` is finite and `W_u` has no isolated point”. References: EGA IV (18.12.1), “separated case”; EGA IV (18.12.3).

> **Stacks Project, Tag 02LP**, the main assertion. Let `f : X ⟶ S` be separated and locally of
> finite type and let `s : S` be such that the fibre `X_s` has only finitely many isolated points,
> i.e. only finitely many points of `X` over `s` at which `f` is quasi-finite. Then there is an
> elementary étale neighbourhood `(U, u)` of `s` — an étale `g : U ⟶ S` with `g u = s` inducing an
> isomorphism of residue fields — and a decomposition of `U ×_S X` into two complementary
> open-and-closed pieces `V` and `W` such that `V ⟶ U` is finite and the fibre `W_u` contains no
> isolated point, i.e. the second projection is quasi-finite at no point of `W` over `u`.

```lean
theorem exists_elementaryEtale_isCompl_not_quasiFiniteAt_of_finite_isolatedPoints
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f] {s : S}
    (hfin : {x : X | f.base x = s ∧ f.QuasiFiniteAt x}.Finite) :
    ∃ (U : Scheme.{u}) (g : U ⟶ S) (u : U), Etale g ∧ g.base u = s ∧
        IsIso (g.residueFieldMap u) ∧
      ∃ V W : (pullback f g).Opens, IsCompl V W ∧
        IsFinite (V.ι ≫ pullback.snd f g) ∧
        ∀ w : W, (pullback.snd f g).base (W.ι.base w) = u →
          ¬ (pullback.snd f g).QuasiFiniteAt (W.ι.base w)
```

**`AlgebraicGeometry.exists_elementaryEtale_isCompl_isEmpty_fiber_of_finite_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/SplitFiniteFibre.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/SplitFiniteFibre.lean#L296). The attribute's comment: “the final assertion: `W_u = ∅` when the fibre over `s` is finite”. References: EGA IV (18.12.1), “separated, finite fibre”; EGA IV (18.12.3).

> **Stacks Project, Tag 02LP**, the final assertion. Let `f : X ⟶ S` be separated and locally of
> finite type with finite fibre over `s : S`. Then there is an elementary étale neighbourhood
> `(U, u)` of `s` and a decomposition of `U ×_S X` into two complementary open-and-closed pieces `V`
> and `W` such that `V ⟶ U` is finite and `W` has no point over `u` at all.

```lean
theorem exists_elementaryEtale_isCompl_isEmpty_fiber_of_finite_fiber {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsSeparated f] {s : S}
    (hfin : (f.base ⁻¹' {s}).Finite) :
    ∃ (U : Scheme.{u}) (g : U ⟶ S) (u : U), Etale g ∧ g.base u = s ∧
        IsIso (g.residueFieldMap u) ∧
      ∃ V W : (pullback f g).Opens, IsCompl V W ∧
        IsFinite (V.ι ≫ pullback.snd f g) ∧
        ∀ w : W, (pullback.snd f g).base (W.ι.base w) ≠ u
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.41, Tag 04HF](https://stacks.math.columbia.edu/tag/04HF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
