---
declaration: section
origin: cited
lean: FilteredDifferentialObject, FilteredDifferentialObject.exists_page_iso, FilteredDifferentialObject.spectralSequence, FilteredDifferentialObject.π_spectralSequence_d, FilteredDifferentialObject.homologyπ_spectralSequence_iso_hom, FilteredDifferentialObject.pageZeroIso, FilteredDifferentialObject.spectralSequence_d_zero, FilteredDifferentialObject.pageOneIso
statement: formalized
proof: formalized
---

# 12.23 Spectral sequences: filtered differential objects

Section 12.23 of the Stacks Project, [Tag 012A](https://stacks.math.columbia.edu/tag/012A). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 012B, a definition

[Tag 012B](https://stacks.math.columbia.edu/tag/012B) in the Stacks Project.

**`FilteredDifferentialObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean#L70). The attribute's comment: “the filtered object `(K, F)` is `toFilteredObjectForDifferential` (Definition 0121: a `ℤ`-indexed decreasing filtration by subobjects); `d` is an endomorphism of filtered objects (`d_respects`) with `d ≫ d = 0` (`d_squared`)”.

> A *filtered differential object* `(K, F, d)` of an abelian category `A` is a filtered object
> `(K, F)` of `A` endowed with an endomorphism `d : (K, F) → (K, F)` whose square is zero:
> `d ∘ d = 0`.

```lean
structure FilteredDifferentialObject extends FilteredObjectForDifferential C
```

## Tag 012C, a lemma

[Tag 012C](https://stacks.math.columbia.edu/tag/012C) in the Stacks Project.

**`FilteredDifferentialObject.exists_page_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L208).

> The object `E_r^p` of the `r`-th page is `Z_r^p / B_r^p`, where, inside `gr^p K`,
> `Z_r^p = (F^p K ∩ d⁻¹(F^{p + r} K) + F^{p + 1} K) / F^{p + 1} K` and
> `B_r^p = (F^p K ∩ d(F^{p - r + 1} K) + F^{p + 1} K) / F^{p + 1} K`; the isomorphism is the identity
> on the classes of elements of `F^p K ∩ d⁻¹(F^{p + r} K)`.

```lean
theorem exists_page_iso (r p : ℤ) :
    ∃ e : X.page r p ≅ cokernel (Subobject.ofLE
      (X.F p ⊓ imageSubobject ((X.F (p - r + 1)).arrow ≫ X.d) ⊔ X.F (p + 1))
      (X.pageCycles r p ⊔ X.F (p + 1))
      (sup_le_sup_right (X.inf_imageSubobject_le_pageCycles r p) _)),
      cokernel.π _ ≫ e.hom = Subobject.ofLE _ _
        (le_sup_left : X.pageCycles r p ≤ X.pageCycles r p ⊔ X.F (p + 1)) ≫ cokernel.π _
```

**`FilteredDifferentialObject.spectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L465).

> The spectral sequence `(E_r, d_r)_{r ≥ 0}` associated to a filtered differential object
> `(K, F, d)`: its `r`-th page is the graded object `E_r^p = Z_r^p / (D_r^p ∩ Z_r^p)` with the
> differential `d_r^p : E_r^p ⟶ E_r^{p + r}` induced by `d`, and the cohomology of `(E_r, d_r)` is
> identified with `E_{r + 1}` by the page-turn isomorphism.

```lean
noncomputable def spectralSequence : SpectralSequence A (fun r => ComplexShape.up' r) 0
```

**`FilteredDifferentialObject.π_spectralSequence_d`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L476).

> The differential `d_r^p : E_r^p ⟶ E_r^{p + r}` of the spectral sequence is induced by
> `d : Z_r^p ⟶ Z_r^{p + r}`.

```lean
lemma π_spectralSequence_d (r : ℤ) (hr : 0 ≤ r) (p p' : ℤ) (h : p + r = p') :
    cokernel.π _ ≫ (X.spectralSequence.page r hr).d p p' = X.pageδ r p p' h ≫ cokernel.π _
```

**`FilteredDifferentialObject.homologyπ_spectralSequence_iso_hom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L483).

> The page-turn isomorphism of the spectral sequence sends the class of an `r`-cycle represented
> by `x ∈ Z_{r + 1}^p` to the class of `x` in `E_{r + 1}^p`.

```lean
lemma homologyπ_spectralSequence_iso_hom (r : ℤ) (hr : 0 ≤ r) (p : ℤ) {T : A}
    (y : T ⟶ (X.spectralSequence.page r hr).cycles p) (x : T ⟶ (X.pageCycles (r + 1) p : A))
    (x' : T ⟶ (X.pageCycles r p : A))
    (hx : x' ≫ (X.pageCycles r p).arrow = x ≫ (X.pageCycles (r + 1) p).arrow)
    (hy : y ≫ (X.spectralSequence.page r hr).iCycles p = x' ≫ cokernel.π _) :
    y ≫ (X.spectralSequence.page r hr).homologyπ p ≫ (X.spectralSequence.iso r (r + 1) p).hom =
      x ≫ cokernel.π _
```

**`FilteredDifferentialObject.pageZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L535).

> `E_0^p = gr^p K`.

```lean
noncomputable def pageZeroIso (p : ℤ) : X.page 0 p ≅ (X.gr p).X
```

**`FilteredDifferentialObject.spectralSequence_d_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L554).

> Under `E_0^p = gr^p K`, the differential `d_0^p` is `gr^p(d)`.

```lean
lemma spectralSequence_d_zero (p : ℤ) :
    (X.spectralSequence.page 0).d p p ≫ (X.pageZeroIso p).hom =
      (X.pageZeroIso p).hom ≫ (X.gr p).d
```

**`FilteredDifferentialObject.pageOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L603).

> `E_1^p = H(gr^p K, gr^p(d))`.

```lean
noncomputable def pageOneIso (p : ℤ) : X.page 1 p ≅ (X.gr p).homology
```

## Tag 012D, a lemma

[Tag 012D](https://stacks.math.columbia.edu/tag/012D) in the Stacks Project.

**`FilteredDifferentialObject.spectralSequence_d_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 747](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L747).

> Under the identifications `E_1^p = H(gr^p K)` and `E_1^{p + 1} = H(gr^{p + 1} K)`, the
> differential `d_1^p` of the spectral sequence is the boundary map in homology of the short exact
> sequence `0 → gr^{p + 1} K → F^p K / F^{p + 2} K → gr^p K → 0`.

```lean
theorem spectralSequence_d_one (p : ℤ) :
    (X.spectralSequence.page 1).d p (p + 1) ≫ (X.pageOneIso (p + 1)).hom =
      (X.pageOneIso p).hom ≫ (X.grShortExactSequence p).δ
```

## Tag 012E, a definition

[Tag 012E](https://stacks.math.columbia.edu/tag/012E) in the Stacks Project.

**`FilteredDifferentialObject.inducedFiltration`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean#L159).

> The `p`-th step of the induced filtration on `H(K, d)` is
> `F^p H(K, d) := Im (H(F^p K, d) ⟶ H(K, d))`.

```lean
noncomputable def inducedFiltration (p : ℤ) : Subobject X.homology
```

## Tag 012F, a lemma

[Tag 012F](https://stacks.math.columbia.edu/tag/012F) in the Stacks Project.

**`CategoryTheory.gr_homology_isSubquotient_stablePage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObject.lean#L394).

> Let `(K, F, d)` be a filtered differential object of an abelian category, let
> `p : ℤ`, and suppose the stable cycles `Z_∞^p` and boundaries `B_∞^p` in degree `p` exist, i.e.
> that `Zinf` is the greatest lower bound of the numerators of the `Z_r^p` and `Binf` the least upper
> bound of the numerators of the `B_r^p`. Then the numerators `D = Im(d) ⊓ F^p K ⊔ F^{p+1} K` and
> `N = Ker(d) ⊓ F^p K ⊔ F^{p+1} K` satisfy `Binf ≤ D ≤ N ≤ Zinf`, and `N / D` is `gr^p H(K, d)`,
> the graded piece of the cohomology for the induced filtration, by the isomorphism compatible with
> the two quotient maps out of `Ker(d) ⊓ F^p K`. In particular the limit term `E_∞^p = Zinf / Binf`
> is defined and has `gr^p H(K, d)` as a subquotient.

```lean
public theorem gr_homology_isSubquotient_stablePage {C : Type u} [Category.{v} C] [Abelian C]
    {K : C} {d : K ⟶ K} (hd : d ≫ d = 0) {F : ℤ → Subobject K} {p : ℤ} (hFp : F (p + 1) ≤ F p)
    {Zinf Binf : Subobject K}
    (hZinf : IsGLB (Set.range fun r : ℕ =>
      F p ⊓ (Subobject.pullback d).obj (F (p + (r : ℤ))) ⊔ F (p + 1)) Zinf)
    (hBinf : IsLUB (Set.range fun r : ℕ =>
      F p ⊓ imageSubobject ((F (p - (r : ℤ))).arrow ≫ d) ⊔ F (p + 1)) Binf)
    {D N : Subobject K} (hD : D = imageSubobject d ⊓ F p ⊔ F (p + 1))
    (hN : N = kernelSubobject d ⊓ F p ⊔ F (p + 1))
    (j : (D : C) ⟶ (N : C)) (hj : j ≫ N.arrow = D.arrow)
    {V W : Subobject (ShortComplex.mk d d hd).cycles}
    (hV : V = (Subobject.pullback (ShortComplex.mk d d hd).iCycles).obj (F p))
    (hW : W = (Subobject.pullback (ShortComplex.mk d d hd).iCycles).obj (F (p + 1)))
    {FH FH' : Subobject (ShortComplex.mk d d hd).homology}
    (hFH : FH = imageSubobject (V.arrow ≫ (ShortComplex.mk d d hd).homologyπ))
    (hFH' : FH' = imageSubobject (W.arrow ≫ (ShortComplex.mk d d hd).homologyπ))
    (ι : (FH' : C) ⟶ (FH : C)) (hι : ι ≫ FH.arrow = FH'.arrow)
    (a : (V : C) ⟶ (N : C)) (ha : a ≫ N.arrow = V.arrow ≫ (ShortComplex.mk d d hd).iCycles)
    (b : (V : C) ⟶ (FH : C))
    (hb : b ≫ FH.arrow = V.arrow ≫ (ShortComplex.mk d d hd).homologyπ) :
    Binf ≤ D ∧ D ≤ N ∧ N ≤ Zinf ∧
      ∃ e : cokernel j ≅ cokernel ι, a ≫ cokernel.π j ≫ e.hom = b ≫ cokernel.π ι
```

## Tag 012I, a definition

[Tag 012I](https://stacks.math.columbia.edu/tag/012I) in the Stacks Project.

**`FilteredDifferentialObject.WeaklyConverges`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 852](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L852). The attribute's comment: “weakly\_converges”.

> The spectral sequence of `(K, F, d)` *weakly converges* to `H(K)` (Stacks 012I): for every `p`
> the limit term `E_∞^p = Z_∞^p / B_∞^p` exists, i.e. the numerators of the cycles have an
> intersection `Z_∞^p` and those of the boundaries a union `B_∞^p`, and `gr^p H(K) = E_∞^p` via the
> comparison of Stacks 012F: there is an isomorphism `Z_∞^p / B_∞^p ≅ gr^p H(K)` compatible with the
> canonical maps to both from `Ker(d) ∩ F^p K`.

```lean
def WeaklyConverges : Prop
```

**`FilteredDifferentialObject.Abuts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 868](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L868). The attribute's comment: “abuts”.

> The spectral sequence of `(K, F, d)` *abuts* to `H(K)` (Stacks 012I): it weakly converges and
> the induced filtration on `H(K)` is separated, `⋂_p F^p H(K) = 0`, and exhaustive,
> `⋃_p F^p H(K) = H(K)`.

```lean
def Abuts : Prop
```

## Tag 012J, a lemma

[Tag 012J](https://stacks.math.columbia.edu/tag/012J) in the Stacks Project.

**`FilteredDifferentialObject.weaklyConverges_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 960](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L960). The attribute's comment: “(1)”.

> The spectral sequence of a filtered differential object weakly converges to `H(K)` if and only
> if equality holds in (012G) and (012H) for every `p`: the intersection of the numerators of the
> cycles is `(Ker(d) ∩ F^p K) + F^{p + 1} K` and the union of the numerators of the boundaries is
> `(Im(d) ∩ F^p K) + F^{p + 1} K`.

```lean
theorem weaklyConverges_iff : X.WeaklyConverges ↔ ∀ p : ℤ,
    IsGLB (Set.range (X.cyclesNumerator p)) (X.stableCyclesBound p) ∧
    IsLUB (Set.range (X.boundariesNumerator p)) (X.stableBoundariesBound p)
```

**`FilteredDifferentialObject.abuts_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean, line 1096](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredDifferentialObjectSpectralSequence.lean#L1096). The attribute's comment: “(2)”.

> The spectral sequence of a filtered differential object abuts to `H(K)` if and only if it
> weakly converges to `H(K)`, `⋂_p ((Ker(d) ∩ F^p K) + Im(d)) = Im(d)` and
> `⋃_p ((Ker(d) ∩ F^p K) + Im(d)) = Ker(d)`.

```lean
theorem abuts_iff : X.Abuts ↔ X.WeaklyConverges ∧
    IsGLB (Set.range fun p => kernelSubobject X.d ⊓ X.F p ⊔ imageSubobject X.d)
      (imageSubobject X.d) ∧
    IsLUB (Set.range fun p => kernelSubobject X.d ⊓ X.F p ⊔ imageSubobject X.d)
      (kernelSubobject X.d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.23, Tag 012A](https://stacks.math.columbia.edu/tag/012A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
