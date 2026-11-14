---
declaration: module
origin: cited
lean: TwoHiggsDoublet.EffectivePotential.eval_aeval_comp, TwoHiggsDoublet.EffectivePotential.cartanSubst, TwoHiggsDoublet.EffectivePotential.eval_cartanSubst, TwoHiggsDoublet.EffectivePotential.aeval_cartanSubst_eq, TwoHiggsDoublet.EffectivePotential.residualSubst, TwoHiggsDoublet.EffectivePotential.eval_residualSubst, TwoHiggsDoublet.EffectivePotential.aeval_residualSubst_eq, TwoHiggsDoublet.EffectivePotential.hyperchargeEigen
statement: formalized
proof: formalized
---

# The two Higgs doublet potential as a polynomial in the gauge invariants

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.Invariants`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean): 56 declarations, 47 with a docstring.

> Every gauge-invariant polynomial 2HDM potential is a polynomial in the four Gram bilinears.

## i. Overview

> In the *bilinear formalism* of the two Higgs doublet model (hep-ph/0605184
> [ref: arxiv\_hep\_ph\_0605184]) the four gauge-invariant bilinears — the Gram vector `gramVector`
> — describe the gauge orbits of the configuration space. This file proves the corresponding
> statement for the potential: every
> gauge-invariant polynomial effective potential is a polynomial in these four gauge-invariant
> bilinears.
>
> The proof gauge-fixes the potential to the polynomial family of orbit representatives `repHiggs X`
> and runs the following physical pipeline:
>
> 1. **Charge balancing.** Invariance under the gauge torus forces the potential, written in
>    hypercharge eigen-coordinates, to be supported only on hypercharge-neutral monomials.
> 2. **Generation.** Every neutral monomial is a product of the five neutral gauge-invariant
>    quadratic bilinears, so the potential is a polynomial in them.
> 3. **Clearing the norms.** A power of `‖Φ1‖²` (resp. `‖Φ2‖²`, via the doublet swap) times the
>    potential is a genuine polynomial in the Gram vector.
> 4. **Coprimality.** `‖Φ1‖²` and `‖Φ2‖²` are coprime in the (algebraically independent) Gram ring,
>    which removes these factors and yields the Gram polynomial.
>
> Mathematically the result is the first fundamental theorem of invariant theory for `SU(2)`
> acting on two doublets in `ℂ²`.

## ii. Key results

> * `exists_polynomial_repHiggs_sliceBilinear` — on gauge representatives, the potential is a
>   polynomial in the five real gauge-invariant bilinears.
> * `exists_normSq_Φ1_clearing`, `exists_normSq_Φ2_clearing` — a power of `‖Φ1‖²` (resp. `‖Φ2‖²`)
>   times the potential is a polynomial in the Gram vector.
> * `exists_polynomial_on_repHiggs` — the potential on representatives is a polynomial in the Gram
>   vector.
> * `effectivePotential_is_polynomial_gramVector` — a gauge-invariant polynomial potential is a
>   polynomial in the four gauge-invariant bilinears.

## iv. References

> * The bilinear formalism: https://arxiv.org/abs/hep-ph/0605184. [ref: arxiv\_hep\_ph\_0605184]

**`TwoHiggsDoublet.EffectivePotential.eval_aeval_comp`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L83).

> Pushing an evaluation through an `aeval` substitution.

```lean
lemma eval_aeval_comp {R : Type*} [CommRing R] {κ ι : Type*} (x : ι → R)
    (f : κ → MvPolynomial ι R) (G : MvPolynomial κ R) :
    eval x (aeval f G) = eval (fun i => eval x (f i)) G
```

## A. Gauge-torus invariance of the potential on the slice

> Invariance of the potential under the gauge torus forces the slice polynomial `P` to be invariant
> under the hypercharge rotations of its variables: the Cartan rotation `cartanSubst` and the residual
> `U(1)` rotation `residualSubst`.

**`TwoHiggsDoublet.EffectivePotential.cartanSubst`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L100).

> The Cartan hypercharge rotation of the slice parameters, as a substitution of the polynomial
> variables.

```lean
noncomputable def cartanSubst (u : unitary ℂ) : Fin 6 → MvPolynomial (Fin 6) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.eval_cartanSubst`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L106).

```lean
lemma eval_cartanSubst (u : unitary ℂ) (a : Fin 6 → ℝ) :
    (fun k => MvPolynomial.eval a (cartanSubst u k)) = cartanRotParam u a
```

**`TwoHiggsDoublet.EffectivePotential.aeval_cartanSubst_eq`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L115).

> Gauge (Cartan) invariance of the potential forces the slice polynomial to be invariant under the
> hypercharge rotation of its variables.

```lean
lemma aeval_cartanSubst_eq {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) (u : unitary ℂ) :
    aeval (cartanSubst u) P = P
```

**`TwoHiggsDoublet.EffectivePotential.residualSubst`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L128).

> The residual `U(1)` rotation of the perpendicular parameter, as a substitution.

```lean
noncomputable def residualSubst (c : unitary ℂ) : Fin 6 → MvPolynomial (Fin 6) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.eval_residualSubst`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L134).

```lean
lemma eval_residualSubst (c : unitary ℂ) (a : Fin 6 → ℝ) :
    (fun k => MvPolynomial.eval a (residualSubst c k)) = resRotParam c a
```

**`TwoHiggsDoublet.EffectivePotential.aeval_residualSubst_eq`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L143).

> Gauge (residual `U(1)`) invariance forces the slice polynomial to be invariant under the
> perpendicular rotation of its variables.

```lean
lemma aeval_residualSubst_eq {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) (c : unitary ℂ) :
    aeval (residualSubst c) P = P
```

## B. Hypercharge eigen-coordinates and charge balancing

> Changing to hypercharge eigen-coordinates `z, z̄, w₀, w̄₀, w₁, w̄₁` diagonalises the gauge-torus
> rotation into a scaling by the hypercharges `cartanCharge` (Cartan) and `hyperCharge` (residual).
> Feeding an infinite-order phase into the invariance from part A shows that every monomial of the
> potential carrying nonzero hypercharge has vanishing coefficient.

**`TwoHiggsDoublet.EffectivePotential.hyperchargeEigen`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L166).

> Change to hypercharge eigen-coordinates: `aₖ` in terms of `z, z̄, w₀, w̄₀, w₁, w̄₁`
> (indices `0..5`). This diagonalises the gauge-torus rotation into a scaling.

```lean
noncomputable def hyperchargeEigen : Fin 6 → MvPolynomial (Fin 6) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.diagCartan`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L173).

> The Cartan hypercharge, diagonal in eigen-coordinates: charges `(1,-1,1,-1,-1,1)`.

```lean
noncomputable def diagCartan (u : unitary ℂ) : Fin 6 → MvPolynomial (Fin 6) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.diagRes`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L179).

> The residual `U(1)`, diagonal in eigen-coordinates: only the perpendicular pair is charged.

```lean
noncomputable def diagRes (c : unitary ℂ) : Fin 6 → MvPolynomial (Fin 6) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.bind₁_diagCartan_hyperchargeEigen`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L185).

> Conjugation identity: the diagonal Cartan scaling, pulled back through the eigen-coordinate
> change, is the (complexified) Cartan rotation substitution.

```lean
lemma bind₁_diagCartan_hyperchargeEigen (u : unitary ℂ) (k : Fin 6) :
    bind₁ (diagCartan u) (hyperchargeEigen k)
      = bind₁ hyperchargeEigen (map (algebraMap ℝ ℂ) (cartanSubst u k))
```

**`TwoHiggsDoublet.EffectivePotential.bind₁_diagRes_hyperchargeEigen`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L199).

> Conjugation identity for the residual `U(1)`.

```lean
lemma bind₁_diagRes_hyperchargeEigen (c : unitary ℂ) (k : Fin 6) :
    bind₁ (diagRes c) (hyperchargeEigen k)
      = bind₁ hyperchargeEigen (map (algebraMap ℝ ℂ) (residualSubst c k))
```

**`TwoHiggsDoublet.EffectivePotential.cartanCharge`**, a def, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L214).

> The Cartan hypercharges of `z, z̄, w₀, w̄₀, w₁, w̄₁`.

```lean
def cartanCharge : Fin 6 → ℤ
```

**`TwoHiggsDoublet.EffectivePotential.hyperCharge`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L217).

> The residual-`U(1)` hypercharges (only the perpendicular pair is charged).

```lean
def hyperCharge : Fin 6 → ℤ
```

**`TwoHiggsDoublet.EffectivePotential.Qslice`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L221).

> The slice potential, complexified and written in hypercharge eigen-coordinates.

```lean
noncomputable def Qslice (P : MvPolynomial (Fin 6) ℝ) : MvPolynomial (Fin 6) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.diagCartan_eq`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L226).

> The Cartan diagonal in the charge form consumed by the charge-balancing engine.

```lean
lemma diagCartan_eq (u : unitary ℂ) :
    diagCartan u = fun i => C ((u : ℂ) ^ (cartanCharge i)) * X i
```

**`TwoHiggsDoublet.EffectivePotential.diagRes_eq`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L235).

> The residual diagonal in the charge form consumed by the engine.

```lean
lemma diagRes_eq (c : unitary ℂ) :
    diagRes c = fun i => C (((c : ℂ) ^ 6) ^ (hyperCharge i)) * X i
```

**`TwoHiggsDoublet.EffectivePotential.bind₁_diagCartan_Qslice`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L247).

> In eigen-coordinates, the Cartan hypercharge acts by the diagonal scaling, and the slice
> potential is invariant under it.

```lean
lemma bind₁_diagCartan_Qslice {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) (u : unitary ℂ) :
    bind₁ (diagCartan u) (Qslice P) = Qslice P
```

**`TwoHiggsDoublet.EffectivePotential.bind₁_diagRes_Qslice`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L259).

> Likewise for the residual `U(1)`.

```lean
lemma bind₁_diagRes_Qslice {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) (c : unitary ℂ) :
    bind₁ (diagRes c) (Qslice P) = Qslice P
```

**`TwoHiggsDoublet.EffectivePotential.exists_infiniteOrder_unitary`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L270).

> There is a gauge phase of infinite order (`exp i`), needed to run charge balancing.

```lean
lemma exists_infiniteOrder_unitary :
    ∃ ω : unitary ℂ, ∀ n : ℤ, (ω : ℂ) ^ n = 1 → n = 0
```

**`TwoHiggsDoublet.EffectivePotential.coeff_Qslice_eq_zero`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L296).

> **Hypercharge balancing.** Every monomial of the slice potential `Qslice P` (in eigen-
> coordinates) that carries nonzero Cartan or residual hypercharge has vanishing coefficient.

```lean
lemma coeff_Qslice_eq_zero {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) (m : Fin 6 →₀ ℕ)
    (hm : (∑ i ∈ m.support, (m i : ℤ) * cartanCharge i ≠ 0) ∨
          (∑ i ∈ m.support, (m i : ℤ) * hyperCharge i ≠ 0)) :
    (Qslice P).coeff m = 0
```

## C. Generation by the neutral gauge-invariant bilinears

> The hypercharge-neutral monomials of `Qslice P` are exactly the products of the five neutral
> quadratic bilinears `z z̄, w₀ w̄₀, z w̄₀, z̄ w₀, w₁ w̄₁` — the gauge invariants.
> This is the (abelian)generation step: combined Cartan- and residual-neutrality of a
> monomial forces it to be a product of
> these five, because every charged variable carries a unit Cartan charge and the residual charges
> come in an exact `±1` pair.

**`TwoHiggsDoublet.EffectivePotential.neutralBilinear`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L330).

> The five hypercharge-neutral quadratic bilinears in eigen-coordinates:
> `z z̄`, `w₀ w̄₀`, `z w̄₀`, `z̄ w₀`, `w₁ w̄₁`.

```lean
noncomputable def neutralBilinear : Fin 5 → MvPolynomial (Fin 6) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.charge_univ_eq_support`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L334).

> The charge of a monomial, summed over the whole index set, equals the sum over its support.

```lean
lemma charge_univ_eq_support (w : Fin 6 → ℤ) (m : Fin 6 →₀ ℕ) :
    ∑ i, (m i : ℤ) * w i = ∑ i ∈ m.support, (m i : ℤ) * w i
```

**`TwoHiggsDoublet.EffectivePotential.chargeSum_add`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L342).

> A charge sum is additive in the monomial.

```lean
lemma chargeSum_add (w : Fin 6 → ℤ) (a b : Fin 6 →₀ ℕ) :
    ∑ k, ((a + b) k : ℤ) * w k = (∑ k, (a k : ℤ) * w k) + ∑ k, (b k : ℤ) * w k
```

**`TwoHiggsDoublet.EffectivePotential.chargeSum_single`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L350).

> The charge sum of a single generator is the charge of that variable.

```lean
lemma chargeSum_single (w : Fin 6 → ℤ) (i : Fin 6) :
    ∑ k, ((Finsupp.single i (1 : ℕ)) k : ℤ) * w k = w i
```

**`TwoHiggsDoublet.EffectivePotential.monomial_mem_adjoin_neutralBilinear`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L356).

> **Generation.** Every hypercharge-neutral monomial is a product of the five bilinears.

```lean
lemma monomial_mem_adjoin_neutralBilinear (m : Fin 6 →₀ ℕ)
    (hA : ∑ i, (m i : ℤ) * cartanCharge i = 0) (hB : ∑ i, (m i : ℤ) * hyperCharge i = 0) :
    monomial m (1 : ℂ) ∈ Algebra.adjoin ℂ (Set.range neutralBilinear)
```

**`TwoHiggsDoublet.EffectivePotential.Qslice_mem_adjoin_neutralBilinear`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L488).

> The slice potential lies in the subalgebra generated by the five bilinears: every monomial that
> survives is hypercharge-neutral, hence a product of the bilinears.

```lean
lemma Qslice_mem_adjoin_neutralBilinear {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) :
    Qslice P ∈ Algebra.adjoin ℂ (Set.range neutralBilinear)
```

**`TwoHiggsDoublet.EffectivePotential.exists_aeval_neutralBilinear`**, a lemma, [line 514](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L514).

> Consequently the complexified slice potential is `aeval neutralBilinear G` for some polynomial
> `G` in the five bilinears.

```lean
lemma exists_aeval_neutralBilinear {V : EffectivePotential} (hI : IsInvariant V)
    {P : MvPolynomial (Fin 6) ℝ} (hP : ∀ a, V (sliceR a) = P.eval a) :
    ∃ G : MvPolynomial (Fin 5) ℂ, aeval neutralBilinear G = Qslice P
```

## D. The potential on representatives as a polynomial in the bilinears

> Evaluating at the hypercharge eigen-point of a representative `repHiggs X`, and descending from the
> complex value back to its real part, turns the generation result of part C into the statement that
> the value `V (repHiggs X)` is a polynomial in the five real gauge-invariant bilinears
> `‖Φ1‖², Re⟪⟫, Im⟪⟫, |Φ2₁|², |Φ2₀|²`.

**`TwoHiggsDoublet.EffectivePotential.aRep`**, a def, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L532).

> The slice parameters realising `repHiggs X` as a point of the slice family.

```lean
def aRep (X : Fin 4 → ℝ) : Fin 6 → ℝ
```

**`TwoHiggsDoublet.EffectivePotential.repHiggs_eq_sliceR`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L534).

```lean
lemma repHiggs_eq_sliceR (X : Fin 4 → ℝ) : repHiggs X = sliceR (aRep X)
```

**`TwoHiggsDoublet.EffectivePotential.eigenPoint`**, a def, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L540).

> The hypercharge eigen-point `(z, z̄, w₀, w̄₀, w₁, w̄₁)` of `repHiggs X`: here `z = X₀` is real,
> `w₀ = X₁ + i X₂` and `w₁ = X₃` is real.

```lean
noncomputable def eigenPoint (X : Fin 4 → ℝ) : Fin 6 → ℂ
```

**`TwoHiggsDoublet.EffectivePotential.aeval_hyperchargeEigen_eigenPoint`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L547).

> The eigen-coordinate change sends the eigen-point of `repHiggs X` back to its
> slice parameters.

```lean
lemma aeval_hyperchargeEigen_eigenPoint (X : Fin 4 → ℝ) (k : Fin 6) :
    aeval (eigenPoint X) (hyperchargeEigen k) = algebraMap ℝ ℂ (aRep X k)
```

**`TwoHiggsDoublet.EffectivePotential.eval_Qslice_eigenPoint`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L558).

> The complexified slice potential, evaluated at the eigen-point of `repHiggs X`, returns the real
> value `V (repHiggs X)`.

```lean
lemma eval_Qslice_eigenPoint (P : MvPolynomial (Fin 6) ℝ) (X : Fin 4 → ℝ) :
    eval (eigenPoint X) (Qslice P) = algebraMap ℝ ℂ (P.eval (aRep X))
```

**`TwoHiggsDoublet.EffectivePotential.realPart`**, a def, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L570).

> The real part of a complex polynomial, taken coefficient-wise.

```lean
noncomputable def realPart (H : MvPolynomial (Fin 5) ℂ) : MvPolynomial (Fin 5) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.realPart_coeff`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L574).

```lean
lemma realPart_coeff (H : MvPolynomial (Fin 5) ℂ) (m : Fin 5 →₀ ℕ) :
    (realPart H).coeff m = (H.coeff m).re
```

**`TwoHiggsDoublet.EffectivePotential.realPart_C`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L579).

```lean
lemma realPart_C (a : ℂ) : realPart (C a) = C a.re
```

**`TwoHiggsDoublet.EffectivePotential.realPart_add`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L583).

```lean
lemma realPart_add (p q : MvPolynomial (Fin 5) ℂ) :
    realPart (p + q) = realPart p + realPart q
```

**`TwoHiggsDoublet.EffectivePotential.realPart_mul_X`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L588).

```lean
lemma realPart_mul_X (p : MvPolynomial (Fin 5) ℂ) (i : Fin 5) :
    realPart (p * X i) = realPart p * X i
```

**`TwoHiggsDoublet.EffectivePotential.realPart_eval`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L597).

> Evaluating a complex polynomial at a real point and taking the real part is the same as
> evaluating its real part.

```lean
lemma realPart_eval (H : MvPolynomial (Fin 5) ℂ) (y : Fin 5 → ℝ) :
    (eval (fun j => (↑(y j) : ℂ)) H).re = (realPart H).eval y
```

**`TwoHiggsDoublet.EffectivePotential.sliceBilinear`**, a def, [line 608](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L608).

> The five real gauge-invariant bilinears, evaluated at `repHiggs X`:
> `‖Φ1‖², Re⟪⟫, Im⟪⟫, |Φ2₁|², |Φ2₀|²`.

```lean
def sliceBilinear (X : Fin 4 → ℝ) : Fin 5 → ℝ
```

**`TwoHiggsDoublet.EffectivePotential.transf`**, a def, [line 614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L614).

> The complex substitution expressing each bilinear, at the eigen-point, through the real
> generators (the off-diagonal pair `z w̄₀, z̄ w₀` mix `Re⟪⟫` and `Im⟪⟫`).

```lean
noncomputable def transf : Fin 5 → MvPolynomial (Fin 5) ℂ
```

**`TwoHiggsDoublet.EffectivePotential.neutralBilinear_eval_eigenPoint`**, a lemma, [line 620](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L620).

> The bilinears at the eigen-point of `repHiggs X` are the real generators,
> read through `transf`.

```lean
lemma neutralBilinear_eval_eigenPoint (X : Fin 4 → ℝ) (i : Fin 5) :
    eval (eigenPoint X) (neutralBilinear i)
      = eval (fun j => (↑(sliceBilinear X j) : ℂ)) (transf i)
```

**`TwoHiggsDoublet.EffectivePotential.exists_polynomial_repHiggs_sliceBilinear`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L633).

> **The potential on representatives, in the bilinears.** A gauge-invariant polynomial potential,
> on the representative family, is a polynomial in the five real gauge-invariant bilinears
> `‖Φ1‖², Re⟪⟫, Im⟪⟫, |Φ2₁|², |Φ2₀|²`.

```lean
lemma exists_polynomial_repHiggs_sliceBilinear {V : EffectivePotential} {n : ℕ}
    (hI : IsInvariant V) (h : HasMaxMassDimLE V n) :
    ∃ p : MvPolynomial (Fin 5) ℝ, ∀ X : Fin 4 → ℝ, V (repHiggs X) = p.eval (sliceBilinear X)
```

## E. Clearing the `‖Φ1‖²` and `‖Φ2‖²` factors

> Part D expresses the value as a polynomial in the bilinears, but two of them — `|Φ2₀|²`
>   and `|Φ2₁|²`
> — are not directly Gram polynomials. Multiplying by a power of `‖Φ1‖²` clears these; the
> doublet swap of `SwapDoublet` then gives the mirror statement with `‖Φ2‖²`.

**`TwoHiggsDoublet.EffectivePotential.sliceBilinearPoly`**, a def, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L661).

> The five bilinear generators, as polynomials in the four representative parameters.

```lean
noncomputable def sliceBilinearPoly : Fin 5 → MvPolynomial (Fin 4) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.gramPoly`**, a def, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L666).

> The four Gram components, as polynomials in the four representative parameters.

```lean
noncomputable def gramPoly : Fin 1 ⊕ Fin 3 → MvPolynomial (Fin 4) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.sliceBilinearPoly_eval`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L671).

```lean
lemma sliceBilinearPoly_eval (X : Fin 4 → ℝ) (i : Fin 5) :
    (sliceBilinearPoly i).eval X = sliceBilinear X i
```

**`TwoHiggsDoublet.EffectivePotential.gramPoly_eval`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L676).

```lean
lemma gramPoly_eval (X : Fin 4 → ℝ) (μ : Fin 1 ⊕ Fin 3) :
    (gramPoly μ).eval X = (repHiggs X).gramVector μ
```

**`TwoHiggsDoublet.EffectivePotential.exists_clearing_mem`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L688).

> Some power of `‖Φ1‖² = X₀²` times the value polynomial lies in the Gram
> subalgebra: multiplying by `X₀²` pairs each `X₁²+X₂²` into `(X₀X₁)²+(X₀X₂)²` and each `X₃²` into
> the determinant `X₀²X₃²`, both of which are Gram polynomials.

```lean
lemma exists_clearing_mem (p : MvPolynomial (Fin 5) ℝ) :
    ∃ N : ℕ, (X 0) ^ (2 * N) * aeval sliceBilinearPoly p ∈
      Algebra.adjoin ℝ (Set.range gramPoly)
```

**`TwoHiggsDoublet.EffectivePotential.exists_gram_clearing`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L750).

> **Denominator clearing.** For the value polynomial `p`, some power of `‖Φ1‖² = X₀²`
> times `p ∘ sliceBilinear` is a polynomial in the Gram vector.

```lean
lemma exists_gram_clearing (p : MvPolynomial (Fin 5) ℝ) :
    ∃ (A : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ) (N : ℕ), ∀ X : Fin 4 → ℝ,
      (X 0) ^ (2 * N) * p.eval (sliceBilinear X) = A.eval ((repHiggs X).gramVector)
```

**`TwoHiggsDoublet.EffectivePotential.exists_normSq_Φ1_clearing`**, a lemma, [line 768](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L768).

> **`‖Φ1‖²`-clearing, on all configurations.** A power of `‖Φ1‖²` times a gauge-invariant
> polynomial potential is, everywhere, a polynomial in the Gram vector.

```lean
lemma exists_normSq_Φ1_clearing {V : EffectivePotential} {n : ℕ}
    (hI : IsInvariant V) (h : HasMaxMassDimLE V n) :
    ∃ (A : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ) (N : ℕ), ∀ φ : TwoHiggsDoublet,
      (‖φ.Φ1‖ ^ 2) ^ N * V φ = A.eval φ.gramVector
```

**`TwoHiggsDoublet.EffectivePotential.swapSubst`**, a def, [line 787](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L787).

> The Gram-vector substitution induced by swapping the doublets (sign flip on the imaginary and
> difference components).

```lean
noncomputable def swapSubst : (Fin 1 ⊕ Fin 3) → MvPolynomial (Fin 1 ⊕ Fin 3) ℝ
```

**`TwoHiggsDoublet.EffectivePotential.exists_normSq_Φ2_clearing`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L794).

> **`‖Φ2‖²`-clearing, on all configurations.** A power of `‖Φ2‖²` times a gauge-invariant
> polynomial potential is, everywhere, a polynomial in the Gram vector. Obtained from
> `exists_normSq_Φ1_clearing` for the doublet-swapped potential.

```lean
lemma exists_normSq_Φ2_clearing {V : EffectivePotential} {n : ℕ}
    (hI : IsInvariant V) (h : HasMaxMassDimLE V n) :
    ∃ (B : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ) (M : ℕ), ∀ φ : TwoHiggsDoublet,
      (‖φ.Φ2‖ ^ 2) ^ M * V φ = B.eval φ.gramVector
```

## F. Independence and coprimality of the Gram invariants

> The four Gram invariants are algebraically independent (`gramPoly_injective`), and the two linear
> combinations `‖Φ1‖² = (g₀+g₃)/2` and `‖Φ2‖² = (g₀-g₃)/2` are coprime in the Gram ring
> (`uPow_dvd`). Together these let the `‖Φ1‖²` and `‖Φ2‖²` factors be cancelled.

**`TwoHiggsDoublet.EffectivePotential.gramPoly_injective`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L821).

> The four Gram invariants are algebraically independent: the Gram substitution is injective.

```lean
lemma gramPoly_injective :
    Function.Injective
      (aeval gramPoly : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ → MvPolynomial (Fin 4) ℝ)
```

**`TwoHiggsDoublet.EffectivePotential.uPow_dvd`**, a lemma, [line 894](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L894).

> `‖Φ1‖²` and `‖Φ2‖²`, as the distinct linear forms `(g₀±g₃)/2` of the Gram ring, are coprime:
> if `‖Φ1‖²ᴺ · B = ‖Φ2‖²ᴹ · A` then `‖Φ1‖²ᴺ ∣ A`.

```lean
lemma uPow_dvd {N M : ℕ} {A B : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ}
    (hAB : (C (1 / 2) * (X (Sum.inl 0) + X (Sum.inr 2))) ^ N * B
       = (C (1 / 2) * (X (Sum.inl 0) - X (Sum.inr 2))) ^ M * A) :
    (C (1 / 2) * (X (Sum.inl 0) + X (Sum.inr 2))) ^ N ∣ A
```

## G. The gauge-invariant potential as a polynomial in the Gram vector

> Every configuration is gauge equivalent to a representative `repHiggs X`
> (`exists_smul_eq_repHiggs`) whose Gram vector is polynomial in the parameters
> (`gramVector_repHiggs_*`). Combining the two norm clearings of part E with the coprimality of part F
> removes the `‖Φ1‖²`/`‖Φ2‖²` factors and produces the Gram polynomial on representatives
> (`exists_polynomial_on_repHiggs`); gauge invariance then transports it to all configurations.

**`TwoHiggsDoublet.EffectivePotential.exists_polynomial_on_repHiggs`**, a lemma, [line 949](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L949).

> **On representatives.** A gauge-invariant polynomial potential, restricted to the polynomial
> family of orbit representatives `repHiggs X`, is a polynomial in the Gram components of that
> family. Proved by the doublet-swap argument: clearing the `‖Φ1‖²` factor (aligning `Φ1`) and the
> `‖Φ2‖²` factor (aligning `Φ2`, via the gauge-commuting swap), then using that `‖Φ1‖²` and `‖Φ2‖²`
> are coprime in the Gram ring.

```lean
lemma exists_polynomial_on_repHiggs {V : EffectivePotential} {n : ℕ}
    (hI : IsInvariant V) (h : HasMaxMassDimLE V n) :
    ∃ p : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ,
      ∀ X : Fin 4 → ℝ, V (repHiggs X) = p.eval (repHiggs X).gramVector
```

**`TwoHiggsDoublet.EffectivePotential.effectivePotential_is_polynomial_gramVector`**, a lemma, [line 997](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean#L997).

> **The two Higgs doublet potential in the bilinear formalism.** A gauge-invariant polynomial
> effective potential of maximum mass dimension `n` is a polynomial in the four gauge-invariant
> bilinears — the entries of the Gram vector.

```lean
lemma effectivePotential_is_polynomial_gramVector {V : EffectivePotential} {n : ℕ}
    (hI: IsInvariant V) (h : HasMaxMassDimLE V n) :
    ∃ p : MvPolynomial (Fin 1 ⊕ Fin 3) ℝ, (∀ φ : TwoHiggsDoublet, V φ = p.eval φ.gramVector)
```

## Depends on

- [The effective potential of the two Higgs doublet model](twohdm-effectivepotential.md)
- [The gauge slice and the hypercharges of the doublet components](twohdm-gaugeslice.md)

## Proof depends on

- [Charge balancing for polynomials](twohdm-chargebalance.md)
- [Swapping the two Higgs doublets](twohdm-swapdoublet.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Invariants.lean)
