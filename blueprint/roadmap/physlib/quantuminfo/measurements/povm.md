---
declaration: module
origin: cited
lean: POVM.traceLeft_measurementMap_eq_measure, POVM, POVM.measurementMap, POVM.measurementMap_apply_matrix, POVM.measurementMap_apply_hermitianMat, POVM.measure, POVM.measureDiscard, POVM.measureDiscard_apply
statement: formalized
proof: formalized
---

# Positive Operator-Valued Measures

The module `QuantumInfo.Measurements.POVM`, [QuantumInfo/Measurements/POVM.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean): 10 declarations, 6 with a docstring, 1 listed as significant.

> A Positive Operator-Valued Measures, or POVM, is the most general notion of a quantum "measurement":
> a collection of positive semidefinite (PSD) operators that sum to the identity. These induce a distribution,
> `POVM.measure`, of measurement outcomes; and they induce a CPTP map, `POVM.measurement_map`, which changes the state
> but adds learned information.
>
> Developing this theory is important if one wants to discuss classical information across quantum channels, as POVMs
> are the route to get back to classical information (a `ProbDistribution` of outcomes).
>
> …

**`POVM`**, a structure, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L41).

> A POVM is a (finite) collection of PSD matrices on the same Hilbert space
> that sum to the identity. Here `X` indexes the matrices, and `d` is the space
> dimension.
>
> Applied to an `MState` on that on that space with
> `POVM.measure`, this produces a distribution of outcomes indexed by the same
> type as the collection.
>
> This measurement action can be composed with `MState.of_classical`, in which
> case it is equal to a CPTP map `measurement_map`.

```lean
structure POVM (X : Type*) (d : Type*) [Fintype X] [Fintype d] [DecidableEq d] where
  mats : X → HermitianMat d ℂ
  nonneg : ∀ x, 0 ≤ (mats x)
  normalized : ∑ x, mats x = 1
```

**`POVM.measurementMap`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L52).

> The act of measuring is a quantum channel, that maps a `d`-dimensional quantum
> state to an `d × X`-dimensional quantum-classical state.

```lean
def measurementMap (Λ : POVM X d) : CPTPMap d (d × X)
```

**`POVM.measurementMap_apply_matrix`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L99).

```lean
lemma measurementMap_apply_matrix (Λ : POVM X d) (m : Matrix d d ℂ) :
  Λ.measurementMap.map m =  ∑ x : X,
    ((((Λ.mats x) ^ (1/2:ℝ)).mat * m * ((Λ.mats x)^(1/2:ℝ)).mat) ⊗ₖ Matrix.single x x 1)
```

**`POVM.measurementMap_apply_hermitianMat`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L108).

```lean
lemma measurementMap_apply_hermitianMat (Λ : POVM X d) (m : HermitianMat d ℂ) :
  Λ.measurementMap.toHPMap m = ∑ x : X,
    --TODO: Something like `HermitianMat.single` to make this better
    ((m.conj ((Λ.mats x)^(1/2:ℝ)).mat : HermitianMat d ℂ) ⊗ₖ HermitianMat.diagonal ℂ (fun y ↦ ite (x = y) 1 0))
```

**`POVM.measure`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L122).

> A POVM leads to a distribution of outcomes on any given mixed state ρ.

```lean
def measure (Λ : POVM X d) (ρ : MState d) : ProbDistribution X
```

**`POVM.traceLeft_measurementMap_eq_measure`**, a theorem, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L130). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum-classical `POVM.measurement_map`, gives a marginal on the right equal to `POVM.measure`.

```lean
theorem traceLeft_measurementMap_eq_measure (Λ : POVM X d) (ρ : MState d) :
    (Λ.measurementMap ρ).traceLeft = MState.ofClassical (Λ.measure ρ)
```

**`POVM.measureDiscard`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L157).

> The action of measuring a state with the POVM `Λ`, discarding the resulting state, and keeping
> the mixed state recording the outcome. This resulting state is purely diagonal, as given in
> `POVM.measureDiscard_apply`.

```lean
noncomputable def measureDiscard (Λ : POVM X d) : CPTPMap d X
```

**`POVM.measureDiscard_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L160).

```lean
lemma measureDiscard_apply (Λ : POVM X d) (ρ : MState d) :
    Λ.measureDiscard ρ = MState.ofClassical (Λ.measure ρ)
```

**`POVM.measureForget`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L166).

> The action of measuring a state with the POVM `Λ`, forgetting the measurement outcome, and
> keeping the disturbed state.

```lean
noncomputable def measureForget (Λ : POVM X d) : CPTPMap d d
```

**`POVM.measureForget_eq_kraus`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean#L169).

```lean
lemma measureForget_eq_kraus (Λ : POVM X d) :
    Λ.measureForget = CPTPMap.of_kraus_CPTPMap (fun i ↦ (Λ.mats i) ^ (1/2 : ℝ)) (by
      simpa [-one_div, fun x ↦ HermitianMat.pow_half_mul (Λ.nonneg x), HermitianMat.ext_iff]
        using Λ.normalized
    )
```

## Depends on

- [Completely Positive Trace Preserving maps](../channels/cptp.md)

## Sources

- [QuantumInfo/Measurements/POVM.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Measurements/POVM.lean)
