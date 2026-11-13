---
declaration: section
origin: cited
lean: HomologicalComplex.cylinder.exists_map_descEquiv, CochainComplex.diamond.exists_unique_comparison, CategoryTheory.SimplicialObject.exists_homotopy_of_homotopy_normalizedMooreComplex_map
statement: formalized
proof: formalized
---

# 14.29 More homotopies in abelian categories

Section 14.29 of the Stacks Project, [Tag 01A1](https://stacks.math.columbia.edu/tag/01A1). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01A2, a lemma

[Tag 01A2](https://stacks.math.columbia.edu/tag/01A2) in the Stacks Project.

**`HomologicalComplex.cylinder.exists_map_descEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean#L188).

> **Stacks 01A2**.
> Let `C` be an additive category and `c` a complex shape in which every index is the target of a
> relation (as for chain complexes). Then the cylinder `⋄K = K.cylinder` of a complex `K` represents
> the functor `M ↦ {(a, b, h) | a, b : K ⟶ M and h a homotopy from a to b}`: the map sending
> `f : ⋄K ⟶ M` to the triple obtained by composing the two inclusions `ι₀ K, ι₁ K : K ⟶ ⋄K` and the
> canonical homotopy between them with `f` is a bijection. Moreover `K ↦ ⋄K` is functorial, by the
> unique action on morphisms compatible with the inclusions and with the canonical homotopy.

```lean
public theorem exists_map_descEquiv (hc : ∀ j, ∃ i, c.Rel i j) :
    ∃ map : ∀ (K L : HomologicalComplex C c), (K ⟶ L) → (K.cylinder ⟶ L.cylinder),
      (∀ K : HomologicalComplex C c, map K K (𝟙 K) = 𝟙 K.cylinder) ∧
      (∀ (K L M : HomologicalComplex C c) (φ : K ⟶ L) (ψ : L ⟶ M),
        map K M (φ ≫ ψ) = map K L φ ≫ map L M ψ) ∧
      (∀ (K L : HomologicalComplex C c) (φ : K ⟶ L), ι₀ K ≫ map K L φ = φ ≫ ι₀ L) ∧
      (∀ (K L : HomologicalComplex C c) (φ : K ⟶ L), ι₁ K ≫ map K L φ = φ ≫ ι₁ L) ∧
      (∀ (K L : HomologicalComplex C c) (φ : K ⟶ L) (i j : ι) (hij : c.Rel j i),
        inlX K i j hij ≫ (map K L φ).f j = φ.f i ≫ inlX L i j hij) ∧
      ∀ K M : HomologicalComplex C c,
        ∃ e : (Σ (a : K ⟶ M) (b : K ⟶ M), Homotopy a b) ≃ (K.cylinder ⟶ M),
          ∀ x : Σ (a : K ⟶ M) (b : K ⟶ M), Homotopy a b,
            ι₀ K ≫ e x = x.1 ∧ ι₁ K ≫ e x = x.2.1 ∧
              ∀ (i j : ι) (hij : c.Rel j i),
                inlX K i j hij ≫ (e x).f j = x.2.2.hom i j
```

## Tag 01A3, a lemma

[Tag 01A3](https://stacks.math.columbia.edu/tag/01A3) in the Stacks Project.

**`CochainComplex.diamond.exists_unique_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean, line 1260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean#L1260).

> **Stacks 01A3**.
> Let `0 → A ⊕ A → B → Cpx → 0` be a short exact sequence of complexes, split in each degree by
> `s n : Cpx_n ⟶ B_n`. If the associated connecting morphism `δ(s) : Cpx → A[-1] ⊕ A[-1]` factors
> through `(1, -1) : A[-1] → A[-1] ⊕ A[-1]` as `δ(s) = (1, -1) ∘ f`, then there is a unique morphism
> `φ : B ⟶ ⋄A` fitting into a commutative diagram of the two short exact sequences whose vertical
> maps are compatible with the splittings `s n` and `σ A n`.

```lean
theorem exists_unique_comparison
    (A B Cpx : CochainComplex C ℤ)
    (i : double A ⟶ B) (r : B ⟶ Cpx)
    (p q : ∀ n, B.X n ⟶ A.X n) (s : ∀ n, Cpx.X n ⟶ B.X n)
    (f : Cpx ⟶ shift1 A)
    -- degreewise biproduct splitting `B_n ≅ (A_n ⊕ A_n) ⊕ C_n`
    (hsr : ∀ n, s n ≫ r.f n = 𝟙 _)
    (hip : ∀ n, i.f n ≫ biprod.lift (p n) (q n) = 𝟙 _)
    (hsplit : ∀ n,
      biprod.lift (p n) (q n) ≫ i.f n + r.f n ≫ s n = 𝟙 (B.X n))
    -- the factorization `δ(s) = (1,-1) ∘ f`
    (hfac1 : ∀ n, s n ≫ B.d n (n + 1) ≫ p (n + 1) = f.f n)
    (hfac2 : ∀ n, s n ≫ B.d n (n + 1) ≫ q (n + 1) = -(f.f n)) :
    ∃! φ : B ⟶ diamond A,
      (i ≫ φ = ι A) ∧
      (φ ≫ ρ A = r ≫ f) ∧
      (∀ n, s n ≫ φ.f n = f.f n ≫ σ A n)
```

## Tag 01A4, a lemma

[Tag 01A4](https://stacks.math.columbia.edu/tag/01A4) in the Stacks Project.

**`CategoryTheory.SimplicialObject.exists_homotopy_of_homotopy_normalizedMooreComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean, line 800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopyLift.lean#L800). The attribute's comment: “the homotopy of 019K is presented by the family of components `h_{n + 1, i + 1} ∘ sⁿᵢ` it corresponds to under 019L, which is Mathlib's `SimplicialObject.Homotopy`, and out of which the chain homotopy `s(h)` of 019Q is built; `N(h)` is `s(h)` conjugated by the canonical splitting `N ⊆ s` of 019A”.

> **Stacks 01A4**.
> Let `a, b : U ⟶ V` be morphisms of simplicial objects of an abelian category and let `H` be a chain
> homotopy between the induced maps `N(a), N(b) : N(U) ⟶ N(V)` of normalized Moore complexes. Then
> `a` and `b` are simplicially homotopic, and moreover the homotopy `K` can be chosen so that the
> chain homotopy it induces on normalized Moore complexes is `H` itself: `Hₙ = p_V ∘ s(K)ₙ ∘ ι_U`,
> where `s(K)` is the chain homotopy of `K` on the alternating face map complexes
> ([Stacks, Tag 019Q]) and `ι_U`, `p_V` are the canonical inclusion of and projection onto the
> normalized Moore complex. By [Stacks, Tag 019L] such a `K` is the same thing as a homotopy
> `h : U × Δ[1] ⟶ V` from `a` to `b` in the sense of [Stacks, Tag 019K], with
> `K.h i = sⁿᵢ ≫ h_{n + 1, i + 1}`.

```lean
public theorem exists_homotopy_of_homotopy_normalizedMooreComplex_map
    (H : _root_.Homotopy ((normalizedMooreComplex A).map a) ((normalizedMooreComplex A).map b)) :
    ∃ K : Homotopy a b, ∀ n : ℕ, H.hom n (n + 1) =
      (inclusionOfMooreComplexMap U).f n ≫ K.toChainHomotopy.hom n (n + 1) ≫
        (PInftyToNormalizedMooreComplex V).f (n + 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.29, Tag 01A1](https://stacks.math.columbia.edu/tag/01A1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
