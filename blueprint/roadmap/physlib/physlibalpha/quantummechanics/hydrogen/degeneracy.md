---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.polyLaplacian, PhyslibAlpha.Hydrogen.harmonicSubmodule, PhyslibAlpha.Hydrogen.finrank_homogeneousSubmodule, PhyslibAlpha.Hydrogen.polyLaplacian_apply, PhyslibAlpha.Hydrogen.polyLaplacian_isHomogeneous, PhyslibAlpha.Hydrogen.pderiv_eq_zero_of_isHomogeneous_zero, PhyslibAlpha.Hydrogen.polyLaplacian_eq_zero_of_lt_two, PhyslibAlpha.Hydrogen.fischerWeight
statement: formalized
proof: formalized
---

# The degeneracy of the hydrogen bound states

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.Degeneracy`, [PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean): 45 declarations (1 instance with no name), 29 with a docstring.

## i. Overview

> The bound states `boundState H N l P` of `Eigenfunctions.lean` at the Bohr level `n = N + l` are
> built from homogeneous harmonic polynomials `P` of degree `l ≤ n`. The space of such polynomials
> in `d` variables has dimension `C(l + d - 1, d - 1) - C(l + d - 3, d - 1)`, which is `2l + 1` for
> `d = 3`. The bound states for different `l` and linearly independent `P` are linearly
> independent, so the level `n` carries at least `Σ_{l ≤ n} (2l + 1) = (n + 1)²` independent
> eigenfunctions in three dimensions.

## ii. Key results

> - `harmonicSubmodule` : homogeneous harmonic polynomials of degree `l` in `d` variables.
> - `finrank_harmonicSubmodule` : their dimension.
> - `boundState_eigen_of_mem_harmonicSubmodule` : such polynomials give bound states.
> - `boundStateMap_injective` : the bound states of one level are linearly independent.
> - `finrank_range_boundStateMap` : they span a space of dimension `Σ_{l ≤ n} dim Harm_l`.
> - `finrank_range_boundStateMap_three` : `(n + 1)²` independent bound states in three dimensions.

## iv. References

> - S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, 2nd ed., Graduate Texts in
>   Mathematics 137, Springer (2001), chapter 5 (Harmonic Polynomials),
>   doi:10.1007/978-1-4757-8137-3\_5.

## A. Homogeneous harmonic polynomials

**`PhyslibAlpha.Hydrogen.polyLaplacian`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L63).

> The Laplacian `Σᵢ ∂ᵢ² P` of a polynomial in `d` variables.

```lean
def polyLaplacian (d : ℕ) : MvPolynomial (Fin d) ℝ →ₗ[ℝ] MvPolynomial (Fin d) ℝ
```

**`PhyslibAlpha.Hydrogen.harmonicSubmodule`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L67).

> The homogeneous harmonic polynomials of degree `l` in `d` variables.

```lean
def harmonicSubmodule (d l : ℕ) : Submodule ℝ (MvPolynomial (Fin d) ℝ)
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L70).

```lean
instance (d l : ℕ) : FiniteDimensional ℝ (harmonicSubmodule d l)
```

**`PhyslibAlpha.Hydrogen.finrank_homogeneousSubmodule`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L77).

> The homogeneous polynomials of degree `l` in `d ≥ 1` variables form a space of dimension
> `C(l + d - 1, d - 1)`: their monomials correspond to multisets of size `l` in `d` letters.

```lean
lemma finrank_homogeneousSubmodule {d : ℕ} (hd : 1 ≤ d) (l : ℕ) :
    Module.finrank ℝ (homogeneousSubmodule (Fin d) ℝ l) = (l + d - 1).choose (d - 1)
```

**`PhyslibAlpha.Hydrogen.polyLaplacian_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L93).

```lean
lemma polyLaplacian_apply {d : ℕ} (P : MvPolynomial (Fin d) ℝ) :
    polyLaplacian d P = ∑ i, pderiv i (pderiv i P)
```

**`PhyslibAlpha.Hydrogen.polyLaplacian_isHomogeneous`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L98).

> The Laplacian lowers the degree of a homogeneous polynomial by two.

```lean
lemma polyLaplacian_isHomogeneous {d l : ℕ} {P : MvPolynomial (Fin d) ℝ}
    (hP : P.IsHomogeneous (l + 2)) : (polyLaplacian d P).IsHomogeneous l
```

**`PhyslibAlpha.Hydrogen.pderiv_eq_zero_of_isHomogeneous_zero`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L104).

> A homogeneous polynomial of degree `0` is constant, so its derivatives vanish.

```lean
lemma pderiv_eq_zero_of_isHomogeneous_zero {d : ℕ} {Q : MvPolynomial (Fin d) ℝ}
    (hQ : Q.IsHomogeneous 0) (i : Fin d) : pderiv i Q = 0
```

**`PhyslibAlpha.Hydrogen.polyLaplacian_eq_zero_of_lt_two`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L114).

> The Laplacian vanishes on homogeneous polynomials of degree `0` and `1`.

```lean
lemma polyLaplacian_eq_zero_of_lt_two {d l : ℕ} {P : MvPolynomial (Fin d) ℝ}
    (hP : P.IsHomogeneous l) (hl : l < 2) : polyLaplacian d P = 0
```

**`PhyslibAlpha.Hydrogen.fischerWeight`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L121).

> The weight `m! = Πⱼ mⱼ!` of a monomial exponent `m`.

```lean
noncomputable def fischerWeight (m : Fin d →₀ ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.fischerWeight_pos`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L123).

```lean
lemma fischerWeight_pos (m : Fin d →₀ ℕ) : 0 < fischerWeight m
```

**`PhyslibAlpha.Hydrogen.fischerWeight_add_single`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L126).

```lean
lemma fischerWeight_add_single (m : Fin d →₀ ℕ) (i : Fin d) :
    fischerWeight (m + Finsupp.single i 1) = fischerWeight m * ((m i : ℝ) + 1)
```

**`PhyslibAlpha.Hydrogen.fischer`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L142).

> The Fischer inner product `Σₘ m! Pₘ Qₘ` of two polynomials.

```lean
noncomputable def fischer (P Q : MvPolynomial (Fin d) ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.fischer_eq_sum`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L145).

```lean
lemma fischer_eq_sum {d : ℕ} {P Q : MvPolynomial (Fin d) ℝ} {S : Finset (Fin d →₀ ℕ)}
    (hS : P.support ⊆ S) :
    fischer P Q = ∑ m ∈ S, fischerWeight m * P.coeff m * Q.coeff m
```

**`PhyslibAlpha.Hydrogen.fischer_zero_left`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L150).

```lean
lemma fischer_zero_left (Q : MvPolynomial (Fin d) ℝ) : fischer 0 Q = 0
```

**`PhyslibAlpha.Hydrogen.fischer_add_left`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L153).

```lean
lemma fischer_add_left (P P' Q : MvPolynomial (Fin d) ℝ) :
    fischer (P + P') Q = fischer P Q + fischer P' Q
```

**`PhyslibAlpha.Hydrogen.fischer_sum_left`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L164).

```lean
lemma fischer_sum_left {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial (Fin d) ℝ)
    (Q : MvPolynomial (Fin d) ℝ) : fischer (∑ i ∈ s, f i) Q = ∑ i ∈ s, fischer (f i) Q
```

**`PhyslibAlpha.Hydrogen.fischer_sum_right`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L171).

```lean
lemma fischer_sum_right {ι : Type*} (s : Finset ι) (P : MvPolynomial (Fin d) ℝ)
    (f : ι → MvPolynomial (Fin d) ℝ) : fischer P (∑ i ∈ s, f i) = ∑ i ∈ s, fischer P (f i)
```

**`PhyslibAlpha.Hydrogen.fischer_zero_right`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L176).

```lean
lemma fischer_zero_right (P : MvPolynomial (Fin d) ℝ) : fischer P 0 = 0
```

**`PhyslibAlpha.Hydrogen.fischer_mul_X`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L180).

> Multiplication by `Xᵢ` is adjoint to `∂ᵢ` for the Fischer inner product.

```lean
lemma fischer_mul_X (P Q : MvPolynomial (Fin d) ℝ) (i : Fin d) :
    fischer (P * X i) Q = fischer P (pderiv i Q)
```

**`PhyslibAlpha.Hydrogen.fischer_self_pos`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L189).

> The Fischer inner product is positive definite.

```lean
lemma fischer_self_pos {P : MvPolynomial (Fin d) ℝ} (hP : P ≠ 0) : 0 < fischer P P
```

**`PhyslibAlpha.Hydrogen.rSq`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L195).

> `r² = Σᵢ Xᵢ²`.

```lean
def rSq (d : ℕ) : MvPolynomial (Fin d) ℝ
```

**`PhyslibAlpha.Hydrogen.rSq_isHomogeneous`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L197).

```lean
lemma rSq_isHomogeneous (d : ℕ) : (rSq d).IsHomogeneous 2
```

**`PhyslibAlpha.Hydrogen.rSq_ne_zero`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L200).

```lean
lemma rSq_ne_zero {d : ℕ} (hd : 1 ≤ d) : rSq d ≠ 0
```

**`PhyslibAlpha.Hydrogen.eq_zero_of_polyLaplacian_eq_zero_of_eq_rSq_mul`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L207).

> A harmonic polynomial divisible by `r²` vanishes: `⟨r² P, r² P⟩ = ⟨P, Δ(r² P)⟩ = 0`.

```lean
lemma eq_zero_of_polyLaplacian_eq_zero_of_eq_rSq_mul {d : ℕ} {P Q : MvPolynomial (Fin d) ℝ}
    (hQ : polyLaplacian d Q = 0) (hQP : Q = rSq d * P) : Q = 0
```

**`PhyslibAlpha.Hydrogen.finrank_harmonicSubmodule_add_finrank`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L224).

> `dim Harm_{l+2} + dim Hom_l = dim Hom_{l+2}`: the Laplacian `Hom_{l+2} → Hom_l` is onto.

```lean
lemma finrank_harmonicSubmodule_add_finrank {d : ℕ} (hd : 1 ≤ d) (l : ℕ) :
    Module.finrank ℝ (harmonicSubmodule d (l + 2)) +
        Module.finrank ℝ (homogeneousSubmodule (Fin d) ℝ l) =
      Module.finrank ℝ (homogeneousSubmodule (Fin d) ℝ (l + 2))
```

**`PhyslibAlpha.Hydrogen.finrank_harmonicSubmodule`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L275).

> The homogeneous harmonic polynomials of degree `l` in `d ≥ 2` variables form a space of
> dimension `C(l + d - 1, d - 1) - C(l + d - 3, d - 1)`.

```lean
lemma finrank_harmonicSubmodule {d : ℕ} (hd : 2 ≤ d) (l : ℕ) :
    Module.finrank ℝ (harmonicSubmodule d l) =
      (l + d - 1).choose (d - 1) - (l + d - 3).choose (d - 1)
```

**`PhyslibAlpha.Hydrogen.finrank_harmonicSubmodule_three`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L293).

> In three variables the homogeneous harmonic polynomials of degree `l` form a space of
> dimension `2l + 1`.

```lean
lemma finrank_harmonicSubmodule_three (l : ℕ) :
    Module.finrank ℝ (harmonicSubmodule 3 l) = 2 * l + 1
```

**`PhyslibAlpha.Hydrogen.sum_two_mul_add_one`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L306).

> `Σ_{l ≤ n} (2l + 1) = (n + 1)²`.

```lean
lemma sum_two_mul_add_one (n : ℕ) : ∑ l ∈ Finset.range (n + 1), (2 * l + 1) = (n + 1) ^ 2
```

## B. Polynomials as functions on space

**`PhyslibAlpha.Hydrogen.toFun`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L318).

> A polynomial in `d` variables as a function on `Space d`.

```lean
def toFun {d : ℕ} (P : MvPolynomial (Fin d) ℝ) (y : Space d) : ℝ
```

**`PhyslibAlpha.Hydrogen.toFun_C`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L321).

```lean
lemma toFun_C {d : ℕ} (a : ℝ) : toFun (C a : MvPolynomial (Fin d) ℝ) = fun _ => a
```

**`PhyslibAlpha.Hydrogen.toFun_add`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L326).

```lean
lemma toFun_add {d : ℕ} (P Q : MvPolynomial (Fin d) ℝ) : toFun (P + Q) = toFun P + toFun Q
```

**`PhyslibAlpha.Hydrogen.toFun_mul_X`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L330).

```lean
lemma toFun_mul_X {d : ℕ} (P : MvPolynomial (Fin d) ℝ) (j : Fin d) :
    toFun (P * X j) = fun y => toFun P y * y j
```

**`PhyslibAlpha.Hydrogen.contDiff_toFun_infty`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L336).

> Polynomials are smooth.

```lean
lemma contDiff_toFun_infty {d : ℕ} (P : MvPolynomial (Fin d) ℝ) : ContDiff ℝ ∞ (toFun P)
```

**`PhyslibAlpha.Hydrogen.contDiff_toFun`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L345).

> Polynomials are twice continuously differentiable.

```lean
lemma contDiff_toFun {d : ℕ} (P : MvPolynomial (Fin d) ℝ) : ContDiff ℝ 2 (toFun P)
```

**`PhyslibAlpha.Hydrogen.differentiable_toFun`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L348).

```lean
lemma differentiable_toFun {d : ℕ} (P : MvPolynomial (Fin d) ℝ) : Differentiable ℝ (toFun P)
```

**`PhyslibAlpha.Hydrogen.deriv_toFun`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L352).

> The partial derivative of a polynomial function is the polynomial partial derivative.

```lean
lemma deriv_toFun {d : ℕ} (i : Fin d) (P : MvPolynomial (Fin d) ℝ) :
    ∂[i] (toFun P) = toFun (pderiv i P)
```

**`PhyslibAlpha.Hydrogen.euler_toFun`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L372).

> Euler's relation `Σᵢ yᵢ ∂ᵢP = l P` for a homogeneous polynomial of degree `l`.

```lean
lemma euler_toFun {d l : ℕ} {P : MvPolynomial (Fin d) ℝ} (hP : P.IsHomogeneous l)
    (y : Space d) : ∑ i, y i * ∂[i] (toFun P) y = l * toFun P y
```

**`PhyslibAlpha.Hydrogen.laplacian_toFun`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L379).

> The Laplacian of a polynomial function is the polynomial Laplacian.

```lean
lemma laplacian_toFun {d : ℕ} (P : MvPolynomial (Fin d) ℝ) (y : Space d) :
    Δ (toFun P) y = toFun (polyLaplacian d P) y
```

**`PhyslibAlpha.Hydrogen.boundState_eigen_of_mem_harmonicSubmodule`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L386).

> A homogeneous harmonic polynomial of degree `l` gives the bound state
> `boundState H N l P` of energy `E_{N+l}`, away from the nucleus.

```lean
lemma boundState_eigen_of_mem_harmonicSubmodule (H : QuantumMechanics.HydrogenAtom d)
    (hd : 2 ≤ d) (hk : 0 < H.k) (N l : ℕ) {P : MvPolynomial (Fin d) ℝ}
    (hP : P ∈ harmonicSubmodule d l) {x : Space d} (hx : x ≠ 0) :
    -((Constants.ℏ : ℝ) ^ 2 / (2 * H.m)) * Δ (boundState H N l (toFun P)) x +
        H.potential x * boundState H N l (toFun P) x =
      H.energyLevel (N + l) * boundState H N l (toFun P) x
```

## C. Linear independence of the bound states

**`PhyslibAlpha.Hydrogen.toFun_smul_of_isHomogeneous`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L405).

> A homogeneous polynomial of degree `l` scales as `P(t y) = t^l P(y)`.

```lean
lemma toFun_smul_of_isHomogeneous {d l : ℕ} {P : MvPolynomial (Fin d) ℝ}
    (hP : P.IsHomogeneous l) (t : ℝ) (y : Space d) : toFun P (t • y) = t ^ l * toFun P y
```

**`PhyslibAlpha.Hydrogen.eq_zero_of_sum_pow_mul`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L418).

> If `Σ_l c_l t^l f_l(t) = 0` for all `t > 0`, with continuous `f_l` and `f_l(0) ≠ 0`, then
> all `c_l` vanish: compare the lowest powers of `t` as `t → 0⁺`.

```lean
lemma eq_zero_of_sum_pow_mul {n : ℕ} (c : Fin (n + 1) → ℝ) (f : Fin (n + 1) → ℝ → ℝ)
    (hf : ∀ l, Continuous (f l)) (hf0 : ∀ l, f l 0 ≠ 0)
    (h : ∀ t, 0 < t → ∑ l, c l * t ^ (l : ℕ) * f l t = 0) : c = 0
```

**`PhyslibAlpha.Hydrogen.boundStateMap`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L477).

> The bound states of the level `n`: a family `(P_l)_{l ≤ n}` of homogeneous harmonic
> polynomials gives `Σ_l boundState H (n - l) l P_l`.

```lean
def boundStateMap (H : QuantumMechanics.HydrogenAtom d) (n : ℕ) :
    ((l : Fin (n + 1)) → harmonicSubmodule d l) →ₗ[ℝ] (Space d → ℝ)
```

**`PhyslibAlpha.Hydrogen.boundStateMap_injective`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L491).

> The bound states of one level, for different `l` and linearly independent polynomials, are
> linearly independent. Along a ray `y = t ω` the summand of degree `l` is `e^(-κ t ‖ω‖)` times
> `t^l P_l(ω)` times a Laguerre polynomial in `t` that does not vanish at `t = 0`.

```lean
lemma boundStateMap_injective (H : QuantumMechanics.HydrogenAtom d) (n : ℕ) :
    Function.Injective (boundStateMap H n)
```

**`PhyslibAlpha.Hydrogen.finrank_range_boundStateMap`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L532).

> The bound states of the level `n` span a space of dimension `Σ_{l ≤ n} dim Harm_l`.

```lean
lemma finrank_range_boundStateMap (H : QuantumMechanics.HydrogenAtom d) (n : ℕ) :
    Module.finrank ℝ (LinearMap.range (boundStateMap H n)) =
      ∑ l : Fin (n + 1), Module.finrank ℝ (harmonicSubmodule d l)
```

**`PhyslibAlpha.Hydrogen.finrank_range_boundStateMap_three`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean#L538).

> In three dimensions the level `n` carries `(n + 1)²` linearly independent bound states.

```lean
lemma finrank_range_boundStateMap_three (H : QuantumMechanics.HydrogenAtom 3)
    (n : ℕ) : Module.finrank ℝ (LinearMap.range (boundStateMap H n)) = (n + 1) ^ 2
```

## Depends on

- [The bound-state wave functions of the `d`-dimensional hydrogen atom](eigenfunctions.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/Degeneracy.lean)
