---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_etaleNeighborhood_openCopies_cover_fibers, AlgebraicGeometry.exists_etaleNeighborhood_disjoint_openCopies_decomposition, Stacks.Etale.exists_etale_pullback_iso_sigma, Stacks.Etale.exists_etaleCover_pullback_iso_sigma, Stacks.Etale.exists_isSplitOver
statement: formalized
proof: formalized
---

# 41.18 Étale local structure of étale morphisms

Section 41.18 of the Stacks Project, [Tag 04HK](https://stacks.math.columbia.edu/tag/04HK). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04HL, a lemma

[Tag 04HL](https://stacks.math.columbia.edu/tag/04HL) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_openCopies_cover_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalStructure/OpenCopies.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalStructure/OpenCopies.lean#L134).

> **Stacks Project, Tag 04HL.** A morphism which is étale at finitely many distinct points of
> one fibre admits, after an étale base change, open subschemes of the base change which map
> isomorphically onto the new base, meet one another nowhere over the distinguished point, and
> together contain every point of that fibre lying over one of the given points.

```lean
public theorem exists_etaleNeighborhood_openCopies_cover_fibers
    {X S : Scheme.{u}} (f : X ⟶ S) (n : ℕ) (x : Fin n → X) (s : S)
    (hinj : Function.Injective x) (hx : ∀ i, f (x i) = s) (hetale : ∀ i, EtaleAt f (x i)) :
    ∃ (U : EtaleNeighborhood S s) (m : Fin n → ℕ)
      (V : (Σ i, Fin (m i)) → (pullback f U.toBase).Opens),
      (∀ a, IsIso ((V a).ι ≫ pullback.snd f U.toBase)) ∧
      (∀ a b, a ≠ b → ∀ z : (pullback f U.toBase : Scheme.{u}),
        z ∈ (V a).1 → z ∈ (V b).1 → pullback.snd f U.toBase z ≠ U.point) ∧
      (∀ i (z : (pullback f U.toBase : Scheme.{u})),
        pullback.snd f U.toBase z = U.point → pullback.fst f U.toBase z = x i →
          ∃ j : Fin (m i), z ∈ (V ⟨i, j⟩).1)
```

## Tag 04HM, a lemma

[Tag 04HM](https://stacks.math.columbia.edu/tag/04HM) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_disjoint_openCopies_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalStructure/DisjointDecomposition.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/LocalStructure/DisjointDecomposition.lean#L406).

> **Stacks Project, Tag 04HM.** After an étale base change, a separated morphism which is étale
> at finitely many points over one point of the base is the disjoint union of copies of the new
> base together with a remainder whose distinguished fibre contains none of those points. If the
> given points exhaust the original fibre, that remaining fibre is empty.

```lean
public theorem exists_etaleNeighborhood_disjoint_openCopies_decomposition
    {X S : Scheme.{u}} (f : X ⟶ S) [IsSeparated f] (n : ℕ) (x : Fin n → X) (s : S)
    (hx : ∀ i, f (x i) = s) (hetale : ∀ i, EtaleAt f (x i)) :
    ∃ (U : EtaleNeighborhood S s) (W : (pullback f U.toBase).Opens) (m : Fin n → ℕ)
      (V : (Σ i, Fin (m i)) → (pullback f U.toBase).Opens),
      sSup (Set.range V) ⊔ W = ⊤ ∧ Pairwise (Disjoint on V) ∧ (∀ a, Disjoint (V a) W) ∧
        (∀ a, IsIso ((V a).ι ≫ pullback.snd f U.toBase)) ∧
        (∀ (z : (W.ι ≫ pullback.snd f U.toBase).fiber U.point) (i : Fin n),
          ((W.ι ≫ pullback.snd f U.toBase).fiberι U.point ≫ W.ι ≫
            pullback.fst f U.toBase) z ≠ x i) ∧
        ((∀ y : X, f y = s → ∃ i, y = x i) →
          IsEmpty ((W.ι ≫ pullback.snd f U.toBase).fiber U.point))
```

## Tag 04HN, a lemma

[Tag 04HN](https://stacks.math.columbia.edu/tag/04HN) in the Stacks Project.

**`Stacks.Etale.exists_etale_pullback_iso_sigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleLocal.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleLocal.lean#L243).

> Let `f : X ⟶ S` be a finite étale morphism of schemes and let `s : S`. There is an étale
> neighbourhood `g : U ⟶ S` of `s`, a finite index type `ι` and an isomorphism
> `X ×_S U ≅ ∐_{i : ι} U` over `U`; that is, `X` becomes a finite disjoint union of copies of the
> base, each mapping isomorphically onto it, after an étale base change near `s`.

```lean
theorem exists_etale_pullback_iso_sigma {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f] [Etale f]
    (s : S) :
    ∃ (U : Scheme.{u}) (g : U ⟶ S) (_ : Etale g) (u : U) (_ : g u = s) (ι : Type u)
      (_ : Finite ι) (e : pullback f g ≅ ∐ fun _ : ι ↦ U),
      e.hom ≫ Limits.Sigma.desc (fun _ ↦ 𝟙 U) = pullback.snd f g
```

**`Stacks.Etale.exists_etaleCover_pullback_iso_sigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleLocal.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleLocal.lean#L254). The attribute's comment: “étale covering form”.

> A finite étale morphism `f : X ⟶ S` admits an étale covering `𝒰` of `S` together with, for
> each member `i`, a finite index type `ι i` and an isomorphism `X ×_S 𝒰.X i ≅ ∐_{ι i} 𝒰.X i` over
> `𝒰.X i`.

```lean
theorem exists_etaleCover_pullback_iso_sigma {X S : Scheme.{u}} (f : X ⟶ S)
    [IsFinite f] [Etale f] :
    ∃ (𝒰 : S.Cover.{u} (Scheme.precoverage @Etale)) (ι : 𝒰.I₀ → Type u)
      (_ : ∀ i, Finite (ι i)) (e : ∀ i, pullback f (𝒰.f i) ≅ ∐ fun _ : ι i ↦ 𝒰.X i),
      ∀ i, (e i).hom ≫ Limits.Sigma.desc (fun _ ↦ 𝟙 (𝒰.X i)) = pullback.snd f (𝒰.f i)
```

**`Stacks.Etale.exists_isSplitOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SplitOver.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SplitOver.lean#L177). The attribute's comment: “sheets over an étale neighbourhood”.

> **Stacks 04HN**, in terms of sheets. Let `f : X ⟶ S` be finite étale and let `q : V ⟶ S`
> be any scheme over `S`. Every point of `V` has an étale neighbourhood `g : W ⟶ V` over which
> `f` has sheet data.

```lean
public theorem exists_isSplitOver {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f] [Etale f]
    {V : Scheme.{u}} (q : V ⟶ S) (v : V) :
    ∃ (W : Scheme.{u}) (g : W ⟶ V) (_ : Etale g) (w : W) (_ : g w = v),
      Nonempty (IsSplitOver f (g ≫ q))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.18, Tag 04HK](https://stacks.math.columbia.edu/tag/04HK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
