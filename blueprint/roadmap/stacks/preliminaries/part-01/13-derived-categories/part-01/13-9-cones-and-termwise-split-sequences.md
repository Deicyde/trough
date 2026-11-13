---
declaration: section
origin: cited
lean: CochainComplex.mappingCone, CochainComplex.mappingCone.inr, CochainComplex.mappingCone.fst, CochainComplex.mappingCone.mapOfHomotopy, CochainComplex.mappingCone.trianglehMapOfHomotopy, exists_factorThrough_mappingCone, exists_factor_through_shifted_mappingCone, HomologicalComplex.Hom.IsDegreewiseSummandInclusion
statement: formalized
proof: formalized
---

# 13.9 Cones and termwise split sequences

Section 13.9 of the Stacks Project, [Tag 014D](https://stacks.math.columbia.edu/tag/014D). 15 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 014E, a definition

[Tag 014E](https://stacks.math.columbia.edu/tag/014E) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.mappingCone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L38) (StacksFrontier): “the cone C(f) of a morphism of complexes”. References: SGA 4 XVII (1.1.1); SGA 4 XVII (5.5.25.2), “partial”; SGA 4½ Etat 0 (1.2.1); SGA 5 VII (7.2.1).
- [`CochainComplex.mappingCone.inr`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.inr#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L39) (StacksFrontier): “the canonical morphism i : L → C(f)”.
- [`CochainComplex.mappingCone.fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.fst#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L40) (StacksFrontier): “the canonical morphism p : C(f) → K[1], as a cocycle of degree 1”.

## Tag 014F, a lemma

[Tag 014F](https://stacks.math.columbia.edu/tag/014F) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.mappingCone.mapOfHomotopy`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.mapOfHomotopy#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L42) (StacksFrontier): “the morphism c : C(f₁) → C(f₂) induced by a homotopy”.
- [`CochainComplex.mappingCone.trianglehMapOfHomotopy`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.trianglehMapOfHomotopy#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L44) (StacksFrontier): “(a, b, c) is a morphism of triangles in K(A)”.

## Tag 08RI, a lemma

[Tag 08RI](https://stacks.math.columbia.edu/tag/08RI) in the Stacks Project.

**`exists_factorThrough_mappingCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1190). The attribute's comment: “(1)”.

> If the composite `f ≫ g` is null-homotopic then `g` factors
> through the mapping cone of `f`, via the canonical inclusion `mappingCone.inr f`.

```lean
theorem exists_factorThrough_mappingCone
    {K L M : CochainComplex C ℤ} (f : K ⟶ L) (g : L ⟶ M)
    (H : Homotopy (f ≫ g) 0) :
    ∃ gbar : mappingCone f ⟶ M, mappingCone.inr f ≫ gbar = g
```

**`exists_factor_through_shifted_mappingCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1252). The attribute's comment: “(2)”.

> If the composite `f ≫ g` is null-homotopic then `f` factors through the shifted mapping cone
> `C(g)[-1]`, via the shifted projection `pShift g`.

```lean
theorem exists_factor_through_shifted_mappingCone
    {K L M : CochainComplex C ℤ} (f : K ⟶ L) (g : L ⟶ M)
    (H : Homotopy (f ≫ g) 0) :
    ∃ fbar : K ⟶ (CategoryTheory.shiftFunctor (CochainComplex C ℤ) (-1 : ℤ)).obj (mappingCone g),
      fbar ≫ pShift g = f
```

## Tag 014G, a definition

[Tag 014G](https://stacks.math.columbia.edu/tag/014G) in the Stacks Project.

**`HomologicalComplex.Hom.IsDegreewiseSummandInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L260). The attribute's comment: “termwise split injection: each component is isomorphic, as an arrow, to the inclusion `X ⟶ X ⊞ Z` of a direct summand”.

> A morphism of complexes `α : K ⟶ L` is a *termwise split injection* in the sense of
> [Stacks, Tag 014G] if each component `α.f n : K.X n ⟶ L.X n` is isomorphic, as an arrow, to the
> inclusion `biprod.inl : X ⟶ X ⊞ Z` of a direct summand, for some objects `X` and `Z` of the
> category. The complementary summand `Z` is required to exist in the category; this is stronger
> than `IsDegreewiseSplitMono` unless idempotents split
> (`isDegreewiseSummandInclusion_iff_isDegreewiseSplitMono`, in
> `StacksFrontier.Algebra.Homology.HomotopyCategory.DegreewiseSummand`).

```lean
public def IsDegreewiseSummandInclusion (α : K ⟶ L) : Prop
```

**`HomologicalComplex.Hom.IsDegreewiseSummandProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L272). The attribute's comment: “termwise split surjection: each component is isomorphic, as an arrow, to the projection `X ⊞ Z ⟶ X` onto a direct summand”.

> A morphism of complexes `β : K ⟶ L` is a *termwise split surjection* in the sense of
> [Stacks, Tag 014G] if each component `β.f n : K.X n ⟶ L.X n` is isomorphic, as an arrow, to the
> projection `biprod.fst : X ⊞ Z ⟶ X` onto a direct summand, for some objects `X` and `Z` of the
> category. The complementary summand `Z` is required to exist in the category; this is stronger
> than `IsDegreewiseSplitEpi` unless idempotents split
> (`isDegreewiseSummandProjection_iff_isDegreewiseSplitEpi`, in
> `StacksFrontier.Algebra.Homology.HomotopyCategory.DegreewiseSummand`).

```lean
public def IsDegreewiseSummandProjection (β : K ⟶ L) : Prop
```

## Tag 014H, a lemma

[Tag 014H](https://stacks.math.columbia.edu/tag/014H) in the Stacks Project.

**`exists_homotopic_comm_of_isTermwiseSplitInjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1106). The attribute's comment: “(1)”.

> Consider a square
>
>       A ---f---> B
>       |          |
>       a          b
>       |          |
>       v          v
>       C ---g---> D
>
> of morphisms of cochain complexes that commutes up to homotopy
> (`b ∘ f ∼ g ∘ a`, i.e. `Nonempty (Homotopy (f ≫ b) (a ≫ g))`). If `f` is a
> termwise split injection, then there is a morphism `b'` homotopic to `b` such
> that the square commutes on the nose: `b' ∘ f = g ∘ a` (`f ≫ b' = a ≫ g`).

```lean
theorem exists_homotopic_comm_of_isTermwiseSplitInjection {Ac Bc Cc Dc : CochainComplex 𝒜 ℤ}
    (f : Ac ⟶ Bc) (a : Ac ⟶ Cc) (b : Bc ⟶ Dc) (g : Cc ⟶ Dc)
    (hsq : Nonempty (Homotopy (f ≫ b) (a ≫ g)))
    (hf : IsTermwiseSplitInjection f) :
    ∃ b' : Bc ⟶ Dc, Nonempty (Homotopy b' b) ∧ f ≫ b' = a ≫ g
```

**`exists_homotopic_comm_of_isTermwiseSplitSurjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1122). The attribute's comment: “(2)”.

> Consider a square of morphisms of cochain complexes `f : A ⟶ B`, `a : A ⟶ C`, `b : B ⟶ D`,
> `g : C ⟶ D` that commutes up to homotopy (`Nonempty (Homotopy (f ≫ b) (a ≫ g))`). If `g` is a
> termwise split surjection, then there is a morphism `a'` homotopic to `a` such that the square
> commutes on the nose: `g ∘ a' = b ∘ f` (`a' ≫ g = f ≫ b`).

```lean
theorem exists_homotopic_comm_of_isTermwiseSplitSurjection {Ac Bc Cc Dc : CochainComplex 𝒜 ℤ}
    (f : Ac ⟶ Bc) (a : Ac ⟶ Cc) (b : Bc ⟶ Dc) (g : Cc ⟶ Dc)
    (hsq : Nonempty (Homotopy (f ≫ b) (a ≫ g)))
    (hg : IsTermwiseSplitSurjection g) :
    ∃ a' : Ac ⟶ Cc, Nonempty (Homotopy a' a) ∧ a' ≫ g = f ≫ b
```

## Tag 013N, a lemma

[Tag 013N](https://stacks.math.columbia.edu/tag/013N) in the Stacks Project.

**`CochainComplex.exists_factorization_isDegreewiseSplitMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L433).

> Let `α : K ⟶ L` be a morphism of cochain complexes of an additive category. Then there are a
> complex `L'`, a factorization `α = α' ≫ π` of `α` through `L'` with `α'` a termwise split
> injection, and a section `s : L ⟶ L'` of `π` with `π ≫ s` homotopic to `𝟙 L'`. Moreover `L'`
> inherits the vanishing bounds of `K` and `L`, so that `L'` is bounded below, bounded above or
> bounded as soon as both `K` and `L` are.

```lean
public theorem exists_factorization_isDegreewiseSplitMono {A : Type*} [Category A]
    [Preadditive A] [HasBinaryBiproducts A] {K L : CochainComplex A ℤ} (α : K ⟶ L) :
    ∃ (L' : CochainComplex A ℤ) (α' : K ⟶ L') (π : L' ⟶ L) (s : L ⟶ L'),
      α' ≫ π = α ∧ α'.IsDegreewiseSplitMono ∧ s ≫ π = 𝟙 L ∧
        Nonempty (Homotopy (π ≫ s) (𝟙 L')) ∧
        (∀ a : ℤ, K.IsStrictlyGE (a + 1) → L.IsStrictlyGE a → L'.IsStrictlyGE a) ∧
        (∀ a : ℤ, K.IsStrictlyLE a → L.IsStrictlyLE a → L'.IsStrictlyLE a)
```

## Tag 0642, a lemma

[Tag 0642](https://stacks.math.columbia.edu/tag/0642) in the Stacks Project.

**`CochainComplex.exists_isDegreewiseSplitEpi_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L524).

> Let `α : K ⟶ L` be a morphism of cochain complexes of an additive category. Then there are a
> complex `K'`, a factorization `α = i ≫ α'` of `α` through `K'` with `α'` a termwise split
> surjection, and a retraction `s : K' ⟶ K` of `i` with `s ≫ i` homotopic to `𝟙 K'`. Moreover `K'`
> inherits the vanishing bounds of `K` and `L`, so that `K'` is bounded below, bounded above or
> bounded as soon as both `K` and `L` are.

```lean
public theorem exists_isDegreewiseSplitEpi_factorization [HasBinaryBiproducts A]
    {K L : CochainComplex A ℤ} (α : K ⟶ L) :
    ∃ (K' : CochainComplex A ℤ) (i : K ⟶ K') (α' : K' ⟶ L) (s : K' ⟶ K),
      i ≫ α' = α ∧ α'.IsDegreewiseSplitEpi ∧ i ≫ s = 𝟙 K ∧
        Nonempty (Homotopy (s ≫ i) (𝟙 K')) ∧
        (∀ a : ℤ, K.IsStrictlyGE a → L.IsStrictlyGE a → K'.IsStrictlyGE a) ∧
        (∀ a : ℤ, K.IsStrictlyLE a → L.IsStrictlyLE (a - 1) → K'.IsStrictlyLE a)
```

## Tag 014I, a definition

[Tag 014I](https://stacks.math.columbia.edu/tag/014I) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.Splitting`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.Splitting#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L46) (StacksFrontier): “the given direct sum decompositions `B^n = A^n ⊕ C^n` compatible with `α^n` and `β^n` (with `s^n` and `π^n`): a termwise split exact sequence is a short complex `S` of cochain complexes with a splitting `σ n : (S.map (eval _ _ n)).Splitting` in each degree”.
- [`CochainComplex.homOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.homOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L50) (StacksFrontier): “the associated morphism of complexes `δ : C^• → A^•[1]`”.
- [`CochainComplex.homOfDegreewiseSplit_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.homOfDegreewiseSplit_f#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L52) (StacksFrontier): “the degree-`n` component of `δ`, `π^{n+1} ∘ d_B^n ∘ s^n`: it is the `(n, n+1)` component of `cocycleOfDegreewiseSplit`”.
- [`CochainComplex.cocycleOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.cocycleOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L55) (StacksFrontier): “the cocycle `(σ p).s ≫ d_B ≫ (σ q).r` underlying `δ`”.
- [`CochainComplex.triangleOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.triangleOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch13.lean#L57) (StacksFrontier): “the triangle `(A^•, B^•, C^•, α, β, δ)` associated to the termwise split sequence”.

## Tag 05SS, a lemma

[Tag 05SS](https://stacks.math.columbia.edu/tag/05SS) in the Stacks Project.

**`trianglehOfDegreewiseSplit_iso_of_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1161). References: SGA 4½ Etat 0 (1.2.4).

> The triangles in `K(𝒜)` attached to two families of degreewise splittings of a short complex
> `S` of cochain complexes are equal, so they are isomorphic by an isomorphism whose three
> components are the identities of `Q.obj S.X₁`, `Q.obj S.X₂`, `Q.obj S.X₃`. Equality transports
> express these identities between the canonically equal objects of the two triangles.

```lean
theorem trianglehOfDegreewiseSplit_iso_of_identity
    {C : Type*} [Category C] [Preadditive C]
    (S : ShortComplex (CochainComplex C ℤ))
    (σ σ' : (n : ℤ) → (S.map (HomologicalComplex.eval C (ComplexShape.up ℤ) n)).Splitting) :
    ∃ e : CochainComplex.trianglehOfDegreewiseSplit S σ ≅
          CochainComplex.trianglehOfDegreewiseSplit S σ',
      e.hom.hom₁ = eqToHom (by simp) ∧ e.hom.hom₂ = eqToHom (by simp) ∧
        e.hom.hom₃ = eqToHom (by simp)
```

## Tag 086L, a lemma

[Tag 086L](https://stacks.math.columbia.edu/tag/086L) in the Stacks Project.

**`HomotopyCategory.comp_eq_zero_of_degreewiseSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L375).

> Let `S : 0 → A → B → C → 0` be a termwise split exact sequence of complexes in a preadditive
> category `𝒜`, with a splitting `σ i` in each degree. If `b : K ⟶ B` and `b' : B ⟶ L` are
> morphisms of the homotopy category `K(𝒜)` with `b ≫ (B → C) = 0` and `(A → B) ≫ b' = 0`, then
> `b' ∘ b = 0` in `K(𝒜)`.

```lean
public theorem comp_eq_zero_of_degreewiseSplit
    {S : ShortComplex (HomologicalComplex 𝒜 c)}
    (σ : ∀ i, (S.map (HomologicalComplex.eval 𝒜 c i)).Splitting)
    {K L : HomotopyCategory 𝒜 c}
    (b : K ⟶ (quotient 𝒜 c).obj S.X₂) (b' : (quotient 𝒜 c).obj S.X₂ ⟶ L)
    (hb : b ≫ (quotient 𝒜 c).map S.g = 0) (hb' : (quotient 𝒜 c).map S.f ≫ b' = 0) :
    b ≫ b' = 0
```

## Tag 014K, a lemma

[Tag 014K](https://stacks.math.columbia.edu/tag/014K) in the Stacks Project.

**`CochainComplex.mappingCone.isIso₃_of_isIso₁₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 709](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L709).

> Let `f₁ : K₁ ⟶ L₁` and `f₂ : K₂ ⟶ L₂` be morphisms of cochain complexes of an additive
> category `𝒜`, and let `φ = (a, b, c)` be a morphism of triangles of the homotopy category `K(𝒜)`
> from the cone triangle `K₁ ⟶ L₁ ⟶ C(f₁) ⟶ K₁⟦1⟧` of `f₁` to the cone triangle of `f₂`. If `a`
> and `b` are homotopy equivalences, i.e. isomorphisms in `K(𝒜)`, then so is `c`.

```lean
public theorem isIso₃_of_isIso₁₂ [HasZeroObject 𝒜] [HasBinaryBiproducts 𝒜]
    {K₁ L₁ K₂ L₂ : CochainComplex 𝒜 ℤ} {f₁ : K₁ ⟶ L₁} {f₂ : K₂ ⟶ L₂}
    (φ : triangleh f₁ ⟶ triangleh f₂) (h₁ : IsIso φ.hom₁) (h₂ : IsIso φ.hom₂) :
    IsIso φ.hom₃
```

## Tag 014L, a lemma

[Tag 014L](https://stacks.math.columbia.edu/tag/014L) in the Stacks Project.

**`CochainComplex.exists_triangleh_iso_trianglehOfDegreewiseSplit_and_exists_iso_triangleh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 944](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L944). References: SGA 4 XVII (1.1.1), “both final assertions”; SGA 7 XIII (1.4.2), “partial”.

> Let `𝒜` be an additive category.
>
> (1) Given a termwise split exact sequence of cochain complexes — a short complex `S` together
> with a splitting `σ n` of each of its degreewise evaluations — the cone triangle
> `S.X₁ → S.X₂ → C(S.f) --(-p)--> S.X₁[1]` of its first map is isomorphic in `K(𝒜)` to the triangle
> `S.X₁ → S.X₂ → S.X₃ --δ--> S.X₁[1]` associated to the sequence, by an isomorphism of triangles
> which is the identity on `S.X₁` and on `S.X₂` and whose third component is the class of the
> canonical morphism `C(S.f) ⟶ S.X₃` given by the projection onto `S.X₂` followed by `S.g`; in
> particular that canonical morphism is a homotopy equivalence.
>
> (2) Given a morphism of cochain complexes `f : K ⟶ L`, there are a termwise split exact sequence
> `K → L̃ → M` starting at `K` and an isomorphism in `K(𝒜)` from its associated triangle
> `K → L̃ → M --δ--> K[1]` to the cone triangle `K → L → C(f) --(-p)--> K[1]` of `f` which is the
> identity on `K`.

```lean
public theorem exists_triangleh_iso_trianglehOfDegreewiseSplit_and_exists_iso_triangleh
    {𝒜 : Type*} [Category 𝒜] [Preadditive 𝒜] [HasZeroObject 𝒜] [HasBinaryBiproducts 𝒜] :
    (∀ (S : ShortComplex (CochainComplex 𝒜 ℤ))
        (σ : ∀ n, (S.map (eval 𝒜 (ComplexShape.up ℤ) n)).Splitting),
        ∃ e : mappingCone.triangleh S.f ≅ trianglehOfDegreewiseSplit S σ,
          e.hom.hom₁ = 𝟙 ((HomotopyCategory.quotient 𝒜 (ComplexShape.up ℤ)).obj S.X₁) ∧
            e.hom.hom₂ = 𝟙 ((HomotopyCategory.quotient 𝒜 (ComplexShape.up ℤ)).obj S.X₂) ∧
            e.hom.hom₃ = (HomotopyCategory.quotient 𝒜 (ComplexShape.up ℤ)).map
              (mappingCone.desc S.f 0 S.g (by simp))) ∧
      ∀ {K L : CochainComplex 𝒜 ℤ} (f : K ⟶ L),
        ∃ (L' M : CochainComplex 𝒜 ℤ) (f' : K ⟶ L') (g : L' ⟶ M) (w : f' ≫ g = 0)
          (σ : ∀ n, ((ShortComplex.mk f' g w).map (eval 𝒜 (ComplexShape.up ℤ) n)).Splitting)
          (e : trianglehOfDegreewiseSplit (ShortComplex.mk f' g w) σ ≅ mappingCone.triangleh f),
          e.hom.hom₁ = 𝟙 ((HomotopyCategory.quotient 𝒜 (ComplexShape.up ℤ)).obj K)
```

## Tag 014M, a lemma

[Tag 014M](https://stacks.math.columbia.edu/tag/014M) in the Stacks Project.

**`CochainComplex.exists_composableArrows_isDegreewiseSplitMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 678](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L678).

> Let `F : A₀ ⟶ A₁ ⟶ ⋯ ⟶ Aₙ` be a sequence of composable morphisms of cochain complexes of an
> additive category. Then there are a sequence `G : B₀ ⟶ B₁ ⟶ ⋯ ⟶ Bₙ` and a morphism of diagrams
> `φ : G ⟶ F` such that each `Bᵢ ⟶ Bᵢ₊₁` is a termwise split injection and each `Bᵢ ⟶ Aᵢ` is a
> homotopy equivalence. Moreover, if all the `Aᵢ` are bounded below (resp. bounded above), then so
> are all the `Bᵢ`.

```lean
public theorem exists_composableArrows_isDegreewiseSplitMono {n : ℕ}
    (F : ComposableArrows (CochainComplex A ℤ) n) :
    ∃ (G : ComposableArrows (CochainComplex A ℤ) n) (φ : G ⟶ F),
      (∀ (i : ℕ) (_ : i + 1 ≤ n), (G.map' i (i + 1)).IsDegreewiseSplitMono) ∧
      (∀ i, HomologicalComplex.homotopyEquivalences A (ComplexShape.up ℤ) (φ.app i)) ∧
      ((∀ i, CochainComplex.plus A (F.obj i)) → ∀ i, CochainComplex.plus A (G.obj i)) ∧
      ((∀ i, CochainComplex.minus A (F.obj i)) → ∀ i, CochainComplex.minus A (G.obj i))
```

## Tag 014N, a lemma

[Tag 014N](https://stacks.math.columbia.edu/tag/014N) in the Stacks Project.

**`CochainComplex.exists_triangleOfDegreewiseSplit_invRotate_iso_mappingCone_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 1053](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L1053).

> Let `𝒜` be an additive category and let `S` be a termwise split short exact sequence of
> cochain complexes of `𝒜`, split by `σ`, with associated triangle
> `S.X₁ → S.X₂ → S.X₃ --δ--> S.X₁[1]` (`CochainComplex.triangleOfDegreewiseSplit`). Then the
> inverse rotation `S.X₃[-1] --δ[-1]--> S.X₁ --S.f--> S.X₂` of that triangle is isomorphic, by an
> isomorphism of triangles of complexes which is the identity on `S.X₃[-1]` and on `S.X₁`, to the
> cone triangle `S.X₃[-1] --δ[-1]--> S.X₁ --i--> C(δ[-1]) --(-p)--> S.X₃[-1][1]` of its own first
> map.

```lean
public theorem exists_triangleOfDegreewiseSplit_invRotate_iso_mappingCone_triangle
    (S : ShortComplex (CochainComplex 𝒜 ℤ))
    (σ : ∀ n, (S.map (eval 𝒜 (ComplexShape.up ℤ) n)).Splitting) :
    ∃ e : (triangleOfDegreewiseSplit S σ).invRotate ≅
        mappingCone.triangle (triangleOfDegreewiseSplit S σ).invRotate.mor₁,
      e.hom.hom₁ = 𝟙 ((triangleOfDegreewiseSplit S σ).invRotate.obj₁) ∧
        e.hom.hom₂ = 𝟙 S.X₁
```

## Tag 014O, a lemma

[Tag 014O](https://stacks.math.columbia.edu/tag/014O) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.mappingCone.triangleRotateIsoTriangleOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.triangleRotateIsoTriangleOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L721) (StacksFrontier): “the rotated cone triangle is the triangle of a termwise split sequence”.
- [`CochainComplex.mappingCone.triangleRotateShortComplexSplitting`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.mappingCone.triangleRotateShortComplexSplitting#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 723](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L723) (StacksFrontier): “the degreewise splitting of that sequence”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.9, Tag 014D](https://stacks.math.columbia.edu/tag/014D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
