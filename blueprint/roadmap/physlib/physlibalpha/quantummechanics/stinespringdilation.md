---
declaration: module
origin: cited
lean: stinespringOp_apply, complCard, Ud_orthonormal₁, Ud_orthonormal₂, unitary_of_orthonormal, tracefree_version, heisenberg_schrõdinger, unitaryForm_of_general
statement: formalized
proof: formalized
---

# Stinespring dilation

The module `PhyslibAlpha.QuantumMechanics.StinespringDilation`, [PhyslibAlpha/QuantumMechanics/StinespringDilation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean): 56 declarations, 55 with a docstring, 11 listed as significant.

> Kraus maps, the Stinespring isometry and unitary dilation, and completion of Kraus families.

## i. Overview

> Completely positive maps on matrices over an `RCLike` field, given by a Kraus family `K`, act as
> `krausApply K ρ = ∑ i, K i * ρ * (K i)ᴴ`. The Stinespring operator `stinespringOp K` (often `V`)
> stacks the Kraus operators into one matrix, and the Kraus map is recovered as the partial trace of
> `V ρ Vᴴ`. For a trace-preserving family `V` is an isometry; its columns are extended to an
> orthonormal basis to build a unitary dilation `Ud`, which acts on `ρ` tensored with an ancilla
> state. A trace non-increasing family is completed to a trace-preserving one by adding one extra
> Kraus operator.
>
> …

## ii. Key results

> - `krausApply` : the completely positive map of a Kraus family.
> - `IsKrausChannel`, `QuantumOperation` : trace-preserving and trace non-increasing Kraus families.
> - `densityMatrix` : density matrices.
> - `tr₂` : the partial trace over the second factor.
> - `stinespringOp` : the Stinespring isometry `V`.
> - `stinespringForm_CPTP_isometry` : `V` is an isometry for a trace-preserving family.
> - `Ud`, `Ud_unitary` : the unitary dilation, and its unitarity.
> - `stinespringGeneralForm_works`, `stinespringUnitaryForm_works` : the dilation forms reproduce
>   `krausApply K`.
> - `krausCompletion`, `krausCompletion_isometry_of_TNI` : the completion of a trace non-increasing
>   family, and its isometry property.
> - `CPTP_of_CPTNI` : every quantum operation extends to a quantum channel.
> - `stinespringForm_eq` : a version of the Stinespring dilation theorem,
>   `tr₂ (stinespringDilation K ρ) = krausApply K ρ`.

## iv. References

> * None.

## A. Kraus maps and density matrices

**`krausApply`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L82).

> Completely positive map given by a (not necessarily minimal) Kraus family.

```lean
def krausApply {R : Type*} [Mul R] [Star R] [AddCommMonoid R]
    {q r : Type*} [Fintype q] [Fintype r]
    (K : r → Matrix q q R) (ρ : Matrix q q R) : Matrix q q R
```

**`krausApply.posSemidef`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L88).

> Kraus operator preserves PSD property.

```lean
lemma krausApply.posSemidef {R : Type*} [Ring R] [PartialOrder R] [StarRing R]
    [AddLeftMono R]
    {q r : Type*} [Fintype q] [Fintype r]
    (K : r → Matrix q q R)
    {ρ : Matrix q q R} (hρ : ρ.PosSemidef) :
    (krausApply K ρ).PosSemidef
```

**`IsKrausChannel`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L97).

> A Kraus family defines a quantum channel: its Kraus operators satisfy `∑ Kᵢᴴ Kᵢ = 1`.

```lean
def IsKrausChannel {R : Type*} [Mul R] [One R] [Star R] [AddCommMonoid R]
    {q r : Type*} [Fintype q] [Fintype r] [DecidableEq q]
    (K : r → Matrix q q R)
```

**`QuantumOperation`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L103).

> Quantum operation.

```lean
def QuantumOperation {R : Type*} [RCLike R]
    {q r : Type*} [Fintype q] [Fintype r] [DecidableEq q]
    (K : r → Matrix q q R)
```

**`densityMatrix`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L108).

> Density matrix.

```lean
def densityMatrix {R : Type*} [Ring R] [PartialOrder R] [StarRing R] (d : Type*) [Fintype d]
```

**`densityMatrix.convexComb`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L112).

> Density matrices are closed under real convex combinations.

```lean
def densityMatrix.convexComb {R : Type*} [RCLike R]
    {d : ℕ} (ρ₀ ρ₁ : densityMatrix (Fin d) (R := R)) {t : R}
    (hp₀ : 0 ≤ t) (hp₁ : 0 ≤ 1 - t) : densityMatrix (Fin d) (R := R)
```

## B. The Stinespring isometry

**`tr₂`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L128).

> Also known as `partialTraceRight`.

```lean
def tr₂ {R : Type*} [Ring R] {m n m' : Type*} [Fintype n]
    (ρ : Matrix (m × n) (m' × n) R) : Matrix m m' R
```

**`stinespringOp`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L133).

> `stinespringOp` is often written as `V`.

```lean
def stinespringOp {R : Type*} [Ring R]
    {m r : Type*} [Fintype r] [DecidableEq r]
  (K : r → Matrix m m R) : Matrix (m × r) m R
```

**`stinespringOp_apply`**, a theorem, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L141). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Entrywise formula for the Stinespring isometry: its `((x₁, x₂), y)` entry is `K x₂ x₁ y`.

```lean
theorem stinespringOp_apply {R : Type*} [Ring R] {m r : Type*} [Fintype r] [DecidableEq r]
    (K : r → Matrix m m R) (x : m × r) (y : m) :
    stinespringOp K x y = K x.2 x.1 y
```

**`stinespringDilation`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L148).

> The Stinespring dilation.

```lean
def stinespringDilation {R : Type*} [Ring R] [StarRing R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (K : r → Matrix m m R)
    (ρ : Matrix m m R)
```

**`stinespringForm`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L156).

> The partial trace of the Stinespring dilation.

```lean
def stinespringForm {R : Type*} [Ring R] [StarRing R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (K : r → Matrix m m R)
```

**`stinespringOp_adjoint_mul_self`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L162).

> A useful identity for Stinespring dilations.

```lean
lemma stinespringOp_adjoint_mul_self {R : Type*} [Ring R] [StarRing R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (K : r → Matrix m m R) :
    ∑ i, star K i * K i = (stinespringOp K)ᴴ * stinespringOp K
```

**`stinespringForm_CPTNI`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L176).

> A useful identity for completely positive, trace non-increasing maps.

```lean
lemma stinespringForm_CPTNI {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m] [DecidableEq m]
    (K : r → Matrix m m R)
  (hK : ∑ i, (K i)ᴴ * K i ≤ 1) :
  (stinespringOp K)ᴴ * (stinespringOp K) ≤ 1
```

**`stinespringForm_CPTP_isometry`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L187).

> The Stinespring operator of a completely positive, trace-preserving maps
> is an isometry. (Note that `stinespringOp K` is not a square matrix in general.)

```lean
lemma stinespringForm_CPTP_isometry {R : Type*} [Ring R] [StarRing R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m] [DecidableEq m]
  {K : r → Matrix m m R}
  (hK : ∑ i, (K i)ᴴ * K i = 1) :
  (stinespringOp K)ᴴ * (stinespringOp K) = 1
```

**`stinespringOrtho`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L199).

> Proving the columns of `V = stinespringOp K` are independent is a step
> on the way to constructing the unitary dilation.

```lean
lemma stinespringOrtho {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m] [DecidableEq m]
    {K : r → Matrix m m R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) :
  Orthonormal (𝕜 := R)
      fun j : m => WithLp.toLp 2 fun i : m × r => stinespringOp K i j
```

## C. Extending the Stinespring columns to an orthonormal basis

**`basisCard`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L240).

> `m` will of course be finite and bounded by `n` here,
> but no need to assume or prove that.

```lean
lemma basisCard {R : Type*} [RCLike R] {n m : Type*} [Fintype n] {s : Matrix n m R}
    (ho : Orthonormal R fun j ↦ WithLp.toLp 2 fun i ↦ s i j) :
    Fintype.card n =
    ho.toSubtypeRange.exists_orthonormalBasis_extension.choose.card
```

**`stinespringCard`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L251).

> Calculating the cardinality of the orthonormal basis obtained by
> extending the Stinespring orthonormal set, the columns of `stinespringOp K`.

```lean
lemma stinespringCard {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m] [DecidableEq m]
    {K : r → Matrix m m R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) :
    Fintype.card (m × r) = (stinespringOrtho
    hK).toSubtypeRange.exists_orthonormalBasis_extension.choose.card
```

**`complCard`**, a theorem, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L267). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> We need the 1 matrix, which we don't seem to have for an arbitrary
> `[Fintype m]`.
> Since we are comparing `Fin r` and `Fin (r-1)` we also cannot too
> easily use an arbitrary `[Fintype r] [Zero r]`.

```lean
theorem complCard {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    let 𝓞 := fun j ↦ WithLp.toLp 2 fun i ↦ stinespringOp K i j;
    let theRange := Submodule.span R (Set.range 𝓞);
    let u' := (exists_orthonormalBasis R theRangeᗮ).choose;
      Fintype.card (Fin m × Fin (r-1)) = #u'
```

**`Fin.predAboveOfNe`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L318).

> See discussion at https://leanprover.zulipchat.com/#narrow/channel/217875-Is-there-code-for-X.3F/topic/succAbove.20and.20predAbove.20lemmas/with/584270574

```lean
def Fin.predAboveOfNe {n : ℕ} {k i : Fin n}
    (h : i ≠ k) : Fin (n - 1)
```

**`Fin.predAboveOfNe_injective`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L325).

> A "missing lemma" for `Fin` types.

```lean
lemma Fin.predAboveOfNe_injective (n : ℕ) (k x y : Fin n)
    (hx : x ≠ k) (hy : y ≠ k)
    (heq : Fin.predAboveOfNe hx = Fin.predAboveOfNe hy) : x = y
```

**`onbPart`**, a def, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L338).

> The way this is written, `Fin r` and `Fin (r-1)` both occur
> so it is tricky to go to a general `Fintype`.

```lean
def onbPart {R : Type*} [RCLike R]
    {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
  (hK : ∑ i, (K i)ᴴ * K i = 1) (x : Fin m × Fin r) {z : Fin r} (hx : ¬x.2 = z) :
  -- if we make it `r+2` then the `x.2≠0` becomes unused.
  Fin m × Fin r → R
```

**`onbPart_inner`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L354).

```lean
lemma onbPart_inner {R : Type*} [RCLike R] {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) {z : Fin r}
    {y : Fin m × Fin r} (hy : ¬y.2 = z)
    {x : Fin m × Fin r} (hx : ¬x.2 = z)
    (h : y ≠ x) :
    inner R (WithLp.toLp 2 <| onbPart hK y hy)
            (WithLp.toLp 2 <| onbPart hK x hx) = 0
```

**`onbPart_norm`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L395).

> The vectors in the Stinespring orthonormal basis have norm 1.

```lean
lemma onbPart_norm {R : Type*} [RCLike R] {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (x : Fin m × Fin r)
    {z : Fin r} (hx : ¬x.2 = z) :
    ‖WithLp.toLp 2 <| onbPart hK x hx‖ = 1
```

## D. The unitary dilation

**`Ud`**, a def, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L412).

> Also known as `unitaryDilation`. Respects x,y order.

```lean
def Ud {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    Matrix (Fin m × Fin r) (Fin m × Fin r) R
```

**`generalDilation`**, a def, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L424).

> This generalization of Stinespring dilation has the right
> "shape" but otherwise nothing specific to it.

```lean
def generalDilation {R : Type*}
    {m r : Type*} [DecidableEq r]
    (z : r)
    (S : Matrix (m × r) m R)
    (M : Matrix (m × r) (m × r) R) :
    Matrix (m × r) (m × r) R
```

**`dilation`**, a def, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L434).

> A general, not necessarily unitary, dilation.

```lean
def dilation {R : Type*} [Ring R]
    {m r : Type*} [Fintype r] [DecidableEq r]
    (K : r → Matrix m m R) (z : r) (M : Matrix (m × r) (m × r) R) :
    Matrix (m × r) (m × r) R
```

**`Ud_orthonormal₁`**, a theorem, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L442). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> One version of orthonormality of `stinespringOp`.

```lean
theorem Ud_orthonormal₁ {R : Type*} [RCLike R] {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    Orthonormal R fun y ↦ if hy : y.2 = z then WithLp.toLp 2 fun i ↦ stinespringOp K i y.1
    else WithLp.toLp 2 fun i ↦ onbPart hK y hy i
```

**`Ud_orthonormal₂`**, a theorem, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L489). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Stinespring dilation columns form an orthonormal basis.

```lean
theorem Ud_orthonormal₂ {R : Type*} [RCLike R]
    {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
  (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    Orthonormal R fun y ↦
      WithLp.toLp 2 fun i ↦ if hy : y.2 = z then stinespringOp K i y.1 else onbPart hK y hy i
```

**`smul_self_one_of_norm_one`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L510).

> If `β` has length 1 then the dot product of `β` with itself is 1.

```lean
lemma smul_self_one_of_norm_one {R : Type*} [RCLike R]
    {t : Type*} [Fintype t] {β : t → R} (hj : ‖WithLp.toLp 2 β‖ = 1) :
  ∑ x, (starRingEnd R) (β x) * β x = 1
```

**`unitary_of_orthonormal`**, a theorem, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L527). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A matrix whose columns are orthonormal is unitary.

```lean
theorem unitary_of_orthonormal {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m] [DecidableEq m]
    (α : Matrix (m × r) (m × r) R)
  (h₀ : Orthonormal R fun i ↦ WithLp.toLp 2 (α i)) : α * star α = 1
```

**`Ud_unitaryT`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L549).

> The transpose of the unitary dilation is unitary.

```lean
lemma Ud_unitaryT {R : Type*} [RCLike R]
    {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    (Ud hK z)ᵀ ∈ unitary _
```

**`Ud_unitary`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L561).

> The unitary dilation `Ud` is in fact unitary.

```lean
lemma Ud_unitary {R : Type*} [RCLike R]
    {m r : ℕ} {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    (Ud hK z) ∈ unitary _
```

## E. Stinespring forms

**`tr₂_e₀Xe₀`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L589).

> Taking the partial trace of a tensor product with a matrix of trace 1 is the
> identity map.

```lean
lemma tr₂_e₀Xe₀ {R : Type*} [RCLike R]
    {m w : Type*} [Fintype w]
    (e : Matrix w w R) (htr : e.trace = 1)
    (ρ : Matrix m m R) :
    tr₂ (ρ ⊗ₖ e) = ρ
```

**`stinespringUnitaryForm`**, a def, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L606).

> The Stinespring unitary form.

```lean
def stinespringUnitaryForm {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r)
    (ρ : Matrix (Fin m) (Fin m) R) :
    (Matrix (Fin m) (Fin m) R)
```

**`stinespringUnitaryFormE`**, a def, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L615).

> The Stinespring unitary form, general version.

```lean
def stinespringUnitaryFormE {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) (e : Matrix (Fin r) (Fin r) R)
    (ρ : Matrix (Fin m) (Fin m) R) :
    (Matrix (Fin m) (Fin m) R)
```

**`tracefree_version`**, a theorem, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L624). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Trace-free version of the Stinespring Dilation Theorem.

```lean
theorem tracefree_version {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    {K : r → Matrix m m R}
    (ρ : Matrix m m R) :
    let K' := fun i x y => star <| K i y x; let U := (stinespringOp K');
    Uᴴ * (ρ ⊗ₖ (1 : Matrix r r R)) * U = stinespringForm K ρ
```

**`heisenberg_schrõdinger`**, a theorem, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L641). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A Heisberg picture / Schrödinger picture view of the Stinespring dilation.

```lean
theorem heisenberg_schrõdinger {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    {K : r → Matrix m m R}
    (ρ : Matrix m m R) :
  let K' := fun i x y => star <| K i y x
  let U := (stinespringOp K'); let V := stinespringOp K
  let schrõdinger := tr₂ (V * ρ * Vᴴ); -- evolve the state forward: V = V(t), ρ = ρ(0)
  let heisenberg := Uᴴ * (ρ ⊗ₖ (1 : Matrix r r R)) * U;
  -- ρ ⊗ₖ 1 is an "observable"; evolve it backward
    schrõdinger = heisenberg
```

**`generalForm`**, a def, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L656).

> A further generalization of `stinespringGeneralForm`.

```lean
def generalForm {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (z : r)
    (S : Matrix (m × r) m R)
    (M : Matrix (m × r) (m × r) R)
```

**`stinespringGeneralForm`**, a def, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L665).

> General form of the Stinespring dilation.

```lean
def stinespringGeneralForm {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (K : r → Matrix m m R) (z : r)
    (M : Matrix (m × r) (m × r) R)
```

**`stinespringGeneralFormE`**, a def, [line 673](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L673).

> Even more general form of the Stinespring dilation.

```lean
def stinespringGeneralFormE {R : Type*} [RCLike R]
    {m r : Type*} [Fintype r] [DecidableEq r] [Fintype m]
    (K : r → Matrix m m R) (z : r) (e : Matrix r r R)
    (M : Matrix (m × r) (m × r) R)
```

**`unitaryForm_of_general`**, a theorem, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L686). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> When we plug in `M = Ud hK`
> into the general `stinespringGeneralForm`,
> then we do get
> `stinespringUnitaryForm hK`.

```lean
theorem unitaryForm_of_general {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    stinespringGeneralForm K z (Ud hK z) =
    stinespringUnitaryForm hK z
```

**`unitaryForm_of_general_e`**, a theorem, [line 699](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L699). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Stinespring unitary form as a general form applied to the unitary dilation.

```lean
theorem unitaryForm_of_general_e {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) (e : Matrix (Fin r) (Fin r) R) :
    stinespringGeneralFormE K z e (Ud hK z) =
    stinespringUnitaryFormE hK z e
```

**`stinespringGeneralForm_works`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L719).

> Note we don't need any special properties of M,
> and we don't need K to be CPTP.
>
> Uses `Fin` types because of the use of
> `Fin.sum_univ_succAbove` in the proof.

```lean
lemma stinespringGeneralForm_works {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R) (z : Fin r)
    (M : Matrix (Fin m × Fin r) (Fin m × Fin r) R) :
    stinespringGeneralForm K z M = krausApply K
```

**`stinespringUnitaryForm_works`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L745).

> Notice that unitarity is a side property, it is not why
> the Stinespring form works.
>
> Here `z` is the coordinate used for the ancilla.

```lean
lemma stinespringUnitaryForm_works {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r) :
    stinespringUnitaryForm hK z = krausApply K
```

## F. The Kraus completion

**`krausCompletion`**, a def, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L761).

> The "orthogonal" CPTP completion of a CPTNI map.
> `Vtilde` is an alternative name for `krausCompletion`.

```lean
def krausCompletion {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R) :
    Matrix (Fin m × Fin (r+1)) (Fin m) R
```

**`stinespringOp_gram`**, a theorem, [line 768](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L768). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Gram matrix of the Stinespring isometry is `∑ i, (K i)ᴴ * K i`.

```lean
theorem stinespringOp_gram {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R) :
    (stinespringOp K)ᴴ * stinespringOp K = ∑ i, star (K i) * K i
```

**`krausCompletion_isometry_of_TNI`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L785).

> Mar 14, 2026 by Bjørn for 4.27
> June 13, 2026 by Aristotle for 4.31 including
> `stinespringOp_gram` and `stinespringOp_apply`.

```lean
lemma krausCompletion_isometry_of_TNI {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, star K i * K i ≤ 1) :
    (krausCompletion K)ᴴ * krausCompletion K = 1
```

## G. Partial traces and unitary dilations

**`unital`**, a def, [line 842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L842).

> A unital operator.

```lean
def unital {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R)
```

**`subunital`**, a def, [line 846](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L846).

> A subunital operator.

```lean
def subunital {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R)
```

**`partialTrace_tensor`**, a lemma, [line 851](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L851).

> The identity `Tr_B (A ⨂ B) = Tr(B) · A`

```lean
lemma partialTrace_tensor {R : Type*} [RCLike R] {m n : ℕ}
    (A : Matrix (Fin m) (Fin m) R) (B : Matrix (Fin n) (Fin n) R) :
    tr₂ (A ⊗ₖ B) = (trace B) • A
```

**`krausApply_of_tensor`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L864).

> A unitary dilation view of the application of a Kraus operator.

```lean
lemma krausApply_of_tensor {R : Type*} [RCLike R] {m r : ℕ}
    {K : Fin r → Matrix (Fin m) (Fin m) R}
    (hK : ∑ i, (K i)ᴴ * K i = 1) (z : Fin r)
    (ρ α : Matrix (Fin m) (Fin m) R) (β : Matrix (Fin r) (Fin r) R)
    (hβ : β.trace = 1) (h : (Ud hK z) * (ρ ⊗ₖ (single z z 1)) * (Ud hK z)ᴴ = α ⊗ₖ β) :
    krausApply K ρ = α
```

**`trace_tr₂`**, a lemma, [line 879](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L879).

> Trace of partial trace equals trace.

```lean
lemma trace_tr₂ {R : Type*} [RCLike R] {m n : ℕ}
    (ρ : Matrix (Fin m × Fin n) (Fin m × Fin n) R) :
    trace ρ = trace (tr₂ ρ)
```

## H. Completing quantum operations to channels

**`krausCompletionChannelMap`**, a def, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L892).

> The Kraus completion as a map from
> operations to channels.

```lean
def krausCompletionChannelMap {R : Type*} [RCLike R] {q r : ℕ}
    {K : Fin r → Matrix (Fin q) (Fin q) R} (hK : QuantumOperation K) :
    {K : Fin (r+1) → Matrix (Fin q) (Fin q) R | IsKrausChannel K}
```

**`CPTP_of_CPTNI`**, a lemma, [line 906](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L906).

> The "not orthogonal" CPTP completion of a CPTNI map.

```lean
lemma CPTP_of_CPTNI {R : Type*} [RCLike R]
    {q r : ℕ}
    {K : Fin r → Matrix (Fin q) (Fin q) R}
    (hq : QuantumOperation K) :
    ∃ K' : Fin (r+1) → Matrix (Fin q) (Fin q) R,
    IsKrausChannel K' ∧
    ∀ i, ∀ H : i ≠ Fin.last r, K' i = K ⟨i.1, Fin.val_lt_last H⟩
```

## I. The Stinespring dilation theorem

**`partialTraceLeft`**, a def, [line 940](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L940).

> Partial trace on the left of a tensor product.

```lean
def partialTraceLeft {R : Type*} [RCLike R]
    {m n : Type*} [Fintype m]
    (ρ : Matrix (m × n)
                (m × n) R) : Matrix (n) (n) R
```

**`stinespringForm_eq`**, a theorem, [line 947](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean#L947). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A version of the Stinespring Dilation Theorem.

```lean
theorem stinespringForm_eq {R : Type*} [RCLike R] {m r : ℕ}
    (K : Fin r → Matrix (Fin m) (Fin m) R)
    (ρ : Matrix (Fin m) (Fin m) R) :
    tr₂ (stinespringDilation K ρ) = krausApply K ρ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/QuantumMechanics/StinespringDilation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/StinespringDilation.lean)
