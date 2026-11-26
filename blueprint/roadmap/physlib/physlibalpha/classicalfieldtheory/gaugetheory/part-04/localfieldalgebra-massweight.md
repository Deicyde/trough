---
declaration: module
origin: cited
lean: GaugeFieldData.massWeightAssignment, GaugeFieldData.massWeightScale, GaugeFieldData.massWeightScale_ιFermion, GaugeFieldData.massWeightScale_ιBoson, GaugeFieldData.massWeightScale_ιConnection, GaugeFieldData.instRingPolynomialLocalFieldAlgebra, GaugeFieldData.monomialₗ, GaugeFieldData.halfPoly
statement: formalized
proof: formalized
---

# The mass-weight filtration and the invariants of a local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.MassWeight`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean): 68 declarations, 51 with a docstring.

> The grading of the local field algebra by mass weight, and its gauge and Lorentz invariants of
> bounded mass weight.

## i. Overview

> The local field algebra of a field datum is graded by mass weight: a generator `∂_s φ_α`
> of a field of mass weight `w` has weight `w + 2 |s|`, a connection generator `∂_s A_μ` has
> weight `2 + 2 |s|`. The grading is recorded by the algebra endomorphisms scaling each
> generator by `c` to its weight, for real `c`.
>
> The same grading is also recorded with the scalar replaced by a formal variable. The
> mass-weight polynomial is the algebra map into the polynomials over the local field algebra
> sending a generator of weight `n` to `X ^ n` times itself. It is built from the universal
> property of the local field algebra. The polynomials over a noncommutative algebra are
> noncommutative, so the statistics of the images have to be checked, and they follow from
> those of the coefficients. The weight-`n` piece is the eigenspace on which the mass-weight
> polynomial is `X ^ n`, and the filtration is the join of the pieces of weight at most `w`.
> Setting the formal variable to a real number `c` gives back the scaling by `c`, so the
> weight-`n` piece is also the set of elements scaled by `c ^ n` for every `c`.
>
> Together with the actions of the jet gauge group and of the Lorentz group this gives the
> submodule of gauge and Lorentz invariants of mass weight at most `w`, which is what a
> Lagrangian classification describes. Everything here is generic: a model contributes only
> its datum.

## ii. Key results

> - `GaugeFieldData.massWeightScale` : the scaling of the local field algebra by `c` to the
>   mass weight of each generator.
> - `GaugeFieldData.massWeightPoly` : the mass-weight polynomial, sending a generator of
>   weight `n` to `X ^ n` times itself.
> - `GaugeFieldData.massWeightPoly_fermionSymbol`, `massWeightPoly_bosonSymbol` and their
>   conjugates : the symbols `∂_s ψ` of a species of mass weight `w` have weight `w + 2 |s|`.
> - `GaugeFieldData.massWeightPoly_gaugeField` : the gauge-field symbols `∂_s A_μ`
>   have weight `2 (1 + |s|)`.
> - `GaugeFieldData.massWeightScale_eq_polyEval_comp_massWeightPoly` : the scaling by `c` is
>   the mass-weight polynomial evaluated at `c`.
> - `GaugeFieldData.massWeightSubmodule`, `massWeightSubmoduleLE` : the graded pieces and
>   the filtration.
> - `GaugeFieldData.mem_massWeightSubmodule_iff_massWeightScale` : the weight-`n` piece is the
>   set of elements scaled by `c ^ n` under the scaling by every real `c`.
> - `GaugeFieldData.gaugeInvariants`, `lorentzInvariants`, `invariantsLE` : the invariants,
>   and the invariants of mass weight at most `w`.
> - `GaugeFieldData.bosonNormSq` : the contraction `φ† φ` of a bosonic species with its
>   conjugate through a basis of its value space, the simplest invariant.
> - `GaugeFieldData.invariantsLE_map` : an isomorphism of local field algebras respecting the
>   actions and the mass-weight polynomial carries the invariants of one datum onto those of the
>   other.

## iv. References

> * None.

## A. The mass-weight scaling

**`GaugeFieldData.massWeightAssignment`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L102).

> The assignment scaling each generator by `c` to its mass weight. A component function
> `∂_s φ_α` of a species of mass weight `w` by `c ^ (w + 2 |s|)`, a connection generator
> `∂_s A_μ` by `c ^ (2 + 2 |s|)`. The relations hold because the images are generators of
> the same kind.

```lean
noncomputable def massWeightAssignment (c : ℝ) : T.Assignment T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightScale`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L116).

> The mass-weight scaling of the local field algebra, the algebra endomorphism
> scaling each generator by `c` to its mass weight.

```lean
noncomputable def massWeightScale (c : ℝ) : T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightScale_ιFermion`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L120).

```lean
lemma massWeightScale_ιFermion (c : ℝ) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.massWeightScale c (T.ιFermion i x)
      = T.ιFermion i (FieldDerivSpace.massWeightScale (T.fermion i).massWeight (c : ℂ) x)
```

**`GaugeFieldData.massWeightScale_ιBoson`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L127).

```lean
lemma massWeightScale_ιBoson (c : ℝ) (j : T.BosonSpecies)
    (y : FieldDerivSpace (T.boson j)) :
    T.massWeightScale c (T.ιBoson j y)
      = T.ιBoson j (FieldDerivSpace.massWeightScale (T.boson j).massWeight (c : ℂ) y)
```

**`GaugeFieldData.massWeightScale_ιConnection`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L134).

```lean
lemma massWeightScale_ιConnection (c : ℝ) (v : GaugeBoson.FieldDerivSpace G) :
    T.massWeightScale c (T.ιConnection v)
      = T.ιConnection (GaugeBoson.FieldDerivSpace.massWeightScale G c v)
```

## B. The mass-weight polynomial

> Replacing the scalar `c` of the scaling by a formal variable `X` turns the scaling into a
> grading. The image of a generator is a polynomial over the local field algebra whose
> coefficients are generators of the same species, so the relations among the generators hold
> for their images coefficient by coefficient. That is what makes the images a compatible
> assignment, and the grading the algebra map it induces.

### B.1. The grading of a component function

**`GaugeFieldData.instRingPolynomialLocalFieldAlgebra`**, an instance, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L160).

> The polynomials over the local field algebra form a ring. The instance is recorded here
> so that it is found directly, without searching through the tensor-product structure of
> the local field algebra once more.

```lean
noncomputable instance instRingPolynomialLocalFieldAlgebra :
    Ring (Polynomial T.LocalFieldAlgebra)
```

**`GaugeFieldData.monomialₗ`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L166).

> The monomial of degree `n` over the local field algebra, as a map of complex vector
> spaces rather than of modules over the local field algebra.

```lean
noncomputable def monomialₗ (n : ℕ) :
    T.LocalFieldAlgebra →ₗ[ℂ] Polynomial T.LocalFieldAlgebra
```

**`GaugeFieldData.halfPoly`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L173).

> One half of the grading of a component space, for a species of mass weight `w`. It
> sends the symbol `∂_s φ` to `X ^ (w + 2 |s|)` times its image under `k`, and is defined on
> the multiset basis of the derivative labels.

```lean
noncomputable def halfPoly {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] T.LocalFieldAlgebra) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] Polynomial T.LocalFieldAlgebra
```

**`GaugeFieldData.monomialₗ_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L183).

```lean
lemma monomialₗ_apply (n : ℕ) (x : T.LocalFieldAlgebra) :
    T.monomialₗ n x = Polynomial.monomial n x
```

**`GaugeFieldData.halfPoly_basis_tmul`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L188).

> On the symbol `∂_s φ` the half grading is the monomial of degree `w + 2 |s|`, since the
> field contributes `w` and each derivative two.

```lean
lemma halfPoly_basis_tmul {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] T.LocalFieldAlgebra)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (x : W) :
    T.halfPoly w k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x))
```

**`GaugeFieldData.halfPoly_coeff_mem`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L200).

> Every coefficient of the half grading lies in the range of `k`. The derivative monomials
> span the derivative labels, and on each of them the half grading is a single monomial
> whose coefficient is in the range.

```lean
lemma halfPoly_coeff_mem {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] T.LocalFieldAlgebra)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W) (n : ℕ) :
    (T.halfPoly w k z).coeff n ∈ LinearMap.range k
```

### B.2. The images of the generators

> The image of a matter generator is the sum of the two half gradings of its component
> space, at the mass weight of its species, with the symbol maps of the species as the maps
> `k`. The image of a connection generator is the grading of the complexified gauge-boson
> algebra, pushed into the local field algebra coefficient by coefficient.

**`GaugeFieldData.fermionPoly`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L244).

> The grading of the component space of a fermionic species, the half gradings of the
> symbols and of the conjugate symbols, at the mass weight of the species.

```lean
noncomputable def fermionPoly (i : T.FermionSpecies) :
    FieldDerivSpace (T.fermion i) →ₗ[ℂ] Polynomial T.LocalFieldAlgebra
```

**`GaugeFieldData.bosonPoly`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L252).

> The grading of the component space of a bosonic species, the half gradings of the
> symbols and of the conjugate symbols, at the mass weight of the species.

```lean
noncomputable def bosonPoly (j : T.BosonSpecies) :
    FieldDerivSpace (T.boson j) →ₗ[ℂ] Polynomial T.LocalFieldAlgebra
```

**`GaugeFieldData.connectionOfAlgHom`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L260).

> An algebra map out of the complexified connection factor, read on the connection
> generators, `v ↦ h (1 ⊗ v)`. It is stated for an arbitrary complex algebra `C`, so that
> the real structure of `C` is the one the generator assignments use.

```lean
noncomputable def connectionOfAlgHom {C : Type*} [Ring C] [Algebra ℂ C]
    (h : (ℂ ⊗[ℝ] SymmetricAlgebra ℝ (GaugeBoson.FieldDerivSpace G)) →ₐ[ℂ] C) :
    GaugeBoson.FieldDerivSpace G →ₗ[ℝ] C
```

**`GaugeFieldData.connectionPoly`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L273).

> The grading of the connection generators, a real-linear map from
> `GaugeBoson.FieldDerivSpace G` to `Polynomial T.LocalFieldAlgebra`, the grading of the
> complexified gauge-boson algebra, pushed into the local field algebra coefficient by
> coefficient. Its type is left to be inferred, so that the real structure on the
> polynomials is the one `connectionOfAlgHom` and the generator assignments use.

```lean
noncomputable def connectionPoly
```

**`GaugeFieldData.fermionPoly_apply`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L280).

```lean
lemma fermionPoly_apply (i : T.FermionSpecies) (x : FieldDerivSpace (T.fermion i)) :
    T.fermionPoly i x = T.halfPoly (T.fermion i).massWeight (T.fermionSymbolMap i) x.1
      + T.halfPoly (T.fermion i).massWeight (T.conjFermionSymbolMap i) x.2
```

**`GaugeFieldData.bosonPoly_apply`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L284).

```lean
lemma bosonPoly_apply (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j)) :
    T.bosonPoly j y = T.halfPoly (T.boson j).massWeight (T.bosonSymbolMap j) y.1
      + T.halfPoly (T.boson j).massWeight (T.conjBosonSymbolMap j) y.2
```

**`GaugeFieldData.connectionPoly_apply`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L288).

```lean
lemma connectionPoly_apply (v : GaugeBoson.FieldDerivSpace G) :
    T.connectionPoly v = Polynomial.mapAlgHom T.includeConnection
      (LocalGaugeFieldAlgebra.complexMassWeightPoly (G := G)
        ((1 : ℂ) ⊗ₜ[ℝ] SymmetricAlgebra.ι ℝ (GaugeBoson.FieldDerivSpace G) v))
```

**`GaugeFieldData.fermionPoly_inl`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L295).

> On an unconjugated symbol `∂_s ψ^φ` of a fermionic species of mass weight `w` the
> grading is the monomial of degree `w + 2 |s|`.

```lean
lemma fermionPoly_inl (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.fermionPoly i (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
      = Polynomial.monomial ((T.fermion i).massWeight + 2 * Multiset.card s)
          (T.fermionSymbol i s φ)
```

**`GaugeFieldData.fermionPoly_inr`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L304).

> On a conjugate symbol `∂_s ψ̄^φ` the grading is the monomial of the same degree.

```lean
lemma fermionPoly_inr (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.fermionPoly i (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
      = Polynomial.monomial ((T.fermion i).massWeight + 2 * Multiset.card s)
          (T.conjFermionSymbol i s φ)
```

**`GaugeFieldData.bosonPoly_inl`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L314).

> On an unconjugated symbol `∂_s φ^χ` of a bosonic species of mass weight `w` the
> grading is the monomial of degree `w + 2 |s|`.

```lean
lemma bosonPoly_inl (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.bosonPoly j (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
      = Polynomial.monomial ((T.boson j).massWeight + 2 * Multiset.card s)
          (T.bosonSymbol j s φ)
```

**`GaugeFieldData.bosonPoly_inr`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L323).

> On a conjugate symbol `∂_s φ̄^χ` the grading is the monomial of the same degree.

```lean
lemma bosonPoly_inr (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.bosonPoly j (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
      = Polynomial.monomial ((T.boson j).massWeight + 2 * Multiset.card s)
          (T.conjBosonSymbol j s φ)
```

**`GaugeFieldData.fermionPoly_coeff_mem`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L333).

> Every coefficient of the image of a fermionic generator is a generator of the same
> species.

```lean
lemma fermionPoly_coeff_mem (i : T.FermionSpecies) (x : FieldDerivSpace (T.fermion i))
    (n : ℕ) : (T.fermionPoly i x).coeff n ∈ LinearMap.range (T.ιFermion i)
```

**`GaugeFieldData.bosonPoly_coeff_mem`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L344).

> Every coefficient of the image of a bosonic generator is a generator of the same
> species.

```lean
lemma bosonPoly_coeff_mem (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j))
    (n : ℕ) : (T.bosonPoly j y).coeff n ∈ LinearMap.range (T.ιBoson j)
```

**`GaugeFieldData.fermionPoly_mul_swap`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L355).

> The images of two fermionic generators anticommute, because their coefficients are
> fermionic generators.

```lean
lemma fermionPoly_mul_swap (i j : T.FermionSpecies) (x : FieldDerivSpace (T.fermion i))
    (y : FieldDerivSpace (T.fermion j)) :
    T.fermionPoly i x * T.fermionPoly j y = -(T.fermionPoly j y * T.fermionPoly i x)
```

**`GaugeFieldData.commute_bosonPoly`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L365).

> The image of a bosonic generator is central, because its coefficients are.

```lean
lemma commute_bosonPoly (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j))
    (q : Polynomial T.LocalFieldAlgebra) : Commute (T.bosonPoly j y) q
```

**`GaugeFieldData.commute_mapAlgHom_includeConnection`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L374).

> A polynomial with coefficients in the connection factor is central, because the
> connection factor is.

```lean
lemma commute_mapAlgHom_includeConnection
    (p : Polynomial (ℂ ⊗[ℝ] SymmetricAlgebra ℝ (GaugeBoson.FieldDerivSpace G)))
    (q : Polynomial T.LocalFieldAlgebra) :
    Commute (Polynomial.mapAlgHom T.includeConnection p) q
```

**`GaugeFieldData.commute_connectionPoly`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L383).

> The image of a connection generator is central.

```lean
lemma commute_connectionPoly (v : GaugeBoson.FieldDerivSpace G)
    (q : Polynomial T.LocalFieldAlgebra) : Commute (T.connectionPoly v) q
```

### B.3. The mass-weight polynomial and its generators

**`GaugeFieldData.massWeightPolyAssignment`**, a def, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L399).

> The grading of the generators as a compatible assignment in the polynomials over the
> local field algebra. The fermionic images anticommute and the bosonic and connection
> images are central, because their coefficients do and are.

```lean
noncomputable def massWeightPolyAssignment :
    T.Assignment (Polynomial T.LocalFieldAlgebra)
```

**`GaugeFieldData.massWeightPoly`**, a def, [line 420](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L420).

> The mass-weight polynomial of the local field algebra, the algebra map sending a
> generator of mass weight `n` to `X ^ n` times itself, so that the coefficient of `X ^ n`
> in the image of an element is its part of mass weight `n`.

```lean
noncomputable def massWeightPoly : T.LocalFieldAlgebra →ₐ[ℂ] Polynomial T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightPoly_ιFermion`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L426).

```lean
lemma massWeightPoly_ιFermion (i : T.FermionSpecies) (x : FieldDerivSpace (T.fermion i)) :
    T.massWeightPoly (T.ιFermion i x) = T.fermionPoly i x
```

**`GaugeFieldData.massWeightPoly_ιBoson`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L431).

```lean
lemma massWeightPoly_ιBoson (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j)) :
    T.massWeightPoly (T.ιBoson j y) = T.bosonPoly j y
```

**`GaugeFieldData.massWeightPoly_ιConnection`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L436).

```lean
lemma massWeightPoly_ιConnection (v : GaugeBoson.FieldDerivSpace G) :
    T.massWeightPoly (T.ιConnection v) = T.connectionPoly v
```

**`GaugeFieldData.massWeightPoly_fermionSymbol`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L442).

> The symbol `∂_s ψ^φ` of a fermionic species of mass weight `w` has weight
> `w + 2 |s|`.

```lean
lemma massWeightPoly_fermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.massWeightPoly (T.fermionSymbol i s φ)
      = Polynomial.monomial ((T.fermion i).massWeight + 2 * Multiset.card s)
          (T.fermionSymbol i s φ)
```

**`GaugeFieldData.massWeightPoly_conjFermionSymbol`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L451).

> The conjugate symbol `∂_s ψ̄^φ` has the same weight `w + 2 |s|`.

```lean
lemma massWeightPoly_conjFermionSymbol (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.massWeightPoly (T.conjFermionSymbol i s φ)
      = Polynomial.monomial ((T.fermion i).massWeight + 2 * Multiset.card s)
          (T.conjFermionSymbol i s φ)
```

**`GaugeFieldData.massWeightPoly_bosonSymbol`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L460).

> The symbol `∂_s φ^χ` of a bosonic species of mass weight `w` has weight `w + 2 |s|`.

```lean
lemma massWeightPoly_bosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.massWeightPoly (T.bosonSymbol j s φ)
      = Polynomial.monomial ((T.boson j).massWeight + 2 * Multiset.card s)
          (T.bosonSymbol j s φ)
```

**`GaugeFieldData.massWeightPoly_conjBosonSymbol`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L469).

> The conjugate symbol `∂_s φ̄^χ` has the same weight `w + 2 |s|`.

```lean
lemma massWeightPoly_conjBosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.massWeightPoly (T.conjBosonSymbol j s φ)
      = Polynomial.monomial ((T.boson j).massWeight + 2 * Multiset.card s)
          (T.conjBosonSymbol j s φ)
```

**`GaugeFieldData.massWeightPoly_gaugeField`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L480).

> The gauge-field symbol `∂_s A_μ^φ` has mass weight `2 (1 + |s|)`, since the gauge field has
> mass dimension one and each derivative adds one more. This is the form of the hypothesis
> that the mass weights of the covariant towers take.

```lean
lemma massWeightPoly_gaugeField (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.massWeightPoly (T.gaugeField s μ φ)
      = Polynomial.monomial (2 * (1 + Multiset.card s)) (T.gaugeField s μ φ)
```

### B.4. Evaluation at a real number

> Setting the formal variable of the mass-weight polynomial to a real number `c` gives back the
> mass-weight scaling by `c`. The scalar `c` is central, so evaluation at it is an algebra map,
> and it is enough to compare the two algebra maps on the generators.

**`GaugeFieldData.polyEval`**, a def, [line 515](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L515).

> Evaluation of a polynomial over the local field algebra at a real number `c`. It is an
> algebra map because `c` is central.

```lean
noncomputable def polyEval (c : ℝ) :
    Polynomial T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.polyEval_monomial`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L521).

> Evaluating the monomial `x X ^ n` at `c` gives `c ^ n x`.

```lean
lemma polyEval_monomial (c : ℝ) (n : ℕ) (x : T.LocalFieldAlgebra) :
    T.polyEval c (Polynomial.monomial n x) = ((c : ℂ) ^ n) • x
```

**`GaugeFieldData.polyEval_eq_sum`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L529).

> Evaluation at `c` as a sum over the coefficients.

```lean
lemma polyEval_eq_sum (c : ℝ) (q : Polynomial T.LocalFieldAlgebra) :
    T.polyEval c q = ∑ m ∈ Finset.range (q.natDegree + 1), ((c : ℂ) ^ m) • q.coeff m
```

**`GaugeFieldData.eq_zero_of_forall_polyEval_eq_zero`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L537).

> A polynomial over the local field algebra vanishing at every real number is zero, its
> coefficients being those of an identically vanishing polynomial function.

```lean
lemma eq_zero_of_forall_polyEval_eq_zero {q : Polynomial T.LocalFieldAlgebra}
    (h : ∀ c : ℝ, T.polyEval c q = 0) : q = 0
```

**`GaugeFieldData.polyEval_halfPoly`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L550).

> The half grading evaluated at `c` is the mass-weight scaling of the half component space,
> `c ^ w` times the derivative-degree scaling by `c ^ 2`.

```lean
lemma polyEval_halfPoly (c : ℝ) {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] T.LocalFieldAlgebra)
    (z : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W) :
    T.polyEval c (T.halfPoly w k z) = ((c : ℂ) ^ w) • k (TensorProduct.map
      (SpaceTimeDerivAlgebraℂ.gradeScale ((c : ℂ) ^ 2)).toLinearMap LinearMap.id z)
```

**`GaugeFieldData.polyEval_fermionPoly`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L569).

> The image of a fermionic generator evaluated at `c` is its mass-weight scaling by `c`.

```lean
lemma polyEval_fermionPoly (c : ℝ) (i : T.FermionSpecies) (x : FieldDerivSpace (T.fermion i)) :
    T.polyEval c (T.fermionPoly i x)
      = T.ιFermion i (FieldDerivSpace.massWeightScale (T.fermion i).massWeight (c : ℂ) x)
```

**`GaugeFieldData.polyEval_bosonPoly`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L581).

> The image of a bosonic generator evaluated at `c` is its mass-weight scaling by `c`.

```lean
lemma polyEval_bosonPoly (c : ℝ) (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j)) :
    T.polyEval c (T.bosonPoly j y)
      = T.ιBoson j (FieldDerivSpace.massWeightScale (T.boson j).massWeight (c : ℂ) y)
```

**`GaugeFieldData.polyEval_connectionPoly`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L595).

> The image of a connection generator evaluated at `c` is its mass-weight scaling by `c`.
> The evaluation is pushed through the inclusion of the connection factor, where it is the
> evaluation of the gauge-boson grading.

```lean
lemma polyEval_connectionPoly (c : ℝ) (v : GaugeBoson.FieldDerivSpace G) :
    T.polyEval c (T.connectionPoly v)
      = T.ιConnection (GaugeBoson.FieldDerivSpace.massWeightScale G c v)
```

**`GaugeFieldData.massWeightScale_eq_polyEval_comp_massWeightPoly`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L614).

> The mass-weight scaling by `c` is the mass-weight polynomial evaluated at `c`, since both are
> algebra maps, and they agree on the generators.

```lean
lemma massWeightScale_eq_polyEval_comp_massWeightPoly (c : ℝ) :
    T.massWeightScale c = (T.polyEval c).comp T.massWeightPoly
```

**`GaugeFieldData.massWeightScale_apply`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L626).

```lean
lemma massWeightScale_apply (c : ℝ) (x : T.LocalFieldAlgebra) :
    T.massWeightScale c x = T.polyEval c (T.massWeightPoly x)
```

## C. The graded pieces and the filtration

**`GaugeFieldData.massWeightSubmodule`**, a def, [line 640](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L640).

> The weight-`n` piece of the local field algebra, the eigenspace on which the
> mass-weight polynomial is the monomial `X ^ n`.

```lean
noncomputable def massWeightSubmodule (n : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_massWeightSubmodule`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L656).

> Membership of the weight-`n` piece is the eigenvalue equation.

```lean
lemma mem_massWeightSubmodule {n : ℕ} {x : T.LocalFieldAlgebra} :
    x ∈ T.massWeightSubmodule n ↔ T.massWeightPoly x = Polynomial.monomial n x
```

**`GaugeFieldData.massWeightScale_of_mem_massWeightSubmodule`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L661).

> The mass-weight scaling by `c` multiplies the weight-`n` piece by `c ^ n`.

```lean
lemma massWeightScale_of_mem_massWeightSubmodule {n : ℕ} {x : T.LocalFieldAlgebra}
    (hx : x ∈ T.massWeightSubmodule n) (c : ℝ) :
    T.massWeightScale c x = ((c : ℂ) ^ n) • x
```

**`GaugeFieldData.mem_massWeightSubmodule_iff_massWeightScale`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L670).

> The weight-`n` piece is the set of elements scaled by `c ^ n` under the mass-weight
> scaling by every real `c`. Conversely to the eigenvalue equation, the difference of the two
> sides of it is a polynomial vanishing at every real number.

```lean
lemma mem_massWeightSubmodule_iff_massWeightScale {n : ℕ} {x : T.LocalFieldAlgebra} :
    x ∈ T.massWeightSubmodule n ↔ ∀ c : ℝ, T.massWeightScale c x = ((c : ℂ) ^ n) • x
```

**`GaugeFieldData.massWeightSubmoduleLE`**, a def, [line 680](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L680).

> The mass-weight filtration, the join of the pieces of weight at most `w`. An element
> lies in it exactly when it is a sum of eigenvectors of the mass-weight polynomial of weight at
> most `w`.

```lean
noncomputable def massWeightSubmoduleLE (w : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightSubmodule_le_massWeightSubmoduleLE`**, a lemma, [line 683](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L683).

```lean
lemma massWeightSubmodule_le_massWeightSubmoduleLE {k w : ℕ} (h : k ≤ w) :
    T.massWeightSubmodule k ≤ T.massWeightSubmoduleLE w
```

**`GaugeFieldData.coeff_massWeightPoly_eq_zero_of_mem_massWeightSubmoduleLE`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L690).

> An element of the filtration up to weight `w` has no component above `w`, so the
> coefficient of `X ^ n` in its image under the mass-weight polynomial vanishes for `n > w`.

```lean
lemma coeff_massWeightPoly_eq_zero_of_mem_massWeightSubmoduleLE {w n : ℕ} (hn : w < n)
    {x : T.LocalFieldAlgebra} (hx : x ∈ T.massWeightSubmoduleLE w) :
    (T.massWeightPoly x).coeff n = 0
```

## D. The invariants

**`GaugeFieldData.gaugeInvariants`**, a def, [line 715](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L715).

> The gauge invariants, the elements fixed by every jet of gauge transformations.

```lean
noncomputable def gaugeInvariants : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_gaugeInvariants_iff`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L719).

```lean
lemma mem_gaugeInvariants_iff {x : T.LocalFieldAlgebra} :
    x ∈ T.gaugeInvariants ↔ ∀ U : G.gaugeJetGroup, T.repJet U x = x
```

**`GaugeFieldData.lorentzInvariants`**, a def, [line 724](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L724).

> The Lorentz invariants, the elements fixed by every Lorentz transformation.

```lean
noncomputable def lorentzInvariants : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_lorentzInvariants_iff`**, a lemma, [line 728](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L728).

```lean
lemma mem_lorentzInvariants_iff {x : T.LocalFieldAlgebra} :
    x ∈ T.lorentzInvariants ↔ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x
```

**`GaugeFieldData.invariantsLE`**, a def, [line 734](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L734).

> The invariants of mass weight at most `w`, the gauge and Lorentz invariants in the
> filtration. A Lagrangian of mass dimension at most `w / 2` is an element of it.

```lean
noncomputable def invariantsLE (w : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_invariantsLE_iff`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L737).

```lean
lemma mem_invariantsLE_iff {w : ℕ} {x : T.LocalFieldAlgebra} :
    x ∈ T.invariantsLE w ↔ x ∈ T.massWeightSubmoduleLE w
      ∧ (∀ U : G.gaugeJetGroup, T.repJet U x = x) ∧ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x
```

## E. The contraction of a boson with its conjugate

**`GaugeFieldData.bosonNormSq`**, a def, [line 751](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L751).

> The contraction `φ† φ` of a bosonic species with its conjugate, through a basis of
> its value space, the sum over the basis of the conjugate coordinate times the coordinate.
> For a scalar in a unitary representation it is the mass term.

```lean
noncomputable def bosonNormSq (j : T.BosonSpecies) {ι : Type} [Fintype ι] [DecidableEq ι]
    (b : Module.Basis ι ℂ (T.BosonValue j)) : T.LocalFieldAlgebra
```

## F. Transport along an isomorphism

> An isomorphism of local field algebras intertwining the jet gauge action, the Lorentz
> action and the mass-weight polynomial carries the graded pieces, the filtration and the
> invariants of one datum onto those of the other. This is what relates two presentations
> of the same field content, such as a model's table and a hand-built datum.

**`GaugeFieldData.mem_massWeightSubmodule_apply_iff`**, a lemma, [line 772](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L772).

> The mass-weight polynomial is respected, so the weight-`n` piece is carried onto the
> weight-`n` piece.

```lean
lemma mem_massWeightSubmodule_apply_iff
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x))
    (n : ℕ) (x : T.LocalFieldAlgebra) :
    e x ∈ T'.massWeightSubmodule n ↔ x ∈ T.massWeightSubmodule n
```

**`GaugeFieldData.massWeightSubmodule_map`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L784).

```lean
lemma massWeightSubmodule_map
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x)) (n : ℕ) :
    (T.massWeightSubmodule n).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.massWeightSubmodule n
```

**`GaugeFieldData.massWeightSubmoduleLE_map`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L794).

```lean
lemma massWeightSubmoduleLE_map
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x)) (w : ℕ) :
    (T.massWeightSubmoduleLE w).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.massWeightSubmoduleLE w
```

**`GaugeFieldData.mem_massWeightSubmoduleLE_apply_iff`**, a lemma, [line 802](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L802).

> The filtration is respected, element by element.

```lean
lemma mem_massWeightSubmoduleLE_apply_iff
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x)) (w : ℕ)
    (x : T.LocalFieldAlgebra) :
    e x ∈ T'.massWeightSubmoduleLE w ↔ x ∈ T.massWeightSubmoduleLE w
```

**`GaugeFieldData.mem_invariantsLE_apply_iff`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L811).

> The invariants of mass weight at most `w` are respected, element by element.

```lean
lemma mem_invariantsLE_apply_iff
    (hjet : ∀ (U : G.gaugeJetGroup) x, e (T.repJet U x) = T'.repJet U (e x))
    (hlor : ∀ (Λ : SL(2,ℂ)) x, e (T.repLorentzGroup Λ x) = T'.repLorentzGroup Λ (e x))
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x)) (w : ℕ)
    (x : T.LocalFieldAlgebra) :
    e x ∈ T'.invariantsLE w ↔ x ∈ T.invariantsLE w
```

**`GaugeFieldData.invariantsLE_map`**, a lemma, [line 824](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean#L824).

> The invariants of mass weight at most `w` are carried onto the invariants of mass
> weight at most `w` by an isomorphism respecting the two actions and the mass-weight
> polynomial.

```lean
lemma invariantsLE_map (hjet : ∀ (U : G.gaugeJetGroup) x, e (T.repJet U x) = T'.repJet U (e x))
    (hlor : ∀ (Λ : SL(2,ℂ)) x, e (T.repLorentzGroup Λ x) = T'.repLorentzGroup Λ (e x))
    (hpoly : ∀ x, (T.massWeightPoly x).map (e : T.LocalFieldAlgebra →+* T'.LocalFieldAlgebra)
      = T'.massWeightPoly (e x)) (w : ℕ) :
    (T.invariantsLE w).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.invariantsLE w
```

## Depends on

- [The mass-weight polynomial on the gauge-boson jet algebra](../part-01/gaugeboson-localgaugefieldalgebra-massweightpoly.md)
- [The field symbols of the local field algebra and their transformation laws](localfieldalgebra-symbols.md)

## Proof depends on

- [Commuting and anticommuting polynomials](../../../mathematics/part-02/formathlib/algebra-polynomial-commute.md)
- [Vector-valued polynomial functions of a real variable](../../../mathematics/part-02/formathlib/algebra-polynomial-sumsmulpow.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/MassWeight.lean)
