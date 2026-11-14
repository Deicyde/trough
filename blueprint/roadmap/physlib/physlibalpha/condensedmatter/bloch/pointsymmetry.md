---
declaration: module
origin: cited
lean: CondensedMatter.Bloch.fibreMatrix, CondensedMatter.Bloch.fibreMatrix_apply, CondensedMatter.Bloch.fibreMatrix_mul, CondensedMatter.Bloch.fibreMatrix_mul_conjTranspose, CondensedMatter.Bloch.fibreMatrix_conjTranspose_mul, CondensedMatter.Bloch.hoppingSymbol, CondensedMatter.Bloch.IsInvariant, CondensedMatter.Bloch.IsCovariant
statement: formalized
proof: formalized
---

# Symmetry of the Bloch matrices of a crystal

The module `PhyslibAlpha.CondensedMatter.Bloch.PointSymmetry`, [PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean): 31 declarations, 27 with a docstring; 1 private, not shown.

> The Bloch matrices of a symmetric crystal at momenta in one orbit of the point group are
> conjugate, and at a momentum fixed by a symmetry they commute with it.

## i. Overview

> Take a crystal with translation group `G` and the finite set `F` of sites in a cell, and a
> translation-invariant Hamiltonian on `ℓ²(G, ℂ^F)` given by hopping matrices `T r`. Its Bloch
> matrix at a momentum `χ` is `b(χ) = ∑_r χ(r) T r`. A symmetry `s = (A, σ, b)` moves the site `i`
> of the cell `n` to the site `σ i` of the cell `A n + b i`. On the Fourier transform
> `ψ̂(χ) = ∑_n χ(n) ψ(n)` it acts by
> `(U_s ψ)^(χ) = V_s(χ) ψ̂(χ ∘ A)`, where the fibre matrix `V_s(χ)` is the monomial matrix with the
> entry `χ(b i)` at `(σ i, i)`. The symmetry carries the fibre at `χ ∘ A` to the fibre at
> `s • χ = χ ∘ A⁻¹`. The fibre matrices satisfy the cocycle identity
> `V_{st}(χ) = V_s(χ) V_t(s⁻¹ • χ)`, and they are unitary. The phases `χ(b i)` come from the
> offsets `b i` of the sites: for a symmetry that is a pure rotation or reflection of a crystal
> with one site per cell they are absent, and a screw axis or glide plane is what makes them
> momentum dependent.
>
> The Hamiltonian commutes with `U_s` exactly when `V_s(s • χ) b(χ) = b(s • χ) V_s(s • χ)` for all
> `χ`, which is what *covariance* of the symbol means. It holds when the hopping is invariant
> under the symmetry, `T (A r + b i - b j) (σ i) (σ j) = T r i j`. Two consequences follow. Along
> an orbit of the point group, the Bloch matrices are unitarily equivalent, so their eigenvalues
> are the same: the bands are functions on the irreducible zone. At a momentum fixed by `s`, the
> Bloch matrix commutes with `V_s(χ)`, so its eigenspaces are representation spaces of the little
> group, and an eigenvalue of a Hermitian Bloch matrix has multiplicity at least the least
> dimension of an invariant subspace: the degeneracies forced by symmetry.

## ii. Key results

> - `fibreMatrix` : the monomial matrix of a symmetry at a momentum.
> - `fibreMatrix_mul` : the cocycle identity.
> - `fibreMatrix_unitary` : the fibre matrices are unitary.
> - `hoppingSymbol` : the Bloch matrix of a family of hopping matrices.
> - `IsCovariant`, `isCovariant_of_invariant` : invariant hopping has a covariant symbol.
> - `eigenvalues_eq_of_covariant` : the bands agree at momenta related by a symmetry.
> - `bandsOnZone` : the bands are functions on the irreducible zone.
> - `uniformHopping`, `isCovariant_uniformHopping` : uniform hopping on a periodic graph is covariant
>   under all its bond-preserving symmetries.
> - `iUnion_spectrum_eq_of_covers` : the spectrum is the union over an irreducible zone.
> - `two_le_finrank_of_no_common_eigenvector` : a criterion for twofold degeneracy.
> - `le_finrank_eigenspace`, `le_finrank_eigenspace_of_littleGroup` : the multiplicity of an
>   eigenvalue at a momentum fixed by the symmetries is at least the least dimension of an
>   invariant subspace.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The fibre matrices

**`CondensedMatter.Bloch.fibreMatrix`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L88).

> The fibre matrix of a symmetry `s = (A, σ, b)` at the momentum `χ`: the monomial matrix with
> the entry `χ(b i)` at `(σ i, i)`.

```lean
noncomputable def fibreMatrix (s : CellSymmetry G F) (χ : BrillouinZone G) :
    Matrix F F ℂ
```

**`CondensedMatter.Bloch.fibreMatrix_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L94).

```lean
lemma fibreMatrix_apply (s : CellSymmetry G F) (χ : BrillouinZone G) (j i : F) :
    fibreMatrix s χ j i = if j = s.perm i then (χ (Multiplicative.ofAdd (s.shift i)) : ℂ) else 0
```

**`CondensedMatter.Bloch.fibreMatrix_mul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L99).

> **The cocycle identity** for the fibre matrices: `V_{st}(χ) = V_s(χ) V_t(s⁻¹ • χ)`.

```lean
lemma fibreMatrix_mul (s t : CellSymmetry G F) (χ : BrillouinZone G) :
    fibreMatrix (s * t) χ = fibreMatrix s χ * fibreMatrix t (s⁻¹ • χ)
```

**`CondensedMatter.Bloch.fibreMatrix_mul_conjTranspose`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L119).

> The fibre matrices are unitary.

```lean
lemma fibreMatrix_mul_conjTranspose (s : CellSymmetry G F) (χ : BrillouinZone G) :
    fibreMatrix s χ * (fibreMatrix s χ)ᴴ = 1
```

**`CondensedMatter.Bloch.fibreMatrix_conjTranspose_mul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L137).

> The fibre matrices are unitary.

```lean
lemma fibreMatrix_conjTranspose_mul (s : CellSymmetry G F) (χ : BrillouinZone G) :
    (fibreMatrix s χ)ᴴ * fibreMatrix s χ = 1
```

## B. The symbol of a hopping family

**`CondensedMatter.Bloch.hoppingSymbol`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L144).

> The Bloch matrix `b(χ) = ∑_r χ(r) T r` of a finite family of hopping matrices.

```lean
noncomputable def hoppingSymbol (T : G →₀ Matrix F F ℂ) (χ : BrillouinZone G) : Matrix F F ℂ
```

**`CondensedMatter.Bloch.IsInvariant`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L150).

> A family of hopping matrices is invariant under a symmetry `(A, σ, b)` when
> `T (A r + b i - b j) (σ i) (σ j) = T r i j`: the amplitude to hop from `j` to `i` across `r`
> equals the amplitude between the transformed sites across the transformed displacement.

```lean
def IsInvariant (T : G →₀ Matrix F F ℂ) (s : CellSymmetry G F) : Prop
```

**`CondensedMatter.Bloch.IsCovariant`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L155).

> A symbol `b` on the Brillouin zone is covariant under a symmetry when the fibre matrix
> intertwines it: `V_s(s • χ) b(χ) = b(s • χ) V_s(s • χ)`.

```lean
def IsCovariant (b : BrillouinZone G → Matrix F F ℂ) (s : CellSymmetry G F) : Prop
```

**`CondensedMatter.Bloch.entry`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L160).

> The entries of a hopping family at a fixed pair of orbitals, as a finitely supported function
> of the displacement.

```lean
noncomputable def entry (T : G →₀ Matrix F F ℂ) (i j : F) : G →₀ ℂ
```

**`CondensedMatter.Bloch.hoppingSymbol_apply`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L166).

```lean
lemma hoppingSymbol_apply (T : G →₀ Matrix F F ℂ) (χ : BrillouinZone G) (i j : F) :
    hoppingSymbol T χ i j = (entry T i j).sum fun r m => (χ (Multiplicative.ofAdd r) : ℂ) * m
```

**`CondensedMatter.Bloch.smul_apply_linear`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L178).

```lean
lemma smul_apply_linear (s : CellSymmetry G F) (χ : BrillouinZone G) (r : G) :
    (s • χ) (Multiplicative.ofAdd (s.linear r)) = χ (Multiplicative.ofAdd r)
```

**`CondensedMatter.Bloch.isCovariant_of_invariant`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L183).

> **Invariant hopping has a covariant Bloch symbol.**

```lean
lemma isCovariant_of_invariant {T : G →₀ Matrix F F ℂ} {s : CellSymmetry G F}
    (hT : IsInvariant T s) : IsCovariant (hoppingSymbol T) s
```

## C. Bands on the irreducible zone

**`CondensedMatter.Bloch.conj_of_covariant`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L240).

> A covariant symbol is conjugated by the fibre matrix between a momentum and its image.

```lean
lemma conj_of_covariant {b : BrillouinZone G → Matrix F F ℂ} {s : CellSymmetry G F}
    (hb : IsCovariant b s) (χ : BrillouinZone G) :
    b (s • χ) = fibreMatrix s (s • χ) * b χ * (fibreMatrix s (s • χ))ᴴ
```

**`CondensedMatter.Bloch.charpoly_eq_of_covariant`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L246).

> The Bloch matrices at related momenta have the same characteristic polynomial.

```lean
lemma charpoly_eq_of_covariant {b : BrillouinZone G → Matrix F F ℂ} {s : CellSymmetry G F}
    (hb : IsCovariant b s) (χ : BrillouinZone G) :
    (b (s • χ)).charpoly = (b χ).charpoly
```

**`CondensedMatter.Bloch.eigenvalues_eq_of_covariant`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L254).

> **The bands agree at momenta related by a symmetry.** If the Bloch matrices are Hermitian,
> their eigenvalues at `χ` and `s • χ` coincide.

```lean
lemma eigenvalues_eq_of_covariant {b : BrillouinZone G → Matrix F F ℂ}
    (hH : ∀ χ, (b χ).IsHermitian) {s : CellSymmetry G F} (hb : IsCovariant b s)
    (χ : BrillouinZone G) : (hH (s • χ)).eigenvalues = (hH χ).eigenvalues
```

**`CondensedMatter.Bloch.bandsOnZone`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L263).

> **The bands are functions on the irreducible zone.** For a symbol that is covariant under all
> bond-preserving symmetries of a crystal, the eigenvalues of the Bloch matrices depend only on the
> orbit of the momentum under the point group.

```lean
noncomputable def bandsOnZone {g : PeriodicGraph (Crystal.ofUnitCell G F)}
    {b : BrillouinZone G → Matrix F F ℂ} (hH : ∀ χ, (b χ).IsHermitian)
    (hb : ∀ s : g.symmetries, IsCovariant b s) : g.IrreducibleZone → (F → ℝ)
```

## D. The little group at a momentum

**`CondensedMatter.Bloch.commute_of_smul_eq`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L274).

> At a momentum fixed by a symmetry, the Bloch matrix commutes with its fibre matrix.

```lean
lemma commute_of_smul_eq {b : BrillouinZone G → Matrix F F ℂ} {s : CellSymmetry G F}
    (hb : IsCovariant b s) {χ : BrillouinZone G} (hχ : s • χ = χ) :
    fibreMatrix s χ * b χ = b χ * fibreMatrix s χ
```

**`CondensedMatter.Bloch.le_finrank_eigenspace`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L283).

> **Symmetry-enforced degeneracy.** If `M` commutes with a set of matrices and every nonzero
> subspace invariant under them has dimension at least `m`, every eigenspace of `M` has dimension
> at least `m`.

```lean
lemma le_finrank_eigenspace (M : Matrix F F ℂ) (S : Set (Matrix F F ℂ))
    (hcomm : ∀ V ∈ S, V * M = M * V) {m : ℕ}
    (hS : ∀ W : Submodule ℂ (F → ℂ), W ≠ ⊥ → (∀ V ∈ S, ∀ w ∈ W, V.mulVec w ∈ W) →
      m ≤ Module.finrank ℂ W) (μ : ℂ) (hμ : ∃ v : F → ℂ, v ≠ 0 ∧ M.mulVec v = μ • v) :
    m ≤ Module.finrank ℂ (Module.End.eigenspace (Matrix.toLin' M) μ)
```

**`CondensedMatter.Bloch.le_finrank_eigenspace_of_littleGroup`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L301).

> **Degeneracy forced by the little group.** For a symbol covariant under the bond-preserving
> symmetries of a crystal, if every nonzero subspace of `ℂ^F` invariant under the fibre matrices of
> the little group at `χ` has dimension at least `m`, every eigenspace of the Bloch matrix at `χ` has
> dimension at least `m`.

```lean
lemma le_finrank_eigenspace_of_littleGroup {g : PeriodicGraph (Crystal.ofUnitCell G F)}
    {b : BrillouinZone G → Matrix F F ℂ} (hb : ∀ s : g.symmetries, IsCovariant b s)
    (χ : BrillouinZone G) {m : ℕ}
    (hS : ∀ W : Submodule ℂ (F → ℂ), W ≠ ⊥ →
      (∀ s ∈ g.littleGroup χ, ∀ w ∈ W, (fibreMatrix (s : CellSymmetry G F) χ).mulVec w ∈ W) →
      m ≤ Module.finrank ℂ W) (μ : ℂ) (hμ : ∃ v : F → ℂ, v ≠ 0 ∧ (b χ).mulVec v = μ • v) :
    m ≤ Module.finrank ℂ (Module.End.eigenspace (Matrix.toLin' (b χ)) μ)
```

## E. Hopping from a graph and its symmetries

**`CondensedMatter.Bloch.uniformHopping`**, a def, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L325).

> Hopping with the amplitude `t` between any two bonded sites of a periodic graph: the entry
> `(i, j)` of the matrix at the displacement `r` is `t` when the site `j` of a cell is bonded to the
> site `i` of the cell displaced by `r`.

```lean
noncomputable def uniformHopping (g : PeriodicGraph (Crystal.ofUnitCell G F)) (t : ℂ) :
    G →₀ Matrix F F ℂ
```

**`CondensedMatter.Bloch.uniformHopping_apply`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L345).

```lean
lemma uniformHopping_apply (g : PeriodicGraph (Crystal.ofUnitCell G F)) (t : ℂ) (r : G) (i j : F) :
    uniformHopping g t r i j = if g.Bonded j i r then t else 0
```

**`CondensedMatter.Bloch.isInvariant_uniformHopping`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L353).

> **Uniform hopping is invariant under every bond-preserving symmetry.**

```lean
lemma isInvariant_uniformHopping (g : PeriodicGraph (Crystal.ofUnitCell G F)) (t : ℂ)
    {s : CellSymmetry G F} (hs : s ∈ g.symmetries) : IsInvariant (uniformHopping g t) s
```

**`CondensedMatter.Bloch.isCovariant_uniformHopping`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L360).

> **Uniform hopping has a covariant Bloch symbol under every bond-preserving symmetry.**

```lean
lemma isCovariant_uniformHopping (g : PeriodicGraph (Crystal.ofUnitCell G F)) (t : ℂ)
    (s : g.symmetries) : IsCovariant (hoppingSymbol (uniformHopping g t)) s
```

**`CondensedMatter.Bloch.isHermitian_hoppingSymbol`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L370).

> If `(T r)ᴴ = T (-r)` for all `r`, the Bloch matrices are Hermitian.

```lean
lemma isHermitian_hoppingSymbol {T : G →₀ Matrix F F ℂ} (hT : ∀ r, (T r)ᴴ = T (-r))
    (χ : BrillouinZone G) : (hoppingSymbol T χ).IsHermitian
```

**`CondensedMatter.Bloch.bonded_symm`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L404).

> Bonds are symmetric: the bond from `i` to `j` across `d` is the bond from `j` to `i` across
> `-d`.

```lean
lemma bonded_symm (g : PeriodicGraph (Crystal.ofUnitCell G F)) (i j : F) (d : G) :
    g.Bonded i j d ↔ g.Bonded j i (-d)
```

**`CondensedMatter.Bloch.isHermitian_hoppingSymbol_uniform`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L416).

> Uniform real hopping gives Hermitian Bloch matrices at every momentum.

```lean
lemma isHermitian_hoppingSymbol_uniform (g : PeriodicGraph (Crystal.ofUnitCell G F)) (t : ℝ)
    (χ : BrillouinZone G) : (hoppingSymbol (uniformHopping g (t : ℂ)) χ).IsHermitian
```

## F. Restricting to a set of representatives

**`CondensedMatter.Bloch.CoversOrbits`**, a def, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L431).

> A set of momenta covers the orbits of the point group when every momentum is carried into it by
> some element of the point group. An irreducible zone is a set that covers the orbits.

```lean
def CoversOrbits (g : PeriodicGraph (Crystal.ofUnitCell G F)) (D : Set (BrillouinZone G)) : Prop
```

**`CondensedMatter.Bloch.spectrum_eq_range_eigenvalues`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L435).

> The spectrum of a Bloch matrix is the set of its eigenvalues.

```lean
lemma spectrum_eq_range_eigenvalues {M : Matrix F F ℂ} (hM : M.IsHermitian) :
    spectrum ℂ M = ((↑) : ℝ → ℂ) '' Set.range hM.eigenvalues
```

**`CondensedMatter.Bloch.spectrum_eq_of_covariant`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L440).

> **The spectra of the Bloch matrices at related momenta agree.**

```lean
lemma spectrum_eq_of_covariant {b : BrillouinZone G → Matrix F F ℂ}
    (hH : ∀ χ, (b χ).IsHermitian) {s : CellSymmetry G F} (hb : IsCovariant b s)
    (χ : BrillouinZone G) : spectrum ℂ (b (s • χ)) = spectrum ℂ (b χ)
```

**`CondensedMatter.Bloch.iUnion_spectrum_eq_of_covers`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L449).

> **The spectrum over the whole Brillouin zone is the spectrum over an irreducible zone.** If a
> symbol is covariant under the bond-preserving symmetries, it suffices to take the union of the
> spectra of its Bloch matrices over a set of momenta that covers the orbits of the point group.

```lean
lemma iUnion_spectrum_eq_of_covers {g : PeriodicGraph (Crystal.ofUnitCell G F)}
    {b : BrillouinZone G → Matrix F F ℂ} (hH : ∀ χ, (b χ).IsHermitian)
    (hb : ∀ s : g.symmetries, IsCovariant b s) {D : Set (BrillouinZone G)}
    (hD : CoversOrbits g D) :
    (⋃ χ : BrillouinZone G, spectrum ℂ (b χ)) = ⋃ χ ∈ D, spectrum ℂ (b χ)
```

**`CondensedMatter.Bloch.two_le_finrank_of_no_common_eigenvector`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean#L469).

> **A criterion for twofold degeneracy.** If the matrices in `S` have no common eigenvector, every
> nonzero invariant subspace has dimension at least `2`. Combined with
> `le_finrank_eigenspace_of_littleGroup`, this forces every eigenvalue of the Bloch matrix at a
> momentum whose little group has no common eigenvector in `ℂ^F` to be at least twofold degenerate.

```lean
lemma two_le_finrank_of_no_common_eigenvector (S : Set (Matrix F F ℂ))
    (h : ¬∃ v : F → ℂ, v ≠ 0 ∧ ∀ V ∈ S, ∃ c : ℂ, V.mulVec v = c • v)
    (W : Submodule ℂ (F → ℂ)) (hW : W ≠ ⊥) (hinv : ∀ V ∈ S, ∀ w ∈ W, V.mulVec w ∈ W) :
    2 ≤ Module.finrank ℂ W
```

## Depends on

- [Symmetries of a crystal acting on its Brillouin zone](../crystal/part-01/brillouin.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/PointSymmetry.lean)
