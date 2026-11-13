---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.AngularMomentumRepresentation, PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jp, PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jm, PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_z_p, PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_z_m, PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_p_m, PhyslibAlpha.Sl2.AngularMomentumRepresentation.isSl2Triple, PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsIrreducible
statement: formalized
proof: formalized
---

# Abstract angular momentum representations

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.Basic`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean): 41 declarations, 31 with a docstring.

> Packages three endomorphisms obeying the angular momentum commutation relations and
> connects them to `sl₂`.

## i. Overview

> The commutation relations for three complex-linear angular momentum operators determine an
> `sl₂` triple with Cartan operator `2Jz` and raising and lowering operators `Jp` and `Jm`.
> This lets Mathlib’s primitive-vector theory classify finite-dimensional irreducible
> representations. The square `Jx² + Jy² + Jz²` commutes with the three operators and acts as
> `j(j+1)` on an irreducible representation of highest weight `2j`.

## ii. Key results

> - `AngularMomentumRepresentation` records the angular momentum commutators.
> - `isSl2Triple` identifies `2Jz`, `Jp`, and `Jm` with an `sl₂` triple.
> - `Jsq_eq_smul` gives the Casimir eigenvalue on an irreducible representation.
> - `magneticBasisVec` defines the lowering-string vectors; no basis theorem is asserted here.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Angular momentum and its `sl₂` triple

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation`**, a structure, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L58).

> Angular momentum representation. Three operators
> `Jx, Jy, Jz` on a state space `V`, satisfying the `so(3)` commutation relations
> `[Jx,Jy] = iJz` and cyclic permutations. (The physical requirement that they be
> self-adjoint on a Hilbert space is out of scope for this algebraic model.)

```lean
structure AngularMomentumRepresentation where
  /-- The first Cartesian component of angular momentum. -/
  Jx : Module.End ℂ V
  /-- The second Cartesian component of angular momentum. -/
  Jy : Module.End ℂ V
  /-- The third Cartesian component of angular momentum. -/
  Jz : Module.End ℂ V
  comm_xy : ⁅Jx, Jy⁆ = Complex.I • Jz
  comm_yz : ⁅Jy, Jz⁆ = Complex.I • Jx
  comm_zx : ⁅Jz, Jx⁆ = Complex.I • Jy
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jp`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L74).

> Ladder operators. `J± := Jx ± iJy`.

```lean
def Jp (ρ : AngularMomentumRepresentation V) : Module.End ℂ V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jm`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L77).

```lean
def Jm (ρ : AngularMomentumRepresentation V) : Module.End ℂ V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_z_p`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L81).

> Commutation relations for the ladder operators:
> `[Jz, J±] = ±J±` and `[J+, J-] = 2Jz`.

```lean
lemma comm_z_p (ρ : AngularMomentumRepresentation V) : ⁅ρ.Jz, ρ.Jp⁆ = ρ.Jp
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_z_m`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L87).

```lean
lemma comm_z_m (ρ : AngularMomentumRepresentation V) : ⁅ρ.Jz, ρ.Jm⁆ = -ρ.Jm
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.comm_p_m`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L93).

```lean
lemma comm_p_m (ρ : AngularMomentumRepresentation V) :
    ⁅ρ.Jp, ρ.Jm⁆ = (2 : ℂ) • ρ.Jz
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.isSl2Triple`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L117).

> Angular momentum generates an `sl₂`-triple, via
> `h := 2 • Jz`, `e := J+`, `f := J-` (the doubling of `Jz` reconciles the physicists'
> normalization `[Jz,J±]=±J±` with the `sl₂`-triple normalization `[h,e]=2e`).
>
> The hypothesis `ρ.Jz ≠ 0` is necessary: the all-zero representation
> (`Jx = Jy = Jz = 0`) satisfies every field of `AngularMomentumRepresentation`
> but gives `h = 2 • Jz = 0`, which `IsSl2Triple` explicitly excludes
> (`h_ne_zero`) — the trivial, spin-`0` representation does not generate an
> honest copy of `sl₂` inside `End(V)`.

```lean
lemma isSl2Triple (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    IsSl2Triple ((2 : ℂ) • ρ.Jz) ρ.Jp ρ.Jm
```

### A.1. Spin classification

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.IsIrreducible`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L134).

> Irreducibility of an angular momentum representation: no proper subspace is
> invariant under `Jx`, `Jy`, and `Jz` simultaneously.

```lean
def IsIrreducible (ρ : AngularMomentumRepresentation V) : Prop
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jx_mem_sl2`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L143).

> Irreducibility transfers along the bridge:
> `ρ.IsIrreducible` agrees with irreducibility of the induced module for the `sl₂`-subalgebra
> generated by `(2Jz, J+, J-)` (via the automatic `LieSubalgebra.lieRingModule`/`lieModule`
> instances restricting the tautological `Module.End ℂ V`-action on `V`).

```lean
lemma Jx_mem_sl2 (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    ρ.Jx ∈ (ρ.isSl2Triple hz).toLieSubalgebra ℂ
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jy_mem_sl2`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L148).

```lean
lemma Jy_mem_sl2 (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    ρ.Jy ∈ (ρ.isSl2Triple hz).toLieSubalgebra ℂ
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jz_mem_sl2`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L161).

```lean
lemma Jz_mem_sl2 (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    ρ.Jz ∈ (ρ.isSl2Triple hz).toLieSubalgebra ℂ
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jp_mem_of_invariant`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L167).

```lean
lemma Jp_mem_of_invariant (ρ : AngularMomentumRepresentation V)
    (W : Submodule ℂ V) (hx : ∀ v ∈ W, ρ.Jx v ∈ W)
    (hy : ∀ v ∈ W, ρ.Jy v ∈ W) {v : V} (hv : v ∈ W) : ρ.Jp v ∈ W
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jm_mem_of_invariant`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L173).

```lean
lemma Jm_mem_of_invariant (ρ : AngularMomentumRepresentation V)
    (W : Submodule ℂ V) (hx : ∀ v ∈ W, ρ.Jx v ∈ W)
    (hy : ∀ v ∈ W, ρ.Jy v ∈ W) {v : V} (hv : v ∈ W) : ρ.Jm v ∈ W
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.sl2_invariant_of_angular_invariant`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L179).

```lean
lemma sl2_invariant_of_angular_invariant (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz ≠ 0) (W : Submodule ℂ V)
    (hx : ∀ v ∈ W, ρ.Jx v ∈ W) (hy : ∀ v ∈ W, ρ.Jy v ∈ W)
    (hzW : ∀ v ∈ W, ρ.Jz v ∈ W) {x : ↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ)}
    {v : V} (hv : v ∈ W) : ⁅x, v⁆ ∈ W
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.nontrivial_of_Jz_ne_zero`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L194).

> A nonzero `Jz` forces the representation space to be nontrivial.

```lean
lemma nontrivial_of_Jz_ne_zero (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    Nontrivial V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.lieSubmodule_stable`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L201).

> Lie submodules are stable under every operator in the generated subalgebra.

```lean
lemma lieSubmodule_stable (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0)
    (N : LieSubmodule ℂ ↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ) V) {x : Module.End ℂ V}
    (hx : x ∈ (ρ.isSl2Triple hz).toLieSubalgebra ℂ) : ∀ v ∈ (N : Submodule ℂ V), x v ∈ N
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.angular_irreducible_implies_sl2`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L208).

```lean
lemma angular_irreducible_implies_sl2 (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz ≠ 0) (hirr : ρ.IsIrreducible) :
    LieModule.IsIrreducible ℂ ↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ) V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.sl2_irreducible_implies_angular`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L219).

```lean
lemma sl2_irreducible_implies_angular (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz ≠ 0)
    (hirr : LieModule.IsIrreducible ℂ ↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ) V) :
    ρ.IsIrreducible
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.isIrreducible_iff`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L234).

> Invariance under `Jx`, `Jy`, `Jz` is equivalent to irreducibility for the generated
> `sl₂` Lie subalgebra.

```lean
lemma isIrreducible_iff (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) :
    ρ.IsIrreducible ↔ LieModule.IsIrreducible ℂ (↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ)) V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.spin_classification`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L242).

> A finite-dimensional irreducible angular momentum representation is isomorphic to a
> standard `sl₂` module for the subalgebra generated by `(2Jz, Jp, Jm)`.

```lean
lemma spin_classification [FiniteDimensional ℂ V] (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz ≠ 0) (hirr : ρ.IsIrreducible) :
    ∃ n : ℕ, letI := standardSl2ModuleLieRingModule (K := ℂ) (n := n) (ρ.isSl2Triple hz)
      Nonempty (V ≃ₗ⁅ℂ, ↥((ρ.isSl2Triple hz).toLieSubalgebra ℂ)⁆ StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jp_mul_Jm`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L254).

> `J+J- = Jx²+Jy²+Jz`: the standard ladder-operator identity, a purely algebraic
> consequence of the commutation relations (no representation theory needed). Used to
> reduce `Jsq_eq_smul` to a statement about `Jp * Jm`, via
> `J² = Jp*Jm + Jz*Jz - Jz` (equivalently `Jm*Jp + Jz*Jz + Jz`).

```lean
lemma Jp_mul_Jm (ρ : AngularMomentumRepresentation V) :
    ρ.Jp * ρ.Jm = ρ.Jx * ρ.Jx + ρ.Jy * ρ.Jy + ρ.Jz
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_eq_Jp_mul_Jm`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L270).

> `J² = J+J- + Jz² - Jz`: a purely algebraic consequence of the commutation
> relations (no representation theory needed), used to reduce `Jsq_eq_smul` to a
> statement about the ladder operators.

```lean
lemma Jsq_eq_Jp_mul_Jm (ρ : AngularMomentumRepresentation V) :
    ρ.Jx * ρ.Jx + ρ.Jy * ρ.Jy + ρ.Jz * ρ.Jz =
      ρ.Jp * ρ.Jm + ρ.Jz * ρ.Jz - ρ.Jz
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.leibniz_end`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L277).

> Product Leibniz rule for the associative-ring bracket on `Module.End ℂ V`:
> `⁅a*x, z⁆ = a*⁅x,z⁆ + ⁅a,z⁆*x`.

```lean
lemma leibniz_end (a x z : Module.End ℂ V) :
    (⁅a * x, z⁆ : Module.End ℂ V) = a * ⁅x, z⁆ + ⁅a, z⁆ * x
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.mul_eq_of_lie_eq`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L283).

> Unfolds the associative-ring bracket relation `⁅a, b⁆ = c` into `a * b = b * a + c`.

```lean
lemma mul_eq_of_lie_eq {a b c : Module.End ℂ V} (h : (⁅a, b⁆ : Module.End ℂ V) = c) :
    a * b = b * a + c
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_comm_p`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L290).

> `J²` commutes with `J+`: a step towards showing `J²` is central, hence (on an
> irreducible module) acts as a scalar.

```lean
lemma Jsq_comm_p (ρ : AngularMomentumRepresentation V) :
    (⁅ρ.Jx * ρ.Jx + ρ.Jy * ρ.Jy + ρ.Jz * ρ.Jz, ρ.Jp⁆ : Module.End ℂ V) = 0
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_comm_m`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L302).

> `J²` commutes with `J-`: a step towards showing `J²` is central, hence (on an
> irreducible module) acts as a scalar.

```lean
lemma Jsq_comm_m (ρ : AngularMomentumRepresentation V) :
    (⁅ρ.Jx * ρ.Jx + ρ.Jy * ρ.Jy + ρ.Jz * ρ.Jz, ρ.Jm⁆ : Module.End ℂ V) = 0
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_comm_z`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L314).

> `J²` commutes with `Jz`: derived from `Jsq_comm_p`/`Jsq_comm_m` via the Jacobi
> identity, since `2•Jz = ⁅Jp,Jm⁆`.

```lean
lemma Jsq_comm_z (ρ : AngularMomentumRepresentation V) :
    (⁅ρ.Jx * ρ.Jx + ρ.Jy * ρ.Jy + ρ.Jz * ρ.Jz, ρ.Jz⁆ : Module.End ℂ V) = 0
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq`**, a def, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L322).

> The quadratic angular momentum operator `Jx² + Jy² + Jz²`.

```lean
def Jsq (ρ : AngularMomentumRepresentation V) : Module.End ℂ V
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.JpJm_on_primitive`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L326).

> On a primitive vector of weight `n`, `Jp Jm` acts by `n`.

```lean
lemma JpJm_on_primitive (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0)
    {n : ℕ} {v : V} (P : (ρ.isSl2Triple hz).HasPrimitiveVectorWith v (n : ℂ)) :
    ρ.Jp (ρ.Jm v) = (n : ℂ) • v
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jz_on_primitive`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L340).

> The Cartan operator acts by half the highest weight on a primitive vector.

```lean
lemma Jz_on_primitive (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0)
    {n : ℕ} {v : V} (P : (ρ.isSl2Triple hz).HasPrimitiveVectorWith v (n : ℂ)) :
    ρ.Jz v = ((n : ℂ) / 2) • v
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_on_primitive`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L350).

> The quadratic operator has the expected eigenvalue on a primitive vector.

```lean
lemma Jsq_on_primitive (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0)
    {n : ℕ} {v : V} (P : (ρ.isSl2Triple hz).HasPrimitiveVectorWith v (n : ℂ)) :
    ρ.Jsq v = ((n : ℂ) / 2 * ((n : ℂ) / 2 + 1)) • v
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.ker_scalar_stable`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L363).

> An eigenspace of an endomorphism is stable under commuting endomorphisms.

```lean
lemma ker_scalar_stable (C A : Module.End ℂ V) (c : ℂ)
    (hCA : (⁅C, A⁆ : Module.End ℂ V) = 0)
    {v : V} (hv : v ∈ LinearMap.ker (C - c • (1 : Module.End ℂ V))) :
    A v ∈ LinearMap.ker (C - c • (1 : Module.End ℂ V))
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jx_apply_eq`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L379).

> `Jx` is half the sum of the ladder operators.

```lean
lemma Jx_apply_eq (ρ : AngularMomentumRepresentation V) (v : V) :
    ρ.Jx v = ((1 : ℂ) / 2) • (ρ.Jp v + ρ.Jm v)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jy_apply_eq`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L385).

> `Jy` is `-i/2` times the difference of the ladder operators.

```lean
lemma Jy_apply_eq (ρ : AngularMomentumRepresentation V) (v : V) :
    ρ.Jy v = (-(Complex.I / 2)) • (ρ.Jp v - ρ.Jm v)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_ker_stable_x`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L397).

> The `J²` eigenspace is stable under `Jx`.

```lean
lemma Jsq_ker_stable_x (ρ : AngularMomentumRepresentation V) (c : ℂ)
    {v : V} (hv : v ∈ LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V))) :
    ρ.Jx v ∈ LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V))
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_ker_stable_y`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L406).

> The `J²` eigenspace is stable under `Jy`.

```lean
lemma Jsq_ker_stable_y (ρ : AngularMomentumRepresentation V) (c : ℂ)
    {v : V} (hv : v ∈ LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V))) :
    ρ.Jy v ∈ LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V))
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_ker_eq_top`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L415).

> A nonzero vector in a `J²` eigenspace forces that eigenspace to be everything.

```lean
lemma Jsq_ker_eq_top (ρ : AngularMomentumRepresentation V)
    (hirr : ρ.IsIrreducible) (c : ℂ) {v : V} (hv : v ≠ 0)
    (hmem : v ∈ LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V))) :
    LinearMap.ker (ρ.Jsq - c • (1 : Module.End ℂ V)) = ⊤
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_eq_scalar_of_eigenvector`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L425).

> A nonzero `J²` eigenvector forces `J²` to be that scalar on an irreducible module.

```lean
lemma Jsq_eq_scalar_of_eigenvector (ρ : AngularMomentumRepresentation V)
    (hirr : ρ.IsIrreducible) (c : ℂ) {v : V} (hv : v ≠ 0)
    (hCv : ρ.Jsq v = c • v) : ρ.Jsq = c • (1 : Module.End ℂ V)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_eq_zero_of_Jz_eq_zero`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L434).

> If `Jz = 0`, the commutation relations force all three angular momentum operators
> to vanish.

```lean
lemma Jsq_eq_zero_of_Jz_eq_zero (ρ : AngularMomentumRepresentation V)
    (hz : ρ.Jz = 0) : ρ.Jsq = 0
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.Jsq_eq_smul`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L448).

> On an irreducible finite-dimensional representation, `J²` acts by `j(j+1)` for
> some `j = n/2`.

```lean
lemma Jsq_eq_smul [FiniteDimensional ℂ V] (ρ : AngularMomentumRepresentation V)
    (hirr : ρ.IsIrreducible) :
    ∃ n : ℕ, ρ.Jsq = ((n : ℂ) / 2 * ((n : ℂ) / 2 + 1)) • (1 : Module.End ℂ V)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.magneticBasisVec`**, a def, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean#L462).

> Magnetic-weight ladder vectors: given a primitive vector
> `v₀` of weight `n` for the triple `(2Jz, J+, J-)`, this defines `(J-)ᵏ v₀` for
> `k = 0,…,n`. …

```lean
def magneticBasisVec (ρ : AngularMomentumRepresentation V) (hz : ρ.Jz ≠ 0) {n : ℕ} {v₀ : V}
    (_ : (ρ.isSl2Triple hz).HasPrimitiveVectorWith v₀ (n : ℂ)) (k : Fin (n + 1)) : V
```

## Depends on

- [The standard sl₂ Lie module](../../mathematics/part-02/representationtheory/sl2-basic.md)

## Proof depends on

- [Classification of irreducible sl₂ modules](../../mathematics/part-02/representationtheory/sl2-classification.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Basic.lean)
