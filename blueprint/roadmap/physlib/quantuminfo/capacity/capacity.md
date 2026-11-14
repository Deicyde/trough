---
declaration: module
origin: cited
lean: CPTPMap.emulates_self, CPTPMap.emulates_trans, CPTPMap.εApproximates_self, CPTPMap.εApproximates_monotone, CPTPMap.achievesRate_0, CPTPMap.id_achievesRate_log_dim, CPTPMap.zero_le_quantumCapacity, CPTPMap.Emulates
statement: formalized
proof: formalized
---

# Quantum Capacity

The module `QuantumInfo.Capacity.Capacity`, [QuantumInfo/Capacity/Capacity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean): 11 declarations, 11 with a docstring, 7 listed as significant.

## i. Overview

> This file focuses on defining and proving theorems about the quantum capacity, the maximum
> asymptotic rate at which quantum information can be coherently transmitted through a quantum
> channel. The precise definition is not consistent in the literature, see
> `QuantumInfo/Capacity/Capacity_doc.lean` for a note on what has been used and how that was used
> to arrive at the following definition:
>
>  1. A channel A `Emulates` another channel B if there are D and E such that D∘A∘E = B.
>  2. A channel A `εApproximates` channel B (of the same dimensions) if for every state ρ, the
>     fidelity F(A(ρ), B(ρ)) is at least 1-ε.
>  3. A channel A `AchievesRate` R:ℝ if for every ε>0, n copies of A emulates some channel B such
>     that log2(dimout(B))/n ≥ R, and that B is εApproximately the identity.
>  4. The `quantumCapacity` of the channel A is the supremum of the achievable rates, i.e.
>     `sSup { R : ℝ | AchievesRate A R }`.

## ii. Key results

> The most basic facts:
>  * `emulates_self`: Every channel emulates itself.
>  * `emulates_trans`: If A emulates B and B emulates C, then A emulates C. (That is, emulation
>    is an ordering.)
>  * `εApproximates A B ε` is equivalent to the existence of some δ (depending on ε and dims(A))
>    so that |A-B| has diamond norm at most δ, and δ→0 as ε→0.
>  * `achievesRate_0`: Every channel out of a nonempty space achievesRate 0. So, in that case,
>    the set of achievable rates is Nonempty.
>  * If a channel achievesRate R₁, it also achievesRate every R₂ ≤ R₁, i.e. it is an interval
>    extending left towards -∞. Achievable rates are `¬BddBelow`.
>  * `bddAbove_achievesRate`: A channel C : dimX → dimY cannot achievesRate R with
>    `R > log2(min(dimX, dimY))`. Thus, the interval is `BddAbove`.
>
> …

## iv. References

> * Watrous's notes, Chapter 8 of The Theory of Quantum Information. [ref: watrous\_tqi\_ch8]

## A. Basic definitions

**`CPTPMap.Emulates`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L109).

> A channel Λ₁ `Emulates` another channel Λ₂ if there are D and E such that D∘Λ₁∘E = Λ₂.

```lean
def Emulates (Λ₁ : CPTPMap d₁ d₂) (Λ₂ : CPTPMap d₃ d₄) : Prop
```

**`CPTPMap.εApproximates`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L116).

> A channel A `εApproximates` channel B of the same dimensions if for every state ρ, the
> fidelity F(A(ρ), B(ρ)) is at least 1-ε.

```lean
def εApproximates (A B : CPTPMap d₁ d₂) (ε : ℝ) : Prop
```

**`CPTPMap.AchievesRate`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L123).

> A channel A `AchievesRate` R:ℝ if for every ε>0, some n copies of A emulates a channel B such
> that log2(dimout(B))/n ≥ R, and that B εApproximates the identity channel.

```lean
def AchievesRate (A : CPTPMap d₁ d₂) (R : ℝ) : Prop
```

**`CPTPMap.quantumCapacity`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L133).

> The quantum capacity of a channel A: the supremum of all rates R such that
> `A.AchievesRate R`, i.e. the maximum asymptotic rate at which quantum information can be
> coherently transmitted through the channel.

```lean
noncomputable def quantumCapacity (A : CPTPMap d₁ d₂) : ℝ
```

## B. Emulation between channels

**`CPTPMap.emulates_self`**, a theorem, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L147). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every quantum channel emulates itself.

```lean
theorem emulates_self (Λ : CPTPMap d₁ d₂) : Λ.Emulates Λ
```

**`CPTPMap.emulates_trans`**, a theorem, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L152). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a quantum channel A emulates B, and B emulates C, then A emulates C.

```lean
theorem emulates_trans (Λ₁ : CPTPMap d₁ d₂) (Λ₂ : CPTPMap d₃ d₄) (Λ₃ : CPTPMap d₅ d₆)
    (h₁₂ : Λ₁.Emulates Λ₂) (h₂₃ : Λ₂.Emulates Λ₃) : Λ₁.Emulates Λ₃
```

## C. Approximation between channels

**`CPTPMap.εApproximates_self`**, a theorem, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L169). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every quantum channel perfectly approximates itself, that is, `εApproximates` with `ε = 0`.

```lean
theorem εApproximates_self (Λ : CPTPMap d₁ d₂) : Λ.εApproximates Λ 0
```

**`CPTPMap.εApproximates_monotone`**, a theorem, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L173). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a quantum channel A approximates B with ε₀, it also approximates B with all larger ε₁.

```lean
theorem εApproximates_monotone {A B : CPTPMap d₁ d₂} {ε₀ : ℝ} (h : A.εApproximates B ε₀)
    {ε₁ : ℝ} (h₂ : ε₀ ≤ ε₁) : A.εApproximates B ε₁
```

## D. Achievable rates

**`CPTPMap.achievesRate_0`**, a theorem, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L188). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every quantum channel out of a nonempty space achieves at least a rate of zero.

```lean
theorem achievesRate_0 (Λ : CPTPMap d₁ d₂) [Nonempty d₁] : Λ.AchievesRate 0
```

**`CPTPMap.id_achievesRate_log_dim`**, a theorem, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L195). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity channel on D dimensional space achieves a rate of log2(D).

```lean
theorem id_achievesRate_log_dim :
    (id (dIn := d₁)).AchievesRate (Real.logb 2 (Fintype.card d₁))
```

## E. The quantum capacity

**`CPTPMap.zero_le_quantumCapacity`**, a theorem, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean#L250). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Quantum channel capacity is nonnegative for channels out of a nonempty space.

```lean
theorem zero_le_quantumCapacity (Λ : CPTPMap d₁ d₂) [Nonempty d₁] :
    0 ≤ Λ.quantumCapacity
```

## Depends on

- [Completely Positive Trace Preserving maps](../channels/cptp.md)
- [QuantumInfo.States.Mixed.Fidelity](../states/mixed/fidelity.md)

## Sources

- [QuantumInfo/Capacity/Capacity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Capacity/Capacity.lean)
