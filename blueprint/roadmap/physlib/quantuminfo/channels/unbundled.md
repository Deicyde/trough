---
declaration: module
origin: cited
lean: MatrixMap.IsTracePreserving_iff_trace_choi, MatrixMap.IsTracePreserving.apply_trace, MatrixMap.IsTracePreserving.trace_choi, MatrixMap.IsTracePreserving.comp, MatrixMap.IsTracePreserving.id, MatrixMap.IsTracePreserving.unit_linear, MatrixMap.IsTracePreserving.kron, MatrixMap.IsTracePreserving.piProd
statement: formalized
proof: formalized
---

# Properties of Matrix Maps

The module `QuantumInfo.Channels.Unbundled`, [QuantumInfo/Channels/Unbundled.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean): 62 declarations, 42 with a docstring, 35 listed as significant.

> Building on `MatrixMap`s, this defines the properties: `IsTracePreserving`, `Unital`,
> `IsHermitianPreserving`, `IsPositive` and `IsCompletelyPositive`. They have basic facts
> such as closure under composition, addition, and scaling.
>
> These are the *unbundled* versions, which just state the relevant properties of a given `MatrixMap`.
> The bundled versions are `HPMap`, `UnitalMap`, `TPMap`, `PMap`, and `CPMap` respectively, given
> in Bundled.lean.

**`MatrixMap.IsTracePreserving`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L37).

> A linear matrix map is *trace preserving* if trace of the output equals trace of the input.

```lean
def IsTracePreserving (M : MatrixMap A B R) : Prop
```

**`MatrixMap.IsTracePreserving_iff_trace_choi`**, a theorem, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L42). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A map is trace preserving iff the partial trace of the Choi matrix is the identity.

```lean
theorem IsTracePreserving_iff_trace_choi [DecidableEq A] (M : MatrixMap A B R) : M.IsTracePreserving
    ↔ M.choi_matrix.traceLeft = 1
```

**`MatrixMap.IsTracePreserving.apply_trace`**, a theorem, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L72). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Simp lemma: the trace of the image of a IsTracePreserving map is the same as the original
> trace.

```lean
theorem apply_trace (h : M.IsTracePreserving) (ρ : Matrix A A R)
    : (M ρ).trace = ρ.trace
```

**`MatrixMap.IsTracePreserving.trace_choi`**, a theorem, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L77). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace of a Choi matrix of a TP map is the cardinality of the input space.

```lean
theorem trace_choi [DecidableEq A] (h : M.IsTracePreserving) :
    M.choi_matrix.trace = (Finset.univ (α := A)).card
```

**`MatrixMap.IsTracePreserving.comp`**, a theorem, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L83). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The composition of IsTracePreserving maps is also trace preserving.

```lean
theorem comp (h₁ : M.IsTracePreserving) (h₂ : M₂.IsTracePreserving) :
    IsTracePreserving (M₂ ∘ₗ M)
```

**`MatrixMap.IsTracePreserving.id`**, a theorem, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L90). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity MatrixMap IsTracePreserving.

```lean
theorem id : (id A R).IsTracePreserving
```

**`MatrixMap.IsTracePreserving.unit_linear`**, a theorem, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L95). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Unit linear combinations of IsTracePreserving maps are IsTracePreserving.

```lean
theorem unit_linear {M₁ M₂ : MatrixMap A B R} {x y : R}
    (h₁ : M₁.IsTracePreserving) (h₂ : M₂.IsTracePreserving) (hxy : x + y = 1) :
    (x • M₁ + y • M₂).IsTracePreserving
```

**`MatrixMap.IsTracePreserving.kron`**, a theorem, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L103). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The kronecker product of IsTracePreserving maps is also trace preserving.

```lean
theorem kron {M₁ : MatrixMap A B R} {M₂ : MatrixMap C D R} (h₁ : M₁.IsTracePreserving) (h₂ : M₂.IsTracePreserving) :
    (M₁ ⊗ₖₘ M₂).IsTracePreserving
```

**`MatrixMap.IsTracePreserving.piProd`**, a theorem, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L136). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The `MatrixMap.piProd` product of IsTracePreserving maps is also trace preserving.

```lean
theorem piProd {Λi : ∀ i, MatrixMap (dI i) (dO i) R} (h₁ : ∀ i, (Λi i).IsTracePreserving) :
    (MatrixMap.piProd Λi).IsTracePreserving
```

**`MatrixMap.IsTracePreserving.of_kraus_isTracePreserving`**, a theorem, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L166). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The channel X ↦ ∑ k : κ, (M k) * X * (N k)ᴴ formed by Kraus operators M, N : κ → Matrix B A R
> is trace-preserving if ∑ k : κ, (N k)ᴴ * (M k) = 1

```lean
theorem of_kraus_isTracePreserving
  (M N : κ → Matrix B A S)
  (hTP : (∑ k, (N k).conjTranspose * (M k)) = 1) :
  (MatrixMap.of_kraus M N).IsTracePreserving
```

**`MatrixMap.IsTracePreserving.submatrix`**, a theorem, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L179). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `MatrixMap.submatrix` is trace-preserving when the function is an equivalence.

```lean
theorem submatrix (e : A ≃ B) : (MatrixMap.submatrix R e).IsTracePreserving
```

**`MatrixMap.Unital`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L191).

> A linear matrix map is *unital* if it preserves the identity.

```lean
def Unital (M : MatrixMap A B R) : Prop
```

**`MatrixMap.Unital.map_1`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L201).

```lean
lemma map_1 (h : M.Unital) : M 1 = 1
```

**`MatrixMap.Unital.id`**, a theorem, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L206). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity `MatrixMap` is `Unital`.

```lean
theorem id : (id A R).Unital
```

**`MatrixMap.IsHermitianPreserving`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L223).

> A linear matrix map is *Hermitian preserving* if it maps `IsHermitian` matrices to `IsHermitian`.

```lean
def IsHermitianPreserving (M : MatrixMap A B R) : Prop
```

**`MatrixMap.IsPositive`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L227).

> A linear matrix map is *positive* if it maps `PosSemidef` matrices to `PosSemidef`.

```lean
def IsPositive [Fintype A] [Fintype B] (M : MatrixMap A B R) : Prop
```

**`MatrixMap.IsCompletelyPositive`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L232).

> A linear matrix map is *completely positive* if, for any integer n, the tensor product
> with `I(n)` is positive.

```lean
def IsCompletelyPositive [Fintype A] [Fintype B] [DecidableEq A] (M : MatrixMap A B R) : Prop
```

**`MatrixMap.IsHermitianPreserving.id`**, a theorem, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L239). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity MatrixMap IsHermitianPreserving.

```lean
theorem id : (id A R).IsPositive
```

**`MatrixMap.IsHermitianPreserving.comp`**, a theorem, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L243). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The composition of IsHermitianPreserving maps is also Hermitian preserving.

```lean
theorem comp {M₁ : MatrixMap A B R} {M₂ : MatrixMap B C R}
    (h₁ : M₁.IsHermitianPreserving) (h₂ : M₂.IsHermitianPreserving) : IsHermitianPreserving (M₂ ∘ₗ M₁)
```

**`MatrixMap.IsPositive.IsHermitianPreserving`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L253).

```lean
lemma IsHermitianPreserving {M : MatrixMap A B R}
    (hM : IsPositive M) : IsHermitianPreserving M
```

**`MatrixMap.IsPositive.comp`**, a theorem, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L266). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The composition of IsPositive maps is also positive.

```lean
theorem comp {M₁ : MatrixMap A B R} {M₂ : MatrixMap B C R} (h₁ : M₁.IsPositive)
    (h₂ : M₂.IsPositive) : IsPositive (M₂ ∘ₗ M₁)
```

**`MatrixMap.IsPositive.id`**, a theorem, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L273). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity MatrixMap IsPositive.

```lean
theorem id : (id A R).IsPositive
```

**`MatrixMap.IsPositive.add`**, a theorem, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L277). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Sums of IsPositive maps are IsPositive.

```lean
theorem add {M₁ M₂ : MatrixMap A B R} (h₁ : M₁.IsPositive) (h₂ : M₂.IsPositive) :
    (M₁ + M₂).IsPositive
```

**`MatrixMap.IsPositive.smul`**, a theorem, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L282). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Nonnegative scalings of IsPositive maps are IsPositive.

```lean
theorem smul {M : MatrixMap A B R} (hM : M.IsPositive) {x : R} (hx : 0 ≤ x) :
    (x • M).IsPositive
```

**`MatrixMap.IsCompletelyPositive.of_Fintype`**, a theorem, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L292). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Definition of a CP map, but with `Fintype T` in the definition instead of a `Fin n`.

```lean
theorem of_Fintype  {M : MatrixMap A B R} (h : IsCompletelyPositive M)
    (T : Type*) [Fintype T] [DecidableEq T] :
    (M.kron (LinearMap.id : MatrixMap T T R)).IsPositive
```

**`MatrixMap.IsCompletelyPositive.IsPositive`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L321).

```lean
lemma IsPositive {M : MatrixMap A B R}
    (hM : IsCompletelyPositive M) : IsPositive M
```

**`MatrixMap.IsCompletelyPositive.comp`**, a theorem, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L348). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The composition of IsCompletelyPositive maps is also completely positive.

```lean
theorem comp [DecidableEq B] {M₁ : MatrixMap A B R} {M₂ : MatrixMap B C R} (h₁ : M₁.IsCompletelyPositive)
    (h₂ : M₂.IsCompletelyPositive) : IsCompletelyPositive (M₂ ∘ₗ M₁)
```

**`MatrixMap.IsCompletelyPositive.id`**, a theorem, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L361). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The identity MatrixMap IsCompletelyPositive.

```lean
theorem id : (id A R).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive.add`**, a theorem, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L366). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Sums of IsCompletelyPositive maps are IsCompletelyPositive.

```lean
theorem add {M₁ M₂ : MatrixMap A B R} (h₁ : M₁.IsCompletelyPositive) (h₂ : M₂.IsCompletelyPositive) :
    (M₁ + M₂).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive.smul`**, a theorem, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L373). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Nonnegative scalings of `IsCompletelyPositive` maps are `IsCompletelyPositive`.

```lean
theorem smul {M : MatrixMap A B R} (hM : M.IsCompletelyPositive) {x : R} (hx : 0 ≤ x) :
    (x • M).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive.zero`**, a theorem, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L381). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The zero map `IsCompletelyPositive`.

```lean
theorem zero : (0 : MatrixMap A B R).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive.finset_sum`**, a theorem, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L385). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A finite sum of completely positive maps is completely positive.

```lean
theorem finset_sum {ι : Type*} [Fintype ι] {m : ι → MatrixMap A B R} (hm : ∀ i, (m i).IsCompletelyPositive) :
    (∑ i, m i).IsCompletelyPositive
```

**`MatrixMap.kron_kronecker_const`**, a theorem, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L398). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The map that takes M and returns M ⊗ₖ C, where C is positive semidefinite, is a completely
> positive map.

```lean
theorem kron_kronecker_const {C : Matrix d d R} (h : C.PosSemidef) {h₁ h₂ : _} : IsCompletelyPositive
    (⟨⟨fun M => M ⊗ₖ C, h₁⟩, h₂⟩ : MatrixMap A (A × d) R)
```

**`MatrixMap.choi_of_kraus`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L442).

```lean
lemma choi_of_kraus (K : κ → Matrix B A 𝕜) :
    (MatrixMap.of_kraus K K).choi_matrix = ∑ k, Matrix.vecMulVec (fun (x : B × A) => K k x.1 x.2) (fun (x : B × A) => star (K k x.1 x.2))
```

**`MatrixMap.conj`**, a def, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L457).

> The linear map of conjugating a matrix by another, `x → y * x * yᴴ`.

```lean
def _root_.MatrixMap.conj (y : Matrix B A R) : MatrixMap A B R
```

**`MatrixMap.conj_isPositive`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L463).

```lean
lemma conj_isPositive (M : Matrix B A 𝕜) : (conj M).IsPositive
```

**`MatrixMap.IsPositive_sum`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L467).

```lean
lemma IsPositive_sum {ι : Type*} [Fintype ι] (f : ι → MatrixMap A B ℂ) (h : ∀ i, (f i).IsPositive) :
    (∑ i, f i).IsPositive
```

**`MatrixMap.of_kraus_isPositive`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L483).

```lean
lemma of_kraus_isPositive (K : κ → Matrix B A ℂ) :
    (of_kraus K K).IsPositive
```

**`MatrixMap.conj_kron`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L490).

```lean
lemma conj_kron (M : Matrix B A 𝕜) (N : Matrix D C 𝕜) [DecidableEq C] :
    conj M ⊗ₖₘ conj N = conj (M ⊗ₖ N)
```

**`MatrixMap.congruence_one_eq_id`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L531).

```lean
lemma congruence_one_eq_id : conj (1 : Matrix A A ℂ) = MatrixMap.id A ℂ
```

**`MatrixMap.congruence_CP`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L535).

```lean
lemma congruence_CP {A B : Type*} [Fintype A] [Fintype B] [DecidableEq A] [DecidableEq B] (M : Matrix B A 𝕜) : (conj M).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive_sum`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L544).

```lean
lemma IsCompletelyPositive_sum {ι : Type*} [Fintype ι] (f : ι → MatrixMap A B ℂ) (h : ∀ i, (f i).IsCompletelyPositive) :
    (∑ i, f i).IsCompletelyPositive
```

**`MatrixMap.of_kraus_eq_sum_conj`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L549).

```lean
lemma of_kraus_eq_sum_conj (K : κ → Matrix B A 𝕜) :
    of_kraus K K = ∑ k, conj (K k)
```

**`MatrixMap.of_kraus_CP`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L554).

```lean
lemma of_kraus_CP (K : κ → Matrix B A 𝕜) : (of_kraus K K).IsCompletelyPositive
```

**`MatrixMap.exists_kraus_of_choi_PSD`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L567).

```lean
lemma exists_kraus_of_choi_PSD
    (C : Matrix (B × A) (B × A) 𝕜) (hC : C.PosSemidef) :
    ∃ (K : (B × A) → Matrix B A 𝕜), C = (MatrixMap.of_kraus K K).choi_matrix
```

**`MatrixMap.choi_matrix_eq_map_proj`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L583).

```lean
lemma choi_matrix_eq_map_proj (M : MatrixMap A B R) :
    M.choi_matrix = (M ⊗ₖₘ MatrixMap.id A R) (Matrix.vecMulVec (fun (x : A × A) => if x.1 = x.2 then 1 else 0) (fun (x : A × A) => star (if x.1 = x.2 then 1 else 0)))
```

**`MatrixMap.choi_PSD_iff_CP_map`**, a theorem, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L594). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Choi's theorem on completely positive maps: A map `IsCompletelyPositive` iff its Choi Matrix is PSD.

```lean
theorem choi_PSD_iff_CP_map (M : MatrixMap A B R) :
    M.IsCompletelyPositive ↔ M.choi_matrix.PosSemidef
```

**`MatrixMap.conj_eq_mulRightLinearMap_comp_mulRightLinearMap`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L607).

```lean
lemma conj_eq_mulRightLinearMap_comp_mulRightLinearMap (y : Matrix B A R) :
    conj y = mulRightLinearMap B R y.conjTranspose ∘ₗ mulLeftLinearMap A R y
```

**`MatrixMap.conj_isCompletelyPositive`**, a theorem, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L613). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The act of conjugating (not necessarily by a unitary, just by any matrix at all) is completely positive.

```lean
theorem conj_isCompletelyPositive (M : Matrix B A R) : (conj M).IsCompletelyPositive
```

**`MatrixMap.IsCompletelyPositive.submatrix`**, a theorem, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L668). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `MatrixMap.submatrix` is completely positive

```lean
theorem IsCompletelyPositive.submatrix (f : B → A) : (MatrixMap.submatrix R f).IsCompletelyPositive
```

**`MatrixMap.of_kraus_isCompletelyPositive`**, a theorem, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L675). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The channel X ↦ ∑ k : κ, (M k) * X * (M k)ᴴ formed by Kraus operators M : κ → Matrix B A R
> is completely positive

```lean
theorem of_kraus_isCompletelyPositive (M : κ → Matrix B A R) :
    (of_kraus M M).IsCompletelyPositive
```

**`MatrixMap.choi_of_kraus_R`**, a theorem, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L684). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Choi matrix of a map in symmetric Kraus form is a sum of rank-1 projectors.

```lean
theorem choi_of_kraus_R [DecidableEq A] (K : κ → Matrix B A 𝕜) :
    (of_kraus K K).choi_matrix = ∑ k, Matrix.vecMulVec (fun (x : B × A) => K k x.1 x.2) (fun (x : B × A) => star (K k x.1 x.2))
```

**`MatrixMap.choi_eq_kron_id_apply_choi_id`**, a lemma, [line 706](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L706).

```lean
lemma choi_eq_kron_id_apply_choi_id (M : MatrixMap A B R) :
    M.choi_matrix = (M ⊗ₖₘ MatrixMap.id A R) ((MatrixMap.id A R).choi_matrix)
```

**`MatrixMap.choi_id_is_PSD`**, a lemma, [line 734](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L734).

```lean
lemma choi_id_is_PSD {A R : Type*} [Fintype A] [DecidableEq A] [RCLike R] :
    (MatrixMap.id A R).choi_matrix.PosSemidef
```

**`MatrixMap.is_CP_implies_choi_PSD`**, a lemma, [line 755](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L755).

```lean
lemma is_CP_implies_choi_PSD {A B R : Type*} [Fintype A] [Fintype B] [DecidableEq A] [DecidableEq B] [RCLike R] (M : MatrixMap A B R) (hCP : M.IsCompletelyPositive) :
    M.choi_matrix.PosSemidef
```

**`MatrixMap.IsCompletelyPositive.exists_kraus`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L760).

```lean
lemma IsCompletelyPositive.exists_kraus (Φ : MatrixMap A B R) (hCP : Φ.IsCompletelyPositive) :
    ∃ (M : (B × A) → Matrix B A R), Φ = of_kraus M M
```

**`MatrixMap.cp_subunital_kadison_schwarz`**, a lemma, [line 770](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L770).

> Kadison-Schwarz for completely positive subunital matrix maps.

```lean
lemma cp_subunital_kadison_schwarz {M : MatrixMap A B ℂ} [DecidableEq B]
    (hM : M.IsCompletelyPositive) (hM1 : M 1 ≤ (1 : Matrix B B ℂ))
    (X : Matrix A A ℂ) :
    (M X)ᴴ * M X ≤ M (Xᴴ * X)
```

**`MatrixMap.positive_subunital_norm_apply_le`**, a theorem, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L811). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A positive subunital matrix map is contractive on positive inputs.

```lean
theorem positive_subunital_norm_apply_le {M : MatrixMap A B ℂ} [DecidableEq B]
    (hM : M.IsPositive) (hM1 : M 1 ≤ (1 : Matrix B B ℂ))
    {X : Matrix A A ℂ} (hX : 0 ≤ X) :
    ‖M X‖ ≤ ‖X‖
```

**`MatrixMap.cp_subunital_opNorm_le_one`**, a theorem, [line 848](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L848). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A completely positive subunital matrix map is contractive in operator norm.

```lean
theorem cp_subunital_opNorm_le_one {M : MatrixMap A B ℂ} [DecidableEq B]
    (hM : M.IsCompletelyPositive) (hM1 : M 1 ≤ (1 : Matrix B B ℂ))
    (X : Matrix A A ℂ) :
    ‖M X‖ ≤ ‖X‖
```

**`MatrixMap.kron_of_kraus`**, a theorem, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L863). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kronecker product of two Kraus maps is the Kraus map of the Kronecker products of the operators.

```lean
theorem kron_of_kraus {A B C D R : Type*} [Fintype A] [Fintype B] [Fintype C] [Fintype D]
    [DecidableEq A] [DecidableEq C] [CommSemiring R] [StarRing R] [SMulCommClass R R R]
    {κ ι : Type*} [Fintype κ] [Fintype ι]
    (M : κ → Matrix B A R) (N : ι → Matrix D C R) :
    of_kraus M M ⊗ₖₘ of_kraus N N =
    of_kraus (fun (k : κ × ι) => M k.1 ⊗ₖ N k.2) (fun k => M k.1 ⊗ₖ N k.2)
```

**`MatrixMap.IsCompletelyPositive.kron`**, a theorem, [line 901](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L901). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kronecker product of IsCompletelyPositive maps is also completely positive.

```lean
theorem kron {D : Type*} [DecidableEq C] [Fintype D] {M₁ : MatrixMap A B R} {M₂ : MatrixMap C D R}
    (h₁ : M₁.IsCompletelyPositive) (h₂ : M₂.IsCompletelyPositive) : IsCompletelyPositive (M₁ ⊗ₖₘ M₂)
```

**`MatrixMap.IsCompletelyPositive.piProd`**, a theorem, [line 915](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean#L915). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The `MatrixMap.piProd` product of IsCompletelyPositive maps is also completely positive.

```lean
theorem piProd {Λi : ∀ i, MatrixMap (dI i) (dO i) R} (h₁ : ∀ i, (Λi i).IsCompletelyPositive) :
    IsCompletelyPositive (MatrixMap.piProd Λi)
```

## Depends on

- [Linear maps of matrices](matrixmap.md)

## Sources

- [QuantumInfo/Channels/Unbundled.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Unbundled.lean)
