---
declaration: section
origin: cited
lean: HomologicalComplex₂.exists_iso_pages_totalFiltration₂, HomologicalComplex₂.isLeast_totalFiltration₁, HomologicalComplex₂.isLeast_totalFiltration₂, HomologicalComplex₂.exists_iso_pages_totalFiltration₁, HomologicalComplex₂.WeaklyConvergesToTotalHomology₁, HomologicalComplex₂.AbutsToTotalHomology₁, HomologicalComplex₂.ConvergesToTotalHomology₁, HomologicalComplex₂.WeaklyConvergesToTotalHomology₂
statement: formalized
proof: formalized
---

# 12.25 Spectral sequences: double complexes

Section 12.25 of the Stacks Project, [Tag 012X](https://stacks.math.columbia.edu/tag/012X). 5 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0130, a lemma

[Tag 0130](https://stacks.math.columbia.edu/tag/0130) in the Stacks Project.

**`HomologicalComplex₂.exists_iso_pages_totalFiltration₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean#L47). The attribute's comment: “(2), (4) and (6)”.

> **Stacks 0130, the second filtration.** Let `(''E_r, ''d_r)` be the spectral sequence of the
> total complex of a double complex `K^{•,•}` filtered by the second coordinate, presented as in
> [Stacks, Tag 012M] by its pages `Z_r^{p,q}/D_r^{p,q}` and its differentials induced by `d`. Then
> 2. `''E_0^{p,q} = K^{q,p}` with `''d_0^{p,q} = d_1^{q,p}`;
> 4. `''E_1^{p,q} = H^q(K^{•,p})` with `''d_1^{p,q} = (-1)^q H^q(d_2^{•,p})`; here `H^q(K^{•,p})`
>    is written as the `p`-th term of `H^q_I(K^{•,•})`, whose differential is induced by `d_2`;
> 6. `''E_2^{p,q} = H^p_{II}(H^q_I(K^{•,•}))`.
>
> That the filtration `F` this is stated for really is
> `F_{II}^p Tot^n = ⨁_{i + j = n, j ≥ p} K^{i,j}` is the companion statement
> `isLeast_totalFiltration₂`, which shares the parameters `F` and `hF` with this one; the two
> together are the content of [Stacks, Tag 0130] for the second filtration.

```lean
public theorem exists_iso_pages_totalFiltration₂
    (F : ∀ (_p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₂.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hZ : ∀ r p n : ℤ, Z r p n = F p n ⊓
      (Subobject.pullback ((K.total (ComplexShape.up ℤ)).d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» ((K.total (ComplexShape.up ℤ)).d (n - 1) n)).obj
        (Z (r - 1) (p - r + 1) (n - 1)))
    (E : CohomologicalSpectralSequence C 0)
    (e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
    (hδ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
      ∃ δ : (Z r p n : C) ⟶ (Z r (p + r) (n + 1) : C),
        δ ≫ (Z r (p + r) (n + 1)).arrow =
          (Z r p n).arrow ≫ (K.total (ComplexShape.up ℤ)).d n (n + 1) ∧
        cokernel.π (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
            (e r p q n hr hn).inv ≫ (E.page r hr).d (p, q) (p + r, q - r + 1) =
          δ ≫ cokernel.π (Subobject.ofLE _ _ (inf_le_right :
              D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤ Z r (p + r) (n + 1))) ≫
            (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) :
    (∃ α : ∀ p q : ℤ, (E.page 0 le_rfl).X (p, q) ≅ (K.X q).X p,
      ∀ p q : ℤ, (E.page 0 le_rfl).d (p, q) (p, q + 1) ≫ (α p (q + 1)).hom =
        (α p q).hom ≫ (K.d q (q + 1)).f p) ∧
    (∃ β : ∀ p q : ℤ, (E.page 1 zero_le_one).X (p, q) ≅ (K.homology q).X p,
      ∀ p q : ℤ, (E.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (β (p + 1) q).hom =
        (β p q).hom ≫ (q.negOnePow • (K.homology q).d p (p + 1))) ∧
    ∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅ (K.homology q).homology p)
```

**`HomologicalComplex₂.isLeast_totalFiltration₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Filtration.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Filtration.lean#L288). The attribute's comment: “the first filtration is ⨁_{i ≥ p} K^{i,j}”.

> **Stacks 0130, the first filtration is the one intended.** The degreewise steps `F p n` of the
> filtration of `Tot(K^{•,•})` by the first coordinate are `F_I^p Tot^n = ⨁_{i + j = n, i ≥ p}
> K^{i,j}`, characterized without arbitrary suprema of subobjects: `F p n` contains the image of
> every summand inclusion `K^{i,j} ⟶ Tot^n` with `i ≥ p`, and it is the least subobject of `Tot^n`
> that does. Consequently the filtration is decreasing in `p`. Together with
> `exists_iso_pages_totalFiltration₁`, which is stated for the same `F` under the same hypothesis
> `hF`, this is the content of [Stacks, Tag 0130] for the first filtration: the identifications of
> the pages there are identifications for *this* filtration.

```lean
public theorem isLeast_totalFiltration₁
    (F : ∀ (_p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₁.filtration.ι.app (op p)).f n)) :
    (∀ (p i j n : ℤ) (hij : i + j = n), p ≤ i →
      imageSubobject (K.ιTotal (ComplexShape.up ℤ) i j n hij) ≤ F p n) ∧
    (∀ (p n : ℤ) (W : Subobject ((K.total (ComplexShape.up ℤ)).X n)),
      (∀ (i j : ℤ) (hij : i + j = n), p ≤ i →
        imageSubobject (K.ιTotal (ComplexShape.up ℤ) i j n hij) ≤ W) → F p n ≤ W) ∧
    (∀ p p' n : ℤ, p ≤ p' → F p' n ≤ F p n)
```

**`HomologicalComplex₂.isLeast_totalFiltration₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Filtration.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Filtration.lean#L308). The attribute's comment: “the second filtration is ⨁_{j ≥ p} K^{i,j}”.

> **Stacks 0130, the second filtration is the one intended.** The degreewise steps `F p n` of the
> filtration of `Tot(K^{•,•})` by the second coordinate are `F_{II}^p Tot^n =
> ⨁_{i + j = n, j ≥ p} K^{i,j}`, characterized without arbitrary suprema of subobjects: `F p n`
> contains the image of every summand inclusion `K^{i,j} ⟶ Tot^n` with `j ≥ p`, and it is the least
> subobject of `Tot^n` that does. Consequently the filtration is decreasing in `p`. Together with
> `exists_iso_pages_totalFiltration₂`, which is stated for the same `F` under the same hypothesis
> `hF`, this is the content of [Stacks, Tag 0130] for the second filtration: the identifications of
> the pages there are identifications for *this* filtration.

```lean
public theorem isLeast_totalFiltration₂
    (F : ∀ (_p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₂.filtration.ι.app (op p)).f n)) :
    (∀ (p i j n : ℤ) (hij : i + j = n), p ≤ j →
      imageSubobject (K.ιTotal (ComplexShape.up ℤ) i j n hij) ≤ F p n) ∧
    (∀ (p n : ℤ) (W : Subobject ((K.total (ComplexShape.up ℤ)).X n)),
      (∀ (i j : ℤ) (hij : i + j = n), p ≤ j →
        imageSubobject (K.ιTotal (ComplexShape.up ℤ) i j n hij) ≤ W) → F p n ≤ W) ∧
    (∀ p p' n : ℤ, p ≤ p' → F p' n ≤ F p n)
```

**`HomologicalComplex₂.exists_iso_pages_totalFiltration₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Pages.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Pages.lean#L497). The attribute's comment: “(1), (3) and (5)”.

> **Stacks 0130, the first filtration.** Let `('E_r, 'd_r)` be the spectral sequence of the total
> complex of a double complex `K^{•,•}` filtered by the first coordinate, presented as in
> [Stacks, Tag 012M] by its pages `Z_r^{p,q}/D_r^{p,q}` and its differentials induced by `d`. Then
> 1. `'E_0^{p,q} = K^{p,q}` with `'d_0^{p,q} = (-1)^p d_2^{p,q}`;
> 3. `'E_1^{p,q} = H^q(K^{p,•})` with `'d_1^{p,q} = H^q(d_1^{p,•})`;
> 5. `'E_2^{p,q} = H^p_I(H^q_{II}(K^{•,•}))`, the cohomology in degree `p` of the complex
>    `p ↦ H^q(K^{p,•})`.
>
> That the filtration `F` this is stated for really is `F_I^p Tot^n = ⨁_{i + j = n, i ≥ p} K^{i,j}`
> is the companion statement `isLeast_totalFiltration₁`, which shares the parameters `F` and `hF`
> with this one; the two together are the content of [Stacks, Tag 0130] for the first filtration.

```lean
public theorem exists_iso_pages_totalFiltration₁
    (F : ∀ (_p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₁.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hZ : ∀ r p n : ℤ, Z r p n = F p n ⊓
      (Subobject.pullback ((K.total (ComplexShape.up ℤ)).d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject ((K.total (ComplexShape.up ℤ)).X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» ((K.total (ComplexShape.up ℤ)).d (n - 1) n)).obj
        (Z (r - 1) (p - r + 1) (n - 1)))
    (E : CohomologicalSpectralSequence C 0)
    (e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
    (hδ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
      ∃ δ : (Z r p n : C) ⟶ (Z r (p + r) (n + 1) : C),
        δ ≫ (Z r (p + r) (n + 1)).arrow =
          (Z r p n).arrow ≫ (K.total (ComplexShape.up ℤ)).d n (n + 1) ∧
        cokernel.π (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
            (e r p q n hr hn).inv ≫ (E.page r hr).d (p, q) (p + r, q - r + 1) =
          δ ≫ cokernel.π (Subobject.ofLE _ _ (inf_le_right :
              D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤ Z r (p + r) (n + 1))) ≫
            (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) :
    (∃ α : ∀ p q : ℤ, (E.page 0 le_rfl).X (p, q) ≅ (K.X p).X q,
      ∀ p q : ℤ, (E.page 0 le_rfl).d (p, q) (p, q + 1) ≫ (α p (q + 1)).hom =
        (α p q).hom ≫ (p.negOnePow • (K.X p).d q (q + 1))) ∧
    (∃ β : ∀ p q : ℤ, (E.page 1 zero_le_one).X (p, q) ≅ (K.X p).homology q,
      ∀ p q : ℤ, (E.page 1 zero_le_one).d (p, q) (p + 1, q) ≫ (β (p + 1) q).hom =
        (β p q).hom ≫ HomologicalComplex.homologyMap (K.d p (p + 1)) q) ∧
    ∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
      (((HomologicalComplex.homologyFunctor C (ComplexShape.up ℤ) q).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj K).homology p)
```

## Tag 0131, a definition

[Tag 0131](https://stacks.math.columbia.edu/tag/0131) in the Stacks Project.

**`HomologicalComplex₂.WeaklyConvergesToTotalHomology₁`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L345). The attribute's comment: “`('E_r, 'd_r)` weakly converges”.

> **Stacks 0131, the first spectral sequence, weak convergence.** The spectral sequence
> `('E_r, 'd_r)` of `Tot(K^{•,•})` filtered by the first coordinate weakly converges to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev WeaklyConvergesToTotalHomology₁ : Prop
```

**`HomologicalComplex₂.AbutsToTotalHomology₁`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L352). The attribute's comment: “`('E_r, 'd_r)` abuts”.

> **Stacks 0131, the first spectral sequence, abutment.** The spectral sequence
> `('E_r, 'd_r)` of `Tot(K^{•,•})` filtered by the first coordinate abuts to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev AbutsToTotalHomology₁ : Prop
```

**`HomologicalComplex₂.ConvergesToTotalHomology₁`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L359). The attribute's comment: “`('E_r, 'd_r)` converges”.

> **Stacks 0131, the first spectral sequence, convergence.** The spectral sequence
> `('E_r, 'd_r)` of `Tot(K^{•,•})` filtered by the first coordinate converges to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev ConvergesToTotalHomology₁ : Prop
```

**`HomologicalComplex₂.WeaklyConvergesToTotalHomology₂`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L366). The attribute's comment: “`(''E_r, ''d_r)` weakly converges”.

> **Stacks 0131, the second spectral sequence, weak convergence.** The spectral sequence
> `(''E_r, ''d_r)` of `Tot(K^{•,•})` filtered by the second coordinate weakly converges to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev WeaklyConvergesToTotalHomology₂ : Prop
```

**`HomologicalComplex₂.AbutsToTotalHomology₂`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L373). The attribute's comment: “`(''E_r, ''d_r)` abuts”.

> **Stacks 0131, the second spectral sequence, abutment.** The spectral sequence
> `(''E_r, ''d_r)` of `Tot(K^{•,•})` filtered by the second coordinate abuts to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev AbutsToTotalHomology₂ : Prop
```

**`HomologicalComplex₂.ConvergesToTotalHomology₂`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L380). The attribute's comment: “`(''E_r, ''d_r)` converges”.

> **Stacks 0131, the second spectral sequence, convergence.** The spectral sequence
> `(''E_r, ''d_r)` of `Tot(K^{•,•})` filtered by the second coordinate converges to
> `H^n(Tot(K^{•,•}))`.

```lean
abbrev ConvergesToTotalHomology₂ : Prop
```

## Tag 0132, a lemma

[Tag 0132](https://stacks.math.columbia.edu/tag/0132) in the Stacks Project.

**`CategoryTheory.SpectralSequence.AbutsTo.prop_of_prop_page_firstQuadrant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/AbutsToWeakSerreFirstQuadrant.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/AbutsToWeakSerreFirstQuadrant.lean#L66). The attribute's comment: “part (4), for a first-quadrant `CohomologicalSpectralSequence` presented by `SpectralSequence.AbutsTo`, with the page hypothesis split into vanishing outside the first quadrant and membership at the nonnegative bidegrees”.

> **Stacks 0132 part (4) for a first quadrant spectral sequence.**  Let `E` be a cohomological
> spectral sequence of an abelian category which abuts to a graded object `H`, let `P` be a weak
> Serre subcategory, and let `r` be a page of `E`.  If the terms of `E_r` vanish outside the first
> quadrant and those at the nonnegative bidegrees lie in `P`, then every `H n` lies in `P`.
>
> This is `CategoryTheory.SpectralSequence.AbutsTo.prop_of_prop_page` with its hypothesis on the
> page split into the two clauses a first quadrant spectral sequence provides: `P` contains the
> zero object and is closed under isomorphisms, so the vanishing clause gives `P` at the bidegrees
> the other clause does not reach.

```lean
theorem AbutsTo.prop_of_prop_page_firstQuadrant {r₀ : ℤ}
    {E : CohomologicalSpectralSequence C r₀} {H : ℤ → C} (hE : AbutsTo E H)
    (P : ObjectProperty C) [P.IsWeakSerreClass] {r : ℤ} (hr : r₀ ≤ r)
    (hzero : ∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page r hr).X (p, q)))
    (hP : ∀ p q : ℕ, P ((E.page r hr).X ((p : ℤ), (q : ℤ)))) (n : ℤ) : P (H n)
```

**`HomologicalComplex₂.isBounded_and_converges_totalFiltration₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean#L205).

> **Stacks 0132, the first filtration.** If every diagonal of the double complex `K^{•,•}` has
> only finitely many nonzero terms, then the spectral sequence `E` of `Tot(K^{•,•})` filtered by the
> first coordinate, presented as in `CochainComplex.isBounded_and_converges_of_isDegreewiseFinite`, is
> bounded, the filtration it induces on each `H^n(Tot(K^{•,•}))` is finite, `E` converges to
> `H^*(Tot(K^{•,•}))`, and a weak Serre subcategory containing one whole page of `E` contains every
> `H^n(Tot(K^{•,•}))`.

```lean
public theorem isBounded_and_converges_totalFiltration₁
    (hK : ∀ n : ℤ, {pq : ℤ × ℤ | pq.1 + pq.2 = n ∧ ¬ IsZero ((K.X pq.1).X pq.2)}.Finite)
    (F : ∀ (_p n : ℤ), Subobject (K.totalFiltration₁.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₁.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.totalFiltration₁.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.totalFiltration₁.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.totalFiltration₁.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.totalFiltration₁.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
    (FH : ∀ (n _p : ℤ), Subobject (K.totalFiltration₁.X.homology n))
    (hFH : ∀ n p : ℤ, FH n p =
      imageSubobject
        (HomologicalComplex.homologyMap (K.totalFiltration₁.filtration.ι.app (op p)) n))
    (E : CohomologicalSpectralSequence C 0)
    (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))) :
    (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0 le_rfl).X (p, n - p))}.Finite) ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
    (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
      (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
    (∀ p n : ℤ,
      IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (K.totalFiltration₁.X.d n (n + 1))).obj (F (p + r) (n + 1))
            ⊔ F (p + 1) n)
        (kernelSubobject (K.totalFiltration₁.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
      IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (K.totalFiltration₁.X.d (n - 1) n)).obj (F (p - r) (n - 1))
            ⊔ F (p + 1) n)
        (imageSubobject (K.totalFiltration₁.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
    (∀ (P : ObjectProperty C) [P.IsWeakSerreClass] (r : ℤ) (hr : 0 ≤ r),
      (∀ p q : ℤ, P ((E.page r hr).X (p, q))) → ∀ n : ℤ, P (K.totalFiltration₁.X.homology n))
```

**`HomologicalComplex₂.isBounded_and_converges_totalFiltration₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/DoubleComplex/Convergence.lean#L247).

> **Stacks 0132, the second filtration.** If every diagonal of the double complex `K^{•,•}` has
> only finitely many nonzero terms, then the spectral sequence `E` of `Tot(K^{•,•})` filtered by the
> second coordinate, presented as in `CochainComplex.isBounded_and_converges_of_isDegreewiseFinite`,
> is bounded, the filtration it induces on each `H^n(Tot(K^{•,•}))` is finite, `E` converges to
> `H^*(Tot(K^{•,•}))`, and a weak Serre subcategory containing one whole page of `E` contains every
> `H^n(Tot(K^{•,•}))`.

```lean
public theorem isBounded_and_converges_totalFiltration₂
    (hK : ∀ n : ℤ, {pq : ℤ × ℤ | pq.1 + pq.2 = n ∧ ¬ IsZero ((K.X pq.1).X pq.2)}.Finite)
    (F : ∀ (_p n : ℤ), Subobject (K.totalFiltration₂.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.totalFiltration₂.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.totalFiltration₂.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.totalFiltration₂.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.totalFiltration₂.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.totalFiltration₂.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
    (FH : ∀ (n _p : ℤ), Subobject (K.totalFiltration₂.X.homology n))
    (hFH : ∀ n p : ℤ, FH n p =
      imageSubobject
        (HomologicalComplex.homologyMap (K.totalFiltration₂.filtration.ι.app (op p)) n))
    (E : CohomologicalSpectralSequence C 0)
    (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))) :
    (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0 le_rfl).X (p, n - p))}.Finite) ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
    (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
      (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
    (∀ p n : ℤ,
      IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (K.totalFiltration₂.X.d n (n + 1))).obj (F (p + r) (n + 1))
            ⊔ F (p + 1) n)
        (kernelSubobject (K.totalFiltration₂.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
      IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (K.totalFiltration₂.X.d (n - 1) n)).obj (F (p - r) (n - 1))
            ⊔ F (p + 1) n)
        (imageSubobject (K.totalFiltration₂.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
    (∀ (P : ObjectProperty C) [P.IsWeakSerreClass] (r : ℤ) (hr : 0 ≤ r),
      (∀ p q : ℤ, P ((E.page r hr).X (p, q))) → ∀ n : ℤ, P (K.totalFiltration₂.X.homology n))
```

## Tag 0133, a lemma

[Tag 0133](https://stacks.math.columbia.edu/tag/0133) in the Stacks Project.

**`quasiIso_total_of_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean, line 1431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean#L1431). The attribute's comment: “p”.

> Under the hypotheses, the total complex of `DA` exists and the induced
> map `K^• → Tot(A^{•,•})` is a quasi-isomorphism (variant in the first
> variable `p`).

```lean
theorem quasiIso_total_of_resolution
    (K : HomologicalComplex A (ComplexShape.up ℤ))
    (DA : HomologicalComplex₂ A (ComplexShape.up ℤ) (ComplexShape.up ℤ))
    (α : K ⟶ rowZero DA)
    (h : Hypotheses K DA α) :
    ∃ _ : DA.HasTotal (ComplexShape.up ℤ),
      ∃ (f : K ⟶ DA.total (ComplexShape.up ℤ)),
        (∀ n : ℤ, f.f n =
          α.f n ≫ DA.ιTotal (ComplexShape.up ℤ) n 0 n (by simp)) ∧
          QuasiIso f
```

**`quasiIso_total_of_resolution_flip`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean, line 1446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean#L1446). The attribute's comment: “q”.

> Under the hypotheses for `DA.flip`, the total complex of `DA` exists and the induced
> map `K^• → Tot(A^{•,•})` is a quasi-isomorphism (variant in the second variable `q`).

```lean
theorem quasiIso_total_of_resolution_flip
    (K : HomologicalComplex A (ComplexShape.up ℤ))
    (DA : HomologicalComplex₂ A (ComplexShape.up ℤ) (ComplexShape.up ℤ))
    (α : K ⟶ rowZero DA.flip)
    (h : Hypotheses K DA.flip α) :
    ∃ _ : DA.HasTotal (ComplexShape.up ℤ),
      ∃ (f : K ⟶ DA.total (ComplexShape.up ℤ)),
        (∀ n : ℤ, f.f n =
          α.f n ≫ DA.ιTotal (ComplexShape.up ℤ) 0 n n (by simp)) ∧
          QuasiIso f
```

## Tag 0FKH, a lemma

[Tag 0FKH](https://stacks.math.columbia.edu/tag/0FKH) in the Stacks Project.

**`isHomotopyEquiv_total_of_isHomotopyEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean, line 1737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/TotalComplexQuasiIso.lean#L1737).

> Let `M^•` be a complex of an abelian category and `A^{•,•}` a complex of
> complexes. If `a : M^•[0] ⟶ A^{•,•}` is part of a homotopy equivalence in the
> category of complexes of complexes, then the canonical induced map
> `α : M^• ⟶ Tot(A^{•,•})` is a homotopy equivalence.

```lean
theorem isHomotopyEquiv_total_of_isHomotopyEquiv
    {V : Type*} [Category V] [Abelian V]
    (M : HomologicalComplex V (ComplexShape.up ℤ))
    (A : HomologicalComplex₂ V (ComplexShape.up ℤ) (ComplexShape.up ℤ))
    [A.HasTotal (ComplexShape.up ℤ)]
    (a : HomotopyEquiv (singleObjComplex M) A) :
    Nonempty {e : HomotopyEquiv M (A.total (ComplexShape.up ℤ)) //
        e.hom = totalAlpha M A a.hom}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.25, Tag 012X](https://stacks.math.columbia.edu/tag/012X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
