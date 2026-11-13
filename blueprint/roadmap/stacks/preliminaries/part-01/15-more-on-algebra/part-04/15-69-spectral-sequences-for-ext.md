---
declaration: section
origin: cited
lean: StacksDraft.ExtSpectralSequence.exists_ext_homology_spectralSequence, StacksDraft.ExtSpectralSequence.exists_ext_complex_spectralSequence
statement: formalized
proof: formalized
---

# 15.69 Spectral sequences for Ext

Section 15.69 of the Stacks Project, [Tag 0AVG](https://stacks.math.columbia.edu/tag/0AVG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AVH, an equation

[Tag 0AVH](https://stacks.math.columbia.edu/tag/0AVH) in the Stacks Project.

**`StacksDraft.ExtSpectralSequence.exists_ext_homology_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Ext/SpectralSequence.lean, line 794](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Ext/SpectralSequence.lean#L794).

> **Stacks 0AVH.** For `M` in an abelian category with enough injectives and `K` in its bounded
> below derived category, there is a filtered complex `T` of abelian groups, together with the
> filtration, cycle, boundary and induced-filtration data `Fil`, `Z`, `D`, `FH` of
> [Stacks, Tag 012M], a spectral sequence `E` whose page at `(r, p, q)` is identified with the
> canonical subquotient `Z_r^{p,q}/(D_r^{p,q} ⊓ Z_r^{p,q})` and whose differential is induced by the
> differential of `T`, and isomorphisms `Hⁿ(T) ≅ Extⁿ(M, K)` and `E₂ⁱʲ ≅ Extⁱ(M, Hʲ(K))`, the latter
> factoring through the canonical page-`2` subquotient. The spectral sequence is bounded, the
> filtration it induces on each `Hⁿ(T)` is finite, it converges to `H^*(T)` (the differentials
> vanish for `r ≫ 0` and the inclusions (012S) and (012T) for the stable cycles and boundaries are
> equalities, which by [Stacks, Tag 012V] says exactly that `E_∞^{p,q}` is the graded piece
> `gr^pHⁿ(T)`), and on each total-degree diagonal every page vanishes outside a finite range of
> columns, so the spectral sequence degenerates there.
>
> `T` is `Tot(Hom(M, I))` for `I` a Cartan-Eilenberg resolution ([Stacks, Tag 015I]) of a bounded
> below complex of injective objects representing `K`, filtered by the second coordinate; the pages
> are identified by [Stacks, Tag 0130] and the second page is rewritten with [Stacks, Tag 015J] and
> `StacksDraft.DerivedCoyoneda.rightDerivedSmallCoyonedaIso`. The column vanishing is deduced from
> the finiteness of the diagonals of the zeroth page, which propagates to every later page because
> each page object is the homology of the previous one
> (`CategoryTheory.SpectralSequence.isZero_page_of_le`); it does not involve the stable cycles.
>
> This is the `0AVH` endpoint; `exists_ext_homology_spectralSequence_of_data` is the same statement
> with `Fil`, `Z`, `D`, `FH` universally quantified, with the `e₂`/`filteredE₂Iso` compatibility,
> the differential compatibility and the column-vanishing conjuncts dropped, and with `E₂`
> identified with `Ext` by an isomorphism not tied to the canonical subquotient.

```lean
public theorem exists_ext_homology_spectralSequence
    (C : Type u) [Category.{v} C] [Abelian C] [EnoughInjectives C]
    [HasDerivedCategory.{w} C] (M : C) (K : DerivedCategory.Plus C) :
    ∃ (T : FilteredObject (CochainComplex AddCommGrpCat.{w} ℤ) ℤᵒᵖ)
      (Fil : ∀ (_p n : ℤ), Subobject (T.X.X n))
      (_hFil : ∀ p n : ℤ, Fil p n = Subobject.mk ((T.filtration.ι.app (op p)).f n))
      (Z : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
      (_hZ : ∀ r p n : ℤ, Z r p n =
        Fil p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
      (D : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
      (_hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
        (Subobject.«exists» (T.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
      (FH : ∀ (n _p : ℤ), Subobject (T.X.homology n))
      (_hFH : ∀ n p : ℤ, FH n p =
        imageSubobject (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))
      (E : CohomologicalSpectralSequence AddCommGrpCat.{w} 0)
      (pageIso : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
        cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
      (filteredE₂Iso : ∀ i j : ℤ,
        cokernel (Subobject.ofLE _ _
            (inf_le_right : D 2 i (i + j) ⊓ Z 2 i (i + j) ≤ Z 2 i (i + j))) ≅
          AddCommGrpCat.of (Abelian.zExt.{u, v, w} M
            ((DerivedCategory.homologyFunctor.{w, v, u} C j).obj
              (DerivedCategory.Plus.ι.{w, v, u}.obj K)) i))
      (e₂ : ∀ i j : ℤ, (E.page 2 zero_le_two).X (i, j) ≅
        AddCommGrpCat.of (Abelian.zExt.{u, v, w} M
          ((DerivedCategory.homologyFunctor.{w, v, u} C j).obj
            (DerivedCategory.Plus.ι.{w, v, u}.obj K)) i))
      (_abutmentIso : ∀ n : ℤ, T.X.homology n ≅
        AddCommGrpCat.of (DerivedCategory.Ext.{u, v, w}
          ((DerivedCategory.singleFunctor.{w, v, u} C 0).obj M)
          (DerivedCategory.Plus.ι.{w, v, u}.obj K) n)),
      (∀ i j : ℤ, (e₂ i j).hom =
        (pageIso 2 i j (i + j) zero_le_two rfl).hom ≫ (filteredE₂Iso i j).hom) ∧
      (∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
        ∃ δ : (Z r p n : AddCommGrpCat.{w}) ⟶ (Z r (p + r) (n + 1) : AddCommGrpCat.{w}),
          δ ≫ (Z r (p + r) (n + 1)).arrow = (Z r p n).arrow ≫ T.X.d n (n + 1) ∧
          cokernel.π (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
              (pageIso r p q n hr hn).inv ≫ (E.page r hr).d (p, q) (p + r, q - r + 1) =
            δ ≫ cokernel.π (Subobject.ofLE _ _ (inf_le_right :
                D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤ Z r (p + r) (n + 1))) ≫
              (pageIso r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) ∧
      (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0 le_rfl).X (p, n - p))}.Finite) ∧
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
      (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
        (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
      (∀ p n : ℤ,
        IsGLB (Set.range fun r : ℕ =>
            Fil p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
              Fil (p + 1) n)
          (kernelSubobject (T.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
        IsLUB (Set.range fun r : ℕ =>
            Fil p n ⊓ (Subobject.«exists» (T.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
              Fil (p + 1) n)
          (imageSubobject (T.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n)) ∧
      ∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧
        ∀ (r i j : ℤ) (hr : 0 ≤ r), i + j = n → (i < a ∨ b < i) →
          IsZero ((E.page r hr).X (i, j))
```

## Tag 0AVI, an equation

[Tag 0AVI](https://stacks.math.columbia.edu/tag/0AVI) in the Stacks Project.

**`StacksDraft.ExtSpectralSequence.exists_ext_complex_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Ext/SpectralSequence.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Ext/SpectralSequence.lean#L633).

> **Stacks 0AVI.** If a bounded below complex `K` represents an object of the bounded below
> derived category, there is a cohomological spectral sequence
> `E₁ⁱʲ = Extʲ(M, Kⁱ)` abutting to `Extⁱ⁺ʲ(M, K)`.

```lean
public theorem exists_ext_complex_spectralSequence
    (C : Type u) [Category.{v} C] [Abelian C] [EnoughInjectives C]
    [HasDerivedCategory.{w} C] (M : C) (K : CochainComplex C ℤ)
    (hK : ∃ a : ℤ, K.IsStrictlyGE a) :
    ∃ (E : CohomologicalSpectralSequence AddCommGrpCat.{w} 1)
      (_e₁ : ∀ i j : ℤ, (E.page 1).X (i, j) ≅
        AddCommGrpCat.of (Abelian.zExt.{u, v, w} M (K.X i) j))
      (G : ∀ _p n : ℤ, Subobject
        (AddCommGrpCat.of
          (DerivedCategory.Ext.{u, v, w}
            ((DerivedCategory.singleFunctor.{w, v, u} C 0).obj M)
            (DerivedCategory.Q.obj K) n)))
      (hG : ∀ p p' n : ℤ, p ≤ p' → G p' n ≤ G p n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ G a n = ⊤ ∧ G b n = ⊥) ∧
      ∀ p q : ℤ, ∃ r₀ : ℤ, 1 ≤ r₀ ∧ ∀ (r : ℤ) (hr : 1 ≤ r), r₀ ≤ r →
        (E.page r hr).d (p, q) (p + r, q + 1 - r) = 0 ∧
        (E.page r hr).d (p - r, q + r - 1) (p, q) = 0 ∧
        Nonempty ((E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE (G (p + 1) (p + q)) (G p (p + q))
            (hG p (p + 1) (p + q) (by omega))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.69, Tag 0AVG](https://stacks.math.columbia.edu/tag/0AVG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
