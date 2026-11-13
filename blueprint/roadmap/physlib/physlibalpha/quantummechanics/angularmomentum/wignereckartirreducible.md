---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.standard_bracket_eSub, PhyslibAlpha.Sl2.standard_bracket_fSub, PhyslibAlpha.Sl2.standard_bracket_hSub, PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv, PhyslibAlpha.Sl2.AngularMomentumRepresentation.exists_isStandardEquiv, PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.pos, PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.symm_ρE, PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.symm_ρF
statement: formalized
proof: formalized
---

# The Wigner–Eckart theorem for irreducible angular momentum representations

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.WignerEckartIrreducible`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean): 17 declarations, 8 with a docstring.

> Tensor operators between arbitrary finite-dimensional irreducible angular momentum
> representations.

## i. Overview

> `AngularMomentumRepresentation` packages operators `Jx, Jy, Jz` on a complex vector space with
> the angular momentum commutation relations. By `spin_classification`, a finite-dimensional
> irreducible representation with `Jz ≠ 0` is isomorphic to a standard module `V(n)` by a linear
> equivalence carrying `J₊`, `J₋` and `2Jz` to `e`, `f` and `h`; `n = 2j` is twice the spin.
>
> A tensor operator of rank `k` from `ρ₁` on `V` to `ρ₂` on `W` is a linear map
> `T : V(k) → Hom(V, W)` with `[J₊, T x] = T (e x)`, `[J₋, T x] = T (f x)` and
> `[2Jz, T x] = T (h x)`. Conjugating with the equivalences turns it into a tensor operator between
> standard modules, so the results for standard modules carry over:
>
> - two tensor operators of the same rank between the same irreducible representations are
>   proportional (the Wigner–Eckart theorem: a single reduced matrix element);
> - a nonzero tensor operator satisfies the triangle rule for the spins.
>
> The spin-0 representation (`Jz = 0`) is excluded throughout, since it does not generate a copy of
> `sl₂`.

## ii. Key results

> - `IsStandardEquiv` and `exists_isStandardEquiv` give the comparison with a standard module.
> - `IsTensorOperatorOf` is the predicate for tensor operators between representations.
> - `IsTensorOperatorOf.isTensorOperator_conjStd` transports a tensor operator to standard modules.
> - `IsTensorOperatorOf.exists_eq_smul_of_ne_zero` is the Wigner–Eckart theorem.
> - `IsTensorOperatorOf.triangleRule` is the triangle rule.

## iv. References

> - E. P. Wigner, *Group Theory and its Application to the Quantum Mechanics of Atomic Spectra*,
>   Academic Press (1959), chapter 21.

## A. Comparison with the standard modules

**`PhyslibAlpha.Sl2.standard_bracket_eSub`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L76).

```lean
lemma standard_bracket_eSub (t : IsSl2Triple h e f) (w : StandardSl2Module K n) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    ⁅eSub (K := K) t, w⁆ = ρE w
```

**`PhyslibAlpha.Sl2.standard_bracket_fSub`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L83).

```lean
lemma standard_bracket_fSub (t : IsSl2Triple h e f) (w : StandardSl2Module K n) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    ⁅fSub (K := K) t, w⁆ = ρF w
```

**`PhyslibAlpha.Sl2.standard_bracket_hSub`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L90).

```lean
lemma standard_bracket_hSub (t : IsSl2Triple h e f) (w : StandardSl2Module K n) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    ⁅hSub (K := K) t, w⁆ = ρH w
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv`**, a structure, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L104).

> A linear equivalence `V ≃ V(n)` carrying `J₊`, `J₋` and `2Jz` to `e`, `f` and `h`.

```lean
structure IsStandardEquiv (ρ : AngularMomentumRepresentation V) {n : ℕ}
    (ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n) : Prop where
  map_Jp : ∀ v, ψ (ρ.Jp v) = ρE (ψ v)
  map_Jm : ∀ v, ψ (ρ.Jm v) = ρF (ψ v)
  map_Jz : ∀ v, ψ (((2 : ℂ) • ρ.Jz) v) = ρH (ψ v)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.exists_isStandardEquiv`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L112).

> A finite-dimensional irreducible representation with `Jz ≠ 0` is isomorphic to a standard
> module by a standard equivalence.

```lean
lemma exists_isStandardEquiv [FiniteDimensional ℂ V] (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz ≠ 0) (hirr : ρ.IsIrreducible) :
    ∃ (n : ℕ) (ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n), ρ.IsStandardEquiv ψ
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.pos`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L142).

> A standard equivalence for a representation with `Jz ≠ 0` lands in some `V(n)` with
> `n > 0`.

```lean
lemma IsStandardEquiv.pos {ρ : AngularMomentumRepresentation V} {n : ℕ}
    {ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n} (hψ : ρ.IsStandardEquiv ψ) (hz : ρ.Jz ≠ 0) : 0 < n
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.symm_ρE`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L159).

```lean
lemma IsStandardEquiv.symm_ρE {ρ : AngularMomentumRepresentation V} {n : ℕ}
    {ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n} (hψ : ρ.IsStandardEquiv ψ) (y : StandardSl2Module ℂ n) :
    ψ.symm (ρE y) = ρ.Jp (ψ.symm y)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.symm_ρF`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L164).

```lean
lemma IsStandardEquiv.symm_ρF {ρ : AngularMomentumRepresentation V} {n : ℕ}
    {ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n} (hψ : ρ.IsStandardEquiv ψ) (y : StandardSl2Module ℂ n) :
    ψ.symm (ρF y) = ρ.Jm (ψ.symm y)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsStandardEquiv.symm_ρH`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L169).

```lean
lemma IsStandardEquiv.symm_ρH {ρ : AngularMomentumRepresentation V} {n : ℕ}
    {ψ : V ≃ₗ[ℂ] StandardSl2Module ℂ n} (hψ : ρ.IsStandardEquiv ψ) (y : StandardSl2Module ℂ n) :
    ψ.symm (ρH y) = ((2 : ℂ) • ρ.Jz) (ψ.symm y)
```

## B. Tensor operators between representations

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsTensorOperatorOf`**, a structure, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L185).

> A tensor operator of rank `k` from `ρ₁` on `V` to `ρ₂` on `W`: a linear map
> `T : V(k) → Hom(V, W)` with `[J₊, T x] = T (e x)`, `[J₋, T x] = T (f x)` and
> `[2Jz, T x] = T (h x)`.

```lean
structure IsTensorOperatorOf (ρ₁ : AngularMomentumRepresentation V)
    (ρ₂ : AngularMomentumRepresentation W) (T : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W) :
    Prop where
  comm_p : ∀ x, ρ₂.Jp ∘ₗ T x - T x ∘ₗ ρ₁.Jp = T (ρE x)
  comm_m : ∀ x, ρ₂.Jm ∘ₗ T x - T x ∘ₗ ρ₁.Jm = T (ρF x)
  comm_z : ∀ x, ((2 : ℂ) • ρ₂.Jz) ∘ₗ T x - T x ∘ₗ ((2 : ℂ) • ρ₁.Jz) = T (ρH x)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.conjStd`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L193).

> Conjugation of an operator-valued map by linear equivalences `V ≃ V(n₁)` and `W ≃ V(n₂)`.

```lean
def conjStd {n₁ n₂ : ℕ} (ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁)
    (ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂) (T : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W) :
    StandardSl2Module ℂ k →ₗ[ℂ] StandardSl2Module ℂ n₁ →ₗ[ℂ] StandardSl2Module ℂ n₂
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.conjStd_apply`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L198).

```lean
lemma conjStd_apply {n₁ n₂ : ℕ} (ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁)
    (ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂) (T : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W)
    (x : StandardSl2Module ℂ k) (y : StandardSl2Module ℂ n₁) :
    conjStd ψ₁ ψ₂ T x y = ψ₂ (T x (ψ₁.symm y))
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.conjStd_injective`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L203).

```lean
lemma conjStd_injective {n₁ n₂ : ℕ} (ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁)
    (ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂) {T S : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W}
    (h : conjStd ψ₁ ψ₂ T = conjStd ψ₁ ψ₂ S) : T = S
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsTensorOperatorOf.isTensorOperator_conjStd`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L213).

> Conjugation by standard equivalences turns a tensor operator between representations into a
> tensor operator between standard modules.

```lean
lemma IsTensorOperatorOf.isTensorOperator_conjStd {ρ₁ : AngularMomentumRepresentation V}
    {ρ₂ : AngularMomentumRepresentation W} {T : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W}
    (hT : IsTensorOperatorOf ρ₁ ρ₂ T) {n₁ n₂ : ℕ} {ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁}
    {ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂} (h₁ : ρ₁.IsStandardEquiv ψ₁)
    (h₂ : ρ₂.IsStandardEquiv ψ₂) : IsTensorOperator (conjStd ψ₁ ψ₂ T)
```

## C. The Wigner–Eckart theorem

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsTensorOperatorOf.conjStd_zero`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L241).

```lean
lemma conjStd_zero {n₁ n₂ : ℕ} (ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁)
    (ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂) :
    conjStd ψ₁ ψ₂ (0 : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W) = 0
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsTensorOperatorOf.triangleRule`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L249).

> **Triangle rule** for irreducible representations: a nonzero tensor operator of rank `k`
> from `ρ₁ ≅ V(n₁)` to `ρ₂ ≅ V(n₂)` satisfies `TriangleRule k n₁ n₂`, i.e. `|j₁ - j₂| ≤ κ ≤ j₁ + j₂`
> for `k = 2κ`, `n₁ = 2j₁`, `n₂ = 2j₂`.

```lean
lemma triangleRule (h₁z : ρ₁.Jz ≠ 0) {T : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W}
    (hT : IsTensorOperatorOf ρ₁ ρ₂ T) (hT0 : T ≠ 0) {n₁ n₂ : ℕ}
    {ψ₁ : V ≃ₗ[ℂ] StandardSl2Module ℂ n₁} {ψ₂ : W ≃ₗ[ℂ] StandardSl2Module ℂ n₂}
    (hψ₁ : ρ₁.IsStandardEquiv ψ₁) (hψ₂ : ρ₂.IsStandardEquiv ψ₂) : TriangleRule k n₁ n₂
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsTensorOperatorOf.exists_eq_smul_of_ne_zero`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean#L263).

> **Wigner–Eckart theorem** for irreducible representations: two tensor operators of the same
> rank between the same irreducible representations are proportional, provided the second is
> nonzero.

```lean
lemma exists_eq_smul_of_ne_zero (h₁z : ρ₁.Jz ≠ 0) (h₁ : ρ₁.IsIrreducible) (h₂z : ρ₂.Jz ≠ 0)
    (h₂ : ρ₂.IsIrreducible) {T S : StandardSl2Module ℂ k →ₗ[ℂ] V →ₗ[ℂ] W}
    (hT : IsTensorOperatorOf ρ₁ ρ₂ T) (hS : IsTensorOperatorOf ρ₁ ρ₂ S) (hS0 : S ≠ 0) :
    ∃ c : ℂ, T = c • S
```

## Depends on

- [Abstract angular momentum representations](basic.md)
- [Selection rules for multipole transitions](selectionrules.md)

## Proof depends on

- [The projection theorem for vector operators](projectiontheorem.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartIrreducible.lean)
